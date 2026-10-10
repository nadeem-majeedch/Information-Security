---
title: "LAB-09 — Secure Coding and Input-Validation Testing"
layout: default
---

# LAB-09 — Secure Coding and Input-Validation Testing

**Lab ID:** LAB-09 · **Difficulty:** Intermediate · **Estimated duration:** 3 hours · **Module:** M10 · **Mode:** Local code review, static analysis, and local-only execution

## Scenario

**NoteNest** (fictional student-notes startup) inherited a small Flask service from a hackathon team and wants a security pass before coursework season. You are contracted to: review the provided code, find the seeded weaknesses with *and* without tooling, fix them, prove the fixes with re-scans, and write a short remediation report for the team. The app is deliberately insecure training code — it runs **only on your machine, bound to localhost**, and never touches a network peer.

## Learning Objectives

1. Systematically review code against a checklist mapped to CWE/OWASP classes (injection, path traversal, secrets, weak hashing, missing authz, unsafe eval, debug mode).
2. Run an automated static analyzer (Bandit) and interpret true positives vs noise.
3. Remediate each finding with a correct, minimal fix (parameterized queries, path confinement, env-var secrets, salted slow KDF, authz checks, `ast.literal_eval`/no-eval, debug off).
4. Re-scan and demonstrate measurable improvement (findings before → after).
5. Connect fixes to secure-SDLC gates: what should run in CI on every commit (preview of M18).

## Prerequisites and Required Skills

- M09 (vulnerability classes) and M10 module (secure SDLC, CWE). Basic Python reading ability (M10 outcome 1; if new, complete a Python intro first — see [Prerequisites](../../prerequisites.md)).
- No web server exposure: execution bound to `127.0.0.1`.

## Tools, Operating Systems, and Versions

| Tool | Purpose | Install |
|---|---|---|
| Python 3.9+ | Runs the app/fixes | python.org or preinstalled |
| Bandit (current) | Python SAST (static analysis) | `python3 -m pip install --user bandit` |
| Flask (needed only for optional live test) | Local run | `python3 -m pip install --user flask` |
| Optional: Semgrep Community | Second opinion | `pip install semgrep` (registry rules need network once) |
| Any editor + `diff` | Fixes + evidence | built-in |

**$0.** Provided file: [`data/vulnerable_app.py`](./data/vulnerable_app.py).

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-09/`; copy `data/vulnerable_app.py` into a scratch dir `~/notenest-lab/`.
2. Install Bandit (`python3 -m pip install --user bandit` — installs a static-analysis tool locally).
3. Permissions: your machine only. **Do not** deploy, forward ports, or expose the app beyond localhost.

## Lab Environment and Starting State

One deliberately vulnerable Python file with **7 seeded weaknesses** (numbered comments aid *self-checking only* — your report must explain each without quoting the "WEAKNESS n" labels, since real code doesn't label its bugs). Starting state: no scan run, no fixes applied. Optional live mode: `python3 vulnerable_app.py` serves on `http://127.0.0.1:5000` (localhost only — `host="127.0.0.1"` guarantees no LAN exposure; debug mode is on *because it's weakness 7*).

## Tasks

1. **Manual review first (tools second):** walk the file with this checklist; for each hit record *line, weakness class (CWE), why it's exploitable, impact*. Checklist: secrets in code; weak password storage; string-built SQL; path traversal; unsafe deserialization/eval; missing authorization on privileged action; debug/verbose mode in production path.
2. **Baseline scan:** `bandit -r . -f json -o bandit-baseline.json vulnerable_app.py` — *what it does:* recursively (`-r`) runs AST-based rules over the file, outputs JSON. Then `bandit -r . vulnerable_app.py` (readable table). Record counts by severity (HIGH/MEDIUM/…). Which findings match your manual list? Which did tools find that you missed (and vice versa)? That gap analysis is a graded artifact.
3. **Remediate all 7** with minimal correct fixes:
   - Secret → `API_KEY = os.environ.get("NOTENEST_API_KEY")` + document (never commit values — M10/LAB-18 secrets scanning).
   - MD5 password → salted slow KDF: `hashlib.scrypt`/`bcrypt`-style with per-user salt; note *why* (ties LAB-03 evidence).
   - SQL string build → parameterization: `cursor.execute("SELECT name, email FROM users WHERE id = ?", (uid,))` (driver-style placeholder; explain the difference: data never becomes syntax).
   - Path traversal → confine: `base = Path("/var/notes").resolve(); p = (base / filename).resolve(); if not p.is_relative_to(base): raise ValueError` — explain `resolve()` collapses `../`.
   - `eval` → remove or restrict: compute with an explicit parser/whitelisted ops; `ast.literal_eval` only handles literals — state why it's insufficient for arithmetic and what you chose instead.
   - Missing authz → require an authenticated admin: check session/role before acting (conceptual code fine; explain defense).
   - `debug=True` → `debug=False` (or env-driven), explaining the risk (interactive debugger = arbitrary code execution if reachable).
4. **Re-scan:** same Bandit command → `bandit-after.json`. **Expected: 0 HIGH**; explain any remaining MEDIUM/LOW (accepted-risk reasoning or further fix).
5. **(Optional, local-only) functional check:** install Flask, run `python3 vulnerable_app.py`, visit `http://127.0.0.1:5000` in a browser, confirm it still starts after your fixes (`Ctrl+C` to stop). *If Flask isn't available, skip — static proof suffices.* Never bind to `0.0.0.0`.
6. **CI gate design:** write the 5-line pipeline intent: when code is pushed → run Bandit (fail on HIGH) → run secret scan (Gitleaks) → run tests → then merge. Name the two OWASP/SAMM concepts: security gates in the SDLC, findings-as-build-failures.
7. **Remediation report** (deliverable below).

