# NIST AI RMF + ISO 42001 Audit Report

**Generated:** 2026-08-18 22:47:55

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

**Explanation:** The policy does not mention understanding, managing, or documenting legal and regulatory compliance requirements related to AI.

**Recommendation:** Add a dedicated legal and regulatory compliance section requiring regular auditing of AI systems against applicable international, national, and local laws.


#### 🟡 GOVERN-1.2 - PARTIAL

**Explanation:** Section 3 outlines trustworthy AI principles (fairness, transparency, safety, privacy), but the policy lacks detail on how these are systematically integrated into actual operational procedures and business practices.

**Recommendation:** Expand Section 5 (Development Standards) and Section 6 (Monitoring) to define the specific procedures used to enforce and verify these principles.


#### 🟡 GOVERN-1.3 - PARTIAL

**Explanation:** Section 4 references 'high-risk AI systems' undergoing review, but the policy does not define organizational risk tolerance levels or establish a formal risk assessment framework.

**Recommendation:** Define risk tolerance thresholds and establish a formal methodology for categorizing AI systems based on their risk level (e.g., Low, Medium, High).


#### 🟡 GOVERN-1.4 - PARTIAL

**Explanation:** While basic governance structures (CTO and Governance Committee) are introduced, there is no comprehensive risk management process based on prioritized organizational risk tolerances.

**Recommendation:** Document a formal AI Risk Management process outlining how risks are systematically identified, mitigated, and tracked.


#### 🟡 GOVERN-1.5 - PARTIAL

**Explanation:** Section 6 establishes monitoring of systems for drift and incidents, but there is no mandate to periodically review and update the AI risk management process itself.

**Recommendation:** Add a requirement for an annual executive review and third-party audit of the AI policy and risk management framework.


#### ❌ GOVERN-1.6 - GAP

**Explanation:** The policy makes no mention of establishing or keeping an inventory of AI systems.

**Recommendation:** Mandate the creation and maintenance of a centralized AI Asset Register to track all developed, procured, and deployed AI systems.


#### ❌ GOVERN-1.7 - GAP

**Explanation:** Decommissioning, phase-out, or retirement procedures for AI systems are completely unaddressed.

**Recommendation:** Incorporate decommissioning guidelines to ensure that retired models and their data dependencies are safely disabled, archived, and deleted.


#### 🟡 GOVERN-2.1 - PARTIAL

**Explanation:** Section 4 assigns overall oversight to the CTO and Governance Committee, but it does not clarify the precise operational lines of communication and duties for managing AI risks.

**Recommendation:** Define the precise responsibilities of development, security, and operational teams in mapping, measuring, and reporting risks to the Governance Committee.


#### ❌ GOVERN-2.2 - GAP

**Explanation:** Training, awareness, or competency requirements for personnel managing AI risks are not mentioned.

**Recommendation:** Add a clause mandating regular AI risk management, bias, and security training for all personnel involved in the AI lifecycle.


#### ✅ GOVERN-2.3 - COMPLIANT

**Explanation:** The CTO is explicitly designated as the executive leader responsible for overseeing AI initiatives.

**Recommendation:** None.


#### ❌ GOVERN-3.1 - GAP

**Explanation:** There is no requirement for interdisciplinary or diverse team representation in risk assessment and decision-making.

**Recommendation:** Incorporate language requiring that the AI Governance Committee consist of a diverse and interdisciplinary group of stakeholders, including technical, legal, and operational experts.


#### ❌ GOVERN-3.2 - GAP

**Explanation:** The policy fails to define or assign roles for human-AI interaction or oversight mechanisms.

**Recommendation:** Establish explicit guidelines on when human-in-the-loop (HITL), human-on-the-loop (HOTL), or human-in-command (HIC) architectures must be implemented.


#### 🟡 GOVERN-4.1 - PARTIAL

**Explanation:** The policy highlights safety and security principles, but does not provide details on programs or corporate culture initiatives promoting critical thinking and safety-first design.

**Recommendation:** Include commitment statements or reward mechanisms encouraging teams to question, challenge, and report potential AI safety and ethical concerns without fear of retaliation.


#### ❌ GOVERN-4.2 - GAP

**Explanation:** There is no mandate for teams to document the expected risks and impacts of the AI technologies they deploy.

**Recommendation:** Implement a mandatory requirement for AI Impact Assessments (AIIAs) to document risks, limitations, and societal impacts during system planning.


#### 🟡 GOVERN-4.3 - PARTIAL

**Explanation:** The policy mandates validation and incident reporting to the security team, but lacks explicit details on systematic testing frameworks or external information sharing.

**Recommendation:** Elaborate on the validation criteria and establish processes for sharing anonymized incident data externally or internally for shared learning.


#### ❌ GOVERN-5.1 - GAP

**Explanation:** No feedback mechanisms are defined to capture potential individual and societal impacts from external stakeholders.

**Recommendation:** Establish a public-facing portal or feedback loop to collect and prioritize complaints or performance feedback from external actors and impacted individuals.


#### ❌ GOVERN-5.2 - GAP

**Explanation:** The policy contains no provisions for incorporating external feedback into the design and update phases of AI systems.

**Recommendation:** Incorporate a requirement for the AI Governance Committee to review external feedback quarterly and mandate design adjustments for systems with documented issues.


#### 🟡 GOVERN-6.1 - PARTIAL

