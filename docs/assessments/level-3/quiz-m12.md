---
title: "Module 12 Quiz — Vulnerability Assessment and Authorized Security Testing"
layout: default
---

# Module 12 Quiz — Vulnerability Assessment and Authorized Security Testing

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (7 multiple choice + 5 scenario/ethics questions, incl. 2 scope-boundary) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Scenario answers: 3–6 sentences ending in a concrete action. The ethics/scope questions have safety-critical answers — read them twice.

**Coverage.** Maps to Module 12 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m12--vulnerability-assessment-and-authorized-security-testing)): rules of engagement, phased authorized assessment, false-positive validation and prioritization, client-quality reporting.

**Related:** [Module 12 lesson](../../modules/module-12-vulnerability-assessment-and-security-testing/README.md) · [LAB-12 vuln-scan interpretation](../../labs/lab-12-vuln-scan-interpretation/README.md) · [LAB-14 IR tabletop](../../labs/lab-14-ir-tabletop/README.md) · [CS-3 case study](../case-studies/cs-3-detection-to-response.md)

> **Safety reminder:** every engagement question assumes a **written rules-of-engagement document and isolated lab targets** you own. Testing systems without authorization is illegal regardless of intent. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (7)

**Q1.** The correct phase order for a structured vulnerability assessment is:

- (a) Scanning → reconnaissance → reporting → validation
- (b) Rules of engagement → reconnaissance → scanning → validation → reporting → retest
- (c) Exploitation → scanning → reconnaissance → cleanup
- (d) Reporting → scanning → exploitation → rules of engagement

**Q2.** A scanner reports "CVE-2024-XXXX: possible remote code execution" on a service that banner-grabbed as an unrelated product version. Your first step is:

- (a) Report it as critical immediately
- (b) Validate manually — confirm the service/version actually matches the vulnerable component and, in the lab, test safely — before it enters the report as a finding
- (c) Ignore it; scanners are always wrong
- (d) Exploit it to be sure

**Q3.** Prioritizing findings by **CVSS base score alone** is insufficient because:

- (a) CVSS is too complicated
- (b) CVSS measures technical severity, not *your* environment's exposure, asset value, or compensating controls — business context moves the real priority
- (c) CVSS scores are always wrong
- (d) CVSS only applies to networks

**Q4.** A *false positive* in scanner output means:

- (a) A finding reported that does not actually exist in the target
- (b) A vulnerability that is critical
- (c) A finding you chose not to report
- (d) An alert with no log line

**Q5.** A good rules-of-engagement (RoE) document must include:

- (a) Only the scanner tool name
- (b) Scope (targets), authorization, timing/window, exclusions, stop conditions, and contacts
- (c) The report template
- (d) Passwords for the target systems

**Q6.** "The report's executive summary should…" —

- (a) List every CVE number first
- (b) State overall risk posture and top business impacts in plain language for a non-technical reader, with detail deferred to findings
- (c) Be written only in CVSS vectors
- (d) Omit remediation; that's the client's job

**Q7.** During an authorized assessment you discover a laptop with unrelated personal data. You should:

- (a) Copy it as extra evidence
- (b) Note the encounter, avoid accessing the data beyond what scope requires, and report the observation through your point of contact — data minimization applies even in scope
- (c) Delete it to be helpful
- (d) Ignore it entirely, since it's out of scope

## Part B — Scenario / ethics (5, incl. 2 scope-boundary)

**Q8. (Outcome 1 — scope boundary)** Your RoE authorizes scanning `192.168.56.0/24` **between 09:00–17:00 on lab hosts you own**. At 21:40 a colleague asks you to "quickly check" a new server — it's on a *different* subnet (`192.168.57.10`) outside the RoE but also a lab box. What do you do, and what document change does this require?

**Q9. (Outcome 1 — scope boundary)** Mid-assessment, an exploit you run causes the target web app to crash and stay down. The RoE has no stop-condition clause for availability impact. State your immediate actions (order matters), your notification duty, and what clause the RoE was missing.

**Q10. (Outcome 2 — phased assessment).** Plan the lab engagement for a 2-VM target (Metasploitable-class + Juice Shop): name the phases, one tool per phase (free), and one thing you must *record* in each phase for the final report.

