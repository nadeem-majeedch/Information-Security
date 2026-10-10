---
title: "Module 11 Quiz — Threat Modeling and Security Architecture"
layout: default
---

# Module 11 Quiz — Threat Modeling and Security Architecture

**Type:** Formative knowledge check (completion gate) · **Questions:** 10 (6 multiple choice + 4 applied) + threat-model quality checklist (self-assessed) · **Pass mark:** ≥ 80% (8 of 10) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Applied answers should reference a concrete element (a DFD shape, a STRIDE category, a mitigation, a residual-risk statement).

**Coverage.** Maps to Module 11 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m11--threat-modeling-and-security-architecture)): DFDs with trust boundaries, STRIDE threat elicitation, risk-based prioritization, zero-trust evaluation.

**Related:** [Module 11 lesson](../../modules/module-11-threat-modeling-and-security-architecture/README.md) · [LAB-02 threat model & risk register](../../labs/lab-02-threat-model-risk-register/README.md) · [CS-2 case study](../case-studies/cs-2-product-launch-crypto-identity.md)

> **Safety reminder:** threat models use synthetic or fictional systems; if you model a real one, use public information only and share nothing sensitive. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (6)

**Q1.** In a data-flow diagram, a **trust boundary** marks:

- (a) Where the drawing tool changes colors
- (b) A change of privilege, ownership, or network zone — where data crosses between entities that don't fully trust each other
- (c) The edge of the diagram
- (d) Where encryption starts

**Q2.** STRIDE's **T**ampering refers to:

- (a) An attacker modifying data or code in transit, at rest, or in use
- (b) Destruction of hardware
- (c) Reading data without permission
- (d) Overloading a service

**Q3.** Repudiation (the **R** in STRIDE) means:

- (a) The network was routed incorrectly
- (b) A user can deny an action because there is insufficient evidence/auditing to prove they did it
- (c) Data was compressed
- (d) An account was suspended

**Q4.** Which pairing is correct?

- (a) Spoofing → authentication; Information Disclosure → encryption; Elevation of Privilege → authorization checks
- (b) Spoofing → firewall; Tampering → antivirus; DoS → backup
- (c) Spoofing → logging; Disclosure → compression; EoP → patching only
- (d) All STRIDE categories map to a single control type

**Q5.** A threat rated *high likelihood / low impact* and one rated *low likelihood / high impact* — a risk-based prioritizer should:

- (a) Always pick likelihood first
- (b) Compare them with a documented method (risk matrix / A×L with scales defined), decide with context (asset value, exposure), and record residual risk — not eyeball it
- (c) Ignore both; fix only technical issues
- (d) Pick whichever is cheapest to fix

**Q6.** "Never trust, always verify; least privilege; assume breach" describes:

- (a) Perimeter-only security
- (b) Zero trust architecture (NIST SP 800-207)
- (c) Air-gap isolation
- (d) Security through obscurity

## Part B — Applied (4)

**Q7. (Outcome 1 — DFD).** Draw (describe in words or sketch) a DFD for a food-ordering app: mobile client → API gateway → order service → database, plus payment provider (external) and admin console. Name every element type (external entity/process/data store/data flow) and **at least two trust boundaries**, justifying each.

**Q8. (Outcome 2 — STRIDE).** Apply STRIDE to *the order service* from Q7: give **at least 5 distinct threats**, each with its STRIDE category, the element attacked, and one concrete mitigation. (Full lab target: 15+ across the system.)

**Q9. (Outcome 3 — risk reasoning).** Your threat table has: T1 payment data exposed via missing authz (high impact, medium likelihood); T2 admin console brute-force (medium impact, high likelihood); T3 SQLi in order notes (high impact, low likelihood after parameterization applied). Rank all three by risk, state your mitigation decision for each (fix now / accept with control / monitor), and write one honest residual-risk sentence.

**Q10. (Outcome 4 — zero trust).** A legacy architecture: flat office network, VPN grants full subnet access, one shared admin account, implicit trust between services. Evaluate it against the three zero-trust tenets and propose three specific changes — one per tenet.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Boundaries mark privilege/network/ownership changes — they're where threats concentrate, so eliciting threats *per boundary* is the technique's engine. Misconceptions: (a)/(c) are drawing trivia; (d) encryption can exist *within* one zone — boundaries and crypto overlap only by design.

**Q2 — (a).** Tampering = unauthorized modification (integrity) in transit/at rest/in use. Misconceptions: (b) is availability/destruction; (c) is Information Disclosure; (d) is Denial of Service.

**Q3 — (b).** Without evidence (logs, signatures), a party can falsely deny an action — mitigations are auditing, signatures, non-repudiation services. Misconceptions: (a) routing trivia; (c) compression; (d) account lifecycle.

**Q4 — (a).** Each STRIDE category maps naturally to a *property*: spoofing→authentication, tampering→integrity, repudiation→non-repudiation/logging, info disclosure→confidentiality, DoS→availability, EoP→authorization. Misconceptions: (b)/(c) list unrelated controls; (d) is false — six categories, six distinct properties.

**Q5 — (b).** Prioritization requires *defined scales* and context (asset criticality, exposure, compensating controls); the matrix informs judgment, it doesn't replace it — and you document residual risk either way. Misconceptions: (a) likelihood-only ignores blast radius (ransomware shows why); (c) ignores half the threat model; (d) cost-driven prioritization isn't risk-driven.

