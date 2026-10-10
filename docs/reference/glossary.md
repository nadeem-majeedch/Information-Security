---
title: "Glossary of Security Terminology"
layout: default
---

# Glossary of Security Terminology

**Part of:** [Reference Library](README.md) · Concise, course-consistent definitions. **Modules** show where the term is taught/tested — if a term appears in a quiz before its module, check here first, then read the module. Terms are defined as the *course* uses them; standards bodies sometimes use broader senses (noted where it matters).

**AAL** — *Authentication Assurance Level* (NIST SP 800-63-4): 1–3 scale of how strongly an authentication event is proven. M07.

**ACL** — *Access Control List*: ordered rules granting/denying access to a resource (files, interfaces, firewall rules). M04, M05, M08.

**Active Directory (AD)** — Microsoft directory service for identities/groups in Windows domains; common lateral-movement target. Referenced in M07, M14 contexts.

**Asset** — Anything that has value to the organization (data, systems, people, reputation). The starting point of inventory and CIA classification. M01.

**Attack surface / attack vector** — *Surface:* everything an attacker can reach. *Vector:* the specific path used (email, exposed service…). M02, M11.

**Availability** — CIA pillar: authorized users get what they need when they need it. M01.

**Baseline drift** — Configuration changing away from the approved state over time; what a hygiene bot detects. M18.

**Buffer overflow** — Writing past an allocation's bounds; classic memory-safety bug class (largely eliminated in memory-safe languages). M10.

**Chain of custody** — Documented record of who held evidence, when, and what was done to it — from collection to disposition. M14.

**CIA triad** — *Confidentiality, Integrity, Availability*: the three properties security protects. M01.

**Classification (data)** — Labeling data by sensitivity (e.g., public/internal/personal/sensitive) to drive handling rules. M03, M17.

**Confidentiality** — CIA pillar: only authorized parties can read the data. M01.

**Confused deputy** — A program tricked into using its own privileges on the attacker's behalf (e.g., SSRF, path tricks). M09, M10.

**Control** — A safeguard that reduces risk. By function: **preventive** (stops it), **detective** (notices it), **corrective** (fixes it after); also administrative/technical/physical. M01, M02.

**CVSS** — *Common Vulnerability Scoring System*: 0–10 **technical severity** for vulnerabilities (course uses v4.0). Not business risk. M09, M12.

**CWE** — *Common Weakness Enumeration*: standardized *type of weakness* (e.g., CWE-79 = XSS) — used for code/config findings. M09, M10.

**Data controller / processor** — GDPR roles: controller determines purposes/means; processor acts on the controller's behalf. M17.

**Defense in depth** — Multiple independent layers so one failure isn't game over. M01, M08.

**DFD** — *Data-flow diagram*: processes, data stores, flows, external entities + trust boundaries — the canvas of threat modeling. M11.

**Detection engineering** — Writing, testing, tuning, and maintaining detection rules as versioned code. M13, M15.

**DPIA** — *Data Protection Impact Assessment*: structured assessment of privacy risk for high-risk processing, done at design time. M17.

**EDR** — *Endpoint Detection and Response*: endpoint telemetry + behavioral detection + response tooling. M05, M13.

**Entropy (key/token)** — Unpredictability of a value. High entropy = hard to guess; passwords need length/wordlist entropy, tokens need CSPRNG generation. M06, M07.

**Exploit / exploitation** — Using a vulnerability to produce unintended behavior; in this course, against local lab targets only. M12.

**Fail-open vs fail-closed** — Whether a system continues (open) or blocks (closed) when a security component fails. Design decision worth stating explicitly. M08, M18.

**FIDO2 / WebAuthn** — Browser/platform standard for phishing-resistant authenticators (passkeys). M07.

**Forensics (digital)** — Collecting and analyzing digital evidence under documented procedure (imaging, hashing, chain of custody). M14.

**Hardening** — Reducing a system's attack surface: close what's unneeded, configure securely, verify each change. M05, M16.

**Hashing** — One-way fixed-size digest of data; used for integrity, identifiers (SHA-256), and — with salt + work factor — password storage. Distinct from encryption. M01, M06.

