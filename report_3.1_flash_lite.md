# NIST AI RMF + ISO 42001 Audit Report

**Generated:** 2026-08-18 21:28:33

## Executive Summary

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 1 |
| Partial | 5 |
| Gaps | 31 |

**Compliance Rate:** 2.7%

---

## Detailed Findings

### NIST AI RMF


#### ❌ GOVERN-1.1 - GAP

**Explanation:** The policy lacks any mention of legal, regulatory, or compliance obligations.

**Recommendation:** Add a section addressing compliance with applicable laws, regulations, and industry standards.


#### ✅ GOVERN-1.2 - COMPLIANT

**Explanation:** Section 3 explicitly lists principles for trustworthy AI.

**Recommendation:** None.


#### 🟡 GOVERN-1.3 - PARTIAL

**Explanation:** The policy mentions a 'high-risk' review, but does not define a process for determining risk tolerance or systematic risk management.

**Recommendation:** Document the criteria for determining 'high-risk' and the organization's risk tolerance levels.


#### ❌ GOVERN-1.4 - GAP

**Explanation:** There is no mention of a structured risk management process or transparency in outcomes.

**Recommendation:** Define a formal AI risk management framework/process to be followed for all AI deployments.


#### 🟡 GOVERN-1.5 - PARTIAL

**Explanation:** Monitoring is mentioned in Section 6, but roles and responsibilities for reviewing the risk management process itself are undefined.

**Recommendation:** Explicitly assign roles for the periodic review of the AI risk management process.


#### ❌ GOVERN-1.6 - GAP

**Explanation:** The policy does not mention maintaining an AI system inventory.

**Recommendation:** Require the maintenance of an AI system inventory, including details on model provenance and purpose.


#### ❌ GOVERN-1.7 - GAP

**Explanation:** There are no guidelines regarding the decommissioning or retirement of AI systems.

**Recommendation:** Add a clause on the safe retirement and decommissioning of AI systems.


#### 🟡 GOVERN-2.1 - PARTIAL

**Explanation:** The CTO and Governance Committee are mentioned, but specific lines of communication are not defined.

**Recommendation:** Clarify the escalation paths and communication protocols for AI risk management.


#### ❌ GOVERN-2.2 - GAP

**Explanation:** No training requirements are mentioned.

**Recommendation:** Mandate AI risk management training for all personnel involved in AI lifecycles.


#### 🟡 GOVERN-2.3 - PARTIAL

**Explanation:** The CTO is assigned oversight, but explicit executive accountability for final deployment decisions is missing.

**Recommendation:** State clearly that executive leadership retains final accountability for AI system deployment risks.


#### ❌ GOVERN-3.1 - GAP

**Explanation:** There is no requirement for a diverse, interdisciplinary team in the governance process.

**Recommendation:** Require that the AI Governance Committee be comprised of diverse, interdisciplinary members.


#### ❌ GOVERN-3.2 - GAP

**Explanation:** The policy does not address human-AI configuration or oversight roles.

**Recommendation:** Define requirements for human-in-the-loop oversight and clear boundaries for human-AI interaction.


#### ❌ GOVERN-4.1 - GAP

**Explanation:** The policy focuses on rules but does not address fostering a 'safety-first' culture.

**Recommendation:** Include a statement on promoting a culture of safety and critical thinking regarding AI impact.


#### ❌ GOVERN-4.2 - GAP

**Explanation:** No documentation requirements for risk assessments are mandated beyond general review.

**Recommendation:** Require formal documentation of risk assessments, impact analyses, and mitigation strategies.


#### 🟡 GOVERN-4.3 - PARTIAL

**Explanation:** Testing and incident reporting are mentioned, but formal information-sharing mechanisms are absent.

**Recommendation:** Establish a process for sharing AI incident information internally and, where applicable, externally.


#### ❌ GOVERN-5.1 - GAP

**Explanation:** No mechanism exists for collecting feedback from stakeholders outside the organization.

**Recommendation:** Establish a public or stakeholder feedback loop for societal/individual impacts.