**Explanation:** Section 7 requires third-party AI reviews before integration, but does not outline specific risks like IP infringement or data privacy violations.

**Recommendation:** Update Section 7 to specify that reviews of third-party systems must explicitly evaluate intellectual property rights, licensing compliance, and training data provenance.


#### ❌ GOVERN-6.2 - GAP

**Explanation:** Contingency planning for failures or sudden outages of high-risk third-party AI services is completely omitted.

**Recommendation:** Require fallback mechanisms or service-level agreements (SLAs) for any critical third-party AI integrations to ensure operational continuity.


#### ❌ MAP-1.1 - GAP

**Explanation:** The policy does not require mapping or documenting intended purposes, beneficial uses, deployment settings, or legal contexts of AI systems.

**Recommendation:** Mandate that every proposed AI project compile a Context of Use document detailing its deployment setting, user expectations, and beneficial goals.


#### ❌ MAP-1.2 - GAP

**Explanation:** There are no provisions to ensure interdisciplinary expertise and diversity when analyzing the operational context of AI systems.

**Recommendation:** Require that initial project assessments must involve non-technical teams such as UX researchers, legal advisors, and subject-matter experts.


#### ❌ MAP-1.3 - GAP

**Explanation:** The policy fails to link AI initiatives to the organization's overarching mission, goals, or strategy.

**Recommendation:** Require that the business case for any new AI system must document alignment with ACME Corp's corporate strategy and core values.


#### ❌ MAP-1.4 - GAP

**Explanation:** No instructions exist for defining or re-evaluating the business value of AI systems.

**Recommendation:** Implement periodic reviews to verify that deployed AI systems still deliver their intended business value relative to alternative solutions.


#### ❌ MAP-1.5 - GAP

**Explanation:** Mapping and documenting specific risk tolerances for distinct AI application domains are not mandated.

**Recommendation:** Require risk threshold maps that define acceptable levels of false positives/negatives for different system classifications.


#### ❌ MAP-1.6 - GAP

**Explanation:** There is no mention of requirements elicitation or assessing socio-technical implications during system design.

**Recommendation:** Incorporate socio-technical analysis into the product design phase to evaluate how system outputs affect human workflow and user behavior.


#### ❌ MAP-2.1 - GAP

**Explanation:** Defining tasks, functionalities, and exact implementation methods of AI systems is not required.

**Recommendation:** Mandate detailed technical specifications mapping each system component to specific tasks and modeling methodologies.


#### ❌ MAP-2.2 - GAP

**Explanation:** There is no requirement to document the boundaries, limitations, and knowledge thresholds of the models.

**Recommendation:** Require developers to maintain 'Model Cards' documenting limitations, training data boundaries, and acceptable use guidelines.


#### 🟡 MAP-2.3 - PARTIAL

**Explanation:** Section 5 requires validation and representative testing data, which touches upon TEVV, but does not explicitly reference scientific integrity or structured TEVV methodologies.

**Recommendation:** Formally mandate the adoption of Test, Evaluation, Verification, and Validation (TEVV) procedures, highlighting scientific rigor and reproducibility.


#### ❌ MAP-3.1 - GAP

**Explanation:** There is no requirement to document the potential benefits of intended AI systems during the mapping phase.

**Recommendation:** Incorporate a 'Benefits Analysis' segment into the pre-development approval checklist.


#### ❌ MAP-3.2 - GAP

**Explanation:** The policy fails to require estimation of potential financial or non-monetary costs (e.g., reputational or safety impacts) resulting from AI failures.

**Recommendation:** Require project proposals to complete a failure-mode cost estimation, analyzing potential liability, reputation damage, and user harm.


#### ❌ MAP-3.3 - GAP

**Explanation:** System categorization and defining targeted application scopes are not documented.

**Recommendation:** Define a categorization taxonomy to clearly mark where a given system is safe to deploy and where its use is prohibited.


#### ❌ MAP-3.4 - GAP

**Explanation:** Defining and documenting operator proficiency requirements is completely unaddressed.

**Recommendation:** Add a standard requiring the development of clear operator training materials and minimum competency assessments prior to deployment.


#### ❌ MAP-3.5 - GAP

**Explanation:** Human oversight parameters are not defined or documented for mapping phases.

**Recommendation:** Ensure that the AI design documentation specifies the operational workflows and tools required for humans to monitor and override AI decisions.


#### 🟡 MAP-4.1 - PARTIAL

**Explanation:** Third-party reviews are required, but there is no specific framework for mapping the legal and technological risks of discrete third-party components (e.g., open-source libraries or foundational APIs).

**Recommendation:** Establish a Software Bill of Materials (SBOM) requirement for all AI models to track and analyze component-level legal risks.


#### ❌ MAP-4.2 - GAP

**Explanation:** The policy does not require identifying or documenting internal risk controls for AI system components.

**Recommendation:** Add requirements to document input validation, guardrail models, and output filtering controls at the system level.


#### ❌ MAP-5.1 - GAP

**Explanation:** Mapping the likelihood and magnitude of impact from AI systems is not required.

**Recommendation:** Require the use of a risk matrix evaluating both the likelihood of failure and severity of consequence during initial system design.


#### ❌ MAP-5.2 - GAP

**Explanation:** Practices and designated personnel for engaging with AI actors and integrating feedback are missing from the mapping phase.

**Recommendation:** Assign specific ownership within product teams to collect and register feedback from deployment partners and end-users.

