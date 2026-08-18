# NIST AI RMF + ISO 42001 Audit Report

**Generated:** 2026-08-18 23:01:02

## Executive Summary

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 1 |
| Partial | 10 |
| Gaps | 26 |

**Compliance Rate:** 2.7%

---

## Detailed Findings

### NIST AI RMF


#### ❌ GOVERN-1.1 - GAP

**Explanation:** The policy does not mention legal, statutory, or regulatory compliance requirements applicable to AI systems.

**Recommendation:** Incorporate a dedicated compliance section requiring mapping, tracking, and documentation of applicable AI laws, regulations, and industry standards.


#### 🟡 GOVERN-1.2 - PARTIAL

**Explanation:** Section 3 outlines trustworthy AI principles (fairness, transparency, safety, privacy), but lacks operational procedures for integrating them into day-to-day practices.

**Recommendation:** Establish standard operating procedures (SOPs) and metrics to operationalize and enforce trustworthy AI principles across development lifecycles.


#### 🟡 GOVERN-1.3 - PARTIAL

**Explanation:** Section 4 references 'high-risk AI systems', but does not define organizational risk tolerance, classification criteria, or risk assessment methodologies.

**Recommendation:** Define an enterprise AI risk tolerance framework and establish clear risk tiering criteria (e.g., low, medium, high) with associated mandatory controls.


#### 🟡 GOVERN-1.4 - PARTIAL

**Explanation:** High-level governance oversight is established, but formal policies outlining transparent AI risk management processes and prioritization controls are missing.

**Recommendation:** Document and publish formal AI risk assessment and management procedures that reflect ACME Corp's risk priorities.


#### 🟡 GOVERN-1.5 - PARTIAL

**Explanation:** Section 6 mandates monitoring for performance drift and incident reporting, but lacks periodic review of the overarching AI risk management framework.

**Recommendation:** Institute annual or event-driven audit and review cycles for the AI governance and risk management processes with assigned owner responsibilities.


#### ❌ GOVERN-1.6 - GAP

**Explanation:** The policy does not mandate or establish an AI system inventory or registry.

**Recommendation:** Mandate the creation and maintenance of a centralized AI system inventory capturing system metadata, risk tiers, and resource allocations.


#### ❌ GOVERN-1.7 - GAP

**Explanation:** There are no provisions covering the secure decommissioning, archiving, or phase-out of AI systems.

**Recommendation:** Add a decommissioning protocol outlining data retention, model archiving, user communication, and risk management during system retirement.


#### 🟡 GOVERN-2.1 - PARTIAL

**Explanation:** Section 4 assigns oversight to the CTO and AI Governance Committee, but specific roles, responsibilities, and communication channels for risk mapping and measuring are not detailed.

**Recommendation:** Develop a RACI matrix defining roles, escalation pathways, and communication channels for AI risk management.


#### ❌ GOVERN-2.2 - GAP

**Explanation:** The policy contains no requirement for workforce or partner training on AI risk management.

**Recommendation:** Implement mandatory, role-based AI ethics and risk management training for developers, deployers, and decision-makers.


#### ✅ GOVERN-2.3 - COMPLIANT

**Explanation:** Section 4 explicitly designates the CTO as accountable for overseeing AI initiatives and assigns high-risk review authority to the AI Governance Committee.

**Recommendation:** Maintain regular executive reporting schedules to ensure sustained leadership oversight.


#### ❌ GOVERN-3.1 - GAP

**Explanation:** The policy does not address diversity in background, expertise, or demographics within AI risk decision-making bodies.

**Recommendation:** Ensure the AI Governance Committee includes multidisciplinary stakeholders (e.g., legal, ethics, domain experts, civil society representatives).


#### ❌ GOVERN-3.2 - GAP

**Explanation:** The policy does not define roles or requirements for human oversight or human-in-the-loop configurations.

**Recommendation:** Define policies specifying human oversight requirements (human-in-the-loop, human-on-the-loop, human-in-command) based on system risk tiers.


#### 🟡 GOVERN-4.1 - PARTIAL

**Explanation:** Section 3 and Section 5 emphasize safety and security reviews, but broad organizational culture and critical thinking commitments are not formalized.

**Recommendation:** Articulate organizational commitments to a safety-first AI culture, including whistleblower protections and challenge mechanisms.


#### ❌ GOVERN-4.2 - GAP

**Explanation:** The policy does not mandate documentation of identified risks, impact assessments, or mitigation strategies for AI projects.

**Recommendation:** Require mandatory AI Impact Assessments (AIIA) and risk logs for all AI systems prior to deployment.


#### 🟡 GOVERN-4.3 - PARTIAL

**Explanation:** Section 5 requires validation and security reviews, and Section 6 requires incident reporting, but external information sharing mechanisms are absent.

**Recommendation:** Add requirements for post-incident reviews, knowledge sharing, and contribution to industry incident reporting databases.


#### ❌ GOVERN-5.1 - GAP

**Explanation:** No mechanism exists for soliciting, considering, or prioritizing feedback from external stakeholders regarding societal or individual impacts.

**Recommendation:** Establish public/external feedback channels and stakeholder consultation processes for AI deployments.


#### ❌ GOVERN-5.2 - GAP

**Explanation:** No workflow is established to incorporate adjudicated feedback into system design or updates.

**Recommendation:** Define a structured process for logging, adjudicating, and integrating stakeholder feedback into the AI lifecycle.


