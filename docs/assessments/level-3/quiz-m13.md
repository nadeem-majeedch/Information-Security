---
title: "Module 13 Quiz — Logging, Monitoring, and Security Operations"
layout: default
---

# Module 13 Quiz — Logging, Monitoring, and Security Operations

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 triage scenarios) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Triage scenarios: give **verdict (TP/FP), severity, and next action** for every alert — all three are required for full credit.

**Coverage.** Maps to Module 13 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m13--logging-monitoring-and-security-operations)): log pipeline decisions, detection rules mapped to ATT&CK, alert triage, SOC/alert-lifecycle concepts.

**Related:** [Module 13 lesson](../../modules/module-13-logging-monitoring-and-security-operations/README.md) · [LAB-13 log analysis](../../labs/lab-13-log-analysis/README.md) · [LAB-12 scan interpretation](../../labs/lab-12-vuln-scan-interpretation/README.md) · [CS-3 case study](../case-studies/cs-3-detection-to-response.md)

> **Safety reminder:** trigger detections only against lab hosts you own, inside your RoE window. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** The alert lifecycle in order is:

- (a) Triage → collect → respond → detect
- (b) Collect → correlate → detect → triage → respond
- (c) Detect → collect → correlate → respond
- (d) Respond → detect → collect → triage

**Q2.** What should a security log record for an authentication event at minimum?

- (a) Only the timestamp
- (b) Who, what, when, source, and outcome (success/failure) — enough to reconstruct and attribute the action
- (c) The user's password, for replay value
- (d) Nothing; logs fill disks

**Q3.** **MTTD** and **MTTR** measure:

- (a) Memory throughput and transfer rates
- (b) Mean time to detect and mean time to respond/resolve — the two core SOC health metrics
- (c) Machine type and target rate
- (d) Only matter for large SOCs

**Q4.** A detection rule that fires on "≥ 5 failed logins in 2 minutes" and *also* fires whenever the org's own monitoring host restarts with a scripted login check is:

- (a) A perfect rule
- (b) Tuned incorrectly — its own infrastructure creates false positives; exclude known service accounts/sources
- (c) Proof that all rules are useless
- (d) A signature-free rule

**Q5.** Which is the best reason to map detections to **MITRE ATT&CK** techniques?

