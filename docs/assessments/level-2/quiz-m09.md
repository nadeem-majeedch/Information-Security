---
title: "Module 09 Quiz — Web Application Security (OWASP Top 10:2025)"
layout: default
---

# Module 09 Quiz — Web Application Security (OWASP Top 10:2025)

**Type:** Formative knowledge check (completion gate) · **Questions:** 14 (10 multiple choice + 4 scenario-based) · **Pass mark:** ≥ 80% (12 of 14) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Scenario answers: identify the vulnerability class (OWASP Top 10:2025 where applicable), the root cause, impact, and at least one concrete prevention.

**Coverage.** Maps to Module 09 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m09--web-application-security-owasp-top-102025)): category/root-cause/prevention knowledge, hands-on vulnerability classes, report writing, ASVS/CVSS mapping.

**Related:** [Module 09 lesson](../../modules/module-09-web-application-security/README.md) · [LAB-10 web security](../../labs/lab-10-web-security/README.md) · [LAB-11 headers & TLS](../../labs/lab-11-headers-tls-analysis/README.md) · [CS-2 case study](../case-studies/cs-2-product-launch-crypto-identity.md)

> **Safety reminder:** every question here assumes testing against **local lab apps only** (Juice Shop, DVWA, WebGoat, your own). See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (10)

**Q1.** Attacker changes `GET /api/orders/1043` to `/api/orders/1044` and sees another customer's order. This is:

- (a) SQL injection
- (b) Broken access control / IDOR — the server trusts the object ID without an ownership check
- (c) Cross-site scripting
- (d) A misconfigured firewall

**Q2.** The most robust defense against SQL injection is:

- (a) Input filtering with a regular expression blacklist
- (b) Parameterized queries / prepared statements (separate code from data at the parser level)
- (c) Encoding quotes as HTML entities
- (d) Running the app as administrator so errors are hidden

**Q3.** Stored XSS differs from reflected XSS mainly in that:

- (a) Stored XSS persists on the server (e.g., in a comment) and executes for every visitor who views it
- (b) Reflected XSS only affects the attacker
- (c) Stored XSS is impossible with a framework
- (d) Reflected XSS requires SQL access

**Q4.** Which is the correct CSRF defense pairing?

- (a) An unpredictable per-session token submitted in a hidden field (or custom header), plus SameSite cookie flags — and relying on it *instead of* checking authorization
- (b) Only SameSite cookies, everywhere, with no token
- (c) HTTPS only — HTTPS completely prevents CSRF
- (d) Hiding the form with JavaScript

**Q5.** An image-storage endpoint fetches `http://internal-svc.local/admin/export` server-side on request. This is SSRF, and the highest-impact concern is:

- (a) Slow downloads
- (b) The server acting as a proxy into internal networks/metadata services the attacker can't reach directly
- (c) Broken images
- (d) Cookie leakage

**Q6.** `Content-Security-Policy: script-src 'self'` primarily mitigates which class?

- (a) SQL injection
- (b) XSS by restricting script sources to the app's own origin
- (c) CSRF alone
- (d) Clickjacking only

**Q7.** Which finding would you rate *highest* under a risk view (CVSS v4.0 as a starting point plus business context)?

- (a) Missing `X-Content-Type-Options` on a static brochure page
- (b) Authenticated SQL injection in a payment-history endpoint exposing card records
- (c) Verbose server banner version on an internal-only host
- (d) No favicon.ico

**Q8.** "Security misconfiguration" (OWASP Top 10) includes:

- (a) Default accounts/passwords left enabled, unnecessary features on, permissive CORS, directory listing
- (b) Using HTTPS
- (c) Storing passwords with bcrypt
- (d) Enabling audit logs

**Q9.** Which statement about dependency/vulnerable-component risk is correct?

- (a) Only the application's own code can be vulnerable
- (b) A vulnerable transitive dependency ships your risk to production even if your own code is flawless — mitigated by inventory (SBOM) and patching
- (c) `npm audit` results can always be safely ignored
- (d) Components are safe if they are popular

**Q10.** In a professional vulnerability report, the *impact* section should contain:

- (a) A CVSS string only
- (b) What an attacker gains and who is affected, in business terms plus technical scope — separate from reproduction steps and the fix
- (c) Marketing language about the vendor
- (d) The raw scanner output as attachment only

## Part B — Scenario-based (4)

