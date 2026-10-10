---
title: "CAP-ADV — Advanced Final Assessment"
layout: default
---

# CAP-ADV — Advanced Final Assessment

**Type:** Advanced final assessment (integrative, written) · **Spans:** all 19 modules · **Format:** open-book, unsupervised, time-boxed · **Suggested time:** 2.5 hours (one sitting preferred) · **Questions:** 20 (7 multiple choice + 13 constructed response) · **Total:** 45 points · **Suggested pass:** ≥ 70% (32 of 45 points) · **Unlimited retakes after 48h re-study**

**When to take it:** after M18, before or alongside the M19 capstone. It is the hardest *written* instrument in the course — it does not replace the capstone (which is practical) or the weighted components in the [Assessment Guide](../../assessment-guide.md); it stress-tests judgment across the whole curriculum.

**Instructions.**
1. Set a 2.5-hour timer. One sitting; open book (course pages, framework docs — no AI-generated answers if you want the score to mean something).
2. Answer **everything** before revealing any worked answers. The answers are collapsible and public *by design* (see the [student-answer policy](../README.md#student-facing-answer-policy--read-this)) — attempt first, then reveal, section by section.
3. Score as you go: **MCQ = 1 point each (7). Constructed response = graded with the point bands printed in each worked answer (38). Total 45.**
4. Self-assess honestly. A 70% earned by peeking first tells you nothing; the retake exists so the *first* attempt can be honest.

**Coverage:** maps to the course-level outcomes in [Learning Outcomes](../../learning-outcomes.md) — one or more questions per level, weighted toward *integration and judgment* rather than recall. Difficulty progresses within each section: comprehension → application → analysis → evaluation.

**Related:** [Assessment Hub](../README.md) · [CS-1](../case-studies/cs-1-breach-at-meridian.md) · [CS-2](../case-studies/cs-2-product-launch-crypto-identity.md) · [CS-3](../case-studies/cs-3-detection-to-response.md) · [CS-4](../case-studies/cs-4-cloud-privacy-automation.md) · [Capstone rubric](capstone-rubric.md)

> **Safety reminder:** this is a *written* assessment — no live targets involved. Where it asks you to plan testing, your plans must fit the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Section A — Foundations (M01–M05) · 7 points

**Q1. (MCQ, 1 pt)** A company pays a ransom and recovers data; a week later an auditor finds the *backup server* was also encrypted because it was domain-joined and always-on. The primary failure here is best described as:

- (a) Confidentiality only
- (b) Availability planning that ignored the assumption "backups must be outside the attacker's reach" (and integrity of the restored copy)
- (c) A cryptographic failure
- (d) An acceptable transfer decision

**Q2. (MCQ, 1 pt)** Under a 5×5 matrix, which pair of risks should be remediated first *when both must be fixed this month*?
- (a) Likelihood 1 × Impact 5; Likelihood 5 × Impact 1
- (b) Likelihood 3 × Impact 5; Likelihood 5 × Impact 3
- (c) They are equal; pick randomly
- (d) Neither — likelihood is irrelevant once impact is known

**Q3. (Constructed, 3 pts)** Given the `192.168.56.x` brute-force-to-`svc_backup` narrative from [CS-1](../case-studies/cs-1-breach-at-meridian.md): name the **two** endpoint/identity weaknesses that let a password guess become root, the **control type** of "watching the firewall logs," and one control from *each* type (preventive, detective, corrective) that you would implement. *(3 pts: 1 weakness pair, 1 correct control typing, 1 correct control per type.)*

**Q4. (Constructed, 2 pts)** Your office manager says: "Encryption solved — we enabled HTTPS, so our stored customer files are encrypted." Diagnose the two distinct category errors in one short paragraph. *(2 pts: 1 per error — transport vs. data-at-rest; a protocol vs. a storage state.)*

## Section B — Core technical (M06–M11) · 14 points

**Q5. (MCQ, 1 pt)** A teammate rotates the AES-GCM IV by *repeating* it across messages with the same key after the first 2⁴ messages. Most accurate consequence:
- (a) Only confidentiality degrades slightly
- (b) Nonce reuse under one key can expose the authentication key → forgeries become possible (catastrophic, not gradual)
- (c) Nothing; GCM ignores IVs
- (d) The key must be changed every message or the cipher stops

**Q6. (MCQ, 1 pt)** Which access-control change best embodies *separation of duties* for deployments?
- (a) Give the developer production deploy rights plus audit logging
- (b) Require two distinct roles: one may commit to main, a different one may approve the production release
- (c) Require a longer password for deploy accounts
- (d) Move deploy rights to a shared team account with logging

**Q7. (Configuration analysis, 3 pts)** Review this firewall excerpt for a 3-zone lab (`mgmt`, `work`, `lab`) and give three problems with one-line impacts, then a corrected principle (not necessarily every line):
```
1. allow work → any any
2. allow mgmt → lab any
3. allow lab → * any
4. deny * → * any
```
*(3 pts: 1 per valid problem — any-any over-permission / lab egress unconstrained / rule 4 unreachable or mgmt scope too wide / ordering issues; + corrected rule principle stated.)*

**Q8. (Practical investigation, 3 pts)** You find an IDOR returning other users' bookings on your own staging app. Give: OWASP category, the server-side fix pattern (one line of code-level intent), and **two** tests that would prevent its return — one functional, one automated-in-CI. *(3 pts: 1 category, 1 fix, 1 per test type.)*

**Q9. (Constructed, 3 pts)** Explain *why* "just add CSP" fails as the sole XSS defense, and "just add parameterized queries" can *still* leave an injection class open (name one example: e.g., second-order, ORDER BY/dynamic identifier, or NoSQL/operator injection). Two short paragraphs. *(3 pts: 1 CSP-is-depth-not-fix rationale, 1 correctly-named residual injection class, 1 sound overall reasoning.)*

**Q10. (Threat-model judgment, 3 pts)** Given a 2-tier design (web + DB in one subnet, flat office LAN, shared admin account), propose **three** changes, each mapped to a STRIDE category *and* a zero-trust tenet. *(3 pts: 1 per distinct change with correct dual-mapping.)*

## Section C — Assessment & defense (M12–M15) · 14 points

**Q11. (MCQ, 1 pt)** The correct *immediate* action when a live forensic host is discovered during monitoring is:
- (a) Power it off to stop the attacker
- (b) Capture volatile evidence (connections/processes/memory) before state-destroying actions, then isolate at the network
- (c) Start deleting malware files to help
- (d) Uninstall the AV so it stops interfering

**Q12. (MCQ, 1 pt)** Scanner says "CVE-X critical" on a host whose actual service banner doesn't match the vulnerable product. Correct classification and action:
- (a) False positive → exclude the rule permanently
- (b) True positive → escalate immediately
- (c) Unvalidated candidate → validate manually before it becomes a finding
- (d) Informational → report as an observation with critical severity

**Q13. (Log interpretation, 3 pts)** Given a log excerpt (use the pattern from [LAB-13](../../labs/lab-13-log-analysis/README.md) if you want a concrete dataset): identify the most suspicious *sequence* (not single line), state why sequence beats any individual line, and give verdict/severity/next action for it. *(3 pts: 1 correct sequence identification, 1 correlation rationale, 1 complete triad of verdict+severity+action.)*

**Q14. (Scope/ethics, 3 pts)** During an authorized assessment, a coworker asks you to check "one more host" not in the RoE, at 22:00. Give your decision, the document change required, and **two** harms an improvised scan could cause even on a friendly network. *(3 pts: 1 decision (decline pending amendment), 1 named document change, 2 harms.)*

**Q15. (IR sequencing, 3 pts)** Order and justify: restore-from-backup, eradicate persistence, capture memory, notify per plan, scope the incident, verify eradication. Flag the one ordering error that would guarantee a repeat incident. *(3 pts: 1 near-correct order, 1 justification of capture-early, 1 identification of restore-before-eradicate (or restore-before-scope) as the fatal error.)*

**Q16. (Malware-to-defense, 3 pts)** A training binary: writes `ProgramData\syscache.dat`, Run-key persistence, spawns encoded PowerShell, DNS to a lab domain. Provide 2 typed IOCs, 1 ATT&CK technique for persistence, and 1 Sigma rule *idea* whose conjunction keeps false positives low. *(3 pts: 2 correct typed IOCs, 1 correct technique ID, 1 precision-aware rule design.)*

## Section D — Advanced & integration (M16–M19) · 10 points

**Q17. (MCQ, 1 pt)** In SaaS, the customer remains responsible for:
- (a) Patching the vendor's app
- (b) Identity provisioning, access governance, and the data uploaded (including classification)
- (c) Physical security of the datacenter
- (d) Hypervisor isolation

**Q18. (Scenario judgment, 3 pts)** A proposed bot auto-deletes any public bucket, no human approval. Analyze with all three automation failure modes (name each as applicable/not), give one concrete wrong-fire scenario, and redesign the auto/human split. *(3 pts: 1 correct failure-mode analysis, 1 concrete scenario, 1 sound redesign.)*

**Q19. (Privacy, 3 pts)** An app wants to keep deleted users' messages "indefinite, for analytics." Name the principles violated, state the lawful alternative (what must actually be true), and the retention-schedule line you'd write for messages. *(3 pts: 1 principles (storage limitation/minimization), 1 lawful alternative (true anonymization with no re-identification path, or bounded retention with basis), 1 concrete schedule.)*

**Q20. (Integration capstone-preview, 3 pts)** For a 15-person startup scenario (web app + internal network, $0 budget): name the **first three artifacts** you'd produce in order across the course (from threat model → hardening → assessment → detection), and state the one *decision* that most determines whether the rest is well-targeted. *(3 pts: 1 coherent artifact sequence covering ≥ 3 stages, 1 correct identification of the pivotal decision (risk-based scoping/prioritization: what's in scope and what matters most), 1 for justified reasoning.)*

