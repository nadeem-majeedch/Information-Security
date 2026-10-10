---
title: "Module 07 Quiz — Identity, Authentication, Authorization, and Access Management"
layout: default
---

# Module 07 Quiz — Identity, Authentication, Authorization, and Access Management

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 scenario) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Scenario answers: 3–6 sentences, ending with a concrete control (name the standard or mechanism).

**Coverage.** Maps to Module 07 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m07--identity-authentication-authorization-and-access-management)): IAAA, authentication factors vs. NIST SP 800-63-4, least privilege/RBAC, SSO/OAuth flows.

**Related:** [Module 07 lesson](../../modules/module-07-identity-and-access-management/README.md) · [LAB-06 auth & access control](../../labs/lab-06-auth-access-control/README.md) · [CS-2 case study](../case-studies/cs-2-product-launch-crypto-identity.md)

> **Safety reminder:** IAM, MFA, and directory changes belong to lab VMs and local apps you own — never to production identity systems. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** A login page accepts the username but tells the attacker nothing else until the password is submitted. Which IAAA element failed when a *valid* username with a wrong password returns "no such user"?

- (a) Identification — the system never learns who you are
- (b) Authentication — the response leaks whether the account exists, enabling enumeration
- (c) Authorization — the user reached a page they shouldn't
- (d) Accounting — no log was written

**Q2.** Under NIST SP 800-63-4 thinking, the strongest phishing-resistant authenticator for a high-value login is:

- (a) SMS one-time code
- (b) Knowledge-based security questions
- (c) A passkey / FIDO2 hardware authenticator bound to the origin
- (d) A longer password with quarterly rotation

**Q3.** "Alice can read every file in Finance because she is in the Finance group" is an example of:

- (a) Mandatory access control
- (b) Role-based access control with a group-derived permission
- (c) Attribute-based access control
- (d) Discretionary access control exercised by Alice personally

**Q4.** Which statement about **least privilege** and **separation of duties** is correct?

- (a) They are the same control
- (b) Least privilege limits each account to what its task needs; separation of duties splits a sensitive operation across two or more people so one cannot act alone
- (c) Separation of duties means users may not share passwords
- (d) Least privilege applies only to root accounts

**Q5.** In an OAuth 2.0 / OIDC authorization-code flow, the **redirect URI** must be strictly validated because:

- (a) A loose allow-list lets an attacker receive the authorization code at their own URL and exchange it for tokens
- (b) It determines the encryption algorithm
- (c) It is where passwords are sent
- (d) It sets the session timeout

**Q6.** Which is the correct order of the IAAA concepts in a typical access attempt?

- (a) Authorization → Accounting → Authentication → Identification
- (b) Identification → Authentication → Authorization → Accounting
- (c) Authentication → Identification → Accounting → Authorization
- (d) Accounting → Identification → Authorization → Authentication

**Q7.** A JWT passed in a URL query string is problematic mainly because:

- (a) URLs are too short for tokens
- (b) Tokens in URLs leak via history, logs, and Referer headers, and query strings are commonly logged
- (c) JWTs cannot be validated in URLs
- (d) GET requests cannot carry headers

**Q8.** Recovery flows (account reset via email link) must be treated as authentication because:

- (a) Email is always the strongest factor
- (b) Whoever completes the reset *becomes* the account — so the reset link is effectively a temporary credential and must be single-use, time-limited, and non-enumerating
- (c) Reset flows are exempt from logging
- (d) They bypass the need for any identity proofing

## Part B — Scenario (4)

**Q9. (Outcome 1 — IAAA)** A web app shows every logged-in user an "Admin" button; clicking it returns `403`. The team says "users are authenticated, so IAAA is working." Identify which IAAA element is actually failing (or mis-implemented) and describe two concrete fixes.

**Q10. (Outcome 3 — RBAC)** Design a permission matrix for a 5-person team (founder, 2 developers, marketer, support) on a small file store + deployment system. Give roles, permissions (read/write/deploy/admin), and name one principle that prevents the marketer from shipping code.

**Q11. (Outcome 2 — MFA)** A startup wants "MFA for everyone" using SMS codes. Evaluate this choice against NIST SP 800-63-4 guidance, name a better option and a weaker-user fallback, and state one recovery-path risk to document.

**Q12. (Outcome 4 — OAuth)** During an OIDC login trace you notice the app accepts `redirect_uri=https://partner.example/anything` for *any* subdomain of `partner.example`, and the token response is logged in full. Give two vulnerabilities this creates and the corresponding fixes.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Differential responses ("user not found" vs. "wrong password") let an attacker enumerate valid accounts — an authentication flaw (and often CWE-204 observable discrepancy). Misconceptions: (a) identification did happen (username supplied); (c) authorization governs what you may *do* after login; (d) accounting is logging, orthogonal to the leak.

**Q2 — (c).** FIDO2/passkeys are origin-bound, so a phishing site cannot obtain a usable assertion — this is AAL3-class phishing resistance. Misconceptions: (a) SMS is interceptable (SIM swap, SS7) and phishable in real time; (b) knowledge-based questions are guessable/OSINT-able and deprecated by NIST; (d) rotation rules are out of favor and passwords remain phishable at any length.

**Q3 — (b).** Access derives from membership in a defined *role* (group), administered by the org — classic RBAC. Misconceptions: (d) would be DAC (owner decides); (a) MAC requires security labels/policy (e.g., clearance levels), not groups; (c) ABAC evaluates attributes (device, time, location), not just group membership.

