---
title: "LAB-15 — Digital Forensics on a Synthetic Evidence Bundle"
layout: default
---

# LAB-15 — Digital Forensics on a Synthetic Evidence Bundle

**Lab ID:** LAB-15 · **Difficulty:** Advanced · **Estimated duration:** 3 hours · **Module:** M14 · **Mode:** Analysis of provided synthetic artifacts (no live targets, no real malware)

## Scenario

At 02:35 UTC, monitoring on **Orchid Hostings'** shared web server `web01` fired "WEB_SHELL_EXECUTION." The on-call analyst isolated the host at 02:41 and took a disk image (documented, out of scope for you). You are the **forensics analyst** assigned the artifact *extraction set* — three small synthetic files exported from that image. Your job: reconstruct what the attacker did, in order; state what each action proves; answer the investigation questions the incident owner wrote; and hand back a timeline and report that could survive scrutiny — using only the provided files.

## Learning Objectives

1. Practice evidence handling discipline: record hashes, note provenance, maintain a (synthetic) chain of custody.
2. Reconstruct an attack narrative from heterogeneous artifacts (timeline CSV, shell history, crontab) with timestamps reconciled.
3. Distinguish what each artifact *proves* vs merely *suggests* (source reliability).
4. Map attacker behavior to MITRE ATT&CK techniques with justified IDs.
5. Produce a forensic-style report: scope, method, findings, timeline, conclusions bounded by evidence, and a "what we'd collect next" list.

## Prerequisites and Required Skills

- M14 module (evidence order, chain of custody, timelines), M13 (log literacy), M05 (persistence locations).
- Skills: spreadsheet or sorting tools, careful reading. Optional: `sort`, `csvcut`, or a spreadsheet app.

## Tools, Operating Systems, and Versions

- Provided bundle (all synthetic, reserved `.example` domains, no real indicators):
  - [`data/timeline.csv`](./data/timeline.csv) — 20 merged events from multiple sources
  - [`data/bash_history.txt`](./data/bash_history.txt) — attacker commands recovered from root's shell history
  - [`data/crontab.txt`](./data/crontab.txt) — root crontab as collected
- `sha256sum` (coreutils) for integrity recording; any CSV viewer; optional The Sleuth Kit for the extension task (free).
- **Documented larger-dataset source (optional):** NIST CFReDS (Computer Forensics Reference Data Sets) — `https://cfreds.nist.gov` — free synthetic/reference forensic images; use only their synthetic sets, per its own guidance.

