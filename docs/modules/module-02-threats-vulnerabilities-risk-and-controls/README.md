---
title: "Module 02 — Threats, Vulnerabilities, Risk, and Controls"
layout: default
---

# Module 02 — Threats, Vulnerabilities, Risk, and Controls

> **Level 1 · Foundations · Beginner · Estimated study time: 10–12 hours**
> **Prerequisites:** [Module 01](../module-01-information-security-foundations/README.md).

## Why This Module Matters

You have unlimited needs and a limited budget — of money, time, and attention. *Risk* is the tool that decides what gets protected first. Without it, security work devolves into two traps: buying whatever tool was advertised (spend without priority) or panicking over every headline (equal priority = no priority). This module turns the vocabulary of Module 01 into a working method: identify who might attack you, what weakness they could use, how likely and how costly it would be, and what to do first. You will build your first **risk register** — the single most reusable artifact in this course — and learn to read vulnerability reports like a practitioner rather than a passenger.

## Prerequisites and Estimated Study Time

- **Prerequisites:** [Module 01](../module-01-information-security-foundations/README.md) (CIA triad and the threat/vulnerability/risk/control vocabulary).
- **Estimated study time:** 10–12 hours — ~4 h reading, ~4 h labs (risk register + CVE sheet), ~2 h knowledge check and revision.
- **Tools:** a spreadsheet or Markdown editor; a browser for the NVD and CISA KEV catalog. All free.

## Learning Outcomes

By the end of this module, you can:

1. Identify common threat actors, motivations, and capability tiers (script kiddie → nation-state). *(Understand)*
2. Differentiate threat, vulnerability, exposure, likelihood, and impact using standardized definitions. *(Understand)*
3. Apply a simple risk formula (risk = likelihood × impact) to rank 8 risks on a 5×5 matrix. *(Apply)*
4. Select appropriate control types (preventive/detective/corrective; technical/administrative/physical) for given risks. *(Apply)*

---

## Core Concepts

### 1. Threat actors: who causes harm, and why

**Plain language.** A **threat actor** is the who behind a threat — a person or group that causes harm on purpose, or a force that does it without intent. Knowing *why* they act tells you *how* they act.

**Technical detail.** Actors differ along two axes: **motivation** (what they want) and **capability** (what they can do — tools, time, money, skill). The tiers below are a teaching ladder, not official categories:

| Tier | Who | Typical motivation | Typical capability | Example behaviors |
|---|---|---|---|---|
| Curious beginner (*script kiddie*) | Someone running others' tools | Thrills, bragging, learning | Low — public tools, little custom work | Mass scanning, using ready-made exploit kits |
| Hacktivist | Ideologically driven group | Politics, protest | Low–medium — defacements, DDoS campaigns | Targeted websites, publicity-driven attacks |
| Organized cybercriminal | Profit-driven group | Money | Medium–high — specialization, Ransomware-as-a-Service | Phishing, credential theft, extortion |
| Insider (malicious) | Employee/contractor | Revenge, money, ideology | **High access, low need to break in** | Abusing legitimate access, data theft |
| Insider (negligent) | Anyone | None — accident | Unlimited *access*, zero intent | Misdirected email, cloud share left public |
| Advanced persistent threat (APT) / nation-state | State-sponsored teams | Espionage, sabotage, strategic goals | Very high — time, custom tools, patience | Long hidden intrusions, supply-chain attacks |

**Worked example.** A student's personal blog: low-value target for criminals (little to steal), attractive to script kiddies (easy defacement for bragging), irrelevant to an APT. Contrast: a defense contractor's research share — APT-interest. *Same vulnerability, completely different risk:* this is why threat context matters before you score anything.

**The insight to keep:** many real incidents involve **no attacker at all** — misconfiguration, accidents, and environmental failures (the "threat actor" is gravity, coffee, or a tired administrator).

### 2. Vulnerabilities, exposure, and the vulnerability lifecycle

