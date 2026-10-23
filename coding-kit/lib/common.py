"""Shared evidence, coordinate and stage validation for source-only coding."""
import hashlib
import json
import re
from pathlib import Path

STAGES = ("strict", "lenient", "reconcile", "verify", "final")
PRIORS = {"strict": (), "lenient": (), "reconcile": ("strict", "lenient"),
          "verify": ("reconcile",), "final": ("reconcile", "verify")}


def canonical(value):
    return (json.dumps(value, sort_keys=True, ensure_ascii=False, separators=(",", ":")) + "\n").encode()


def sha(data):
    return hashlib.sha256(data).hexdigest()


def read(path):
    return json.loads(Path(path).read_text(encoding="utf-8"))


def write_new(path, value):
    path = Path(path)
    data = canonical(value)
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists():
        if path.read_bytes() != data: raise ValueError(f"Refusing changed overwrite: {path}")
        return
    with path.open("xb") as handle: handle.write(data)


def safe_name(value):
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9_.-]{0,100}", value) or value in {".", ".."}:
        raise ValueError("Unsafe run/model name")
    return value


def contribution_key(row):
    return f"contribution:{row['source_kind']}:{row['source_id'] or 'incident'}:{row['target_id']}"


def feature_objects(coding):
    """Compare meaning-bearing objects by stable identity, never array position."""
    result = {"scope": {"status": coding["scope_status"], "reason": coding["scope_reason"]},
              "primary": {"status": coding["primary_status"], "reason": coding["primary_reason"]},
              "source_quality": coding["source_quality"], "gaps": coding["gaps"],
              "unresolved": coding["unresolved"], "notes": coding["notes"]}
    for field in ("causes", "vectors", "harms", "challenges"):
        for row in coding[field]: result[f"{field}:{row['concept_id']}"] = row
    for row in coding["harm_chains"]: result[f"chain:{row['from_id']}:{row['to_id']}"] = row
    for row in coding["contributions"]: result[contribution_key(row)] = row
    return result


def changed_keys(a, b):
    fa, fb = feature_objects(a), feature_objects(b)
    return {k for k in fa.keys() | fb.keys() if fa.get(k) != fb.get(k)}


def candidates(coding):
    result = {f"challenges:{r['concept_id']}" for r in coding["challenges"] if r["evidence_status"] == "likely"}
    return result | {contribution_key(r) for r in coding["contributions"]}


def verification_targets(coding, registry):
    result = {f"challenges:{r['concept_id']}" for r in coding["challenges"]}
    result |= {f"harms:{r['concept_id']}" for r in coding["harms"]
               if (registry[r['concept_id']]['path'][0] == "Distal" and r["realization_status"] == "realized")
               or r['evidence_basis'] == 'maintainer_presumption'}
    return result | {contribution_key(r) for r in coding["contributions"]}


def validate_evidence(evidence, source):
    reports = {r["report_number"]: r["row"] for r in source["reports"]}
    for entry in evidence:
        row = source["incident"] if entry["report_number"] is None else reports.get(entry["report_number"])
        if row is None: raise ValueError("Evidence names an unlinked report")
        text = row.get(entry["field"], "")
        # Readable source packets add only display wrapping. Whitespace is not substantive evidence.
        norm = lambda x: " ".join(str(x).split())
        if not norm(entry["quote"]) or norm(entry["quote"]) not in norm(text):
            raise ValueError("Evidence quote is absent from its named source field")


def all_evidence(value):
    if isinstance(value, dict):
        for k, v in value.items():
            if k == "evidence": yield v
            else: yield from all_evidence(v)
    elif isinstance(value, list):
        for v in value: yield from all_evidence(v)


