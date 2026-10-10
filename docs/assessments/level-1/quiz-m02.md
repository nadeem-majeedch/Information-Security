---
title: "Module 02 Quiz — Threats, Vulnerabilities, Risk, and Controls"
layout: default
---

# Module 02 Quiz — Threats, Vulnerabilities, Risk, and Controls

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 scenario-based short answer) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Short answers should be 2–5 sentences and, where a risk is scored, show the likelihood × impact reasoning.

**Coverage.** Maps to Module 02 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m02--threats-vulnerabilities-risk-and-controls)).

**Related:** [Module 02 lesson](../../modules/module-02-threats-vulnerabilities-risk-and-controls/README.md) · [LAB-02](../../labs/lab-02-threat-model-risk-register/README.md) · [CS-1 case study](../case-studies/cs-1-breach-at-meridian.md)

---

## Part A — Multiple choice (8)

**Q1.** Which threat actor is typically motivated by ideology and attention rather than money, and often has modest technical capability?

- (a) Nation-state
- (b) Hacktivist
- (c) Organized crime
- (d) Insider

**Q2.** The **vulnerability lifecycle** proceeds in which order?

- (a) Patch → discovery → disclosure → exploitation
- (b) Discovery → disclosure → patch → exploitation
- (c) Discovery → disclosure → (unpatched window) → exploitation; patching reduces the window
- (d) Exploitation → discovery → disclosure → patch

**Q3.** A CVE identifier is best described as:

- (a) A fix for a vulnerability
- (b) A unique identifier for a *known* vulnerability in specific software
- (c) A guarantee that a system is safe once assigned
- (d) An attacker's handle

**Q4.** CVSS measures which of the following?

- (a) How urgently you must patch *your* system
- (b) The technical severity of a vulnerability, independent of your business context
- (c) Whether a vulnerability has been exploited in the wild
- (d) The financial loss from an incident

**Q5.** Which is a **corrective** control?

- (a) A firewall rule blocking a port
- (b) Restoring from backup after ransomware encrypts files
- (c) A security-awareness poster
- (d) A badge reader on the server-room door

**Q6.** Which control *type* (by nature) is a security policy document?

- (a) Technical
- (b) Administrative
- (c) Physical
- (d) Detective

**Q7.** "Risk = likelihood × impact" — if a rare event would be catastrophic, the risk is:

- (a) Low, because it is rare
- (b) Not zero; a high impact can keep risk elevated despite low likelihood
- (c) Irrelevant until it happens
- (d) Undefined, because likelihood is a guess

**Q8.** Which risk treatment means you deliberately do nothing and formally record the decision?

- (a) Mitigate
- (b) Transfer
- (c) Accept
- (d) Avoid

## Part B — Scenario-based short answer (4)

**Q9.** A scanner flags an old library on an internal file server that no one can reach from the internet. State whether this is a *vulnerability* or a *risk*, and explain what additional information you need to decide the risk level.

**Q10.** A small shop's Wi-Fi router has a default admin password and sits on the same network as the card terminal. Score this risk on a 5×5 matrix (likelihood × impact) with one line of justification, then name the single most important control and its treatment type.

**Q11.** Classify each as **preventive**, **detective**, or **corrective**: (a) endpoint detection and response raising an alert, (b) disabling a user account after someone leaves, (c) full-disk encryption.

**Q12.** An attacker with no resources finds a public bug bounty page and copies a public exploit. Which capability tier and which *motivation* best fit, and how does that change the controls you would prioritize versus a nation-state?

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b) Hacktivist.** Ideology/attention-driven, often moderate capability, publicly visible activity. *Misconception:* (d) an insider already has access and is usually personally or financially motivated, not attention-driven; (a) nation-states are resourced and *stealthy* — publicity is the wrong tell; (c) organized crime is financial.

**Q2 — (c).** Discovery → disclosure → (unpatched window) → exploitation; patching *shortens* the window but cannot remove the earlier phases. *Misconception:* (b) is the seductive near-miss — it puts *patch* before *exploitation*, implying you are always patched before anyone tries; (a) and (d) reverse causality entirely (you cannot patch before discovery; exploitation does not wait for disclosure).

**Q3 — (b).** A CVE is a unique *identifier* — a name — not a fix, not a safety guarantee; assignment means the weakness exists and is catalogued. *Misconception:* (a) confuses *naming* with *fixing*; (c) mistakes a catalogue entry for a certification that the system is safe.

