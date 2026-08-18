# NIST AI RMF + ISO 42001 Audit Report

**Generated:** 2026-08-18 22:53:38

## Executive Summary

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 3 |
| Partial | 11 |
| Gaps | 23 |

**Compliance Rate:** 8.1%

---

## Detailed Findings

### NIST AI RMF


#### ❌ GOVERN-1.1 - GAP

**Explanation:** The policy does not address legal, regulatory, or compliance requirements related to AI development and deployment.

**Recommendation:** Add explicit policy language requiring the identification, documentation, and compliance monitoring of all applicable AI legal and regulatory requirements.


#### ✅ GOVERN-1.2 - COMPLIANT

**Explanation:** Section 3 explicitly articulates core trustworthy AI principles (fairness, transparency, safety, privacy) and Section 4-6 integrate them into governance and monitoring practices.

**Recommendation:** Maintain principles and expand operational procedures to detail how each trustworthy characteristic is measured.


#### 🟡 GOVERN-1.3 - PARTIAL

**Explanation:** Section 4 references 'high-risk AI systems,' indicating risk level awareness, but fails to define risk management procedures or organizational risk tolerance guidelines.

**Recommendation:** Define organizational risk tolerance thresholds and implement a structured risk categorization framework.


#### 🟡 GOVERN-1.4 - PARTIAL

**Explanation:** The policy outlines high-level governance structures, but lacks formal, published procedures detailing transparent risk management controls and prioritization.

**Recommendation:** Publish detailed risk management procedures and establish transparent criteria for risk prioritization based on organizational values.


#### 🟡 GOVERN-1.5 - PARTIAL

**Explanation:** Section 6 specifies performance monitoring and incident reporting, but lacks provisions for periodic review of the AI risk management framework itself.

**Recommendation:** Incorporate requirements for regular (e.g., annual) reviews of the AI governance policy and risk management process outcomes.


#### ❌ GOVERN-1.6 - GAP

**Explanation:** The policy does not establish mechanisms or requirements for maintaining an inventory of organizational AI systems.

**Recommendation:** Establish a centralized AI asset inventory process to register and track all internal and third-party AI models across their lifecycle.


#### ❌ GOVERN-1.7 - GAP

**Explanation:** The policy contains no provisions for the safe decommissioning, phase-out, or retirement of AI systems.

**Recommendation:** Develop explicit procedures for model decommissioning, addressing data retention, model archival, and risk control during phase-out.


#### 🟡 GOVERN-2.1 - PARTIAL

**Explanation:** Section 4 assigns general oversight to the CTO and Governance Committee, but specific roles, lines of communication, and responsibilities for risk mapping and measuring are omitted.

**Recommendation:** Document clear operational roles and cross-departmental communication workflows for AI risk mapping, measurement, and mitigation.


#### ❌ GOVERN-2.2 - GAP

**Explanation:** The policy makes no mention of AI risk management training, awareness, or competency requirements for personnel or external partners.

**Recommendation:** Institute mandatory, role-based AI risk management and ethics training for all personnel and third-party partners involved in AI operations.


#### ✅ GOVERN-2.3 - COMPLIANT

**Explanation:** Section 4 designates the Chief Technology Officer (CTO) and AI Governance Committee as responsible for overseeing AI initiatives and reviewing high-risk systems.

**Recommendation:** Document executive decision thresholds and formalize escalation paths for critical AI risk acceptances.


#### ❌ GOVERN-3.1 - GAP

**Explanation:** The policy does not mandate interdisciplinary or demographic diversity within the AI Governance Committee or risk decision-making teams.

**Recommendation:** Require interdisciplinary representation (e.g., legal, compliance, ethics, domain experts, diverse backgrounds) on the AI Governance Committee.


#### ❌ GOVERN-3.2 - GAP

**Explanation:** The policy does not define or differentiate roles and responsibilities for human-AI interaction or levels of human oversight.

**Recommendation:** Formally define operational standards for human-in-the-loop, human-on-the-loop, and human-out-of-the-loop oversight mechanisms.


#### 🟡 GOVERN-4.1 - PARTIAL

**Explanation:** Section 3 and Section 5 advocate for safety and security validation, but the policy lacks programmatic measures to foster a critical thinking and safety-first culture.

**Recommendation:** Incorporate policy directives encouraging safety-first mindsets, ethical challenge channels, and critical assessment incentives across AI development teams.


#### ❌ GOVERN-4.2 - GAP

**Explanation:** The policy does not require organizational teams to document identified AI risks and potential impacts.

**Recommendation:** Mandate Risk Impact Assessments (RIAs) and risk logs for all AI projects prior to design and deployment phases.


#### ✅ GOVERN-4.3 - COMPLIANT

**Explanation:** Section 5 mandates pre-deployment testing on representative data, and Section 6 requires performance monitoring and incident reporting to security.

**Recommendation:** Establish clear protocols for broader information sharing and post-incident lessons-learned dissemination.


#### ❌ GOVERN-5.1 - GAP

**Explanation:** The policy contains no mechanisms to gather or integrate external stakeholder feedback regarding societal or individual impacts.

**Recommendation:** Implement formal mechanisms (e.g., public feedback channels, external impact reviews) to collect external stakeholder input on high-impact AI systems.


#### ❌ GOVERN-5.2 - GAP

**Explanation:** The policy lacks processes to regularly incorporate adjudicated feedback from AI actors into system design updates.

**Recommendation:** Define a feedback integration workflow ensuring stakeholder input is formally evaluated and incorporated into ongoing AI model iterations.


