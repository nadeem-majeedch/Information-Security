---
title: "Case Study CS-4 — Cloud, Privacy, and Automation (Level 4)"
layout: default
---

# Case Study CS-4 — Cloud, Privacy, and Automation (Level 4)

**Type:** Cross-module case study (integrative, scenario-based) · **Spans:** Modules 16–18 · **Level:** 4 · **Estimated time:** 75 minutes · **Graded weight:** checkpoint (see [Assessment Guide §5.2](../../assessment-guide.md#52-scenario-exercise-rubric-component-b-per-scenario-20-points))

This case study fuses Level 4 — cloud/infrastructure security (M16), privacy/compliance/risk (M17), and security automation (M18) — into one migration decision. Work it **after** finishing M18.

**Instructions.** Read the scenario and answer all six questions before revealing the model answers. Questions 4–6 are *decisions* — justify each with risk reasoning. Self-assess against the rubric at the end.

**Related lessons:** [M16](../../modules/module-16-cloud-and-infrastructure-security/README.md) · [M17](../../modules/module-17-privacy-data-protection-and-compliance/README.md) · [M18](../../modules/module-18-security-automation-and-emerging-challenges/README.md)

---

## The scenario

**Tidewater Lettings** is a 12-person rental-agency moving from an office server to a cloud provider. Their plan, as written by the office manager:

1. **IaC:** a Terraform/compose bundle from a tutorial, including: DB port `0.0.0.0/0` ("temporary"), `admin_password = "changeme123"` in a variables file, an IAM user with `Action = "*"` ("to avoid permission errors"), and a storage bucket `tidewater-backups` with **public read** ("so the team can grab backups from anywhere").
2. **Container:** the new tenant-portal app image runs as root, `curl | bash` install, `.env` with the live payment-provider key in the image, `--privileged`.
3. **Data:** tenant records — names, addresses, **right-to-rent identity document scans**, financial references, and app telemetry. The migration plan says: "copy everything, keep it all, delete nothing — we might need it."
4. **Automation proposal:** "Auto-delete any public bucket or open security group the moment a scanner flags it — no approvals — and post results to the team chat."
5. **Incident:** during a trial migration, an engineer's laptop (with the backup decryption key in `.env`) is lost on a train. Records *may* have been on it. Nobody has told the DPO or the tenants.
6. **Emerging-tech idea:** leadership wants an AI assistant to read tenant emails and auto-draft tenancy renewals — starting next month.

All cloud resources are fictional; use provider **free tiers or local emulation only**, and never real tenant data in labs.

---

## Questions

**Q1 — Shared responsibility & hardening (M16).** For facts 1 and 2: identify every issue, assign the responsibility (customer/provider/shared where relevant), and give the fix. Which two are launch-blockers today?

**Q2 — Privacy & breach duty (M17).** Classify the data in fact 3. Then evaluate "copy everything, keep it all": which principles fail, what your retention plan should say per data class, and — for fact 5 — walk the breach-response steps in order (detection → assessment → notification logic → records), naming who must be told and when. Was the engineer's `.env` practice a *privacy* failure too, not just a security one?

**Q3 — Automation safety (M18).** Critique fact 4's auto-delete bot against the three failure modes (alert fatigue, silent failure, unsafe automation). Which failure applies most, with a concrete scenario of it firing wrong? Redesign the bot: what it may do automatically, what needs a human, and the reliability mechanisms it must have.

**Q4 — Prioritization (M16–M18).** The migration date is fixed in 3 weeks. Rank facts 1–5 as a remediation plan: what blocks launch, what ships with compensating controls, what proceeds in parallel. Justify each placement in one line (risk reasoning).

**Q5 — Data-driven AI decision (M17/M18).** For fact 6: give a go/no-go with conditions — data-protection gates (lawful basis, minimization, retention), security gates (the assistant's access scope, egress, injection handling per M18), and the automation failure modes that apply to *auto-drafting renewals*. What would you ship first instead, if anything?

**Q6 — Control mapping & metrics (M17/M18).** Map this engagement's work so far to **CSF 2.0 Functions** (Govern/Identify/Protect/Detect/Respond/Recover) — one line per function naming what you did or a gap. Then name 2 automation metrics you'd report monthly (beyond "alerts fired") and one guardrail metric proving your automation hasn't become a blind spot.

---

## Model answers

<details>
<summary><b>Q1 — Shared responsibility & hardening (M16)</b></summary>

**Fact 1 — Terraform/compose issues:** (a) **DB `0.0.0.0/0`** — customer responsibility; fix: bind private subnet + security group allowing only the app tier's IPs/security groups, and the DB engine's own auth. (b) **`admin_password` in variables file** — customer; fix: revoke/rotate `changeme123` *immediately* (it's in git history), move to the provider's secret store (or TF `${}` data source referencing secrets, never committed), `.gitignore` + secret scanning (Gitleaks). (c) **IAM `Action = "*"`** — customer; fix: scope to explicit actions/resources with conditions; least privilege is *your* side of shared responsibility even though IAM is "on the provider's platform." (d) **Public-read backups bucket** — customer; fix: Block Public Access at account level, private ACLs + signed URLs or an authenticated sharing path, encryption on, public-access alarm. **Fact 2 — image issues:** root user (fix: `USER app`, cap-drop, read-only rootfs), `curl | bash` (fix: pinned versions + checksums), **live payment key in image layers** (fix: *revoke/rotate the key first* — layers are permanent history — then inject at runtime via orchestrator secrets; `.dockerignore` the `.env`), `--privileged` (fix: remove; drop caps, resource limits, no host mounts). **Provider's half:** physical/hosts/hypervisor/managed-service patching, platform IAM *infrastructure*, and managed encryption machinery — you rely on their attestations; everything above the hypervisor in facts 1–2 is *yours*. **Two launch-blockers today:** (1) the **public backups bucket + plaintext DB password** — active, external exposure of tenant data before launch even happens; (2) the **`.env` payment key in the image** — a live financial credential in an artifact that will be pushed to registries and retained forever. Both are exploitable-now, cheap-to-fix, and unfixable-after-the-fact (rotate + rebuild). → [M16 lesson](../../modules/module-16-cloud-and-infrastructure-security/README.md) · [LAB-17](../../labs/lab-17-cloud-config-review/README.md)

</details>

<details>
<summary><b>Q2 — Privacy & breach duty (M17)</b></summary>

**Classification:** names/addresses = **personal**; right-to-rent document scans = **sensitive** (identity documents — fraud-target high-value tier); financial references = **sensitive/high-risk personal**; telemetry = **personal** (behavioral, linked to account). **"Copy everything, keep it all" fails:** **storage limitation/retention** (indefinite retention of sensitive data with no purpose-end — GDPR-style violation and pure breach-surface accumulation), **data minimization** (no necessity test passed), and it breaks **purpose limitation** ("might need it" is not a specified purpose) — and it inflates every risk score in the DPIA you haven't written yet. **Retention plan per class:** identity docs — collect for the statutory right-to-rent period, then delete (not archive); financial references — purpose-end + statutory retention (tax rules), then anonymize/delete; tenant contact records — tenancy end + legally required dispute window, then purge; telemetry — rolling window (e.g., 90 days) or aggregate-anonymize; backups — same schedules enforced by *backup aging* (a delete that doesn't reach backups isn't a delete), with documented verification. **Fact 5 breach steps in order:** (1) *detect & record* — timestamp of discovery (clocks start at **awareness**); (2) *contain* — remote-wipe/credential-revoke: the laptop key means rotate the backup decryption key and rotate any credentials in that `.env` *immediately*; (3) *assess* — was the `.env` actually on the device? full-disk encryption? what records did it unlock? likelihood/risk to tenants (this assessment determines the duty); (4) *notify logic* — DPO/internal accountable person **now** (same day, fact 5's silence is itself a process failure); if risk to rights/freedoms is non-trivial: **supervisory authority within 72h** of awareness; **affected tenants without undue delay** if high risk; document if not notifying (and why); (5) *record* — breach register entry: facts, assessment, decisions, evidence, follow-ups. **Was `.env` a privacy failure too?** Yes — privacy failures aren't only about *data handling choices*: putting the decryption key for *sensitive tenant records* on a movable device with no controls failed the **integrity/confidentiality safeguards** that privacy law requires you to have for that data class; the security lapse and the privacy obligation are the same event viewed from two sides (security is the control layer privacy depends on — M01/M17 link). → [M17 lesson](../../modules/module-17-privacy-data-protection-and-compliance/README.md)

</details>

<details>
<summary><b>Q3 — Automation safety (M18)</b></summary>

**Failure-mode critique:** **Unsafe automation — applies, and it's disqualifying as proposed.** Concrete wrong-fire scenario: the scanner flags the *migration* bucket while a teammate is mid-fix (or flags an SG rule that's a documented, time-boxed exception — e.g., a vendor sync window); the bot deletes the bucket → **irreversible data loss** (backups gone) and/or tears down the migration mid-cutover → outage — all *without a human*, and destruction of the very data the incident in fact 5 already endangered. Deleting storage is the *least reversible* action available to a bot; a false positive becomes unrecoverable loss. **Alert fatigue — applies second:** if the bot also *posts everything* to chat, the team drowns in public-SG chatter (tutorial templates are noisy), and they'll mute the channel — so when the *payment-key* finding posts, nobody sees it. **Silent failure — applies third:** the scanner's API rate-limits or the bot's token expires → no deletions, no errors visible → the team believes auto-remediation is on when it isn't (false coverage — the Q7 M18 lesson again). **Redesign:** *May do automatically (reversible + low-risk):* open **non-public** alerts, open tickets, generate a **proposed** fix PR, and apply *read-only* guardrails like enabling "block public access" flags **on empty/new resources**; auto-post **digests** (daily summary, not per-finding spam). *Requires a human:* anything **destructive or service-affecting** — deleting buckets, closing security groups on running systems, revoking access — gated behind confirmation with a rollback path and asset-criticality check (production = named approver). *Reliability mechanisms:* heartbeat/dead-man on the bot itself (silent-failure fix), retries with backoff for transient API errors (then *degraded* status, never fake success), non-zero exit codes, full audit log of every proposed/executed action, exclusions with owner+expiry (fatigue fix), and **reversibility policy**: prefer create/patch over delete whenever an alternative exists. → [M18 lesson](../../modules/module-18-security-automation-and-emerging-challenges/README.md)

</details>

<details>
<summary><b>Q4 — Prioritization (M16–M18)</b></summary>

**Blocks launch (must be done before any tenant data lands):** (fact 1b) **rotate & remove the plaintext DB password** + (fact 1d) **close the public bucket** + (fact 2, key) **revoke/rotate the leaked payment key & rebuild the image** — one line: these are live, externally reachable exposures of credentials/data; launch would be publishing a breach. Also (fact 1a) DB `0.0.0.0/0` → private before data flows — same reason: it's the data's front door. (fact 2 core) **non-root + no `--privileged`** — blocks launch: a container breakout at launch is trivially cheap for attackers and the fix is a rebuild, not a change window. **Ships with compensating controls (parallel-fix-this-week):** IAM wildcard → *scope to a documented interim policy* (tightly bounded actions + monitoring) if full least-privilege modeling needs time — compensate with access alarming and no long-lived keys (M16); `curl | bash` → pin versions in the same rebuild; **fact 3 retention** → *pilot* the deletion pipeline on telemetry first, full schedule within the statutory windows (nothing new collected under the old "keep everything" rule — collection freeze is immediate, deletion automation can ramp); **fact 4 bot** → ship the *alerting + proposed-PR* version now, destructive actions gated (Q3). **Proceeds in parallel (schedule, don't block):** DPIA completion + breach-register discipline (fact 5's process fix — the *notification* itself is immediate, the paperwork ramps); monthly automation metrics (Q6); AI-assistant gates (fact 6 — no-go until Q5 conditions met). **Justification logic:** *exploitable-now × data-at-stake first; irreversible-second; process/measurement next* — and anything with a legal clock (breach notification, collection freeze) is immediate regardless of rank.

</details>

<details>
<summary><b>Q5 — Data-driven AI decision (M17/M18)</b></summary>

**Verdict: NO-GO as proposed — conditional go only after gates pass; ship something smaller first.** *Data-protection gates:* lawful basis for reading tenant emails (contract-performance vs. consent — auto-processing of communications likely needs clear notice and probably opt-in), **minimization** (the assistant needs tenancy *facts*, not full mailbox history), purpose limitation (renewal drafting only — no marketing reuse), retention of model inputs/outputs defined, DPIA addendum for automated decision-making (renewals affecting housing = consequential), and human-readable disclosure to tenants. *Security gates:* least-privilege access scope (drafts-only, no *send* — and mailbox scope limited to renewal-related threads), egress allow-listing + human confirmation before any outbound message (the M18 prompt-injection control), treat model output as untrusted (no auto-execution, verify pulled dates/amounts against source of truth), full logging of model-assisted actions, vendor review (where does mail data go? training on it is a purpose violation unless separately agreed). *Automation failure modes:* **unsafe automation** — auto-*sending* a wrong renewal (wrong price/dates via hallucination) is a contractual/privacy harm with no rollback; **silent failure** — draft pipeline stops and renewals silently never get sent (housing deadlines!); **alert fatigue** — verification-review queue floods if every draft needs full re-check and reviewers rubber-stamp. **Ship first instead:** an *assistive* version — the assistant **summarizes** renewal candidates and **drafts** into a review queue where a human approves every send (human-in-the-loop from day one), with heartbeat on the queue (nothing sits >48h) and monthly checks of error rates in drafts. Automation of *sending* is a later milestone behind measured draft-accuracy — exactly the M18 principle: automate enrichment and reversible steps first, gate irreversible ones. → [M17 lesson](../../modules/module-17-privacy-data-protection-and-compliance/README.md) · [M18 lesson](../../modules/module-18-security-automation-and-emerging-challenges/README.md)

</details>

<details>
<summary><b>Q6 — Control mapping & metrics (M17/M18)</b></summary>

**CSF 2.0 map:** **Govern** — engagement ran under written scope/roles; *gap:* no formal data-governance policy yet (retention schedule missing until Q2) — fix via DPIA sign-off ownership. **Identify** — data inventory/classification (Q2) + asset review (facts 1–2); *gap:* full asset/data-flow map not yet built. **Protect** — hardening fixes (Q1), least privilege, key rotation, image rebuild, encryption on buckets. **Detect** — scanner + posture checks + proposed monitoring for public-access alarms; *gap:* runtime detection (M13-style) for the new cloud environment (flow logs/audit alerting) — noted as follow-up. **Respond** — breach handling for fact 5 (contain/assess/notify path). **Recover** — backup *integrity* work (decryption-key rotation, backup-aging alignment); *gap:* tested restoration of the new backups — schedule before cutover. **Two monthly automation metrics:** (1) **MTTD/MTTR for posture findings** — time from detection to *verified fix* per class (measures whether automation actually shortens the loop, not just fires); (2) **coverage** — % of assets/scopes covered by automated checks (exposes silent-failure drift when hosts/buckets fall out of scan scope). **Guardrail metric:** **automation health/false-action rate** — heartbeat uptime (missed runs) + count of automated actions *reverted* (wrong-fire ratio) + scoped-exclusion inventory with expiries. Together they answer: is it running (silent failure), is it right (unsafe), and is it tuned (fatigue) — the three failure modes as numbers. → [M17 lesson](../../modules/module-17-privacy-data-protection-and-compliance/README.md) · [M18 lesson](../../modules/module-18-security-automation-and-emerging-challenges/README.md)

</details>

---

## Rubric (self-assess)

| Criterion | Max | What a full-credit answer does |
|---|---|---|
| Technical accuracy | 8 | Correct responsibility assignment, principle names, failure-mode analysis |
| Prioritization & justification | 6 | Launch-blocker logic tied to exposure × data × irreversibility |
| Integration across modules | 3 | Links privacy ↔ security ↔ automation (breach clock, AI gates, metrics) |
| Clarity and structure | 3 | Organised, unambiguous |
| **Pass = ≥ 12/20** | | |

**Completion check:** all six answered; Q1 names both launch-blockers with rotation-before-rebuild ordering; Q2 walks breach steps with the 72h clock; Q3 redesigns the bot (auto vs. human split + reliability); Q5 gives conditional no-go with named gates.

**Next:** [CAP-ADV — Advanced Final Assessment](../final/advanced-final.md) · **Previous:** [M18 quiz](../level-4/quiz-m18.md) · **Hub:** [Assessment Hub](../README.md)
