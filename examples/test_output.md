# NIST AI RMF + ISO 42001 Audit Report

**Generated:** 2026-09-02 19:16:27



## Executive Summary

| Metric | Count |
| :--- | :--- |
| Total Requirements | 37 |
| Compliant | 2 |
| Partial | 17 |
| Gaps | 18 |

**Compliance Rate:** 5.4%

---

## Detailed Findings

### NIST AI RMF


#### ✅ GOVERN-1.1 - COMPLIANT

**Explanation:** Section 1 explicitly mandates legal compliance and requires the Legal Department to maintain a register of AI-specific legal obligations with mandatory breach reporting within 48 hours.

**Recommendation:** Maintain current policy provisions and establish routine auditing of the legal register to ensure ongoing currency.


#### 🟡 GOVERN-1.2 - PARTIAL

**Explanation:** The policy references responsible AI and tracks basic metrics (accuracy, drift, complaints in Section 3), but does not systematically define or integrate core trustworthy AI characteristics (e.g., fairness, explainability, safety, privacy) across operational processes.

**Recommendation:** Explicitly define characteristics of trustworthy AI within policy documentation and integrate them into pre-deployment verification checklists.


#### ❌ GOVERN-1.3 - GAP

**Explanation:** Section 6 explicitly notes that risk appetite is not formally documented or quantified and decisions are made on an ad-hoc basis, preventing structured risk management based on risk tolerance.

**Recommendation:** Formally document and quantify organizational risk tolerances and implement defined procedures to scale risk management activities according to risk levels.


#### ❌ GOVERN-1.4 - GAP

**Explanation:** Section 2 explicitly states resource allocation is not tied to risk levels and Section 6 relies on ad-hoc decisions, failing to establish transparent, priority-driven risk management processes.

**Recommendation:** Develop transparent risk management procedures that prioritize oversight and control implementation based on system risk tiers.


#### ✅ GOVERN-1.5 - COMPLIANT

**Explanation:** Section 3 defines regular semi-annual reviews of high-risk AI systems by the AI Governance Board, assessing key metrics and distributing documented findings.

**Recommendation:** Expand the review schedule to encompass lower-risk systems on an annual basis to ensure total portfolio coverage.


#### 🟡 GOVERN-1.6 - PARTIAL

**Explanation:** Section 2 establishes a quarterly master spreadsheet inventory, but explicitly admits prioritizing inventory maintenance on a best-effort basis without risk-based resource allocation.

**Recommendation:** Allocate explicit resourcing and establish automated inventory tooling prioritized by system risk categorization.


#### ❌ GOVERN-1.7 - GAP

**Explanation:** The policy contains no provisions or procedures regarding the safe decommissioning or retirement of AI systems.

**Recommendation:** Establish standard operating procedures for AI system decommissioning, addressing data archiving, model retirement, and stakeholder notification.


#### 🟡 GOVERN-2.1 - PARTIAL

**Explanation:** Roles are assigned to Legal, CTO, Governance Board, and Operators, but lines of communication and duties for mapping and measuring AI risks specifically are fragmented and informal.

**Recommendation:** Publish a comprehensive RACI matrix defining explicit duties for mapping, measuring, and managing AI risks across product lifecycles.


#### ❌ GOVERN-2.2 - GAP

**Explanation:** Section 5 explicitly waives formal training and competency assessment requirements for operators before they review AI outputs.

**Recommendation:** Mandate formal AI risk, bias, and operation training with competency evaluations for all human operators and development personnel.


#### 🟡 GOVERN-2.3 - PARTIAL

**Explanation:** Business leaders make risk decisions (Section 6), but ad-hoc decision-making lacks formal executive governance protocols and documented accountability.

**Recommendation:** Implement formal executive risk acceptance workflows for high-risk AI deployments.


#### ❌ GOVERN-3.1 - GAP

**Explanation:** The policy makes no provision for interdisciplinary teams or diverse domain/demographic expertise in AI risk management decision-making.

