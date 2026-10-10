---
title: "Module 17 Quiz — Privacy, Data Protection, Risk Management, and Compliance"
layout: default
---

# Module 17 Quiz — Privacy, Data Protection, Risk Management, and Compliance

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 scenario) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Scenario answers: classify the data/flow first, then apply the principle — a control without a classification is not an answer.

**Coverage.** Maps to Module 17 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m17--privacy-data-protection-risk-management-and-compliance)): privacy vs. security vs. confidentiality, data-flow mapping and DPIA, cross-framework control mapping, privacy-by-design evaluation.

**Related:** [Module 17 lesson](../../modules/module-17-privacy-data-protection-and-compliance/README.md) · [LAB-02 threat model & risk register](../../labs/lab-02-threat-model-risk-register/README.md) · [LAB-17 cloud config review](../../labs/lab-17-cloud-config-review/README.md) · [CS-4 case study](../case-studies/cs-4-cloud-privacy-automation.md)

> **Safety reminder:** privacy exercises use synthetic or public post-mortem data only — no real personal data in submissions. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** *Privacy* differs from *security* and *confidentiality* in that:

- (a) They are synonyms used for different audiences
- (b) Privacy governs **how and why** personal data is collected, used, shared, and retained (lawful basis, purpose limitation, rights) — while security/confidentiality are the *controls* that protect it
- (c) Privacy only applies to healthcare data
- (d) Security is a superset of privacy

**Q2.** **Derived data** (e.g., "inferred credit risk" or "predicted churn score") is significant because:

- (a) It isn't personal data
- (b) It is generated *from* personal data, can drive decisions about the person, and inherits (and can amplify) the original data's obligations
- (c) It never needs review
- (d) Only original data is regulated

**Q3.** A **DPIA** (Data Protection Impact Assessment) should be done:

- (a) After launch, once complaints arrive
- (b) Before building/processing that introduces high risk — mapping flows, risks, and mitigations while design is still cheap to change
- (c) Only when a regulator demands it
- (d) Once per company, ever

**Q4.** *Purpose limitation* means:

- (a) Data may be kept forever
- (b) Personal data is collected for specified, explicit purposes and not used for incompatible later purposes without a new basis
- (c) Only limited data is ever useful
- (d) Storage is capped by disk size

**Q5.** Mapping controls across **CSF 2.0 Functions ↔ CIS v8.1** is useful because:

- (a) One is a law, the other a fine
- (b) CSF's functions (Govern/Identify/Protect/Detect/Respond/Recover) give an outcome-oriented frame, while CIS v8.1 gives *actionable, prioritized* safeguards — combining them turns strategy into tasks and reveals gaps either alone would miss
- (c) It replaces both with a third framework
- (d) Cross-mapping is only for auditors

**Q6.** Under *data minimization*, a fitness app should collect:

- (a) Everything, "just in case"
- (b) Only what the stated purpose needs — heart rate for heart-rate features, not contacts and precise location by default
- (c) Whatever the SDK defaults to
- (d) Identical data from all users for consistency

**Q7.** A **retention schedule** primarily operationalizes:

- (a) Aesthetic data hygiene
- (b) Deleting/anonymizing data when its purpose and legal retention ends — bounding breach impact (less data = less harm) and privacy exposure
- (c) Faster backups
- (d) Compliance checkbox collection

**Q8.** Which is a **privacy-by-design** choice?

- (a) Add privacy features if regulators ask
- (b) Default-new-users to private visibility, collect account-level (not precise) location, and make consent granular and revocable — privacy as a default, not an add-on
- (c) Hide data practices in a 40-page policy
- (d) Pseudonymize only after an incident

## Part B — Scenario (4)

**Q9. (Outcome 1 — classification).** A student-health-app scenario contains: full name + student ID; email; **diagnosis notes** entered by a counselor; **appointment times**; app telemetry (feature usage); inferred "wellbeing risk score"; and support-chat transcripts. Classify each (personal / sensitive-special-category / derived / non-personal), and state the handling consequence for the sensitive group.

**Q10. (Outcome 2 — DPIA).** Build the DPIA outline for that app: list the data-flow map elements (sources → processing → recipients, including any cloud), three inherent risks with likelihood/impact, one mitigation each, and the residual-risk + sign-off fields a DPIA must end with.