#### 🟡 GOVERN-6.1 - PARTIAL

**Explanation:** Section 7 states third-party AI must be reviewed, but lacks specifics regarding supply chain risks, data provenance, intellectual property, or licensing.

**Recommendation:** Establish comprehensive third-party AI procurement guidelines covering IP rights, security evaluations, data privacy, and vendor compliance.


#### ❌ GOVERN-6.2 - GAP

**Explanation:** The policy contains no contingency or business continuity planning for third-party AI failures or outages.

**Recommendation:** Develop business continuity and contingency plans (e.g., fallbacks, kill-switches) for critical third-party AI services.


#### ❌ MAP-1.1 - GAP

**Explanation:** The policy lacks guidelines for documenting intended use cases, deployment context, target populations, and legal expectations at the system level.

**Recommendation:** Require a System Context Document for every AI project outlining intended use, operational boundaries, and legal constraints.


#### ❌ MAP-1.2 - GAP

**Explanation:** No requirement exists ensuring context establishment involves interdisciplinary and diverse teams.

**Recommendation:** Incorporate cross-functional scoping workshops (technical, legal, operational, domain experts) at project inception.


#### 🟡 MAP-1.3 - PARTIAL

**Explanation:** Section 1 and Section 3 provide high-level organizational purpose and principles, but do not align specific AI goals with strategic mission objectives.

**Recommendation:** Mandate that AI business cases document explicit alignment with organizational mission, strategy, and ethical guidelines.


#### ❌ MAP-1.4 - GAP

**Explanation:** There are no requirements to evaluate or periodically re-evaluate the business value and context of AI use cases.

**Recommendation:** Implement mandatory business value justification and periodic post-implementation reviews for AI systems.


#### ❌ MAP-1.5 - GAP

**Explanation:** Organizational risk tolerance levels for AI are not defined or documented.

**Recommendation:** Formulate and publish documented risk appetite/tolerance statements for AI performance, safety, and compliance.


#### ❌ MAP-1.6 - GAP

**Explanation:** The policy does not require eliciting socio-technical requirements or assessing broad societal implications during system design.

**Recommendation:** Integrate socio-technical impact elicitation into early-stage AI system requirements engineering.


#### ❌ MAP-2.1 - GAP

**Explanation:** No requirement specifies defining system tasks, algorithmic methods, or functional boundaries.

**Recommendation:** Mandate detailed technical specifications detailing methods, models, baseline datasets, and functional boundaries for all AI systems.


#### ❌ MAP-2.2 - GAP

**Explanation:** The policy does not mandate documenting system limitations, knowledge boundaries, or human oversight guidelines.

**Recommendation:** Require Model Cards or System FactSheets documenting known limitations, failure modes, and appropriate operational parameters.


#### 🟡 MAP-2.3 - PARTIAL

**Explanation:** Section 5 requires validation, security reviews, and representative testing data, but lacks formal Test, Evaluation, Verification, and Validation (TEVV) frameworks.

**Recommendation:** Establish a formalized TEVV protocol including scientific integrity checks, robustness metrics, and benchmark testing standards.


#### ❌ MAP-3.1 - GAP

**Explanation:** No requirement exists to formally examine and document expected benefits against baseline performance.

**Recommendation:** Require benefit-risk analysis documentation for each proposed AI initiative.


#### ❌ MAP-3.2 - GAP

**Explanation:** The policy does not address assessing non-monetary costs, potential negative impacts, or error consequences.

**Recommendation:** Include failure mode and effects analysis (FMEA) to assess potential direct and indirect costs of AI errors.


#### ❌ MAP-3.3 - GAP

**Explanation:** The policy defines overall organizational scope but does not mandate specifying targeted application scope for individual AI systems.

**Recommendation:** Require system specifications to define explicit in-scope and out-of-scope application boundaries and intended user groups.


#### ❌ MAP-3.4 - GAP

**Explanation:** The policy does not specify proficiency requirements or competence assessments for AI system operators.

**Recommendation:** Define training and competency certification criteria for personnel operating or making decisions based on AI outputs.


#### ❌ MAP-3.5 - GAP

**Explanation:** Processes and protocols for human oversight are not established or documented.

**Recommendation:** Establish operational protocols defining oversight mechanisms, override capabilities, and escalation paths for operators.


#### ❌ MAP-4.1 - GAP

**Explanation:** The policy does not require risk mapping for individual AI components, open-source libraries, or external dependencies.

**Recommendation:** Implement Software Bill of Materials (SBOM) and AI component risk mapping processes covering third-party libraries and pretrained weights.


#### 🟡 MAP-4.2 - PARTIAL

**Explanation:** Section 5 and Section 7 mandate security reviews and third-party reviews, but do not structure specific internal risk controls per component.

**Recommendation:** Document specific control baselines for internal vs. external AI components, including data provenance and vulnerability scanning.


#### ❌ MAP-5.1 - GAP

**Explanation:** No guidelines are provided for assessing the likelihood and magnitude of potential AI impacts.

**Recommendation:** Define a standardized risk matrix assessing impact likelihood and severity across safety, privacy, fairness, and business domains.


#### ❌ MAP-5.2 - GAP

**Explanation:** There are no documented practices or assigned personnel for ongoing AI actor engagement and feedback integration.

**Recommendation:** Assign dedicated roles to manage ongoing stakeholder engagement and channel insights back into iterative risk mapping.

