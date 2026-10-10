---
title: "Case Study CS-1 — Breach at Meridian Labs (Level 1)"
layout: default
---

# Case Study CS-1 — Breach at Meridian Labs (Level 1)

**Type:** Cross-module case study (integrative, scenario-based) · **Spans:** Modules 01–05 · **Level:** 1 · **Estimated time:** 60–90 minutes · **Graded weight:** checkpoint (see [Assessment Guide §5.2](../../assessment-guide.md#52-scenario-exercise-rubric-component-b-per-scenario-20-points))

This case study deliberately fuses the whole of Level 1 — triad vocabulary (M01), risk and controls (M02), governance and authorization (M03), networking (M04), and endpoint security (M05) — into one realistic small-organization breach. Work it **after** finishing M05.

**Instructions.** Read the scenario, then answer all six questions in your own words before revealing the model answers. Questions 5 and 6 require you to make a *decision* and justify it, not recall a fact. Self-assess against the published rubric at the end.

**Related lessons:** [M01](../../modules/module-01-information-security-foundations/README.md) · [M02](../../modules/module-02-threats-vulnerabilities-risk-and-controls/README.md) · [M03](../../modules/module-03-governance-policy-ethics-and-law/README.md) · [M04](../../modules/module-04-networking-fundamentals-for-security/README.md) · [M05](../../modules/module-05-operating-system-and-endpoint-security/README.md)

---

## The scenario

**Meridian Labs** is a 12-person research consultancy. Each researcher has a Linux workstation; the firm runs one shared project server (`web01`, internal IP `192.168.56.20`) that hosts a small client-upload web page and stores client deliverables. The office router doubles as the firewall. There is no dedicated IT staff — an "IT lead" role is split between two researchers.

On **10 October** you are asked to review a bad night. The facts you are given:

1. **03:14–03:19** — A burst of ~45 failed password attempts hits `web01` from `192.168.56.105`, trying usernames including `admin`, `dbadmin`, `oracle`, `postgres`, and — repeatedly — the service account `svc_backup`.
2. **03:19:47** — A single **successful** password login for `svc_backup` from the *same* source `192.168.56.105`.
3. Shortly after, `svc_backup` uses `sudo` to run `/bin/cat /etc/shadow`.
4. **Later that week** — two client deliverable folders are found altered, and one month of prior work is missing from the server. There are no independent backups.
5. When asked, IT confirms the office router still uses its **default admin password**, and the internal upload page has **no login** — anyone on the office Wi-Fi can upload to it.
6. The `web01` firewall was logging blocked external scans all week, but nobody was watching the logs.

You own this review. Everything here is a **fictional** firm on the reserved `192.168.56.x` lab range — you are *not* scanning or touching any real system.

---

## Questions

**Q1 — CIA triad (M01).** For the altered and missing deliverable folders, state which CIA pillar(s) failed for each and why. Distinguish the *alteration* from the *loss*.

**Q2 — Vocabulary (M01/M02).** From facts 1 and 5, identify one **threat**, one **vulnerability**, the **risk**, and one **control** (present *or* missing). Use the four terms precisely.

**Q3 — Risk scoring (M02).** Score the default-router-password risk on a 5×5 likelihood × impact matrix with one line of justification, and name whether you would accept, avoid, mitigate, or transfer it — and why.

**Q4 — Root cause (M04/M05).** The brute force succeeded because `svc_backup` had a guessable password *and* could elevate via `sudo`. Explain what two endpoint/identity weaknesses this reveals (M05), and why the firewall's ignored logs (fact 6) represent a *detection* failure rather than a *prevention* failure.

**Q5 — Decision (M02/M03).** You have budget for **three** controls before anything else. Choose them, justify each against a specific fact, and classify each as preventive/detective/corrective. (There is no single right answer — you are graded on reasoning.)

**Q6 — Governance/authorization (M03).** Before you investigate `web01` any further, what written authorization and scope do you need? State what you may examine, what you must not, and how you would handle any real client data you encounter.

---

## Model answers

<details>
<summary><b>Q1 — CIA triad</b></summary>

The **alteration** of deliverables is a primary **integrity** failure — data changed by an unauthorized process, and it went undetected (integrity includes *detecting* unauthorized change). The **loss** of a month's work is an **availability** failure — authorized users can no longer get what they need, because the only copy was destroyed with no independent backup. Confidentiality is a *side question* here: ask whether the attacker also *read* the files (the `cat /etc/shadow` and staging actions in fact 3 suggest the box was fully compromised, so treat disclosure as likely until ruled out). One control per pillar: version history/change alerts (integrity detection), tested 3-2-1 offsite backups (availability recovery), and access control plus encryption (confidentiality). → [M01 §2](../../modules/module-01-information-security-foundations/README.md)

</details>

<details>
<summary><b>Q2 — Threat / vulnerability / risk / control</b></summary>

- **Threat:** the actor behind `192.168.56.105` conducting password brute force (and, by extension, any insider on the office Wi-Fi).
- **Vulnerability:** the default router admin password (fact 5) *and* the weak, guessable `svc_backup` password that could `sudo` (facts 1, 5) — plus the no-login upload page.
- **Risk:** that a reachable threat exploits these weaknesses to gain privileged access to `web01`, leading to alteration, theft, or destruction of client data — and the impact matters (client trust, contracts, legal).
- **Control (missing):** unique service-account credentials with MFA/least privilege, and active monitoring of the firewall/auth logs (fact 6). A present-but-weak "control" is the firewall itself — it *logged* the activity, so it partly worked as detective; the failure was that nobody watched it.

Precision check: the scanner-style fact (default password) is a *vulnerability*; only when you add a reachable threat *and* meaningful impact does it become *risk*.

</details>

<details>
<summary><b>Q3 — Risk scoring</b></summary>

Default router admin password, reachable from inside the office Wi-Fi. **Likelihood: 4/5** — trivially guessable, publicly documented default, and the attacker is already on the LAN. **Impact: 5/5** — the router is the perimeter for a server holding client data; control of it means full network exposure. **Score ≈ Extreme (High).** Treatment: **mitigate** — you cannot avoid (the firm needs the router) and transferring (insurance) does not fix the exposure. Mitigation: change the default credential, segment the client-upload/server VLAN from staff Wi-Fi, and enable administrative-access logging. Justification line: *rare-but-catastrophic is not the issue here — this is likely AND catastrophic, so it is your top priority.*

</details>

<details>
<summary><b>Q4 — Root cause and detection vs prevention</b></summary>

Two endpoint/identity weaknesses (M05): (1) **weak/credential reuse on a privileged service account** — `svc_backup` had a password that survived a short brute force, violating least-privilege credential hygiene; (2) **over-broad `sudo`** — a backup service account that can run arbitrary commands (`cat /etc/shadow`) as root means one compromised credential becomes full root. The fix is a random, vaulted service credential plus a `sudoers` entry restricted to only the backup command.

The firewall logs (fact 6) are a **detection** gap, not prevention: the firewall *did* block external scans — prevention worked — but nobody reviewed the logs, so there was no alerting/triage. Prevention stops the event; detection notices it when prevention is bypassed. Here detection was the layer that failed, which is why the brute force ran for five minutes unnoticed. → [M05](../../modules/module-05-operating-system-and-endpoint-security/README.md) · [M04](../../modules/module-04-networking-fundamentals-for-security/README.md)

</details>

<details>
<summary><b>Q5 — Decision (graded on reasoning)</b></summary>

A strong answer picks three *distinct* control types tied to specific facts, e.g.:

1. **Reset the router admin password + segment the network** (preventive/technical) — directly closes fact 5, the most reachable root cause.
2. **Vault a random `svc_backup` credential and restrict its `sudoers` to the backup command; disable password auth for service accounts** (preventive/technical) — closes the exact path that succeeded in facts 1–3.
3. **Stand up active log review / alerting on auth + firewall logs** (detective/process) — fixes fact 6 so the next brute force pages someone.

Justify *why these three*: they map to the confirmed compromise path (2), the easiest reachable weakness (1), and the failure that let it run undetected (6). Alternate valid sets include tested offsite backups (corrective) or MFA on admin access — what matters is that each is tied to a fact and correctly typed. An answer that lists three preventive technical tools with no detective or corrective control, or that ignores the `sudo` escalation, is weaker.

</details>

<details>
<summary><b>Q6 — Governance / authorization (M03)</b></summary>

Before touching `web01` further you need **written authorization** from the accountable owner (the client's or Meridian's designated authority), defining **scope**: which host(s) (`web01` only, or named IPs), which actions (log review, config audit — *not* exploitation), the time window, and explicit exclusions (no testing of live client data, no scanning beyond named hosts). You must **not** exceed that scope — e.g., do not reuse the found credentials to "see what else you can reach," and do not scan other firms on a shared network. Any real client data you encounter must be **minimized** (do not copy it), **protected** (encrypt any evidence), and **reported, not exfiltrated**. Record that you are authorized, that scope is confirmed in writing, and stop and re-confirm if new targets appear mid-investigation. → [M03](../../modules/module-03-governance-policy-ethics-and-law/README.md) · [Lab Safety Policy](../../lab-safety-policy.md)

</details>

---

## Rubric (self-assess)

| Criterion | Max | What a full-credit answer does |
|---|---|---|
| Technical accuracy | 8 | Correct pillar, terms, scoring, and root cause |
| Justification quality | 6 | Decisions tied to specific facts, reasoning shown |
| Safety / ethics reasoning | 4 | Explicit authorization, scope, and data handling (Q6) |
| Clarity and structure | 2 | Organised, unambiguous |
| **Pass = ≥ 12/20** | | |

**Completion check:** all six questions answered with reasoning (not just labels); Q5 picks three *typed* controls tied to facts; Q6 names written authorization + scope + data handling.

**Next:** [Level 2 quizzes](../level-2/quiz-m06.md) · [Assessment Hub](../README.md)