**Plain language.** A **vulnerability** is a weakness. **Exposure** is being *reachable* by a threat that could use that weakness — a hole in a wall nobody can reach is still a weakness, but not an exposure. **Likelihood** is how probable exploitation is; **impact** is how much it would matter if it happened.

**Technical detail.** Software vulnerabilities get permanent identifiers: a **CVE** (Common Vulnerabilities and Exposures) ID like `CVE-2024-12345`, assigned by the CVE program and catalogued in the US **NVD** (National Vulnerability Database). Severity is commonly expressed as a **CVSS** score (Common Vulnerability Scoring System — FIRST.org); version **4.0** (November 2023) is current. Scores run 0.0–10.0 with bands: *None* 0.0, *Low* 0.1–3.9, *Medium* 4.0–6.9, *High* 7.0–8.9, *Critical* 9.0–10.0. CVSS reflects technical severity; it is **not** your risk (more below).

Every vulnerability has a lifecycle — and risk changes at every stage:

```text
 Bug exists      Vendor learns     Patch         Public          Exploit        Patch
 (unknown)  ──►  of it        ──►  available ──► disclosure ──►  code often  ──►  widely
                  privately        (silent)      + CVE issued     appears        adopted
      │                                │              │              │             │
   risk: low,                 risk rising:       risk high:      risk peaks:   risk falls:
   no one knows it            you CAN fix        unpatched =      active attacks but many
                               — will you?        your choice      in the wild    never patch
                             ◄──── "patch gap" ────►
```

The gap between "patch available" and "patch installed" is where most mass compromise happens — this is a *process* failure, not a zero-day mystery. CISA's **Known Exploited Vulnerabilities (KEV) catalog** lists CVEs with confirmed real-world exploitation: if a KEV entry affects you, patching jumps the queue regardless of raw CVSS.

### 3. Risk: where the four words combine

**Plain language.** Risk is the *size of the worry*: how likely, times how much it would hurt.

**Technical detail.** For teaching we use the qualitative form:

```text
                 risk  ≈  likelihood  ×  impact
```

Score each 1–5 on a **5×5 matrix** and multiply (or place them in the matrix cells directly):

| Score | Likelihood (within a year) | Impact (if it happens) |
|---|---|---|
| 1 | Rare — would need unusual coincidence | Minimal — annoyance, no real loss |
| 2 | Unlikely — possible but not expected | Minor — small cost, quick fix |
| 3 | Possible — has happened to similar systems | Moderate — money/time loss, recoverable |
| 4 | Likely — expected without action | Major — serious financial/reputational harm |
| 5 | Almost certain — actively exploited now | Severe — safety, legal, or existential harm |

Risk scores 1–25: treat **1–5 as low** (accept or monitor), **6–10 medium** (plan), **11–15 high** (act soon), **16–25 critical** (act now). These bands are a course convention — organizations set their own.

**Four treatments** for any identified risk:

| Treatment | Meaning | Example |
|---|---|---|
| **Mitigate** | Reduce likelihood or impact with controls | Firewall, MFA, backups |
| **Avoid** | Stop the activity causing the risk | Drop the legacy protocol nobody needs |
| **Transfer** | Share the financial consequence | Insurance, contracted provider SLAs |
| **Accept** | Consciously tolerate (documented!) | Cosmetic website defacement risk on a hobby blog |

**The central trap:** `CVSS 9.8 ≠ risk 9.8`. CVSS measures the *technical severity of a vulnerability class*; your risk also depends on *exposure* (is the affected thing reachable?), *asset value* (does anyone care?), and *existing controls*. An internet-facing unpatched web server with a KEV-listed CVE: high CVSS **and** high risk. The same CVE in an offline kiosk: high CVSS, low risk. Always compute both.

### 4. Controls: the taxonomy you will use all course

**Plain language.** A control is anything that reduces risk. Two useful classifications: *when* it acts, and *what kind* of thing it is.

**Technical detail.** Control types by function:

| Type | Acts | Examples |
|---|---|---|
| **Preventive** | Before harm occurs | Firewall rules, MFA, access control, security awareness training, encrypted backups |
| **Detective** | During/after — tells you it happened or is happening | IDS alerts, log monitoring, file-integrity checks, alarm systems |
| **Corrective** | After harm — limits damage and restores | Restore from backup, patch, revoke compromised credentials |
| *(Supporting: **deterrent** — discourages; **recovery** — restores; **compensating** — a substitute when the ideal control can't be used)* | | |

By nature: **technical** (software/hardware — encryption, antivirus), **administrative** (rules and people — policies, training, background checks), **physical** (the real world — locks, badges, cameras).

**Worked example — risk → controls across all three types.** Risk: *"Employee falls for a phishing email (likelihood 4) → mailbox and money at risk (impact 4) → risk 16, critical."* A balanced treatment:

- **Preventive/administrative:** security awareness training (quarterly).
- **Preventive/technical:** MFA on mail (blocks stolen passwords), SPF/DKIM/DMARC (fake-sender defense).
- **Detective/technical:** alert on logins from new countries/devices.
- **Corrective/administrative:** password + session revocation procedure; a call-back rule for payment changes.

One control never carries a critical risk — this is Module 01's defense in depth, now with priorities attached.

### 5. Control collections: CSF 2.0 and CIS Controls

You don't invent controls from scratch. Two free frameworks structure the menu:

- **NIST CSF 2.0** (verified Feb 2024): the six Functions from M01 — *Govern, Identify, Protect, Detect, Respond, Recover* — as outcome statements, good for organizing a program.
- **CIS Controls v8.1** (June 2024): **18 prioritized safeguards** with three **Implementation Groups** — *IG1* (essential cyber hygiene, smallest effort), *IG2* (multi-user networks with IT assets), *IG3* (full set, sensitive/high-value environments). Start at IG1; grow into IG2/IG3. This course's labs build toward IG1-style hygiene.

---

## Worked Example: A Home Risk Register, Row by Row

**Scenario.** Amira lives in a shared flat; the household Wi-Fi router, four laptops, and a family bank app are in scope. One full row, as you would write it:

| # | Risk description | Threat | Vulnerability | L (1–5) | I (1–5) | Score | Treatment | Control(s) chosen | Residual |
|---|---|---|---|---|---|---|---|---|---|
| R3 | Attacker joins flat's Wi-Fi and reads unencrypted traffic | Guest in flat / visitor | Wi-Fi password shared with 15 people; some devices HTTP-only | 3 | 3 | **9 (high)** | Mitigate | Change PSK quarterly; guests on separate network/PSK; prefer HTTPS sites | Medium — guests still risky |

Read what each column contributes: without *threat* and *vulnerability* columns the row is vague ("Wi-Fi risk" helps no one); without *residual risk* you pretend the control ended the story. R3 scores 9 → high → schedule this month, not "someday."

Then rank: her rows might come out **R7 router default admin password (4×5=20)**, **R1 no backup of thesis folder (3×5=15)**, **R3 (9)**, **R5 phone no screen lock (3×3=9)**… and now she knows the *order of work* — which is the entire point.

---

## Step-by-Step Procedures

### Procedure A — Build a risk register (10 rows)

1. **Scope:** write one sentence: what's in (flat's devices/accounts) and what's out (landlord's CCTV). Scope creep kills registers.
2. **Enumerate risks:** brainstorm 15+ candidate rows, each phrased as *"Event → affected asset"*, with a distinct threat and vulnerability column.
3. **Score likelihood** 1–5 using evidence, not vibes (check KEV/exploitation status for tech causes; count "how many people can do this?" for access causes).
4. **Score impact** 1–5 through the CIA lens from M01 (worst realistic single event, not apocalypse).
5. **Multiply** and place into bands (1–5 low / 6–10 medium / 11–15 high / 16–25 critical).
6. **Choose a treatment** per row (mitigate/avoid/transfer/accept) — acceptance must be written down.
7. **Select controls:** ≥ 1 preventive for high/critical rows; add detective where impact is high.
8. **Record residual risk** after controls — honestly.
9. **Sort** the register by score; this is your work order.
10. **Review:** set a diary date (home: every 6 months; business: quarterly or after any incident).