**Recommendation:** Mandate interdisciplinary representation (e.g., technical, legal, domain expertise, ethics) on the AI Governance Board.


#### 🟡 GOVERN-3.2 - PARTIAL

**Explanation:** Section 5 establishes human operator approval for customer-facing outputs, but lacks defined roles, operational boundaries, or configurations for different human-AI oversight tiers.

**Recommendation:** Document specific guidelines for Human-in-the-Loop, Human-on-the-Loop, and Human-over-the-Loop operational models.


#### ❌ GOVERN-4.1 - GAP

**Explanation:** The policy does not establish or encourage organizational practices fostering a safety-first mindset or critical thinking in AI design and development.

**Recommendation:** Embed safety-by-design guidelines and critical risk review checkpoints into early development methodologies.


#### ❌ GOVERN-4.2 - GAP

**Explanation:** There is no requirement in the policy for teams to conduct or document AI impact assessments or risk logs during development.

**Recommendation:** Require mandatory AI Impact Assessments (AIIAs) and documented risk registers prior to system deployment.


#### 🟡 GOVERN-4.3 - PARTIAL

**Explanation:** Section 3 tracks metrics (drift, accuracy) semi-annually and Section 1 mandates 48-hour compliance reporting, but standardized testing procedures and incident response plans are absent.

**Recommendation:** Formulate structured pre-deployment Testing, Evaluation, Verification, and Validation (TEVV) protocols and an AI Incident Response Plan.


#### 🟡 GOVERN-5.1 - PARTIAL

**Explanation:** Section 3 includes tracking user complaints, but lacks broader processes to collect, prioritize, and integrate external stakeholder feedback regarding societal impacts.

**Recommendation:** Establish external feedback submission channels and formal mechanisms to review broader societal and end-user impacts.


#### 🟡 GOVERN-5.2 - PARTIAL

**Explanation:** Section 3 states review findings are distributed to stakeholders, but no closed-loop mechanism is specified to regularly incorporate feedback back into system design.

**Recommendation:** Institute a formal feedback adjudication workflow that feeds review outcomes back into product development backlogs.


#### 🟡 GOVERN-6.1 - PARTIAL

**Explanation:** Section 4 requires third-party vendors to provide SOC 2 Type II reports, but omits coverage of intellectual property infringement or broader AI supply chain risks.

**Recommendation:** Update vendor management policies to evaluate third-party AI systems for IP licensing, data usage rights, and algorithmic transparency.


#### ❌ GOVERN-6.2 - GAP

**Explanation:** Section 4 explicitly states that no formal contingency processes exist if a critical third-party AI service experiences an outage, fails, or unexpectedly changes model behavior.

**Recommendation:** Develop explicit contingency, fallback, and business continuity plans for all critical third-party AI dependencies.


#### ❌ MAP-1.1 - GAP

**Explanation:** The policy does not require teams to document system-level intended purposes, deployment contexts, normative expectations, or legal context prior to development.

**Recommendation:** Implement a mandatory system intake form requiring documentation of intended purpose, target deployment context, and beneficial uses.


#### ❌ MAP-1.2 - GAP

**Explanation:** The policy does not address interdisciplinary team requirements or domain diversity during context establishment.

**Recommendation:** Require cross-functional intake reviews involving technical, operational, legal, and subject-matter experts.


#### 🟡 MAP-1.3 - PARTIAL

**Explanation:** Section 6 asserts commitment to responsible AI, but organizational strategic goals and missions regarding AI adoption are not formally documented.

**Recommendation:** Formally document Acme Corp's AI mission statement and strategic objectives within policy documentation.


#### ❌ MAP-1.4 - GAP

**Explanation:** The policy does not require defining or periodically re-evaluating the business context or strategic business value of AI deployments.

**Recommendation:** Mandate business value definitions and periodic business-use reviews during semi-annual monitoring.


#### ❌ MAP-1.5 - GAP