---

## Worked answers and scoring

<details>
<summary><b>Section A — answers (10 pts)</b></summary>

**Q1 — (b).** The ransomware lesson is that *reachability of backups* is the availability design assumption; an always-on domain-joined backup host is inside the attacker's blast radius (and restoration integrity is in question). Misconceptions: (a) the headline harm is you couldn't reliably recover — availability; (c) no crypto broke; (d) paying is not the analyzed control failure — the backup architecture is. *(1 pt)*

**Q2 — (b).** 3×5 = 15 vs 5×3 = 15 — equal scores, but (b) avoids the trap answers: (a) 5 vs 5 are the *lowest* total scores in the set (a 1×5 is rare; a 5×1 is annoying-but-cheap) — many candidates rank (a) first because a "5" is visible; (c) abdicates the matrix's purpose; (d) is false — both dimensions drive priority. Accept (b) with a score-based justification; full credit for the reasoning: *equal score → then use tiebreakers (exposure, asset value).* *(1 pt; 0 if picked without any reasoning when asked to justify.)*

**Q3.** **Two weaknesses:** (i) weak/guessable credential on a *privileged* service account (no MFA, no vaulting); (ii) over-broad `sudo` — a backup account able to run arbitrary commands as root (violating least privilege / separation of duties). **Control type for log-watching:** *detective*. **One per type:** preventive — vault a random service credential + restrict `sudoers` to the backup command (or disable password auth for service accounts); detective — alerting/triage on auth+firewall logs (threshold on failure bursts); corrective — tested offline 3-2-1 restore procedure + credential rotation playbook. *(3 pts: 1 (both weaknesses), 1 (detective), 1 (all three types correct).)*