def validate_coding(coding, stage, registry):
    field_axes = {"causes": {"Cause"}, "vectors": {"Vector"}, "harms": {"Proximal", "Distal"}, "challenges": {"Challenges"}}
    present = {}
    for field, axes in field_axes.items():
        ids = []
        for row in coding[field]:
            cid = row["concept_id"]
            if cid not in registry or registry[cid]["path"][0] not in axes or len(registry[cid]["path"]) < 2:
                raise ValueError(f"Invalid {field} coordinate: {cid}")
            ids.append(cid)
            if row["evidence_basis"] == "likely_inference" and field != "challenges":
                raise ValueError("Likely inference is confined to eligible Challenges/contributions")
            if row["evidence_basis"] == "maintainer_presumption":
                if field != "harms" or registry[cid]["path"][:len(registry["E174"]["path"])] != registry["E174"]["path"]:
                    raise ValueError("D23 presumption is confined to Proximal Sexual Abuse & Exploitation")
                if row["depiction_provenance"] != "unknown" or row["proximal_basis"] != "maintainer_presumption":
                    raise ValueError("D23 requires unknown provenance and explicit presumption basis")
            elif field == "harms" and row["proximal_basis"] == "maintainer_presumption":
                raise ValueError("Presumption basis and evidence basis disagree")
            if field == "challenges":
                likely = row["evidence_status"] == "likely"
                if likely and any(x in registry[cid]['path'] for x in ('Overreliance', 'Lack of AI Literacy', 'Scalable Oversight Gap')):
                    raise ValueError("D12/D21/H04A require demonstrated human state or supervisory capacity; likelihood alone is insufficient")
                if likely != (row["evidence_basis"] == "likely_inference"):
                    raise ValueError("Challenge evidence status and basis disagree")
                if stage == "strict" and likely: raise ValueError("Strict cannot emit a likely Challenge")
            if field == 'harms' and row['privacy_qualifiers'] and 'Privacy' not in registry[cid]['path']:
                raise ValueError('H02 privacy qualifiers require a Privacy coordinate')
        if len(ids) != len(set(ids)): raise ValueError(f"Duplicate {field} coordinate")
        present[field] = set(ids)
        for cid in ids:
            path = registry[cid]["path"]
            if any(registry[other]["path"][:len(path)] == path for other in ids if other != cid):
                raise ValueError("Do not duplicate an ancestor and descendant for the same coded concept")
    if coding["scope_status"] in {"out_of_scope", "uncertain"}:
        if any(coding[f] for f in (*field_axes, "harm_chains", "contributions", "gaps")):
            raise ValueError("Out-of-scope/uncertain scope retains source/reason with empty code arrays")
        if coding["primary_status"] != "not_applicable": raise ValueError("Scope and primary status disagree")
    else:
        n = sum(r["primary"] for r in coding["causes"])
        if coding["primary_status"] == "resolved" and n != 1: raise ValueError("Resolved primary needs exactly one primary Cause")
        if coding["primary_status"] != "resolved" and n: raise ValueError("Unresolved/unknown primary cannot force a primary Cause")
        if not coding["causes"] and coding["primary_status"] != "unknown": raise ValueError("No supported Cause requires unknown primary")
    edges = {cid: set() for cid in present["harms"]}
    chain_keys = []
    for row in coding["harm_chains"]:
        a, b = row["from_id"], row["to_id"]
        if a not in edges or b not in edges or a == b: raise ValueError("Dangling/self Harm chain")
        if registry[a]["path"][0] != registry[b]["path"][0]: raise ValueError("Harm chains are same-axis; use contribution for Distal-directed pathways")
        edges[a].add(b); chain_keys.append((a, b))
    if len(chain_keys) != len(set(chain_keys)): raise ValueError("Duplicate chain")
    def visit(cid, trail):
        if cid in trail: raise ValueError("Cyclic Harm chain")
        for nxt in edges[cid]: visit(nxt, trail | {cid})
    for cid in edges: visit(cid, set())
    incoming = {b for children in edges.values() for b in children}
    for row in coding["harms"]:
        cid = row["concept_id"]
        expected = "chain_link" if edges[cid] else "terminal" if cid in incoming else "parallel"
        if row["role"] != expected: raise ValueError(f"Harm role does not match explicit chain: {cid}")
    keys = []
    for row in coding["contributions"]:
        target = registry.get(row["target_id"])
        if not target or target["path"][0] != "Distal" or len(target["path"]) < 2: raise ValueError("Contribution target must be a current Distal concept")
        kind, sid = row["source_kind"], row["source_id"]
        if kind == "incident":
            if sid is not None: raise ValueError("Incident contribution source_id must be null")
        elif sid not in present[{"cause": "causes", "vector": "vectors", "harm": "harms"}[kind]]:
            raise ValueError("Contribution source is not coded")
        likely = row["evidence_status"] == "likely"
        if likely and any(x in target['path'] for x in ('Erosion of Trust', 'Erosion of Norms')):
            raise ValueError('D11 generic destinations require the reported societal state in both profiles')
        if likely != (row["evidence_basis"] == "likely_inference"): raise ValueError("Contribution status/basis disagree")
        if stage == "strict" and likely: raise ValueError("Strict cannot emit a likely contribution")
        keys.append(contribution_key(row))
    if len(keys) != len(set(keys)): raise ValueError("Duplicate contribution")
    for gap in coding["gaps"]:
        if gap["nearest_concept_id"] is not None and gap["nearest_concept_id"] not in registry: raise ValueError("Unknown nearest-home ID")


