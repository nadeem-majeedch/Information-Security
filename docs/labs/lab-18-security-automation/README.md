---
title: "LAB-18 — Security Automation with Synthetic Logs"
layout: default
---

# LAB-18 — Security Automation with Synthetic Logs

**Lab ID:** LAB-18 · **Difficulty:** Intermediate · **Estimated duration:** 2.5 hours · **Module:** M18 · **Mode:** Local scripting over provided synthetic datasets (no live systems, no external API keys)

## Scenario

**Northwind Hosting** (fictional) has a 40 GB daily auth log and four analysts who *grep* it by hand — it doesn't scale, and findings live in people's shell histories instead of being reviewable. You are hired to build the first slice of the **detection pipeline** the team wishes they had: small, readable, testable scripts that turn raw lines into a prioritized alert file and a shareable report. Everything runs on your machine against course-provided synthetic logs (the same dataset used by [LAB-13](../lab-13-log-analysis/README.md)), so your pipeline can be built, broken, and re-run freely.

## Learning Objectives

1. Write defensive automation that parses, normalizes, detects, and reports on security logs.
2. Implement **rule-as-data**: detection logic held in a separate config (JSON/YAML), not buried in code — so analysts can tune without editing Python.
3. Validate automation the professional way: test fixtures (known-good/known-bad lines), counting assertions, and a documented false-positive baseline.
4. Handle the operational realities: malformed lines, time parsing, duplicate suppression, severity ordering.
5. Package a mini-pipeline (extract → detect → enrich → report) with a README another analyst can run in one command.

## Prerequisites and Required Skills

- M18 module (automation concepts, pipeline stages), M13 (log formats, alert triage), LAB-13 (dataset familiarity).
- Skills: basic Python 3 (loops, lists, file I/O) — starter snippets provided; command-line basics.

## Tools, Operating Systems, and Versions

- Python 3.8+ (preinstalled on most systems; verify `python3 --version`).
- Provided datasets: [`data/syslog-sample.log`](./data/syslog-sample.log) (synthetic syslog — detections) and LAB-13's `auth-attempts.csv` + `admin-actions.jsonl` (enrichment/correlation).
- Standard library only (`re`, `json`, `csv`, `datetime`, `argparse`) — **no pip installs required**, so nothing to audit or break offline.
- Optional: `jq` for quick sanity checks; any editor or VS Code.