- (a) It makes reports longer
- (b) It links alerts to known adversary behaviors, exposing coverage *gaps* (which tactics you can't see) rather than just listing alerts
- (c) It is legally required for every rule
- (d) ATT&CK replaces the need for tuning

**Q6.** Log retention must balance:

- (a) Keep forever always, with no cost
- (b) Investigation needs (dwell time of attackers vs. retention window) against storage/privacy cost — retain long enough to detect and investigate, minimize what's sensitive
- (c) Delete everything after 24 hours
- (d) Retention only matters for compliance checkboxes

**Q7.** "Alert fatigue" in a SOC means:

- (a) Analysts need more caffeine
- (b) Too many low-value alerts desensitize analysts, so real incidents get missed — the core human-failure mode of monitoring
- (c) Alerts expire
- (d) Screens are too bright

**Q8.** A **Sigma** rule's advantage is:

- (a) It executes attacks
- (b) Vendor-neutral detection logic you can convert to Splunk/ELK/Sentinel queries — write once, deploy per backend
- (c) It encrypts logs
- (d) It replaces the SIEM

## Part B — Triage scenarios (4)

**Q9.** Alert: **"Repeated failed logins — 38 failures then 1 success for user `dbadmin` from `192.168.56.105` within 4 minutes."** Your asset list says `192.168.56.105` is a scanner you own, running inside the RoE window. Give verdict, severity, and next action — and say what single data source makes your verdict defensible.

**Q10.** Alert: **"New scheduled task created: `SysHelper` → runs `C:\Users\Public\upd.exe` at logon."** No change ticket exists. The host is a finance workstation. Give verdict, severity, next action, and the *next two artifacts* you'd collect (naming where each lives).

**Q11.** Alert: **"Outbound DNS query volume 40× baseline — domain `x9q-update[.]net`, newly registered."** The same host shows a software inventory entry installed this morning by the user. Verdict, severity, action — and is DNS allow-listing something you'd deploy here? Why/why not?

**Q12.** Alert: **"404 burst — 300× baseline 404s on `/api/users` from an internal office IP."** The team says "it's the new intern exploring the API." Verdict, severity, action — what evidence would you want *before* accepting the explanation, and which ATT&CK technique does 404-bursting map to if malicious?

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Collect → correlate → detect → triage → respond: data exists first, patterns emerge from correlation, a detection fires, a human/system judges it, then action. Misconceptions: (a)/(c)/(d) all put action before evidence or detection before collection.

**Q2 — (b).** 5 W's + outcome: enough to attribute (who), reconstruct (what/when/from where), and know success vs. failure (the difference between an attempt and a compromise). Misconceptions: (a) useless for attribution; (c) logging passwords is a credential leak (and usually prohibited); (d) rotation/retention solves disk, not silence.

**Q3 — (b).** MTTD/MTTR: how long threats hide and how long they live once seen — the metrics that justify monitoring investment. Misconceptions: (a) hardware metrics; (c) invented expansions; (d) they matter most exactly where incidents are frequent.

**Q4 — (b).** Tuning problem: known-internal sources (your monitoring scripts) must be baselined/excluded — otherwise noise trains analysts to ignore the alert. Misconception: (c) is alert-fatigue despair; (d) irrelevant.

**Q5 — (b).** ATT&CK maps detections to adversary tactics/techniques so you can answer "what can't we see?" — coverage-gap analysis, not alert vanity. Misconceptions: (a) brevity is the opposite; (c) no universal legal mandate; (d) mapping and tuning are complementary.

**Q6 — (b).** Retention ≥ max acceptable dwell time for your threat model, bounded by storage cost and privacy minimization (PII in logs has its own obligations — M17). Misconceptions: (a) unlimited retention is costly *and* a privacy liability; (c) 24h can't cover weekend detection; (d) compliance is one stakeholder, not the whole balance.

**Q7 — (b).** Chronic noise → desensitization → slow or missed real detections — tune for signal quality (precision), not raw alert count. Misconceptions: (a) joke answer; (c) no such mechanic; (d) ergonomics, not SOC design.

**Q8 — (b).** Sigma's YAML logic converts to backend queries (pySigma), avoiding vendor lock-in and enabling shared detection research. Misconceptions: (a) rules detect, not attack; (c) unrelated; (d) it needs a backend to run.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** **Verdict: true detection, expected-benign by context** (not a sensor fault). **Severity: informational** during the authorized window. **Action:** confirm the event falls inside the documented RoE window and the scanner's asset record, annotate the alert with "authorized testing — ref RoE," close, and ensure a suppression/baseline *scoped by asset + time window* (so an identical burst from an *unknown* source still fires). **Defensible data source:** the RoE document + asset inventory linking `192.168.56.105` to your scanner — without that written context your verdict is a guess. (Contrast with CS-1: same pattern, no RoE = incident.) → [LAB-13](../../labs/lab-13-log-analysis/README.md)

**Q10.** **Verdict: true positive (high confidence)** — unsigned persistence creation on a finance host with no change ticket. **Severity: high** (persistence = attacker intent to survive reboots; finance host = high-value target). **Action:** isolate/restrict the host (network containment per IR plan), preserve memory/disk before removal, identify how `upd.exe` arrived (user install vs. dropper), check `upd.exe` hash against your IOC list, escalate to IR (M14). **Next two artifacts:** (1) the file itself — `C:\Users\Public\upd.exe` — hash + signature + strings; (2) its persistence registration — `HKCU\Software\Microsoft\Windows\CurrentVersion\Run` (or Task Scheduler XML in `C:\Windows\System32\Tasks\`) plus the Prefetch entry (`C:\Windows\Prefetch\UPD.EXE-*.pf`) proving execution history. → [M15 lesson link via CS-3]

**Q11.** **Verdict: true positive until disproven** — 40× DNS volume to a newly registered domain is classic beaconing/DNS-exfil behavior (ATT&CK T1071.004 application-layer protocol / T1048 exfiltration). **Severity: high** until proven otherwise — "new software this morning" is a *correlated fact that raises suspicion*, not an alibi (users don't normally generate 40× DNS baselines). **Action:** identify process→domain mapping (DNS query logs + host process listing), check the installed software's vendor/reputation, block the domain at the resolver, capture a PCAP of the host's DNS, and if the domain is confirmed malicious, treat the host as compromised → IR. **DNS allow-listing?** For a *small* org with a known software inventory, egress allow-listing dramatically cuts beacon/C2 freedom — but plan it carefully: breaking DNS breaks everything, so start in monitor/log mode, baseline legitimate domains (updates, SaaS), then enforce. A deny-by-default DNS posture is high-value where the software footprint is stable; pure logging-first is the safer sequence. → [Module 13 lesson](../../modules/module-13-logging-monitoring-and-security-operations/README.md)

**Q12.** **Verdict: unconfirmed — investigate before accepting.** The intern story is plausible (benign-by-context), but "someone said so" is not evidence. **Severity: medium pending validation** (404 bursting is classic pre-exploitation enumeration). **Evidence to require:** (1) the *source* — does the internal IP match the intern's workstation (DHCP/asset record)? (2) the *shape* — real API exploration shows varied, slowing requests with referers/session; enumeration shows systematic wordlist progression (`/api/users/1`…`n`, common paths, high rate, no session); (3) *account* — was the intern authenticated, and does their project plausibly need it? (4) *outcome* — did any 404 cluster around auth-sensitive paths? **ATT&CK if malicious:** T1595.003 (active scanning: wordlist scanning) / T1110 (brute force) if credential-oriented; web-path enumeration maps to T1595 active scanning. **Action if confirmed benign:** document, baseline their IP, close; **if systematic:** treat as possible recon, contain the source host, and check the API for probing responses (no user enumeration via status codes).

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Log pipeline build (practical).** Tier (a) Wazuh/Elastic full stack, or Tier (b) `journalctl`/`auditd` + a scripted analyzer reporting failed logins and sudo events. Demonstrate retention/rotation settings and one query that answers "failed logins in the last 24h." Both tiers satisfy the requirement.
2. **Detection pack (configuration analysis).** Author 6 Sigma-style rules (repeated failed logins, new SUID binary, unusual outbound DNS, web 404 burst, sudo misuse, scheduled-task creation), map each to an ATT&CK technique ID, and **trigger each in the lab** with captured alert evidence.
3. **Risk prioritization.** You can only watch 3 of 10 log sources this quarter (auth, web, DNS, EDR, cloud audit, mail, VPN, DB, app, proxy). Choose 3, justify with threat model + data sensitivity, and state what risk you're consciously accepting by not watching the rest.
4. **Triage shift (investigation).** Process the 5 pre-generated alert cases in LAB-13: fill verdict/severity/action per alert, then write three sentences on which alert you escalated *first* and why — timing and asset value should drive the order.

*Programming spec — exercise 1 (analyzer script):*
- **Sample input:** the lab `auth.log` (or `journalctl` export), e.g. `Oct  9 03:14:02 web01 sshd[214]: Failed password for invalid user oracle from 192.168.56.105 port 51107 ssh2` and the later `... Accepted password for svc_backup from 192.168.56.105 ...`.
- **Expected behavior:** parse timestamp, source IP, user, result; group failures per IP in 10-minute windows; print one row per window; **exit 0** on success, **non-zero** if the log is unreadable/empty; never emit a partial row without a `DEGRADED` header.
- **Sample output:** `2026-10-09T03:14-03:19 | 192.168.56.105 | 45 failures -> 1 success | users: svc_backup, admin, dbadmin | FLAG: targeted-bruteforce`
- **Evaluation criteria:** counts match a hand-tally of the file; timezone stated in the header; one row per window; rotation demonstrated (logrotate config or `journalctl --disk-usage` before/after).

*Review guidance:* triage answers need **all three parts** (verdict, severity, action). A verdict without an action is an unfinished triage; an action without a verdict is a coin flip. Exercise 2's *trigger evidence* is required — a rule that was never fired is untested.

**Next:** [M14 quiz](./quiz-m14.md) · **Previous:** [M12 quiz](./quiz-m12.md) · **Hub:** [Assessment Hub](../README.md)
