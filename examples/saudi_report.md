# NCA-ECC AI Control Gap Analysis (Mapped from NIST AI RMF)

**Generated:** 2026-09-02 19:24:45

**Note:** This report maps NIST AI RMF 1.0 requirements to Saudi NCA-ECC controls. The LLM audited against NIST AI RMF; the control IDs have been translated to their NCA-ECC equivalents for KSA regulatory alignment.

## Executive Summary

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 2 |
| Partial | 10 |
| Gaps | 25 |

**Compliance Rate:** 5.4%

---

## Detailed Findings

### NCA-ECC Controls (Derived from NIST AI RMF)


#### ✅ NCA-ECC 5-1 (Legal & Regulatory Compliance) (mapped from GOVERN-1.1) - COMPLIANT

**Explanation:** Section 1 explicitly mandates compliance with applicable laws/regulations across all operating jurisdictions and assigns the Legal Department to maintain a register of AI-specific legal obligations with mandatory breach reporting.

**Recommendation:** Establish a periodic audit cycle for the legal register and define dynamic procedures for updating it as AI regulations rapidly evolve globally.


#### ❌ NCA-ECC 5-2 (Trustworthy AI Integration) (mapped from GOVERN-1.2) - GAP

**Explanation:** The policy references 'responsible AI' generally in Section 6, but fails to define or integrate key characteristics of trustworthy AI (validity, reliability, safety, security, resilience, fairness, privacy, and transparency) into operational policies.

**Recommendation:** Formally incorporate NIST/ISO trustworthy AI principles into the policy, detailing operational benchmarks and criteria for each characteristic.


#### ❌ NCA-ECC 6-1 (Risk Tolerance & Assessment) (mapped from GOVERN-1.3) - GAP

**Explanation:** Section 6 explicitly notes that risk appetite is 'not formally documented or quantified' and business leaders make ad-hoc decisions, failing to establish risk-tolerance-based management processes.

**Recommendation:** Develop and document a formal Risk Appetite Statement with quantitative and qualitative thresholds tied to standardized risk management tiers.


#### ❌ NCA-ECC 6-2 (Risk Management Transparency) (mapped from GOVERN-1.4) - GAP

**Explanation:** Risk management decisions are made on an ad-hoc, unquantified basis (Section 6), and inventory resourcing is unaligned with risk levels (Section 2), indicating a lack of transparent, priority-based policies.

**Recommendation:** Establish standard operating procedures for risk management that mandate transparent risk scoring, consistent criteria, and documented risk prioritization.


#### ✅ NCA-ECC 7-1 (Monitoring & Review) (mapped from GOVERN-1.5) - COMPLIANT

**Explanation:** Section 3 defines regular monitoring (semi-annual reviews by the AI Governance Board) covering drift, accuracy, and user complaints, with clear roles and documented reporting to stakeholders.

**Recommendation:** Expand monitoring scope beyond high-risk systems to include continuous/automated alerting mechanisms and clear review cadences for medium-risk systems.


#### 🟡 NCA-ECC 5-3 (AI System Inventory) (mapped from GOVERN-1.6) - PARTIAL

**Explanation:** Section 2 establishes a quarterly updated AI system inventory spreadsheet, but explicitly states that maintenance and resource allocation are on a 'best-effort basis' with no alignment to risk levels.

**Recommendation:** Transition from a basic spreadsheet to an automated inventory tool and mandate that inventory maintenance and evaluation resources be scaled according to risk severity.


#### ❌ NCA-ECC 9-1 (Decommissioning & Phase-out) (mapped from GOVERN-1.7) - GAP

**Explanation:** The policy contains no provisions, procedures, or requirements for decommissioning, retiring, or safely phasing out AI systems.

**Recommendation:** Add a dedicated Decommissioning & Retirement section specifying data retention, model sunsetting, user notification, and residual risk assessment procedures.


#### 🟡 NCA-ECC 6-3 (Roles & Communication) (mapped from GOVERN-2.1) - PARTIAL

**Explanation:** Section 1, Section 2, and Section 3 assign specific duties to the Legal Dept, CTO, CCO, and AI Governance Board, but lines of communication for mapping and measuring specific risks across the lifecycle remain unarticulated.

**Recommendation:** Create a detailed Responsible, Accountable, Consulted, and Informed (RACI) matrix for mapping, measuring, and managing AI risks across all lifecycle stages.


#### ❌ NCA-ECC 6-4 (Training & Competency) (mapped from GOVERN-2.2) - GAP

**Explanation:** Section 5 explicitly waives training and competency assessments for operators reviewing AI outputs ('No formal training or competency assessment is required').

**Recommendation:** Mandate baseline and ongoing AI risk management and operational competency training for all personnel and third-party human reviewers.


#### 🟡 NCA-ECC 6-5 (Executive Accountability) (mapped from GOVERN-2.3) - PARTIAL

**Explanation:** Executive roles (CTO, CCO) are involved in monitoring and inventory oversight, but business leaders are permitted to make ad-hoc risk decisions without formal executive oversight or risk sign-off.

**Recommendation:** Institute a formal executive governance approval policy where designated senior officers sign off on deployment risk assessments based on established thresholds.