**$0.**

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-15/`; copy the three `data/` files into `evidence-originals/` (never edit originals — work on copies).
2. Integrity record: `sha256sum evidence-originals/* > bundle.sha256` (*what it does:* prints file fingerprints to a manifest so any later change is detectable — the habit every real examination starts with).
3. Permissions/scope: course-provided files on your machine only. No host is scanned, no domain resolved (they can't resolve — `.example` is reserved), nothing is executed from the bundle.

## Lab Environment and Starting State

Three text/CSV files + your empty workspace. `timeline.csv` mixes sources (`auth.log`, `webserver.log`, `process.log`, `file.artifacts`, `network.log`, `detection.alert`, `response.action`) across 02:11–02:55 UTC on one date. `bash_history.txt` holds the operator's commands in order. `crontab.txt` holds three entries — two boring, one that isn't. Starting state: no narrative, no timeline built, no conclusions.

## Tasks

1. **Integrity first:** verify `bundle.sha256` regenerates identically after your work (`sha256sum -c bundle.sha256` at the end → all OK). Record this as evidence-preservation practice.
2. **Individual artifact examination:** for each file, write 3–5 observations *of the artifact itself* (sources present, time range, gaps, format quirks — e.g., shell history is **not** a guaranteed complete record: commands with leading spaces, `HISTCONTROL` settings, or program-internal actions won't appear. Note that limitation — it's exactly what a real report must say).
3. **Initial access reconstruction:** using `timeline.csv` + `bash_history.txt`, state the intrusion chain with line references: entry vector (which request?), the uploaded artifact, the execution moment, and the privilege context (which user did the web server run as — and what does "session opened ... by (uid=0)" suggest?). Quote evidence per step.
4. **Persistence & artifacts:** identify persistence from `crontab.txt` (which entry? where does it point? what file backs it?) and cross-reference `timeline.csv` (file creation, first execution). Then: `grep -n` both artifacts so every claim carries file+line.
5. **Attacker activity timeline:** build `attack-timeline.md`: timestamp | action | evidence source+line | ATT&CK technique (justify each ID — use attack.mitre.org; expect candidates like T1190 exploit public-facing app, T1059 command interpreter, T1053 scheduled task, T1505 server software component, T1071 web protocols, T1070 indicator removal, T1082 system info discovery, T1083 file discovery, T1005 data from local system, T1041 exfil over C2 — pick what the *evidence supports*, don't pad).
6. **Attribution discipline:** separate: (a) **facts** (log lines, commands), (b) **assessments** (attacker intended X), (c) **unknowns** (identity, entry point of the *initial* webshell delivery path beyond the request, whether exfil succeeded). Explicitly mark the log-deletion command's implication for evidentiary completeness.
7. **Investigation questions (the incident owner's list — answer with evidence):**
   - Q1: What was the initial access vector, and what evidence proves execution followed it?
   - Q2: List all persistence mechanisms with file/line references.
   - Q3: Did data leave the host? What supports "attempted but blocked" vs "exfiltrated"? What single check settles it (egress logs — named, not run)?
   - Q4: What did the attacker do to hinder investigation, and what does that tell you about sophistication (low/medium/high + why)?
   - Q5: Which host account(s) were abused, and what is the *minimum* containment scope (M14: which accounts/keys/hosts now need rotation/isolation)?
8. **Report + next-collection list** (deliverable): forensic report per structure below; plus the "collect next" list — e.g., full disk image carve (TSK walkthrough below), memory image, webserver access/error logs beyond the extract, egress firewall logs, mailbox rules — each with *what question it answers*.

## Expected Observations

| Area | Expected finding (verify in files) |
|---|---|
| Initial access | SQL-injection-style `POST /upload.php?id=1 UNION SELECT…` at 02:14:39, then webshell upload (`shell.jpg.php`), then `cmd=id` execution — classic upload+webshell chain from an internal-range source |
| Privilege | Web app ran with power to open a root-owned shell path (`session opened for user www-data by (uid=0)` — a misconfiguration smell worth stating carefully) |
| Persistence | Cron entry `*/10 * * * * /tmp/.cache/kworker` + the file creation at 02:19:44 + first cron-spawned execution at 02:21:17 (within ~11 min — consistent with a 10-min cadence) |
| Discovery | `find` for `*.db`/`*.sql` in history; `ls /backup/` |
| Staging | `tar czf /tmp/.cache/update.tar.gz` over config + uploads |
| Exfil | DNS + outbound POST to `cdn-metrics.badactor.example` **blocked by egress filter** — attempted, not completed, per provided evidence |
| Anti-forensics | `rm -rf /var/log/apache2/access.log` in history; defacement overwrite (with a `.bak` the attacker made — an own-goal worth noting) |
| Response | Detection 02:35, isolation 02:41, imaging 02:55 — comment on the ~20-minute detection-to-containment window |

## Investigation Questions (analyst-level)

1. The attacker's `cp ... index.html.bak` before defacing: what evidentiary gift did they leave, and what does that pattern suggest about operator discipline?
2. `*/10` cron persistence fires *forever* — rank eradication actions: which first, and why "delete the cron line" alone is insufficient (parent mechanism, the binary, the account, the webshell)?
3. Timeline sources have different timestamp semantics (UTC labeled on CSV; syslog lines in the bundle lack TZ). How do you handle TZ ambiguity in a real report (state assumption + effect on ordering)?
4. The blocked POST: name the control that stopped it (egress filtering) and one detective that should fire *despite* the block (beacon-pattern alerting — M13 tie-in).
5. If only `bash_history.txt` survived (logs wiped), what percentage of the narrative survives, and which question becomes unanswerable? (Justify the "logs are the primary evidence" lesson.)

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| CSV columns split oddly | Commas inside quoted fields | Use a spreadsheet or `python3 -c "import csv…"`; don't trust naive `cut -d,` |
| History looks sparse | That's realistic — it's not a full recording | The gap is a *finding*; say so in the report (Task 2) |
| ATT&CK IDs guessy | Picking from memory | Open attack.mitre.org; pick the technique whose description matches your quoted evidence line |
| Conclusions outrun evidence | Normal bias | Task 6's fact/assessment/unknown tagging is mandatory — graders check it |
| Timeline duplicates events | Same event in two sources | Correlate by timestamp+action; note *corroboration* (two sources agreeing raises confidence — say it) |
| Tempted to "try" the webshell line | It's a log entry, not instructions | Never reconstruct/execute attacker payloads — analysis is textual here (Safety Policy §4) |

## Evidence to Collect

- `bundle.sha256` + final `sha256sum -c` OK output.
- `artifact-notes.md` (Task 2 incl. history-completeness limitation).
- `attack-timeline.md` with per-row evidence references + ATT&CK justifications.
- Answers Q1–Q5 (Task 7) with file+line citations.
- `forensic-report.md` + `next-collection-list.md` (each item: question it answers).
- Safety statement: *course-provided synthetic bundle only; nothing executed, resolved, or scanned; originals untouched (hash-verified).*

## Deliverable and Report Structure

`portfolio/LAB-15/`: (1) evidence inventory + hashes + custody note, (2) method (tools, limitation statement), (3) attack timeline table, (4) investigation answers Q1–Q5, (5) conclusions strictly fact/assessment/unknown-tagged, (6) next-collection list, (7) safety statement. 3–4 pages.

## Completion Checklist

- [ ] Evidence bundle inventoried; every file hashed (SHA-256) and listed
- [ ] Chain-of-custody note written (who/what/when/how obtained)
- [ ] Method documented: tools used (or stated as manual) + an explicit statement of limitations
- [ ] Attack timeline built from timestamps, with each entry citing its source artifact
- [ ] Deleted/hidden artifacts recovered (or the recovery attempt documented)
- [ ] Investigation answers Q1–Q5 each cite a specific artifact — no unsupported claims
- [ ] Conclusions tagged fact vs assessment vs unknown (no conflation)
- [ ] Next-collection list written (what you'd acquire with more access/time)
- [ ] Safety statement written; originals left unchanged

## Cleanup and Reset

1. Nothing executed — no system cleanup needed.
2. Keep `evidence-originals/` unchanged; your work lives in analysis files; consolidate under `portfolio/LAB-15/`.
3. If you installed The Sleuth Kit for the challenge, removal is optional (`sudo apt remove sleuthkit`).

## Optional Challenges

- **Real tooling on a real synthetic image:** download one *synthetic* training image from **NIST CFReDS** (documented free source, `cfreds.nist.gov`) and practice `fls` (list files incl. deleted), `istat` (metadata/timestamps), and `mactime` (timeline text) on it — write half a page on how machine-generated timelines differ from your hand-built one.
- Write the YARA rule (M15 preview) that would match the webshell artifact *pattern* described in the timeline (extension + upload dir + cmd parameter).
- Convert your timeline into the tabletop format of LAB-14 — feeding a future exercise.

## References and Safety Notes

- NIST SP 800-86, *Guide to Integrating Forensic Techniques into Incident Response*: <https://csrc.nist.gov/pubs/sp/800/86/final>; NIST SP 800-61r3 (IR phases): <https://csrc.nist.gov/pubs/sp/800/61/r3/final>.
- The Sleuth Kit documentation: <https://www.sleuthkit.org/>; Autopsy: <https://www.autopsy.com>.
- NIST CFReDS (synthetic/reference forensic datasets): <https://cfreds.nist.gov>.
- MITRE ATT&CK (technique verification): <https://attack.mitre.org>.
- Course: [M14](../../modules/module-14-incident-response-and-digital-forensics/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** all artifacts are synthetic and course-provided; domains use the reserved `.example` TLD (nothing resolves); no payloads are reconstructed or executed; analysis is textual on your own machine (Safety Policy §2/§4).

**Navigation:** · [← Previous: LAB-14](../lab-14-ir-tabletop/README.md) · [Lab index](../README.md) · [Next: LAB-16 →](../lab-16-malware-behavior/README.md)