**Q4 — (b).** Two distinct but complementary controls. Misconceptions: (a) overlapping goals, different mechanisms; (c) credential hygiene, not SoD; (d) least privilege applies to *every* account, service token, and process.

**Q5 — (a).** The redirect URI is where the code is delivered; a permissive matcher (prefix/substring/wildcard) means the code lands with an attacker who then exchanges it for tokens. Misconceptions: (b) algorithm is set elsewhere; (c) codes/passwords never go to redirect URI by design — that's the point; (d) session policy is unrelated.

**Q6 — (b).** You are *identified* (who), then *authenticated* (prove it), then *authorized* (what may you do), then *accounted* (what you did — audit trail). Misconceptions: all other orders break causality — you cannot authorize before knowing identity, and accounting follows the action.

**Q7 — (b).** URLs end up in browser history, proxy/web server logs, and Referer headers — tokens must live in headers/cookies with proper flags instead. Misconceptions: (a) length is not the issue; (c) they *can* be, which is precisely the danger; (d) irrelevant.

**Q8 — (b).** Possession of the reset channel equals account takeover, so the link must authenticate the requestor as strongly as practical: single-use, short expiry, no account enumeration, no session fixation. Misconceptions: (a) email is frequently the *weakest* link (reused passwords, mailbox takeover); (c) resets must be logged; (d) proofing still matters — NIST treats recovery as a same-or-stronger authenticator requirement.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** The 403 means authorization *is* being evaluated server-side — that part works. The failures are: (1) **information/design leakage** — the UI grants every user a view of an admin-only function, revealing role structure and inviting probing; (2) **client-trust risk if any state change is attempted client-side** — if buttons/menus were the only gate anywhere, authorization would be only cosmetic (broken access control, OWASP A01). Fixes: (a) enforce role checks in the UI *and* API (deny-by-default, server is the sole authority), hiding admin affordances for non-admins; (b) return a generic 403 without differentiating "exists but forbidden" vs "does not exist," log every attempt, and add automated authorization tests per role. → [Module 07 lesson](../../modules/module-07-identity-and-access-management/README.md), [LAB-06](../../labs/lab-06-auth-access-control/README.md)

**Q10.** Matrix (one valid design): **Founder** — read/write/deploy/admin (break-glass, with audit); **Developers (role: dev)** — read all code, write to code store, deploy to *staging only*; **Marketer (role: content)** — read/write to marketing folder only; **Support (role: support)** — read customer tickets, no code or infra access. Separation of duties prevents the marketer from shipping code: *deploy* is a permission granted only to the `dev`/`founder` roles, and four-eyes (SoD) can further require a second approver on production deploys. Least privilege is the default: every role starts with zero and gains only listed permissions; access is reviewed quarterly. → [LAB-06](../../labs/lab-06-auth-access-control/README.md)

**Q11.** SMS is a *restricted* authenticator under NIST SP 800-63-4: it is phishable in real time and vulnerable to SIM swapping/SS7 interception, so it cannot support AAL2 for higher-risk actions. Better: **passkeys/FIDO2 (phishing-resistant)** or an **authenticator app (TOTP/push)** as the primary factor. Fallback for users without smartphones: platform passkey or a hardware key, not SMS where avoidable; if SMS must remain, pair it with risk signals (new device, geo-implausibility) and step-up checks. Recovery-path risk to document: **email/reset-link takeover** — anyone controlling the mailbox can re-bind a new authenticator, so reset links must be single-use, time-limited, and themselves protected by MFA or identity proofing.

**Q12.** (1) **Loose redirect-URI matching → authorization-code interception.** A malicious page under any `partner.example` subdomain (or an attacker who takes over one) can capture the `code` and, if the client can't prove possession (no PKCE), exchange it for tokens. Fix: exact-match redirect URIs (no wildcards/subdomain patterns) **plus PKCE (`S256`)**. (2) **Token leakage via logs.** Full token responses in logs expose access/refresh tokens to anyone with log access (and to log-shipping pipelines). Fix: redact Authorization/token fields at the logging layer, keep tokens in memory/secure cookies, and set short lifetimes + rotation so stolen tokens age out. Secondary: validate `state`/`nonce` to block CSRF on the callback. → [Module 07 lesson](../../modules/module-07-identity-and-access-management/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

1. **RBAC verification (practical).** Implement a 4-role permission matrix on a Linux lab host (groups + ACLs) and prove it with `namei -l`, `getfacl`, and test logins as each role — show one *denied* case per role.
2. **Configuration analysis.** Given a real (redacted) OAuth client config with three flaws (wildcard redirect, no PKCE, infinite token lifetime), identify each, its impact, and the fix.
3. **Risk prioritization.** Rank by account-takeover risk: SMS-OTP at a bank, TOTP on a code repo, security questions on webmail, passkey on email — justify each line in one sentence.
4. **Practical investigation.** Trace a real OIDC login you perform (e.g., a provider offering OIDC) with browser dev tools: capture the authorization request, code, and redirect; annotate which parameters prevent tampering and which you'd add.

*Review guidance:* exercise 1 is the M07 portfolio deliverable's evidence form. In every written answer, name the mechanism — "add security" scores zero; "deny-by-default server-side role check with automated per-role tests" scores full.

**Next:** [M08 quiz](./quiz-m08.md) · **Previous:** [M06](./quiz-m06.md) · **Hub:** [Assessment Hub](../README.md)
