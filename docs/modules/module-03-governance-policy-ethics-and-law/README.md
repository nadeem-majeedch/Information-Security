---
title: "Module 03 — Security Governance, Policy, Ethics, and Law"
layout: default
---

# Module 03 — Security Governance, Policy, Ethics, and Law

> **Level 1 · Foundations · Beginner · Estimated study time: 8–10 hours**
> **Prerequisites:** [Module 01](../module-01-information-security-foundations/README.md).

## Why This Module Matters

The techniques you will learn later in this course — scanning, exploitation, interception, credential testing — are identical whether they defend a hospital or rob it. The difference is never the tool; it is **authorization, scope, and intent**. This module builds the frame that keeps your skills lawful and ethical: how organizations decide security rules (governance), how those rules are written so people can follow them (policy), what professional ethics demand of you, and what the law actually says — including Pakistan's Prevention of Electronic Crimes Act, which applies directly to learners in this course's home context. Do this module before your first scanning lab: every subsequent practical in the course references its rules.

## Prerequisites and Estimated Study Time

- **Prerequisites:** [Module 01](../module-01-information-security-foundations/README.md).
- **Estimated study time:** 8–10 hours — ~3 h reading, ~3 h drafting policy and case analyses, ~2 h knowledge check and essay.
- **Tools:** text editor; free official law texts online (links in Further Reading).

## Learning Outcomes

By the end of this module, you can:

1. Distinguish governance, regulation, policy, standard, procedure, and guideline in a hierarchy diagram. *(Understand)*
2. Draft a short personal/household security policy set (acceptable use, password rule, device rule, incident contacts) in correct policy form. *(Apply)*
3. Explain the ethical boundaries of security work: authorization, scope, privacy, and responsible disclosure. *(Understand)*
4. Summarize the purpose and key offense categories of Pakistan's Prevention of Electronic Crimes Act (PECA) 2016 as amended, and contrast it with one other jurisdiction's law (e.g., EU GDPR). *(Understand)*

---

## Core Concepts

### 1. Governance, regulation, compliance — the decision layer

**Plain language.** *Governance* is who gets to decide the rules and how those decisions are checked. *Regulation* is rules imposed from outside (by government). *Compliance* is meeting those external or contractual rules. Governance is broader: it also covers your own goals, risk appetite, and accountability.

**Technical detail.** Ask three governance questions about any organization (or your own digital life): **Who decides?** (board, management, you), **What do they decide?** (risk appetite — how much risk is acceptable in pursuit of goals), and **How is it checked?** (reviews, audits, metrics). NIST CSF 2.0's *Govern* function formalizes exactly these questions — the first pillar of the framework you met in Module 01.

