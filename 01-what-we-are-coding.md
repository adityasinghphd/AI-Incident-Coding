# The risk taxonomy prototype

The risk taxonomy prototype turns an AI incident account into a structured description of how the problem arose, what capability was involved, what was harmed, and what conditions made prevention or response difficult. It gives researchers a shared vocabulary for comparing incidents described in very different language, while retaining the source evidence behind each judgment.

The prototype combines three parts: a hierarchy of defined risk concepts, a coding guide for applying those concepts to incident evidence, and crosswalks connecting them to existing frameworks, including the AI Risk Index (AIRI). It also provides common risk targets for separately coded mitigations. **This is a research prototype, not yet a public release.**

## Five dimensions of an incident

Each axis represents a different dimension of an incident: its causes, the AI capabilities involved, proximal harms, distal harms, and challenges to prevention or response. A single incident can receive several supported codes on an axis, and an axis can remain empty when the evidence does not support a choice.

| Axis | What it records | How to apply the distinction |
| --- | --- | --- |
| Cause | The mechanism through which the problem arose: for example, misuse, malfunction, an emergent interaction, or harmful effects of normal use. | Establish what happened and why the proposed mechanism fits. A bad outcome alone does not prove malfunction or malicious intent. |
| Vector | The AI capability involved in the harmful pathway, such as generating content, predicting or deciding, ingesting data, or acting on a digital or physical system. | Identify the operative capability. A capability is not itself proof of harm; some infrastructure effects of AI can be coded without an applicable capability label. |
| Proximal harm | A supported outcome affecting bounded people, organizations, records, property, or environments. | Identify the affected entity and the outcome, such as wrongful denial of a benefit, financial loss, record corruption, injury, or local pollution. Proximal does not mean minor or short-lived. |
| Distal harm | A supported degradation of a wider social, institutional, economic, or environmental system. | Identify the shared system and the change in its functioning. Severity, duration, or the number of people affected does not by itself establish a systemic outcome. |
| Challenges | Standing conditions that make prevention, oversight, or response difficult, such as overreliance, limited transparency, or a specific governance gap. | Explain the condition and its connection to the incident. A single failure does not automatically establish a standing deficiency. |

Separating these dimensions makes it possible to distinguish the same harmful outcome produced by different mechanisms, or the same capability involved in very different outcomes. It also prevents one broad label, such as “misinformation,” from substituting for the entire incident description.

## Definitions and levels of detail

The hierarchy moves from broad groups to types and, where available, narrower subtypes. Each selected concept has a definition and a position in that hierarchy. Coding notes explain inclusion criteria, exclusions, neighboring concepts, and difficult boundaries. The codebook version fixes which definitions and rules apply to a particular exercise.

Coders choose the most specific concept whose distinguishing criteria are supported. If a report establishes a malfunction but does not establish whether it arose from training data, prediction error, or another mechanism, a broader supported assignment is preferable to guessing a subtype. Selecting a narrower concept already locates it within its broader ancestors; those ancestors should not be counted as additional independent harms.

Multiple codes describe independently supported features. They should not bundle mutually exclusive explanations of an uncertain event. For example, deliberate fabrication and an unintended hallucination should not both be assigned simply because the report does not establish which occurred. That uncertainty belongs in the explanation.

## Evidence and relationships between harms

A coded record retains the incident identifier, source material, selected categories, supporting passages, and reasons for applying each definition. It also records source limitations and qualifications, such as whether an outcome is alleged or established. An unreported detail remains unknown; it does not become evidence that a safeguard was absent.

The prototype distinguishes realized harm from an incident's contribution to a wider risk. A bounded act of discrimination can harm particular people and contribute to systemic rights erosion without proving that the incident itself established a society-wide state. Similarly, a standing Challenge may be directly evidenced or, where the coding protocol permits it, explicitly marked as a case-specific likely inference. Those statuses must remain distinguishable.

Harm links add structure beyond a list of categories. If the evidence shows that one harm led to another, the record can represent a directed chain. If two harms occurred independently, it records them in parallel. Co-occurrence alone does not establish causation, and a possible future consequence is not automatically a realized terminal harm.

## An example from narrative to coding

Consider an invented case: an AI system inserts a fabricated statement into an applicant's administrative record. An official relies on it to deny a benefit, and the report documents the applicant's resulting financial loss. The report also says the official accepted the output without checking it.

| Part of the account | What the prototype separates |
| --- | --- |
| The system produced fabricated information unintentionally | A possible hallucination mechanism under Cause, provided the facts establish that it was unintended. |
| It generated text used in an administrative process | Content generation under Vector. Human reliance on that text does not automatically establish that the AI itself had decision-making authority. |
| False information entered the applicant's record | Record-integrity harm, distinct from the act of generating the text. |
| The benefit was wrongfully denied and financial loss followed | Separately supported rights and economic harms, with a chain only where the account supports those links. |
| The official acted without checking the output | Assess Overreliance under the guide's verification criteria; do not infer every other oversight or governance deficiency. |
| The incident might undermine public trust | Do not code realized societal loss of trust without evidence of that wider outcome. Assess any contribution separately. |

The example is a demonstration of the coding distinctions, not an observed incident or evidence of their reliability. A reviewer can inspect each assignment against the narrative instead of accepting a single summary label.

## Crosswalking between risk frameworks

A crosswalk records how a category in one framework relates to a category in another. The prototype acts as a common reference point: a researcher can start with an external framework's terminology, identify corresponding prototype concepts, and retrieve incidents coded to them. Connections to AIRI support comparison with that framework as well.

Mappings preserve the original category, its source, the destination concept, and the rationale for the connection. They need not be one-to-one. A broad source category may cover several narrower concepts; two frameworks may overlap only partly; and a source concept may have no adequate destination. A mapping should make these differences visible rather than treating every connection as an equivalence.

For example, a framework category combining “privacy and autonomy” may connect to several concepts in the prototype. An incident supporting unauthorized disclosure can then be found through that broad category without automatically receiving a Loss of Agency code. Each incident assignment still has to meet its own definition. Conversely, a broad incident code cannot be used to assert a narrower external category without the missing evidence.

## Connecting incident coding to mitigations

Mitigation coding uses the same risk concepts as targets for interventions described in source documents. This lets researchers ask which proposed measures address a mechanism, capability, outcome, or standing condition seen in an incident. The mitigation record retains the intervention, its conditions, and the kind of relationship claimed, such as direct reduction, observation, enablement, or remedy.

A shared target makes an intervention relevant for examination. Establishing that it would have prevented a particular incident requires additional evidence about timing, implementation, coverage, and causal effect. The prototype organizes those questions; a crosswalk alone does not answer them.

The intended uses are therefore to compare incident patterns, inspect coding decisions, translate between framework vocabularies, identify gaps in representation, and connect incident evidence with candidate mitigations. How consistently models and people can apply these distinctions is the subject of the validation experiment described in Page 06.