**Q4.** Error 1: **category mismatch** — HTTPS encrypts data *in transit*, not files *at rest*; enabling TLS on the web server says nothing about the storage layer. Error 2: **protocol vs. state** — "encryption" as a property of stored files requires the storage/backup layer to be encrypted (with managed keys, at-rest settings), and even that protects only specific threat scenarios (stolen disk/offline access), not a logged-in attacker. One line: *transport protection ≠ data-at-rest protection, and neither is automatic — each is a separate configuration with separate threat coverage.* *(2 pts: 1 per error.)*

</details>

<details>
<summary><b>Section B — answers (14 pts)</b></summary>

**Q5 — (b).** GCM nonce reuse under one key is catastrophic: the GHASH authentication key can be recovered → attackers can *forge* authenticated messages. Misconceptions: (a) it's integrity failure first; (c) false; (d) not the mechanism. *(1 pt)*

**Q6 — (b).** Two *distinct* roles with no single actor able to both change code and release it — classic SoD. Misconceptions: (a) and (d) keep one identity able to act alone (shared accounts destroy accountability, defeating even the logging); (c) credential strength ≠ duty separation. *(1 pt)*

**Q7.** Problems (any three, 1 each with impact): (1) `allow work → any any` — full any-any from workstations: no segmentation, lateral movement unrestricted; (2) `allow lab → * any` — the attack lab can egress anywhere, including the internet: a compromised lab host becomes a pivot/C2 platform; (3) `allow mgmt → lab any` — management zone needs *specific services* (SSH/agent), not any port, into the most dangerous zone; (4) rule 4 is unreachable *if* a broader allow precedes it, and there's no explicit `established` handling or logging mentioned — deny-any must be the final implicit rule with logging. **Corrected principle:** default-deny, allow-by-exception: specific services mgmt→lab (tcp 22/443), lab→internet *blocked* (or explicit needed FQDNs only), work→internet tcp 443, state-return allowed, log denies — with blocked-flow tests for each zone pair. *(3 pts.)*