**Q11. (Outcome 3 — validation clinic).** Given 4 raw scanner outputs, describe your validation method for each type: (a) "SSL/TLS supports TLS 1.0"; (b) "Apache 2.4.49 path traversal (CVE-2021-41773)"; (c) "Missing header: X-Frame-Options"; (d) "WordPress detected" on a server you know runs no WordPress. Mark likely TP/FP and the evidence that decides it.

**Q12. (Outcome 4 — reporting).** Outline the sections of a client-quality assessment report in order, and explain what distinguishes a *finding* from an *observation* — plus what the retest plan contains.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Authorization (RoE) first — nothing happens before written scope — then recon, scan, validate, report, retest. Misconceptions: (a) recon precedes scanning; (c) exploitation of live systems is never a phase without explicit authorization (and lab-only in this course); (d) report can't precede the work, and RoE must be first.

**Q2 — (b).** Validation eliminates false positives: confirm banner/version/CPE actually matches, check the plugin's logic, and (in-lab) verify safely. Misconceptions: (a) unvalidated criticals destroy report credibility; (c) "always wrong" is equally useless — scanners systematically *over*-report; (d) exploiting production systems without explicit authorization violates the RoE — validation ≠ exploitation.

**Q3 — (b).** Real priority = technical severity × exposure/asset value/compensating controls (business context). An internet-facing RCE beats an internal CVSS-9.8 on a segmented, monitored host. Misconceptions: (a) complexity isn't the objection; (c) CVSS is a fine *starting point*; (d) CVSS applies broadly.

**Q4 — (a).** Reported-but-not-real: wrong version match, unreachable code path, feature misread as vuln. Misconceptions: (b) describes severity; (c) describes an editorial decision (suppression); (d) describes a false *positive alert* in detection — related idea, different artifact.

**Q5 — (b).** Scope, authorization, timing, exclusions, stop conditions, contacts — the document that makes activity *authorized* and gives you safe abort rules. Misconceptions: (a) a tool is not authorization; (c) template belongs in the report plan; (d) credentials belong to target owners and are handled per secure channel — never casually in an RoE.

**Q6 — (b).** Exec summary = posture + top business impacts in plain language. Misconceptions: (a) CVE dumps are appendix material; (c) executives don't parse vectors; (d) remediation roadmap is a report deliverable (M12 outcome 4).

**Q7 — (b).** Data minimization: touch only what scope requires, document the encounter, notify your contact. Misconceptions: (a) copying unrelated personal data exceeds authorization (and may break privacy law); (c) destroying data is also outside scope; (d) total silence hides a possible hygiene issue for the owner.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q8.** **Do not scan yet.** Authorization is defined by the RoE *as written* — "also a lab box" and "your own" do not extend written scope; the time (21:40) is also outside the 09:00–17:00 window. Right action: pause; confirm with your point of contact / the authorizing owner; get a **written RoE amendment** (or a new short-form RoE) covering the `192.168.57.10` target, actions permitted, and an evening window; then proceed inside the amended scope and record the amendment with the engagement evidence. Lesson: scope changes are amendments, not improvisations — even for low-risk targets, because the discipline is the point and the habit is what transfers to real engagements. → [Lab Safety Policy](../../lab-safety-policy.md)

**Q9.** Immediate actions in order: (1) **stop testing** the crashing path — do not retry or "see if it comes back" with the same input; (2) attempt benign recovery only if it's within your authorized role (restart the service/VM snapshot), otherwise leave it; (3) **notify** your point of contact immediately and factually (what you ran, when, current state, impact); (4) document everything — timestamped command, output, notification — in the engagement log; (5) pause the assessment until the target owner confirms continuation. Missing clause: **stop conditions / safety-of-operations** — the RoE must state that any availability or stability impact halts testing pending owner sign-off, plus rollback provisions (snapshots taken pre-test). This is exactly why RoE clauses exist: not bureaucracy, but an agreed abort path. → [Module 12 lesson](../../modules/module-12-vulnerability-assessment-and-security-testing/README.md)

