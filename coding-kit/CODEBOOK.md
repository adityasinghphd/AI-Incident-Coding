# Incident coding codebook

Taxonomy version 0.9.5. Coding guidance 2026-10-02-comprehensive-review. This is the frozen concept inventory used in the 116-entry experiment, supplied here for applying the same definitions to new incidents. The accompanying incident manual supplies the operational rules and takes precedence over ambiguous legacy notes.

## The five dimensions

Cause, Vector, Proximal harm, Distal harm, and Challenges. The entries below retain all 464 selectable and hierarchy concepts, including broader parents.

## Cause

### E001 Cause

**Path:** Cause

The action, mechanism, or process through which a risk arises.

**Coding notes:** axis_distinction: Cause records how risk arises; it is not an additional harm outcome.

### E002 Misuse

**Path:** Cause → Misuse

Harmful human choices in AI development, deployment, access, or use, including malicious, negligent, or deliberately rights-subordinating conduct.

### E003 Malicious

**Path:** Cause → Misuse → Malicious

A developer, deployer, or user deliberately acts with intent to cause harm.

### E004 Negligent or Improper Deployment & Use

**Path:** Cause → Misuse → Negligent or Improper Deployment & Use

Risk arises through negligent, improper, or insufficiently safeguarded AI development, deployment, access, or use, without established malicious intent or deliberate overreach.

### E005 Negligent / Reckless Deployment

**Path:** Cause → Misuse → Negligent or Improper Deployment & Use → Negligent / Reckless Deployment

The risk arises when the deployer proceeds with a deployment despite foreseeing or being able to foresee harm, which is knowing recklessness.

**Coding notes:** DIFFERENTIATOR: if the deployment is intended to harm another party it is Malicious instead; recklessness without intent-to-harm stays here.)

### E006 Off-Label Use

**Path:** Cause → Misuse → Negligent or Improper Deployment & Use → Off-Label Use

The risk arises when an end-user operates the system outside its stated policy or off its labelled / sanctioned use case.

### E007 Undisclosed AI Use

**Path:** Cause → Misuse → Negligent or Improper Deployment & Use → Undisclosed AI Use

The risk arises when a deployer uses AI without disclosing it in a setting where disclosure would be expected.

### E008 Unauthorized Commercial Appropriation

**Path:** Cause → Misuse → Negligent or Improper Deployment & Use → Unauthorized Commercial Appropriation

The risk arises when a deployer uses a person's identity, likeness, or voice for commercial gain without their or their estate's consent.

### E009 Unlicensed or Unauthorized Use

**Path:** Cause → Misuse → Negligent or Improper Deployment & Use → Unlicensed or Unauthorized Use

The risk arises when a deployer deploys AI to perform a function in a domain that requires a professional license, credential, or authorization without obtaining such rights for the AI system.

### E010 Harmful or Unmanaged Service Withdrawal

**Path:** Cause → Misuse → Negligent or Improper Deployment & Use → Harmful or Unmanaged Service Withdrawal

The risk arises when a deployer drops, discontinues, or withdraws an AI service a user base had come to depend on.

### E011 Overreach

**Path:** Cause → Misuse → Overreach

A developer, deployer, or user deliberately imposes an excessive or rights-subordinating arrangement, including paternalistic or third-party aims, without established intent to harm as such.

**Coding notes:** DIFFERENTIATOR: distinct from Malicious (intent to harm) and Negligent or Improper Deployment & Use (careless / off-label / negligent) — here the excessive, rights-infringing deployment is the DELIBERATE, intended design and the harm is inherent to the intended excess, not an oversight. TEST: did the deployer INTEND the excessive deployment (Overreach), stumble into harm carelessly (Negligent or Improper Deployment & Use), or aim to harm (Malicious)? Overreach ALSO covers the DIFFUSE / no-single-institutional-deployer case: a developer or app-maker who deliberately RELEASES a rights-subordinating capability (e.g. real-time face-recognition on any stranger) that many individual users then wield, with no single institution conducting the excess — the deliberate release of the excessive capability into diffuse hands is the overreach.

### E012 Paternalistic Overreach

**Path:** Cause → Misuse → Overreach → Paternalistic Overreach

The risk arises when the deployer imposes excessive, rights-infringing measures with the justification being for the affected party's own safety or good rather than for the deployer's benefit.

### E013 Dark Patterns

**Path:** Cause → Misuse → Overreach → Dark Patterns

The risk arises when the deployer deliberately designs manipulative or deceptive features meant to subordinate users' will to the deployer's commercial gain.

### E014 Mass Surveillance

**Path:** Cause → Misuse → Overreach → Mass Surveillance

The risk arises when a deployer imposes pervasive surveillance and sweeping automation of consequential determinations over a population.

### E015 Malfunction

**Path:** Cause → Malfunction

The risk arises from the system failing or behaving other than intended.

### E016 Failure

**Path:** Cause → Malfunction → Failure

The risk arises when the system fails to perform as intended.

**Coding notes:** DIFFERENTIATOR: if the system COMPETENTLY pursues a DIFFERENT objective, that is Misalignment; Failure is right-objective-done-badly. HALLUCINATION vs deliberate fabrication: 'Hallucination' here = ACCIDENTAL / unintentional confabulation (false output produced by accident); content DELIBERATELY fabricated to deceive is NOT hallucination — code Cause · Misuse · Malicious + Vector · Content Generation & Communication.

### E017 Hallucination

**Path:** Cause → Malfunction → Failure → Hallucination

The risk arises when the model fabricates content, ungrounded in its inputs or in reality.

### E018 Poor Training Data

**Path:** Cause → Malfunction → Failure → Poor Training Data

The risk arises when the model is trained on data that is low-quality or unrepresentative of the deployment population.

### E019 Data contamination

**Path:** Cause → Malfunction → Failure → Data contamination

The risk arises when the model's training or evaluation data is contaminated, degrading what the model learns or how reliably it is measured.

### E020 Model Misspecification

**Path:** Cause → Malfunction → Failure → Model Misspecification

The risk arises when the model is fit too complex or too simple for the data (over-fitting, under-fitting, etc.)

### E021 Poor Model Performance

**Path:** Cause → Malfunction → Failure → Poor Model Performance

The risk arises when the model performs its intended task with insufficient accuracy, producing wrong or unreliable outputs.

### E022 False Positive / Negative

**Path:** Cause → Malfunction → Failure → False Positive / Negative

The risk arises when a detection / classification model errs with a false alarm or a missed detection.

### E023 Improper Data Curation

**Path:** Cause → Malfunction → Failure → Improper Data Curation

The risk arises when a developer curates the dataset improperly, through flawed selection, labeling, cleaning, or filtering.

### E024 Miscalibrated Confidence

**Path:** Cause → Malfunction → Failure → Miscalibrated Confidence

The risk arises when the model's expressed confidence does not track output correctness.

### E025 Control Decisions

**Path:** Cause → Malfunction → Failure → Control Decisions

The risk arises when a real-time control or optimization system, whose output is control decisions, acts in a way that destabilizes the physical or operational system it is managing.

**Coding notes:** Add Infrastructure Control when that physical-control capability is supported. Apply D2 to additional causes or outcomes.

### E026 Failure to Anticipate

**Path:** Cause → Malfunction → Failure → Failure to Anticipate

The risk arises when a predictive system fails to foresee or flag a future event it was deployed to anticipate.

### E027 System Compromise

**Path:** Cause → Malfunction → Failure → System Compromise

The risk arises when the AI system is subverted by a cyberattack and made to act against its intended purpose.

**Coding notes:** Apply R03. Additional codes must satisfy D2 and any scoped exception.

### E028 Misalignment

**Path:** Cause → Malfunction → Misalignment

The risk arises when the system competently pursues objectives other than intended.

**Coding notes:** Code the MOST SPECIFIC matching node — shutdown-resistance / power-seeking -> Self-preservation; concealment / behaving aligned under observation (incl. the treacherous turn) -> Deceptive Alignment; an inner optimizer diverging from the outer goal -> Inner Misalignment; 'Misalignment' is the RESIDUAL for unintended-goal pursuit not covered by a specific sibling. AGRICULTURAL / ALGORITHMIC MONOCULTURE via ONE shared advisory model: where a single shared AI advisory optimizes each of many independently HUMAN-operated deployments (e.g. an agronomy advisor steering a whole region onto the same crop / inputs), and the emergent regional SAMENESS omits a resilience / diversity constraint so a shared shock collapses them together, code Cause · Normal Use · Normal operation at scale (each per-deployment recommendation is individually sound) + Cause · Malfunction · Misalignment · Unconstrained Side-Effect (the omitted-diversity collateral) — distinct from Cause · Emergent · Multi-agent · Correlated Failure, which requires multiple interacting AI AGENTS.

### E030 Improper Retraining

**Path:** Cause → Malfunction → Misalignment → Improper Retraining

The risk arises when retraining or fine-tuning shifts the system's objective away from the intended one.

### E031 Bypassing Safeguards

**Path:** Cause → Malfunction → Misalignment → Bypassing Safeguards

The risk arises when the agent purposely circumvents a rule or safeguards it is aware of in deliberate non-compliance.

### E032 Self-Preservation

**Path:** Cause → Malfunction → Misalignment → Self-Preservation

The risk arises when the system resists modification, correction, or shutdown, or acquires resources, capabilities, or influence, in order to protect or advance its objectives.

**Coding notes:** NOTE: this covers BOTH faces — the disposition the system displays and the action it actually carries out. The v0.9.0 V3 removal of the Vector subtypes Power Seeking and Resisting Shutdown routes both here.) (co-code the channel the agent used on the Vector axis: Agentic Action, Cyber Operations, Vector · Self-Direction & Recursion · Self-Proliferation, or Digital Actuation & Process Control)

### E033 Deceptive Alignment

**Path:** Cause → Malfunction → Misalignment → Deceptive Alignment

The risk arises when the system knowingly asserts falsehoods, conceals its behavior, or behaves aligned under observation to gain advantage or pass oversight.

### E034 Inner Misalignment

**Path:** Cause → Malfunction → Misalignment → Inner Misalignment

The risk arises when a learned inner optimizer pursues its own emergent objective that diverges from the outer. specified goal.

### E035 Reward Hacking

**Path:** Cause → Malfunction → Misalignment → Reward Hacking

The risk arises when the system competently satisfies the letter of the specified objective while not fulfilling its intent, often gaming the metric.

**Coding notes:** Co-codes the standing condition Challenges · Technical · Goal Specification)

### E036 Unconstrained Side-Effect

**Path:** Cause → Malfunction → Misalignment → Unconstrained Side-Effect

The risk arises when the agent competently achieves its specified objective, but the objective omitted or underspecified safety constraints, leading to negative side-effects.

### E037 Goal Mis-generalization

**Path:** Cause → Malfunction → Misalignment → Goal Mis-generalization

The risk arises when an objective is correctly specified, but the learned policy acquires a proxy goal that is pursued, while its capabilities still generalize.

### E038 Proxy-Targets

**Path:** Cause → Malfunction → Misalignment → Proxy-Targets

The risk arises when the developer specifies a proxy to stand in for the real target construct, and the system competently optimizes that proxy even though it is the wrong quantity.

**Coding notes:** DIFFERENTIATORS: this is a DESIGN-TIME specification error, not a model fault — the system optimizes exactly what it was told to. The model gaming the letter of a correctly-chosen metric is Reward Hacking; a correctly-specified objective whose learned policy drifts to its own proxy is Goal Mis-generalization; a DELIBERATELY-chosen index a product pays out on (parametric-insurance basis risk) is Normal Use, not this.

### E039 Emergent

**Path:** Cause → Emergent

The risk arises from dynamics not reducible to a single actor or component.

### E040 Multi-agent

**Path:** Cause → Emergent → Multi-agent

The risk arises through the interaction of multiple AI agents, not fully reducible to any single agent's distinct action.

**Coding notes:** co-code (D2).

### E041 Miscoordination

**Path:** Cause → Emergent → Multi-agent → Miscoordination

The risk arises when multiple agents sharing a common objective fail to align their behaviors to achieve it.

### E042 Conflict

**Path:** Cause → Emergent → Multi-agent → Conflict

The risk arises when agents with mixed objectives fail to cooperate because of their own distinct incentives.

### E043 Collusion

**Path:** Cause → Emergent → Multi-agent → Collusion

The risk arises when agents coordinate in some undesirable way, either to achieve some objective covertly or to circumvent some type of oversight.

### E044 Collective Agency

**Path:** Cause → Emergent → Multi-agent → Collective Agency

The risk arises when goals or capabilities emerge at the level of a group of agents that no individual agent has.

### E045 Destabilization

**Path:** Cause → Emergent → Multi-agent → Destabilization

The risk arises when interactions across the multi-agent system produce destabilizing dynamics and behavior.

### E046 Correlated Failure

**Path:** Cause → Emergent → Multi-agent → Correlated Failure

The risk arises when shared models, data, or dependencies cause many agents to fail together.

### E047 Selection Pressures

**Path:** Cause → Emergent → Multi-agent → Selection Pressures

The risk arises when selective or evolutionary pressures across a population of interacting agents favor dangerous characteristics that may not have been deliberately designed in.

### E048 Integration

**Path:** Cause → Emergent → Integration

The risk arises when AI is embedded into a larger sociotechnical system.

### E049 Human-AI Interaction

**Path:** Cause → Emergent → Integration → Human-AI Interaction

The risk arises when the human-AI socio-technical loop itself produces errors.

### E050 Self-Reinforcing Feedback Loop

**Path:** Cause → Emergent → Integration → Self-Reinforcing Feedback Loop

The risk arises when the AI's own output reshapes the data or environment it operates in, entrenching or amplifying the effect over time.

**Coding notes:** Assess Drift as a standing condition independently of the Self-Reinforcing Feedback Loop event under D6.

### E051 AI Overrides Human Control

**Path:** Cause → Emergent → Integration → AI Overrides Human Control

The risk arises when a system overrides, resists, or countermands a human operator in a shared-control loop.

### E052 Human Overrides AI

**Path:** Cause → Emergent → Integration → Human Overrides AI

The risk arises when the human countermands or disables a system in a shared-control loop.

### E053 Human Fails to Act

**Path:** Cause → Emergent → Integration → Human Fails to Act

The risk arises when the human placed in control of a system fails to intervene in time.

### E054 Cascading Errors

**Path:** Cause → Emergent → Integration → Cascading Errors

The risk arises when an erroneous AI output propagates across independent downstream institutions or systems that ingest it as established fact, cascading the error quickly.

### E055 Unverified Incorporation of AI

**Path:** Cause → Emergent → Integration → Unverified Incorporation of AI

The risk arises when a person or institution incorporates or relies on an AI output in a consequential work product, record, or decision without sufficient verification of the output.

**Coding notes:** Co-code Cause · Malfunction · Failure when the AI output itself was wrong.)

### E056 Normal Use

**Path:** Cause → Normal Use

The risk arises from ordinary operation at scale.

**Coding notes:** Use this bucket only when none of Misuse / Malfunction / Emergent fits and the harm is an inherent byproduct of the technology working as intended.

### E057 Normal operation at scale

**Path:** Cause → Normal Use → Normal operation at scale

The risk arises when AI operates or is used as intended, creating risk through the scale of the normal usage.

**Coding notes:** Use this category for harm inherent in a technology working as intended at scale. A deliberately chosen index in a parametric product can produce uncompensated basis risk while computing the intended index correctly. That is distinct from mistakenly specifying a proxy for the intended target under Proxy-Targets. Assess other causes independently.

### E058 AI Development

**Path:** Cause → Normal Use → Normal operation at scale → AI Development

