"""Mechanical checklist derived exclusively from the current job's permitted priors."""
from common import PRIORS, feature_objects, changed_keys, candidates, verification_targets

def build(stage, priors, registry):
    if set(priors) != set(PRIORS[stage]):
        raise ValueError('Contract must use exactly the permitted stage priors')
    result={'version':'2.0','stage':stage,'instructions':'This is a mechanical checklist, not coding advice. Make all substantive decisions from source and manual. VALIDATION_RULES.py is read-only reference text; do not execute tools.'}
    if stage=='reconcile':
        result['version']='3.0'
        a=priors['strict']['coding']; b=priors['lenient']['coding']
        fa=feature_objects(a); fb=feature_objects(b)
        result['differences_required']=[{'feature_key':k,'strict':fa.get(k),'lenient':fb.get(k)} for k in sorted(changed_keys(a,b))]
        result['differences_instruction']='The listed strict/lenient snapshots are read-only reference. Return exactly one differences row per listed feature_key with ONLY feature_key and your own resolution. Do not return strict or lenient fields. No missing, extra or duplicate feature keys. The controller inserts the exact immutable prior snapshots, including null, arrays, prose and metadata, then applies the original canonical schema and VALIDATION_RULES.py checks. SCHEMA.json defines your wire response; LEDGER_ASSEMBLY.py explains only this mechanical insertion. All coding, evidence, inference reviews and resolutions remain your authored decisions and are validated unchanged.'
        result['prior_candidate_keys']=sorted(candidates(a)|candidates(b))
        result['inference_instruction']='Review each prior_candidate_key PLUS any new likely Challenge or contribution in your proposed coding exactly once. Include ALL contributions, even evidenced ones. Decision include iff the feature exists in your coding, including a promoted likely-to-evidenced Challenge; otherwise exclude. Make your own evidence/rule/support assessment.'
    elif stage=='verify':
        coding=priors['reconcile']['coding']; features=feature_objects(coding)
        result['inference_tests_required']=[{'target_key':k,'burden':('eligible_likelihood' if features[k].get('evidence_status')=='likely' else 'scoped_exception' if features[k].get('evidence_basis')=='maintainer_presumption' else 'source_support')} for k in sorted(verification_targets(coding,registry))]
        result['instruction']='Test each listed target exactly once with the listed burden. Decide verdict, evidence and issues yourself. Also investigate omissions; the target list does not replace a full source/manual review.'
    elif stage=='final':
        result['issue_dispositions_required']=[{'issue_id':r['issue_id'],'feature_keys':r['feature_keys']} for r in priors['verify']['issues']]
        result['instruction']='Dispose each listed issue once. Compare every final feature object against PRIOR_reconcile.coding using feature_objects in VALIDATION_RULES.py. Log all changed objects, including prose and metadata. Each changed object needs an accepted/modified issue covering that key. A sound verifier requires an exact copy of coding and empty ledgers.'
    return result
