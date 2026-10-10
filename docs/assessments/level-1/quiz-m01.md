---
title: "Module 01 Quiz — Foundations and the CIA Triad"
layout: default
---

# Module 01 Quiz — Foundations and the CIA Triad

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 short answer) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Attempt *every* question before revealing any answer. For multiple choice, pick the single best answer. For short answer, write 2–4 sentences in your own words. Mark yourself against the worked answers, then re-attempt anything you missed. Recall the rule: a wrong first attempt is data, not a penalty.

**Coverage.** Maps to Module 01 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m01--information-security-foundations-and-the-cia-triad)). Each answer links back to the lesson section that teaches it.

**Related:** [Module 01 lesson](../../modules/module-01-information-security-foundations/README.md) · [LAB-01](../../labs/lab-01-cia-case-analysis/README.md) · [CS-1 case study](../case-studies/cs-1-breach-at-meridian.md)

> **Safety reminder:** case analysis here uses fictional and synthetic scenarios only; any hands-on practice follows the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** A hospital's X-ray images are silently altered by faulty storage software and no alarm ever fires. Which pillar of the CIA triad fails *first and foremost*?

- (a) Confidentiality
- (b) Integrity
- (c) Availability
- (d) Authenticity

**Q2.** Which statement best defines **risk**?

- (a) Any vulnerability that a scanner reports
- (b) The uncertainty of loss when a threat can exploit a vulnerability *and* the resulting impact matters
- (c) An attack that has already occurred
- (d) The number of firewalls an organization has deployed

**Q3.** Which of these is an **information asset**?

- (a) The office chair
- (b) The spreadsheet of student grades
- (c) The building's electricity bill
- (d) The security guard

**Q4.** A power cut leaves a service unreachable for six hours. Confidentiality and integrity were never touched. Which pillar failed?

- (a) Confidentiality
- (b) Integrity
- (c) Availability
- (d) None — nothing was stolen

**Q5.** Which statement about **controls** is correct?

- (a) A control eliminates risk entirely
- (b) A control is only a product you buy
- (c) A control reduces risk and always costs something
- (d) A control is the same thing as a vulnerability

**Q6.** In the CIA triad, **integrity** means information is:

- (a) Secret from everyone
- (b) Fast to access
- (c) Changed only by authorized, known processes
- (d) Encrypted at rest

**Q7.** Which pairing correctly matches a **defense-in-depth layer** to its control?

- (a) People layer — firewall rule
- (b) Data layer — encryption and backups
- (c) Network layer — awareness training
- (d) Process layer — cable lock

**Q8.** Which NIST CSF 2.0 Function asks, *"How would we know something bad is happening?"*

- (a) Govern
- (b) Identify
- (c) Detect
- (d) Recover

## Part B — Short answer (4)

**Q9.** In your own words, distinguish a **threat** from a **vulnerability**, giving one example of each drawn from the *same* scenario.

**Q10.** Give two examples of an **availability** violation and one control that would address each.

**Q11.** Explain how mandating a very long, complex passphrase — with no password manager allowed — can create a *new* vulnerability. Reason using people / process / technology.

**Q12.** You are handed a new shared project folder at work. Using the six-step CIA impact-analysis procedure from the lesson, list the **first three steps** you would take.

---

## Worked answers

<details>
<summary><b>Part A answers</b> — attempt the questions first</summary>

**Q1 — (b) Integrity.** Data changed without authorization, and detection also failed. *Misconception:* (a) confidentiality would require someone to have **read** the images — they were altered, not viewed; (c) availability held (the files stayed reachable); (d) authenticity is the adjacent question “are these the real images?”, but the primary failure is that the data is **wrong**.

**Q2 — (b).** Risk is *not* the same as vulnerability — a scanner finding is a vulnerability; risk combines that weakness with a reachable threat *and* a meaningful impact. *Misconception:* (a) confuses one *ingredient* with the whole; (c) is realized loss (an incident), not the uncertainty of loss; (d) counts controls, which measure effort, not exposure.

**Q3 — (b).** The grades carry information value and have an owner. *Misconception:* (a), (c), and (d) are physical resources that *support* work with information — protecting the chair, the bill, or the guard protects no confidentiality, integrity, or availability.