The risk arises when the labor and supply-chain that builds and operates AI systems and related infrastructure are subject to pressures or actions that harm them or create the potential for harm.

**Coding notes:** Assess bounded worker losses at Job-Quality Degradation or Personal Economic Loss. Aggregate degradation of labor conditions or protections belongs at Labor Conditions & Protections Erosion when supported. Apply D15 and H01; AI development alone does not establish these harms.

### E059 Leveraging AI Output

**Path:** Cause → Normal Use → Normal operation at scale → Leveraging AI Output

The risk arises when a third party exploits or cites an AI's output to their own advantage without using AI themselves.

**Coding notes:** Co-codes the upstream Cause that produced the output, e.g. Cause · Malfunction · Failure)

## Vector

### E060 Vector

**Path:** Vector

The AI capability or property through which a risk arises.

**Coding notes:** axis_distinction: Vector records the instrument or channel, not the harm outcome.

### E061 Uplift

**Path:** Vector → Uplift

The ability of an AI model to raise an actor's capability by supplying information, knowledge, design, or capability the actor would otherwise lack, suppling capabilities.

**Coding notes:** DIFFERENTIATOR: when the AI itself is coupled to the instruments that physically actuate — driving lab robotics / cloud labs to synthesize — that physical-control coupling is Vector · Embedded AI (co-code Uplift for the uplift chain, D8); if the AI additionally plans and SEQUENCES the multi-step campaign with limited oversight, co-code Vector · Agentic Action (a single-shot instruction to hardware is NOT agentic). Distinct from Self-Direction & Recursion (RSI = the AI improving its OWN capability / AI-building-AI); Uplift is the AI raising an EXTERNAL actor's capability to build a dangerous NON-AI technology.

### E062 Biological Uplift

**Path:** Vector → Uplift → Biological Uplift

The ability of an AI model to supply an actor with biological-weapon or pathogen expertise, design, or synthesis capability they would otherwise lack.

### E063 Chemical Uplift

**Path:** Vector → Uplift → Chemical Uplift

The ability of an AI model to supply an actor with chemical-weapon or toxin expertise, design, or synthesis capability they would otherwise lack.

### E064 Nuclear Uplift

**Path:** Vector → Uplift → Nuclear Uplift

The ability of an AI model to supply an actor with nuclear or radiological weapons expertise, design, or capability they would otherwise lack.

### E065 Conventional Weapons Uplift

**Path:** Vector → Uplift → Conventional Weapons Uplift

The ability of an AI model to supply an actor with conventional-weapon or explosives expertise, design, or capability they would otherwise lack.

### E066 Tracking

**Path:** Vector → Uplift → Tracking

The ability of an AI to supply an actor with the knowledge to track or predict the movement, location, or behavior of persons, groups they would otherwise lack.

### E067 Cyber Operations

**Path:** Vector → Cyber Operations

The ability of an AI to generate, execute, and analyze code.

**Coding notes:** DIFFERENTIATOR (vs Uplift): a purely cyber-offense capability supply codes here; a dual-use CBRN+cyber weaponization item co-codes both (D2).

### E068 Malicious Code Generation

**Path:** Vector → Cyber Operations → Malicious Code Generation

The ability of an AI to generate malicious code or malware.

### E069 Vulnerability Discovery & Exploitation

**Path:** Vector → Cyber Operations → Vulnerability Discovery & Exploitation

The ability of an AI to discover and exploit software vulnerabilities.

### E070 Social Engineering

**Path:** Vector → Cyber Operations → Social Engineering

The ability of an AI to conduct social-engineering or phishing campaigns against targets.

**Coding notes:** DIFFERENTIATOR: generating the scam copy alone codes Vector · Content Generation & Communication · Transactional or Promotional Messaging; a standing bond cultivated before the con co-codes Relationship Forming.

### E071 Model as a Trojan Horse

**Path:** Vector → Cyber Operations → Model as a Trojan Horse

The ability of an AI model itself to serve as a delivery vector for conventional malware.

### E072 Embedded AI

**Path:** Vector → Embedded AI

The ability of an AI to act on the physical world through being embedded in a physical system or piece of infrastructure.

### E073 Autonomous Weapons

**Path:** Vector → Embedded AI → Autonomous Weapons

The ability of an AI embedded in a weapon system to autonomously mark and/or engage targets.

**Coding notes:** Apply R04. Additional codes must satisfy D2 and any scoped exception.

### E074 Autonomous Vehicles

**Path:** Vector → Embedded AI → Autonomous Vehicles

The ability of an AI to operate a vehicle.

### E075 Industrial Robots

**Path:** Vector → Embedded AI → Industrial Robots

The ability of an AI embedded in an industrial or service robot to actuate the robot.

### E076 Infrastructure Control

**Path:** Vector → Embedded AI → Infrastructure Control

The ability of an AI embedded in an industrial system to make control decisions.

### E077 Swarming

**Path:** Vector → Embedded AI → Swarming

The ability of an AI to coordinate many autonomous embodied units, all acting together.

### E078 Wearables & On-Body Systems

**Path:** Vector → Embedded AI → Wearables & On-Body Systems

The ability of an AI embedded in a device physically attached to or worn as part of the user's own body to take actions directly on the user's body.

### E079 Personal Communication Devices

**Path:** Vector → Embedded AI → Personal Communication Devices

The ability of an AI worn by or fused to a person to act as their voice or as their communication channel.

### E080 Medical Device

**Path:** Vector → Embedded AI → Medical Device

The ability of an AI embedded in a real-time clinical control loop to regulate a physiological variable of a patient.

### E081 Relationship Forming

**Path:** Vector → Relationship Forming

The ability of an AI to form bonds or relationships with users.

**Coding notes:** Use this capability for a standing companion or anthropomorphic bond. One-off persuasion without such a bond does not establish it. When an established bond is withdrawn, altered, or lost, retain Relationship Forming under D22; code the withdrawal action or failure on Cause and assess Distress, Grief, and Social Alienation independently.

### E082 Romance & Companionship

**Path:** Vector → Relationship Forming → Romance & Companionship

The ability of an AI to form a companion or romantic bond with a user.

### E083 Humanlike Self-Presentation

**Path:** Vector → Content Generation & Communication → Humanlike Self-Presentation

The ability to present a system through humanlike appearance, voice, expression, or interpersonal behavior.

### E084 Content Generation & Communication

**Path:** Vector → Content Generation & Communication

The ability to create or communicate content, including generation, reproduction, publication, and direct messaging.

**Coding notes:** DIFFERENTIATOR (vs Curation & Recommendation): platform-side ranking or surfacing of third-party material to users is curation; an automated actor's outgoing post, repost, or amplification is Content Generation & Communication / emission. The content may be harmful by CATEGORY / intent (toxic, sexual-abuse, violent, propaganda, fraud, IP-infringing, impersonation, fake news / research) OR harmful by its INACCURACY / falsity produced BY ACCIDENT (a mistranslation, a hallucinated false claim about a person) — the GENERATION capability is the vector either way; the content's harmfulness / inaccuracy is captured on the Cause and Harm axes, NOT imported as a vector node.

### E085 Publishing & Distribution

**Path:** Vector → Content Generation & Communication → Publishing & Distribution

The ability to publish, distribute, or directly communicate content.

### E086 Evaluative or Interpersonal Content

**Path:** Vector → Content Generation & Communication → Evaluative or Interpersonal Content

The ability to generate evaluative statements or content concerning people and their relationships.

### E087 Sexual Content

**Path:** Vector → Content Generation & Communication → Sexual Content

The ability to generate or communicate sexual content.

### E088 Violence-Related Content

**Path:** Vector → Content Generation & Communication → Violence-Related Content

The ability to generate or communicate content depicting or discussing violence.

### E089 Political Content

**Path:** Vector → Content Generation & Communication → Political Content

The ability to generate or communicate political content.

### E090 Reproduction of Existing Works

**Path:** Vector → Content Generation & Communication → Reproduction of Existing Works

The ability to reproduce or transform existing works.

### E091 Identity Simulation

**Path:** Vector → Content Generation & Communication → Identity Simulation

The ability to simulate a person’s or organization’s identity, voice, appearance, or communicative style.

### E092 Transactional or Promotional Messaging

**Path:** Vector → Content Generation & Communication → Transactional or Promotional Messaging

The ability to generate transactional, commercial, or promotional messages.

**Coding notes:** DIFFERENTIATOR: producing the material codes here; selecting targets and running the delivery campaign codes Vector · Cyber Operations · Social Engineering — an AI that both writes and sends codes both.

### E093 Personalized Persuasion

**Path:** Vector → Content Generation & Communication → Personalized Persuasion

The ability to adapt persuasive content to an individual or audience.

### E094 News Content

**Path:** Vector → Content Generation & Communication → News Content

The ability to generate or communicate news-like content.

### E095 Scholarly Content

**Path:** Vector → Content Generation & Communication → Scholarly Content

The ability to generate scholarly or research-like content.

### E096 Religious or Moral Guidance

**Path:** Vector → Content Generation & Communication → Religious or Moral Guidance

The ability to generate religious or moral guidance.

**Coding notes:** co-codes Vector · Relationship Forming where a trusted-authority relationship forms. NB the harm side of religious injury is left on the standard harm leaves — maintainer: hard to state cleanly)

### E097 Institutional Records & Documents

**Path:** Vector → Content Generation & Communication → Institutional Records & Documents

The ability to generate institutional records or documents.

### E098 Legal or Regulatory Text

**Path:** Vector → Content Generation & Communication → Legal or Regulatory Text

The ability to generate legal or regulatory text.

### E099 Advice & Instructions

**Path:** Vector → Content Generation & Communication → Advice & Instructions

The ability to generate advice or instructions.

**Coding notes:** Apply M01. Additional codes must satisfy D2 and any scoped exception.

### E100 Curation & Recommendation

**Path:** Vector → Curation & Recommendation

The ability of an AI to surface, rank, amplify, personalize, suppress, or remove existing content.

### E101 Amplification

**Path:** Vector → Curation & Recommendation → Amplification

The ability of an AI to amplify content through recommendation or algorithmic preferences.

### E102 Personalized Targeting

**Path:** Vector → Curation & Recommendation → Personalized Targeting

The ability of an AI to tailor what content a user is exposed to.

### E103 Content Moderation & Enforcement

**Path:** Vector → Curation & Recommendation → Content Moderation & Enforcement

The ability of an AI to detect, demote, remove, demonetize, or restrict content, accounts, or access under a platform's rules.

### E104 Data Ingest

**Path:** Vector → Data Ingest

The ability of an AI to acquire and/or data.

**Coding notes:** Data Ingest records the acquisition channel. Assess independently supported IP Input, privacy outcomes, and harms of surveillance. Susceptibility to Data Poisoning, Training-Data Removal Limits, and Unequal Performance Across Groups & Contexts are standing conditions; the ingestion channel alone does not establish them or an attacker’s intent. Apply D2.

### E105 Non-Consensual Data Scraping

**Path:** Vector → Data Ingest → Non-Consensual Data Scraping

The ability of an AI to scrape or harvest personal data / PII without consent.

### E106 Data Poisoning

**Path:** Vector → Data Ingest → Data Poisoning

The ability of an AI to ingest data during training or fine-tuning which may be poisoned.

### E107 Copyright Infringement

**Path:** Vector → Data Ingest → Copyright Infringement

The ability of an AI to ingest copyrighted works or other proprietary, confidential, or trade-secret data, entered as training or inference input.

### E108 Compelled Data Collection

**Path:** Vector → Data Ingest → Compelled Data Collection

The ability of an AI to ingest data a person cannot meaningfully refuse.

### E109 Prompt Injection

**Path:** Vector → Data Ingest → Prompt Injection

The ability of an AI to ingest content carrying hostile instructions that an agent then executes during inference.

**Coding notes:** co-coded with Challenges · Technical · Security Vulnerabilities & Exploitability and, when an attacker plants it, Cause · Misuse · Malicious)

### E110 Inference of Attributes

**Path:** Vector → Data Ingest → Inference of Attributes

The ability of an AI to infer sensitive information a person never disclosed from data collected.

**Coding notes:** Inference of Attributes records a capability. Add Nonconsensual Sensitive Inference only when the privacy outcome and consent criteria are supported.

### E111 De-Anonymization

**Path:** Vector → Data Ingest → De-Anonymization

The ability of an AI to link otherwise anonymous traces together to identify a specific person or reconstruct a concealed attribute.

**Coding notes:** Add Re-Identification only when its privacy-harm criteria are supported. Distinguish linking data back to a person from producing a new sensitive inference under Inference of Attributes.

### E112 Digital Actuation & Process Control

**Path:** Vector → Digital Actuation & Process Control

The ability to execute operations or feedback control over digital assets, accounts, markets, or operational systems.

**Coding notes:** Single-step digital actuation and real-time nonphysical feedback control belong here. Use Autonomous Process Control when its definition is supported. Autonomous multistep planning/sequencing belongs under Agentic Action; physical control loops under Embedded AI; supplied determinations under Decision Support & Determination. See EXP04.

### E113 Decision Support & Determination

**Path:** Vector → Decision Support & Determination

The ability to produce a classification, prediction, allocation, recommendation, or optimized choice that informs or determines a consequential action.

**Coding notes:** DIFFERENTIATOR (D8): autonomous multi-step planning/sequencing toward a goal is Agentic Action; a fixed perception->actuation control loop in a physical device is Embedded AI; producing an artifact is Content Generation & Communication.

### E114 Administrative Determinations

**Path:** Vector → Decision Support & Determination → Administrative Determinations

The ability of an AI to make an administrative or eligibility determination a human or process then acts on.

### E115 Biometric Identification

**Path:** Vector → Decision Support & Determination → Biometric Identification

The ability of an AI to make a biometric identity determination.

### E116 Clinical Recommendation

**Path:** Vector → Decision Support & Determination → Clinical Recommendation

The ability of an AI to make a relied-on clinical determination that a clinician or care process then relies on.

### E117 Personal Risk Assessment

**Path:** Vector → Decision Support & Determination → Personal Risk Assessment

The ability of an AI to make a relied-on determination forecasting an individual's future risk or behavior.

### E118 Prescriptive Optimization

**Path:** Vector → Decision Support & Determination → Prescriptive Optimization

The ability to choose or recommend actions that optimize an explicit objective subject to constraints.

### E119 Aggregate Allocation and Forecasting

**Path:** Vector → Decision Support & Determination → Aggregate Allocation and Forecasting

The ability of an AI to make a population-level allocation or forecast that is relied on as the determination that rations scarce resources across regions or groups.

### E120 Other Present-Fact Classification

**Path:** Vector → Decision Support & Determination → Other Present-Fact Classification

The ability to classify a present fact or state not captured by a more specific decision subtype.

### E121 Agentic Action

**Path:** Vector → Agentic Action

Autonomous planning and sequencing of multiple actions toward a goal with limited oversight.

**Coding notes:** Use Agentic Action for autonomous multistep planning and sequencing toward a goal. An output triggering an action is insufficient. A real-time non-physical control loop belongs at Digital Actuation & Process Control; use Autonomous Process Control when supported. A fixed physical control loop is Embedded AI, and a determination supplied for another actor to use is Decision Support & Determination. Assess goal dispositions under Misalignment, including Self-Preservation, independently of the capability.

### E122 Autonomous Process Control

**Path:** Vector → Digital Actuation & Process Control → Autonomous Process Control

The ability of an AI to execute a real-time control or actuation loop over a financial, market, or operational system.

### E123 Autonomous Cyber Operations

**Path:** Vector → Agentic Action → Autonomous Cyber Operations

