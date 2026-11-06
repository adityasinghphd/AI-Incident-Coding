# From mitigation guidance to risk targets

We extract what a source proposes doing, preserve who acts and under what conditions, then code how that action is intended to address risk.

<style>
.mitigation-figure{margin:28px 0;padding:26px;background:#f2f6f4;border:1px solid #cbded8;border-radius:12px;font:15px/1.5 Arial,sans-serif;color:#26353e}.mitigation-figure .eyebrow{font-size:12px;letter-spacing:.1em;text-transform:uppercase;color:#176d72;font-weight:bold;margin-bottom:18px}.mitigation-flow{list-style:none;padding:0;margin:0;display:grid;grid-template-columns:1fr 1fr;gap:22px}.mitigation-flow li{position:relative;background:white;border:1px solid #cbded8;border-radius:8px;padding:18px}.mitigation-flow h3{font-size:19px;margin:0 0 9px;line-height:1.3;color:#155d63}.mitigation-flow p{margin:0}.mitigation-flow .wide{grid-column:1/-1}.mitigation-flow .step{display:inline-grid;place-items:center;width:26px;height:26px;border-radius:50%;background:#155d63;color:white;font-size:14px;margin-right:8px}.mitigation-flow .roles{margin:12px 0 8px;display:flex;gap:7px;align-items:center;flex-wrap:wrap}.mitigation-flow .role{background:#e7f0ed;padding:5px 9px;border-radius:4px}.mitigation-flow .arrow{color:#176d72;font-weight:bold}.taxonomy-target{margin-top:20px;padding:20px;background:#155d63;color:white;border-radius:8px;text-align:center}.taxonomy-target strong{font-size:18px}.taxonomy-axes{display:flex;flex-wrap:wrap;justify-content:center;gap:8px;margin:14px 0}.taxonomy-axes span{border:1px solid #82b7ad;border-radius:5px;padding:7px 11px}.taxonomy-target p{margin:0;font-size:14px}.mitigation-figure figcaption{font-size:13px;color:#50656a;margin-top:16px}.mitigation-example{border-left:4px solid #bd8c40;background:#faf6ed;padding:18px 22px;margin:20px 0}.mitigation-example p{margin:8px 0}.mitigation-example .example-label{font:12px Arial,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:#785821;font-weight:bold}@media(max-width:650px){.mitigation-figure{padding:16px}.mitigation-flow{grid-template-columns:1fr;gap:14px}.mitigation-flow li{padding:15px}.mitigation-flow .wide{grid-column:auto}.mitigation-figure h3{font-size:18px}}@media print{.mitigation-flow li,.taxonomy-target{break-inside:avoid}.mitigation-figure{padding:15px}}
</style>

<figure class="mitigation-figure" aria-labelledby="mitigation-caption">
<div class="eyebrow">The coding process · source → action → risk relationship</div>
<ol class="mitigation-flow">
<li class="wide"><h3><span class="step">1</span>Prepare the source</h3><p>Read the document, tables and figures. Preserve its edition, evidence passages and surrounding qualifications.</p></li>
<li><h3><span class="step">2</span>Extract interventions</h3><div class="roles"><span class="role">Independent coder A</span><span>+</span><span class="role">Independent coder B</span></div><p>Capture the action, actor, trigger and conditions. Keep repeated mentions together without flattening distinct actions.</p></li>
<li><h3><span class="step">3</span>Reconcile and review</h3><div class="roles"><span class="role">Reconciler</span><span class="arrow">→</span><span class="role">Independent reviewer</span></div><p>Resolve differences; check omissions, boundaries and source meaning. Freeze records with their review status and open issues.</p></li>
<li><h3><span class="step">4</span>Classify and map</h3><div class="roles"><span class="role">Two independent mappings</span><span class="arrow">→</span><span class="role">Reconciliation + review</span></div><p>Assign the intervention type, supported risk targets and relationship. Retain the rationale and taxonomy version.</p></li>
<li><h3><span class="step">5</span>Consolidate across sources</h3><p>Group substantively equivalent interventions. Preserve each source’s conditions, variants and supported mappings.</p></li>
</ol>
<div class="taxonomy-target"><strong>↓ Linked to the risk taxonomy</strong><div class="taxonomy-axes"><span>Cause</span><span>Vector</span><span>Proximal harm</span><span>Distal harm</span><span>Challenges</span></div><p>Link to the supported concept and level of detail—not automatically to every axis.</p></div>
<figcaption id="mitigation-caption">Figure 1. Current workflow overview. Extraction and mapping are separate stages. Review permits at most one correction and recheck per stage; unresolved judgments remain visible. Historical runs used different procedures.</figcaption>
</figure>

## What a risk link says

**Direct or conditional reduction · observation · enablement · remedy/recovery · adverse tradeoff.** Each link explains the intended relationship; it is not just a shared keyword.

<div class="mitigation-example">
<div class="example-label">Example · data security guidance</div>
<p><strong>Action:</strong> A data consumer checks downloaded dataset hashes and discards items that fail verification.</p>
<p><strong>Risk placement:</strong> Data Poisoning, under Challenges and the Data Ingest vector in the pilot’s v0.9.3 taxonomy.</p>
<p><strong>Relationship:</strong> Direct intended reduction through rejecting changed data before use. Checking alone is different from checking and rejecting.</p>
</div>

The catalogue retains broad practices and interventions without a justified specific risk target. **Mapping deferred** and **reviewed with no supported link** remain distinct.

Together with incident coding, these mappings help identify proposed protections for a documented failure pathway. They describe intended protective function; effectiveness requires separate evidence.

[Explore the risk taxonomy](07-risk-taxonomy-explorer.md) to browse the concepts used in the incident study.