#### ❌ NCA-ECC 5-4 (Diverse Decision-Making) (mapped from GOVERN-3.1) - GAP

**Explanation:** The policy does not require or mention interdisciplinary or diverse team participation in AI risk assessment or decision-making.

**Recommendation:** Mandate that AI risk governance committees and evaluation teams include interdisciplinary roles (e.g., ethics, domain expertise, legal, technical, and end-user representatives).


#### 🟡 NCA-ECC 5-5 (Human-AI Oversight Roles) (mapped from GOVERN-3.2) - PARTIAL

**Explanation:** Section 5 mandates human review for customer-facing decisions, but fails to define operational roles, escalation protocols, or guidelines for non-customer-facing systems.

**Recommendation:** Detail specific Human-in-the-Loop (HITL), Human-on-the-Loop (HOTL), and Human-out-of-the-Loop (HOOTL) operational guidelines and escalation workflows.


#### ❌ NCA-ECC 7-2 (Safety Culture) (mapped from GOVERN-4.1) - GAP

**Explanation:** The policy lacks provisions promoting a safety-first mindset, critical thinking, or a culture of responsible AI innovation.

**Recommendation:** Include clear policy directives that empower employees to raise AI safety concerns (whistleblower/stop-work authority) without fear of retaliation.


#### ❌ NCA-ECC 7-3 (Risk Documentation) (mapped from GOVERN-4.2) - GAP

**Explanation:** There is no policy requirement for project teams to perform or document formal risk and impact assessments during AI design, development, or deployment.

**Recommendation:** Require mandatory AI Impact Assessments (AIIA) and Risk Registers for all AI projects prior to moving into production.


#### 🟡 NCA-ECC 7-4 (Testing & Incident Sharing) (mapped from GOVERN-4.3) - PARTIAL

**Explanation:** Section 3 covers periodic tracking of metrics (drift, accuracy, user complaints) and Section 1 mandates reporting legal non-compliance, but formal incident management and cross-team information sharing procedures are absent.

**Recommendation:** Implement a formal AI Incident Response Plan (AI-IRP) detailing identification, containment, post-incident root cause analysis, and internal/external information sharing.


#### 🟡 NCA-ECC 8-1 (External Feedback) (mapped from GOVERN-5.1) - PARTIAL

**Explanation:** Section 3 mentions reviewing 'user complaints' semi-annually, but there is no systematic mechanism to actively engage, collect, or prioritize feedback from external stakeholders or impacted communities.

**Recommendation:** Establish external feedback submission channels and formal intake processes for external stakeholders and impacted communities.


#### ❌ NCA-ECC 8-2 (Feedback Integration) (mapped from GOVERN-5.2) - GAP

**Explanation:** The policy lacks processes to adjudicate feedback and systematically feed insights back into system design, retraining, or implementation iterations.

**Recommendation:** Define a closed-loop feedback mechanism requiring product teams to document how external and operational feedback directly impacts model updates and retrainings.


#### 🟡 NCA-ECC 10-1 (Third-Party Risk) (mapped from GOVERN-6.1) - PARTIAL

**Explanation:** Section 4 requires vendors to provide SOC 2 Type II reports, but fails to address broader third-party AI risks such as IP infringement, data leakage, or vendor model bias.

**Recommendation:** Expand third-party vendor risk assessments to cover IP indemnification, data usage policies, shadow AI usage, and vendor bias evaluations.


#### ❌ NCA-ECC 10-2 (Third-Party Contingency) (mapped from GOVERN-6.2) - GAP

**Explanation:** Section 4 explicitly states that 'no formal contingency processes exist if a critical third-party AI service experiences an outage, fails, or unexpectedly changes its model behavior.'

**Recommendation:** Develop business continuity and contingency plans (e.g., model fallback options, multi-provider architecture, prompt regression testing) for critical vendor AI dependencies.


#### ❌ NCA-ECC 5-6 (Context & Deployment) (mapped from MAP-1.1) - GAP

**Explanation:** The policy document contains no requirements to document intended purposes, deployment contexts, or societal expectations for individual AI models.

**Recommendation:** Mandate the completion of standardized System Description and Context Templates (e.g., AI Model Cards) for every project prior to development.


#### ❌ NCA-ECC 5-7 (Interdisciplinary Context) (mapped from MAP-1.2) - GAP

**Explanation:** There are no requirements to assemble interdisciplinary teams or leverage diverse skills when mapping context and risk.

**Recommendation:** Incorporate interdisciplinary review requirements into the project intake process, specifying domain expertise and stakeholder perspectives required.


#### ❌ NCA-ECC 6-6 (Mission Alignment) (mapped from MAP-1.3) - GAP

**Explanation:** The policy does not mandate alignment of AI projects with broader organizational mission, ethics, or strategic goals.

**Recommendation:** Require business cases for AI systems to document alignment with Acme Corp's mission and ethical values during project initiation.


#### ❌ NCA-ECC 6-7 (Business Value) (mapped from MAP-1.4) - GAP

**Explanation:** Business value and context of use are not required to be documented or periodically re-evaluated under current policy.