**Q4 — (b).** CVSS reports *technical severity*, independent of your business context; turning severity into *your* priority requires business context — exactly the M02 “CVSS vs. risk” lesson. *Misconception:* (a) is what you *do with* CVSS, not what it measures; (c) is threat-intelligence/exploitation-in-the-wild data, not CVSS; (d) belongs to business-impact analysis.

**Q5 — (b).** Restoring from backup acts *after* harm to return to normal — corrective. *Misconception:* (a) firewall rule and (d) badge reader block the event *before* it happens — preventive; (c) poster is administrative/awareness. The tell: a corrective control only matters once the harm has occurred.

**Q6 — (b) Administrative.** A policy document is a rule/process control. *Misconception:* (d) *detective* comes from a different axis — what a control **does** (prevent/detect/correct) — while the question asks what it **is** by nature: technical, administrative, or physical.

**Q7 — (b).** Low likelihood does not cancel catastrophic impact; risk can stay elevated — why “rare but existential” events still justify controls, and why insurance exists. *Misconception:* (a) applies the intuition “rare = safe” — one high factor cannot zero the other; (d) treats an estimate as grounds to ignore risk, when judgment-based estimates are exactly what a 5×5 matrix encodes.

**Q8 — (c) Accept.** A conscious, recorded decision to bear the risk as-is. *Misconception:* (a) *mitigate* changes likelihood/impact — it does something; (d) *avoid* ends the activity entirely; (b) *transfer* shifts financial consequence (insurance) — “deliberately do nothing but record it” is uniquely **accept**.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** It is a **vulnerability** as reported. To decide *risk* you need: can any threat actually reach it (is the server truly isolated, or reachable by insiders/lateral movement)? What is the data's confidentiality impact? Is a known exploit applicable, and has it been seen in the wild (KEV)? Only when reachability *and* impact combine does it become risk. → [Lesson: CVSS vs. risk](../../modules/module-02-threats-vulnerabilities-risk-and-controls/README.md)

**Q10.** *Likelihood* high (default password is trivially guessable and publicly documented); *impact* high (card-terminal data). 5×5 → **High/Extreme** (e.g., likelihood 4 × impact 5). Most important control: change the default admin credential and put the card terminal on a **separate segmented network** (preventive, technical). Treatment = **mitigate**. → [Risk matrix + controls](../../modules/module-02-threats-vulnerabilities-risk-and-controls/README.md)

**Q11.** (a) EDR alert = **detective** (it notices harm in progress). (b) Disabling a leaver's account = **preventive** (stops future unauthorized use). (c) Full-disk encryption = **preventive** (stops offline data reading if the device is lost). Note: the *recovery* after encryption failure would be corrective — type depends on when the control acts.

**Q12.** Tier = low capability (script-kiddie / opportunistic); motivation = notoriety or curiosity, not money. Controls shift *away* from nation-state-grade defenses (advanced persistent threat detection, air-gapping) toward fundamentals: patch the known CVE quickly, close the public exposure, and monitor for the *public* exploit's signatures — because the attack is commodity and loud, not stealthy and bespoke.

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Risk register build.** Produce a 6-row risk register for your home network (router, IoT, laptop, cloud accounts). Columns: asset, threat, vulnerability, likelihood, impact, score, treatment, single most important control. Sort by score descending.
2. **CVE walk-through.** Pick one recent CVE from the NVD. Document: the vector, the CVSS v4.0 base score, affected software versions, whether it is in the CISA KEV catalog, and the concrete patch/mitigation path.
3. **Actor profile.** Write a one-page profile of a threat actor targeting a small business. Map their three most likely attack vectors to specific controls (name the control *type* for each).
4. **Severity vs. risk.** Find a CVE with a high CVSS score that would be *low* risk for your isolated home lab, and one with a moderate score that would be *high* risk for a small business. Explain the context that flips each.

*Review guidance:* 2 and 4 reinforce that CVSS is severity, not your priority. 3 forces the preventive/detective/corrective and technical/administrative/physical vocabulary to be used precisely. If your register has no *treatment* column filled, revisit the accept/avoid/mitigate/transfer definitions.

**Next:** [Module 03 quiz](./quiz-m03.md) · [Previous: M01](./quiz-m01.md) · [Assessment Hub](../README.md)
