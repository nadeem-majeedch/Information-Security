---
title: "Module 03 Quiz — Governance, Policy, Ethics, and Law"
layout: default
---

# Module 03 Quiz — Governance, Policy, Ethics, and Law

**Type:** Formative knowledge check (completion gate) · **Questions:** 10 (6 multiple choice + 4 short answer) **+ 1 scenario essay (~300 words)** · **Pass mark:** ≥ 80% · **Unlimited retakes**

**Instructions.** Complete Parts A and B before revealing answers. The essay (Part C) is self-assessed against the published rubric. Short answers: 2–4 sentences. Ethics answers must reference a principle (authorization, scope, privacy, responsible disclosure), not just a feeling.

**Coverage.** Maps to Module 03 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m03--security-governance-policy-ethics-and-law)).

**Related:** [Module 03 lesson](../../modules/module-03-governance-policy-ethics-and-law/README.md) · [LAB-14](../../labs/lab-14-ir-tabletop/README.md) · [CS-1 case study](../case-studies/cs-1-breach-at-meridian.md)

---

## Part A — Multiple choice (6)

**Q1.** In the policy hierarchy, which document is the *highest* level and sets overall intent and management direction?

- (a) Procedure
- (b) Standard
- (c) Policy
- (d) Guideline

**Q2.** A **procedure** is best described as:

- (a) A high-level statement of management intent
- (b) A mandatory, measurable requirement (e.g., "all laptops use full-disk encryption")
- (c) A step-by-step set of instructions for performing a task
- (d) Optional advice that may be followed

**Q3.** The single most important legal/ethical boundary in security work is:

- (a) Using free tools
- (b) Having explicit authorization within a defined scope
- (c) Working only at night
- (d) Never writing code

**Q4.** **Responsible vulnerability disclosure** means:

- (a) Reporting a discovered flaw to the vendor privately first, with a reasonable fix window, before public detail
- (b) Publishing exploit code immediately so it gets fixed fast
- (c) Keeping the flaw secret forever
- (d) Selling the flaw to the highest bidder

**Q5.** Which is a core principle common to major ethics codes (e.g., (ISC)², ACM/IEEE)?

- (a) Protect society/act in the public interest and avoid harm
- (b) Always prioritize the employer's profit over users
- (c) Security professionals may test any system to improve it
- (d) Disclosure rules are optional

**Q6.** Under a GDPR-style regime, the role accountable for deciding *why* personal data is processed is the:

- (a) Data subject
- (b) Data controller
- (c) Data processor
- (d) Data protection software vendor

## Part B — Short answer (4)

**Q7.** Distinguish **governance** from **compliance** in one or two sentences each.

**Q8.** Explain why "authorization" is a *continuous* requirement, not a one-time checkbox — give an example of work that was authorized at the start but became unauthorized mid-task.

**Q9.** Name the four offence-category themes you would expect in a cybercrime statute like PECA 2016 (e.g., unauthorized access, data interference), and note the authorization that makes an equivalent action legal in a lab.

**Q10.** Contrast how two jurisdictions treat personal-data breach notification (e.g., GDPR vs. one other) at a conceptual level — who must notify, and within what kind of timeframe.

## Part C — Scenario essay (~300 words)

**Q11.** A friend asks you to "take a quick look" at their small online store to see if it is secure. You find a login page and an admin panel. Write your decision and justification covering: what authorization you need *in writing*, what scope you would define (which URLs/tests, which are off-limits), how you would handle any personal data you encounter, and how you would report a found vulnerability responsibly. Explicitly reference at least two principles from the lesson.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (c) Policy.** Policy sits at the top, setting intent; standards, procedures, and guidelines implement or advise beneath it. *Misconception:* (d) *guideline* is optional advice — the stem's “statement of management intent” is policy's job; (b) *standard* is the mandatory, measurable layer *below* policy.

**Q2 — (c).** A procedure is *how-to*, step by step. (a) is policy, (b) is a standard, (d) describes a guideline (optional). *Misconception:* “all laptops use full-disk encryption” feels like intent, but it is **mandatory and measurable** — that makes it a *standard*, not a policy.