### Procedure B — Analyze one CVE (fill your CVE sheet)

1. Open <https://nvd.nist.gov> → search the CVE ID given in your module exercise (or any KEV entry: <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>).
2. Record: product + versions affected; attack vector (network/adjacent/local/physical); what the flaw allows (confidentiality/integrity/availability impact ratings in the CVSS vector).
3. Read the **CVSS v4.0 base score** and band; note if NVD also shows v3.1 (older but still common) — always cite the version you used.
4. Check **CISA KEV**: listed? If yes, note the remediation due date policy (US federal due dates; copy the discipline, not the jurisdiction).
5. Find the **fix**: vendor advisory → fixed version → your exposure (do you run this product? is it reachable?).
6. Write one line of risk in register format: *threat, vulnerability, L, I, score, treatment.*

---

## Common Mistakes, Misconceptions, and Troubleshooting

| Mistake / misconception | Why it is wrong | Correction |
|---|---|---|
| "CVSS is our risk score" | CVSS ignores exposure, asset value, and your controls | Keep CVSS in the CVE sheet; compute L×I separately |
| "Fix = patch, end of story" | Many risks have no patch (physique: insider risk, phishing) — and some patched systems stay risky (unrebooted, unverified) | Mix controls (table in §4); always verify |
| "Risk can be eliminated" | Risk can only be *managed*; new tech brings new risk | Always record **residual risk** |
| Scoring everything 4–5 | No priority = no decision | Calibrate: 5 = active exploitation / severe harm; most things are 2–3 |
| Listing "hackers" as the threat | Too vague to design any control | Name actor tier + motivation (§1 table) |
| Forgetting *exposure* | An unreachable vulnerability and a public one are worlds apart | Ask: "can a threat actually reach it?" before scoring |
| Accepting risks silently | Un-recorded acceptance becomes an incident surprise later | Acceptance rows need owner + review date |
| Control shopping before risk analysis | Tools without a row to justify them don't get maintained | Register first, tool list second |

**Troubleshooting:** *register scores all look the same* → your impact column probably measures effort, not harm; redo impacts through CIA (M01 §6). *Can't decide likelihood* → look for evidence: KEV listing, "exploitation observed," vendor "exploited in the wild" notes push you to 4–5; pure theoretical with no public exploit sits at 1–2.

---

## Lab 2 — Risk Register and CVE Analysis

*Paperwork-only lab: no scanning, no target systems. Overview and portfolio rules: [Lab Collection](../../labs/README.md).*

**Dedicated lab worksheet:** [LAB-02 — Threat Modeling and Risk Register Preparation](../../labs/lab-02-threat-model-risk-register/README.md) · [Full lab collection](../../labs/README.md).

**Objective:** a 10-row personal risk register + one full CVE analysis sheet.

**Steps:**

1. Create `portfolio/M02/`.
2. Scope a system you actually own (home network, laptop + accounts, student project server).
3. Build the register using **Procedure A** (10 rows minimum, all columns filled, sorted by score).
4. Choose one KEV-listed CVE (any) and complete **Procedure B** → `cve-analysis.md`.
5. Write a 5-sentence justification for your #1 row: why that treatment, why those controls, what residual risk remains.
6. Safety statement: targets used = *none (documentation exercise)*; isolation = *not applicable*.

**Completion check:** 10 scored/sorted rows; CVE sheet with CVSS version noted; KEV consulted; top-row justification present.

---

## Knowledge Check

*Formative — self-graded; retake until ≥ 80% (10 of 12). Attempt all answers before opening the key.*

**Extend your practice:** [Module 02 quiz — more questions, worked answers, and outcome mapping](../../assessments/level-1/quiz-m02.md) · module-end review exercises are on the same page · [Assessment Hub](../../assessments/README.md)

**Multiple choice (8):**

1. Which statement best separates exposure from vulnerability?
   - (a) They are synonyms  (b) Exposure is being reachable by a threat that can use the weakness; vulnerability is the weakness itself  (c) Exposure only applies to servers  (d) Vulnerability only applies to people