## Expected Observations

| Stage | Expected |
|---|---|
| Manual review | 7/7 classes identified (checklist is the safety net) |
| Bandit baseline | Multiple HIGH findings (e.g., `assert_used`-style N/A here, but hard-coded password hash/`eval`/`debug`/`random`-class findings appear; exact rule names vary by Bandit version — **record yours**) |
| Gap analysis | Tools flag patterns; you flag design issues (e.g., no authn concept) — both needed |
| After fixes | HIGH count = 0; remaining items justified |
| Insight | Automation catches *known patterns*; humans catch *missing* things tools can't see (absent auth checks, business logic) |

## Investigation Questions

1. Parameterized query: exactly *why* does the placeholder prevent SQL injection? (Parse-then-bind vs string assembly — one paragraph.)
2. Your path fix used `resolve()` + `is_relative_to`. Construct one input (`../../etc/passwd` style) and trace it through your fixed code step by step.
3. Bandit found `eval`; suppose it *didn't*. Which checklist step still catches it? What does that prove about SAST coverage limits?
4. The env-var secret fix: what stops the next commit from leaking it? Design the *process* (never-in-repo, secret scanner, rotation policy) in 3 bullets.
5. Is `md5(pw)` acceptable "just for a student project"? Use LAB-03 timing evidence to argue, then state the migration line (slow KDF from day one).

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `bandit: command not found` | `--user` scripts dir not in PATH | `python3 -m bandit ...` (module form) or add `~/.local/bin` to PATH |
| pip install blocked | PEP 668 / externally-managed env | Use a venv: `python3 -m venv ~/notenest-lab/.venv && source .../bin/activate` then pip inside it |
| App won't start after fixes | Missing import (`os`, `pathlib`) or Flask absent | Add imports; skip live test if Flask unavailable (static proof is sufficient) |
| "0 findings after" but you expect some | Bandit config/exit-code confusion | Run with `-f table` to confirm; check you scanned the *fixed* file path |
| Diff evidence missing | Forgot to version the original | Keep pristine copy: `cp vulnerable_app.py pristine.py` **before** editing |
| Path fix still passes bad input | Used string concat without `resolve()` | Follow Task 3 exactly; test `../` inputs mentally or with a tiny harness |

## Evidence to Collect

- `review-notes.md` — manual checklist table (line / CWE / exploit / impact) without using the "WEAKNESS" labels as the answer.
- `bandit-baseline.json` + `bandit-after.json` (or table screenshots) with counts.
- `fixes.diff` — `diff -u pristine.py vulnerable_app.py > fixes.diff` (*what it does:* unified diff of original vs fixed — your primary evidence artifact).
- `gap-analysis.md` — tool vs human findings.
- `ci-gate.md` — the 5-step pipeline design.
- Safety statement: *local static review + localhost-only optional run; no deployment, no network exposure, no real credentials.*

## Deliverable and Report Structure

`portfolio/LAB-09/`: (1) scope + file hash (`sha256sum pristine.py`), (2) manual findings table, (3) baseline scan summary, (4) `fixes.diff` with per-fix rationale, (5) after-scan summary + residual-risk note, (6) gap analysis, (7) CI gate design, (8) safety statement. 2–3 pages.

## Completion Checklist

- [ ] Manual review documented for all 7 classes (CWE named per finding)
- [ ] Bandit baseline run, counts recorded, JSON saved
- [ ] Gap analysis: tool-only vs human-only findings
- [ ] All 7 weaknesses fixed with explained, minimal correct fixes
- [ ] Re-scan shows 0 HIGH (remaining items justified)
- [ ] `fixes.diff` generated and annotated
- [ ] CI gate design written (5 steps, names 2 SDLC concepts)
- [ ] Safety statement written (localhost-only)

## Cleanup and Reset

1. Stop any running local server (`Ctrl+C`); confirm nothing listens: `ss -tulnp | grep 5000` (empty).
2. Remove scratch: `rm -rf ~/notenest-lab` (path echoed first — your own folder only) **after** copying evidence to the portfolio.
3. Uninstall optional tooling only if desired (`pip uninstall bandit flask`) — leave if planning LAB-18.
4. Nothing changed on any network or shared system; no secrets were ever real (the seeded key is a fake `sk_live_FAKE_…` marker).

## Optional Challenges

- Add a *new* seeded weakness of your own (e.g., insecure direct object reference in a route) and fix it — document how you'd add a Bandit/custom rule or test to catch it forever.
- Run Semgrep too and compare rule overlap with Bandit (three-way gap analysis: manual vs Bandit vs Semgrep).
- Convert Task 6 into an actual local script (`security-gate.sh` returning non-zero on HIGH) — direct seed for LAB-18.

## References and Safety Notes

- Bandit documentation: <https://bandit.readthedocs.io/>; Semgrep rules: <https://semgrep.dev/docs>.
- OWASP Top 10:2025 (A03 Injection, A02 Cryptographic Failures, A05 Security Misconfiguration); OWASP SAMM: <https://owaspsamm.org>.
- CWE Top 25: <https://cwe.mitre.org/top25>; OWASP *Input Validation* & *Secrets Management* Cheat Sheets: <https://cheatsheetseries.owasp.org>.
- Course: [M10](../../modules/module-10-secure-programming/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** the provided app is deliberately vulnerable training code — run only on `127.0.0.1` on your own machine, never deploy, never point scanners at systems you don't own (Safety Policy §3/§5). The seeded "API key" is a fake marker, not a credential; no real secrets appear anywhere.

**Navigation:** · [← Previous: LAB-08](../lab-08-firewall-config-audit/README.md) · [Lab index](../README.md) · [Next: LAB-10 →](../lab-10-web-security/README.md)