**Q11. (Outcome 3 — control mapping).** Map **5 controls** for this app across (a) CSF 2.0 Function and (b) CIS v8.1 safeguard (or family). Use: encryption at rest of notes; MFA for counselors; log review of record access; annual access recertification; incident-response plan. Show the mapping as a small table and flag one gap the mapping reveals.

**Q12. (Outcome 4 — privacy critique).** A product update: (i) starts sharing precise location with a "personalization partner" under ToS clause 14.2 buried at registration; (ii) retains deleted-account data "for analytics" indefinitely. For each: name the principle violated (consent/purpose limitation/retention), whether the design *could* be repaired technically, and the design fix you'd require before shipping.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Privacy = governance of data *use* (lawful basis, purpose, rights, accountability); security/confidentiality = technical/administrative protections of the data. Privacy needs security to be meaningful; security without privacy can still process data unlawfully. Misconceptions: (a) collapsing them hides real obligations; (c) privacy covers all personal data; (d) security protects data, privacy governs its *processing* — neither subsumes the other cleanly.

**Q2 — (b).** Derived/inferred data is still personal data when it relates to an identifiable person, and it's often *more* consequential (decisions are made from it) while being less transparent to the subject. Misconceptions: (a) "derived ≠ personal" is a common and costly error; (c)/(d) wrong on both counts.