2. A vulnerability has CVSS 9.8 but sits on an offline kiosk with no network path. Your risk is:
   - (a) Automatically critical  (b) Determined by multiplying 9.8 × 5  (c) Lower than the CVSS suggests, because exposure is minimal  (d) Unknowable
3. Which is a **corrective** control?
   - (a) MFA  (b) Firewall  (c) Restoring files from backup after ransomware  (d) Security awareness training
4. What makes a KEV-listed CVE special?
   - (a) It has the highest CVSS possible  (b) It is confirmed exploited in real attacks  (c) It is unpatchable  (d) It only affects old software
5. "Risk = likelihood × impact" in this course produces a score whose bands treat 16–25 as:
   - (a) Low  (b) Medium  (c) High  (d) Critical
6. Which row is written correctly (event → asset, distinct threat and vulnerability)?
   - (a) "Wi-Fi risk"  (b) "Hackers attack my laptop"  (c) "Visitor in flat joins Wi-Fi (threat) and reads thesis in HTTP traffic (vulnerability) → thesis confidentiality"  (d) "Buy a firewall"
7. An insider abusing legitimate access scores high likelihood mainly because:
   - (a) They are unskilled  (b) They need no exploitation — access is already granted  (c) Insiders never get caught  (d) Their tools are expensive
8. Which control collection is prioritized into Implementation Groups IG1–IG3?
   - (a) NIST CSF 2.0  (b) CIS Controls v8.1  (c) CVSS v4.0  (d) CVE

**Short answer (4):**

9. Explain in 2–3 sentences why an unpatched vulnerability on a public web server is a *higher* risk than the same one on an isolated lab VM — using the words threat, exposure, and asset value.
10. Give one example each of preventive, detective, and corrective controls against phishing, using all three control *natures* (technical/administrative/physical — one per type).
11. Your risk register shows score 18 (critical) for "no backup of coursework." Which treatment(s) would you choose and why is "accept" a poor option?
12. Describe the patch gap and why it is a process failure rather than a zero-day problem.

<details>
<summary><b>Answer key</b> — attempt the questions first</summary>

1. **(b)** — the weakness may be unreachable; exposure is reachability by a capable threat.
2. **(c)** — CVSS is technical severity, not your risk; low exposure and low asset value drop L and I.
3. **(c)** — restoration after harm; MFA/firewall are preventive, training is administrative preventive.
4. **(b)** — confirmed real-world exploitation; KEV presence raises likelihood regardless of raw CVSS.
5. **(d) Critical** (16–25); 11–15 high, 6–10 medium, 1–5 low.
6. **(c)** — names cause, weakness, and affected pillar/asset; others are vague or solutions-first.
7. **(b)** — authorized access removes the need to defeat any technical control.
8. **(b)** — CIS v8.1's 18 safeguards with IG1/IG2/IG3 tiers.
9. *Model:* the public server is exposed to remote threats with little effort, and its availability/integrity affect real users and revenue (high asset value); the lab VM has no reachable threat path and near-zero asset value — same vulnerability, far lower likelihood and impact.
10. *Example set:* preventive technical = spam filter; preventive administrative = payment call-back rule; detective technical = alert on look-alike-domain email; corrective administrative = revoke sessions + reset password drill; physical (stretch) = printed phishing-report card by each desk (a physical reminder enforcing process). Full credit for any 3 with natures correctly assigned.
11. Mitigate: automated backups to two media + one offsite (3-2-1), verified by restore test. Accept is poor because impact is high (a whole semester lost) and likelihood of disk failure/user error over a year is non-trivial — accepting would risk an unrecoverable loss.
12. The patch gap is the delay between a fix being available and being installed. During it, defenders are not fighting an unknown "zero-day" — they are choosing (through absent process/priority/ownership) not to apply a known fix while exploits appear; most mass compromises exploit this gap.

</details>

## Scenario Exercises (Practice)

*Practice — graded checkpoint S1 arrives after Module 03. Answer in 100–200 words or a table.*