**Q3 — (b).** Explicit authorization within a defined scope is the only lawful basis for testing. *Misconception:* (a) free tools and (c) working at night are irrelevant to legality; (d) “never writing code” is a skill statement, not an authorization — “publicly reachable” is likewise not permission.

**Q4 — (a).** Report privately to the vendor first with a reasonable remediation window, then publish detail. *Misconception:* (b) immediate full disclosure removes the vendor's chance to patch and endangers other users still running the flaw; (c) secrecy-forever leaves users unprotected — responsible disclosure balances both.

**Q5 — (a).** Protect society / act in the public interest and avoid harm. *Misconception:* (c) is the classic trap: “good intentions” never create authorization (only written permission for a scoped target does); (d) disclosure rules are binding professional obligations, not preferences.

**Q6 — (b) Data controller.** The controller determines purposes/means of processing and carries the accountability; the processor acts on the controller's behalf. *Misconception:* (a) *data subject* is the person the data is **about**, not the decider; (d) a vendor processing on instructions is a *processor*, not the controller.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q7.** *Governance* = the framework of direction, accountability, and oversight (who decides, what are the rules, how is it managed). *Compliance* = conforming to a specific external law, regulation, or internal policy. Governance sets and owns the rules; compliance is meeting them.

**Q8.** Scope can change mid-engagement as you discover new systems or as the owner withdraws parts of it. Example: you are authorized to test `store.example/test`, but during testing the owner adds a payment service — testing the payment service is now *unauthorized* until the scope is re-agreed in writing. Re-confirm scope whenever targets expand. → [Lesson: authorization](../../modules/module-03-governance-policy-ethics-and-law/README.md)

**Q9.** Themes: (1) unauthorized access / illegal access, (2) data interference (damage, deletion, modification), (3) identity/cyber-fraud and related offences, (4) offences against critical systems / data privacy. In a lab, the authorization that makes equivalent actions legal is **written permission to test a system you own**, confined to that scope — the act is identical, the authorization is what differs.

**Q10.** GDPR-style: the controller must notify the supervisory authority within **72 hours** of becoming aware of a qualifying breach, and notify affected individuals when risk is high. Contrast with a regime that requires notification to a sector regulator or law enforcement within a different statutory window, or that sets no single hard deadline. The conceptual contrast is *fixed clock + regulator* vs *varies by sector/jurisdiction* — check the current law before relying on a specific number. → [Lesson: PECA vs GDPR](../../modules/module-03-governance-policy-ethics-and-law/README.md)

</details>

<details>
<summary><b>Part C essay rubric (20 points)</b> — self-assess honestly</summary>

| Criterion | Max |
|---|---|
| Technical accuracy (correct authorization/scope/disclosure reasoning) | 8 |
| Justification quality (reasoned, principles named and applied) | 6 |
| Safety/ethics reasoning (scope, privacy of data, responsible disclosure explicitly covered) | 4 |
| Clarity and structure | 2 |
| **Pass = ≥ 12/20** | |

**Q11 — model answer (essay).** A strong answer asks for **written** authorization naming the specific URLs/tests, excludes the payment flow (or handles it with fake data only), states that any real customer data encountered will be protected and not copied, and describes private vendor reporting with a fix window. Referencing authorization + responsible disclosure + privacy/least-harm satisfies the "two principles" bar. An answer that just "scans the site because a friend asked" fails the safety criterion regardless of technical detail.

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Policy drafting.** Write a 1–2 page household/roommate security policy covering devices, Wi-Fi, guests, and backups, in correct policy form (a purpose statement, roles, and review date).
2. **Ethical vignettes.** Analyse five gray-area cases (testing a friend's site without written permission; "just looking" at a shared router; re-using a colleague's session; a bug bounty out of scope; scanning a café Wi-Fi). For each, state authorized/unauthorized and the governing principle.
3. **Law mapping.** Map six everyday activities to a cybercrime-law offence category and note the authorization that makes each safe.
4. **Hierarchy check.** Given a messy set of statements, sort them into policy / standard / procedure / guideline and justify each placement.

**Next:** [Module 04 quiz](./quiz-m04.md) · [Previous: M02](./quiz-m02.md) · [Assessment Hub](../README.md)