**Q4 — (c) Availability.** C and I held; authorized users simply could not obtain the service — the classic “nothing was stolen but we still lost” case. *Misconception:* (d) applies only the confidentiality lens (“stolen”); the pillars fail independently of theft.

**Q5 — (c).** Controls *reduce* risk — never to zero — and each costs money, time, or convenience. *Misconception:* (a) confuses a control with a guarantee (“we bought the tool” ≠ “we are secure”); (b) ignores that policies and awareness are controls too.

**Q6 — (c) Integrity.** Authorized, *known* change only — including the ability to *detect* unauthorized change, not just prevent it. *Misconception:* (a) is confidentiality's definition; (d) encryption is a *mechanism* that can support confidentiality or integrity, not the principle itself.

**Q7 — (b) Data-layer protection.** Encryption and backups protect the data itself. *Misconception:* (a) and (c) swap layers — awareness training is the *people* layer, cable locks are *physical*; (d) confuses the *process* layer with *physical* — mismatched layers is the standard trap.

**Q8 — (c) Detect.** “How would we know?” is detection. *Misconception:* (a) Govern = who decides and what the rules are; (b) Identify = what do we have; (d) Recover = how do we get back to normal — none of them answers *how would we know*.

*Common distractor note:* "Authenticity" (option d in Q1) is about whether something is genuine — real vs forged — not whether correct data was changed. If you picked it, revisit the authenticity/non-repudiation paragraph.

</details>

<details>
<summary><b>Part B model answers</b> — compare your reasoning</summary>

**Q9.** A **threat** is a *potential cause* of harm (a burglar, a flood, a bored employee). A **vulnerability** is a *weakness* that lets that cause succeed (an unlocked window, an unpatched bug). Same scenario — home network: the *threat* is a neighbour misusing your Wi-Fi; the *vulnerability* is the router's default admin password. One is the actor/event, the other is the gap it exploits. → [Lesson §3](../../modules/module-01-information-security-foundations/README.md)

**Q10.** *(a)* A website knocked offline by a DDoS flood — control: DDoS mitigation or a CDN. *(b)* Files unreadable after a disk dies with no backup — control: tested 3-2-1 backups (three copies, two media types, one offsite). Both are "authorized users cannot get what they need."

**Q11.** If users cannot *remember* a long random passphrase and are forbidden a password manager, they will write it on a sticky note or reuse a predictable variant — converting a technical strength into a people/process weakness. The fix is length **paired with** a password manager and a no-reuse rule, not length alone. → [People/process/technology, Lesson §5](../../modules/module-01-information-security-foundations/README.md)

**Q12.** (1) **List the assets** in the folder (the files and who depends on them). (2) **Name the owner** — the accountable person. (3) **Rate confidentiality impact** if the folder leaked (then, in steps 4–6, integrity, availability, and the top control). → [Six-step procedure](../../modules/module-01-information-security-foundations/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

These pull the whole module together. Write full answers, then compare with the sketches below.

1. **The club laptop.** A student club keeps its member list and treasury spreadsheet on one laptop everyone borrows. Give one likely violation of *each* pillar (C, I, A), one practical control for each, and name the asset owner.
2. **"It's in the cloud now, we're done."** A small company moves all documents to an encrypted cloud drive and the IT lead declares the job finished. Using people/process/technology and the CSF functions, name **three** things this overlooks.
3. **Control trade-off.** Management proposes a 12-character passphrase, changed every 30 days, no password manager. Analyse the confidentiality benefit *and* the new risks. Propose a better balance.
4. **Incident-to-triad drill.** Take any recent public breach. Fill a three-row table: which pillar failed, which vulnerability enabled it, which safeguard would have prevented *or* detected it. Note that one control rarely covers all three pillars.

*Review guidance:* 1 — C: others read the member list (owner: club treasurer); I: treasury edited with no version history; A: single laptop, no backup. Controls: login-per-user, version history + change alerts, an offsite backup. 2 — access management/who owns the data, patching and configuration drift, logging and recovery, and the shared-responsibility gap. 3 — the benefit is real, but forced rotation without a manager drives reuse and sticky notes; propose length + manager + MFA + no forced rotation. 4 — expect exactly one dominant pillar per breach with a *different* fix and a *different* detection method.

**Next:** [Module 02 quiz](./quiz-m02.md) · return to the [Assessment Hub](../README.md)
