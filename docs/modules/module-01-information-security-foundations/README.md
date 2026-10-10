---
title: "Module 01 — Information Security Foundations and the CIA Triad"
layout: default
---

# Module 01 — Information Security Foundations and the CIA Triad

> **Level 1 · Foundations · Beginner · Estimated study time: 8–10 hours**
> **Prerequisites:** none — this is the entry point of the course.

## Why This Module Matters

Every security headline — a bank app leaking customer data, a hospital shutting down after ransomware, a vote count nobody can verify — is a story about the same three ideas: information that should have been **secret**, information that should have been **untouched**, or a service that should have been **available**. Before you can configure a firewall or analyze malware, you need a precise vocabulary for what is being protected, from whom, and why. This module gives you that vocabulary. It is deliberately tool-free: you will think, write, and classify rather than type commands. Learners who skip foundations end up memorizing tool flags without knowing what they are protecting — and that shows the moment a real decision is in front of them.

## Prerequisites and Estimated Study Time

- **Prerequisites:** none. You need only basic computer literacy (installing software, managing files) and comfortable reading English.
- **Estimated study time:** 8–10 hours — roughly 3 hours of reading, 3 hours on the exercises and lab, 1–2 hours on the knowledge check and revision.
- **Tools:** none required. A plain text editor (Notepad++, VS Code, or even paper) is enough.

## Learning Outcomes

By the end of this module, you can:

1. Define information security, cybersecurity, and *information asset* in your own words with accurate examples. *(Remember)*
2. Explain the CIA triad and give two real-world examples of each pillar's violation and corresponding safeguard. *(Understand)*
3. Distinguish *threat*, *vulnerability*, *risk*, and *control* in at least 8/8 scenario cards. *(Understand)*
4. Classify a personal asset inventory by confidentiality, integrity, and availability impact. *(Apply)*

---

## Core Concepts

### 1. Information, information security, and information assets

**Plain language.** *Information security* (often shortened to *infosec*) means keeping information useful and safe: the right people can use it, the wrong people cannot read it or change it, and it works when someone needs it. *Cybersecurity* is the same goal when the information lives on computers and networks — in practice the terms overlap heavily, and this course uses them interchangeably.

**Technical detail.** You protect *information*, not just *files*. An **information asset** is anything that carries value in information form: a customer database, an email mailbox, a source-code repository, a spreadsheet of exam marks, even the trust in your identity documents. Every asset has an **asset owner** — the person or role accountable for deciding how it is protected (you, your team lead, a registrar). Ownership is accountability, not possession: your university owns your student record, but you still suffer if it leaks.

Key terms used from here on:

| Term | Definition |
|---|---|
| **Information asset** | Data or knowledge in any form that has value to someone |
| **Asset owner** | The person/role accountable for an asset's protection decisions |
| **Confidentiality** | Information is seen only by those authorized to see it |
| **Integrity** | Information and code are changed only by authorized, known processes |
| **Availability** | Information and services are usable when authorized users need them |
| **Threat** | Anything that *could* cause harm — an actor (a burglar) or an event (a flood) |
| **Vulnerability** | A weakness that a threat can exploit — an unlocked door, an unpatched bug |
| **Risk** | The uncertainty of loss, arising from a threat exploiting a vulnerability *and* how much it would matter |
| **Control** | Anything you put in place to reduce risk — a lock (technical), a rule (administrative), a safe (physical) |

**Example.** Your photo library is an information asset; you are its owner. Your little brother (threat) knowing your password (vulnerability) could expose private photos (risk). A password change plus a screen lock (controls) reduces that risk.

### 2. The CIA triad

**Plain language.** The **CIA triad** — **C**onfidentiality, **I**ntegrity, **A**vailability — is the three-question test you will apply to every system in this course: *Can the wrong people read it? Can the wrong people change it? Does it work when needed?*

**Technical detail.**

