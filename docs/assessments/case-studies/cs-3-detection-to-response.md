---
title: "Case Study CS-3 — From Detection to Response (Level 3)"
layout: default
---

# Case Study CS-3 — From Detection to Response (Level 3)

**Type:** Cross-module case study (integrative, scenario-based) · **Spans:** Modules 12–15 · **Level:** 3 · **Estimated time:** 90 minutes · **Graded weight:** checkpoint (see [Assessment Guide §5.2](../../assessment-guide.md#52-scenario-exercise-rubric-component-b-per-scenario-20-points))

This case study fuses Level 3 — authorized testing (M12), monitoring and triage (M13), incident response and forensics (M14), and malware analysis (M15) — into a single incident timeline. Work it **after** finishing M15.

**Instructions.** Read the scenario and answer all six questions before revealing the model answers. Questions 4–6 are *decisions* — justify each. Self-assess against the rubric at the end.

**Related lessons:** [M12](../../modules/module-12-vulnerability-assessment-and-security-testing/README.md) · [M13](../../modules/module-13-logging-monitoring-and-security-operations/README.md) · [M14](../../modules/module-14-incident-response-and-digital-forensics/README.md) · [M15](../../modules/module-15-malware-and-defensive-analysis/README.md)

---

## The scenario

**Harborview Dental** (14 staff, one IT contractor) runs a practice-management server and a public appointment-booking website. On a Tuesday you are engaged — under a **written RoE covering `10.10.40.0/24`, business hours only** — to finish an authorized vulnerability assessment started Monday.

Facts, in order:

1. **Mon 10:00–16:00** — Your authorized scan of the booking web server finds an outdated web framework with a known RCE (validated manually: version confirmed, safe probe only) and a missing security header. Ratings: RCE = critical (internet-facing); header = low.
2. **Mon 16:10** — The contractor asks you to "also quickly check" the practice-management server at `10.10.55.8` — outside your RoE subnet. You decline pending an amendment; the contractor says "just scan, it's our box."
3. **Tue 09:12** — Monitoring (M13 pipeline) alerts: *web server → outbound connection to a newly registered domain `appt-sync[.]cc` observed 04:40; DNS volume 25× baseline.*
4. **Tue 09:20** — A second alert: new scheduled task `WinSvchHelper` → `C:\ProgramData\appt\helper.exe` on the booking *web* server. The web server runs the practice's appointment sync tool.
5. **Tue 09:31** — Helpdesk reports an appointment confirmation email containing a patient's name sent **from the practice's own mailing system** at 04:52 to an address the patient doesn't recognize.
6. **Tue 10:05** — Forensic collection begins on the web server: memory dump, disk image (both hashed SHA-256), auth/web/DNS logs preserved. By noon, timeline correlation shows: framework RCE exploited at **04:38** (from a VPS in a country the practice has no business with), `helper.exe` written at 04:41, persistence at 04:42, outbound at 04:40–04:52.
7. Static triage of `helper.exe`: SHA-256 recorded; strings show an email-sending library and `patients_export.csv`; packed (high entropy); YARA (custom) matches. Dynamic analysis **in the isolated sandbox** shows: reads the appointment DB export, attempts SMTP to `mail.appt-sync[.]cc` (blocked in sandbox), writes the Run-key entry.
8. The Monday report had **not yet been delivered** when the incident began.

All hosts are fictional or course-provided lab systems; the timeline is synthetic and drawn from the course's training data.

---

## Questions

**Q1 — Scoping discipline (M12).** Evaluate fact 2: should you have scanned the practice-management server? What does your refusal protect — and what document change would let you proceed? Does fact 8 (undelivered report) change your obligations now?

**Q2 — Triage to incident (M13).** For facts 3–5: give verdict, severity, and next action per alert, and explain what *correlation* across the three converts them from alerts into a confirmed incident. Which ATT&CK techniques do the observations map to?

**Q3 — IR sequencing (M14).** Order the response actions for this incident and justify: (a) eradicate `helper.exe` + persistence, (b) notify patients/practice per plan, (c) isolate web server, (d) block C2 domain at DNS/proxy, (e) verify eradication, (f) restore framework-patched service, (g) scope: which other hosts/data affected (check email/DB access), (h) capture evidence. What must not happen first, and why?

**Q4 — Forensic reasoning (M14).** Fact 6's timeline is your evidence. State the *first-access* point and the attacker's actions in order, cite which artifact class proves each step, and name two things you'd still verify before stating root cause "with confidence."

**Q5 — Malware-to-defense (M15).** From fact 7: produce 4 IOCs (typed), 2 ATT&CK techniques, and 2 detections (1 Sigma for persistence, 1 YARA for the sample family). One line each on why your Sigma rule won't drown in false positives.

**Q6 — Lessons and roadmap (M12–M15).** Write the top 4 lessons-learned items with owners and due dates. One must fix the *assessment process* (report latency — fact 8), one the *detection coverage gap* (how did 04:38 exploitation precede the 09:12 alert?), one the *control* that would have reduced impact, and one the *authorization culture* issue from fact 2.

---

## Model answers

<details>
<summary><b>Q1 — Scoping discipline (M12)</b></summary>

**No — not without an amendment.** Your RoE covers `10.10.40.0/24` only; `10.10.55.8` is outside it. "It's our box" is *not* authorization: the contractor's assurance may not reflect the owner's actual consent (multi-tenant? third-party patient data? a different signatory?), and an informal OK creates no record. **What the refusal protects:** (1) your legal/ethical standing — authorized scope is the line between assessment and unauthorized access; (2) evidence integrity — findings outside scope can be thrown out and your report disowned; (3) the client — an unscoped scan of a clinical system could disrupt care systems and void insurance/contracts. **To proceed:** written RoE **amendment** (or short-form RoE) naming `10.10.55.8`, permitted actions (scan-only vs. validation), window, exclusions, and stop conditions — countersigned by the accountable owner, then scan inside the new scope. **Fact 8:** an undelivered critical finding does *not* change your authorization boundaries — but it does create a **duty to deliver fast-track**: notify the contact immediately of the critical (verbal + written interim notice) while finishing the full report, because a known-exploited-in-the-wild critical on an internet-facing host with an incident now *underway* makes report latency itself a risk you're contributing to. Scope discipline and delivery urgency are separate obligations; neither cancels the other. → [M12 lesson](../../modules/module-12-vulnerability-assessment-and-security-testing/README.md) · [Lab Safety Policy](../../lab-safety-policy.md)

</details>

<details>
<summary><b>Q2 — Triage to incident (M13)</b></summary>

**Fact 3 (outbound + DNS 25×):** verdict — **TP, high, act now**: unknown outbound to a newly registered domain outside baseline = possible C2/beacon/exfil (T1071.004 DNS C2 / T1048 exfil). Action: identify process→domain, block domain at resolver/proxy, capture PCAP, pivot to host. **Fact 4 (new Run-key task with unsigned binary):** verdict — **TP, high**: persistence creation with no change ticket (T1547.001) → isolate candidate, hash/collect `helper.exe`. **Fact 5 (unexpected auto-email with patient data):** verdict — **TP, high with privacy dimension**: probable exfiltration via legitimate mail channel (T1070.008/SMTP-based exfil; also data-theft) → preserve mailbox logs/sent items, notify privacy lead (patient PII → breach-assessment clock starts, M17). **Correlation:** any one alert is suspicious-but-plausible (scan noise, IT change, mailing bug); *same host + same window (04:40–04:52) + attacker-controlled infrastructure + no change record + patient data leaving* turns three observations into one **confirmed incident with established scope and impact** — that's the collect → correlate → detect step working, and it escalates from *alert* (event) to *incident* (confirmed adverse event requiring IR). **ATT&CK:** T1190 (exploit public-facing app, 04:38), T1547.001 (Run-key persistence), T1071.004 (DNS), T1105/T1041 (C2/exfil over SMTP), T1567 (exfiltration over web service — if web upload observed). → [M13 lesson](../../modules/module-13-logging-monitoring-and-security-operations/README.md)

</details>

<details>
<summary><b>Q3 — IR sequencing (M14)</b></summary>

**Order with justification:** (h) **capture evidence first-ish** — actually *begin concurrently with containment*: memory + disk image + logs *before* destructive changes (fact 6 shows this happened — memory before eradication), because eradication destroys the proof of how they got in. (c) **isolate the web server** — stop active C2/exfil *while keeping it live for imaging* (network cut, not power-off). (d) **block C2 domain** at DNS/proxy — cheap, immediate, org-wide protection, and it also stops other potential victims. (g) **scope** — which hosts reached `appt-sync[.]cc`? what did the DB export contain? which emails left? (this informs whether one-host or multi-host and starts the breach clock). (b) **notify per plan** — practice owner immediately; patient-notification obligations depend on scoping/PII findings (legal clocks run from *discovery*, so don't wait for perfection — early internal notice, factual external drafts coordinated with the practice). (a) **eradicate** `helper.exe` + Run key + confirm the initial vector (framework patch applied — the exploit path must die too). (e) **verify eradication** — rescan, IOC sweep across fleet, monitor for recurrence. (f) **restore/repatched service** — only *after* (a)+(e): restore to a patched baseline (or apply the M12 fix), then retest. **Must NOT happen first:** eradication/reimage *before* evidence capture (memory + process/network state gone, root-cause question unanswered → the next incident repeats it) **and** restore before eradication (you re-infect the fresh copy). Also must-not: quietly fixing without breach assessment — patient PII left the practice; notification duties attach to *discovery*. → [M14 lesson](../../modules/module-14-incident-response-and-digital-forensics/README.md) · [LAB-14](../../labs/lab-14-ir-tabletop/README.md)

</details>

<details>
<summary><b>Q4 — Forensic reasoning (M14)</b></summary>

**First access: 04:38** — the framework RCE request (proof: **web server access/error logs** showing the exploit payload URI/POST at 04:38, plus the framework's own logs). **Attacker's actions in order, with proving artifact class:** (1) **04:38 initial access** via RCE — *web access logs* (+ framework error/debug traces); (2) **04:41 tool staging** — `helper.exe` written to `C:\ProgramData\appt\` — *filesystem timestamps (mtime/ctime) + MFT/directory entry*; (3) **04:42 persistence** — Run-key/scheduled task created — *registry/systemd artifact + task XML* (and Prefetch/Amcache showing first execution); (4) **04:40–04:52 collection + C2/exfil** — DB export read, SMTP/DNS to `appt-sync[.]cc`, patient email at 04:52 — *DNS/proxy logs, mailbox sent-items, file access timestamps on `patients_export.csv`*; (5) memory corroboration — *memory dump* showing loaded `helper.exe` + open sockets at capture. All times normalized to one timezone before ordering (M14 discipline). **Two things to verify before "root cause with confidence":** (1) the RCE was *actually exploitable and used* — not just version-present: confirm the exploit request succeeded (response code/body, error-log evidence, or process-spawn evidence at 04:38), closing the gap between "vulnerable version" and "exploited vulnerability"; (2) **initial-access completeness** — rule out a *second* vector (valid credentials in auth logs? another internet-facing service? the contractor's Monday activities?) by checking auth logs for successes and confirming no earlier first-contact than 04:38. (Bonus: confirm `helper.exe` hash/SIG lack — that the binary is attacker-written, not a legitimate tool renamed.) → [LAB-15](../../labs/lab-15-digital-forensics/README.md)

</details>

<details>
<summary><b>Q5 — Malware-to-defense (M15)</b></summary>

**IOCs (4, typed):** (1) *File hash:* SHA-256 of `helper.exe` (exact-sample hunting across EDR/mail); (2) *File path + persistence:* `C:\ProgramData\appt\helper.exe` + Run key `WinSvchHelper` (host detection); (3) *Network domain:* `appt-sync[.]cc` and `mail.appt-sync[.]cc` (DNS/proxy block + hunting); (4) *Network infra:* the sender VPS IP from fact 6 (firewall/flow-log hunting — note: IPs rot; domain+hash have longer dwell value). **ATT&CK (2):** **T1547.001** (Run Keys persistence) and **T1071.004** (Application Layer Protocol: DNS/SMTP for C2+exfil) — plus T1190 for the chain's start. **Detection 1 — Sigma (persistence):**
```yaml
detection:
  selection:
    TargetObject|contains: '\CurrentVersion\Run\'
    Details|contains: 'ProgramData\appt\'
  condition: selection
level: high
```
*FP control:* the conjunction is **path + value specific** (Run keys fire constantly; the *specific* `ProgramData\appt` value doesn't), so precision stays high — generic Run-key rules would flood. **Detection 2 — YARA (family):** match on the packed sample's stable features — the email-library string set + `patients_export.csv` marker + PE section entropy threshold (e.g., `strings: $s1="patients_export" $s2="appt-sync" $smtp_dll; condition: all of them and (entropy of .text > 7.0)`). *FP control:* compound conditions (strings **and** entropy) don't collide with system files; test against `System32` before deployment (M15 exercise discipline), and note packing means *runtime* strings/behavior rule complements static YARA. → [M15 lesson](../../modules/module-15-malware-and-defensive-analysis/README.md) · [LAB-16](../../labs/lab-16-malware-behavior/README.md)

</details>

<details>
<summary><b>Q6 — Lessons learned (M12–M15)</b></summary>

1. **Assessment process — close report latency (owner: you/contractor; due: 5 business days).** A critical internet-facing RCE sat undelivered while the incident began. Fix: interim-notice rule — *any critical finding is communicated verbally+written within 2 hours of validation*, full report within 48h; add the clause to the RoE template and the M12 report checklist; measure: validation-to-notification time per engagement.
2. **Detection coverage gap — exploitation at 04:38 wasn't noticed until 09:12 (owner: IT contractor; due: 30 days).** The 4.5-hour gap: alerts watched *egress/persistence*, not *exploitation itself*. Fix: add detections at the entry point (web-app exploit patterns, framework error-rate spike, WAF-in-front-of-booking-site decision), reduce DNS/alert latency to near-real-time, and ensure after-hours alert routing (04:38 fell outside business-hours staffing — a 24/7 escalation path or automated blocking for high-confidence signals). Measure: MTTD for a red-team-planted exploit in the next tabletop.
3. **Control that would have reduced impact (owner: practice owner; due: 45 days).** Patch the outdated framework (the M12 fix — *this incident is the argument*) + segment the web server from the patient DB (it read `patients_export.csv` directly — a boundary would have forced a second hop and bought detection time). Layer: outbound allow-listing would have blocked `appt-sync[.]cc` at 04:40, hours before the alert. Prioritize: patch (prevent) → segmentation (contain) → egress control (detect/limit).
4. **Authorization culture (owner: both parties; due: immediate/ongoing).** "Just scan, it's our box" is how unauthorized-access incidents happen — including well-intentioned ones. Fix: RoE amendment procedure documented in the MSA, contractor staff briefed that scope changes require written amendments, and an explicit line in engagement closeout confirming *no out-of-scope activity occurred*. Measure: zero scope exceptions per engagement; amendments on file for every extra target.

*(Full credit: one lesson per required theme, each with owner + date + measurable outcome.)* → [M12](../../modules/module-12-vulnerability-assessment-and-security-testing/README.md) · [M13](../../modules/module-13-logging-monitoring-and-security-operations/README.md) · [M14](../../modules/module-14-incident-response-and-digital-forensics/README.md) · [M15](../../modules/module-15-malware-and-defensive-analysis/README.md)

</details>

---

## Rubric (self-assess)

| Criterion | Max | What a full-credit answer does |
|---|---|---|
| Technical accuracy | 8 | Correct triage verdicts, sequencing, artifact citations, IOC/rule quality |
| Reasoning & prioritization | 6 | Sequences justified (volatile-first, contain-before-recover), decisions tied to facts |
| Safety / scope / ethics | 4 | RoE discipline, notification duties, evidence handling explicit |
| Clarity and structure | 2 | Organised, unambiguous |
| **Pass = ≥ 12/20** | | |

**Completion check:** all six answered; Q2 gives verdict+severity+action for all three alerts; Q3 orders all eight actions with two "must-not-first" reasons; Q5 delivers 4 typed IOCs + 2 detections with FP controls; Q6 has four lessons with owners and dates.

**Next:** [Level 4 case study CS-4](cs-4-cloud-privacy-automation.md) · **Previous:** [M15 quiz](../level-3/quiz-m15.md) · **Hub:** [Assessment Hub](../README.md)