**$0.** No cloud functions, no SaaS tiers, no API keys — deliberately designed so no secret is ever needed (Safety Policy §5).

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-18/pipeline/`; copy the datasets in.
2. Confirm Python: `python3 --version` (≥ 3.8). *What it does:* prints your interpreter version; the lab uses only features present in 3.8+.
3. Scope statement: *scripts run only on local course files; no network calls (nothing imports `requests`/`urllib`); no real systems, users, or credentials touched.*
4. Ground rule for this lab: **every script must be re-runnable and deterministic** — same input → same output, so your report is reproducible evidence.

## Lab Environment and Starting State

Local directory with: `syslog-sample.log` (~200 lines: sshd failures/successes, sudo events, cron noise), plus LAB-13's two files. Starting state: no scripts, no alerts, no baseline. Target deliverable pipeline: `parse → detect → enrich → report`.

## Tasks

1. **Parser foundation — `parse_logs.py`:** read `syslog-sample.log`, emit a normalized list of dicts (`time`, `host`, `process`, `message`, `raw`). Handle **malformed lines** gracefully: count them, log the line number, *continue* (never crash — a parser that dies on one bad line is worse than grep). Show the first 5 parsed records and the malformed count.
2. **Rules as data — `rules.json`:** define at least 3 rules *outside the code*, each with `id`, `name`, `pattern` (regex), `severity`, `field_hint`. Example starter: failed-ssh-burst (`Failed password` count per source IP ≥ 10 in the file), possible-success-after-failures (a `Accepted password` for an IP that previously failed — the classic brute-force success signal from LAB-13), sudo-from-unexpected-context (if present in data). Your `detect.py` loads the JSON and applies rules generically — **prove tunability** by changing a threshold in `rules.json` and re-running without touching code.
3. **Detector — `detect.py`:** produce `alerts.json` with rule id, severity, matched value (e.g., source IP), count, first/last timestamps, and a sample raw line. **Order by severity then count.** Suppress duplicate raw lines (same IP + same rule → one alert with a count, not 40 alerts).
4. **Test fixtures — `tests/`:** write `known_bad.txt` (lines you *constructed* to trip each rule) and `known_good.txt` (benign ssh/cron lines that must NOT alert), plus `test_detect.py` using `assert` statements that run the detector on each and assert expected alert counts. Run `python3 -m unittest` or plain `python3 test_detect.py` — record the passing output. *This is the point of the lab: security automation is only trustworthy when its behavior is itself tested.*
5. **Enrichment/correlation — `enrich.py`:** join alerts with LAB-13's `auth-attempts.csv` (add username(s) seen for the offending IP) and note whether the IP appears in `admin-actions.jsonl` (a successful privileged action after failures = escalate to P1). Output `enriched-alerts.json` + a one-line rationale per alert.
6. **Report — `report.py`:** generate `alerts.md`: executive count line (by severity), then a table of alerts sorted P1→P3, each with *what, when, evidence line, recommended next analyst step* (triage language from M13). Make it something a human would actually read in an on-call handoff.
7. **Baseline & FP discipline:** run over the dataset, document *known false-positive categories* (e.g., a service reboot causing a burst of failures = expected) in `README.md`, with the suppression/tuning approach for each. State the false-positive *rate you observed* (alerts reviewed ÷ alerts fired).
8. **README:** one-command run (`python3 run_all.py` or a 3-line sequence), dataset provenance (synthetic, course-provided), rule-tuning instructions, and how to interpret each alert field.

## Expected Observations

| Task | Expected |
|---|---|
| Parser | >190 records parsed; malformed count reported (dataset includes a couple of broken lines on purpose); **no traceback** |
| Rules-as-data | Editing a threshold in `rules.json` changes alert counts without editing Python |
| Detector | Burst IPs surface with counts (single-digit-to-teen counts on this small set — not thousands); success-after-failures rule fires at least once if present in data |
| Ordering/dedupe | Alerts sorted by severity; each (IP, rule) appears once with a count |
| Tests | All assertions pass on fixtures; known_good produces **zero** alerts |
| Enrichment | Alert rows gain usernames + a privilege-action note; at least one alert escalates rationale |
| Report | Top summary line + readable table; severity distribution matches `alerts.json` counts |
| FP baseline | ≥ 2 FP categories named with tuning approaches |

Exact counts depend on the dataset — your report must *state the counts you got* and reconcile them with your own detector logic (justify, don't hand-wave).

## Investigation Questions

1. Your detector catches a burst rule — an attacker who knows your rule could stay *under* the threshold. What complementary detection (trend/velocity, entropy, allow-list deviation) closes that gap? (Rule evasion thinking, defensively framed.)
2. The same script on a 40 GB log: name two scaling problems you'd hit (memory from loading all lines? re-reading on every run?) and the design change for each (streaming line-by-line; incremental watermark by timestamp).
3. Rules-in-config vs rules-in-code: one advantage *for analysts* and one *risk* (what happens when a config rule has a bad regex that matches everything — who validates `rules.json`?).
4. Your pipeline is deterministic — why does that matter for an investigation (evidence reproducibility, "show your work" to an auditor)?
5. Where does this sit on the M02 control taxonomy: detective or corrective? What single addition would make it *preventive* (e.g., auto-blocking — and what new risks does automation-with-enforcement introduce)?

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `ModuleNotFoundError` | You imported a third-party lib | Stay on stdlib — the lab guarantees zero installs |
| `regex.error` / no matches | Over-escaped pattern or bad anchors | Test fragments with `python3 -c "import re; print(re.findall(r'...', 'line here'))"` before running the full pipeline |
| Every line counts as malformed | Wrong field splitting (syslog format differs from your split) | Print `repr()` of one raw line; adjust split/regex to the actual format |
| Duplicate alerts (40 rows for one IP) | No aggregation step | Dedupe on (rule_id, matched_value) with a counter — see Task 3 |
| Timestamps sort wrong | Mixed formats / timezone-naive strings | Parse to `datetime` with a documented format; note timezone assumption in README |
| Tests fail after tuning `rules.json` | Fixtures hard-coded to old thresholds | Assert against *expected current* behavior; keep fixture thresholds aligned or make tests read the config |
| Output looks nondeterministic | Dict/set iteration or unsorted lists | Sort explicitly before writing (by severity, then count, then key) |

## Evidence to Collect

- `parse_logs.py` output (first 5 records + malformed count).
- `rules.json` (final) + proof of a threshold change altering counts (before/after alert totals).
- `alerts.json` + `enriched-alerts.json` (sanitized — dataset is synthetic, so already safe).
- `tests/` passing run output (screenshot or pasted terminal).
- `alerts.md` report (the human-facing artifact).
- `README.md` with FP baseline + one-command run + rule-tuning notes.
- Safety statement: *local scripts on course-provided synthetic files only; no network access, no API keys, no live systems.*

## Deliverable and Report Structure

`portfolio/LAB-18/pipeline/`: (1) `README.md` (run instructions, dataset provenance, FP baseline), (2) `parse_logs.py`, (3) `rules.json`, (4) `detect.py`, (5) `tests/` + passing output, (6) `enrich.py` + `enriched-alerts.json`, (7) `report.py` + `alerts.md`, (8) safety statement. Code commented with *why* (not line-by-line narration).

## Completion Checklist

- [ ] Parser handles malformed lines without crashing and reports the count
- [ ] ≥ 3 detection rules live in `rules.json`; threshold edit demonstrated
- [ ] Alerts ordered by severity, deduplicated with counts
- [ ] Test fixtures (bad + good) and passing automated tests
- [ ] Enrichment joins LAB-13 data; rationale line per alert
- [ ] `alerts.md` readable report with counts reconciled to `alerts.json`
- [ ] False-positive baseline documented with ≥ 2 categories
- [ ] README enables a fresh analyst to run it in one command
- [ ] Safety statement written (no network, no keys, synthetic data only)

## Cleanup and Reset

1. Stop any running process (all scripts are short-lived foreground runs — `Ctrl+C` if you left one open; nothing persists).
2. Scripts touched only local files; deleting `portfolio/LAB-18/` resets fully. Keep it — it's portfolio evidence.
3. If you added `__pycache__/`, remove it (`rm -rf __pycache__`) — build artifacts, not deliverables.
4. No secrets were used, so no key rotation needed — confirm by grepping your own code for hard-coded values.

## Optional Challenges

- **Streaming mode:** rewrite `detect.py` to process the log line-by-line (generator) so memory stays flat; demonstrate with a larger synthetic file you generate by repeating the dataset with shifted timestamps.
- **MITRE mapping:** add a `technique` field per rule (e.g., brute force → T1110; verify on attack.mitre.org) and group the report by technique.
- **Scheduled run (local only):** wire `run_all.py` into `cron` **on your own machine only** with a comment explaining what a real SOAR/SIEM scheduler would do differently (and why auto-*enforcement* needs human gates — M18 ethics).

## References and Safety Notes

- Python `re`/`json`/`csv`/`unittest` docs: <https://docs.python.org/3/library/> (version 3 docs — match your `python3 --version`).
- NIST SP 800-61 Rev. 2 (*Computer Security Incident Handling Guide*) for the triage-to-response handoff: <https://csrc.nist.gov/pubs/sp/800/61/r2/final>.
- MITRE ATT&CK detection techniques: <https://attack.mitre.org/techniques/>.
- Course: [M18](../../modules/module-18-security-automation-and-emerging-challenges/README.md) · [LAB-13 dataset source](../lab-13-log-analysis/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** defensive automation over course-provided **synthetic** logs; scripts run locally with **no network calls and no API keys**; nothing targets a live system (Safety Policy §2, §5). Because the dataset is synthetic, all generated reports are safe to share as portfolio artifacts (§5).

**Navigation:** · [← Previous: LAB-17](../lab-17-cloud-config-review/README.md) · [Lab index](../README.md) · [Next: LAB-19 →](../lab-19-defensive-capstone/README.md)
