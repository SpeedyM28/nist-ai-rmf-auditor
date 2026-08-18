# NIST AI RMF + ISO 42001 Audit Report

**Generated:** 2026-08-18 23:20:09

## Executive Summary

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 18 |
| Partial | 15 |
| Gaps | 4 |

**Compliance Rate:** 48.6%

---

## Detailed Findings

### NIST AI RMF


#### 🟡 GOVERN-1.1 - PARTIAL

**Explanation:** The text discusses aligning with applicable laws, regulations, and norms conceptually (Section 1.2.2), but lacks concrete procedures for tracking and documenting legal compliance across specific deployments.

**Recommendation:** Establish formal organizational procedures to identify, document, and track legal and regulatory requirements for all AI deployments.


#### ✅ GOVERN-1.2 - COMPLIANT

**Explanation:** Section 3 explicitly defines and integrates all key characteristics of trustworthy AI (valid/reliable, safe, secure/resilient, accountable/transparent, explainable/interpretable, privacy-enhanced, fair/bias managed).

**Recommendation:** Maintain periodic reviews to ensure operational AI projects actively implement and balance these trustworthy attributes.


#### 🟡 GOVERN-1.3 - PARTIAL

**Explanation:** Section 1.2.2 addresses risk tolerance conceptually, but does not provide defined criteria or thresholds for determining the depth of risk management activities.

**Recommendation:** Define explicit risk tolerance thresholds and quantitative/qualitative matrices to govern the depth of risk management activities.


#### 🟡 GOVERN-1.4 - PARTIAL

**Explanation:** Section 1.2.3 discusses risk prioritization and transparency, but actionable policies and priority metrics are not fully established in Part 1.

**Recommendation:** Formalize enterprise-wide AI risk prioritization policies and publish transparent risk management guidelines.


#### 🟡 GOVERN-1.5 - PARTIAL

**Explanation:** Sections 2 and 3 address continuous TEVV, testing, and monitoring throughout the lifecycle, but explicit review schedules and role definitions are incomplete.

**Recommendation:** Establish clear review schedules and assign dedicated operational roles for continuous AI system monitoring.


#### ❌ GOVERN-1.6 - GAP

**Explanation:** The text does not specify mechanisms or resourcing policies for maintaining a comprehensive inventory of AI systems.

**Recommendation:** Build and maintain a centralized AI system inventory resourced according to organizational risk priorities.


#### 🟡 GOVERN-1.7 - PARTIAL

**Explanation:** Section 1.2.3 notes that development and deployment should cease safely when risks are unacceptable, but lacks formal decommissioning workflows.

**Recommendation:** Develop explicit decommissioning and retirement procedures for AI systems to safely manage end-of-life transitions.


#### 🟡 GOVERN-2.1 - PARTIAL

**Explanation:** Section 2 and Figures 2/3 describe AI actors and lifecycle roles, but operational lines of communication and formal documentation standards are not detailed.

**Recommendation:** Document explicit RACI matrices and communication channels for AI risk mapping, measurement, and management.


#### ❌ GOVERN-2.2 - GAP

**Explanation:** The document does not detail personnel or partner AI risk management training programs, curricula, or competency standards.

**Recommendation:** Implement mandatory AI risk management training programs for all internal personnel and third-party partners.


#### 🟡 GOVERN-2.3 - PARTIAL

**Explanation:** Section 1.2.4 highlights senior leadership commitment and organizational culture, but lacks specific executive board decision-making mandates.

**Recommendation:** Institute executive AI governance committees with explicit sign-off authority for high-risk AI deployments.


#### ✅ GOVERN-3.1 - COMPLIANT

**Explanation:** Section 2 explicitly emphasizes that AI risk decision-making must be informed by demographically and disciplinarily diverse teams.

**Recommendation:** Establish formal diversity requirements and interdisciplinary review boards for AI project risk assessments.


#### 🟡 GOVERN-3.2 - PARTIAL

**Explanation:** Sections 1.2.1, 1.2.3, and 3.4 discuss human oversight and human baseline comparison, but concrete policies differentiating oversight roles are omitted.

**Recommendation:** Draft clear guidelines specifying human-in-the-loop, human-on-the-loop, and human-over-the-loop operational protocols.


#### ✅ GOVERN-4.1 - COMPLIANT

**Explanation:** Sections 1.2.3, 1.2.4, and 3.2 explicitly call for safety-first practices, risk-aware culture, and critical evaluation of contexts and impacts.

**Recommendation:** Reinforce safety-first culture through performance evaluations and regular safety review gates.


#### ✅ GOVERN-4.2 - COMPLIANT

**Explanation:** The text mandates documenting risks, potential impacts, residual risks (1.2.3), and harms to individuals and society (Section 1.1).

**Recommendation:** Standardize risk impact assessment (RIA) documentation templates across all development teams.


#### 🟡 GOVERN-4.3 - PARTIAL

**Explanation:** Sections 2, 3.1, and 3.2 highlight TEVV, real-time monitoring, and empirical incident evidence, but lack formal incident response and information sharing protocols.

**Recommendation:** Formulate an AI incident management framework including internal reporting and external information-sharing protocols.


#### ✅ GOVERN-5.1 - COMPLIANT

**Explanation:** Section 2 explicitly includes external civil society, end users, advocacy groups, and affected communities to inform risk context and impacts.

**Recommendation:** Establish formal public feedback mechanisms and stakeholder consultation channels.


#### 🟡 GOVERN-5.2 - PARTIAL

**Explanation:** The document highlights community input and semi-annual feedback integration, but lacks specific adjudication workflows.

**Recommendation:** Create formal adjudication procedures to systematically review and incorporate external stakeholder feedback.