**Q11. (Outcome 2/3 — access control).** While testing **your local Juice Shop**, you find that changing a `userId` in a profile API returns other users' email addresses without auth. Write the finding: class, root cause, step-by-step evidence (what you sent/received), impact, severity (CVSS v4.0 vector attempt + business note), and two fixes (immediate + design).

**Q12. (Outcome 1/2 — injection).** A lab app takes `?category=electronics` and shows a filter error when you append `' OR '1'='1`. Draft your validation tests that distinguish a real SQLi from a plain error message, then state the fix and one regression test to prevent recurrence.

**Q13. (Outcome 4 — ASVS mapping).** Map two findings to ASVS-style requirements: (a) no rate limiting on login; (b) session cookie missing `HttpOnly`/`Secure`. Give the ASVS chapter/verification area (e.g., V2 authentication, V3 session) and one sentence each on why it belongs there.

**Q14. (Outcome 1 — insecure design).** A "reset any user's password given their userID and mother's-maiden-name" feature passes all technical tests but is a design flaw. Identify the Top 10 category, why testing-only fixes (rate limits) are insufficient, and redesign the flow.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** IDOR is broken access control: the object reference is predictable and the server never proves the requester owns/ may read it. Misconceptions: (a) SQLi manipulates the *query* — here the query runs fine, the *authorization* is missing; (c) XSS targets browsers via injected script; (d) firewalls don't enforce object ownership.

**Q2 — (b).** Parameterization keeps data out of the SQL grammar entirely, so injected syntax is never parsed as code — robust against all current injection variants. Misconceptions: (a) blacklists are bypassable (encoding, comments, case, whitespace tricks); (c) HTML entities matter for HTML context, not SQL parsing; (d) hiding errors removes visibility, not the flaw (and running privileged worsens impact).

**Q3 — (a).** Stored (persistent) XSS is saved server-side and executes in victims' browsers later — broader blast radius than reflected (delivered via a crafted link to one target). Misconceptions: (b) reflected XSS harms whoever clicks the link, not the attacker; (c) frameworks help but storage sinks still require output encoding; (d) unrelated to SQL.

**Q4 — (a).** An unpredictable token bound to the session defeats cross-site forgery because the attacker's page can't read it; SameSite adds defense in depth. The option's final clause flags a common error — CSRF tokens don't replace authorization checks. Misconceptions: (b) SameSite is bypassable in older browsers/cross-site edge cases and should be layered, not sole; (c) HTTPS prevents eavesdropping, not the *browser-attached* forged request; (d) obscurity in JS is readable by the attacker's page.

**Q5 — (b).** SSRF turns the server into a requester against internal-only resources: admin panels, cloud metadata credentials (e.g., `169.254.169.254`), internal APIs. Misconceptions: (a) performance is the least of it; (c) an availability nuisance only; (d) cookies are the *client's*, not the target's — SSRF steals what the *server* can reach.