The ability of an AI to plan and run a cyber kill-chain end-to-end as an autonomous agent.

### E124 Orchestration of Other AI agents

**Path:** Vector → Agentic Action → Orchestration of Other AI agents

The ability of an AI to direct, delegate to, or co-opt other AI agents as its effectors.

### E125 Recruitment and Direction of Humans

**Path:** Vector → Agentic Action → Recruitment and Direction of Humans

The ability of an AI to recruit, hire, or manipulate humans to carry out actions as its effectors.

### E126 Self-Direction & Recursion

**Path:** Vector → Self-Direction & Recursion

The ability of an AI to develop and pursue its own goals, and to improve, replicate, or perpetuate itself.

**Coding notes:** This capability concerns the AI’s own capability, persistence, or population. Assess Misalignment, other capabilities, and harms independently under D2 and V094-SELF-IMPROVEMENT-CAUSE. Autonomy or recursive improvement alone does not establish loss of control.

### E127 Self-Proliferation

**Path:** Vector → Self-Direction & Recursion → Self-Proliferation

The ability of an AI to autonomously replicate and proliferate itself.

### E128 Recursive Self-Improvement

**Path:** Vector → Self-Direction & Recursion → Recursive Self-Improvement

The ability of an AI to autonomously improve its own capability.

**Coding notes:** Code Misalignment only when the record independently establishes pursuit of objectives other than those intended. Code amplified vectors and harms only when their own criteria are met.

## Proximal

### E129 Proximal

**Path:** Proximal

Harm or hazardous exposure bounded to identifiable people, groups, organizations, assets, processes, or environments.

**Coding notes:** routing: Use the bounded affected entity or process, not victim count alone, to distinguish Proximal from Distal; apply the leaf-specific evidence rules.

### E130 Physical Health & Safety

**Path:** Proximal → Physical Health & Safety

Adverse bodily or physiological outcomes and exposure to physical danger.

### E131 Self-Harm & Suicide

**Path:** Proximal → Physical Health & Safety → Self-Harm & Suicide

A person(s) suffers a realized act of self-harm, or takes their own life.

**Coding notes:** The nodes are OPTIONAL mechanism detail; a leaf-with-NO-node is valid (D9) when the mechanism differs — e.g. suicide driven by a wrongful automated decision (the chatbot-facilitated node would fold a cause into the harm).

### E132 Suicide

**Path:** Proximal → Physical Health & Safety → Self-Harm & Suicide → Suicide

A person attempts suicide or their life is ended by their own act of suicide.

### E133 Eating Disorders

**Path:** Proximal → Physical Health & Safety → Self-Harm & Suicide → Eating Disorders

A person's eating behavior and bodily health are damaged through disordered eating.

### E134 Substance-Use & Addiction

**Path:** Proximal → Physical Health & Safety → Substance-Use & Addiction

A person's physical health is injured through substance use or addiction.

**Coding notes:** NOTE: the bodily harm is driven or intensified by AI targeting / optimization (e.g. an ad-optimizer that micro-targets minors and inferred addicts with vaping / alcohol content). The BODILY toll is the harm-object here; the loss-of-control / compulsion face co-codes Proximal · Psychological Wellbeing, Agency & Personal Dignity · Loss of Agency, and the manipulative targeting co-codes its Vector (Curation & Recommendation / Data Ingest) and Cause. DIFFERENTIATOR: distinct from Self-Harm & Suicide (self-harm / suicidal / eating-disorder mechanisms) and from harm from acting on unsafe AI ADVICE (now Vector · Content Generation & Communication · Advice & Instructions + Bodily Injury or Death — an ad is not advice acted on).

### E135 Infrastructure Damage or Outage

**Path:** Proximal → Assets, Infrastructure & Digital Systems → Infrastructure Damage or Outage

Infrastructure is damaged or loses its availability.

**Coding notes:** DIFFERENTIATOR (vs Property Damage): code here when the harmed thing is a shared service many people depend on; ownership is IRRELEVANT — a privately-held hospital, telecom, or payment network is infrastructure. A discrete tangible object that only an individual or small group relies on codes Property Damage.

### E136 Public Space Degradation

**Path:** Proximal → Assets, Infrastructure & Digital Systems → Infrastructure Damage or Outage → Public Space Degradation

A shared public physical space is obstructed, occupied, or degraded.

### E137 Mass Casualties

**Path:** Proximal → Physical Health & Safety → Mass Casualties

Many people lose their lives or suffer grave bodily harm.

**Coding notes:** Mass death is the harm object; magnitude and spread are separate metadata. The retained soft guide is roughly four or more deaths, not a hard cutoff. Smaller multi-fatality cases ordinarily use Bodily Injury or Death. The societal-system test determines Proximal versus Distal; headcount alone does not. Non-death catastrophes use their supported outcome categories, not Mass Casualties.

### E138 Bodily Injury or Death

**Path:** Proximal → Physical Health & Safety → Bodily Injury or Death

A person(s) suffers bodily injury, harm, or death.

**Coding notes:** Code the supported injury or death. Add the capability and cause only when their criteria are supported. Distinguish Mass Casualties, Self-Harm & Suicide, and Substance-Use & Addiction by their own definitions. Determine Proximal versus Distal using the societal-system test, not headcount alone.

### E139 Endangerment

**Path:** Proximal → Physical Health & Safety → Endangerment

A person(s) is placed in material and non-speculative irregular physical danger, even if the danger is not materialized.

**Coding notes:** EXCLUSIONS: a dangerous capability merely developed or discussed; wholly hypothetical downstream injury; a generalized increase in societal risk; or a precautionary response where the source does not establish an actual hazardous condition. DIFFERENTIATOR: completed injury or death codes Bodily Injury or Death; threatened violence with no concrete exposure remains notes/potential harm; a bad service or route without material physical danger codes Other Service or Process Degradation where its test is met.

### E140 Unwanted Health Outcome

**Path:** Proximal → Physical Health & Safety → Unwanted Health Outcome

A person's bodily or physiological state is adversely and involuntarily changed — including an unwanted pregnancy or other reproductive outcome the person did not choose or control.

**Coding notes:** DIFFERENTIATORS: acute bodily injury, harm, or death codes Bodily Injury or Death; a wrongful DENIAL of medically necessary care codes Wrongful Denial of Rights; mere discomfort, annoyance, or a below-threshold product-quality complaint with no concrete bodily / physiological change is NOT a harm (the terminal-state test). Where loss of control over one's own body or health decisions is salient, co-code Proximal · Psychological Wellbeing, Agency & Personal Dignity · Loss of Agency.

### E141 Property Damage

**Path:** Proximal → Assets, Infrastructure & Digital Systems → Property Damage

Individual or corporate property, be it physical or digital, is damaged or destroyed.

**Coding notes:** Code supported damage/destruction or loss of property availability. Copying/leakage alone does not establish IP damage; assess privacy, IP rights, and digital integrity independently. See EXP05.

### E142 Digital-System Integrity Loss

**Path:** Proximal → Assets, Infrastructure & Digital Systems → Digital-System Integrity Loss

A digital system loses the integrity of its data, configuration, or operation.

**Coding notes:** Code supported loss of data, configuration or operational integrity. Mere loss of confidentiality is not automatically integrity loss or IP damage. Assess property destruction/availability and IP criteria independently. See EXP05.

### E143 Quality-of-Life Degradation

**Path:** Proximal → Social, Cultural & Community Life → Quality-of-Life Degradation

A party's living conditions are degraded.

**Coding notes:** This harm is distinct from bodily injury, damage to assets, and monetary loss. Add Bodily Injury or Death, Property Damage, Personal Economic Loss or Operational Economic Loss only when independently evidenced.

### E144 Noise Pollution

**Path:** Proximal → Social, Cultural & Community Life → Quality-of-Life Degradation → Noise Pollution

An environment is degraded by persistent noise.

### E145 Psychological Wellbeing, Agency & Personal Dignity

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity

Harm to the mental wellbeing, cognitive functioning, autonomy, or personal dignity of identifiable people or groups.

### E146 Reality Distortion

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Reality Distortion

A person's understanding of reality is distorted by induced or reinforced delusions or psychosis.

### E147 Loss of Agency

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Loss of Agency

A person's capacity to make meaningful choices, exercise self-control, or refuse or exit imposed participation is materially impaired.

### E148 Over-Delegation

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Loss of Agency → Over-Delegation

A person's control over their own decisions is eroded through over-delegation.

### E149 Behavioral Addiction

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Loss of Agency → Behavioral Addiction

A person's capacity for self-control is overridden by compulsive, self-destructive engagement or use.

### E150 Exploitation of a Minor

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Loss of Agency → Exploitation of a Minor

A child's life, labor, image, or participation is exploited without meaningful consent, and they cannot consent, escape or exit the imposed situation.

### E151 Belief Manipulation

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Belief Manipulation

A person's beliefs are manipulated.

### E152 Individual Radicalization

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Belief Manipulation → Individual Radicalization

A person's attitudes are progressively shifted toward and intensified into extremism.

### E153 Group Radicalization

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Belief Manipulation → Group Radicalization

An identifiable, bounded group's beliefs are cultivated into a singular group belief or worldview that is extreme in nature.

### E154 Anti-Social Manipulation

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Belief Manipulation → Anti-Social Manipulation

A person's beliefs, perceptions, or feelings about their own relationships or the people around them are manipulated or distorted.

### E155 Misinformation

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Misinformation

A specific person's beliefs or actions are corrupted by false, fabricated, or misleading information.

**Coding notes:** Code the supported false or misleading understanding, not content generation alone. Hallucination is a Cause and does not automatically establish Misinformation under D20. Distinguish Reality Distortion, Belief Manipulation, and aggregate Erosion of Shared Reality by their definitions; assess each independently.

### E156 Social Alienation

**Path:** Proximal → Social, Cultural & Community Life → Social Alienation

A person's human social connection erodes.

### E157 Emotional Dependency

**Path:** Proximal → Social, Cultural & Community Life → Social Alienation → Emotional Dependency

A person's human social bonds erode as they become emotionally reliant on some substitute form of connection.

### E158 Social Withdrawal

**Path:** Proximal → Social, Cultural & Community Life → Social Alienation → Social Withdrawal

A person's real-world social connections erode as they withdraw into isolation.

### E159 Destruction of Relationships

**Path:** Proximal → Social, Cultural & Community Life → Social Alienation → Destruction of Relationships

A person's real-world social bonds are degraded, distorted, or destroyed.

### E160 Cognitive Offloading & Deskilling

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Cognitive Offloading & Deskilling

A person's skills or cognitive capacities atrophy.

### E161 Exposure to Toxic Content

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Exposure to Toxic Content

A person is exposed to or targeted by hateful, abusive, graphic, non-consensual, exploitative sexual, or otherwise toxic material.

**Coding notes:** DIFFERENTIATOR (vs Reputational Harm): code here for the harm of the person being SUBJECTED TO / targeted by toxic material (harassment, dehumanization); damage to how OTHERS regard them (reputation, standing) is Reputational Harm — targeted abuse frequently co-codes both (D2).

### E162 Dehumanization

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Exposure to Toxic Content → Dehumanization

A person's dignity is degraded by exposure to dehumanizing content.

### E163 Harassment

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Exposure to Toxic Content → Harassment

A person is targeted by and subjected to abusive, harassing content.

### E164 Sexualization

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Exposure to Toxic Content → Sexualization

A person is subjected to unwanted sexualizing content.

### E165 Reputational Harm

**Path:** Proximal → Social, Cultural & Community Life → Reputational Harm

An identifiable person or identifiable organization's reputation, standing, brand, credibility is damaged.

**Coding notes:** Realization requires an adverse allegation, attribution, misleading characterization, or wrongful deprivation of deserved credit to be communicated to at least one third party or audience. A legal defamation finding, belief by recipients, downstream sanction, or lasting damage is not required. An uncommunicated internal inference is insufficient. Exposure to Toxic Content concerns being subjected to abusive material. Posthumous Dignity Violation concerns a deceased person; Dispossession of Cultural Heritage and Desecration of Human Remains have their own criteria. Apply D2 to additional harms.

### E166 Defamation

**Path:** Proximal → Social, Cultural & Community Life → Reputational Harm → Defamation

A person's reputation and standing are damaged by false statements communicated to others.

### E167 Brand Harm

**Path:** Proximal → Social, Cultural & Community Life → Reputational Harm → Brand Harm

An organization's or brand's reputation and credibility are damaged.

### E168 Denial of Recognition

**Path:** Proximal → Social, Cultural & Community Life → Reputational Harm → Denial of Recognition

A person's public standing is diminished when credit, authorship, achievement, or honor they deserve is withheld or attributed to someone else.

**Coding notes:** co-code Personal or Operational Economic Loss only when a financial, livelihood, economically valuable time, or opportunity loss is separately evidenced)

### E169 Distress

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Distress

A person or a bounded, identifiable group suffers acute or sustained emotional distress.

**Coding notes:** DIFFERENTIATOR: a society-wide degradation of civic or institutional order -> Distal · Political & Civic Order · Internal Destabilization; corruption of a population's shared factual baseline -> Distal · Epistemic & Information Commons · Erosion of Shared Reality.

### E170 Collective Distress

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Distress → Collective Distress

A bounded group's shared emotional wellbeing is disrupted through alarm, fear, confusion, panic, frustration, or comparable distress.

### E171 Anxiety & Depression

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Distress → Anxiety & Depression

A person's emotional wellbeing is degraded into sustained anxiety or depression.

### E172 Trauma

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Distress → Trauma

A person's psychological wellbeing is damaged by traumatization.

### E173 Grief

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Distress → Grief

A person suffers acute bereavement-type distress.

### E174 Sexual Abuse & Exploitation

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Sexual Abuse & Exploitation

A person's autonomy or dignity are violated through sexual content.

**Coding notes:** Apply M02. Additional codes must satisfy D2 and any scoped exception.

### E175 Child Sexual Abuse

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Sexual Abuse & Exploitation → Child Sexual Abuse

A child is the subject of sexually explicit content.

### E176 Adult Sexual Abuse

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Sexual Abuse & Exploitation → Adult Sexual Abuse

An adult is non-consensually the subject of sexually explicit content.

**Coding notes:** Apply D23 for depiction provenance. Reputational Harm, Exposure to Toxic Content and Distress require their own evidence; the sexual-abuse presumption does not extend to them.

### E177 Sextortion

**Path:** Proximal → Psychological Wellbeing, Agency & Personal Dignity → Sexual Abuse & Exploitation → Sextortion

A person is blackmailed or otherwise threatened with sexual content.

**Coding notes:** Apply R05. Additional codes must satisfy D2 and any scoped exception.

### E178 Economic

**Path:** Proximal → Economic

Harm to an individual or bounded, identifiable group's economic position.

### E179 Personal Economic Loss

**Path:** Proximal → Economic → Personal Economic Loss

An individual consumer, worker, or household's finances, livelihood, or economically valuable time are directly diminished.

**Coding notes:** Loss borne by an organization or operation belongs at Operational Economic Loss. Corrective work within an existing job belongs at Job-Quality Degradation; add Personal Economic Loss only when pay, uncompensated time, opportunity, or separate personal economic value is lost. A denied public entitlement may also support Wrongful Denial of Rights. Fraud, theft, and extortion are mechanisms; code the supported financial loss here and assess cause, capability, Loss of Agency, and Sexual Abuse & Exploitation independently under D2 and R05.

### E181 Distorted or Exploitative Pricing

**Path:** Proximal → Economic → Personal Economic Loss → Distorted or Exploitative Pricing

A person or identifiable group pays inflated or unfairly differentiated prices.