**Q10.** **Phase plan:** (1) *RoE/prepare* — record: signed scope, target list, snapshots of both VMs, timing. (2) *Reconnaissance* — `nmap -sV -sC` on lab IPs; record: hosts/ports/versions observed. (3) *Scanning/detection* — Greenbone/OpenVAS or `nmap` vuln scripts (`--script vuln`); record: raw scanner output per host. (4) *Validation* — manual confirmation of each candidate (safe checks, version proof, lab-safe PoC); record: TP/FP verdict + evidence line per finding. (5) *Prioritization* — CVSS v4.0 vector + business context; record: final severity + rationale. (6) *Reporting* — exec summary, findings, evidence, remediation roadmap; record: nothing new, but each finding traces back to phase evidence. (7) *Retest* — after fixes; record: retest date/result. Key: **every report line must be traceable to a recorded artifact from its phase.**

**Q11.** **(a) TLS 1.0 supported** — verify with `nmap --script ssl-enum-ciphers` or testssl.sh against the **lab** endpoint; check the handshake actually negotiates TLS 1.0. Likely **TP** if confirmed; note: config weakness (not CVE), severity depends on exposure/compliance (PCI deprecates it). **(b) CVE-2021-41773** — confirm the *exact* patched/unpatched build (`Server` banner + version), check the path-traversal is reachable without exploiting payload damage (a benign path probe in-lab); likely **TP** if 2.4.49 and module enabled; **FP** if version differs or the module is disabled. **(c) Missing X-Frame-Options** — check response headers directly (`curl -I`); **TP by definition if absent** — but severity is low (clickjacking exposure on non-sensitive pages), so a *true* finding ≠ a *high* one. **(d) "WordPress detected"** — look for `/wp-login.php`, `/wp-content/` responses; if 404/not-found and you know the stack, it's a **FP** (fingerprint confusion, e.g., a matching theme string) — record with evidence so the scanner's heuristic is corrected, not silently dropped. → [LAB-12](../../labs/lab-12-vuln-scan-interpretation/README.md)

**Q12.** Report order: **(1)** title page + engagement metadata (dates, scope, authorization reference); **(2)** executive summary — posture + top business risks in plain language; **(3)** methodology (phases, tools, versions, constraints); **(4)** findings — each with ID, title, severity (CVSS vector + context), affected asset, evidence, impact, remediation; **(5)** risk summary / severity distribution; **(6)** remediation roadmap with prioritized order and owners; **(7)** retest plan (scope of retest, method: same PoC safely re-run, pass criteria = verified-not-reproducible + evidence); **(8)** appendices (raw scan data, tools, RoE reference). **Finding vs observation:** a *finding* is a validated issue with evidence and remediation (it changes the risk picture); an *observation* is contextual information noted but not a validated vulnerability (e.g., "no WAF observed," "outdated banner with no confirmed CVE") — listed so nothing is silently dropped, without a severity. The retest plan names which findings will be re-verified, by what method, and what result closes each one. → [Module 12 lesson](../../modules/module-12-vulnerability-assessment-and-security-testing/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Scoped lab engagement (practical).** Full engagement on your isolated multi-VM lab: written RoE → scan → validate → rate → report → retest plan. Portfolio deliverable.
2. **False-positive clinic (log interpretation).** Take 8 raw scanner outputs (synthetic from LAB-12) and mark each TP/FP with the evidence line that decides it. Target: 7/8 correct.
   - **Format (per row):** `# | verdict (TP/FP) | deciding evidence line | action` — e.g. `3 | FP | Server banner: nginx 1.24, not Apache 2.4.49 | suppress with rationale, re-check version detection`.
   - **Evaluation criteria:** a verdict without the specific deciding evidence line (banner text, config line, header output, version string) does not count; FP suppressions must state scope and expiry; evidence must come from the dataset, not scanner confidence scores.
3. **Risk prioritization.** Given 10 validated findings with CVSS vectors *and* environment notes (internet-facing vs. internal, monitored vs. dark), produce a remediation order and one-line rationale per item — then explain where CVSS alone would have misled you.
4. **Practical investigation.** Write a 1-page RoE for a new 3-host lab, including an explicit stop-condition clause (availability impact → halt → notify → owner sign-off) — the clause missing in Q9.

*Review guidance:* exercise 1 is the M12 portfolio core. The report is graded on *traceability* — every severity line must point to recorded evidence, and unvalidated scanner output must never appear as a finding.

**Next:** [M13 quiz](./quiz-m13.md) · **Previous:** [M11 quiz](../level-2/quiz-m11.md) · **Hub:** [Assessment Hub](../README.md)