1. **Score and treat.** Three risks for a small photo studio: (i) no backup of client photos; (ii) designer's laptop has no screen lock in a shared co-working space; (iii) website runs an outdated plugin with a known exploit. Score each (L×I), band it, and choose a treatment + one control per row. Which do you do first, and why?
2. **CVSS vs. risk argument.** A tool vendor emails: "Our product flaw is only CVSS 5.5 — medium — so your risk is low." Using this module's vocabulary, write your reply (what CVSS measures, what your risk also needs, what information you require).
3. **Actor analysis.** A university library portal is being credential-stuffed (automated login attempts using leaked username/password lists from other breaches). Identify the actor tier, motivation, the vulnerability being exploited, and one preventive + one detective control.

## Key Takeaways

1. **Threat actors differ by motivation and capability** — match defenses to realistic actors, and don't forget negligent insiders and non-human threats.
2. **Vulnerability ≠ exposure ≠ risk:** weakness, reachability, and expected loss are three separate questions.
3. **Risk ≈ likelihood × impact** on a 5×5 matrix (course bands: 16–25 critical → act now; 1–5 low → accept/monitor).
4. **CVSS measures technical severity; risk includes exposure, asset value, and existing controls.** Always keep the two apart.
5. The **vulnerability lifecycle** shows why the patch gap — a process failure — is where most mass compromises happen; **CISA KEV** tells you what's actually being exploited.
6. Controls are classified by **function** (preventive/detective/corrective) and **nature** (technical/administrative/physical); critical risks need several, across types.
7. **CIS Controls v8.1 IG1** is the practical checklist of essential hygiene; CSF 2.0 organizes the program around it.
8. A **risk register** — scoped, scored, sorted, with treatments and residual risk — is your ongoing decision document, reviewed on a schedule.

## Self-Assessment Checklist

- [ ] I can name at least five threat-actor tiers with their motivations and typical capability.
- [ ] I can explain threat, vulnerability, exposure, likelihood, and impact without notes, each with an example.
- [ ] I can read a CVE/NVD entry: product affected, CVSS v4.0 score and band, KEV status.
- [ ] I built a 10-row risk register with all columns, scored and sorted, with treatments and residual risk.
- [ ] I can explain why CVSS ≠ risk with a concrete counter-example.
- [ ] I can classify any control as preventive/detective/corrective **and** technical/administrative/physical.
- [ ] I can describe the vulnerability lifecycle and the patch gap, and why KEV matters.
- [ ] I scored ≥ 80% on the knowledge check and completed the CVE analysis sheet.

*If three or more boxes are unchecked, redo Procedures A and B before Module 03.*

## Further Reading

Verified editions as of 2026-10-09.

- **CVSS v4.0 specification** — FIRST.org: <https://www.first.org/cvss/specification-document> (v4.0, released 1 November 2023; current).
- **CISA Known Exploited Vulnerabilities catalog** — the "what's actually being exploited" list: <https://www.cisa.gov/known-exploited-vulnerabilities-catalog>.
- **NIST SP 800-30 Rev. 1, *Guide for Conducting Risk Assessments*** (2012) — the formal method behind simplified 5×5 practice: <https://csrc.nist.gov/pubs/sp/800/30/r1/final>.
- **NVD (National Vulnerability Database)** — CVE records and CVSS vectors: <https://nvd.nist.gov>.
- **CIS Critical Security Controls v8.1** (June 2024) — free download with Implementation Groups: <https://www.cisecurity.org/controls/v8-1>.
- **NIST CSF 2.0** (Feb 2024) — the six Functions used to organize control choices: <https://csrc.nist.gov/pubs/cswp/29/the-nist-cybersecurity-framework-csf-20/final>.

---

**Navigation:** [← Previous: Module 01](../module-01-information-security-foundations/README.md) · [Module index](../README.md) · [Next: Module 03 →](../module-03-governance-policy-ethics-and-law/README.md) · [Lab Safety Policy](../../lab-safety-policy.md) · [Reference Library](../../reference/README.md)