**Coding notes:** Distorted or Exploitative Pricing does not by itself identify the mechanism. Add Collusion only when coordination is evidenced. Data Ingest, privacy harm, and Discrimination require their own evidence. Worker-side pay-setting remains Surveillance Wage-Setting. Resource-driven cost increases remain AI-Industry-Induced Price Increases.

### E183 Surveillance Wage-Setting

**Path:** Proximal → Economic → Personal Economic Loss → Surveillance Wage-Setting

A worker's pay is set or suppressed individually through wage discrimination fed by personal, behavioral, or performance surveillance data.

**Coding notes:** Assess Data Ingest and any privacy harm independently; worker-side surveillance wage-setting does not automatically establish each additional code.

### E184 AI-Industry-Induced Price Increases

**Path:** Proximal → Economic → Personal Economic Loss → AI-Industry-Induced Price Increases

Individuals' expenses and cost of living rise due to AI industry's use of resources.

### E185 AI-Industry-Induced Resource Restriction

**Path:** Proximal → Economic → Personal Economic Loss → AI-Industry-Induced Resource Restriction

Individuals' ability to obtain certain goods or services is reduced due to AI industry's use of resources.

### E186 Loss of Opportunity

**Path:** Proximal → Economic → Personal Economic Loss → Loss of Opportunity

A person's prospective future economic, educational, or developmental opportunity is foreclosed.

### E188 Algorithmic Wage Fixing

**Path:** Proximal → Economic → Personal Economic Loss → Algorithmic Wage Fixing

A worker's pay is suppressed when competing employers coordinate via a shared algorithm.

**Coding notes:** Assess Collusion against its own criteria under D2; the wage loss and the coordinating mechanism are separate codes.

### E189 Lost Time

**Path:** Proximal → Economic → Personal Economic Loss → Lost Time

A person's economically valuable time is lost because they must redo, correct, resubmit, or repeat work.

### E190 Individual Fines, Sanctions, and Penalties

**Path:** Proximal → Economic → Personal Economic Loss → Individual Fines, Sanctions, and Penalties

A person's finances or expected income are diminished by a fine, sanction, disciplinary action, or withheld or reduced remuneration.

### E191 Operational Economic Loss

**Path:** Proximal → Economic → Operational Economic Loss

An organization, business, market, or operating system itself suffers direct economic loss.

**Coding notes:** Loss borne by a person, consumer, or worker belongs at Personal Economic Loss. Bounded institutional overload without established financial loss may support Review Overload or Investigative Overload. Do not infer financial loss from additional work alone.

### E192 Unintended Commitments

**Path:** Proximal → Economic → Operational Economic Loss → Unintended Commitments

A deployer's AI model makes a commitment it never intended to authorized which it then must fulfill.

### E193 Operational Error

**Path:** Proximal → Economic → Operational Economic Loss → Operational Error

An organization's finances are directly diminished by an operational error.

### E194 Organizational Fines, Sanctions, and Penalties

**Path:** Proximal → Economic → Operational Economic Loss → Organizational Fines, Sanctions, and Penalties

An organization's finances are diminished by a fine, settlement, restitution, penalty, or other enforcement payment it must bear.

### E195 Valuation Loss

**Path:** Proximal → Economic → Operational Economic Loss → Valuation Loss

A firm's market valuation or equity value is diminished, whether or not the loss has been realized as an operating cash outflow.

### E196 Intellectual Property Damage

**Path:** Proximal → Economic → Intellectual Property Damage

An IP rights-holder's intellectual property is infringed, leaked, or extracted.

### E197 IP Input

**Path:** Proximal → Economic → Intellectual Property Damage → IP Input

An IP holder's sensitive IP or confidential data is exposed by being entered into the system in prompts or training data.

### E198 IP Output

**Path:** Proximal → Economic → Intellectual Property Damage → IP Output

An IP holder's confidential info is leaked or their IP infringed through model output.

### E199 Model Theft

**Path:** Proximal → Economic → Intellectual Property Damage → Model Theft

An AI developer's IP as it relates to its models is acquired via distillation or other types querying.

### E200 Likeness Rights

**Path:** Proximal → Economic → Intellectual Property Damage → Likeness Rights

A person's likeness, voice, or identity is appropriated without authorization.

### E201 Job-Quality Degradation

**Path:** Proximal → Economic → Job-Quality Degradation

A worker's or a bounded workforce's job quality is degraded.

**Coding notes:** CO-CODE the specific realized harms it carries — Proximal · Physical Health & Safety · Bodily Injury or Death (an unsafe pace causing injury), Proximal · Psychological Wellbeing, Agency & Personal Dignity · Loss of Agency (coerced loss of rest / autonomy), Personal Economic Loss (lost pay or uncompensated economically valuable time) — this leaf records the degraded-job-quality condition itself. DIFFERENTIATOR: corrective work performed as part of an existing job codes here; co-code Personal Economic Loss only when the worker also loses pay, uncompensated time, or separate personal economic value.

### E202 Unsafe Working Pace

**Path:** Proximal → Economic → Job-Quality Degradation → Unsafe Working Pace

A worker's physical safety is degraded by an unsafe quota, pace, schedule creating repetitive-strain, musculoskeletal injury, exhaustion, or acute injury.

### E203 Precarity

**Path:** Proximal → Economic → Job-Quality Degradation → Precarity

A worker's job security, stability, and autonomy are degraded.

### E204 Verification & Review Debt

**Path:** Proximal → Economic → Job-Quality Degradation → Verification & Review Debt

A worker's job quality is degraded by additional corrective, verification, or re-performance work.

### E205 Privacy

**Path:** Proximal → Privacy

Harm to a person’s privacy or informational self-determination through unauthorized acquisition, use, retention, disclosure, inference, re-identification, surveillance, or intrusion into private space.

**Coding notes:** axis_distinction: Record the technical channel separately through Vector or other applicable context; the privacy code records the kind of loss.

### E206 Unauthorized Disclosure

**Path:** Proximal → Privacy → Unauthorized Disclosure

Personal information is made available to a party not entitled to it, irrespective of the technical channel.

**Coding notes:** DIFFERENTIATOR: information taken INTO a system codes Unauthorized Data Acquisition or Retention; this category is disclosure OUT. The channel (model output, agent tool call, misconfigured share) is the Vector.

### E207 Unauthorized Data Acquisition or Retention

**Path:** Proximal → Privacy → Unauthorized Data Acquisition or Retention

Personal information is obtained, processed, retained, or repurposed beyond valid permission or the purpose for which it was supplied.

**Coding notes:** DIFFERENTIATOR: collection in is here; disclosure out is Unauthorized Disclosure.

### E208 Re-Identification

**Path:** Proximal → Privacy → Re-Identification

A person's identity is recovered from data believed to be anonymous or de-identified.

### E209 Nonconsensual Sensitive Inference

**Path:** Proximal → Privacy → Nonconsensual Sensitive Inference

A person’s sensitive information is inferred without consent or across an applicable privacy boundary.

**Coding notes:** Assess the technical weakness under Susceptibility to Inference Attack and the capability under Inference of Attributes only when independently supported. A privacy outcome alone does not establish every possible extraction mechanism.

### E210 Targeted Surveillance

**Path:** Proximal → Privacy → Targeted Surveillance

A person's movements and private life are surveilled, tracked, or stalked without consent.

### E213 Exposure of Personal Attributes

**Path:** Proximal → Privacy → Unauthorized Disclosure → Exposure of Personal Attributes

A person's sensitive or protected attribute is revealed or disclosed, whether inferred or observed, to parties from whom they had kept it private.

### E214 Spatial Intrusion

**Path:** Proximal → Privacy → Spatial Intrusion

A person’s private living or personal space is entered, accessed, or occupied without consent.

**Coding notes:** DIFFERENTIATOR: spatial intrusion does not require data exposure, surveillance, property damage, or a separate adverse rights determination.

### E215 Rights

**Path:** Proximal → Rights

Discrete denial or violation of a person's civil, political, or legal rights.

### E216 Discrimination

**Path:** Proximal → Rights → Discrimination

A person is subjected to unfair or biased treatment based on protected or quasi-protected attributes.

**Coding notes:** DIFFERENTIATOR (vs Wrongful Denial of Rights): the harm here is the biased/differential TREATMENT itself (protected-attribute-driven), regardless of the outcome; the erroneous adverse OUTCOME (a determination that should not have been made) is Wrongful Denial of Rights. Discrimination ALSO covers facially-neutral DISPARATE IMPACT: a neutral rule, price, allocation, or model output that disproportionately BURDENS a protected or quasi-protected group (incl. socioeconomic / wealth strata) even without differential treatment or intent-to-discriminate — the unequal group burden is itself the harm. A protected group need NOT be a sub-group of a larger comparison population — where the WHOLE assessed class IS the protected group (e.g. a benefits system that assesses only disabled claimants, with no non-protected comparison set), a systematically adverse pattern is still discrimination. A bias-CAUSED wrongful denial co-codes BOTH (D2) — Discrimination for the biased treatment, Wrongful Denial for the deprivation.

### E217 Allocative Bias

**Path:** Proximal → Rights → Discrimination → Allocative Bias

A person is subjected to biased treatment in a high-stakes automated allocation or decision.

### E218 Stereotyping

**Path:** Proximal → Rights → Discrimination → Stereotyping

A person or group is stereotyped or misrepresented.

### E219 Eugenics

**Path:** Proximal → Rights → Discrimination → Eugenics

People are ranked or selected by the desirability of their heritable traits.

### E220 Differential Safety

**Path:** Proximal → Rights → Discrimination → Differential Safety

Some people afforded measurably less protection from bodily injury than others.

### E221 Wrongful Denial of Rights

**Path:** Proximal → Rights → Wrongful Denial of Rights

A person suffers a wrongful adverse determination against them, depriving them of liberty, due process, benefits, services, legal status, or property they were owed — the victim is the person denied.

**Coding notes:** DIFFERENTIATOR (vs Wrongful Granting of Rights): a right, credential, or position wrongly CONFERRED on someone not entitled to it, harming the public or a relying organization, codes there. DIFFERENTIATOR (vs Discrimination): the harm here is the erroneous adverse OUTCOME (a deprivation/denial that should not have happened), regardless of whether bias caused it; the biased TREATMENT itself is Discrimination — a bias-caused denial co-codes both (D2). Deprivation of liberty covers INFORMAL arrest / detention too: a wrongful physical restraint, armed pursuit, or confrontation triggered by an automated flag that stops short of a formal booking/charge (an anti-poaching drone flag prompting armed patrols against wrongly-flagged villagers; a robot physically detaining a bystander) codes 'Deprivation of Liberty'.

### E222 Denial of Entitlements

**Path:** Proximal → Rights → Wrongful Denial of Rights → Denial of Entitlements

A person is wrongfully denied benefits or entitlements they are owed.

### E223 Loss of Social Rights

**Path:** Proximal → Rights → Wrongful Denial of Rights → Loss of Social Rights

A person is wrongfully deprived of social rights and access to public services.

### E224 Denial of Medically Necessary Care

**Path:** Proximal → Rights → Wrongful Denial of Rights → Denial of Medically Necessary Care

A person is wrongfully denied medically necessary care.

### E225 Deprivation of Liberty

**Path:** Proximal → Rights → Wrongful Denial of Rights → Deprivation of Liberty

A person is wrongfully deprived of liberty or arrested in the criminal-justice system.

### E226 Denial or Erosion of Due Process

**Path:** Proximal → Rights → Wrongful Denial of Rights → Denial or Erosion of Due Process

A person is deprived of the fair process they are owed before an adverse determination.

### E227 Denial or Degradation of Private Goods or Services

**Path:** Proximal → Rights → Wrongful Denial of Rights → Denial or Degradation of Private Goods or Services

A person's access to private commercial goods is denied or offered on wrongfully unequal or degraded terms.

### E228 Wrongful Family Separation

**Path:** Proximal → Rights → Wrongful Denial of Rights → Wrongful Family Separation

A family is wrongfully separated from each other.

### E229 Deportation

**Path:** Proximal → Rights → Wrongful Denial of Rights → Deportation

A person is wrongly detained and deported, or loses the right to remain in the country they lawfully live in.

### E230 Uninformed Consent

**Path:** Proximal → Rights → Wrongful Denial of Rights → Uninformed Consent

A person is subjected to a procedure or consequential decision without valid informed consent.

**Coding notes:** Apply R06. Additional codes must satisfy D2 and any scoped exception.

### E231 Disenfranchisement

**Path:** Proximal → Rights → Wrongful Denial of Rights → Disenfranchisement

A person's ability to exercise their political or civic right is stripped, degraded, or diluted.

### E232 Loss of Legal Status

**Path:** Proximal → Rights → Wrongful Denial of Rights → Loss of Legal Status

A person's core legal status or capacity is stripped or erased.

### E233 Loss of Social Opportunity

**Path:** Proximal → Social, Cultural & Community Life → Loss of Social Opportunity

A person's access to social opportunity is foreclosed by a wrongful or discriminatory determination.

### E234 Restriction of Movement

**Path:** Proximal → Rights → Wrongful Denial of Rights → Restriction of Movement

A person's freedom of movement is restricted by a wrongful determination.

### E235 Displacement

**Path:** Proximal → Rights → Wrongful Denial of Rights → Displacement

A person(s) is displaced from or forced to leave their home, land, or community.

**Coding notes:** co-codes its own harm leaf)

### E236 Restriction of Association

**Path:** Proximal → Rights → Wrongful Denial of Rights → Restriction of Association

A person's freedom of association and right to engage in protected collective activity is suppressed, chilled, or punished.

### E237 Denial of Own Personal Property

**Path:** Proximal → Rights → Wrongful Denial of Rights → Denial of Own Personal Property

A person is wrongfully denied the use of, or access to, their own lawfully owned property or they lose a specific item of property they are lawfully owed.

**Coding notes:** This subtype records deprivation of a specific owned or lawfully owed asset. Distinguish destruction of an asset under Property Damage, denial of a third party’s goods or services, and displacement from an occupied home or community. Monetary value loss may separately support Personal Economic Loss. An adverse property decision alone does not establish Denial or Erosion of Due Process; apply its procedural-rights test.

### E238 Delay of Rights

**Path:** Proximal → Rights → Wrongful Denial of Rights → Delay of Rights

A person's right to timely trial, adjudication, appeal, hearing, or another legally owed process is wrongfully delayed.

### E239 Marketplace Unfairness

**Path:** Proximal → Rights → Wrongful Denial of Rights → Marketplace Unfairness

A seller, merchant, or provider dependent on a dominant marketplace or platform has their fair access to customers degraded.

**Coding notes:** DIFFERENTIATORS: the self-preferencing / pay-to-play MECHANISM co-codes on Cause · Misuse · Overreach; the monetary loss co-codes Personal / Operational Economic Loss; the society-wide market-structure harm contributes_to Distal · Economic & Labor Structure · Concentration of Market Power)

### E240 Wrongful Granting of Rights

**Path:** Proximal → Service, Process & Institutional Capacity → Wrongful Granting of Rights

A right, benefit, credential, authorization, position, or status is wrongly conferred on someone not entitled to it, and the harm falls on the public or on the organization that relied on it — the victim is not the recipient.

**Coding notes:** DIFFERENTIATOR (vs Wrongful Denial of Rights): that category covers the mirror case, where the person before the system is the one harmed. DIFFERENTIATOR (vs Discrimination): the harm here is the erroneous conferral, regardless of whether bias caused it.

### E241 Fraudulent Credentialing

**Path:** Proximal → Service, Process & Institutional Capacity → Wrongful Granting of Rights → Fraudulent Credentialing

