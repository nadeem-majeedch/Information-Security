---
title: "Module 10 Quiz — Secure Programming and Software Security"
layout: default
---

# Module 10 Quiz — Secure Programming and Software Security

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 code-review) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Code-review questions: name the weakness (CWE where possible), show the vulnerable line, give the fix as code, and state a test that proves the fix.

**Coverage.** Maps to Module 10 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m10--secure-programming-and-software-security)): secure SDLC, finding/fixing seeded weaknesses, SAST/SCA triage, memory-safety reasoning.

**Related:** [Module 10 lesson](../../modules/module-10-secure-programming/README.md) · [LAB-09 secure coding](../../labs/lab-09-secure-coding/README.md) · [LAB-09 vulnerable app](../../labs/lab-09-secure-coding/data/vulnerable_app.py) · [CS-2 case study](../case-studies/cs-2-product-launch-crypto-identity.md)

---

## Part A — Multiple choice (8)

**Q1.** In the secure SDLC, a security requirement written *before* design is most valuable because:

- (a) It makes later audits cheaper
- (b) Flaws prevented at design/requirements are orders of magnitude cheaper than those found in production
- (c) It satisfies a checkbox with no engineering cost
- (d) It replaces the need for code review

**Q2.** "Sanitization" vs "validation" — correct statement:

- (a) They are interchangeable terms
- (b) Validation checks input against an allowed pattern/allow-list before use; sanitization transforms/cleanses data for a specific output context — both context-dependent, neither a universal filter
- (c) Validation is for databases only
- (d) Sanitization means encrypting the input

**Q3.** Secret scanning (e.g., Gitleaks) found an API key in commit history. The correct response order is:

- (a) Delete the key from the current file only; done
- (b) Revoke/rotate the key first, then purge history, then add pre-commit/CI blocking — a key in history is already compromised
- (c) Rewrite git history first, then hope nobody fetched it
- (d) Ignore it; history is immutable

**Q4.** Which tool class finds "call `eval()` on user input" in *your* code?

- (a) SAST — static analysis of source without running it
- (b) DAST — scanning the running app from outside
- (c) Container image scanner
- (d) Dependency version checker

**Q5.** A CI pipeline fails because `npm audit` reports a critical vulnerability in a transitive dependency. Best first action:

- (a) Delete the audit step
- (b) Triage: is the vulnerable code path reachable in your app? Then upgrade/patch, or accept with documented rationale and a follow-up ticket
- (c) Downgrade npm
- (d) Ship and fix later without a ticket

**Q6.** The key risk of *unsafe deserialization* (e.g., unpickling untrusted data) is:

- (a) Slightly larger files
- (b) Attacker-controlled objects can trigger arbitrary code execution during reconstruction
- (c) Slower parsing
- (d) Encoding mismatches

**Q7.** Why do memory-safe languages (Rust, Go, safe Python/Java patterns) change the risk profile?

- (a) They eliminate all vulnerabilities
- (b) They eliminate whole CWE classes (buffer overflow, use-after-free) by construction, shifting residual risk to logic/authorization bugs
- (c) They make SAST unnecessary
- (d) They only improve performance

**Q8.** A mass-assignment vulnerability occurs when:

- (a) The server binds request JSON/form fields directly onto a model, letting the client set `role=admin` or `balance=...` fields it should never choose
- (b) Too many developers edit one file
- (c) The database has too many tables
- (d) Forms use POST instead of PUT

## Part B — Code review (4)

**Q9. (Outcome 2 — injection/path traversal).** Review:
```python
def read_note(user, name):
    path = "/notes/" + user + "/" + name
    return open(path).read()
```
Give two distinct weaknesses (with CWE), fix both in code, and one test per fix.

**Q10. (Outcome 2 — secrets & RNG).**
```javascript
const API_KEY = "sk-live-9f3a...";
const resetToken = require('crypto').prng ? Math.random().toString(36) : Math.random().toString(36);
```
Identify both flaws, the fix for each, and why `Math.random()` for a reset token is a security bug (not a style issue).

**Q11. (Outcome 3 — SAST triage).** Your SAST run reports: (1) `hardcoded-password` in a test fixture for a *local demo DB*; (2) `sql-injection` where a query uses string concatenation of a URL path param; (3) `weak-hash` on a non-security checksum used for cache-busting. For each: true positive / false positive (by context), severity, and action.

**Q12. (Outcome 4 — memory safety).** Explain in ≤ 6 sentences: what a heap use-after-free is, why bounds-checked languages prevent it, and one scenario where a "safe" language still suffers an equivalent class of bug (name it).

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Cost of fix rises dramatically down the lifecycle (requirements → design → code → prod) — prevention is the cheapest control. Misconceptions: (a) audit savings are secondary; (c) it's real engineering, not a checkbox; (d) requirements complement, never replace, code review.

**Q2 — (b).** Both are context-specific: validate to an allow-list for structure, then encode/sanitize for the *destination* context (HTML, SQL via parameters, shell via argv arrays). Misconceptions: (a) treating them as synonyms causes double-encoding bugs and false confidence; (c)/(d) are wrong definitions — SQL safety comes from parameterization, not "validation."

**Q3 — (b).** Assume compromise: rotate first (the key is live in every clone), then purge history (`git filter-repo`), then prevent recurrence (pre-commit hooks + CI secret scan). Misconceptions: (a) history retains it; (c) order matters — rewriting before rotating leaves the old key valid everywhere it leaked; (d) history is mutable *and* already distributed.