- **Confidentiality** fails when data is disclosed to anyone not authorized: a misconfigured cloud bucket, an email sent to the wrong list, spyware on a laptop. Controls: encryption, access control, need-to-know rules.
- **Integrity** fails when data changes without authorization *or without detection*: a grade changed in a database, a tampered invoice, corrupted files after a crash, a browser extension silently rewriting pages. Controls: hashes, digital signatures, version control, input validation, backups.
- **Availability** fails when authorized users cannot get what they need: ransomware encrypting files, a distributed denial-of-service (DDoS — many machines flooding a server with traffic until it collapses), a power cut, or simply a hard disk that nobody backed up. Controls: backups, redundancy (spare components/systems), disaster-recovery planning, capacity planning.

Two supporting properties appear throughout the course: **authenticity** (a communication or identity is genuine — the bank email really is from the bank) and **non-repudiation** (an action cannot be plausibly denied later — a signed transaction record proves who approved it).

**Worked example — three pillars, one service.** A university announces exam results on a web portal:

| Scenario | Pillar violated | What went wrong | Safeguard |
|---|---|---|---|
| Results visible to any student who changes the roll-number in the URL | Confidentiality | The portal checked login, not ownership of the record | Server-side authorization checks (Module 07) |
| A student's marks change from 78 to 88 with no examiner action | Integrity | Database writable through an unmonitored interface | Input validation, change logging, database access control |
| Portal unreachable on result day because it was never load-tested | Availability | Capacity not planned for peak demand | Load testing, scaling, a static fallback page |
| Portal stays offline for three days after a server failure | Availability | No spare capacity or recovery plan | Redundant servers + tested backup/restore (this module's Module 05 preview) |

Notice the pattern: the *same* system can fail each pillar independently, and each failure has a different owner, a different fix, and a different detection method. Security work is largely about never letting these three blur together.

### 3. Threats, vulnerabilities, risks, and controls

**Plain language.** Think of a house: a *threat* is anyone or anything that could break in — a burglar, or a storm. A *vulnerability* is the open window. The *risk* is how likely the break-in is **and** how much you would lose if it happened. A *control* is the lock you add to the window.

**Technical detail.** These four words are used with precision in this course, and confusing them is the most common beginner error:

- A **threat** is a *potential cause* of harm. Threats can be people (an attacker), events (fire, flood), or accidents (an employee deleting a table).
- A **vulnerability** is a *weakness* — in software (an unpatched bug), hardware, configuration (a default password), a process (no backup routine), or people (no awareness training). Vulnerabilities exist whether or not any threat can reach them.
- A **risk** combines the three: *risk arises when a threat can exploit a vulnerability, and the resulting loss matters*. A vulnerability with no reachable threat and no impact is a low risk; a mild vulnerability with catastrophic impact (a backup system that was never tested) can be a high one.
- A **control** (also *safeguard* or *countermeasure*) is what you do about risk. Controls don't remove risk — they *reduce* it, and every control costs something (money, speed, convenience).

**The critical insight:** risk is not the same as vulnerability. Scanners report vulnerabilities; **you** decide risk. Module 02 teaches you to score and rank it.

### 4. Defense in depth

**Plain language.** Never rely on one lock. Stack several independent layers so that if one fails, the next catches the problem.

**Technical detail.** *Defense in depth* arranges controls so an attacker (or accident) must defeat multiple independent layers — reducing the chance any single failure becomes a disaster.

```text
        ┌───────────────────────────────────────────────┐
        │  Awareness & policies (people)                │
        │  ┌─────────────────────────────────────────┐  │
        │  │  Physical: locked door, access card     │  │
        │  │  ┌───────────────────────────────────┐  │  │
        │  │  │  Network: firewall, segmentation  │  │  │
        │  │  │  ┌─────────────────────────────┐  │  │  │
        │  │  │  │  Host: patching, hardening  │  │  │  │
        │  │  │  │  ┌───────────────────────┐  │  │  │  │
        │  │  │  │  │  App: input checks,   │  │  │  │  │
        │  │  │  │  │  authn/authz          │  │  │  │  │
        │  │  │  │  │  ┌─────────────────┐  │  │  │  │  │
        │  │  │  │  │  │ Data: encryption│  │  │  │  │  │
        │  │  │  │  │  │ + backups       │  │  │  │  │  │
        │  │  │  │  │  └─────────────────┘  │  │  │  │  │
        │  │  │  │  └───────────────────────┘  │  │  │  │
        │  │  │  └─────────────────────────────┘  │  │  │
        │  │  └───────────────────────────────────┘  │  │
        │  └─────────────────────────────────────────┘  │
        └───────────────────────────────────────────────┘
```

Each layer needs its own **security baseline** — a documented minimum configuration considered "correct" (e.g., "all workstations: disk encryption on, updates automatic, local firewall on"). You will build baselines in Module 05 and test whether systems drift from them in later modules.

### 5. People, process, technology — and the trade-offs

**Plain language.** Security is never just a product. Every protection has three parts: the *tool* (firewall), the *rule and the person following it* (policy: only admins may change rules), and the *process that keeps both working* (quarterly rule review).

**Technical detail.** Most real failures are not "the software was broken" but "the process was missing" or "the person wasn't told": the patch existed for months but no process applied it; the bucket was secure by default and someone turned it off. Expect every recommendation in this course to have all three dimensions.

Security also **trades off against usability and availability**. The most secure computer is unplugged and locked in a safe — and useless. Strong controls (long unique passwords, mandatory MFA) cost user patience; excessive control invites workarounds, which create *new* vulnerabilities. Your job as a security practitioner is to find the balance that protects the *mission*, not to maximize security in isolation.

### 6. The big picture: NIST CSF 2.0

**Plain language.** A shared map of everything security work covers, so nothing gets forgotten.

**Technical detail.** The **NIST Cybersecurity Framework (CSF) 2.0** (National Institute of Standards and Technology, US, February 2024) organizes all security activity into six **Functions**. It is free, widely referenced, and used as course shorthand throughout:

| Function | One-line question |
|---|---|
| **G**overn | Who decides, what are the rules, and how is this managed? *(new in 2.0)* |
| **I**dentify | What do we have, and what could go wrong? |
| **P**rotect | What stops bad things from happening? |
| **D**etect | How would we know something bad is happening? |
| **R**espond | What do we do when something bad happens? |
| **R**ecover | How do we get back to normal? |

This course's four levels map onto this arc: Level 1–2 build *Identify* and *Protect*, Level 3 builds *Detect* and *Respond*, Level 4 adds *Govern*-level concerns and *Recover* practice.

---

## Worked Example: Reading a Real-World Failure Through the CIA Lens

A small logistics company used a shared spreadsheet (stored in cloud sync) to track deliveries. One evening, a delivery driver's laptop was infected with credential-stealing malware. Attackers used the synced account to:

1. **Read** every customer's address and phone number → **confidentiality failure** (no MFA on the sync account; the laptop had no disk encryption and the browser stored the session — vulnerabilities).
2. **Silently edit** delivery addresses on several orders, redirecting two packages → **integrity failure** (no version history or change alerts on the sheet).
3. **Delete** the previous month's sheet "to cover tracks" → **availability failure** (the sync folder was the *only* copy; there was no independent backup — a *control* failure).

Map it yourself before reading on: *(a) Which single control would have blocked step 1? (b) Which would have detected step 2? (c) Which would have preserved step 3?*

**Evaluation:** (a) MFA on the account (Module 07) plus full-disk encryption (Module 05) — confidentiality layer; (b) version history/change notifications — integrity detection; (c) an independent 3-2-1 backup (three copies, on two kinds of media, one offsite) — availability recovery. Note that one control does not cover all three pillars: this is why the triad exists.

---

## Step-by-Step: CIA Impact Analysis (Your Core Procedure)

Apply this 6-step procedure to any system — your own accounts, a course project, a small office:

1. **List the information assets** (data stores, accounts, devices, services). If you cannot name the data, you cannot protect it.
2. **Name the owner** for each asset (a person or role — for personal assets, "me").
3. **Rate confidentiality impact** if the asset leaked: *Low* (embarrassing), *Moderate* (financial or reputational harm), *High* (safety, legal, or severe financial harm).
4. **Rate integrity impact** if altered without authorization: what wrong decision or harm follows from wrong data?
5. **Rate availability impact** if unavailable: what stops, for how long, at what cost?
6. **Record the top control** you already have and the single control you would add first. (You will learn to justify *why first* in Module 02.)

You will use this exact procedure in the lab below and repeatedly in later modules — for networks (M04), for identity (M07), and inside your capstone (M19).

---

## Common Mistakes, Misconceptions, and Troubleshooting

| Mistake / misconception | Why it is wrong | Correction |
|---|---|---|
| "Security = antivirus + firewall" | Those are two *controls*, mostly protecting one pillar on one layer | Think in pillars × layers (defense in depth) |
| "Confidentiality is the whole job" | Ransomware and outages attack *availability*; tampering attacks *integrity* | Test all three pillars every time |
| "The threat is hackers" | Threats also include storms, coffee spills, interns, and your own tired self at 2 a.m. | Classify threats as human / environmental / accidental |
| "We bought the tool, so we're secure" | Tools without process and people fail silently (unconfigured alerting, unapplied patches) | Ask: who owns this control, and how is it checked? |
| "Availability is a data-center concern; my laptop is different" | A laptop with no backup and a dead disk is an availability failure | Backups start at personal scale (Module 05) |
| "If there's no attacker, there's no risk" | Vulnerabilities + impact exist regardless of who shows up | Risk = threat × vulnerability × impact (formalized in M02) |
| Confusing *data* with the *system* | Backing up data doesn't restore a working service; recovering a server without data is pointless | Analyze assets at both levels |

**Troubleshooting your own understanding:** if you cannot, without notes, explain why "my website was defaced" is primarily an *integrity* problem with a *confidentiality* side-question (did the attacker read anything?), revisit Section 2's table and redo one row of the worked example.

---

## Lab 1 — Asset Inventory and CIA Classification

*This lab is thinking-and-writing only — no scanning, no tools. It satisfies the lab-safety policy trivially, but record it in your portfolio exactly as required so the habit is set. Overview: [Lab Collection](../../labs/README.md).*

**Dedicated lab worksheet:** [LAB-01 — CIA Triad Analysis of Organization Case Studies](../../labs/lab-01-cia-case-analysis/README.md) · [Full lab collection](../../labs/README.md).

**Objective:** build a CIA-graded personal asset inventory and analyze one real failure.

**Steps:**

1. Create `portfolio/M01/` in your course folder.
2. List 10–15 information assets you personally rely on: email account, phone, cloud drive, chat accounts, student/uni portal login, Wi-Fi router admin, laptop files, photos, financial app, saved passwords, etc.
3. For each asset, record: *owner*, *confidentiality impact* (L/M/H), *integrity impact* (L/M/H), *availability impact* (L/M/H), and one sentence justifying the highest rating. Use the Step-by-Step procedure above.
4. Sort the list by highest combined impact. Answer in `inventory.md`: *Which single asset would hurt most if lost today, and which pillar dominates its risk?*
5. Pick one widely reported security incident (any country, any year — e.g., search for "data breach" reports from a bank or hospital). Fill the three-pillar table: what failed (C/I/A), which vulnerability made it possible, and which safeguard would have prevented or detected it.
6. Write your safety statement line for the portfolio pack: targets used = *none (analysis only)*; isolation = *not applicable*.

**Completion check:** inventory of ≥ 10 assets, all four columns filled, one justified answer in step 4, one incident table in step 5.

---

## Knowledge Check

*Formative — self-graded with the answer key below; retake until ≥ 80% (10 of 12 correct). Attempt every question before opening the key.*

**Extend your practice:** [Module 01 quiz — more questions, worked answers, and outcome mapping](../../assessments/level-1/quiz-m01.md) · module-end review exercises are on the same page · [Assessment Hub](../../assessments/README.md)

**Multiple choice (8):**

1. A hospital's X-ray images are silently altered by faulty storage software and no alarm fires. Which pillar fails first?
   - (a) Confidentiality  (b) Integrity  (c) Availability  (d) Authenticity
2. "Risk" is best described as:
   - (a) any vulnerability found by a scanner  (b) the uncertainty of loss when a threat can exploit a vulnerability and the impact matters  (c) an attack that has already happened  (d) the number of firewalls deployed
3. Which item is an **information asset**?
   - (a) The office chair  (b) The spreadsheet of student grades  (c) The electricity bill of the building  (d) The security guard
4. A power cut makes a service unreachable for six hours despite perfect confidentiality and integrity. Which pillar failed?
   - (a) Confidentiality  (b) Integrity  (c) Availability  (d) None — nothing was stolen
5. Which statement about controls is correct?
   - (a) A control eliminates risk entirely  (b) A control is only a product you buy  (c) A control reduces risk and always costs something  (d) A control is the same as a vulnerability
6. In the CIA triad, "integrity" means information is:
   - (a) secret from everyone  (b) fast to access  (c) changed only by authorized, known processes  (d) encrypted
7. Which pairing correctly matches layer and control in defense in depth?
   - (a) People — firewall rule  (b) Data — encryption and backups  (c) Network — awareness training  (d) Process — cable lock
8. Which NIST CSF 2.0 Function asks "How would we know something bad is happening?"
   - (a) Govern  (b) Identify  (c) Detect  (d) Recover

**Short answer (4):**

9. In your own words, distinguish a *threat* from a *vulnerability*, with one example of each from the same scenario.
10. Give two examples of an availability violation and one control for each.
11. Explain why adding a mandatory long passphrase can create a *new* vulnerability (think people/process/technology).
12. Using the six-step CIA procedure, list the first three steps you would take when handed a new shared project folder at work.

<details>
<summary><b>Answer key</b> — attempt the questions first</summary>

1. **(b) Integrity** — data changed without authorization; detection also failed.
2. **(b)** — vulnerability alone is not risk; impact and exploitability combine into risk.
3. **(b)** — the grades carry information value; the chair does not.
4. **(c) Availability** — C and I held; authorized users could not get the service.
5. **(c)** — controls reduce risk and cost money/time/convenience; they never drive risk to zero.
6. **(c)** — authorized, known change only — including detecting unauthorized change.
7. **(b)** — data-layer protection; awareness is people-layer, firewall is network-layer, cable lock is physical.
8. **(c) Detect.**
9. *Model answer:* a threat is a potential cause of harm (a burglar, a flood); a vulnerability is a weakness that lets it happen (an unlocked window). In a home-network scenario the threat might be a neighbor using your Wi-Fi and the vulnerability the default router password — the same scenario, one cause and one weakness.
10. *Examples:* the website is down after a DDoS flood (control: DDoS mitigation/CDN) and files are unreadable after a dead disk with no backup (control: tested 3-2-1 backups).
11. Users, unable to remember long random passphrases, write them on sticky notes or reuse a predictable pattern — turning a technical strength into a people/process weakness. (Real guidance in Module 06/07: length helps *when paired with* password managers and never-reuse rules.)
12. (1) List the assets in the folder (files, who depends on them), (2) name the owner/accountable person, (3) rate confidentiality impact of a leak — then integrity and availability, then top control (steps 4–6).

</details>

## Scenario Exercises (Practice)

*Practice — not graded checkpoint S1 (that comes after Module 03). Write answers of 100–200 words each; compare against the reasoning taught above.*

1. **The shared club laptop.** A student club keeps its member list and treasury spreadsheet on a laptop that everyone borrows. Describe one likely violation of each pillar (C, I, A) and one practical control for each. Name the asset owner.
2. **The "secure" cloud drive.** A small company migrates all documents to a cloud drive. The IT lead says: "It's in the cloud now, it's encrypted, we're done." Using people/process/technology and the CSF functions, explain at least three things this statement overlooks.
3. **Control trade-off.** Management proposes locking the staff portal behind a 12-character passphrase changed every 30 days with no password manager allowed. Analyze the confidentiality benefit *and* the new risks this creates. What balance would you propose?

## Key Takeaways

1. Information security keeps information **confidential, integral, and available** — the CIA triad is the three-question test for every system you meet in this course.
2. **Assets have owners.** You protect information assets (data, accounts, services), and ownership means accountability for protection decisions.
3. **Threat ≠ vulnerability ≠ risk ≠ control:** a cause, a weakness, the uncertainty of loss, and what you do about it. Conflating them is the classic beginner error.
4. **Defense in depth** stacks independent layers; every layer needs a documented security baseline.
5. Security is **people + process + technology**, and it always trades off against usability and availability — max security that users bypass is zero security.
6. **NIST CSF 2.0** (Govern, Identify, Protect, Detect, Respond, Recover) is the shared map of the whole discipline — and of the rest of this course.
7. The six-step **CIA impact analysis** is your reusable core procedure — you will apply it again in M04, M05, M07, and the M19 capstone.

## Self-Assessment Checklist

Check every item you can honestly satisfy *without notes*:

- [ ] I can define information security and *information asset* with my own example.
- [ ] I can state the three pillars and give a distinct failure example for each.
- [ ] I can explain authenticity and non-repudiation and how they support the triad.
- [ ] I can distinguish threat, vulnerability, risk, and control in a fresh scenario (8/8 cards).
- [ ] I can draw or describe defense in depth with at least four layers.
- [ ] I can explain why security needs people, process, *and* technology.
- [ ] I can name the six NIST CSF 2.0 functions and what each asks.
- [ ] I completed Lab 1: inventory of ≥ 10 assets with CIA ratings and one incident analysis.
- [ ] I scored ≥ 80% on the knowledge check (retake as needed).
- [ ] I wrote my scenario exercises and can defend my reasoning.

*If more than two boxes are unchecked, re-read Sections 2–4 before moving on.*

## Further Reading

Verified editions as of 2026-10-09; confirm the publisher's page if citing later.

- **NIST Cybersecurity Framework 2.0** — NIST CSWP 29 (February 2024). Free PDF and web version: <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final>. Read the CSF 2.0 Quick-Start Guide for a shorter entry point.
- **NIST SP 800-12 Rev. 1, *An Introduction to Information Security*** (2017) — the clearest official introduction to the vocabulary and program-level view: <https://csrc.nist.gov/pubs/sp/800/12/r1/final>.
- **CISA, Cybersecurity Best Practices** — plain-language guidance from the US cyber agency: <https://www.cisa.gov/resources-tools>.
- **NIST SP 800-39, *Managing Information Security Risk*** (2011) — organization-level risk view for when you outgrow personal scope: <https://csrc.nist.gov/publications/detail/sp/800-39/final>.
- **ENISA Threat Landscape** (annual, free) — real-world examples to practice CIA analysis on current incidents: <https://www.enisa.europa.eu/topics/cyber-threats/threat-landscape>.

---

**Navigation:** [Module index](../README.md) · [Next: Module 02 →](../module-02-threats-vulnerabilities-risk-and-controls/README.md) · [Assessment Guide](../../assessment-guide.md) · [Lab Safety Policy](../../lab-safety-policy.md) · [Reference Library](../../reference/README.md)