#### ✅ GOVERN-6.1 - COMPLIANT

**Explanation:** Section 1.2.1 addresses third-party software/hardware/data risks, and Section 3.4 addresses intellectual property and copyright compliance.

**Recommendation:** Establish robust third-party AI vendor risk assessment protocols and copyright compliance auditing.


#### ❌ GOVERN-6.2 - GAP

**Explanation:** While third-party risks are identified in 1.2.1, specific contingency workflows for third-party failures or outages are not specified.

**Recommendation:** Develop business continuity and contingency plans specifically addressing third-party AI component failures.


#### ✅ MAP-1.1 - COMPLIANT

**Explanation:** Sections 1, 1.2.2, and 2 detail understanding intended purpose, application context, deployment settings, laws, and norms.

**Recommendation:** Require formal context-of-use documentation prior to model design and deployment.


#### ✅ MAP-1.2 - COMPLIANT

**Explanation:** Section 2 explicitly calls for interdisciplinary, demographically diverse teams across key lifecycle dimensions (Context, Data, Model, Task).

**Recommendation:** Implement interdisciplinary scoping workshops for all new AI initiatives.


#### 🟡 MAP-1.3 - PARTIAL

**Explanation:** Aligning decisions with organizational values and missions is mentioned conceptually (Exec Summary, 1.2.2), but explicit alignment steps are omitted.

**Recommendation:** Mandate explicit strategic alignment checks between proposed AI projects and core organizational goals.


#### 🟡 MAP-1.4 - PARTIAL

**Explanation:** Exec Summary and Section 1 discuss value and impact trade-offs, but formal business case re-evaluation procedures are missing.

**Recommendation:** Implement periodic business value and risk-benefit re-evaluations throughout the AI lifecycle.


#### ✅ MAP-1.5 - COMPLIANT

**Explanation:** Section 1.2.2 explicitly directs organizations to define, document, and adhere to reasonable risk tolerances.

**Recommendation:** Formalize a Risk Appetite Statement specifically governing AI system deployment thresholds.


#### ✅ MAP-1.6 - COMPLIANT

**Explanation:** Exec Summary and Section 2 detail the socio-technical nature of AI and requirement gathering across lifecycle dimensions.

**Recommendation:** Use socio-technical impact checklists during early-stage AI system requirements gathering.


#### 🟡 MAP-2.1 - PARTIAL

**Explanation:** Figure 2/3 and Section 2 cover the Task & Output dimension, but specific task mapping instructions are limited in the provided text.

**Recommendation:** Require detailed mapping of algorithm outputs to specific operational tasks and human workflows.


#### ✅ MAP-2.2 - COMPLIANT

**Explanation:** Sections 1.2.1 (inscrutability, model limits), 3.4, and 3.5 address documenting system limits, explainability, and human oversight.

**Recommendation:** Publish model cards or system transparency sheets defining operational boundaries and limits.


#### ✅ MAP-2.3 - COMPLIANT

**Explanation:** Section 2 and Figure 2 prominently feature TEVV (testing, evaluation, verification, validation) considerations throughout all lifecycle stages.

**Recommendation:** Standardize TEVV plan templates across all AI design and development pipelines.


#### ✅ MAP-3.1 - COMPLIANT

**Explanation:** Exec Summary, Section 1, and Figure 1 explicitly mandate evaluating and documenting positive impacts, opportunities, and benefits.

**Recommendation:** Document quantified and qualitative benefit assessments alongside risk profiles.


#### ✅ MAP-3.2 - COMPLIANT

**Explanation:** Section 1.1, 1.2.2, and Figure 1 address negative impacts, non-monetary costs (harms to people/planet), and trade-offs.

**Recommendation:** Conduct comprehensive harm and cost-benefit trade-off analyses prior to deployment.


#### 🟡 MAP-3.3 - PARTIAL

**Explanation:** Section 1.2.3 and 3 discuss application context and scope, but formal categorization and boundary standards are omitted in Part 1.

**Recommendation:** Enforce strict operational scope boundaries and out-of-scope usage guidelines for deployed models.


#### ❌ MAP-3.4 - GAP

**Explanation:** The text mentions human operators but lacks guidelines for defining, assessing, or documenting practitioner and operator proficiency.

**Recommendation:** Establish certification and training verification processes for all AI system operators.


#### ✅ MAP-3.5 - COMPLIANT

**Explanation:** Sections 1.2.1, 1.2.3, 3.1, and 3.4 emphasize human intervention, oversight mechanisms, and documentation.

**Recommendation:** Document escalation protocols and intervention controls for human oversight teams.


#### ✅ MAP-4.1 - COMPLIANT

**Explanation:** Section 1.2.1 addresses third-party hardware/software/data risks, and Section 3.4 covers copyright and legal risk mapping.

**Recommendation:** Perform legal and technology supply-chain risk mapping for all third-party AI assets.


#### 🟡 MAP-4.2 - PARTIAL

**Explanation:** Section 1.2.1 identifies third-party risk factors and safeguards, but detailed control frameworks for components are not specified.

**Recommendation:** Catalog specific technical and administrative controls applied to third-party models and data.


#### ✅ MAP-5.1 - COMPLIANT

**Explanation:** Section 1.1 explicitly defines risk as probability and magnitude of consequences across various harm categories.

**Recommendation:** Standardize likelihood-severity risk scoring matrices across all AI risk evaluations.


#### ✅ MAP-5.2 - COMPLIANT

**Explanation:** Section 2 details ongoing engagement with diverse AI actors across inner and outer lifecycle dimensions to integrate feedback.

**Recommendation:** Assign dedicated stakeholder engagement roles to lead continuous feedback loops.