**Q8.** **Category:** OWASP Top 10:2025 **A01 Broken Access Control** (IDOR). **Fix intent:** server-side authorization on every object access — `if resource.owner_id != session.user_id: deny()` — via centralized middleware (never trust the client's `userId`). **Tests:** (functional) an authenticated request for *another* user's booking returns 403/404 (not 200 + data); (CI-automated) an authorization test matrix in the pipeline that replays each role × each object endpoint and fails the build on any 200-with-foreign-data — this is the M09/M10 "regression test" pattern wired to the gate. *(3 pts: 1 + 1 + 1.)*

**Q9.** CSP alone fails as sole XSS defense: it's *defense in depth* — bypassable via allowed origins (`'self'` hosting user content, JSONP endpoints, CDNs with user uploads), nonce/`'unsafe-inline'` legacy compromises, and it does nothing for non-browser sinks; it also can't fix the underlying unescaped output — the bug remains for other consumers (APIs, mobile clients), and header misconfig silently degrades it. Residual injection despite parameterized queries: **second-order injection** (data stored safely via parameters, later concatenated into a *different* query in a background job), **dynamic identifiers** (`ORDER BY`/table/column names can't be parameterized — need allow-lists), or **NoSQL operator injection** (`{"$gt": ""}` shapes where drivers don't support classic binds) — name one. *(3 pts: 1 depth-not-fix rationale, 1 named residual class, 1 coherent reasoning.)*

**Q10.** Three changes, each dual-mapped (1 each): (1) **Split web/DB into separate zones with a firewall allowing only the app's DB port** — STRIDE *Tampering/EoP* (a compromised web tier can't wander into the DB or LAN), zero-trust tenet **least privilege / microsegmentation**. (2) **Replace shared admin with individual accounts + MFA + just-in-time elevation, audit-logged** — STRIDE *Spoofing + Repudiation* (attribution restored), tenet **never trust, always verify** (every session authenticated per-request/step-up). (3) **Service-to-service authentication and per-request authorization on the app→DB path + central logging with alerting** — STRIDE *Elevation of Privilege / Information Disclosure* (implicit trust removed, lateral movement visible), tenet **assume breach** (detect and limit what an already-present attacker can reach). *(3 pts.)*