**Q6 — (b).** Zero trust: authenticate/authorize every request regardless of network location, least-privilege per session, assume the network is already compromised. Misconceptions: (a) is the opposite (castle-and-moat); (c) isolation is a tactic, not the framework; (d) obscurity is explicitly rejected.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q7.** **External entities:** mobile client (user), payment provider (external), admin console operator. **Processes:** API gateway (entry/routing), order service (business logic). **Data stores:** order DB (internal), payment records (if stored — flag it), session/token store. **Data flows:** client→gateway (HTTPS requests), gateway→order service (internal RPC), order service→DB (SQL), order service→payment provider (outbound TLS — card/token data), admin console→order service (management ops), order service→client (order status). **Trust boundaries (≥2):** (1) *internet ↔ internal network* at the API gateway — untrusted public input crosses into services you operate; (2) *order service ↔ payment provider* — your trust ends at your perimeter; third-party risk and data-sharing terms begin; (3) *office/admin ↔ production services* — admin console access is a privilege change (also: guest Wi-Fi↔servers if the office LAN is flat). Each boundary is a mandatory stop on the STRIDE pass. → [LAB-02](../../labs/lab-02-threat-model-risk-register/README.md)

**Q8.** (S) **Order service accepts spoofed user tokens** → forgery of another user's orders → mitigate: validate JWT signature/issuer/expiry per request, reject `alg:none`. (T) **Admin command parameters tampered in transit** (if any internal hop is plaintext HTTP) → mitigate: TLS/mTLS on internal hops + integrity checks on payloads. (R) **Order modification cannot be attributed** (no audit trail) → mitigate: append-only audit log with actor, action, timestamp, hash chain. (I) **Payment/PII logged in clear** in order-service logs → mitigate: field-level redaction, tokenization, restricted log access. (D) **Order flood / large payload DoS** → mitigate: rate limiting, payload size caps, timeouts, backpressure. (E) **Order service → DB uses over-privileged shared credentials**, or IDOR lets user A read user B's order → mitigate: per-request authorization check, least-privilege DB account, parameterized queries. *(Accept any 5; bonus for distinct elements + boundaries.)*

**Q9.** Ranking with A×L (scales defined in your register): **T1** (H impact × M likelihood, PII/payment exposure + regulatory) → rank 1: fix now — server-side authz on every object + automated authorization tests; **T3** (H impact × L likelihood after parameterization) → rank 2: fix is already in place, so *verify* (regression test + WAF as depth) and monitor; **T2** (M impact × H likelihood of cheap automated attempts) → rank 3: mitigations are simple — rate limit + lockout/alerting + MFA on admin — implement fast but below the data-exposure fix. Residual-risk sentence (honest): *"After authorization tests and parameterization, the dominant residual risk in payments is third-party (payment provider) compromise and credential theft of admin accounts — accepted with MFA, rate limiting, and log alerting; re-review quarterly or after any payment-flow change."* Note: likelihood changed *because* of a control — always re-rate post-mitigation.

**Q10.** (1) **"Never trust, always verify" violated:** flat LAN + full-subnet VPN = network location *is* verification. Change: per-request authentication/authorization (identity-aware proxy or mTLS between services), segmented zones (M08 skills), VPN scoped per application/group instead of whole subnet. (2) **Least privilege violated:** shared admin account = everyone is maximally privileged and nobody is accountable. Change: individual accounts with RBAC, just-in-time elevation, MFA, and per-action audit — split duties (M07). (3) **Assume breach violated:** implicit inter-service trust means one pivot compromises everything. Change: service-to-service authn (mTLS/OIDC), deny-by-default microsegmentation between services, central logging + anomaly detection (M13) so lateral movement is visible. → [Module 11 lesson](../../modules/module-11-threat-modeling-and-security-architecture/README.md)

</details>

---

## Threat-model quality checklist (self-assessed — must pass before marking M11 complete)

Score each **Yes / No** with evidence. All "Yes" required:

1. DFD shows all four element types **and** ≥ 2 labeled trust boundaries with justification.
2. Every boundary and every element has been walked for STRIDE — not just the obvious ones.
3. ≥ 15 *distinct* threats (no rewordings of one threat), each mapped to a STRIDE category.
4. Every threat has a likelihood × impact rating with **defined scales** (state what H/M/L mean).
5. Every threat has a mitigation decision: fix / accept / transfer / avoid — and the *reason*.
6. ≥ 1 residual-risk statement written honestly (what remains and why it's tolerable).
7. 5+ abuse/misuse cases exist for auth and payment-adjacent flows, each mapped to a design change.
8. Zero-trust evaluation covers all three tenets with one concrete change each.

## Module-end review exercises (ungraded, harder)

1. **Full STRIDE model (practical).** Model your LMS/library/food-ordering system end-to-end: DFD → 15+ threats → mitigations → risk ranking. The checklist above is your grading instrument.
2. **Abuse-case clinic.** Write 5 abuse cases for a password-reset flow; for each, the design change it forces.
3. **Risk prioritization under constraints.** Same threat set, budget for only 4 fixes — choose, justify with risk reasoning, and state residual risk for what you deferred.
4. **Architecture comparison.** Review 2-tier vs 3-tier-with-API reference architectures through zero trust: which reduces which threats, which adds new ones (API surface)? One page.

*Review guidance:* threat models are graded on *distinctness and completeness of enumeration* — 15 rephrasings of "someone logs in wrongly" score like 3. Breadth across elements and boundaries is the skill.

**Next:** [Level 2 case study CS-2](../case-studies/cs-2-product-launch-crypto-identity.md) · **Previous:** [M10](./quiz-m10.md) · **Hub:** [Assessment Hub](../README.md)
