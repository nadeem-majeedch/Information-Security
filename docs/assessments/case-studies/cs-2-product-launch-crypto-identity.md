---
title: "Case Study CS-2 — Ship It? Decisions at Launch (Level 2)"
layout: default
---

# Case Study CS-2 — Ship It? Decisions at Launch (Level 2)

**Type:** Cross-module case study (integrative, scenario-based) · **Spans:** Modules 06–11 · **Level:** 2 · **Estimated time:** 90 minutes · **Graded weight:** checkpoint (see [Assessment Guide §5.2](../../assessment-guide.md#52-scenario-exercise-rubric-component-b-per-scenario-20-points))

This case study fuses Level 2 — cryptography (M06), identity and access (M07), network defense (M08), web security (M09), secure programming (M10), and threat modeling (M11) — into one launch-week decision log. Work it **after** finishing M11.

**Instructions.** Read the scenario and answer all six questions before revealing the model answers. Questions 4–6 require a *decision* plus justification; you are graded on reasoning, not on matching a hidden answer. Self-assess against the rubric at the end.

**Related lessons:** [M06](../../modules/module-06-cryptography/README.md) · [M07](../../modules/module-07-identity-and-access-management/README.md) · [M08](../../modules/module-08-network-security/README.md) · [M09](../../modules/module-09-web-application-security/README.md) · [M10](../../modules/module-10-secure-programming/README.md) · [M11](../../modules/module-11-threat-modeling-and-security-architecture/README.md)

---

## The scenario

**Ferryline** is a 6-person startup building a ferry-booking web app. Launch is in 10 days. You are the security reviewer. The team hands you the following state of affairs:

1. **Passwords** are stored as unsalted SHA-256. The lead says "it's hashed, so we're fine."
2. **Sessions** are issued as JWTs with `alg: none` accepted as a convenience for internal tools, stored in `localStorage`, with 30-day expiry and no revocation list.
3. **Admin panel** at `/admin` is reachable from the public internet; login is username + password only, no rate limiting. The team plans "MFA later."
4. **The app** runs on one cloud VM; the firewall allows **SSH from 0.0.0.0/0** and HTTP/HTTPS. The DB port is bound to `0.0.0.0` but "firewalled."
5. During your test you find: (a) an IDOR on `/api/booking/<id>` — changing the id returns other users' bookings; (b) the search box reflects input unescaped (reflected XSS); (c) a webhook URL field that the server fetches server-side with no allow-list (SSRF).
6. **CI** runs no SAST, no dependency audit, no secret scan. One engineer has a live payment-provider key in a local `.env` that got committed once and was "removed from the latest file."
7. The **threat model** (from an intern) is a one-page diagram with boxes labeled "app" and "internet." No boundaries, no threats listed.
8. Marketing wants a **"friends leaderboard"** feature that reveals which ferry routes friends book. Product wants it for Friday.

Everything here is **fictional** on reserved lab addresses; your testing stayed on the team's local staging copy.

---

## Questions

**Q1 — Cryptography (M06).** Evaluate facts 1 and 2. For each: name the weakness (CWE or short name), why the current choice fails, and the correct replacement. For the JWT specifically, state what `alg: none` allows an attacker to do.

**Q2 — Identity and access (M07).** For facts 2 and 3, list the access-management failures and give a prioritized fix list. Which single change most reduces account-takeover risk this week, and why?

**Q3 — Network and web (M08/M09).** Map each of facts 4 and 5a–c to its OWASP Top 10:2025 category (or firewall principle for 4), state the concrete impact, and give one prevention each. For 5c (SSRF), name the highest-value internal target you'd worry about in a cloud VM.

**Q4 — Decision under constraint (M09/M10).** You have 10 days and cannot fix everything. Rank facts 1, 3, 5a, 5b, 5c by launch risk (justify each placement in one line), and name the two things you would *not* ship without — even if something else slips.

**Q5 — Secure SDLC (M10).** Design the minimum CI gate Ferryline can stand up in 10 days: which tools/checks, where they run, what fails the build, and how you handle a true positive found on day 8. Include the secret in fact 6: exact remediation order.

**Q6 — Threat modeling (M11).** Replace the intern's diagram: describe (or sketch) a DFD for the booking app with ≥ 2 trust boundaries, then give **5 STRIDE threats** across those boundaries, each with a mitigation. For fact 8 (the leaderboard feature), write one abuse case and the design change it forces.

---

## Model answers

<details>
<summary><b>Q1 — Cryptography (M06)</b></summary>

**Fact 1 — unsalted SHA-256 passwords.** Weakness: CWE-916 (password hash with insufficient work factor) plus missing salt. Fast, unsalted hashes fall to GPU cracking and precomputed rainbow tables; identical passwords produce identical hashes, so one crack reveals every reuse. Replacement: Argon2id (or bcrypt) with a per-user random salt and an appropriate work factor; migrate by re-hashing on next login plus a forced reset for weak/legacy entries. "It's hashed" is not a security statement — *how* it's hashed is.

**Fact 2 — JWTs with `alg: none`, in `localStorage`, 30 days, no revocation.** Three failures: (a) accepting `alg: none` means the server will validate a token the attacker simply *forged* with no signature — trivial privilege escalation to any user/admin (CWE-347: improper verification of cryptographic signature); (b) `localStorage` + XSS = token theft (see 5b — the two findings compound); (c) 30-day non-revocable tokens mean a stolen token is a 30-day key. Replacement: reject `alg: none` and pin the expected algorithm (HS256/RS256), short-lived access tokens (minutes) + rotating refresh, server-side revocation/logout, `HttpOnly; Secure; SameSite` cookies instead of `localStorage`, and audience/issuer/expiry validation.

→ [M06 lesson](../../modules/module-06-cryptography/README.md) · [M07 lesson](../../modules/module-07-identity-and-access-management/README.md)

</details>

<details>
<summary><b>Q2 — Identity and access (M07)</b></summary>

Failures: **(3)** public admin panel with no MFA and no rate limiting = credential-stuffing target (authentication anti-automation gap, NIST SP 800-63-4 would not carry it above AAL1); **(2)** long-lived revocable-less tokens = broken session management; **(4)** `SSH 0.0.0.0/0` = management plane exposed to the whole internet (authentication at network layer weakened to "know the password"); **(6)** shared live key in a commit = shared-secret hygiene failure (no rotation path).

**Prioritized fix list:** (1) rate-limit + lockout/alert on admin login *and* enable TOTP/passkey MFA on the admin role; (2) restrict SSH to VPN/bastion/office CIDR with key-only auth; (3) shorten and make tokens revocable (Q1 fix); (4) rotate the leaked payment key; (5) formalize roles (admin vs. staff vs. API) with server-side checks.

**Single highest-value change this week:** MFA + rate limiting on the admin panel (fact 3). Admin is the crown-jewel session: password-only, publicly reachable, unthrottled means one guessed/leaked password is instant full compromise, whereas the other fixes reduce blast radius or slow attackers. (Accept a well-argued SSH-first answer *if* it notes SSH brute-force exposure — the rubric wants the reasoning explicit.)

→ [M07 lesson](../../modules/module-07-identity-and-access-management/README.md) · [LAB-06](../../labs/lab-06-auth-access-control/README.md)

</details>

<details>
<summary><b>Q3 — Network and web (M08/M09)</b></summary>

**Fact 4 — firewall.** Violates deny-by-default / least privilege: `SSH from 0.0.0.0/0` exposes the management service globally (should be allow-listed to known CIDRs or a bastion, key-only); DB bound to `0.0.0.0` with "it's firewalled" is **defense-on-one-layer** — bind to `127.0.0.1`/private interface *and* restrict by security group, because one rule regression exposes the data. Prevention: explicit allow-list rules + local bind + verified blocked-flow tests.

**Fact 5a — IDOR.** Category **A01 Broken Access Control**. Impact: anyone reads/edits other users' bookings (PII, travel patterns, payment references). Prevention: server-side ownership check on every object (`session.userId == booking.userId` or role), centralized authorization middleware, automated per-endpoint authz tests.

**Fact 5b — reflected XSS.** Category **A03 Injection** (XSS). Impact: session/token theft (compounded by `localStorage` JWTs in fact 2), actions as the victim, defacement. Prevention: context-aware output encoding + templating that auto-escapes; CSP (`script-src 'self'`) as depth; avoid `innerHTML`.

**Fact 5c — SSRF.** Category **A10 Server-Side Request Forgery** (or insecure design A04 depending on framing — accept either with justification). Impact: the server becomes a proxy into private networks and, on a cloud VM, to **the instance metadata service (`169.254.169.254`)** — the highest-value target, since it hands out IAM/instance credentials. Prevention: strict URL allow-list (scheme + host), block link-local/private ranges, disable following redirects to internal hosts, use IMDSv2 with hop limits.

→ [M08 lesson](../../modules/module-08-network-security/README.md) · [M09 lesson](../../modules/module-09-web-application-security/README.md) · [LAB-10](../../labs/lab-10-web-security/README.md)

</details>

<details>
<summary><b>Q4 — Decision under constraint (M09/M10)</b></summary>

A defensible launch-risk ranking (justify one line each):

1. **5a IDOR** — actively exploitable by any logged-in user with no sophistication; reads all users' bookings = direct privacy/regulatory harm.
2. **Fact 1 password storage** — every existing credential is exposed the moment any copy of the DB leaks; fixes all current *and future* users, and cost is bounded (hash migration).
3. **Fact 3 admin panel** — internet-reachable, no MFA/rate-limit: high-impact but needs a valid password; MFA + throttling is a same-day control.
4. **5c SSRF** — serious (metadata credentials) but requires a reachable URL feature and craftier exploitation; mitigate with an allow-list quickly, harden fully post-launch.
5. **5b reflected XSS** — real, but needs to be delivered to a specific victim and the payoff rises with token theft; auto-escaping + CSP can land quickly; schedule full fix before feature-heavy pushes.

*(Accept alternative orders if impact × exploitability is argued; facts must each get a reason, not just a number.)*

**The two you would not ship without:** **5a access-control fix** (one ownership check + test — direct data exposure otherwise) and **fact 1 password re-hash migration** (protects every credential). Rationale: both are high-impact, low-effort, and hard to remediate *after* a breach — leaked hashes can't be un-leaked, and you can't retroactively prevent bookings already exposed. Rate-limiting admin (fact 3) is the next best candidate and should land the same week.

</details>

<details>
<summary><b>Q5 — Secure SDLC (M10)</b></summary>

**Minimum 10-day CI gate:**

- **SAST:** Semgrep (community ruleset + a few project rules) on every PR — fail the build on `high` findings.
- **Secret scanning:** Gitleaks as a pre-commit hook **and** CI step — fail on any detected credential.
- **Dependency audit:** `npm audit --audit-level=high` / `pip-audit` — fail on high/critical; require a documented accept with ticket otherwise (triage, not blanket-allow).
- **The team's own tests,** including the new authorization test for 5a and the escaping regression test for 5b.
- Optionally add Trivy for the container/VM image; the first four are the non-negotiable floor.

**Behavior:** runs on every PR; **red blocks merge**, findings list file + rule + severity; suppressions allowed only with comment + owner + expiry.

**Day-8 true positive handling:** reproduce → assess reachability/impact → fix in branch → test proves fail-then-pass → merge → if it was a live secret or exploited path, assume compromise: rotate/revoke first, check logs, then document in the release note.

**Fact 6 secret remediation order (exact):** (1) **Revoke/rotate** the payment key at the provider — the commit already distributed it, so treat it as compromised; (2) load the new key from environment/secret manager, never the repo; (3) **purge history** (`git filter-repo`) and force-push, coordinating with the team; (4) **add Gitleaks** pre-commit + CI so it can't recur; (5) verify no other committed secrets (`gitleaks detect --history`). Order matters: rotation before purge, because history rewrite doesn't un-leak a key that already left your machines.

→ [M10 lesson](../../modules/module-10-secure-programming/README.md) · [LAB-09](../../labs/lab-09-secure-coding/README.md)

</details>

<details>
<summary><b>Q6 — Threat modeling (M11)</b></summary>

**DFD:** *External entities:* passenger (browser/app), payment provider, ferry-operator partner API. *Processes:* web frontend, booking API, payment proxy. *Data stores:* bookings DB, sessions store. *Flows:* passenger→frontend (HTTPS), frontend→booking API, booking API→DB, booking API→payment provider, booking API→partner API. **Trust boundaries (≥2):** (1) public internet ↔ Ferryline's cloud VPC at the web tier — untrusted input crosses in; (2) Ferryline ↔ payment provider — third-party trust and cardholder data scope (PCI) begin; (3) app tier ↔ DB/private network — and admin/SSH access ↔ everything (management plane).

**Five STRIDE threats across those boundaries:**
1. **(S)** Attacker forges an `alg:none` admin JWT across boundary 1 → authenticate as admin → *mitigate:* pin algorithm, verify signature/iss/aud/exp, revoke on logout.
2. **(T)** Passenger tampers with a booking price/id in transit or via crafted request to the API → *mitigate:* server-side price recalculation, signed/validated payloads, parameterized queries + ownership checks.
3. **(I)** SSRF (5c) leaks instance metadata credentials → disclosure of cloud identity → *mitigate:* URL allow-list, IMDSv2, no internal ranges.
4. **(D)** Booking flood or huge search payload DoS at launch → *mitigate:* rate limiting, payload caps, timeouts, autoscaling limits.
5. **(E)** IDOR (5a) or over-permissive DB role lets a passenger reach another tenant's data / admin functions → *mitigate:* per-request authorization, least-privilege DB account, per-role automated tests.

**Fact 8 — leaderboard abuse case:** *"As an attacker, I search the leaderboard for a rival's email/route to learn their travel patterns, or I link my account to a colleague's to reveal all their bookings without consent."* → **Design change:** make participation strictly opt-in with granular visibility (routes shared vs. hidden), expose only aggregated or self-selected data, never PII-derived lookups by default, and default-new-users to *private* — this is a privacy-by-design/consent decision (ties to M17), reviewed before Friday.

→ [M11 lesson](../../modules/module-11-threat-modeling-and-security-architecture/README.md) · [LAB-02](../../labs/lab-02-threat-model-risk-register/README.md)

</details>

---

## Rubric (self-assess)

| Criterion | Max | What a full-credit answer does |
|---|---|---|
| Technical accuracy | 8 | Correct CWE/category/STRIDE mapping; fixes actually work |
| Prioritization & justification | 6 | Rankings tied to impact × exploitability, constraints acknowledged |
| Integration across modules | 4 | Links findings (e.g., XSS + localStorage JWTs; SSRF + metadata) |
| Clarity and structure | 2 | Organised, unambiguous |
| **Pass = ≥ 12/20** | | |

**Completion check:** all six answered with reasoning; Q4 ranks all five *with reasons* and names two non-negotiables; Q5 gives the exact secret-remediation order (rotate → purge → gate); Q6 has ≥ 2 boundaries, 5 distinct STRIDE threats with mitigations, and a leaderboard abuse case.

**Next:** [Level 3 case study CS-3](cs-3-detection-to-response.md) · **Previous:** [M11 quiz](../level-2/quiz-m11.md) · **Hub:** [Assessment Hub](../README.md)