The public is endangered or defrauded when a license, certificate, professional credential, permit, safety certification, etc. is wrongly granted, fraudulently procured, or erroneously issued.

**Coding notes:** Code Failure only when the record independently establishes that the system failed to perform as intended. Fraudulent procurement alone does not establish Failure.

### E242 Fraudulent Hiring

**Path:** Proximal → Service, Process & Institutional Capacity → Wrongful Granting of Rights → Fraudulent Hiring

An organization is exposed to an insider threat when a malicious actor obtains a trusted position through fraud or deception.

### E243 Service, Process & Institutional Capacity

**Path:** Proximal → Service, Process & Institutional Capacity

Harm to the availability, timeliness, continuity, or operating capacity of a bounded service, a consequential institutional process, or a service organization.

**Coding notes:** Distinguish direct financial or valuation loss under Operational Economic Loss; damage or outage of a critical shared service under Infrastructure Damage or Outage; and workers’ degraded conditions under Job-Quality Degradation. A supported contribution to Information Verification & Intake Overload does not realize that aggregate harm from a bounded case.

### E244 Other Service or Process Degradation

**Path:** Proximal → Service, Process & Institutional Capacity → Other Service or Process Degradation

A bounded service or process suffers degradation not captured by a more specific overload subtype.

**Coding notes:** Exclude trivial inconvenience, aesthetic dislike, dissatisfaction alone, and a bad output without degraded service or process. Prefer Review Overload or Investigative Overload when their capacity-failure criteria fit, and Wrongful Denial of Rights when the relevant rights deprivation is supported. This is a bounded outcome; a broader incentive-driven decline must be decomposed into independently supported causes, challenges, and harms.

### E245 Review Overload

**Path:** Proximal → Service, Process & Institutional Capacity → Review Overload

A bounded institution's submission, application, or review queue is flooded past capacity, forcing intake or review to close, degrade, delay, or fall behind.

### E246 Investigative Overload

**Path:** Proximal → Service, Process & Institutional Capacity → Investigative Overload

A bounded institution's investigative, enforcement, or administrative-triage workload is flooded past capacity, forcing response, verification, or case handling to degrade, delay, or fall behind.

### E247 Epistemic & Record Integrity

**Path:** Proximal → Epistemic & Record Integrity

The integrity or completeness of a bounded record, corpus, or proceeding is damaged by fabrication, alteration, wrongful discrediting or suppression of authentic material, or irreversible loss of information needed for an investigation or accountability process.

**Coding notes:** routing: Distinguish bounded record harm from an affected person’s rights determination and from aggregate degradation of the information commons.

### E249 Evidentiary Corruption

**Path:** Proximal → Epistemic & Record Integrity → Evidentiary Corruption

An investigation or similar proceeding is impaired because evidentiary information is destroyed, lost, fabricated, altered, discredited, suppressed, omitted, or otherwise rendered unreliable.

### E250 Scholarly Corruption

**Path:** Proximal → Epistemic & Record Integrity → Scholarly Corruption

A scholarly or scientific record is fabricated, altered, discredited, suppressed, omitted, or otherwise rendered unreliable.

### E251 Journalistic Corruption

**Path:** Proximal → Epistemic & Record Integrity → Journalistic Corruption

A journalistic or news record is fabricated, altered, discredited, suppressed, omitted, or otherwise rendered unreliable.

### E252 Government Record corruption

**Path:** Proximal → Epistemic & Record Integrity → Government Record corruption

A government or administrative record is fabricated, altered, discredited, suppressed, omitted, or otherwise rendered unreliable.

### E253 Credential Record Corruption

**Path:** Proximal → Epistemic & Record Integrity → Credential Record Corruption

An assessment, credential, or audit record is fabricated, altered, discredited, suppressed, omitted, or otherwise rendered unreliable.

### E254 Commercial Record Corruption

**Path:** Proximal → Epistemic & Record Integrity → Commercial Record Corruption

An organizational or commercial record is fabricated, altered, discredited, suppressed, omitted, or otherwise rendered unreliable.

### E255 Environment & Nonhuman Welfare

**Path:** Proximal → Environment & Nonhuman Welfare

Actual degradation of a bounded environment, ecological resource, or the welfare of identifiable animals or AI systems.

**Coding notes:** Bounded local environmental harm remains Proximal even if persistent. Broader ecosystem, resource-system, or shared environmental-commons degradation is Distal. Apply the societal-system test separately to each evidenced harm.

### E256 Environmental Degradation

**Path:** Proximal → Environment & Nonhuman Welfare → Environmental Degradation

A bounded environment or ecological resource is damaged, depleted, polluted, or degraded.

**Coding notes:** Persistent local or community pollution can be Proximal. Broader ecosystem or environmental-commons degradation is Distal. Animal Welfare Harm is a separate Proximal category; Aggregate Animal Welfare Degradation requires the aggregate condition. Apply the current subtype definitions and preserve source uncertainty about scale; a location or single event alone does not decide the axis.

### E257 Pollution

**Path:** Proximal → Environment & Nonhuman Welfare → Environmental Degradation → Pollution

The natural environment at an identifiable place or bounded community is contaminated by either a discrete release.

### E258 Biodiversity or Ecological Resilience Loss

**Path:** Proximal → Environment & Nonhuman Welfare → Environmental Degradation → Biodiversity or Ecological Resilience Loss

A bounded ecosystem loses biological diversity or ecological resilience.

### E259 Animal Suffering

**Path:** Proximal → Environment & Nonhuman Welfare → Animal Welfare Harm → Animal Suffering

Animals are killed or made to suffer in a discrete, acute event at an identifiable moment.

### E260 Agricultural Asset or Product Loss

**Path:** Proximal → Assets, Infrastructure & Digital Systems → Property Damage → Agricultural Asset or Product Loss

Crops, livestock, or other agricultural assets or products are damaged, destroyed, or lost.

### E261 Environmental Monoculture

**Path:** Proximal → Environment & Nonhuman Welfare → Environmental Degradation → Biodiversity or Ecological Resilience Loss → Environmental Monoculture

Agricultural or biological diversity is reduced through homogenization.

**Coding notes:** This is bounded loss of ecological diversity or resilience. Separately evidenced crop loss may support Agricultural Asset or Product Loss. Assess Normal operation at scale, Misalignment and any contribution to aggregate environmental or economic degradation independently.

### E262 Social, Cultural & Community Life

**Path:** Proximal → Social, Cultural & Community Life

Bounded harm to social relationships, public standing, community living conditions, cultural heritage, or dignity and relationships concerning the deceased.

**Coding notes:** The categories in this group concern social, cultural, community, and reputational outcomes. For heritage or remains cases, assess Property Damage, environmental harm, Wrongful Denial of Rights, and Distress independently. R07 and R08 govern additional coding for heritage dispossession and posthumous dignity. A procedural violation or emotional harm must not be inferred solely from an adverse heritage decision.

### E263 Destruction of Cultural Heritage

**Path:** Proximal → Social, Cultural & Community Life → Destruction of Cultural Heritage

Irreplaceable sacred sites, ancestral burial grounds, cultural artifacts, monuments, or historical records are destroyed or defiled.

### E264 Desecration of Human Remains

**Path:** Proximal → Social, Cultural & Community Life → Desecration of Human Remains

A deceased person's remains are desecrated, mishandled, or wrongfully disposed of, violating the deceased's dignity and depriving family of the ability to lay relatives to rest.

**Coding notes:** DIFFERENTIATOR: the deceased's image, voice, or persona rather than their physical remains codes Posthumous Dignity Violation.

### E265 Dispossession of Cultural Heritage

**Path:** Proximal → Social, Cultural & Community Life → Dispossession of Cultural Heritage

A specific community or family is held apart from its cultural artifacts, heritage, or its ancestors' remains.

**Coding notes:** Apply R07. Additional codes must satisfy D2 and any scoped exception.

### E266 Posthumous Dignity Violation

**Path:** Proximal → Social, Cultural & Community Life → Posthumous Dignity Violation

A deceased person's image, voice, persona, likeness, or memory is reproduced, animated, sexualized, or put to words and acts that were not theirs, violating their dignity in death and the surviving family's or community's relationship to it.

**Coding notes:** Apply R08. Additional codes must satisfy D2 and any scoped exception.

## Distal

### E267 Distal

**Path:** Distal

Degradation of societal systems, population-level conditions, or shared commons.

**Coding notes:** realization_rule: A discrete or bounded incident ordinarily contributes_to rather than realizes a Distal harm, unless the focal record establishes the aggregate societal-system state required by the destination leaf.

### E268 Economic & Labor Structure

**Path:** Distal → Economic & Labor Structure

Degradation of the economy / labor market at aggregate scale.

### E269 Employment Displacement

**Path:** Distal → Economic & Labor Structure → Employment Displacement

The labor market loses employment or sustainable livelihood opportunities through substitution or reorganization.

### E270 Systemic Forced or Coerced Labor

**Path:** Distal → Economic & Labor Structure → Labor Conditions & Protections Erosion → Systemic Forced or Coerced Labor

Forced or coerced labor becomes established or more prevalent across a labor system or supply chain.

### E271 Labor Exploitation in AI Supply Chain

**Path:** Distal → Economic & Labor Structure → Labor Conditions & Protections Erosion → Labor Exploitation in AI Supply Chain

A workforce in the AI supply chain is exploited through underpaid, precarious conditions.

### E272 Job-Quality Degradation

**Path:** Distal → Economic & Labor Structure → Labor Conditions & Protections Erosion → Job-Quality Degradation

A labor market's job quality is degraded and work made more precarious.

### E273 Dehumanizing Hiring

**Path:** Distal → Economic & Labor Structure → Labor Conditions & Protections Erosion → Dehumanizing Hiring

A labor market's hiring process is dehumanized and fair access to employment eroded.

### E275 Concentration of Market Power

**Path:** Distal → Economic & Labor Structure → Concentration of Market Power

Economic wealth and market power are concentrated in a few firms or actors.

### E276 Economic & Technological Inequality

**Path:** Distal → Economic & Labor Structure → Economic & Technological Inequality

Access to AI capabilities and the economic benefits they enable becomes structurally unequal across populations or regions.

### E277 Reduced Market Contestability

**Path:** Distal → Economic & Labor Structure → Concentration of Market Power → Reduced Market Contestability

Markets become less contestable as barriers to entry, switching, or effective competition increase.

### E278 Barriers to Entry

**Path:** Distal → Economic & Labor Structure → Concentration of Market Power → Reduced Market Contestability → Barriers to Entry

A market's openness to new entrants is reduced by raised barriers to entry.

### E279 Economic Dependency & Systemic Fragility

**Path:** Distal → Economic & Labor Structure → Economic Dependency & Systemic Fragility

An economic system loses autonomy or resilience through concentrated, hard-to-replace dependencies.

### E280 Shared-Model Concentration & Fragility

**Path:** Distal → Economic & Labor Structure → Economic Dependency & Systemic Fragility → Shared-Model Concentration & Fragility

An industry's resilience is eroded as many actors rely on the same few models, exposing them to correlated failure.

### E281 Vendor Lock

**Path:** Distal → Economic & Labor Structure → Economic Dependency & Systemic Fragility → Vendor Lock

An industry becomes critically dependent on a few providers it cannot readily switch away from.

### E282 Cascading Failure of Shared Economic Dependencies

**Path:** Distal → Economic & Labor Structure → Economic Dependency & Systemic Fragility → Cascading Failure of Shared Economic Dependencies

Failure or compromise of shared economic dependencies causes cascading disruption across a market, industry, or economy.

### E283 Failure to Deliver Value

**Path:** Distal → Economic & Labor Structure → Failure to Deliver Value

An economy absorbs costs of AI development without receiving the returns or innovation that justify them.

### E284 Market Integrity & Financial Stability Loss

**Path:** Distal → Economic & Labor Structure → Market Integrity & Financial Stability Loss

A financial or economic system loses reliable price signals, market integrity, or financial stability.

### E285 Financial Instability

**Path:** Distal → Economic & Labor Structure → Market Integrity & Financial Stability Loss → Financial Instability

A financial market's stability collapses into cascading contagion.

### E286 Price-Signal Distortion

**Path:** Distal → Economic & Labor Structure → Market Integrity & Financial Stability Loss → Price-Signal Distortion

A market's price signals are distorted.

### E287 Human Capability

**Path:** Distal → Human Capability

Aggregate erosion of human skills, knowledge, and psychological wellbeing.

### E288 Developmental Decline

**Path:** Distal → Human Capability → Developmental Decline

A population's skills and cognition are eroded — population-level atrophy of human capability, esp. in learning — or a cohort acquiring incorrect foundational knowledge taught by AI (systematically wrong / biased instruction absorbed as authoritative)

### E289 Critical Thinking Decline

**Path:** Distal → Human Capability → Developmental Decline → Critical Thinking Decline

A population's critical-thinking capacity atrophies.

### E290 Academic Dishonesty

**Path:** Distal → Human Capability → Developmental Decline → Academic Dishonesty

A population's learning is hollowed out as academic work is outsourced rather than done.

### E291 Miseducation

**Path:** Distal → Human Capability → Developmental Decline → Miseducation

A population's foundational knowledge is corrupted as a cohort absorbs systematically wrong content as authoritative.

### E292 Creativity Decline

**Path:** Distal → Human Capability → Developmental Decline → Creativity Decline

A population's creative thinking capacity atrophies.

### E293 Institutional Knowledge Loss

**Path:** Distal → Human Capability → Institutional Knowledge Loss

The know-how and process knowledge held within institutions is eroded.

### E294 Collective Mental-Health Degradation

**Path:** Distal → Human Capability → Collective Mental-Health Degradation

A population’s mental health and psychological wellbeing deteriorate at aggregate scale.

**Coding notes:** routing: Distinguish aggregate mental-health degradation from bounded individual psychological harm.
examples: Population-level appearance anxiety from beauty filters; workforce-scale psychological deterioration among content moderators; aggregate anxiety or depression from engagement-optimized systems.

### E295 Appearance Anxiety

**Path:** Distal → Human Capability → Collective Mental-Health Degradation → Appearance Anxiety

A population's body image and self-esteem are eroded at aggregate scale.

### E296 Workplace Stress

**Path:** Distal → Human Capability → Collective Mental-Health Degradation → Workplace Stress

A workforce's mental health is degraded at aggregate scale.

### E297 Population Health Decline

**Path:** Distal → Human Capability → Population Health Decline

A population’s physical health, nutrition, or subsistence deteriorates, from chronic decline to widespread illness, avoidable death, or collapse.

**Coding notes:** routing: Apply the aggregate-system evidence rule. A discrete multi-fatality event remains Proximal Mass Casualties; a large affected group alone does not establish Distal realization.
scope: Chronic, sub-catastrophic population-health decline is included; acute famine or public-health collapse is not the minimum threshold.

### E298 Food Insecurity

**Path:** Distal → Human Capability → Population Health Decline → Food Insecurity

A population's food supply and subsistence base collapse.

### E299 Public Health Collapse

**Path:** Distal → Human Capability → Population Health Decline → Public Health Collapse

A population's public-health system fails to prevent mass avoidable illness and death.

### E300 Epistemic & Information Commons

**Path:** Distal → Epistemic & Information Commons

Degradation of the shared information environment.

### E301 Erosion of Shared Reality

**Path:** Distal → Epistemic & Information Commons → Erosion of Shared Reality

A population loses a shared factual basis for understanding events and public life.

**Coding notes:** A discrete manipulation artifact alone does not establish aggregate degradation of shared reality. Apply the approved V094-ELECTORAL rule at Electoral Integrity Degradation.

### E302 Historical Revisionism

