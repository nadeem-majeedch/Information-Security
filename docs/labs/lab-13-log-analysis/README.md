---
title: "LAB-13 — Log Analysis, Authentication Anomalies, and Alert Triage"
layout: default
---

# LAB-13 — Log Analysis, Authentication Anomalies, and Alert Triage

**Lab ID:** LAB-13 · **Difficulty:** Intermediate · **Estimated duration:** 2.5 hours · **Module:** M13 · **Mode:** Analysis of a provided synthetic log (no live targets)

## Scenario

You are the on-call analyst at **BrightHost** (fictional small hosting firm). Overnight, two alerts fired on `web01`: "multiple SSH failures" and "sudo by service account." The ticket says: *triage, decide, and hand off.* You have the server's auth log — nothing else. Your job mirrors the real M13 triage workflow: establish what happened, how bad, what it means, and what to do next, with evidence for every claim.

## Learning Objectives

1. Parse syslog-style authentication logs with `grep`/`awk`; build a precise event timeline.
2. Distinguish benign noise from a brute-force campaign, a successful compromise indicator, and insider-style anomalies.
3. Complete a triage worksheet: verdict, severity, scope, and escalation decision with justification.
4. Draft a detection rule (Sigma-style) that would have caught the campaign earlier, mapped to MITRE ATT&CK.
5. Recommend preventive/detective controls that shrink this specific risk — connecting findings to M02 control types.

## Prerequisites and Required Skills

- M13 module (log sources, triage workflow, ATT&CK mapping), M05 (what "normal" looks like on a host), M04 (ports/protocols vocabulary).
- Skills: `grep`/`awk` basics (a cheatsheet is inline below), careful timeline writing.

## Tools, Operating Systems, and Versions

- Provided dataset: [`data/auth.log`](./data/auth.log) — **synthetic**, ~70 lines, generated for this lab (realistic sshd/sudo format; RFC-3164-style timestamps; host `web01`; lab-range IPs only).
- Any text tools: `grep`, `sort`, `awk`, or a text editor. Optional: Timeline Explorer-style viewers (not needed).
- Reference: MITRE ATT&CK (browser) for technique IDs.