def validate_record(record, job, source, registry, schema, priors):
    import jsonschema
    jsonschema.Draft202012Validator(schema).validate(record)
    allowed_rules=({f'D{i}' for i in range(2,26) if i not in (3,5)} |
                   {f'EXP{i:02}' for i in range(1,11)} | {f'R{i:02}' for i in range(3,9)} |
                   {'M01','M02','H01','H02','H03','H04','H04A','V094-ELECTORAL','V094-CREDENTIALING-CAUSE',
                    'V094-SELF-IMPROVEMENT-CAUSE','V095-AI-WELFARE-SCOPE'} | registry.keys())
    def rule_check(value):
        if isinstance(value,dict):
            for k,v in value.items():
                if k=='rule_ids' and not set(v)<=allowed_rules:raise ValueError('Unknown or inapplicable incident rule reference')
                rule_check(v)
        elif isinstance(value,list):
            for v in value:rule_check(v)
    rule_check(record)
    for key in ("stage", "incident_id", "model_id", "run_id", "job_id", "source_sha256"):
        if record[key] != job[key]: raise ValueError(f"Output identity mismatch: {key}")
    if set(record["source_review"]["reports_read"]) != {r["report_number"] for r in source["reports"]}:
        raise ValueError("source_review must list every linked report")
    for ev in all_evidence(record): validate_evidence(ev, source)
    stage = record["stage"]
    if stage != "verify": validate_coding(record["coding"], stage, registry)
    if stage == "reconcile":
        required = candidates(priors["strict"]["coding"]) | candidates(priors["lenient"]["coding"]) | candidates(record["coding"])
        reviews = record["inference_reviews"]
        keys = [r["candidate_key"] for r in reviews]
        if len(keys) != len(set(keys)) or set(keys) != required: raise ValueError("Reconciliation must review every inferred/contribution candidate exactly once")
        final_features = feature_objects(record["coding"])
        for r in reviews:
            retained = r["candidate_key"] in final_features
            if (r["decision"] == "include") != retained: raise ValueError("Inference review and reconciled output disagree")
            if r["decision"] == "include" and (r["support_assessment"] not in {"supported", "more_likely_than_not"} or not r["evidence"]):
                raise ValueError("Inference inclusion requires positive source-anchored support")
        differences = changed_keys(priors["strict"]["coding"], priors["lenient"]["coding"])
        got = [r["feature_key"] for r in record["differences"]]
        if len(got) != len(set(got)) or set(got) != differences: raise ValueError("Reconciliation must log every strict/lenient object difference")
        for row in record["differences"]:
            key = row["feature_key"]
            if row["strict"] != feature_objects(priors["strict"]["coding"]).get(key) or row["lenient"] != feature_objects(priors["lenient"]["coding"]).get(key):
                raise ValueError("Difference log does not match immutable prior outputs")
    if stage == "verify":
        coding = priors["reconcile"]["coding"]
        required = verification_targets(coding, registry)
        keys = [r["target_key"] for r in record["inference_tests"]]
        if len(keys) != len(set(keys)) or set(keys) != required: raise ValueError("Verifier must test every Challenge, realized Distal harm and contribution exactly once")
        issues = [r["issue_id"] for r in record["issues"]]
        if len(issues) != len(set(issues)): raise ValueError("Duplicate verifier issue ID")
        if (record["verdict"] == "sound") != (not issues): raise ValueError("Verifier verdict and issue list disagree")
        if issues and record['verdict'] != ('major_issues' if any(i['severity']=='major' for i in record['issues']) else 'minor_issues'):
            raise ValueError('Verifier verdict must match highest issue severity')
        features = feature_objects(coding)
        for row in record["inference_tests"]:
            target = features[row["target_key"]]
            expected = "eligible_likelihood" if target.get("evidence_status") == "likely" else "scoped_exception" if target.get("evidence_basis") == "maintainer_presumption" else "source_support"
            if row["burden"] != expected: raise ValueError("Verifier applied the wrong evidence burden")
            if row["verdict"] == "supported" and (row["issue_id"] is not None or not row["evidence"]): raise ValueError("Supported test requires evidence and no adverse issue")
            if row["verdict"] != "supported" and row["issue_id"] not in issues: raise ValueError("Adverse/uncertain test must point to a verifier issue")
    if stage == "final":
        issues = {r["issue_id"]: r for r in priors["verify"]["issues"]}
        dispositions = record["issue_dispositions"]
        ids = [r["issue_id"] for r in dispositions]
        if len(ids) != len(set(ids)) or set(ids) != set(issues): raise ValueError("Dispose every verifier issue exactly once")
        changes = record["changes"]
        got = [r["feature_key"] for r in changes]
        required = changed_keys(priors["reconcile"]["coding"], record["coding"])
        if len(got) != len(set(got)) or set(got) != required: raise ValueError("Final must log every changed object, including confidence and rationale changes")
        decisions = {r["issue_id"]: r["decision"] for r in dispositions}
        for change in changes:
            for iid in change["issue_ids"]:
                if iid not in issues or decisions[iid] == "reject": raise ValueError("Final change must cite an accepted/modified verifier issue")
                if change["feature_key"] not in issues[iid]["feature_keys"]: raise ValueError("Final change is unrelated to its verifier issue")
            if change['feature_key'] in candidates(record['coding']) and change['feature_key'] not in candidates(priors['reconcile']['coding']):
                if not any(issues[iid]['evidence'] and issues[iid]['rule_ids'] for iid in change['issue_ids']):
                    raise ValueError('Final inferred/contribution addition requires positive source/rule support in its verifier issue')