**Explanation:** Section 6 explicitly confirms organizational risk tolerance is neither formally documented nor quantified.

**Recommendation:** Define, quantify, and document organizational risk appetite and acceptable tolerance thresholds.


#### ❌ MAP-1.6 - GAP

**Explanation:** The policy lacks provisions to elicit system requirements from multi-disciplinary actors or evaluate socio-technical design implications.

**Recommendation:** Integrate socio-technical design evaluation into initial system requirements gathering.


#### ❌ MAP-2.1 - GAP

**Explanation:** The master spreadsheet inventory captures ownership and deployment dates, but not detailed definitions of system tasks or implementation methods.

**Recommendation:** Expand inventory fields to capture explicit model tasks, algorithms used, and operational methods.


#### 🟡 MAP-2.2 - PARTIAL

**Explanation:** Section 5 touches on human review of customer-facing outputs, but documentation of model knowledge limits, edge cases, and failure modes is not required.

**Recommendation:** Mandate documentation of model knowledge limits and operational boundaries using standardized Model Cards.


#### 🟡 MAP-2.3 - PARTIAL

**Explanation:** Section 3 mentions reviewing model drift and accuracy, but formal scientific integrity standards and TEVV frameworks are not defined.

**Recommendation:** Develop comprehensive TEVV frameworks incorporating baseline scientific testing standards across the model lifecycle.


#### ❌ MAP-3.1 - GAP

**Explanation:** The policy does not mandate the identification or documentation of expected benefits for AI systems.

**Recommendation:** Require project proposals to explicitly document anticipated business and user benefits.


#### ❌ MAP-3.2 - GAP

**Explanation:** The policy fails to require estimation or documentation of non-monetary costs or negative social/operational impacts from potential system errors.

**Recommendation:** Mandate cost-benefit and impact analyses covering non-monetary, ethical, and operational risk costs.


#### 🟡 MAP-3.3 - PARTIAL

**Explanation:** System categorization exists implicitly via high-risk designations in Section 3, but systematic documentation of targeted application scopes based on capabilities is absent.

**Recommendation:** Establish formal risk categorization rules and require defined application boundaries for every AI deployment.


#### ❌ MAP-3.4 - GAP

**Explanation:** Section 5 explicitly waives required operator training and competency evaluations, preventing assessment of operator proficiency.

**Recommendation:** Establish mandatory operator proficiency testing and document operator qualifications prior to deployment.


#### 🟡 MAP-3.5 - PARTIAL

**Explanation:** Section 5 mandates human oversight for customer-facing outputs, but lacks defined, assessed, and documented workflows for oversight execution or override tracking.

**Recommendation:** Formulate standard oversight procedures and log operator override actions for periodic governance review.


#### 🟡 MAP-4.1 - PARTIAL

**Explanation:** Section 1 mandates legal compliance tracking, but detailed mapping of component-level technical and legal risks (e.g., training data copyright, open-source model licenses) is not covered.

**Recommendation:** Establish component-level risk mapping for external datasets, base models, and software libraries.


#### 🟡 MAP-4.2 - PARTIAL

**Explanation:** Section 4 specifies vendor SOC 2 Type II controls, but omits risk control identification for internal AI components or broader system architecture.

**Recommendation:** Build a comprehensive technical control baseline applicable to both internal and third-party AI components.


#### ❌ MAP-5.1 - GAP

**Explanation:** The policy lacks a structured methodology to evaluate and document the likelihood and magnitude of potential AI risks and impacts.

**Recommendation:** Adopt a formal risk assessment matrix defining probability and impact scales for AI risk evaluation.


#### 🟡 MAP-5.2 - PARTIAL

**Explanation:** Section 3 includes distributing governance findings to stakeholders, but lacks defined routines and personnel dedicated to regular actor engagement and feedback integration.

**Recommendation:** Designate responsible roles and routines for gathering and integrating stakeholder feedback continuously.