**HMAC** — Hash-based message authentication code: keyed hash proving integrity + authenticity of a message. M06.

**IaaS/PaaS/SaaS** — Cloud service models; anchor the shared-responsibility split (more service = more provider responsibility). M16.

**IAAA** — *Identification, Authentication, Authorization, Accounting*: the four questions — who are you / prove it / what may you do / what did you do. M07.

**Identity proofing** — Verifying a claimed identity is the real person/organization at enrollment. M07.

**IDS / IPS** — *Intrusion Detection/Prevention System*: monitors and alerts (IDS) or blocks (IPS) on pattern matches (e.g., Suricata). M08.

**Incident** — A confirmed adverse event disrupting services or threatening confidentiality/integrity — triaged alerts become incidents by *correlation*. M13, M14.

**Injection** — Sending data that the interpreter reads as *commands* (SQL/command/LDAP…). Fixed by keeping code and data separate (parameterization). M09, M10.

**IOC** — *Indicator of Compromise*: observable artifact (hash, domain, IP, path) suggesting compromise; typed and confidence-rated. M15.

**IR** — *Incident Response*: the lifecycle for handling incidents (prepare → detect/analyze → contain/eradicate/recover → post-incident; NIST SP 800-61r3). M14.

**Kerckhoffs's principle** — A system must be secure even if everything except the key is public. M06.

**Key rotation** — Replacing cryptographic keys on a schedule or after suspected exposure; limits blast radius of a leak. M06, M18.

**Least privilege** — Give each identity only the permissions its task needs, for only as long as needed. M05, M07, M11.

**Log (security-relevant)** — Record of events with who/what/when/from where/outcome — the raw material of detection and forensics. M13.

**Malware** — Malicious software; classified by vector, payload, propagation, business model. M15.

**MDM** — *Mobile Device Management*: centralized policy/enforcement for mobile endpoints. Referenced M05.

**MFA / 2FA** — *Multi-/Two-Factor Authentication*: two or more *independent* factor types (something you know/have/are, plus situational factors). M07.

**MITRE ATT&CK** — Knowledge base of adversary **techniques** observed in the wild, organized by tactic; the vocabulary for detections and threat intel. M13, M15.

**MTTD / MTTR** — *Mean Time To Detect / Respond*: core SOC health metrics. M13.

**Nonce** — A number used once (or never repeated under a key); essential to GCM-family security. M06.

**Non-repudiation** — Ability to prove an action came from a specific party (signatures, strong logs); the "R" gap in STRIDE. M01, M06, M11.

**NVD** — *National Vulnerability Database* (NIST): CVE details, CVSS, affected products. M12.

**OAuth 2.0 / OIDC** — Authorization framework / identity layer on top; the flows behind "Sign in with…". M07.

**OWASP** — *Open Web Application Security Project*: open community producing Top 10, ASVS, WSTG, cheat sheets. M09, M10.

**PAM** — *Privileged Access Management*: vaulting/control of admin credentials and sessions. M07.

**Passkey (FIDO2)** — Device-bound or synced authenticator replacing passwords; origin-bound = phishing-resistant. M07.

**Patch management** — Identifying, testing, deploying, verifying updates — a **preventive** control. M05.

**Path traversal** — `../`-style escaping of an intended directory to read/write unintended files (CWE-22). M09, M10.

**PDLC / SDLC** — *Product/Software Development Lifecycle* — where security activities attach (requirements, design, code, test, release). M10.

**Pentest (penetration test)** — Authorized, scoped, goal-oriented security test ending in a report; differs from vuln assessment in depth and exploitation. M12.

**Phishing** — Deceptive message harvesting credentials/session tokens; variants: spear, whaling, smishing, vishing. M07.

**PII** — *Personally Identifiable Information*: any data that identifies a person (directly or in combination). M03, M17.

**Privilege escalation** — Moving from lower to higher privileges (vertical) or across peer accounts (horizontal). M05, M07.

**Principle of least privilege** — see least privilege.

**Ransomware** — Pay-to-restore malware; defenses: 3-2-1 offline backups, segmentation, EDR, least privilege, tested recovery. M05, M14, M15.