Common confusion: **compliance is not security.** An organization can be compliant and still breached (it met the checklist; the checklist didn't cover the attack). Governance sets direction and verifies outcomes; compliance proves specific rules were followed.

### 2. The policy hierarchy

**Plain language.** Rules live at different altitudes. At the top, short statements of intent; at the bottom, click-by-click instructions.

**Technical detail.**

```text
        ┌────────────────────────────┐
        │  LAWS / REGULATIONS         │  imposed (PECA, GDPR) — non-optional
        ├────────────────────────────┤
        │  POLICY                     │  WHAT and WHY — mandatory, senior-owned
        │  "All data must be encrypted in transit."      │
        ├────────────────────────────┤
        │  STANDARD                   │  WHICH specific requirement — measurable
        │  "TLS 1.2 minimum; HTTPS everywhere."           │
        ├────────────────────────────┤
        │  PROCEDURE                  │  HOW — step-by-step, repeatable
        │  "Enable HTTPS: 1. … 2. … 3. verify with …"     │
        ├────────────────────────────┤
        │  GUIDELINE                  │  RECOMMENDED, not mandatory
        │  "Prefer a password manager on all devices."    │
        └────────────────────────────┘
```

| Layer | Answers | Mandatory? | Example |
|---|---|---|---|
| **Policy** | What must be true | Yes | "Customer data is encrypted wherever stored" |
| **Standard** | Which specific requirement satisfies it | Yes | "AES-256 at rest; TLS 1.2+ in transit" |
| **Procedure** | Exact steps to achieve it | Yes, if you perform the task | Server hardening checklist (Module 05) |
| **Guideline** | Recommended practice | No (default-off) | "Consider a hardware security key" |

**A valid policy states:** purpose (why), scope (what/whom it covers), ownership (who maintains it), requirements (the rules), enforcement (consequences), and review date (when it's revisited). A policy without a review date is a historical document.

### 3. Roles and responsibilities

Security fails in the gap between "someone should do it" and a named person. Governance fixes names: *asset owner* (decides protection level — M01), *data custodian* (implements — IT), *user* (follows rules), *controller/processor* (GDPR roles, §5 below). In your household policy, write these roles explicitly — it is the difference between a document and a fridge-magnet promise.

### 4. Ethics: the boundaries of legitimate security work

**Plain language.** Ethics asks "even if I *could*, *should* I?" Law draws the outer boundary; professional ethics draws a stricter inner one.

**Technical detail.** Four ethical anchors govern everything this course teaches:

1. **Authorization.** Permission must be *explicit, written, specific, and current* for the systems, methods, and dates involved. "They didn't tell me to stop" is not authorization. Course labs authorize only your own/isolated lab systems — see the [Lab Safety Policy](../../lab-safety-policy.md).
2. **Scope.** Test what was agreed, no more. Scope creep — "while I was there I also checked their router" — is how authorized tests become offenses.
3. **Privacy / data minimization.** During any authorized work, touch only the data needed to prove the finding. Copying "extra" data is both an ethical and often a legal breach (and unnecessary to prove a vulnerability).
4. **Responsible disclosure.** When you find a real vulnerability in a service you legitimately use: **stop testing**, don't exfiltrate, report privately via the vendor's security contact (many publish `security.txt`, standardized in RFC 9116), allow reasonable remediation time, and don't publish or demand rewards before coordination. *Public disclosure without coordination harms users first.*

Professional codes put these in writing: the (ISC)² Code of Ethics, the ACM Code of Ethics and Professional Conduct, and IEEE's code all require protecting systems, avoiding harm, and honest disclosure. Cite the one your future profession publishes.

**Gray-area discipline.** "It's just looking" is still access. "No harm intended" is not a defense. "It was publicly reachable" describes *their* misconfiguration, not *your* authorization. Ethics resolves these before law has to.

### 5. The law you will actually meet

**Plain language.** Different countries criminalize the same acts with different wording. You are responsible for the law where *you* are, not where the target is.

**Technical detail.**

**Pakistan — Prevention of Electronic Crimes Act (PECA) 2016, as amended (incl. the Prevention of Electronic Crimes (Amendment) Act, 2025).** Purpose: criminalize core cyber offenses while enabling investigation. The 2025 amendment notably replaced the Federal Investigation Agency's Cyber Crime Wing with a new **National Cyber Crime Investigation Agency (NCCIA)**. Key offense categories you must recognize (summaries for study — always consult the official text for sections and current wording):

- **Unauthorized access** to information systems or data.
- **Unauthorized copying, transmission, or disclosure** of data (including password/traffic interception provisions).
- **Data and system interference** — damaging, deleting, altering, or interrupting data or system function.
- **Cyber-terrorism** — threats to public safety, national security, or critical systems through information systems.
- **Electronic forgery and electronic fraud** — making or using false data for gain.
- **Production, supply, or obtaining unauthorized access devices/code.**
- **Disclosure of confidential information** obtained through authorized access (insider-style offenses).
- **Online child sexual abuse material**, hate speech, and defamation-related provisions.
- **Spoofing** (identity/domain impersonation) and provisions affecting critical cyber infrastructure, including incident-reporting duties for operators.

**European Union — GDPR** (Regulation (EU) 2016/679): regulates *personal data* (any information identifying a person) globally — organizations serving EU residents fall under it regardless of location. Principles: lawfulness/fairness/transparency, purpose limitation, data minimization, accuracy, storage limitation, integrity/confidentiality, accountability. Consequences of failure are administrative fines — a *privacy* regime, not primarily a criminal code.

**United States — CFAA (Computer Fraud and Abuse Act)**: the classic "unauthorized access / exceeding authorized access" statute; the conceptual lesson: access *permission* defines the crime line, and terms-of-service violations have been litigated as access questions.

**Contrast table:**

| Dimension | PECA 2016 (as amended) | GDPR | CFAA |
|---|---|---|---|
| Core focus | Cyber offenses against systems, data, people | Protection of personal data & individual rights | Unauthorized computer access & damage |
| Nature | Criminal law (+ duties/reporting) | Regulatory/administrative (+ significant fines) | Federal criminal law |
| Typical triggers here | Scanning/accessing systems without permission; data theft; interference | Collecting/processing personal data of EU persons | Accessing systems beyond permission |
| Practical lesson for you | Get written authorization; never touch others' systems | Minimize and protect personal data in labs/reports | Authorization, not "publicly reachable," defines legality |

**Law vs. ethics:** lawful ≠ ethical (a legal but deceptive practice), ethical ≠ lawful elsewhere (whistleblowing). This course requires *both*.

---

## Worked Example: An Annotated Household Policy

Draft for "the Haq household" — every required clause labeled:

```text
HOUSEHOLD INFORMATION SECURITY POLICY            [document owner: A. Haq]
---------------------------------------------------------------------------
PURPOSE:  Protect family accounts, finances, and privacy at home.   ← purpose
SCOPE:    All family members, devices, guest Wi-Fi; guests when using
          our network.                                              ← scope
ROLES:    Owner/maintainer: A. Haq (router, updates).
          Users: all members (follow rules below).
          Report-to: A. Haq, immediately, phone ______.             ← roles
REQUIREMENTS:
 1. Passwords: unique per account, 14+ characters, stored in the
    family password manager; MFA on email and banking.              ← policy+standard
 2. Devices: screen lock ≤ 2 min; updates automatic; full-disk
    encryption where available.                                     ← standard
 3. Guests: join "Guest" network only; password shared verbally,
    changed monthly.                                                ← procedure hook
 4. Backups: important folders synced + weekly offline copy.        ← policy
INCIDENTS: unplanned charge, weird login email, lost phone →
    1) change password, 2) enable/verify MFA, 3) call bank, 4) note
    what happened (time, device) for the record.                    ← procedure
ENFORCEMENT: repeated rule-breaking = device review by owner.       ← enforcement
REVIEW: every 6 months or after any incident.         ← review date
```

Why it works: one page, every clause *checkable*, roles named, review date set. Contrast with "Everyone should be careful with passwords" — no scope, no standard, no way to verify; it is a guideline pretending to be a policy.

---

## Step-by-Step Procedures

### Procedure A — Draft a security policy set (household scale)

1. **Declare purpose and scope** — one sentence each; write what's excluded.
2. **Name roles** — owner/maintainer, users, report-to contact.
3. **List 4–6 requirement areas:** passwords/MFA, devices & updates, network & guests, backups, data handling, incident response.
4. For each area write **policy (what)** → **standard (which specific level)** → **procedure (how, only where needed)**.
5. Add **enforcement** and **review date** clauses.
6. **Self-test:** can a family member verify compliance *without asking you*? Rewrite anything they couldn't.
7. **Dry-run one incident** against your own incident clause — time your steps; fix gaps.
8. **Schedule the review** (calendar entry, 6 months).

### Procedure B — Authorization check (use before every future lab)

Before any active testing — including this course's labs — confirm and record:

1. **System:** exact hostnames/IP ranges/URLs in scope.
2. **Permission:** who granted it, in writing (email/doc counts; template below), and until when.
3. **Methods:** what's allowed (scan? exploit? social-engineering — usually prohibited).
4. **Exclusions:** what's explicitly out (production data, third parties).
5. **Stop conditions:** whom to contact if something unexpected appears.
6. **Record it** in your portfolio — M12 makes this a formal Rules of Engagement document.

```text
AUTHORIZATION TO TEST — [name]
I, [owner name], owner/authorized representative of [systems/ranges],
authorize [your name] to perform security testing on the above,
from [date] to [date], methods: [list]. Out of scope: [list].
Emergency contact: ______   Signature: ______  Date: ______
```

---

## Common Mistakes, Misconceptions, and Troubleshooting

| Mistake / misconception | Why it is wrong | Correction |
|---|---|---|
| "If no harm results, no offense" | Unauthorized *access itself* is the offense in PECA/CFAA-style laws | Harmlessness ≠ authorization |
| "It was on the internet, so it was public domain" | Reachability is their misconfiguration; touching it is still your act | Stop; report via responsible disclosure |
| "Compliance = security" | Checklists lag attackers; you can pass and still burn | Governance checks *outcomes*, not only checkboxes |
| "Policy is IT's job / policy = software config" | Policy is a management decision expressed in writing; config *implements* it | Every technical control should trace to a written rule |
| "Ethics is just obeying the law" | Law is the floor; professional codes demand more (disclosure, minimization) | Apply the four anchors (§4) even when law is silent |
| Copying another country's law as "the rules" | Your conduct is judged where *you* act | Study PECA for local context; know GDPR/CFAA only as contrast (§5) |
| Policy without review date or owner | It silently rots | Every document: owner + next review date |
| Testing "just a little" on an employer's system during class exercises | Course exercises authorize lab systems only | Your work engagement — not this course — must authorize work systems |

**Troubleshooting:** *Policy draft feels vague* → every sentence must be verifiable ("updates automatic" ✅ "keep things secure" ✗). *Authorization feels bureaucratic for a small favor* → one paragraph + a reply email is 60 seconds; an unrecorded favor becomes your word against theirs. *Can't decide if something is legal* → if you're asking, don't; take the ethical path (stop, document, disclose).

---

## Lab 3 — Policy Set and Ethics Case Analyses

*Writing-only lab. Overview: [Lab Collection](../../labs/README.md).*

**Applied practice (no dedicated lab):** [LAB-14 — Incident Response Tabletop Exercise](../../labs/lab-14-ir-tabletop/README.md) (governance, legal, and communication decisions under pressure) · [LAB-02 — Risk Register](../../labs/lab-02-threat-model-risk-register/README.md) (risk-treatment decisions) · [Full lab collection](../../labs/README.md).

**Objective:** a complete household/personal policy set + reasoned analysis of five gray-area cases.

**Steps:**

1. Create `portfolio/M03/`.
2. Draft `policy-set.md` using **Procedure A**: purpose, scope, roles, ≥ 4 requirement areas (policy/standard/procedure as needed), enforcement, review date — modeled on the worked example (your own content, not a copy).
3. Complete the **authorization template** for yourself as both grantor and grantee of a hypothetical lab test between two friends (system, dates, methods, exclusions filled in).
4. `ethics-cases.md` — analyze each vignette with the four anchors (authorization, scope, privacy, disclosure), state *stop / proceed / proceed-with-conditions*, and cite the principle that decides it:
   - (a) A friend says "hack my website, I don't mind" over a voice note.
   - (b) Your home router's admin page is open with a default password — from your own flat's Wi-Fi.
   - (c) You discover a classmate portal that lists all students' phone numbers when you change an ID in the URL.
   - (d) A company's cloud bucket appears to expose documents; you've found no security contact yet.
   - (e) You run a port scan "just to see" against your university's public Wi-Fi range during a lab exercise.
5. **Essay (graded-style practice, ~300 words):** "Why authorization must be written, specific, and current — and how the same tool becomes crime or defense." Use at least one PECA offense category and one ethical anchor.
6. Safety statement: targets used = *none (analysis only)*.

**Completion check:** policy passes the §Procedure-A self-test; all 5 cases decided with anchors; essay cites PECA category + ethical anchor.

---

## Knowledge Check

*Formative — self-graded; retake until ≥ 80% (8 of 10). The Lab 3 essay (step 5) is the scenario component; grade it against the 4-criterion rubric: accuracy, justification, safety/ethics reasoning, clarity.*

**Extend your practice:** [Module 03 quiz — more questions, worked answers, and outcome mapping](../../assessments/level-1/quiz-m03.md) · module-end review exercises are on the same page · [Assessment Hub](../../assessments/README.md)

**Multiple choice (6):**

1. "All customer data must be encrypted in transit" is an example of which layer?
   - (a) Procedure  (b) Guideline  (c) Policy  (d) Standard
2. Which pair is correctly matched?
   - (a) Standard — WHY a rule exists  (b) Procedure — step-by-step HOW  (c) Guideline — mandatory for all staff  (d) Regulation — optional internal rule
3. Under GDPR, "collect only what you need" expresses which principle?
   - (a) Data minimization  (b) Obfuscation  (c) Non-repudiation  (d) Defense in depth
4. Your authorized test expands, uninvited, to the target's office router because "I was already there." This violates:
   - (a) Availability  (b) Scope — a core ethical and often legal boundary  (c) The review date  (d) Data minimization only
5. Which statement about compliance and security is true?
   - (a) Compliance guarantees security  (b) You can be compliant and still breached  (c) Security makes compliance irrelevant  (d) They are identical
6. PECA 2016's 2025 amendment is notable for:
   - (a) Legalizing penetration testing  (b) Replacing the FIA Cyber Crime Wing with the NCCIA  (c) Abolishing unauthorized-access offenses  (d) Adopting GDPR principles wholesale

**Short answer (4):**

7. Draw (in text) the policy hierarchy from laws down to guidelines, and give one example of each level relevant to passwords.
8. Explain the difference between *policy* and *standard* using the topic of software updates.
9. State the four ethical anchors of security work and what each forbids in one short example.
10. Contrast PECA and GDPR in one sentence each: what does each primarily regulate, and what is the main consequence of violation?

<details>
<summary><b>Answer key</b> — attempt the questions first</summary>

1. **(c) Policy** — the WHAT/WHY statement; the specific "TLS 1.2+" detail would be the standard beneath it.
2. **(b)** — procedures are HOW; standards are mandatory specifics; guidelines are recommendations; regulations come from outside.
3. **(a)** — purpose limitation and data minimization are core GDPR principles.
4. **(b)** — authorization covers only what was agreed; expansion needs new written permission (scope creep is the classic authorized-test failure).
5. **(b)** — compliance proves rules were followed; attackers don't read checklists (governance must verify outcomes).
6. **(b)** — the amendment created the NCCIA to replace the FIA's Cyber Crime Wing (verify current status against the official text when citing).
7. *Laws/regulations* (PECA — mandatory) → *Policy* ("MFA required for email" ) → *Standard* ("TOTP app or passkey; 12+ digits where applicable" — concrete/measurable) → *Procedure* ("Enable MFA: 1. log in… 2. scan QR… 3. store recovery codes" ) → *Guideline* ("Consider a hardware security key as well").
8. Policy states the requirement and reason ("systems receive security updates within 30 days of release" — owner: management); the standard specifies the measurable bar ("automatic updates enabled; emergency patches ≤ 72 h"); the procedure gives the admin's exact steps. One sentence each, different altitude.
9. **Authorization** — forbids touching systems without explicit written permission (no "just looking"); **Scope** — forbids testing beyond agreed systems/methods (the router example); **Privacy/Minimization** — forbids collecting data beyond proving the finding (don't exfiltrate "extra" records); **Responsible disclosure** — forbids public disclosure/reward demands before coordinated reporting (use the vendor's security contact / security.txt).
10. *PECA:* criminalizes cyber offenses against systems, data, and people in Pakistan — consequence: criminal liability (with NCCIA enforcement post-amendment). *GDPR:* regulates how organizations process EU-related personal data — consequence: administrative fines and remediation orders for the organization.

</details>

## Scenario Exercises (Practice)

*Practice — graded checkpoint S1 (the Level 1 scenario exercise) is issued after this module; these prepare you for it.*

1. **The over-enthusiastic volunteer.** A small charity lets you "look at their website for free." Within ten minutes you've found an admin panel, and out of curiosity you've also enumerated their Wi-Fi network from the parking lot. Identify every boundary crossed (authorization, scope, privacy), and write the email you should send now — including what you will *not* include (data you saw).
2. **Policy or poster?** Evaluate this sentence: "We take security seriously." Rewrite it into a compliant policy + standard + procedure triple with owner and review date.
3. **Jurisdiction puzzle.** A Lahore-based freelance developer processes personal data of clients in Germany and stores backups on a US cloud provider. Which legal regimes plausibly touch this arrangement, and which local law always applies to the developer's own conduct? (Reason it out from §5; one paragraph.)

## Key Takeaways

1. **Governance** = who decides, what they decide (risk appetite), and how it's checked — CSF 2.0's *Govern* function; **compliance is a subset, not a synonym, of security.**
2. Policies form a **hierarchy**: laws → policy (what/why) → standard (which) → procedure (how) → guideline (recommended). Every durable policy carries **purpose, scope, roles, enforcement, and a review date.**
3. The **four ethical anchors** — authorization, scope, privacy/minimization, responsible disclosure — govern every practical in this course and every future engagement.
4. **PECA 2016 (as amended, incl. 2025)** criminalizes unauthorized access, data/system interference, forgery/fraud, disclosure of confidential information, cyber-terrorism, spoofing, and more — with the NCCIA now the lead investigating body; GDPR regulates personal-data processing; CFAA anchors US unauthorized-access law.
5. **Law is the floor; ethics is higher.** "No harm," "publicly reachable," and "I was only looking" are not defenses.
6. **Written, specific, current authorization** — with recorded scope, methods, and stop conditions — is what separates a security professional from an offender.

## Self-Assessment Checklist

- [ ] I can draw the policy hierarchy and give a real example of each of its five layers.
- [ ] I can list the clauses every valid policy needs (purpose, scope, roles, requirements, enforcement, review date).
- [ ] I completed a household/personal policy set that passes the "verify without asking" self-test.
- [ ] I can state the four ethical anchors with an example of what each forbids.
- [ ] I can summarize PECA's offense categories and the 2025 amendment's NCCIA change, and contrast PECA with GDPR and CFAA in a table.
- [ ] I filled the authorization template completely (system, dates, methods, exclusions, contacts).
- [ ] I decided all five ethics vignettes using named principles, not opinions.
- [ ] I scored ≥ 80% on the knowledge check and drafted the essay.

*If more than two boxes are unchecked, redo Procedure A and §5 before continuing — Levels 2–3 assume this frame.*

## Further Reading

Verified as of 2026-10-09; law changes — always check the current official text before citing.

- **PECA 2016 official text and 2025 amendment** — National Assembly of Pakistan documents: <https://www.na.gov.pk> (search "Prevention of Electronic Crimes"); also Pakistan Penal Code/official gazette copies via the Ministry of Information Technology and Telecommunication. Summaries in this course are for study, not legal advice.
- **GDPR full text** — EUR-Lex: <https://eur-lex.europa.eu/eli/reg/2016/679/oj>.
- **(ISC)² Code of Ethics** — <https://www.isc2.org/ethics>.
- **ACM Code of Ethics and Professional Conduct** (2018) — <https://www.acm.org/code-of-ethics>.
- **RFC 9116 — security.txt** (April 2022, the standard contact file for responsible disclosure): <https://www.rfc-editor.org/rfc/rfc9116>.
- **OWASP Vulnerability Disclosure Cheat Sheet** — practical handling guidance: <https://cheatsheetseries.owasp.org/cheatsheets/Vulnerability_Disclosure_Cheat_Sheet.html>.
- **CFAA overview (conceptual)** — US DOJ Computer Crime & Intellectual Property Section materials: <https://www.justice.gov/criminal-ccips>.

---

**Navigation:** [← Previous: Module 02](../module-02-threats-vulnerabilities-risk-and-controls/README.md) · [Module index](../README.md) · [Next: Module 04 →](../module-04-networking-fundamentals-for-security/README.md) · [Reference Library](../../reference/README.md)