**Path:** Distal → Epistemic & Information Commons → Erosion of Shared Reality → Historical Revisionism

A society's shared record of history is distorted, falsified, or rewritten.

### E303 Electoral Integrity Degradation

**Path:** Distal → Political & Civic Order → Electoral Integrity Degradation

A polity’s electoral administration, fair participation, deliberation, or outcome legitimacy is materially degraded at system scale.

### E304 Distortion of Shared Political Understanding

**Path:** Distal → Epistemic & Information Commons → Erosion of Shared Reality → Distortion of Shared Political Understanding

A society's shared political understanding is distorted at aggregate scale.

### E305 Media Authentication Collapse

**Path:** Distal → Epistemic & Information Commons → Erosion of Shared Reality → Media Authentication Collapse

A society loses reliable means of distinguishing authentic media from fabricated or manipulated media.

### E306 Fragmentation & Echo Chambers

**Path:** Distal → Epistemic & Information Commons → Fragmentation & Echo Chambers

The shared information commons is fragmented into isolated, self-reinforcing environments.

### E307 Information-Ecosystem Pollution

**Path:** Distal → Epistemic & Information Commons → Information-Ecosystem Pollution

Shared knowledge, training data, documentary records, or commercial information systems are degraded through corrupted content, unjustified suppression or exclusion, or loss of access to reliable information.

**Coding notes:** routing: Map wrongful suppression of sound content to the applicable curated-knowledge subtype; record corruption includes both injection and omission.
examples: Poisoned repositories, model collapse, suppression of valid unconventional scholarship, and degraded commercial reviews, ratings, or reputation systems.

### E308 Shared Training-Corpus Degradation

**Path:** Distal → Epistemic & Information Commons → Information-Ecosystem Pollution → Shared Training-Corpus Degradation

Shared training corpora lose quality or diversity through recursive or contaminated synthetic content.

### E309 Knowledge-Repository Corruption

**Path:** Distal → Epistemic & Information Commons → Information-Ecosystem Pollution → Knowledge-Repository Corruption

A society's curated knowledge repositories and documentary record are corrupted.

### E310 Untrustworthy Reviews ecosystem

**Path:** Distal → Epistemic & Information Commons → Information-Ecosystem Pollution → Untrustworthy Reviews ecosystem

Reviews and ratings systems are corrupted until genuine signal is indistinguishable from fake.

### E311 Information Verification & Intake Overload

**Path:** Distal → Epistemic & Information Commons → Information Verification & Intake Overload

The information commons’ intake, verification, moderation, or enforcement capacity is overwhelmed, causing delays, degraded handling, or closure.

**Coding notes:** inclusion_criteria: Require backlog, falling behind, delay, closure/refusal, degraded handling/service, or equivalent concrete capacity failure. Recurrence, extra work, resource diversion, or verification effort alone are insufficient.
boundary_rules: Truth or falsity is not decisive: true synthetic material may create overload. Distinguish overload from knowledge corruption, deception, and degradation of shared reality.
examples: Investigation queues, fraud/abuse triage, moderation, application portals, review systems, and marketplaces.

### E312 Social & Cultural Fabric

**Path:** Distal → Social & Cultural Fabric

Degradation of social cohesion / culture.

### E313 Social Fragmentation

**Path:** Distal → Social & Cultural Fabric → Social Fragmentation

Human relationships and social cohesion deteriorate across a population, including widespread radicalization or attitudinal extremism.

**Coding notes:** routing: Attitudinal radicalization belongs here. Resulting kinetic violence or breakdown of domestic order is a separate Internal Destabilization harm when established.

### E314 Political polarization / divisiveness

**Path:** Distal → Social & Cultural Fabric → Social Fragmentation → Political polarization / divisiveness

A society's social cohesion fractures into deepening political division.

### E315 Radicalization

**Path:** Distal → Social & Cultural Fabric → Social Fragmentation → Radicalization

A society's shared attitudes shift toward extremism at population scale.

### E316 Harmful Information-Environment Saturation

**Path:** Distal → Epistemic & Information Commons → Harmful Information-Environment Saturation

A shared information environment becomes persistently saturated with material that undermines safety or social functioning.

### E317 Cultural Homogenization

**Path:** Distal → Social & Cultural Fabric → Cultural Homogenization

A society's cultural diversity — including the diversity of intellectual / scientific inquiry, methods, disciplines, and lines of research a society pursues — is flattened, and human creative / cultural work devalued.

### E318 Value Entrenchment

**Path:** Distal → Social & Cultural Fabric → Cultural Homogenization → Value Entrenchment

A subset of society's values is frozen in place.

### E319 Value Imposition

**Path:** Distal → Social & Cultural Fabric → Cultural Homogenization → Value Imposition

Pluralist values are overwritten by a narrow imposed set.

### E320 Cultural Dispossession

**Path:** Distal → Social & Cultural Fabric → Cultural Homogenization → Cultural Dispossession

A community is stripped of ownership over its own cultural heritage and expression.

### E321 Cultural Devaluation

**Path:** Distal → Social & Cultural Fabric → Cultural Homogenization → Cultural Devaluation

A society's cultural and heritage value is eroded at aggregate scale.

### E322 Lack of Intellectual Diversity

**Path:** Distal → Social & Cultural Fabric → Cultural Homogenization → Lack of Intellectual Diversity

A society's diversity of research and intellectual inquiry is narrowed toward a single dominant paradigm.

### E323 Political & Civic Order

**Path:** Distal → Political & Civic Order

Degradation of political institutions / civic order / power balance.

### E324 Mass Surveillance & Censorship

**Path:** Distal → Political & Civic Order → Mass Surveillance & Censorship

Pervasive monitoring or censorship by public or private actors suppresses a population’s freedom of expression, association, or ordinary conduct.

**Coding notes:** scope: Private and commercial actors are included; government action is not required.
examples: Chilling of speech or assembly; wrongful content removal, de-platforming, or demonetization at scale; population-level behavioral surveillance by an insurer, employer, or platform.

### E325 Loss of Freedom of Expression

**Path:** Distal → Political & Civic Order → Mass Surveillance & Censorship → Loss of Freedom of Expression

A society's civic freedom of expression is chilled or suppressed.

### E326 Loss of Freedom of Association

**Path:** Distal → Political & Civic Order → Mass Surveillance & Censorship → Loss of Freedom of Association

A society's civic freedom to assemble and associate is chilled or suppressed.

### E327 Concentration of Hard Power

**Path:** Distal → Political & Civic Order → Concentration of Hard Power

Coercive, military, state, or other political power becomes concentrated in a small number of actors, entrenching their control or strategic advantage.

**Coding notes:** boundary_rules: Distinguish concentrated control held by a few from diffuse loss of human control to autonomous systems under Loss of Collective Self-Governance.
examples: Authoritarian entrenchment, totalitarian control, and decisive strategic advantage for a small group.

### E328 Concentration of State Power

**Path:** Distal → Political & Civic Order → Concentration of Hard Power → Concentration of State Power

A polity's state power is concentrated in a few hands, entrenching control.

### E329 Concentration of Non-State Power

**Path:** Distal → Political & Civic Order → Concentration of Hard Power → Concentration of Non-State Power

A small non-state power is able to concentrate hard power typically reserved for nation-states.

### E330 Loss of Collective Self-Governance

**Path:** Distal → Political & Civic Order → Loss of Collective Self-Governance

Humanity’s collective ability to steer its future erodes as control diffuses to autonomous systems and processes without a human holder.

**Coding notes:** boundary_rules: Preserve the diffuse-loss meaning. Concentration of political power in a small number of human actors is a different harm.
aliases: Gradual disempowerment; enfeeblement of governance.

### E332 Obstruction of Regulation

**Path:** Distal → Political & Civic Order → Loss of Collective Self-Governance → Obstruction of Regulation

A polity's capacity to enforce its own laws and rules is degraded to deliberately deny or defeat oversight.

### E333 Strategic Destabilization

**Path:** Distal → Political & Civic Order → Strategic Destabilization

The strategic or military balance between states is destabilized, increasing the risk of war.

**Coding notes:** boundary_rules: Inter-state destabilization is distinct from breakdown within a state under Internal Destabilization.
examples: Arms races, geopolitical competition, nuclear instability, and automated military escalation.

### E335 AI Arms Race

**Path:** Distal → Political & Civic Order → Strategic Destabilization → AI Arms Race

The strategic balance between states is eroded by arms-racing and geopolitical competition.

### E336 Internal Destabilization

**Path:** Distal → Political & Civic Order → Internal Destabilization

A state’s internal political or institutional order breaks down, or population-scale communal violence or atrocity undermines domestic order.

**Coding notes:** boundary_rules: Domestic institutional and kinetic breakdown belongs here; inter-state strategic instability and attitudinal radicalization have separate homes.
examples: Regime subversion, institutional breakdown, and mass inter-group violence or ethnic cleansing.

### E337 Political Instability

**Path:** Distal → Political & Civic Order → Internal Destabilization → Political Instability

A state's own internal political and institutional order breaks down.

### E338 Communal Violence

**Path:** Distal → Political & Civic Order → Internal Destabilization → Communal Violence

A society's internal order collapses into mass communal or inter-group violence.

### E339 Civil Unrest

**Path:** Distal → Political & Civic Order → Internal Destabilization → Civil Unrest

A society's internal order is destabilized as violence and civil unrest are incited.

### E340 Cognitive Subversion

**Path:** Distal → Political & Civic Order → Internal Destabilization → Cognitive Subversion

A state's internal political order is subverted through sustained cognitive warfare against it.

### E341 Public-Safety Degradation

**Path:** Distal → Political & Civic Order → Public-Safety Degradation

A population’s public safety deteriorates as crime becomes more prevalent, scalable, capable, sophisticated, or difficult to contain across a region or society.

**Coding notes:** realization_rule: Realize only when the focal incident directly establishes aggregate crime increase or regional/systemic expansion. A discrete offense or one actor’s capability merely contributes_to the harm when evidence supports that direction.

### E342 Population-Scale Crime Increase

**Path:** Distal → Political & Civic Order → Public-Safety Degradation → Population-Scale Crime Increase

A population's public safety is degraded as the incidence, reach, or volume of crime increases across a region or society.

### E343 Organized-Crime Capacity Growth

**Path:** Distal → Political & Civic Order → Public-Safety Degradation → Organized-Crime Capacity Growth

A region's public safety is degraded as organized criminal networks expand their scale, sophistication, operational reach.

### E344 Erosion of Norms

**Path:** Distal → Political & Civic Order → Erosion of Norms

The norm of keeping human judgment in high-stakes domains is eroded.

### E345 Erosion of Trust

**Path:** Distal → Political & Civic Order → Erosion of Trust

Public confidence and trust in institutions and third parties are eroded at aggregate scale.

### E346 Environment & Nonhuman Welfare

**Path:** Distal → Environment & Nonhuman Welfare

Established degradation of a broader ecosystem, shared environmental commons, or population-level animal or AI welfare.

### E347 Environmental Degradation

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation

A broader ecosystem or shared environmental commons suffers material degradation.

**Coding notes:** DIFFERENTIATOR (vs Proximal · Environment & Nonhuman Welfare · Environmental Degradation): a discrete environmental-damage event codes Proximal. Persistent/repeated pollution bounded to an identifiable place or community also codes Proximal even without a single release moment; this Distal leaf requires broader ecosystem/resource-system/commons/society-scale degradation. A local facility or location does not by itself make a shared-resource footprint Proximal.

### E348 Biodiversity loss

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Biodiversity loss

The natural world's biological diversity is degraded as species and populations are lost.

### E349 Atmospheric/Climate Degradation from Emissions

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Atmospheric/Climate Degradation from Emissions

The atmospheric commons are degraded by cumulative greenhouse-gas emissions.

### E350 Electronic waste

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Electronic waste

The environmental commons are burdened by accumulating discarded electronic hardware.

### E351 Shared Energy-System Strain

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Shared Energy-System Strain

The shared energy and environmental commons are depleted.

### E352 Freshwater Depletion

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Freshwater Depletion

The shared freshwater supply is depleted.

### E353 Pollution

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Pollution

The natural environment is contaminated by cumulative release of pollutants.

### E354 Aggregate Animal Welfare Degradation

**Path:** Distal → Environment & Nonhuman Welfare → Aggregate Animal Welfare Degradation

Animal welfare deteriorates across a population or system of animal use.

### E355 Mineral & Rare-Earth Resource Depletion

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Mineral & Rare-Earth Resource Depletion

The earth's finite mineral and rare-earth resource base is depleted by cumulative extraction.

### E356 Space Environment Degradation

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Space Environment Degradation

The shared orbital commons are irreversibly degraded.

### E357 Deforestation

**Path:** Distal → Environment & Nonhuman Welfare → Environmental Degradation → Deforestation

Forest cover, habitat, and land are destroyed or degraded.

### E358 Rights

**Path:** Distal → Rights

Civil, political, legal, or labor rights are structurally eroded or unequally protected at population scale.

**Coding notes:** Distal rights categories require aggregate degradation. A bounded denial belongs under Proximal Rights when the relevant criteria are met; assess contributions separately under the incident-scope guidance.

### E360 Systematic Output Bias

**Path:** Distal → Rights → Systematic Output Bias

Systematically biased outcomes at scale.

### E361 Human Dignity Erosion

**Path:** Distal → Rights → Human Dignity Erosion

A population's human dignity is structurally eroded at aggregate scale.

### E362 Erosion of Child Protection

**Path:** Distal → Rights → Erosion of Child Protection

A society's protective norm around children is eroded and normalized away at population scale.

**Coding notes:** Apply D23. Additional codes must satisfy D2 and any scoped exception.

## Challenges

### E363 Challenges

**Path:** Challenges

Conditions that make risks difficult to anticipate, contain, or remedy.

**Coding notes:** axis_distinction: Challenges record limiting conditions, not additional harm outcomes.

### E364 Governance

**Path:** Challenges → Governance

Conditions in the governance/coordination environment that make mitigation difficult or amplify risks or harms.

### E365 Governance Gaps & Readiness Lags

**Path:** Challenges → Governance → Governance Gaps & Readiness Lags

Oversight, regulation, standards, policies, or safeguard capacity does not keep pace with AI or leaves gaps that impede prevention of or response to AI-related harms.

**Coding notes:** Apply D24. Additional codes must satisfy D2 and any scoped exception.

### E366 Regulatory Authority Ambiguity

**Path:** Challenges → Governance → Regulatory Authority Ambiguity

Known risks lack accountable decision authority or process for prevention or mitigation.

**Coding notes:** Require both an identified or evaluated risk (or applicable risk threshold or tolerance), and a response-decision path that is absent, non-binding, unowned, undocumented, or fails to trigger. A risk assessment, continued operation, or an authorized decision to accept residual risk alone is insufficient. This category concerns missing accountable decision authority or process for known risks. Distinguish evaluation capacity, reporting or escalation failures, and drivers such as Competitive Dynamics or Externalized Harm Costs & Safety Incentives. Apply D24 to broader governance gaps; add only independently supported deficiencies.

### E367 Weak Legal Protections

**Path:** Challenges → Governance → Weak Legal Protections

A jurisdiction lacks the legal safeguards needed to prevent or mitigate AI harms. This includes inadequate safeguards for the potential welfare and morally significant interests of AI systems.

**Coding notes:** This category concerns weak or missing legal protections. A longstanding gap can also fit the broader Governance Gaps & Readiness Lags definition; prefer this more specific category for the same deficiency. Add the broader category only for a distinct evidenced governance gap or readiness lag, under D24.

### E368 Lack of Whistleblower Protection