**RBAC** — *Role-Based Access Control*: permissions grouped into roles assigned to identities. M07.

**Residual risk** — Risk remaining after controls; must be stated, owned, and revisited — never silently assumed away. M02, M19.

**Risk** — Likelihood × impact of loss when a threat exploits a vulnerability; *not* the vulnerability itself. M02.

**Risk treatment** — Mitigate / transfer / avoid / accept, each with justification. M02, M17.

**RoE** — *Rules of Engagement*: written scope, timing, methods, exclusions, and stop conditions authorizing a test. M03, M12.

**Rootkit** — Malware hiding its presence (kernel/userland hooks). M15.

**Roaming profile?** — not a course term.

**Salting** — Adding a unique random value per record before hashing so identical inputs produce identical outputs only with the same salt; defeats precomputation. M06.

**Sandbox** — Isolated environment for running/observing risky code; course sandbox = VM, no shared folders, host-only networking. M15.

**SBOM** — *Software Bill of Materials*: inventory of components/versions in a build; supply-chain visibility. M10, M18.

**Scope (engagement)** — The explicit boundary of what may be tested/collected; exceeding it is unauthorized regardless of intent. M03, M12.

**Security misconfiguration** — Defaults left on, unnecessary features, permissive access, verbose errors — OWASP category and everyday finding. M09, M16.

**Separation of duties** — Splitting a sensitive action across two or more parties so no single actor can complete it alone. M07.

**SIEM** — *Security Information and Event Management*: centralized log collection, correlation, alerting. M13.

**SOC** — *Security Operations Center*: the function that monitors, triages, and responds (tiers 1–3). M13.

**SQL injection** — Data read as SQL; canonical fix is parameterized queries. M09, M10.

**SSRF** — *Server-Side Request Forgery*: server made to request attacker-chosen (often internal) URLs; cloud-metadata danger. M09.

**STRIDE** — Threat categories: Spoofing, Tampering, Repudiation, Information disclosure, Denial of service, Elevation of privilege — mapped to security properties. M11.

**Supply-chain attack** — Compromising a trusted dependency/update path rather than the target directly. M10, M18.

**Threat** — Anything that can exploit a vulnerability and cause harm (actor, event, condition). M01, M02.

**Threat model** — Structured answer to: what are we protecting, from whom, with what controls, what's left over. DFD + STRIDE + register. M11, M19.

**TOCTOU** — *Time-of-check to time-of-use*: state changes between validation and use — a race-class bug. M10.

**TOTP** — *Time-based One-Time Password*: the rotating 6-digit code authenticator apps generate. M07.

**Tripwire / integrity monitoring** — Detecting unauthorized file change by comparing to a known-good baseline/hash. M05, M13.

**Trust boundary** — Line where privilege/ownership/network zone changes; threat modeling's focal points. M11.

**Vulnerability** — A weakness that *could* be exploited — needs threat + impact to become risk. M01, M02.

**VPN** — *Virtual Private Network*: encrypted tunnel between authenticated peers; protects in transit beyond endpoints, not anonymity. M08.

**WAF** — *Web Application Firewall*: HTTP-layer rule set in front of an app; compensating control, not a fix. M09.

**Whitelist/allowlist vs blacklist/blocklist** — Default-allow vs default-deny enumerations; prefer "allow/block list" wording. M05, M16.

**XSS** — *Cross-Site Scripting*: attacker script executed in victims' browsers; fixed by context-aware output encoding (+ CSP as depth). M09.

**YARA** — Pattern-matching rule language for identifying files/memory by features. M15.

**Zero day** — Vulnerability unknown to (or unpatched by) the vendor — no signature exists yet; detection relies on behavior. M12, M15.

**Zero trust** — "Never trust, always verify; least privilege; assume breach" — verify per request regardless of network location. M11.

---

**Missing a term?** Check the module that used it first (the [course roadmap](../course-roadmap.md) maps concepts to modules), then the [reference library](README.md). Adding definitions to your own study notes is part of learning them — write yours in your portfolio's `notes/`.

**Next:** [Tools directory](tools.md) · [Learning pathways](pathways.md) · [Troubleshooting & independent study](study-guide.md)
