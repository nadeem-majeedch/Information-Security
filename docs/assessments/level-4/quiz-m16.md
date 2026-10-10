---
title: "Module 16 Quiz — Cloud and Infrastructure Security"
layout: default
---

# Module 16 Quiz — Cloud and Infrastructure Security

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 scenario/shared-responsibility) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Scenario answers: assign responsibility *explicitly* (customer / provider / shared), then give the control.

**Coverage.** Maps to Module 16 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m16--cloud-and-infrastructure-security)): shared responsibility, container hardening, IaC security, cloud risk evaluation.

**Related:** [Module 16 lesson](../../modules/module-16-cloud-and-infrastructure-security/README.md) · [LAB-17 cloud config review](../../labs/lab-17-cloud-config-review/README.md) · [LAB-09 secure coding](../../labs/lab-09-secure-coding/README.md) · [CS-4 case study](../case-studies/cs-4-cloud-privacy-automation.md)

> **Safety reminder:** cloud and container work happens only on accounts you own (free tier) or local emulation, with no real tenant data. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** Under the shared responsibility model, moving from on-prem to **IaaS** shifts to the *provider*:

- (a) Physical security, hypervisor, and the host OS
- (b) Your application's input validation
- (c) Your IAM policies and security groups
- (d) Your data classification decisions

**Q2.** The #1 real-world cloud breach enabler is most often:

- (a) Provider hypervisor escape
- (b) Customer misconfiguration: public storage buckets, over-permissive roles, open security groups, no logging
- (c) Quantum computing
- (d) Provider billing errors

**Q3.** A container image should run as non-root because:

- (a) It starts faster
- (b) A container breakout or command execution inherits that user — root inside the container maximizes what an attacker can do toward the boundary
- (c) Root is only needed on Windows
- (d) Non-root disables logging

**Q4.** `docker run --privileged` with a host path mount is dangerous because:

- (a) It slows the container
- (b) It grants near-host device/capability access and direct host filesystem reach — container isolation effectively collapses
- (c) It violates naming conventions
- (d) It prevents image scanning

**Q5.** Secrets committed to an image layer (even if later "deleted" in a later layer) are exposed because:

- (a) Docker caches builds
- (b) Image layers are append-only and inspectable — deletion in a new layer doesn't erase the earlier layer's content
- (c) Scanners only read layer 1
- (d) Secrets become public automatically

**Q6.** **IaC scanning** (Checkov/Trivy config) catches:

- (a) Only runtime memory bugs
- (b) Misconfigurations in Terraform/Compose *before* deploy — open security groups, public buckets, plaintext secrets, privileged containers
- (c) Only license issues
- (d) Nothing; IaC is always safe

**Q7.** Which is a *customer* responsibility even in **SaaS**?

- (a) Patching the vendor's application
- (b) Securing user identities/SSO, access provisioning, and the data you upload — plus who can see what
- (c) The provider's physical datacenter
- (d) Hypervisor isolation

**Q8.** Centralized, tamper-resistant logging in a cloud account matters most because:

- (a) Logs are pretty
- (b) Attackers routinely disable local/instance logging first; an account-level (provider-managed) audit trail outlives instance tampering and is the backbone of detection and forensics
- (c) It is always legally required everywhere
- (d) It replaces encryption

## Part B — Scenario / shared-responsibility (4)

**Q9.** Assign responsibility (provider / customer / shared) and name one customer control for each: (a) patching the hypervisor; (b) an S3-style bucket left public with PII; (c) a VM's guest OS unpatched; (d) encryption of data at rest in a managed database.

**Q10.** A team plans to ship a container that: runs as root, has `curl | bash` baked into the build, contains a `.env` with a live API key, runs with `--privileged`, and maps port 8080. Give 4 concrete hardening changes (one per real problem) plus the scan you'd run to prove improvement.

**Q11.** Given a provided Terraform/Compose config with 8 seeded issues (public ingress `0.0.0.0/0` on DB port, plaintext password in variable, host mount of `/`, privileged mode, no resource limits, wildcard IAM `*` actions, untagged/unrotated secrets, no encryption flag) — describe your review method (tool + manual pass), and how you'd prioritize fixes by risk.