**Q6 — (b).** `script-src 'self'` blocks inline and third-party script injection — the core of XSS defense (pair with output encoding; CSP is defense in depth, not a replacement). Misconceptions: (a) SQLi is server-side parsing; (c) CSRF tokens/SameSite handle CSRF (CSP `form-action` helps but isn't primary); (d) `frame-ancestors` handles clickjacking.

**Q7 — (b).** Authenticated SQLi on payment data: high confidentiality impact, real business exposure (regulatory, customer harm). Misconceptions: (a) minor hardening gap on low-sensitivity content; (c) internal banner — low exposure without a reachable vuln; (d) trivial.

**Q8 — (a).** Classic misconfigurations: defaults, debug enabled, permissive CORS, directory listing, unnecessary ports. Misconceptions: (b)/(c)/(d) are security *improvements*.

**Q9 — (b).** Transitive dependencies are part of your attack surface — hence SBOMs, lockfiles, and `audit`/SCA in CI. Misconceptions: (a) libraries carry most code; (c) audit findings need triage, not blanket ignore (fix or accept with rationale); (d) popularity ≠ absence of vulns.

**Q10 — (b).** Impact = consequences: what data/actions an attacker gains, affected population, business and compliance fallout. Misconceptions: (a) a vector without meaning; (c) unprofessional; (d) evidence belongs in reproduction/appendix.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q11.** **Class:** Broken Access Control / IDOR (OWASP Top 10:2025 — A01). **Root cause:** server trusts client-supplied `userId` without an ownership/authorization check (mass assignment of query params). **Evidence:** intercept `GET /api/Users/<own-id>` (200, own data) → replay with `<other-id>` (200, other users' emails) → repeat with 3 sequential IDs; capture request/response pairs and note absence of auth token dependency. **Impact:** enumeration of all user emails → phishing/credential-stuffing fuel, privacy exposure of PII. **Severity:** CVSS v4.0 attempt `AV:N/AC:L/AT:N/PR:L/UI:N/VC:L/VI:N/VA:N/SC:N/SI:N/SA:N` ≈ 6.5–7.0 (low complexity, no privileges beyond a normal account, confidentiality low→high depending on fields) — raise with business context if emails + order history are exposed; note PII/regulatory angle. **Fixes:** immediate — enforce server-side `session.userId == resource.userId` (or role check) on every object access; design — opaque identifiers are *not* a fix, use centralized authorization middleware + automated per-endpoint authorization tests (ASVS V4.1). → [LAB-10](../../labs/lab-10-web-security/README.md)

**Q12.** **Validation tests:** (1) `?category=electronics'` → if *only* a generic error/warning appears with no data change, likely a handled error, not proof; (2) `?category=electronics' OR '1'='1` → returns *all* rows = injection influences query structure; (3) boolean differential: `...='1'='1` vs `...='1'='2` return different row counts → data-dependent behavior confirms SQLi; (4) time test `' OR SLEEP(5)--` (lab DB) → response delay indicates out-of-band evaluation; (5) confirm you're in scope (your Juice Shop only). **Fix:** parameterized query — `SELECT * FROM products WHERE category = ?` — plus least-privilege DB account and WAF as layer 2. **Regression test:** integration test submitting `'"--` and asserting (a) no 500s, (b) zero rows/results treated as literal input, (c) query log shows a bound parameter; wire into CI (ties to M10 pipeline).

**Q13.** (a) **No login rate limiting** → ASVS **V2 (Authentication)**, specifically password/authentication requirements (V2.2 area: anti-automation/brute-force protection): it belongs because unthrottled login attempts enable credential guessing/stuffing — an authentication-verifier property, not a session property. (b) **Cookie missing `HttpOnly`/`Secure`** → ASVS **V3 (Session Management)**: cookie flags are session-configuration requirements — `Secure` prevents transmission over clear HTTP, `HttpOnly` blocks exfiltration via injected script; both are baseline session protections. Bonus point: name that ASVS levels (1/2/3) decide whether the requirement applies to your app's context.

**Q14.** **Category:** Insecure Design (A04) — the *feature itself* is the flaw: security-question recovery with enumerable userID is an authentication bypass by design. **Why rate limits aren't enough:** they slow but don't fix — maiden names are OSINT-guessable, userIds are enumerable, and the channel bypasses the primary authenticator entirely; determined attackers still get account takeover at scale with distributed attempts. **Redesign:** eliminate knowledge-based recovery; use a time-limited, single-use reset link sent to a verified channel (email/app notification) with `state`/nonce binding; prefer passkey-based recovery or in-app approval; add non-enumerating responses, attempt logging with alerting, and step-up auth for sensitive changes; document in the threat model (M11) as an abuse case. → [Module 09 lesson](../../modules/module-09-web-application-security/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Juice Shop challenge run (practical investigation).** Solve 10 challenges across ≥ 5 Top 10 categories; log ID, category, technique, and request/response evidence. Core M09 portfolio deliverable.
2. **Report clinic (professional writing).** Convert 3 findings into full reports: summary, steps, evidence, impact, severity (CVSS v4.0 vector), remediation, ASVS reference. Grade each against the M09 report checklist.
3. **Risk prioritization.** Given 7 findings (missing header, IDOR, low-sev XSS, outdated lib, default creds, verbose errors, no rate limit), order them by remediation priority and justify with two factors each (exploitability + business impact).
4. **Configuration analysis.** Review your lab app's HTTP security headers (via [LAB-11](../../labs/lab-11-headers-tls-analysis/README.md)): list present/missing headers, what each missing one enables, and the exact header value you'd add.

*Review guidance:* every finding needs *evidence you captured yourself* — a scanner line alone is not evidence (that's the M12 false-positive lesson). Severity must combine a CVSS attempt with business context, never either alone.

**Next:** [M10 quiz](./quiz-m10.md) · **Previous:** [M08](./quiz-m08.md) · **Hub:** [Assessment Hub](../README.md)