#### ❌ GOVERN-5.2 - GAP

**Explanation:** No process to incorporate feedback into the design iteration.

**Recommendation:** Mandate that feedback be analyzed and integrated into subsequent AI system updates.


#### 🟡 GOVERN-6.1 - PARTIAL

**Explanation:** Third-party reviews are mentioned, but intellectual property and legal risk to third parties are not explicitly covered.

**Recommendation:** Expand the third-party policy to include intellectual property rights and liability assessments.


#### ❌ GOVERN-6.2 - GAP

**Explanation:** No contingency planning for high-risk third-party system failures.

**Recommendation:** Require contingency/business continuity plans for high-risk third-party AI dependencies.


#### ❌ MAP-1.1 - GAP

**Explanation:** The policy does not require mapping or documentation of system context or intended purpose.

**Recommendation:** Require a 'Statement of Intended Purpose' for every AI project.


#### ❌ MAP-1.2 - GAP

**Explanation:** No mention of team diversity in mapping tasks.

**Recommendation:** Mandate the use of diverse teams for AI context mapping.


#### ❌ MAP-1.3 - GAP

**Explanation:** No requirement for aligning AI with mission goals.

**Recommendation:** Ensure AI system business value is documented against organization goals.


#### ❌ MAP-1.4 - GAP

**Explanation:** No formal requirement to define or re-evaluate business value.

**Recommendation:** Include a mandatory business value assessment during the project proposal phase.


#### ❌ MAP-1.5 - GAP

**Explanation:** Risk tolerance not defined or documented.

**Recommendation:** Develop and communicate an organizational risk appetite statement.


#### ❌ MAP-1.6 - GAP

**Explanation:** Socio-technical implications are not addressed.

**Recommendation:** Mandate a socio-technical impact assessment for all new AI systems.


#### ❌ MAP-2.1 - GAP

**Explanation:** Task definition is not required.

**Recommendation:** Document clear task definitions and methodology for all AI models.


#### ❌ MAP-2.2 - GAP

**Explanation:** Knowledge limits are not discussed.

**Recommendation:** Require developers to document known limitations and boundaries of AI systems.


#### 🟡 MAP-2.3 - PARTIAL

**Explanation:** Validation and security are mentioned, but TEVV (Test, Evaluate, Verify, and Validate) as a scientific discipline is missing.

**Recommendation:** Formalize the TEVV approach in the development standards.


#### ❌ MAP-3.1 - GAP

**Explanation:** Benefits are not formally documented.

**Recommendation:** Add a requirement to document expected benefits and KPIs for AI systems.


#### ❌ MAP-3.2 - GAP

**Explanation:** Non-monetary costs/impacts are not addressed.

**Recommendation:** Include an analysis of potential societal or ethical costs in the risk assessment.


#### ❌ MAP-3.3 - GAP

**Explanation:** Application scope is not required to be specified.

**Recommendation:** Mandate the documentation of clear application boundaries.


#### ❌ MAP-3.4 - GAP

**Explanation:** No proficiency standards for operators defined.

**Recommendation:** Define training requirements for end-users and operators of AI systems.


#### ❌ MAP-3.5 - GAP

**Explanation:** Oversight processes are not documented.

**Recommendation:** Require documentation of manual override procedures and oversight protocols.


#### ❌ MAP-4.1 - GAP

**Explanation:** Legal risk mapping for components is absent.

**Recommendation:** Implement a supply chain assessment that includes legal and IP risk reviews.


#### ❌ MAP-4.2 - GAP

**Explanation:** No requirement for internal risk controls for AI components.

**Recommendation:** Implement a controls matrix for individual AI system components.


#### ❌ MAP-5.1 - GAP

**Explanation:** Impact magnitude and likelihood are not required to be documented.

**Recommendation:** Adopt a formal likelihood/impact assessment matrix.


#### ❌ MAP-5.2 - GAP

**Explanation:** No process for engagement with AI actors.

**Recommendation:** Formalize stakeholder engagement timelines and processes.