#### 🟡 GOVERN-6.1 - PARTIAL

**Explanation:** Section 7 states third-party AI must be reviewed before integration, but does not explicitly address intellectual property infringement or broader supply chain risks.

**Recommendation:** Expand third-party policy terms to explicitly mandate review of intellectual property rights, data provenance, and vendor security posture.


#### ❌ GOVERN-6.2 - GAP

**Explanation:** The policy provides no contingency plans or failure management processes for third-party AI dependencies.

**Recommendation:** Formulate explicit business continuity and contingency response plans for failures, deprecations, or vulnerabilities in third-party AI systems.


#### ❌ MAP-1.1 - GAP

**Explanation:** The policy does not require documenting intended purposes, beneficial uses, deployment settings, or legal contexts for individual AI systems.

**Recommendation:** Require project charters or context documents for all AI projects documenting intended scope, deployment context, and relevant legal/ethical norms.


#### ❌ MAP-1.2 - GAP

**Explanation:** The policy does not require interdisciplinary teams or demographic diversity when establishing system context.

**Recommendation:** Mandate that early-stage context mapping and problem definition include multi-disciplinary stakeholders representing varied domains and backgrounds.


#### 🟡 MAP-1.3 - PARTIAL

**Explanation:** Section 1 and Section 3 outline general policy purpose and principles, but do not mandate that individual AI deployments explicitly align with documented strategic AI goals.

**Recommendation:** Require project proposals to document explicit alignment with organizational business strategy and responsible AI mission goals.


#### ❌ MAP-1.4 - GAP

**Explanation:** The policy does not require defining or re-evaluating the business value or business context of AI systems.

**Recommendation:** Establish requirements for business value definition and periodic review during system lifecycle audits.


#### ❌ MAP-1.5 - GAP

**Explanation:** Organizational risk tolerance levels for AI activities are neither defined nor required to be documented.

**Recommendation:** Define and document qualitative and quantitative risk tolerance thresholds for AI applications.


#### ❌ MAP-1.6 - GAP

**Explanation:** The policy omits requirements for requirement elicitation from relevant AI actors and socio-technical design considerations.

**Recommendation:** Incorporate socio-technical analysis into initial AI system design and requirement specification processes.


#### ❌ MAP-2.1 - GAP

**Explanation:** The policy does not require defining or documenting the specific tasks and implementation methods supported by AI systems.

**Recommendation:** Require detailed technical design specifications outlining specific algorithmic methods, inputs, and functional tasks per system.


#### ❌ MAP-2.2 - GAP

**Explanation:** The policy does not mandate documenting system knowledge limits, potential edge-case failures, or human oversight boundaries.

**Recommendation:** Require standardized Model Cards or System Cards detailing model limitations, confidence bounds, and operational constraints.


#### 🟡 MAP-2.3 - PARTIAL

**Explanation:** Section 5 mandates validation with representative data and security reviews, but does not formalize full Testing, Evaluation, Verification, and Validation (TEVV) procedures.

**Recommendation:** Develop a formal TEVV framework encompassing scientific integrity standards, continuous evaluation, and verification methodologies.


#### ❌ MAP-3.1 - GAP

**Explanation:** The policy does not mandate examining or documenting potential benefits of AI systems during the mapping phase.

**Recommendation:** Include benefit assessment templates in project charters to document expected performance and functional value.


#### ❌ MAP-3.2 - GAP

**Explanation:** The policy omits requirements to assess and document potential monetary and non-monetary costs resulting from system errors.

**Recommendation:** Mandate cost-benefit and impact analysis including potential harm, reputation risk, and operational costs associated with model errors.


#### ❌ MAP-3.3 - GAP

**Explanation:** The policy does not require defining or documenting targeted application scope based on system categorization and capabilities.

**Recommendation:** Require explicit scope boundaries and forbidden use-cases to be documented for each deployed AI model.


#### ❌ MAP-3.4 - GAP

**Explanation:** The policy contains no provisions for assessing, defining, or documenting practitioner/operator proficiency.

**Recommendation:** Implement operator proficiency evaluations and certified operating standards before granting deployment/operational permissions.


#### 🟡 MAP-3.5 - PARTIAL

**Explanation:** Section 4 establishes high-level governance review prior to deployment, but lacks operational procedures for ongoing human oversight during live operations.

**Recommendation:** Detail operational human oversight protocols, including monitoring cadence, override authority, and escalation paths during production.


#### 🟡 MAP-4.1 - PARTIAL

**Explanation:** Section 7 requires reviewing third-party systems, but lacks systematic procedures for mapping technical and legal risks of internal and external components.

**Recommendation:** Implement a standardized risk mapping methodology for all AI components, open-source libraries, and third-party APIs.


#### 🟡 MAP-4.2 - PARTIAL

**Explanation:** Sections 5 and 7 mention validation and security reviews, but lack documented internal control standards for specific AI components.

**Recommendation:** Establish documented internal risk control baselines for data pipelines, feature engineering, model code, and third-party integrations.


#### ❌ MAP-5.1 - GAP

**Explanation:** The policy does not mandate analyzing or documenting the likelihood and magnitude of potential AI impacts.

**Recommendation:** Require quantitative or qualitative impact scoring (evaluating likelihood vs. severity) for all mapped risks during system design.


#### ❌ MAP-5.2 - GAP

**Explanation:** No policy provisions exist for ongoing stakeholder engagement or feedback integration into risk mapping records.

**Recommendation:** Assign responsible roles to maintain ongoing feedback loops with AI actors and update risk mapping documentation continuously.