**$0.** No services, no scanning, no live hosts.

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-13/`; copy `data/auth.log` into it.
2. No accounts, no network activity, no authorization needed — the dataset is course-provided synthetic data (Safety Policy: data rules satisfied; nothing real is touched).
3. Note the dataset's ground truth *header comments* if present; treat the log itself as your only evidence.

## Lab Environment and Starting State

One log file. Events are timestamped `Oct 10` across several hours, mixing: repeated `Failed password` lines (some for *invalid users*), a few `Accepted` logins, `pam_unix ... session opened` lines, and `sudo` entries. IPs are from the RFC1918 lab range (`192.168.56.x`). Starting state: no analysis; no triage decision made.

## Tasks

1. **Orientation:** `wc -l auth.log` (line count); `head -5` / `tail -5`; note the format: `Mon DD HH:MM:SS host process[pid]: message`. Write the two "normal baseline" observations (e.g., daytime logins from a known admin host using **publickey**).
2. **Failure census:**
   ```bash
   grep -c "Failed password" auth.log        # how many failures total
   grep "Failed password" auth.log | awk '{for(i=1;i<=NF;i++) if($i=="from") print $(i+1)}' | sort | uniq -c | sort -rn
   ```
   *What they do:* count failures; then extract the token after each `from` (source IP), tally per IP, sorted by frequency. Expect **one dominant source IP** with dozens of failures — record it and the count.
3. **User census:** `grep "Failed password" auth.log | awk '{print $(NF-5), $(NF-4), $(NF-3)}'`? Simpler and robust: `grep -oE "Failed password for (invalid user )?[a-z_]+" auth.log | sort | uniq -c | sort -rn` — lists targeted usernames with counts, flagging `invalid user` attempts (user-enumeration noise) vs valid accounts (the prize).
4. **Success hunt:** `grep "Accepted" auth.log` — list every successful login: time, method (password/publickey), user, source IP. **The critical question:** did any success come *from the failure storm's IP*? Cross-reference timestamps (storm window vs success time). Record the answer with line numbers.
5. **Anomaly pass:** scan for entries that are odd *even if successful*: root login from a non-admin host; a success at 0x:xx hours; `sudo` commands by a **service account** (e.g., `svc_backup ... USER=root ; COMMAND=...`); `useradd` via sudo; sessions "opened ... by (uid=0)" chains. For each oddity: what legitimate story *could* explain it, and what hostile story could?
6. **Triage worksheet** (fill completely):

   | Field | Your entry |
   |---|---|
   | Incident type (one label) | e.g., credential attack → possible compromise |
   | Timeline (UTC-independent, from log) | first failure → last failure → success(s) → suspicious sudo |
   | Source(s) | IPs + internal/external判断 (all RFC1918 = internal-network attacker story) |
   | Affected account(s) | which were targeted; which succeeded |
   | Severity (L/M/H) + justification | tie to account privilege + actions post-login |
   | Confirmed vs suspected | what the log *proves* vs what needs more data (shell history? process logs?) |
   | Verdict | e.g., TRUE POSITIVE — brute force with successful authentication; escalate |
   | Immediate actions (3) | e.g., isolate/limit source IP at firewall; force-reset the compromised credential; snapshot for forensics (M14 handoff) |
   | Follow-up (3) | disable password auth for SSH; add fail2ban/rate limit; alert tuning; review svc_* account design |

7. **Detection rule (Sigma-style draft):**
   ```yaml
   title: SSH Brute Force Followed by Success (web01)
   logsource: linux-auth   # conceptual source: sshd/pam auth logs
   detection:
     sel_fail:
       message: "Failed password"
     sel_burst:
       # >10 failures from one source within 10 minutes (windowing depends on backend)
     sel_success:
       message: "Accepted"
     condition: sel_burst and sel_success within 10m
   level: high
   tags: [attack.credential_access, t1110.001]
   ```
   Complete it: name the data source it needs, the false-positive sources (helpdesk password resets?), and the tune (threshold/window). ATT&CK: **T1110.001** (Brute Force: Password Guessing) is the anchor — verify on attack.mitre.org and add any follow-on technique for the post-login actions you saw (e.g., account creation → **T1136.001** Create Account: Local Account).
8. **Handoff note:** 5 sentences the IR team (M14) receives: what you confirmed, evidence pointers (log line numbers), what not to touch, and your recommended next owner.

## Expected Observations

| Task | Expected result (verify against the actual file) |
|---|---|
| Failure census | ~46 failures, dominated by a single `192.168.56.105`-style lab IP (one late straggler exists — don't miss it) |
| User census | Mix of `invalid user` names (noise/enumeration) and real-looking accounts (`svc_backup`, `deploy`, `dbadmin`) |
| Success hunt | ≥ 1 `Accepted password` **from the same storm IP** shortly after the burst — the smoking gun |
| Anomalies | A `root` login from a *different* internal IP + `sudo useradd` + `sudo /bin/bash` by a service account — post-compromise behaviors |
| Triage | Verdict = true positive with escalation; "internal IP" noted (rogue device or lateral movement story) |
| Daytime publickey logins | Benign baseline — correctly *not* flagged (an analyst who flags everything burns trust) |

## Investigation Questions

1. The attacker used `svc_backup` — name two design failures that made this account valuable (password auth enabled? over-privileged? service account with interactive login?) and map each to a control (M02 types).
2. `invalid user` attempts: what are they doing tactically (username spray/confirmation), and why must your alerting *not* page someone for them alone?
3. The `sudo ... /bin/bash` line: explain why this elevates the incident from "attempt" to "likely interactive control," and which M14 evidence you'd collect next (memory? process accounting? — noting the log already shows `useradd`).
4. All IPs are RFC1918 (internal). Reconstruct two plausible internal-attacker stories (compromised workstation vs rogue insider vs compromised other server) and the *one check* that distinguishes them.
5. Your Sigma draft: which field would break if the log format changed (timestamp locale? message wording), and what's the engineering fix (normalization — CEF/structured logging discussion)?

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `grep -c` returns small number | Counting only exact case/format | Match the dataset's exact phrasing (`"Failed password"`) — the file is consistent |
| awk extraction looks wrong | Field positions vary with username length | Use the `grep -oE` approach in Task 3 — pattern-based beats position-based (a real engineering lesson) |
| Missing the late straggler failure | You assumed one window | Always `grep -n "Failed password" | tail` — tail events matter |
| Conclusions without line numbers | Evidence discipline slipping | Every claim cites `grep -n` output line numbers |
| Flagged the daytime logins too | No baseline defined | Task 1's baseline exists precisely to separate normal (publickey, business hours, known admin host) from anomalous |
| Timestamps have no year | syslog classic format | Note the limitation; IR needs year/timezone — an honest "data quality" finding for your report |

## Evidence to Collect

- Command transcript (all census commands + key outputs).
- `timeline.md` — ordered events with log line numbers.
- Completed **triage worksheet** (all fields).
- `detection-rule.yml` — your finished Sigma-style draft + FP/tune notes + verified ATT&CK IDs.
- `handoff.md` — 5-sentence IR handoff.
- Safety statement: *analysis confined to the provided synthetic log; no live systems contacted; no credentials used.*

## Deliverable and Report Structure

`portfolio/LAB-13/`: (1) environment/dataset description (synthetic, source = course), (2) census outputs, (3) timeline, (4) triage worksheet, (5) detection rule + tuning notes, (6) control recommendations (preventive/detective typed), (7) handoff note, (8) safety statement. 2–3 pages.

## Completion Checklist

- [ ] Failure/user/success censuses run with recorded commands and outputs
- [ ] Storm source IP identified; late straggler found
- [ ] Success-from-storm-IP correlation found with line numbers
- [ ] ≥ 3 post-login anomalies documented (root login / sudo useradd / sudo bash or equivalent in file)
- [ ] Benign baseline explicitly stated (what was correctly ignored)
- [ ] Triage worksheet complete with severity justification and verdict
- [ ] Sigma-style rule finished (window, threshold, FP sources, ATT&CK IDs verified)
- [ ] 5-sentence handoff written
- [ ] Safety statement written

## Cleanup and Reset

1. Nothing executed against any system — no cleanup needed beyond file tidying.
2. Consolidate working files into `portfolio/LAB-13/`; delete scratch extracts.
3. Dataset is yours to keep; nothing sensitive (it's synthetic by design).

## Optional Challenges

- Write the *preventive* companion: the 5-line sshd hardening config (disable password auth for admin accounts, restrict source ranges) with each line explained — LAB-06/LAB-08 crossover.
- Convert the timeline into the M14 IR-plan format (detection → analysis → containment → eradication → recovery columns).
- Script the census: a 15-line Python or awk program that takes any auth.log and outputs failures-per-IP + successes-after-bursts — the seed of LAB-18's automation.

## References and Safety Notes

- MITRE ATT&CK T1110 (Brute Force) & T1136 (Create Account): <https://attack.mitre.org/techniques/T1110/> · <https://attack.mitre.org/techniques/T1136/>.
- Sigma rule format (community): <https://github.com/SigmaHQ/sigma/wiki>; NIST SP 800-92 (log management): <https://csrc.nist.gov/pubs/sp/800/92/final>.
- CISA #StopRansomware & incident resources: <https://www.cisa.gov/stopransomware>.
- Course: [M13](../../modules/module-13-logging-monitoring-and-security-operations/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** this lab analyzes only course-provided synthetic data on your own machine. The log's internal IPs are documentation, not targets — nothing in this lab may be pinged, scanned, or logged into (Safety Policy §2/§3).

**Navigation:** · [← Previous: LAB-12](../lab-12-vuln-scan-interpretation/README.md) · [Lab index](../README.md) · [Next: LAB-14 →](../lab-14-ir-tabletop/README.md)