**Q3 — (b).** DPIA is a *design-time* instrument: high-risk processing → assess before processing starts (and it's a legal trigger in GDPR-style regimes for high-risk activities). Misconceptions: (a) remediation after launch costs far more and may have already caused harm; (c) DPIAs are for *your* risk reduction, not just enforcement; (d) per-project/per-change.

**Q4 — (b).** Specified purposes at collection; later uses need compatibility analysis or a new lawful basis. Misconceptions: (a) that's unlimited retention (different violation); (c) pun intended, wrong rule; (d) retention schedule covers *time*, not *purpose*.

**Q5 — (b).** Complementary frames: CSF = "what outcomes/what functions," CIS = "which concrete safeguard, in what implementation group." Mapping shows whether every CSF outcome has actionable CIS tasks and where neither covers a need. Misconceptions: (a) neither is a law itself; (c) you don't replace either; (d) practitioners use mapping to reduce audit churn, not only auditors.

**Q6 — (b).** Minimization = collect what's necessary for the stated purpose, no more. Misconceptions: (a) "just in case" is unlimited collection; (c) SDK defaults optimize for the vendor, not your obligations; (d) uniformity ≠ necessity.

**Q7 — (b).** Retention bounds both privacy exposure and breach impact — "you can't lose what you deleted." Misconceptions: (a) hygiene is a side effect; (c) backups are a different control; (d) the schedule exists *because* obligations end, not to collect checkboxes.

**Q8 — (b).** Privacy by design/default: sensible defaults, granular consent, data minimized — all *before* launch. Misconceptions: (a) reactive ≠ by design; (c) concealment is the opposite of the principle's transparency ethos; (d) late pseudonymization leaves a window of full exposure.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** **Name + student ID:** personal (identifiers — treat as confidential, linkable). **Email:** personal (contact identifier). **Diagnosis notes:** **sensitive/special-category** (health data — the highest-handling tier). **Appointment times:** personal, and *indirectly health-sensitive* (reveals counseling visits even without note content — contextual sensitivity matters). **Telemetry:** personal when linked to an account (behavioral data; minimized if aggregated/deleted on schedule). **Wellbeing risk score:** **derived personal data** — decisions may be made from it, so it needs the same rigor as source data plus human-reviewability. **Support transcripts:** personal, potentially sensitive depending on content (screen for health/financial mentions). **Handling consequence for the sensitive group:** elevated lawful-basis/explicit-consent requirements, strict purpose limitation, encryption + restricted access (need-to-know counselors only), audit on *every* access, minimized retention, DPIA mandatory — and never used for marketing or shared beyond the stated purpose. → [Module 17 lesson](../../modules/module-17-privacy-data-protection-and-compliance/README.md)

**Q10.** **Data-flow map:** sources (student user via mobile app; counselor UI; support staff chat) → collection (registration fields, note entry, telemetry SDK, chat) → processing (risk-score computation, appointment scheduling, analytics aggregation, backups) → storage (app DB in cloud provider region X, chat store, backups) → recipients (school administrators? — flag as *needs justification*; cloud provider as processor; support vendor if any) → retention/deletion path. **Three inherent risks (L×I):** (1) unauthorized staff access to diagnosis notes — L: medium, I: high → mitigation: role-based access + per-record audit + annual recertification → residual: low-medium (accepted with monitoring). (2) Breach of unencrypted backups containing notes — L: low, I: high → mitigation: encryption at rest + key separation + backup access restriction → residual: low. (3) Risk score misused to flag/exclude students without review — L: medium, I: high (discriminatory impact) → mitigation: human-in-the-loop decisioning, model input documentation, subject notification → residual: medium (accepted with governance + appeal path). **DPIA end fields:** residual-risk statement (each risk, post-mitigation rating, *accept/escalate* decision) + **sign-off**: technical owner, privacy/DPO sign-off, date, review date. → [LAB-02](../../labs/lab-02-threat-model-risk-register/README.md)

**Q11.** | Control | CSF 2.0 Function | CIS v8.1 (example safeguard) |
|---|---|---|
| Encrypt notes at rest | **Protect** (Data Security) | 3.5 Encrypt Sensitive Data at Rest |
| MFA for counselors | **Protect** (Identity Mgmt/Auth) | 6.3 Require MFA for Externally-Exposed Apps / 6.4 MFA for OS/apps |
| Log review of record access | **Detect** (Continuous Monitoring) | 8.2 Audit Log Review & Analysis |
| Annual access recertification | **Govern** (or Protect — RBAC policy) | 6.1 Establish/Maintain Inventory of Accounts (with review) |
| Incident-response plan | **Respond** (Incident Response Mgmt) | 17.1 Establish & Maintain IR Plan |

**Gap the mapping reveals:** every control lands in Protect/Detect/Respond/Govern — nothing addresses **Identify** (asset/data inventory: *where do notes live, which systems/processors touch them?*) or **Recover** (tested backup restoration). A mapping exercise makes those holes visible as *empty CSF functions with no CIS counterpart chosen* — exactly its purpose. (Accept any defensible CIS/CSF pairing; require the gap insight.) → [Module 17 lesson](../../modules/module-17-privacy-data-protection-and-compliance/README.md)

**Q12.** **(i) Precise location → partner via buried ToS clause.** Violations: **informed consent** (a registration-time clause buried at 14.2 is not freely given, specific, informed, unbundled consent) and **purpose limitation** (personalization by a third party is an incompatible/incompatiblely-communicated secondary use) — likely also unlawful third-party *sharing*. **Repairable technically?** Yes structurally: consent can be unbundled, revocable, and off-by-default. **Design fix before shipping:** make partner sharing a **separate, granular, opt-in toggle** (default off), state purpose + partner identity in plain language at the toggle, provide one-click withdrawal with effect-forward propagation, log consent events — and give users account-level location as the default precision. Ship only with that redesign, not with reworded ToS. **(ii) Indefinite post-deletion retention "for analytics."** Violation: **storage limitation / retention** — deletion must mean deletion (or irreversible anonymization) once purpose + legal hold end; "analytics" is an open-ended purpose, incompatible with indefinite retention. **Repairable?** Yes. **Design fix:** define retention per data class (e.g., account deleted → PII purged within 30 days; *aggregated, non-identifying* stats retained; backups age out on schedule), implement automated deletion pipelines with verification evidence, and document the schedule in the DPIA. If analytics *needs* the record, lawful anonymization — which must actually prevent re-identification — is the only defensible path. → [Module 17 lesson](../../modules/module-17-privacy-data-protection-and-compliance/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

1. **DPIA worksheet (practical).** Complete the full DPIA for the student-health-app scenario: data inventory, flow map, risks with L×I, mitigations, residual risk, sign-off — M17 deliverable.
2. **Control mapping spreadsheet.** Map 15 controls across CSF 2.0 functions and CIS v8.1 for the same scenario; flag gaps (functions with no control, controls with no owner).
3. **Privacy critique (practical investigation).** Analyze 3 real, public product privacy incidents/post-mortems: name the principle violated, the design fix, and what a DPIA would have caught *before* launch.
4. **Risk prioritization.** Your startup can fund one privacy program item this quarter: consent management platform, data inventory tooling, retention automation, or access recertification process. Pick with risk reasoning — and say which CSF/CIS gap your pick closes.

*Review guidance:* classification-first discipline is graded — jumping to "encrypt it" without classifying the data skips the step that determines *whether* encryption, retention, consent, or access change is the right answer.

**Next:** [M18 quiz](./quiz-m18.md) · **Previous:** [M16 quiz](./quiz-m16.md) · **Hub:** [Assessment Hub](../README.md)