**Q12.** Evaluate: *"Our data is in the cloud, so the provider is responsible for its security."* Correct the model, then give the three cloud-specific risks you'd check first in an account you've just inherited (misconfiguration, over-permissive identity, logging gaps) with one concrete check each.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (a).** IaaS: provider runs physical + virtualization layers; the guest OS *up* (including config, IAM, apps, data) stays with the customer. Misconceptions: (b)/(c)/(d) are all customer-side — that's the point of the model.

**Q2 — (b).** Industry post-mortems (Verizon DBIR, cloud security reports) repeatedly show misconfiguration and identity errors dominate — not exotic hypervisor attacks. Misconceptions: (a) real but rare; (c) not a current breach vector; (d) a billing problem, not a breach enabler.

**Q3 — (b).** Least privilege *inside* the boundary: UID 0 in a container can often be mapped to/influence host resources more easily, and any RCE starts at maximum privilege. Misconceptions: (a) unrelated; (c) irrelevant; (d) false — logging is independent of user.

**Q4 — (b).** `--privileged` + host mounts hands the container device access, capabilities, and host filesystem — the isolation that justifies containers is gone. Misconceptions: (a) minor perf effects aren't the issue; (c) conventions don't secure systems; (d) scanning still works, it just reports while you ship anyway.

**Q5 — (b).** Layers are immutable history: `docker history` / `docker save` reveals earlier layers — hence "never build secrets in; inject at runtime (env/secret mount)." Misconceptions: (a) caching preserves builds but isn't the root cause; (c) scanners walk layers; (d) no auto-redaction exists.

**Q6 — (b).** Shift-left config linting: policy-as-code catches the misconfig classes *before* they exist in production. Misconceptions: (a) that's SAST/SCA for code; (c) licensing is separate tooling; (d) false — that's what the tool exists for.

**Q7 — (b).** Even SaaS: *your* identities, entitlements, data, and sharing settings are yours — the vendor runs their app only. Misconceptions: (a)/(c)/(d) are provider responsibilities in every model.

**Q8 — (b).** Detection's first casualty is the local log: attackers wipe instance logs; account-level trails (flow logs, audit trails, object-lock) are out of the instance's reach — enabling MTTD/MTTR (M13) and post-incident timelines (M14). Misconceptions: (c) regulations vary; (d) logging and encryption solve different properties.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** (a) **Provider** — hypervisor patching is squarely theirs in every service model; (customer control: *choose* providers with transparent compliance attestations, and patch your guest OS so the shared seam stays strong). (b) **Customer** — the bucket policy/ACL is yours; **control:** block public access at the account level, enforce encryption + least-privilege bucket policies, and enable public-access alerting. (c) **Customer** — guest OS patching never moves; **control:** patch management/automation (M05 skills) or move to managed/immutable images rebuilt weekly. (d) **Shared** — managed DB: *provider* runs the encryption mechanism and key storage infrastructure, *customer* enables it, chooses key management (provider KMS vs. customer-managed/HYOK), and controls who can decrypt; **control:** enforce `storage_encrypted=true` and restrict KMS key policies/CI wrap. → [Module 16 lesson](../../modules/module-16-cloud-and-infrastructure-security/README.md)