</details>

<details>
<summary><b>Section C — answers (14 pts)</b></summary>

**Q11 — (b).** Volatile-first: memory/sockets/processes die on power-off; network isolation preserves evidence while stopping the attacker. Misconceptions: (a) destroys the best evidence *and* may not stop C2-over-other-paths; (c) alters evidence and is remediation-before-analysis; (d) removes visibility. *(1 pt)*

**Q12 — (c).** Mismatched banner → the finding is an *unvalidated candidate*: validate (confirm version/CPE, safe probe in-lab) before it enters the report. Misconceptions: (a) skips validation; (b) "exclude the rule" hides future true hits; (d) contradictory — critical severity requires validation. *(1 pt)*

**Q13.** *(3 pts)* Using the LAB-13 pattern: the suspicious **sequence** is the failure burst → *success* from the same source (e.g., `192.168.56.105`: ~45 failures across many users incl. `svc_backup` → single success for `svc_backup` → subsequent sudo/`shadow` access). **Why sequence beats any line:** each line alone is explainable (failed logins happen; a success is normal; sudo is routine) — but the *ordered chain* from one source with a targeted-then-successful pattern is the intrusion signature; correlation across time+source+account turns events into an incident (M13's collect→correlate→detect). **Verdict/severity/action:** true positive, **high/critical** (privileged account, likely compromise + escalation), action: verify against RoE/asset list — if the source is *not* an authorized scanner, immediately isolate the host, preserve evidence (memory/logs), and escalate to IR per M14 (if it *is* your authorized scanner with a known window: benign-by-context, log with RoE reference — acceptable alternate if stated). *(1 sequence, 1 rationale, 1 triad.)*

**Q14.** **Decision:** decline — do not scan. Scope is defined by the RoE as written; time (22:00) is outside any stated window; verbal assurance ≠ authorization. **Document change:** written RoE amendment (target `10.x.x.x`, actions permitted, evening window, exclusions, stop conditions, countersign by accountable owner). **Two harms:** (i) legal/contractual — activity outside written scope can constitute unauthorized access regardless of ownership intent, voiding your engagement standing and possibly insurance/contracts; (ii) operational — an unscanned-config *surprise* (fragile legacy service, production-adjacent system, clinical/industrial controller) can be disrupted by port/vuln checks, causing outage or safety issues with no agreed stop-condition to bound it. *(3 pts: 1 + 1 + 2 harms.)*

**Q15.** **Order:** (1) **capture memory** (volatile evidence first — establishes running C2/process state), (2) **notify per plan** (clocks and people start), (3) **scope** (which hosts/data — informs containment breadth), (4) **eradicate persistence**, (5) **verify eradication** (rescan + IOC sweep + monitor), (6) **restore from backup** (known-good, tested, post-eradication only). *Capture before destructive change* justified: eradication destroys the proof of vector/scope. **Fatal error:** restoring (or "reimaging and calling it done") **before eradication/verification** — you restore into a live-compromised environment and watch the fresh copy get re-encrypted (ransomware watches restored files), guaranteeing a repeat; equally fatal: restoring before *scoping* if backups may share the compromise path. *(3 pts.)*

**Q16.** **IOCs (2 typed):** file — SHA-256 of `syscache.dat`/the dropper; registry — `HKCU\...\Run\WinSvchHelper` (or `SysCache`) value pointing at `ProgramData`; network — the lab DNS domain (bonus third). **ATT&CK:** **T1547.001** (Registry Run keys). **Sigma idea:** conjunction of registry-set *and* the specific value/path (`TargetObject endswith '\Run\SysCache'` AND `Details contains 'syscache.dat'`) — Run-key rules fire constantly; requiring the *specific value+path* (optionally + non-standard parent process) keeps precision high, and any allow-list entry must be hash/publisher-based with owner + expiry (names are spoofable). *(3 pts: 2 IOCs + 1 + 1 rule design → award 3 with all parts, 2 with a generic single-condition rule.)*

</details>

<details>
<summary><b>Section D — answers (10 pts)</b></summary>

**Q17 — (b).** Identity, access governance, and customer data (classification, sharing, retention) never move to the vendor. Misconceptions: (a)/(c)/(d) are provider responsibilities in every model. *(1 pt)*

**Q18.** **Failure modes:** *unsafe automation — applies, disqualifying as proposed* (deletion is irreversible); *alert fatigue — applies* (chat-posting every finding mutes the channel → the real payment-key alert is missed); *silent failure — applies* (scanner API rate-limit/token expiry → no deletions *and no alerts* → false coverage). **Wrong-fire scenario:** scanner flags the migration bucket mid-cutover (or a time-boxed exception SG rule) → bot deletes it → unrecoverable backup loss / outage during migration. **Redesign:** auto = open tickets, generate *proposed* fix PRs, enable block-public-access flags on empty/new resources, daily digest instead of per-finding spam; human-gated = anything destructive or service-affecting (bucket deletion, SG closure on live systems) with criticality check + rollback; reliability = heartbeat/dead-man on the bot itself, retry+backoff then *degraded* status, exit-code discipline, audit log of every action, scoped exclusions with owner+expiry. *(3 pts: 1 + 1 + 1.)*

**Q19.** **Principles violated:** storage limitation/retention (indefinite, no purpose-end), data minimization (no necessity test), purpose limitation ("analytics" as an open-ended secondary purpose), and — because messages are personal (possibly sensitive) — it also inflates breach impact for zero benefit. **Lawful alternative:** if kept, data must be **irreversibly anonymized** such that re-identification is not reasonably possible (k-anonymity-style aggregation, no unique users/links, documented method) — then it's outside personal-data scope; anything still linkable needs a lawful basis + bounded retention. **Retention line:** "Direct messages: purged 30 days after account deletion (and from backups on the ≤35-day backup aging schedule); aggregate, non-identifying usage statistics retained ≤12 months; deletion verified by monthly job audit with evidence in the retention log." *(3 pts: 1 + 1 + 1.)*

**Q20.** **Artifact sequence (in order):** (1) **threat model** — DFD with trust boundaries + ≥15 STRIDE threats with risk-ranked mitigations (M11) → *this sets scope and priority*; (2) **hardening/baseline evidence** — host + network + access-control implementation with before/after proof (M05/M07/M08, LC-1 style); (3) **authorized assessment report** — validate the implementation honestly, findings + remediation roadmap (M12/LC-3); then (4) **detections + triage/response evidence** proving detect→respond (M13–M15). *(1 for a coherent sequence covering ≥ 3 stages, 1 for including detection/response or assessment.)* **Pivotal decision:** the **risk-based scoping/prioritization** made in the threat model — *what's in scope, what matters most, what's accepted* — because every downstream artifact (what to harden, what to test, what to detect) is only as well-targeted as that ranking; get it wrong and you harden the wrong things *consistently*. *(1 for naming the decision + justified reasoning.)*

</details>

---

## Score interpretation

| Score | Band | What to do next |
|---|---|---|
| 39–45 (≥ 85%) | Distinction | Proceed confidently to the [M19 capstone](../../modules/module-19-integrated-capstone-project/README.md) with its [rubric](capstone-rubric.md) |
| 32–38 (70–84%) | Pass | Review missed areas by section, then start the capstone |
| 27–31 (60–69%) | Borderline | Re-study weak sections (use quiz links per section), retake after 48h |
| ≤ 26 (< 60%) | Not yet | Return to module quizzes (≥ 80% each) and level case studies first |

**After the attempt:** for every missed point, write one line — *which module's material would have answered it*. That list is your pre-capstone fix list.

**Next:** [Capstone Assessment Rubric](capstone-rubric.md) · **Hub:** [Assessment Hub](../README.md)