**Q4 — (a).** SAST inspects source/bytecode patterns (taint from input to sink) without execution. Misconceptions: (b) DAST sees behavior through HTTP but can't reliably point at the source line; (c) image CVEs, not code paths; (d) SCA covers third-party packages.

**Q5 — (b).** Reachability decides real risk: an audited vuln in an unused code path is lower urgency than a used one — but either way, patch or document acceptance. Misconceptions: (a) deletes your supply-chain early warning; (c) unrelated to the finding; (d) untracked debt on a *critical* finding.

**Q6 — (b).** Deserializers instantiate attacker-chosen classes/handlers, so gadget chains reach code execution (e.g., pickle RCE, Java gadget chains). Misconceptions: (a)/(c) are perf trivia; (d) is a bug, not the headline risk.

**Q7 — (b).** Whole bug classes disappear (CWE-119/416-family), so attacker ROI drops — but logic, authz, crypto-misuse, and dependency flaws remain. Misconceptions: (a) overclaims — safe languages don't stop injection-by-design or IDOR; (c) SAST still finds logic/API misuse; (d) performance is incidental.

**Q8 — (a).** Mass assignment = trusting the client's field list (OWASP A04 insecure design / CWE-915). Misconceptions: (b) merge conflict; (c) schema size; (d) HTTP verb is irrelevant.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** **(1) Path traversal** — `name = "../../etc/passwd"` escapes `/notes/<user>/` (CWE-22); user-controlled concatenation also crosses the intended user's directory (**broken access control/CWE-639** if user prefix is spoofable). **Fix:** resolve and containment-check:
```python
from pathlib import Path
def read_note(user, name):
    base = Path("/notes") / user
    p = (base / name).resolve()
    if not p.is_relative_to(base.resolve()):
        raise ValueError("path escapes note directory")
    return p.read_text()
```
Also allow-list `name` (`^[A-Za-z0-9_-]+$`). **Test:** `read_note("bob", "../../etc/passwd")` raises `ValueError` (400 to client); normal `read_note("bob", "hello.txt")` still works. **(2)** `open()` failure leaks absolute paths/tracebacks (CWE-209) — fix with generic error to client + logged detail server-side; test asserts response body contains no `/notes/` path. → [LAB-09](../../labs/lab-09-secure-coding/README.md)

**Q10.** **Flaw 1: hard-coded live secret** (CWE-798) — anyone with repo access (and anyone who ever clones history) owns the key; the second half of the snippet even *references* `prng` incorrectly, but the headline is: **Fix:** revoke/rotate now, load from env/secret manager (`process.env.API_KEY`), purge history, block with Gitleaks pre-commit/CI. **Flaw 2: `Math.random()` for a reset token** — it's a non-cryptographic PRNG (xorshift128+): outputs are *predictable from observed outputs*; an attacker who sees a few tokens can recover internal state and forge future reset tokens = **account takeover** (CWE-330/338). **Fix:** `crypto.randomBytes(32).toString('base64url')` (256-bit CSPRNG), stored hashed, single-use with short expiry. **Why security, not style:** style issues don't let attackers compute other users' tokens.

**Q11.** (1) **Context-limited false positive** (fixture credential for a local demo DB, not a live secret) — but still action: move to env/fixture builder so scanners stay trustworthy; severity low; ticket + suppression *with comment and expiry*, never a blanket ignore. (2) **True positive, high** — URL param concatenated into SQL = exploitable injection; fix: parameterized query + integration test with `'"--`; block the build. (3) **False positive for security** (cache-busting hash has no security property) — accept with rationale/suppression; severity none; no code change. Triage lesson: severity and action come from *context and reachability*, not the scanner's label alone.

**Q12.** A use-after-free: code frees (or drops the last reference to) a heap allocation, then reads/writes it again — the memory may have been reallocated to another object, so the stale pointer corrupts/reads foreign data; in C/C++ this is attacker-manageable and often code-execution (heap grooming). Memory-safe languages prevent it by construction: ownership/borrowing (Rust) or GC with no manual `free` (Go/Java/Python) means a reference can't outlive its object — invalidating the pointer class entirely. Equivalent residual risk in "safe" languages: **logical use-after-invalidation** — holding a stale *application-level* handle (an ID whose record was deleted or whose permissions changed) and acting on it: the memory is safe, the *authorization/consistency* is not; also **race conditions on shared state** (TOCTOU) survive in any language. Defense shifts to re-checking authorization/state at use time.

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Remediate 8 seeded weaknesses (practical).** Fix the 8 CWE classes in the course vulnerable app (injection, path traversal, hard-coded secrets, unsafe deserialization, weak RNG, SSRF, mass assignment, insecure upload) with before/after tests. Core M10 deliverable.
2. **Build the gate (pipeline analysis).** Wire Semgrep + Gitleaks + `pip-audit`/`npm audit` into a local CI-style script; plant a flaw, capture the *fail* log, fix it, capture the *pass* log. Deliverable: both logs + the workflow file.
3. **Risk prioritization.** SAST returned 42 findings: 1 high injection, 3 medium weak-crypto in dead code, 38 low style/info. Write your triage note: what you fix now, what you schedule, what you suppress — with rationale.
4. **Memory-safety explainer (investigation).** Run a tiny C program with a bounds error in an isolated VM (educational), observe the failure, and write a 200-word mitigation note (bounds checks, compiler mitigations, safe-language rewrite trade-offs).

*Review guidance:* a fix without a *test that fails before and passes after* is not evidence — this fail-then-pass discipline is exactly what the capstone's assessment stage demands.

**Next:** [M11 quiz](./quiz-m11.md) · **Previous:** [M09](./quiz-m09.md) · **Hub:** [Assessment Hub](../README.md)