**Q10.** (1) **Runs as root** → add `USER app` (dedicated non-root UID), `USER` directive *after* dependency copy, verify with `docker exec … id` → UID ≠ 0; also drop capabilities (`--cap-drop ALL` + minimal adds). (2) **`curl | bash` in build** → remove pipe-to-shell; pin exact versions + checksums of installers (supply-chain hygiene; this is also an SBOM/reproducibility win). (3) **Live `.env` in image** → revoke/rotate the key *now* (it's in layers), purge from history/rebuild context via `.dockerignore`, inject at runtime via orchestrator secrets/env — never bake credentials. (4) **`--privileged`** → remove it; use read-only rootfs (`--read-only` + tmpfs for writes), no host mounts, resource limits (`--memory`, `--cpus`), drop all caps, and allow-list needed syscalls; keep port mapping as-is (8080 is fine). **Proof scan:** rebuild then `trivy image <name>` (OS + library CVEs) + `trivy config .` (IaC/compose misconfigs) — capture before/after reports showing privilege/secret findings removed and CVE list reduced; add the scans to the M10 CI gate.

**Q11.** **Method:** (1) automated pass — `checkov`/`trivy config` (or `tfsec`) over the IaC to enumerate policy violations with IDs (e.g., `CKV_AWS_20` public ACL, `CKV_DOCKER_2` privileged); (2) manual pass — read the module/flow: trust boundaries, data classification of what flows through, identity bindings, whether defaults were overridden in *other* files (compose overrides, workspaces); (3) map each finding to a control owner and to CIS-benchmark style checks. **Prioritization by risk:** rank = exposure × impact of the asset — (i) *public DB ingress `0.0.0.0/0` + plaintext password* = top (internet-facing + credential): restrict to app tier/security-group refs + move secret to secret store + rotate; (ii) *wildcard IAM `Action:*` + `Resource:*`* = second (any identity compromise = full account): scope to explicit actions/resources, add conditions; (iii) *host `/` mount + privileged* = third (breakout reach): remove/mount named volumes, drop privileged, limits; (iv) *no encryption flag / unrotated secrets* = next (protective controls & hygiene): enable encryption, secret rotation lifecycle. Rationale: fix what an *external or already-in* attacker reaches first (network+identity), then containment (container isolation), then hygiene. → [LAB-17](../../labs/lab-17-cloud-config-review/README.md)

**Q12.** **Correction:** security is *shared and, for your data, mostly yours* — the provider secures "of the cloud" (infra, hypervisor, facilities, managed-service software); you secure "in the cloud" (identities, network exposure, configuration, your data, your app). "Their security" covers the platform's integrity, not your bucket's ACL or your admin's MFA. **Three first checks:** (1) *Misconfiguration* — run a posture scanner (Prowler/ScoutSuite/CIS tool) and manually check public storage/exposure (`list-buckets` + policy check; security groups `0.0.0.0/0` on 22/3389): verify nothing sensitive is public and encryption is on. (2) *Over-permissive identity* — enumerate users/roles/policies for wildcard `*` actions/resources, unused keys >90 days, no-MFA admins: apply least privilege, enforce MFA, enable credential-report review. (3) *Logging gaps* — confirm account-level audit + VPC flow + storage access logs are **on, centralized, and retention-set** (and that *you* can't be silently logged-off): no logging = no detection (M13) and no forensics (M14) when (1) or (2) pays off. → [LAB-17](../../labs/lab-17-cloud-config-review/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Container hardening (practical).** Take a vulnerable container image, produce a hardened derivative (non-root, no secrets, no privileged, resource limits, read-only where feasible), scan with Trivy showing clean/near-clean before/after. M16 deliverable.
2. **IaC review clinic (configuration analysis).** Audit the provided Compose/Terraform config for the 8 issues, fix each, rescan — with before/after tool output as evidence.
3. **Cloud design review (investigation).** Assess the reference architecture (static site + API + storage) against a CIS-inspired checklist: produce a findings list with risk ratings and one-line fixes. Optional: reproduce *one* item on a free-tier account **you control**.
4. **Risk prioritization.** An inherited account has: public bucket with backups, IAM admin key on a developer laptop, no flow logs, 12 unpatched VMs. Order remediation with 1-line justifications — and state what you check *first* before changing anything (access/scope/blast-radius discipline).

*Review guidance:* shared-responsibility answers must *name the party* — "it's shared" without saying *which half* is half an answer. Every hardening claim needs scan evidence.

**Next:** [M17 quiz](./quiz-m17.md) · **Previous:** [M15 quiz](../level-3/quiz-m15.md) · **Hub:** [Assessment Hub](../README.md)