**Recommendation:** Add a requirement to capture business value metrics and re-evaluate context during semi-annual model reviews.


#### ❌ NCA-ECC 6-8 (Risk Tolerance Documentation) (mapped from MAP-1.5) - GAP

**Explanation:** Section 6 explicitly notes that risk appetite is unquantified and not formally documented.

**Recommendation:** Define formal organizational risk tolerance thresholds (e.g., unacceptable error rates, bias impact thresholds) to inform risk mapping.


#### ❌ NCA-ECC 6-9 (Socio-Technical Requirements) (mapped from MAP-1.6) - GAP

**Explanation:** The policy does not mandate socio-technical impact considerations or multi-actor requirement elicitation during AI system design.

**Recommendation:** Integrate socio-technical assessment guidelines into product development lifecycles to evaluate human-system interaction risks.


#### ❌ NCA-ECC 4-1 (Tasks & Methods) (mapped from MAP-2.1) - GAP

**Explanation:** The policy does not require defining or mapping specific tasks and implementation methods for AI models.

**Recommendation:** Require detailed system functional documentation outlining tasks, model architecture, and input/output parameters.


#### 🟡 NCA-ECC 4-2 (Limits & Oversight) (mapped from MAP-2.2) - PARTIAL

**Explanation:** Section 5 notes human oversight for customer decisions, but does not require documenting model knowledge limits, edge cases, or failure modes.

**Recommendation:** Mandate documentation of model operational boundaries, known limitations, confidence thresholds, and failure modes for operator reference.


#### ❌ NCA-ECC 4-3 (Scientific Integrity & TEVV) (mapped from MAP-2.3) - GAP

**Explanation:** Testing, Evaluation, Verification, and Validation (TEVV) concepts and scientific integrity standards are absent from the document.

**Recommendation:** Establish formal TEVV protocols requiring pre-deployment validation, scientific rigor, and documented benchmarks.


#### ❌ NCA-ECC 4-4 (Benefits Documentation) (mapped from MAP-3.1) - GAP

**Explanation:** The policy does not direct teams to analyze or document the specific intended benefits of AI deployment.

**Recommendation:** Include a cost-benefit analysis requirement in the AI intake process assessing positive value against potential risk.


#### ❌ NCA-ECC 4-5 (Cost & Error Analysis) (mapped from MAP-3.2) - GAP

**Explanation:** Potential non-monetary costs, error consequences, and negative societal externalities are not required to be assessed.

**Recommendation:** Mandate systematic error-mode analysis assessing potential harm to end-users, privacy impact, and reputation risks.


#### ❌ NCA-ECC 4-6 (Application Scope) (mapped from MAP-3.3) - GAP

**Explanation:** The policy scope is enterprise-wide, but there is no requirement to define application-specific boundaries or scope categorizations per model.

**Recommendation:** Require precise scoping statements for each deployment, defining explicitly permitted and prohibited use cases.


#### ❌ NCA-ECC 4-7 (Operator Proficiency) (mapped from MAP-3.4) - GAP

**Explanation:** Section 5 explicitly disclaims training or competency requirements for operators approving AI outputs.

**Recommendation:** Implement formal proficiency assessments and mandatory training certifications for AI operators prior to granting approval authority.


#### 🟡 NCA-ECC 4-8 (Human Oversight Processes) (mapped from MAP-3.5) - PARTIAL

**Explanation:** Section 5 establishes a mandatory human review rule, but lacks formal procedures for evaluating, assessing, or documenting the effectiveness of oversight.

**Recommendation:** Define operational metrics to evaluate human reviewer effectiveness (e.g., override rates, agreement latency, review thoroughness audits).


#### 🟡 NCA-ECC 10-3 (Third-Party Risk Mapping) (mapped from MAP-4.1) - PARTIAL

**Explanation:** Section 1 mandates tracking legal obligations, but fails to establish comprehensive mapping procedures for technological and legal risks across system components.

**Recommendation:** Establish a component-level risk mapping protocol assessing open-source licenses, training data rights, and technical vulnerability risks.


#### 🟡 NCA-ECC 10-4 (Internal Risk Controls) (mapped from MAP-4.2) - PARTIAL

**Explanation:** Section 4 addresses vendor SOC 2 reports, but internal control mapping for third-party AI models and integration points is missing.

**Recommendation:** Document internal control requirements (e.g., input filtering, API rate-limiting, output guardrails) for all integrated third-party AI tools.


#### ❌ NCA-ECC 11-1 (Impact Characterization) (mapped from MAP-5.1) - GAP

**Explanation:** There are no provisions requiring systematic assessment of impact likelihood and magnitude based on deployment history or public incident reports.

**Recommendation:** Adopt a standardized risk matrix assessing likelihood vs. severity/magnitude of adverse events for every AI deployment.


#### ❌ NCA-ECC 11-2 (Engagement & Feedback) (mapped from MAP-5.2) - GAP

**Explanation:** The policy lacks frameworks for regular actor engagement and systematic feedback integration during context mapping.

**Recommendation:** Establish structured regular engagement cycles with end-users and impacted parties to continually refine risk mapping assumptions.