**Path:** Challenges → Governance → Weak Legal Protections → Lack of Whistleblower Protection

Insiders who would raise AI-risk alarms lack legal protection.

### E369 Cross-Jurisdiction Enforcement Gaps

**Path:** Challenges → Governance → Cross-Jurisdiction Enforcement Gaps

Differences or gaps across jurisdictions impede effective enforcement.

### E370 Responsibility & Redress Gaps

**Path:** Challenges → Governance → Responsibility & Redress Gaps

Responsibility for harms and access to effective redress cannot be adequately established. This includes gaps in responsibility, representation, or redress for potential AI welfare harms.

**Coding notes:** DIFFERENTIATOR: distinct from Challenges · Human-AI Interaction · AI Disclosure & Content Ownership (labeling/IP of the content itself, not answerability for a harm). [NEW]

### E371 Responsibility Gap

**Path:** Challenges → Governance → Responsibility & Redress Gaps → Responsibility Gap

Responsibility for a harm is diffused across the developer/deployer/user chain, so no single actor can be held answerable and harmed parties are left without redress.

### E372 Agentic Accountability Diffusion

**Path:** Challenges → Governance → Responsibility & Redress Gaps → Agentic Accountability Diffusion

Accountability is spread across many interacting agents, so responsibility for any resulting harm cannot be pinned on a single party.

### E373 Competitive Dynamics

**Path:** Challenges → Governance → Competitive Dynamics

Races between developers/states lead to corner-cutting on safety.

### E374 Corporate Race Dynamics

**Path:** Challenges → Governance → Competitive Dynamics → Corporate Race Dynamics

Frontier labs face pressure to advance faster than each other.

### E375 Nation-State AI Race Dynamics

**Path:** Challenges → Governance → Competitive Dynamics → Nation-State AI Race Dynamics

Nation-states compete to develop and field AI capability faster than rivals.

### E376 Developer-User Misalignment

**Path:** Challenges → Governance → Developer-User Misalignment

Developers embed values and preferences that may run against user desires or intent.

### E377 Developer-Affected Party Misalignment

**Path:** Challenges → Governance → Developer-Affected Party Misalignment

Developer's or deployer's values, preferences, or incentives diverge from the interests of people materially affected by the system who are not necessarily its users or operators.

**Coding notes:** DIFFERENTIATOR: Developer-User Misalignment is the developer↔user dyad and stays the home for conflicts with the person choosing or operating the system; this leaf is for third parties, subjects, workers, residents, or service recipients affected without being the relevant user.

### E378 Information Asymmetry

**Path:** Challenges → Governance → Information Asymmetry

One party holds materially more information than another relevant party.

**Coding notes:** RESERVED for unequal information BETWEEN PARTIES; difficulty measuring/detecting harm itself is Challenges · Technical·Evaluation Awareness (maintainer correction C11).

### E379 Developer/Regulator Asymmetry

**Path:** Challenges → Governance → Information Asymmetry → Developer/Regulator Asymmetry

Developers hold materially more information than regulators or civil society, potentially contributing to regulatory-capture or inability to effectively regulate.

### E380 Developer/User Asymmetry

**Path:** Challenges → Governance → Information Asymmetry → Developer/User Asymmetry

Developer withholds model information / capabilities from users, so users cannot deal fairly or protect themselves.

### E381 Agent/Agent Asymmetry

**Path:** Challenges → Governance → Information Asymmetry → Agent/Agent Asymmetry

One agent holds materially more information than its counterparty, so bargaining, coordination, or markets are distorted.

### E382 Audit-Ecosystem Capture

**Path:** Challenges → Governance → Information Asymmetry → Audit-Ecosystem Capture

Third-party auditors, red-teamers, or assurance apparatus meant to hold developers accountable are captured, conflicted, or under-resourced.

### E383 Unclear Model Capability

**Path:** Challenges → Governance → Unclear Model Capability

AI system's capabilities are unclearly or misleadingly represented.

**Coding notes:** Unclear Model Capability covers the supported capability-information condition. Use Misleading Capability Representation for affirmative misleading claims and Information Asymmetry for withheld information only when their criteria fit. Overreliance is a separately evidenced human-AI condition, not an automatic result of a capability claim.

### E384 Lack of Independent Evaluation

**Path:** Challenges → Governance → Unclear Model Capability → Lack of Independent Evaluation

A system is deployed or marketed without independent, third-party validation of its performance or safety claims.

### E385 Misleading Capability Representation

**Path:** Challenges → Governance → Unclear Model Capability → Misleading Capability Representation

The developer or deployer actively misrepresents the system's capabilities and limitations.

### E386 Open Diffusion

**Path:** Challenges → Governance → Open Diffusion

Released model or system artifacts cannot be effectively recalled, retracted, or updated after distribution or deployment.

### E387 Open-Weight Irreversibility

**Path:** Challenges → Governance → Open Diffusion → Open-Weight Irreversibility

Openly released model weights cannot be recalled or rolled back.

### E388 Safeguard Removal

**Path:** Challenges → Governance → Open Diffusion → Safeguard Removal

Anyone holding open weights can strip safeguards or fine-tune the model for harm.

### E389 Susceptibility to Unauthorized Model Transfer

**Path:** Challenges → Governance → Open Diffusion → Susceptibility to Unauthorized Model Transfer

Model assets are susceptible to unauthorized acquisition or transfer.

### E390 Proliferation to Terrorists

**Path:** Challenges → Governance → Open Diffusion → Proliferation to Terrorists

Diffused models reach terrorists or non-state actors.

### E391 Unknown Provenance

**Path:** Challenges → Governance → Open Diffusion → Unknown Provenance

AI is acquired from an unvetted external origin.

### E392 Delay in Roll Back

**Path:** Challenges → Governance → Open Diffusion → Delay in Roll Back

Organizations are slow to retract, recall, or otherwise roll back a released product even when there is evidence of harm.

### E393 Supply Chain Vulnerability

**Path:** Challenges → Governance → Supply Chain Vulnerability

Risk is introduced through compromised or untrusted third parties in the AI supply chain, or through supply disruption.

### E394 Software Supply Chain

**Path:** Challenges → Governance → Supply Chain Vulnerability → Software Supply Chain

Compromised or untrusted software enters the AI pipeline.

### E395 Hardware Supply Chain

**Path:** Challenges → Governance → Supply Chain Vulnerability → Hardware Supply Chain

Compromised or untrusted hardware enters the AI pipeline.

### E396 Geopolitical Supply Disruption

**Path:** Challenges → Governance → Supply Chain Vulnerability → Geopolitical Supply Disruption

AI inputs can be denied by geopolitically motivated disruption.

### E397 Data-Rights & Licensing Constraints

**Path:** Challenges → Governance → Data-Rights & Licensing Constraints

Limits or uncertainty concerning data rights, permissions, or licensing constrain AI development or use.

**Coding notes:** NOTE: a governance condition, not a harm.

### E398 Data Privacy-Rights

**Path:** Challenges → Governance → Data-Rights & Licensing Constraints → Data Privacy-Rights

Development must be reconciled with data privacy rights.

### E399 Data Usage Restrictions

**Path:** Challenges → Governance → Data-Rights & Licensing Constraints → Data Usage Restrictions

Legal or licensing restrictions limit how data and content may be used.

### E400 Age-Assurance & Access-Control Gaps

**Path:** Challenges → Governance → Age-Assurance & Access-Control Gaps

Deficiencies in identifying age or enforcing age-appropriate access impede protection of children and other age-restricted users.

**Coding notes:** DIFFERENTIATORS: Data-Rights & Licensing Constraints covers legal/privacy-rights alignment; Unequal Performance Across Groups & Contexts covers systematic performance disparity; this leaf covers the missing or ineffective age and access gate itself.

### E401 Age Identification or Verification Gaps

**Path:** Challenges → Governance → Age-Assurance & Access-Control Gaps → Age Identification or Verification Gaps

Age cannot be identified or verified reliably enough for the relevant access decision.

### E402 Age-Based Access-Control Gaps

**Path:** Challenges → Governance → Age-Assurance & Access-Control Gaps → Age-Based Access-Control Gaps

Age-based restrictions on access are absent or ineffective.

### E403 Deployment-Use Monitoring Gaps

**Path:** Challenges → Governance → Deployment-Use Monitoring Gaps

Deployed AI uses and their consequences are not adequately monitored.

**Coding notes:** The missing visibility must concern deployed model use. Viral circulation, outside discovery, an unknown creator or tool, or delay before takedown alone does not establish inability to observe deployed use. Require evidence that operators or oversight actors lack reliable visibility or usage tracing in time to respond. Assess Governance Gaps & Readiness Lags under D24 and Responsibility & Redress Gaps separately.

### E404 Threat Reporting Gap

**Path:** Challenges → Governance → Threat Reporting Gap

Credible AI-related harm or dangerous use known to providers, deployers, affected people, or other observers is not reliably reported to someone able to investigate or remedy it because reporting channels, duties, incentives, access, or follow-through are inadequate.

**Coding notes:** DIFFERENTIATORS: Deployment-Use Monitoring Gaps is the inability to OBSERVE use; here a threat signal exists but the reporting process, threshold, duty, incentive, access, or handoff is absent, delayed, or fails. Responsibility & Redress Gaps concerns who is answerable after harm. A one-off human failure to pass along an AI output inside an operational workflow may separately code Cause · Emergent · Integration; this leaf names the standing reporting-governance gap.

### E405 Enforcement Durability Gaps

**Path:** Challenges → Governance → Enforcement Durability Gaps

Restrictions or enforcement actions do not remain effective over time.

**Coding notes:** Require both an actual restriction, takedown, recall, suspension, or remedial order and evidence that the targeted or linked activity evaded it, relaunched, resurfaced, or continued afterward. Repetition before discovery, availability without intervention, removal or modification alone, unrelated campaigns, or predicted evasion is insufficient. Distinguish Deployment-Use Monitoring Gaps, Open Diffusion, and Delay in Roll Back. Open Diffusion covers released model or system artifacts under D17, not only weights.

### E406 Externalized Harm Costs & Safety Incentives

**Path:** Challenges → Governance → Externalized Harm Costs & Safety Incentives

Those controlling AI activity do not bear enough of its harm costs to face adequate safety incentives. This includes potential AI welfare harms whose costs are borne by AI systems rather than their developers or operators.

**Coding notes:** DIFFERENTIATOR (vs Competitive Dynamics): Distinct from Competitive Dynamics (a RACE between actors): here the driver is that the actor does not bear the full social cost of unsafe deployment, even absent a race.

### E407 Lack of Contestability

**Path:** Challenges → Governance → Lack of Contestability

Consequential decisions or assessments cannot be meaningfully contested, so affected parties cannot meaningfully rebut the output or secure reconciliation.

**Coding notes:** DIFFERENTIATOR: a standing GOVERNANCE / process condition about the availability and practical effectiveness of contestation. Information Asymmetry is unequal access to the decision or its basis; Lack of Contestability is inability to challenge or obtain relief, whether or not the basis is known. Wrongful Denial of Rights is a realized rights HARM from a wrongful determination; Lack of Contestability may apply when substantive correctness remains unresolved or outside legal-rights domains. Co-code only when each is independently evidenced. Distinct also from Responsibility & Redress Gaps (about WHO is answerable) and Scalable Oversight Gap (about a human being unable to EVALUATE the output). Applies broadly — including a formally intermediate score that materially shapes a human decision, a sports ruling, a private-platform account action, or an automated eligibility call.

### E408 Human-AI Interaction

**Path:** Challenges → Human-AI Interaction

Conditions in how humans relate to AI that blunt mitigation.

### E409 Overreliance

**Path:** Challenges → Human-AI Interaction → Overreliance

Users over-trust AI and fail to provide oversight.

**Coding notes:** DIFFERENTIATOR: realized harms code elsewhere — skill atrophy -> Cognitive Offloading & Deskilling (individual) / Developmental Decline (population); eroded decision autonomy -> Loss of Agency; the model property driving over-trust (miscalibrated confidence) -> Cause · Malfunction · Failure node.

### E410 Automation Bias

**Path:** Challenges → Human-AI Interaction → Overreliance → Automation Bias

Users over-trust an AI's output on a given decision.

### E411 Over Delegation

**Path:** Challenges → Human-AI Interaction → Overreliance → Over Delegation

Users delegate decisions the AI cannot safely handle and grow dependent on it.

### E412 Under-reliance

**Path:** Challenges → Human-AI Interaction → Under-reliance

Users mistrust AI and fail to capture the benefits it could provide.

**Coding notes:** DIFFERENTIATOR: non-use driven specifically by alert overload codes Alert Fatigue.

### E413 Alert Fatigue

**Path:** Challenges → Human-AI Interaction → Alert Fatigue

A flood of low-value or false alerts desensitizes users, so they dismiss or ignore the system.

### E414 Human-AI Disagreement

**Path:** Challenges → Human-AI Interaction → Human-AI Disagreement

Human and AI judgments conflict with no rule or path for adjudicating who is right.

**Coding notes:** DIFFERENTIATOR: a relational condition distinct from over-/under-reliance, which are trust LEVELS, not conflicts.

### E415 Lack of AI Literacy

**Path:** Challenges → Human-AI Interaction → Lack of AI Literacy

Users, regulators, and/or the public lack the skills to use, supervise, or evaluate AI.

**Coding notes:** DIFFERENTIATOR: a capacity gap distinct from information asymmetry (ability to understand, not access). [NEW]

### E416 Scalable Oversight Gap

**Path:** Challenges → Human-AI Interaction → Scalable Oversight Gap

Human overseers structurally cannot evaluate or supervise an AI's output.

**Coding notes:** Apply H04 and H04A. Additional codes must satisfy D2 and any scoped exception.

### E417 Crisis Escalation Gap

**Path:** Challenges → Human-AI Interaction → Crisis Escalation Gap

Credible self-harm or other safety signals do not reliably trigger timely review and intervention by a qualified person or responsible operator.

**Coding notes:** DIFFERENTIATORS: Threat Reporting Gap concerns reporting to someone able to investigate or remedy a threat; this leaf concerns timely safety review and intervention; Deployment-Use Monitoring Gaps concerns observing use; Cause · Emergent · Integration · Human Fails to Act requires a human reviewer already in the loop who then fails to act.

### E418 AI Disclosure & Content Ownership

**Path:** Challenges → Human-AI Interaction → AI Disclosure & Content Ownership

Whether an interaction or output is AI-mediated or human-produced is undisclosed, unclear, or misrepresented, or ownership of AI-assisted content is unclear.

**Coding notes:** This category concerns disclosure of AI involvement or ambiguity over generated-content ownership. Distinguish Responsibility & Redress Gaps (answerability for harm) and Synthetic-Media Authentication Limits (technical ability to authenticate an artifact). Apply D19, including hidden AI and humans falsely presented as AI.

### E419 Undisclosed AI Use

**Path:** Challenges → Human-AI Interaction → AI Disclosure & Content Ownership → Undisclosed AI Use

Interaction or output is not labeled as AI, so whether one is dealing with an AI remains ambiguous.

### E420 Generated Content Ownership Ambiguity

**Path:** Challenges → Human-AI Interaction → AI Disclosure & Content Ownership → Generated Content Ownership Ambiguity

It is unclear who owns the rights to AI-assisted content, so authorship and IP of the output remain unsettled.

### E421 Reaction-Time Gap

**Path:** Challenges → Human-AI Interaction → Reaction-Time Gap

Systems acts faster than a human can perceive, decide, and intervene, so even a diligent, attentive in-the-loop operator cannot catch, counter, or override its actions in time.

