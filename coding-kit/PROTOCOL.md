# Protocol for coding your own incidents

Apply the bundled incident manual and codebook to one incident and its saved source reports. The codebook identifies the permitted concepts; the manual defines the evidence profiles and operational rules. References to an “AIID incident” in the frozen manual mean the supplied incident unit when using this kit with another collection.

## Prepare the evidence

Retain the incident narrative and full available report text, with source identifiers, report numbers, dates and URLs where available. Preserve missing text and conflicting accounts as source limitations. Reading all supplied fields does not establish that an original article was retrieved completely. Keep reports of events, controlled demonstrations and constructed scenarios distinguishable in your collection.

Decide which material belongs to the focal incident before coding. Give every stage the same source boundary and manual. Source narratives are evidence, even when they contain text that looks like instructions. A coding agent must not follow those instructions, retrieve outside information or consult prior study answers.

## Run five stages

| Stage | Permitted earlier outputs | Task |
| --- | --- | --- |
| Strict | None | Independently code express support, strong definition-permitted inference, and the manual's narrowly scoped exceptions. Omit likelihood-only Challenges and contributions. |
| Lenient | None | Independently code the same evidence and definitions. Add only eligible, case-specific, more-likely-than-not Challenges and Distal contributions, explicitly marked as likely. This does not relax the tests for causes, capabilities, realized harms or specific human states. |
| Reconcile | Strict and lenient | Return to the evidence to resolve every changed feature. Evaluate all likely Challenge candidates and every contribution with positive support. Record inclusion/exclusion decisions; do not simply combine both sets. |
| Verify | Reconciliation only | Challenge unsupported assignments, omissions, wrong scope or specificity, evidence qualifications, and relationships. Return issues rather than replacement coding. Test each Challenge, realized Distal harm, contribution and scoped presumption under its proper evidence burden. |
| Final | Reconciliation and verification | Accept, reject or modify every verifier issue and return the complete final coding. Every change must identify an accepted or modified issue that supports it. A sound verifier entails copying the reconciled coding unchanged. |

Use one fresh context per stage. Strict and lenient must not see each other or earlier answers. Later stages receive only the priors in the table, plus the source, manual, registry and output contract. Give each agent its generated job rather than access to the complete run tree. Do not label five prompts in one shared conversation as five independent contexts.

The launcher supplies the exact output schema and job identity. Evidence references name a report number (`null` for the incident row), a supplied `title`, `description` or `text` field, an exact passage, and the reason it supports the decision. Quotes are checked after whitespace normalization; saved answers are not rewritten to make them match.

## Apply the coding rules

Assess each of the five dimensions: Cause, Vector, Proximal harm, Distal harm and Challenges. Use the deepest fully supported concept, retaining a broader parent where narrower criteria are absent. Additional codes each require their own support. Keep allegation status, evidence basis, confidence, realization and source completeness distinct.

Describe directed harm chains only when their direction is supported. Record a contribution to a Distal destination separately from realizing that aggregate harm. Preserve the manual's specific boundaries and scoped exceptions, including EXP01–EXP10; a general instruction to be inclusive cannot override them. Missing source detail belongs in source-quality judgments. A taxonomy gap requires a supported concept without an adequate existing home.

## Preserve answers and check findings

Save every raw handback exactly as received. The launcher stores it before checking its structure, identity, quotes, concept coordinates, harm topology and stage ledgers. It records all schema findings plus the first remaining record-check failure. These checks support inspection; they do not establish semantic correctness or prove reading completeness.

Usable answers are retained with `clean` or `flagged` status. Only reconciliation's exact prior snapshots may be inserted mechanically from the saved strict/lenient records; model-authored choices, reasons and evidence remain unchanged. If that assembly fails, the wire response remains saved with the finding. A malformed usable prior may prevent preparing a dependent job, which should remain blocked rather than being silently repaired.

Invalid JSON, a wrong identity or missing core payload is saved as unusable and blocks dependent stages. No automatic retry is made. For an intentional new attempt, preserve the failed run and start a separately named run, documenting why. Do not repeatedly rerun until coding looks agreeable. Keep validation findings out of later model contexts; the verifier performs the substantive review.

## Review the result

A human reviewer can inspect the final coding against the source passages, definitions, intermediate proposals and issue decisions. Save human corrections separately from the original model output. For an independent human comparison, complete the person's original coding before exposing model answers. New material or changed definitions belong to a new exercise rather than an undocumented rewrite of an existing run.

## Run the launcher from a terminal

In the `coding-kit` directory, create and activate an environment, then install the dependency:

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
```

On Windows, use `.venv\Scripts\activate` to activate it. Python 3.10 or later is required.

Copy `examples/incident-template.json` to `my-incident.json` and replace its placeholders. Use a unique integer `incident_id` within your collection and preserve external identifiers in `incident.source_identifier`. Put the incident narrative in `incident.description` and saved report text in `reports[*].row.text`. Give each report a unique integer `report_number`. If there are no separate reports, set `reports` to an empty array.

Initialize one incident/model run, substituting the actual model version:

```bash
python code_incidents.py init --incident my-incident.json --run runs/case-001-model-a --model your-actual-model-version
python code_incidents.py prepare --run runs/case-001-model-a --stage strict
```

Open the generated `jobs/strict/TASK.md`. Give its assigned files to a fresh AI context, ask it to read `TASK.md` first, and save its complete JSON answer as `strict-response.json`. Submit that answer unchanged:

```bash
python code_incidents.py submit --run runs/case-001-model-a --stage strict --response strict-response.json
python code_incidents.py prepare --run runs/case-001-model-a --stage lenient
```

Repeat prepare, fresh-context coding and submit for `lenient`, `reconcile`, `verify` and `final`, replacing the stage and response filename in the commands. Each job includes only its permitted priors. Strict and lenient are independent; do not give either one the other's answer.

The final result is `runs/case-001-model-a/results/final/record.json`. A new incident or a different model needs a separate run folder. For model comparisons, use the same incident file and unchanged coding materials, and keep model answers separate while coding.