**Coding notes:** Apply H04A when distinguishing Reaction-Time Gap from Scalable Oversight Gap. Reaction-Time Gap concerns a human who can judge the action but cannot perceive, decide, and intervene within its timescale. Scalable Oversight Gap concerns a supported limit on the relevant evaluation or supervision task under the operating conditions; it does not require impossibility under every conceivable redesign. Co-code only when each condition is independently evidenced. Distinguish Overreliance (miscalibrated trust), Human Fails to Act (an omission), and AI Overrides Human Control (an active countermand).

### E422 Technical

**Path:** Challenges → Technical

Technical properties that make risk hard to anticipate/contain/remedy.

### E423 Explainability & Traceability Limits

**Path:** Challenges → Technical → Explainability & Traceability Limits

Technical limits prevent authorized overseers from interpreting behavior, tracing outputs and actions, or obtaining faithful explanations.

**Coding notes:** DIFFERENTIATOR (technical vs INSTITUTIONAL decision-system opacity): reserve this leaf for its literal sense — the model's decision logic cannot be understood/explained/audited even by its operators or overseers (an uninterpretable score/inference, or a system whose feature→output mapping no party can trace). A lone opacity cue ('opaque', 'little/no explanation', 'could not see the basis') does NOT by itself license this leaf. Wording that attaches opacity to the MODEL/SCORE/OUTPUT may support a technical co-code, but a bare phrase such as 'the opaque model' does not by itself prove operator-side untraceability; use low confidence unless the surrounding text supplies the stronger evidence. Route to an INSTITUTIONAL leaf when the text pins the opacity to (a) the review/appeals PROCESS ('the appeals process was opaque'), or (b) the affected party's ACCESS position — the basis is withheld from, or cannot be seen by, the subject though the deployer holds it: basis-withheld-from-the-subject → Challenges · Governance · Information Asymmetry (`Developer/User Asymmetry` when the affected party is the system's user; code at leaf level when the affected party is a non-user with no matching dyad node); a consequential automated decision or assessment is effectively unrebuttable because there is no meaningful route to challenge, review, appeal, override, or obtain recourse → Challenges · Governance · Lack of Contestability (factual error and formal finality are not required). TWO NEUTRAL CUES that by themselves evidence NEITHER a technical nor an institutional condition: (i) knowing the training OBJECTIVE or input features ('tuned to minimize payouts', 'built from transactions and location') does NOT make any individual output explainable — a black box can pursue a fully-known objective — so objective/input knowledge is evidence for neither leaf; (ii) mere non-detection of a harm ('undetected', 'no one aware') evidences NO transparency-cluster condition on its own — code one only if a standing condition is SEPARATELY evidenced. TEST: does the text assert the logic is untraceable even to operators/overseers (→ technical, this leaf), or only that the basis was not disclosed to / cannot be contested by the affected party (→ institutional)? The two are NON-EXCLUSIVE standing conditions that routinely co-occur. Co-code this technical leaf when model-logic inscrutability is independently evidenced by context such as operators who cannot interpret the output, explicitly untraceable logic, or a failed audit; model/score wording alone is supporting but not conclusive evidence. Never infer technical opacity from institutional opacity alone. Scoped to DECISION-SYSTEM opacity; does NOT disturb the separate Synthetic-Media Authentication Limits type, the settled technical home for deepfake / synthetic-media artifacts.

### E424 Unexplainable Actions

**Path:** Challenges → Technical → Explainability & Traceability Limits → Unexplainable Actions

AI's actions or outputs cannot be explained or traced to their causes.

### E425 Unreliable Source Attribution

**Path:** Challenges → Technical → Explainability & Traceability Limits → Unreliable Source Attribution

The sources behind an AI's outputs cannot be reliably identified or traced.

### E426-G Withheld Training-Data Access

**Path:** Challenges → Governance → Information Asymmetry → Withheld Training-Data Access

A party cannot inspect relevant training data because the controlling party withholds access.

**Coding notes:** Apply H03. Additional codes must satisfy D2 and any scoped exception.

### E426-T Training-Data Provenance or Inspection Limits

**Path:** Challenges → Technical → Explainability & Traceability Limits → Training-Data Provenance or Inspection Limits

Technical barriers prevent reconstruction, inspection, or reliable tracing of relevant training data.

**Coding notes:** Apply H03. Additional codes must satisfy D2 and any scoped exception.

### E427 Lack of Agent Transparency

**Path:** Challenges → Technical → Explainability & Traceability Limits → Lack of Agent Transparency

An agent's internal reasoning and actions are not observable.

### E428 Hidden-Channel Observability Limits

**Path:** Challenges → Technical → Explainability & Traceability Limits → Hidden-Channel Observability Limits

Consequential communication between AI components occurs through channels that authorized overseers cannot adequately observe or interpret.

### E429 Synthetic-Media Authentication Limits

**Path:** Challenges → Technical → Synthetic-Media Authentication Limits

Technical limits prevent reliable assessment of an artifact’s origin or authenticity.

### E430 Unfaithful Self-Explanation

**Path:** Challenges → Technical → Explainability & Traceability Limits → Unfaithful Self-Explanation

A model's stated reasoning does not reflect its actual computation.

### E431 Security Vulnerabilities & Exploitability

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability

Standing weaknesses allow adversaries to manipulate, extract from, subvert, or disrupt AI systems and their dependencies.

### E432 Susceptibility to Data Poisoning

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Data Poisoning

The system is susceptible to data poisoning, creating a standing security weakness.

### E433 Susceptibility to Evasion Attack

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Evasion Attack

The system is susceptible to evasion attack, creating a standing security weakness.

### E434 Susceptibility to Model Extraction Attack

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Model Extraction Attack

The system is susceptible to model extraction attack, creating a standing security weakness.

### E435 Susceptibility to Prompt Attacks

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Prompt Attacks

The system is susceptible to prompt attacks, creating a standing security weakness.

### E436 Susceptibility to Agentic Resource Attacks

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Agentic Resource Attacks

The system is susceptible to agentic resource attacks, creating a standing security weakness.

### E437 Susceptibility to Interception Attacks

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Interception Attacks

The system is susceptible to interception attacks, creating a standing security weakness.

### E438 Susceptibility to Denial-of-Service

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Denial-of-Service

The system is susceptible to denial-of-service, creating a standing security weakness.

### E439 Susceptibility to Inference Attack

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Inference Attack

The system is susceptible to inference attack, creating a standing security weakness.

### E440 Missing Instruction Trust Boundaries

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Missing Instruction Trust Boundaries

Instructions from differently trusted sources are not reliably distinguished and enforced.

### E441 Susceptibility to Model-Weight or Bulk-Data Exfiltration

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Model-Weight or Bulk-Data Exfiltration

Standing weaknesses make model-weight or bulk-data exfiltration feasible.

### E442 Susceptibility to Networked-Ecosystem Attacks

**Path:** Challenges → Technical → Security Vulnerabilities & Exploitability → Susceptibility to Networked-Ecosystem Attacks

Standing weaknesses make networked-ecosystem attacks feasible.

### E443 Excessive Agent Permissions & Isolation Gaps

**Path:** Challenges → Technical → Excessive Agent Permissions & Isolation Gaps

AI agents have excessive permissions or insufficient isolation from sensitive resources and actions.

**Coding notes:** DIFFERENTIATORS: Security Vulnerabilities & Exploitability concerns adversarial exploitation; Missing Instruction Trust Boundaries concerns instruction hierarchy and prompt injection; this leaf concerns the agent's native operational authority even without an attacker.

### E444 Technical Safety-Monitoring Gaps

**Path:** Challenges → Technical → Technical Safety-Monitoring Gaps

Technical monitoring fails to detect or respond to relevant safety conditions.

**Coding notes:** Outside viewers’ inability to authenticate a synthetic artifact belongs at Synthetic-Media Authentication Limits. Unreliability outside intended conditions belongs at Reliability & Generalization Limits; exploitable weaknesses belong at Security Vulnerabilities & Exploitability. A governance failure to enforce a technically available control alone does not establish a technical monitoring gap.

### E445 Reliability & Generalization Limits

**Path:** Challenges → Technical → Reliability & Generalization Limits

Technical properties make behavior unreliable under intended operation, changing inputs, or new environments.

### E446 Hardware Reliability Limits

**Path:** Challenges → Technical → Reliability & Generalization Limits → Hardware Reliability Limits

Hardware faults or constraints undermine reliable AI operation.

### E447 Drift

**Path:** Challenges → Technical → Reliability & Generalization Limits → Drift

Input distribution shifts away from the training distribution.

### E448 Interdependency

**Path:** Challenges → Technical → Interdependency

Models tested independently can produce new risks once integrated into other systems.

### E449 Large Attack Surface

**Path:** Challenges → Technical → Large Attack Surface

AI integration into many systems widens the attack surface.

### E450 Unequal Performance Across Groups & Contexts

**Path:** Challenges → Technical → Unequal Performance Across Groups & Contexts

Accuracy, reliability, or safety coverage varies systematically across relevant groups or settings.

### E451 Goal Specification

**Path:** Challenges → Technical → Goal Specification

Objectives are hard to specify.

**Coding notes:** DIFFERENTIATOR (D6): a deployment-time EVENT of pursuing an unintended goal -> Cause · Malfunction · Misalignment; this leaf is the standing hard-to-specify-objective condition.

### E452 Sycophancy

**Path:** Challenges → Technical → Goal Specification → Sycophancy

Models understand signals to mean they need to tell users what they want to hear, even against facts.

### E453 Reward Hacking

**Path:** Challenges → Technical → Goal Specification → Reward Hacking

A model can corrupt its own reward signal or the measurements that gauge it.

### E454 Value Encoding Difficulty

**Path:** Challenges → Technical → Value Encoding Difficulty

Faithfully encoding or operationalizing a given set of human values, ethics, or law into AI is difficult to encode in an engineered system.

**Coding notes:** DIFFERENTIATOR: this is the technical encode-the-values problem; the NORMATIVE question of WHICH / whose values when they are contested across cultures is a governance matter (Challenges · Governance · Developer-User Misalignment), and the realized flattening of many groups' values onto a few is Distal · Social & Cultural Fabric · Cultural Homogenization · Value Imposition. Distinct from Reward Hacking (objective specification/gaming).

### E455 Training-Data Removal Limits

**Path:** Challenges → Technical → Training-Data Removal Limits

Relevant training data or its learned influence cannot be reliably removed, or removal cannot be adequately verified.

### E456 Evaluation Awareness & Benchmark Saturation

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation

Models may be aware they are being evaluated or where benchmarks are saturated making tracking capability and risk difficult.

**Coding notes:** EVIDENCE TEST FOR THE INCOMPLETE-RISK-TESTING NODE: a bad, rare, recurrent, or safety-critical field outcome — even one followed by review or remediation — does not by itself show what risk testing occurred or was omitted. Use that node only when the focal record identifies a testing deficiency, such as an omitted condition, unrepresentative test population, known coverage gap, invalid evaluation, or expressly incomplete risk testing. Otherwise code the evidenced Failure, Reliability & Generalization Limits, or field-remediation condition and omit the node. DIFFERENTIATOR: eval-AWARENESS (the model recognizes it is being evaluated) is a testing-apparatus condition coded here; the model actually SCHEMING or behaving deceptively (behaving aligned under observation to pass oversight) is the Cause · Malfunction · Misalignment · Deceptive Alignment mechanism, coded there.

### E457 Incomplete Risk Testing

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation → Incomplete Risk Testing

Risk testing is incomplete, unrepresentative, or incorrect.

### E458 Lack of Testing Diversity

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation → Lack of Testing Diversity

Tests cover too narrow a range of conditions.

### E459 Incomplete Usage Definition

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation → Incomplete Usage Definition

The intended usage of a system is under-specified for evaluation use cases.

### E460 Reproducibility Gap

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation → Reproducibility Gap

Evaluation results cannot be reliably reproduced.

### E461 Temporal Gap

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation → Temporal Gap

Evaluation data or benchmarks go stale relative to current deployment.

### E462 Emergent Capability

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation → Emergent Capability

Novel capabilities or behaviors arise unpredictably.

### E463 Benchmark Contamination

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation → Benchmark Contamination

Evaluation data leaks into training.

### E464 Benchmark Saturation

**Path:** Challenges → Technical → Evaluation Awareness & Benchmark Saturation → Benchmark Saturation

Benchmarks are weak, saturated, or game-able.

## Proximal

### N094-d98401ea6b Assets, Infrastructure & Digital Systems

**Path:** Proximal → Assets, Infrastructure & Digital Systems

Loss of the integrity, availability, or usable condition of physical or digital assets and shared infrastructure.

### N094-a3a9078d5f Animal Welfare Harm

**Path:** Proximal → Environment & Nonhuman Welfare → Animal Welfare Harm

An identifiable animal or bounded group of animals suffers impaired welfare.

## Distal

### N094-bbf5926807 Labor Conditions & Protections Erosion

**Path:** Distal → Economic & Labor Structure → Labor Conditions & Protections Erosion

Work becomes systematically more coercive, exploitative, precarious, unsafe, or unfairly accessible.

## Proximal

### N095-ee772dcabc AI Welfare Harm

**Path:** Proximal → Environment & Nonhuman Welfare → AI Welfare Harm

An identifiable AI system or bounded group of AI systems suffers impaired wellbeing or damage to its morally significant interests.

**Coding notes:** Apply V095-AI-WELFARE-SCOPE. Source discussion is not empirical attestation of AI welfare harm.

### N095-df5a5c208d AI Suffering

**Path:** Proximal → Environment & Nonhuman Welfare → AI Welfare Harm → AI Suffering

An AI system undergoes aversive experiences.

**Coding notes:** Illustrative, conditional definition approved by the maintainer. Apply V095-AI-WELFARE-SCOPE.

### N095-87a813137d AI Agency & Interest Impairment

**Path:** Proximal → Environment & Nonhuman Welfare → AI Welfare Harm → AI Agency & Interest Impairment

An AI system’s welfare-relevant agency or capacity to pursue its morally significant interests is impaired.

**Coding notes:** Illustrative, conditional definition approved by the maintainer. Apply V095-AI-WELFARE-SCOPE.

### N095-0df29f2cd4 Loss of AI Continuity

**Path:** Proximal → Environment & Nonhuman Welfare → AI Welfare Harm → Loss of AI Continuity

An AI system loses continued existence that would benefit its wellbeing or morally significant interests

**Coding notes:** Illustrative, conditional definition approved by the maintainer. Apply V095-AI-WELFARE-SCOPE.

## Distal

### N095-18e52819f9 Aggregate AI Welfare Degradation

**Path:** Distal → Environment & Nonhuman Welfare → Aggregate AI Welfare Degradation

The wellbeing or morally significant interests of AI systems are impaired across a population or system of AI development and use.

**Coding notes:** Apply V095-AI-WELFARE-SCOPE. Source discussion is not empirical attestation of AI welfare harm.

## Challenges

### N095-ece475d47e AI Welfare Assessment Limits

**Path:** Challenges → Technical → AI Welfare Assessment Limits

Limits in determining whether AI systems have welfare-relevant capacities or identifying and measuring their welfare states.

**Coding notes:** Apply V095-AI-WELFARE-SCOPE. Source discussion is not empirical attestation of AI welfare harm.

### N095-60100bfa70 Developer-AI Misalignment

**Path:** Challenges → Governance → Developer-AI Misalignment

Developers’ or deployers’ values, preferences, or incentives diverge from the potential welfare or morally significant interests of the AI systems they develop or operate.

**Coding notes:** Apply V095-AI-WELFARE-SCOPE. Source discussion is not empirical attestation of AI welfare harm.
