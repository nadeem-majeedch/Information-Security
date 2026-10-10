---
title: "Course Roadmap"
layout: default
---

# Information Security — Course Roadmap

**Course:** Information Security: A Self-Study Course from Beginner to Advanced
**Instructor:** Engr. Dr. Muhammad Nadeem Majeed — Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore, Pakistan
**Status:** DRAFT for instructor review · **Version:** 0.1 · **Last verified:** 2026-10-09
**Companion documents:** [Learning Outcomes](./learning-outcomes.md) · [Prerequisites](./prerequisites.md) · [Assessment Guide](./assessment-guide.md) · [Lab Safety Policy](./lab-safety-policy.md)

---

## How to use this roadmap

- The course contains **19 modules** in **four progressive levels**. Complete them in order unless a module's prerequisites say otherwise.
- Every module defines: prerequisites, measurable learning outcomes, core concepts, lab scenarios, tools and cost, evidence/deliverables, knowledge-check format, estimated study time, completion criteria, and further reading.
- **Every module is completable with $0 spending:** free/open-source tools, local or deliberately vulnerable lab environments, and synthetic data only. No classroom, no instructor demo, no university infrastructure, no paid software.
- Before touching any lab, read the [Lab Safety Policy](./lab-safety-policy.md). Testing is restricted to systems you own or have explicit written authorization to test.
- Pace options: **Steady** (8–10 h/week ≈ 9 months) · **Standard** (10–12 h/week ≈ 7 months) · **Intensive** (15+ h/week ≈ 5 months). Total effort ≈ **300 hours ± 10%**.

## Course at a glance

| Module | Title | Level | Difficulty | Est. time | Signature deliverable |
|---|---|---|---|---|---|
| M01 | Information Security Foundations and the CIA Triad | 1 | Beginner | 8–10 h | Security concept glossary + personal asset inventory |
| M02 | Threats, Vulnerabilities, Risk, and Controls | 1 | Beginner | 10–12 h | Risk register for a home network |
| M03 | Security Governance, Policy, Ethics, and Law | 1 | Beginner | 8–10 h | Personal acceptable-use & incident policy set |
| M04 | Networking Fundamentals for Security | 1 | Beginner | 12–14 h | Packet-capture analysis notebook |
| M05 | Operating System and Endpoint Security | 1 | Beginner | 12–14 h | Hardened workstation evidence pack |
| M06 | Cryptography and Applied Cryptography | 2 | Intermediate | 14–16 h | Cryptographic misuse analysis + secure messaging setup |
| M07 | Identity, Authentication, Authorization, and Access Management | 2 | Intermediate | 12–14 h | IAM design for a small team |
| M08 | Network Security: Perimeter, Segmentation, and Secure Protocols | 2 | Intermediate | 14–16 h | Segmented lab network with firewall rules + IDS alerts |
| M09 | Web Application Security (OWASP Top 10:2025) | 2 | Intermediate | 18–20 h | Web assessment report (Juice Shop) |
| M10 | Secure Programming and Software Security | 2 | Intermediate | 18–20 h | Secure-feature code review + CI security gates |
| M11 | Threat Modeling and Security Architecture | 2 | Intermediate | 12–14 h | STRIDE threat model of a real system |
| M12 | Vulnerability Assessment and Authorized Security Testing | 3 | Intermediate | 16–18 h | Scoped engagement report (lab only) |
| M13 | Logging, Monitoring, and Security Operations | 3 | Intermediate | 16–18 h | Detection rules + triage playbook |
| M14 | Incident Response and Digital Forensics | 3 | Advanced | 18–20 h | IR plan + forensic timeline report |
| M15 | Malware Concepts and Defensive Analysis | 3 | Advanced | 16–18 h | Static/dynamic malware triage report |
| M16 | Cloud and Infrastructure Security | 4 | Advanced | 16–18 h | Hardened container/IaC deployment with audit evidence |
| M17 | Privacy, Data Protection, Risk Management, and Compliance | 4 | Advanced | 12–14 h | Data-flow map + DPIA + control mapping |
| M18 | Security Automation and Emerging Challenges | 4 | Advanced | 14–16 h | Automated security pipeline + emerging-threat brief |
| M19 | Integrated Capstone Project | 4 | Advanced | 30–40 h | End-to-end secure-system portfolio |

**Level totals:** Level 1 ≈ 50–60 h · Level 2 ≈ 88–100 h · Level 3 ≈ 66–74 h · Level 4 ≈ 72–88 h.

## Reference and version policy

Editions below were checked on **2026-10-09**; always confirm the publisher's page for the latest status before citing in submitted work.

| Standard / source | Edition used in this course |
|---|---|
| NIST Cybersecurity Framework | CSF 2.0 (NIST CSWP 29, Feb 2024) |
| NIST incident response | SP 800-61 Rev. 3 (Apr 2025) |
| NIST digital identity | SP 800-63-4 (Jul 2025) |
| NIST security & privacy controls | SP 800-53 Release 5.2.0 (Aug 2025) |
| CIS Critical Security Controls | v8.1 (Jun 2024) |
| OWASP Top 10 | 2025 edition |
| OWASP ASVS | 5.0.0 (May 2025) |
| OWASP Web Security Testing Guide | v4.2 (current stable) |
| MITRE ATT&CK | v19.x (2026 releases) |
| CVSS | v4.0 (FIRST, Nov 2023) |
| ISO/IEC 27001 / 27002 | 2022 editions |
| Pakistan cybercrime law | Prevention of Electronic Crimes Act 2016, as amended (incl. Prevention of Electronic Crimes (Amendment) Act 2025) |

---

# Level 1: Information Security Foundations

*Goal: build correct vocabulary, mental models, and a safe working environment. No prior security knowledge assumed. Difficulty: Beginner.*

---

### M01 — Information Security Foundations and the CIA Triad

- **Level / Difficulty:** Level 1 · Beginner
- **Prerequisites:** None.
- **Measurable learning outcomes:**
  1. Define information security, cybersecurity, and information asset in your own words with accurate examples. *(Remember)*
  2. Explain the CIA triad and give two real-world examples of each pillar's violation and corresponding safeguard. *(Understand)*
  3. Distinguish threat, vulnerability, risk, and control in at least 8/8 scenario cards. *(Understand)*
  4. Classify a personal asset inventory by confidentiality, integrity, and availability impact. *(Apply)*
- **Core concepts:** CIA triad; authenticity and non-repudiation; information asset and asset owner; threat/vulnerability/risk/control vocabulary; security baselines; defense in depth; people-process-technology; security vs. availability vs. usability trade-offs; NIST CSF 2.0 functions (Govern, Identify, Protect, Detect, Respond, Recover).
- **Practical lab scenarios:**
  1. *Asset inventory:* catalog 10–15 personal devices, accounts, and files; label each with CIA impact ratings.
  2. *Triad breakage:* take 6 news incidents, map which CIA pillar failed and why.
  3. *Concept sort:* classify 20 mixed statements as threat / vulnerability / risk / control (self-checked answer key).
- **Tools & estimated cost:** Pen-and-paper or any Markdown editor. **$0.**
- **Evidence / deliverables:** `M01/` portfolio folder — asset inventory table (Markdown/CSV) + 1-page "CIA in my digital life" reflection.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 short answer), self-marked against provided answer key; retake allowed until ≥ 80%.
- **Estimated study time:** 8–10 hours.
- **Completion criteria:** Quiz ≥ 80%; asset inventory complete with CIA labels; can explain all four vocabulary terms without notes.
- **Further reading:** NIST CSF 2.0 (csrc.nist.gov/pubs/cswp/29); NIST SP 800-12 Rev. 1, *An Introduction to Information Security* (2017) — reference title corrected 2026-10-09; CISA, *Cybersecurity Best Practices* (cisa.gov/resources-tools).

---

### M02 — Threats, Vulnerabilities, Risk, and Controls

- **Level / Difficulty:** Level 1 · Beginner
- **Prerequisites:** M01.
- **Measurable learning outcomes:**
  1. Identify common threat actors, motivations, and capability tiers (script kiddie → nation-state). *(Understand)*
  2. Differentiate threat, vulnerability, exposure, likelihood, and impact using standardized definitions. *(Understand)*
  3. Apply a simple risk formula (risk = likelihood × impact) to rank 8 risks on a 5×5 matrix. *(Apply)*
  4. Select appropriate control types (preventive/detective/corrective; technical/administrative/physical) for given risks. *(Apply)*
- **Core concepts:** threat actors and motivation; attack surfaces and attack vectors; vulnerability lifecycle (discovery → disclosure → patch → exploitation); CVE and the NVD; CVSS v4.0 scoring; qualitative vs. quantitative risk analysis; risk treatment (accept, avoid, mitigate, transfer); control taxonomy; NIST CSF 2.0 and CIS Controls v8.1 as control collections.
- **Practical lab scenarios:**
  1. *Risk register:* build a 10-row risk register for your home network/router/IoT setup; score, rank, and treat each risk.
  2. *CVE walk-through:* pick one recent CVE from the NVD; document vector, CVSS v4.0 score, affected software, and the patch/mitigation path.
  3. *Actor profile:* write a one-page profile of a threat actor targeting a small business; map their likely vectors to controls.
- **Tools & estimated cost:** NVD (nvd.nist.gov), FIRST CVSS v4.0 calculator (first.org), any spreadsheet. **$0.**
- **Evidence / deliverables:** Risk register (table) + one CVE analysis sheet.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 scenario-based short answer), self-graded; ≥ 80% to pass.
- **Estimated study time:** 10–12 hours.
- **Completion criteria:** Risk register scored and sorted with justified treatments; CVE sheet complete with correct CVSS interpretation; quiz ≥ 80%.
- **Further reading:** CVSS v4.0 specification (first.org/cvss/specification-document); NIST SP 800-30 Rev. 1, *Guide for Conducting Risk Assessments*; CISA Known Exploited Vulnerabilities catalog (cisa.gov/known-exploited-vulnerabilities-catalog).

---

### M03 — Security Governance, Policy, Ethics, and Law

- **Level / Difficulty:** Level 1 · Beginner
- **Prerequisites:** M01.
- **Measurable learning outcomes:**
  1. Distinguish governance, regulation, policy, standard, procedure, and guideline in a hierarchy diagram. *(Understand)*
  2. Draft a short personal/household security policy set (acceptable use, password rule, device rule, incident contacts) in correct policy form. *(Apply)*
  3. Explain the ethical boundaries of security work: authorization, scope, privacy, and responsible disclosure. *(Understand)*
  4. Summarize the purpose and key offense categories of Pakistan's Prevention of Electronic Crimes Act (PECA) 2016 as amended, and contrast it with one other jurisdiction's law (e.g., EU GDPR). *(Understand)*
- **Core concepts:** governance vs. compliance; policy hierarchy; roles and responsibilities; ethics codes (ISC² / (ISC)² CISSP code, ACM/IEEE); authorized vs. unauthorized access; computer misuse laws — PECA 2016 (as amended, incl. 2025 amendment and NCCIA), EU GDPR basics, US CFAA (conceptual); responsible vulnerability disclosure; professional accountability.
- **Practical lab scenarios:**
  1. *Policy drafting:* write a 1–2 page household/roommate security policy covering devices, Wi-Fi, guests, and backups.
  2. *Gray-area cases:* analyze 5 ethical vignettes (e.g., testing a friend's website without written permission, "just looking" at a shared router) and justify decisions.
  3. *Law mapping:* map 6 everyday activities to PECA 2016 offense categories and note the authorization that makes each safe.
- **Tools & estimated cost:** Text of PECA (na.gov.pk / mins.gov.pk), EUR-Lex GDPR page, any editor. **$0.**
- **Evidence / deliverables:** Policy set document + ethics case-analysis sheet (5 vignettes).
- **Knowledge-check format:** 10-question quiz (6 MCQ + 4 short answer) + 1 scenario essay (≈300 words), self-graded with rubric. ≥ 80%.
- **Estimated study time:** 8–10 hours.
- **Completion criteria:** Policy set passes the provided checklist (scope, roles, review date, enforceability); all vignettes cite authorization/ethics principles; quiz ≥ 80%.
- **Further reading:** PECA 2016 as amended (official text, na.gov.pk); GDPR text (eur-lex.europa.eu); (ISC)² Code of Ethics (isc2.org); OWASP, *Responsible Disclosure* guidance.

---

### M04 — Networking Fundamentals for Security

- **Level / Difficulty:** Level 1 · Beginner
- **Prerequisites:** M01. Basic comfort with installing software.
- **Measurable learning outcomes:**
  1. Map data across the TCP/IP model layers and identify where common security controls sit (TLS, firewall, VPN, DNS security). *(Understand)*
  2. Read a packet capture and identify ARP, DNS, TCP handshake, HTTP, and TLS ClientHello without assistance. *(Apply)*
  3. Explain IP addressing, subnetting (prefix /24 and smaller), NAT, ports, and common services (DNS, DHCP, HTTP/S, SSH). *(Understand)*
  4. Capture and analyze traffic **only on your own isolated lab network** using Wireshark filters. *(Apply)*
- **Core concepts:** TCP/IP and OSI models; Ethernet, ARP, IP, ICMP, TCP/UDP, DNS, DHCP, HTTP/S, TLS handshake; ports and sockets; NAT and routing basics; subnetting; DNS resolution chain; common scanners' logic (probe → response); wireless basics (WPA2/WPA3, SSID, evil twin concept); network-level security overview (firewall, IDS/IPS, VPN, DoS concepts).
- **Practical lab scenarios:**
  1. *Capture & annotate:* record traffic while browsing, resolving DNS, and loading a page; filter and explain 10 packets/steps.
  2. *Handshake reconstruction:* identify a full TCP three-way handshake and TLS negotiation in a capture; draw the sequence.
  3. *Isolated subnet:* build a host-only/virtual network with 2 VMs; assign static IPs; verify connectivity and prove isolation from your real LAN.
- **Tools & estimated cost:** Wireshark (free), VirtualBox or VMware Workstation Player (free for personal use), Nmap (free) for **lab IPs only**. **$0.**
- **Evidence / deliverables:** Lab notebook: 5 annotated screenshots/filters per scenario + a one-page protocol cheat sheet you wrote.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 packet-reading short answer). ≥ 80%.
- **Estimated study time:** 12–14 hours.
- **Completion criteria:** Captures taken and annotated on an isolated network (evidence of isolation included); can label a handshake sequence from memory; quiz ≥ 80%.
- **Further reading:** RFC 1122/793 summaries; Wireshark docs (wiki.wireshark.org); NIST SP 800-41 Rev. 1, *Guidelines on Firewalls and Firewall Policy*; Cloudflare Learning Center, *What is DNS?*

---

### M05 — Operating System and Endpoint Security

- **Level / Difficulty:** Level 1 · Beginner
- **Prerequisites:** M04 (recommended), M01.
- **Measurable learning outcomes:**
  1. Apply OS hardening baseline steps on Linux (user accounts, sudo, firewall, updates, SSH config) and Windows (accounts, UAC, BitLocker awareness, firewall, updates). *(Apply)*
  2. Explain malware protection layers: antivirus/EDR behavior, application control, patching, and least privilege. *(Understand)*
  3. Configure and verify basic endpoint hygiene: disk encryption awareness, secure backup (3-2-1 rule), and browser security settings. *(Apply)*
  4. Detect basic signs of endpoint compromise (unexpected processes, persistence locations, unexpected outbound connections). *(Analyze)*
- **Core concepts:** least privilege and separation of duties; user/account management; patch and vulnerability management; host-based firewall; Windows vs. Linux hardening surfaces (services, registry vs. config files, systemd); disk encryption (BitLocker/LUKS); application allowlisting; endpoint protection (AV/EDR concepts); backup and recovery (3-2-1); browser security; physical security basics.
- **Practical lab scenarios:**
  1. *Harden a VM:* take a fresh Linux VM (e.g., Ubuntu Server) through a 15-point hardening checklist; verify with commands and screenshots.
  2. *Windows baseline:* apply 10 hardening settings on a Windows VM (use Microsoft's free developer VM or your own machine's VM); record before/after evidence.
  3. *Compromise hunt (simulated):* in a provided benign exercise image/script set, find 5 planted indicators (odd startup entry, rogue service, unexpected open port) and document them.
- **Tools & estimated cost:** Ubuntu/Debian ISO (free), VirtualBox (free), Microsoft free Windows developer VMs (free, expiring evaluation images), `lynis` (free) for Linux audit scoring. **$0.**
- **Evidence / deliverables:** Hardening checklist with before/after evidence (10+ screenshots) + lynis/audit output summary + brief reflection.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 short answer). ≥ 80%.
- **Estimated study time:** 12–14 hours.
- **Completion criteria:** VM hardened and verified (services minimized, firewall on, accounts reviewed); all 5 planted indicators found; quiz ≥ 80%.
- **Further reading:** CIS Benchmarks (cisecurity.org/cis-benchmarks — free registration); NIST SP 800-123, *Guide to General Server Security*; Microsoft, *Security baseline documentation* (learn.microsoft.com).

---

# Level 2: Core Technical Security Skills

*Goal: acquire the durable technical core — cryptography, identity, network defense, web security, secure code, and architecture. Difficulty: Intermediate. Labs move to purpose-built vulnerable environments, always isolated per the [Lab Safety Policy](./lab-safety-policy.md).*

---

### M06 — Cryptography and Applied Cryptography

- **Level / Difficulty:** Level 2 · Intermediate
- **Prerequisites:** M01; basic comfort with a terminal (from M04/M05).
- **Measurable learning outcomes:**
  1. Distinguish symmetric, asymmetric, and hash algorithms; give two use cases and one weakness for each family. *(Understand)*
  2. Execute correct key handling: generate a keypair, encrypt/decrypt, sign/verify, and exchange a shared secret using open tooling. *(Apply)*
  3. Detect common cryptographic misuses (ECB mode, static IVs, MD5/SHA-1 for integrity, hard-coded keys, homemade protocols). *(Analyze)*
  4. Explain certificates, PKI, TLS at a conceptual level, and demonstrate a working TLS-protected service in the lab. *(Apply)*
- **Core concepts:** Kerckhoffs's principle; confusion/diffusion; AES, ChaCha20, 3DES (historical); RSA, ECC, Diffie–Hellman; SHA-2/SHA-3, HMAC; modes of operation (CBC, GCM); IVs and nonces; salting and password hashing (bcrypt/scrypt/Argon2/PBKDF2 vs. plain hash); certificates, CA hierarchy, PKI, trust stores; TLS 1.3 overview; key management and rotation; post-quantum cryptography (awareness, NIST PQC standards); crypto misuse patterns (CWE-327/328/780, OWASP Crypto Cheat Sheet).
- **Practical lab scenarios:**
  1. *Crypto toolbox:* use OpenSSL/GnuPG to encrypt a file (symmetric), sign and verify a message (asymmetric), and hash with salt — record every command.
  2. *Misuse hunt:* examine 6 small code/config snippets (ECB image leak, MD5 password hash, fixed IV, hard-coded key, weak RNG, homegrown XOR) and explain the flaw + fix.
  3. *TLS service:* serve a local site over HTTPS using a locally generated self-signed certificate (or free Let's Encrypt on a domain you own); inspect the certificate chain and TLS negotiation with a browser/Wireshark.
- **Tools & estimated cost:** OpenSSL, GnuPG, Python `cryptography` (all free), CyberChef (free, local), Wireshark. **$0.**
- **Evidence / deliverables:** Crypto lab notebook (commands + outputs) + misuse analysis sheet (6 findings, each with CWE/weakness ID).
- **Knowledge-check format:** 14-question quiz (10 MCQ + 4 applied short answer). ≥ 80%.
- **Estimated study time:** 14–16 hours.
- **Completion criteria:** All three labs evidenced; can correctly reason about 5/6 misuse snippets; quiz ≥ 80%.
- **Further reading:** OWASP *Cryptographic Storage Cheat Sheet* and *Password Storage Cheat Sheet* (cheatsheetseries.owasp.org); NIST SP 800-57 (key management) & NIST FIPS 203/204/205 (post-quantum standards, 2024); Serious Cryptography (Aumasson) for further study.

---

### M07 — Identity, Authentication, Authorization, and Access Management

- **Level / Difficulty:** Level 2 · Intermediate
- **Prerequisites:** M05, M06.
- **Measurable learning outcomes:**
  1. Differentiate identification, authentication, authorization, and accounting (IAAA) with examples of failure for each. *(Understand)*
  2. Compare authentication factors and methods (passwords, passkeys/FIDO2, TOTP, SMS risks) against NIST SP 800-63-4 guidance. *(Evaluate)*
  3. Implement least privilege and role-based access control in a local directory/service (Linux groups + a web app's RBAC). *(Apply)*
  4. Explain SSO, OAuth 2.0/OIDC flows conceptually and spot token/redirect flaws. *(Understand)*
- **Core concepts:** IAAA; identity proofing, authenticators, sessions; passwords vs. passkeys (FIDO2/WebAuthn), MFA, TOTP, recovery flows; NIST SP 800-63-4 AAL/IAL/FAL; authorization models (DAC/MAC/RBAC/ABAC); least privilege, separation of duties, privilege escalation risks; SSO, OAuth 2.0, OIDC, JWT, session management flaws; secret and password-manager hygiene; PAM concept.
- **Practical lab scenarios:**
  1. *Directory RBAC:* create users/groups on a Linux VM; implement a permission matrix (read/write/execute per group) and verify with test accounts.
  2. *MFA lab:* enable TOTP-based MFA on a locally hosted app (e.g., a deliberately configured service or Vault/Keycloak demo) and demonstrate enrollment, success, and recovery-path risks.
  3. *OAuth walkthrough:* trace an OIDC login flow using a local demo (e.g., Keycloak + sample app); capture and annotate authorization code, token, and redirect steps.
- **Tools & estimated cost:** Linux VM (free), Keycloak or Vault community edition (free), KeePass/Bitwarden (free tier) as password-hygiene practice. **$0.**
- **Evidence / deliverables:** IAM design note for a 5-person team (roles, permissions, MFA policy) + lab evidence of RBAC and MFA.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 scenario). ≥ 80%.
- **Estimated study time:** 12–14 hours.
- **Completion criteria:** RBAC matrix implemented and verified; MFA enrollment evidence; design note covers roles, least privilege, and recovery risks; quiz ≥ 80%.
- **Further reading:** NIST SP 800-63-4 (pages.nist.gov/800-63-4); OWASP *Authentication Cheat Sheet* & *Authorization Cheat Sheet* (Cheat Sheet Series); OAuth.net (protocol overview).

---

### M08 — Network Security: Perimeter, Segmentation, and Secure Protocols

- **Level / Difficulty:** Level 2 · Intermediate
- **Prerequisites:** M04, M05.
- **Measurable learning outcomes:**
  1. Design a segmented network (VLAN/host-only zones or firewall rule zones) and justify each rule. *(Apply)*
  2. Configure and verify host- and network-based firewall rules (Linux `nftables`/`ufw` or pfSense/OPNsense in a VM). *(Apply)*
  3. Detect simulated reconnaissance and attacks with an IDS (Suricata/Snort) and read its alerts. *(Apply)*
  4. Evaluate secure protocols (SSH vs. Telnet, HTTPS vs. HTTP, WPA3, VPN concepts, DNS security) and recommend replacements. *(Evaluate)*
- **Core concepts:** defense in depth at network layer; packet filtering, stateful inspection, proxy/NGFW concepts; network segmentation and zero-trust networking; DMZ concept; IDS/IPS signatures and false positives; VPN (IPsec, WireGuard) concepts; secure protocols and their plaintext predecessors; DNS security (DoH/DoT basics); wireless security (WPA2/WPA3, evil twin); common DoS/DDoS defenses conceptually.
- **Practical lab scenarios:**
  1. *Segmented lab:* build three zones (management, workstation, target lab) on a host-only network; firewall rules allow only intended flows; prove with connectivity tests (allowed + blocked).
  2. *IDS watch:* deploy Suricata with ET Open rules on the lab path (or Linux `afpacket`/SPAN emulation); generate benign Nmap scans **against lab IPs only**; capture and explain 5 alerts.
  3. *Protocol upgrade:* serve the same service over plaintext and TLS/SSH in the lab; capture both; document what an eavesdropper learns in each case.
- **Tools & estimated cost:** VirtualBox (free), pfSense/OPNsense or Linux + `nftables` (free), Suricata + ET Open rules (free), Nmap/Wireshark (free). **$0.**
- **Evidence / deliverables:** Network diagram + firewall rule table (with justifications) + IDS alert screenshots with triage notes.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 rule-review scenarios). ≥ 80%.
- **Estimated study time:** 14–16 hours.
- **Completion criteria:** Zones enforced (blocked-flow evidence required); ≥ 5 IDS alerts analyzed; quiz ≥ 80%.
- **Further reading:** NIST SP 800-41 Rev. 1 (firewalls); Suricata docs (suricata.io); MITRE ATT&CK ATT&CK for Network (reconnaissance/initial access tactics); Cloudflare Learning Center (VPN/TLS explainers).

---

### M09 — Web Application Security (OWASP Top 10:2025)

- **Level / Difficulty:** Level 2 · Intermediate
- **Prerequisites:** M04 (HTTP), M06 (TLS/crypto basics), M07 (sessions/auth).
- **Measurable learning outcomes:**
  1. Explain each OWASP Top 10:2025 category, its root cause, and at least one concrete prevention per category. *(Understand)*
  2. Demonstrate — **against local lab apps only** — at least 6 vulnerability classes from different Top 10 categories (e.g., broken access control, injection, misconfiguration, insecure design). *(Apply)*
  3. Write a professional vulnerability report for each finding: steps, evidence, impact, remediation, severity. *(Apply)*
  4. Map findings to OWASP ASVS requirements and CVSS v4.0 vectors. *(Apply)*
- **Core concepts:** OWASP Top 10:2025 categories; injection (SQL/NoSQL/command); broken access control and IDOR; cryptographic failures; insecure design; security misconfiguration; vulnerable components; identification/authentication failures; software/data integrity; logging & monitoring gaps; SSRF; XSS and CSRF; session management; security headers; ASVS levels; WSTG test methodology; safe testing scope.
- **Practical lab scenarios:**
  1. *Juice Shop path:* solve 10 OWASP Juice Shop challenges spanning ≥ 5 Top 10 categories; document each with request/response evidence.
  2. *DVWA rotation:* complete low/medium/high exercises for SQLi, XSS, and file upload on DVWA; compare how defenses change per level.
  3. *Report writing:* convert 3 of your findings into full reports (reproduction steps, impact, fix, severity).
- **Tools & estimated cost:** OWASP Juice Shop, DVWA, WebGoat (free); OWASP ZAP (free) and Burp Suite Community (free) for intercepting proxies; browser dev tools. All local/containers. **$0.**
- **Evidence / deliverables:** `M09` report: ≥ 6 findings with evidence + remediation; challenge log (IDs/names solved); ASVS mapping table.
- **Knowledge-check format:** 14-question quiz (10 MCQ + 4 scenario-based). ≥ 80%.
- **Estimated study time:** 18–20 hours.
- **Completion criteria:** ≥ 6 evidenced findings across ≥ 5 Top 10 categories, all from local lab targets; 3 professional-grade reports; quiz ≥ 80%.
- **Further reading:** OWASP Top 10:2025 (top10.owasp.org); OWASP ASVS 5.0 (owasp.org/www-project-application-security-verification-standard); OWASP WSTG v4.2 (wstg.owasp.org); OWASP Cheat Sheet Series.

---

### M10 — Secure Programming and Software Security

- **Level / Difficulty:** Level 2 · Intermediate
- **Prerequisites:** M09 (web vuln vocabulary); working knowledge of one programming language (see [Prerequisites](./prerequisites.md)).
- **Measurable learning outcomes:**
  1. Apply the secure SDLC: security requirements, threat-informed design, coded review, testing, and release gates. *(Apply)*
  2. Find and fix at least 8 seeded weaknesses (CWE classes: injection, path traversal, hardcoded secrets, unsafe deserialization, weak RNG, SSRF, mass assignment, insecure file upload) in provided code. *(Apply)*
  3. Run and interpret SAST, dependency, secret-scanning, and container-scanning tools; triage true vs. false positives. *(Analyze)*
  4. Explain memory-safety classes (buffer overflow, use-after-free) and why memory-safe languages/compilers change the risk. *(Understand)*
- **Core concepts:** OWASP SAMM/secure SDLC; CWE Top 25; input validation and parameterized queries; output encoding; error handling; secrets management; dependency/supply-chain security (SBOM concept, typosquatting); SAST/DAST/IAST/SCA distinctions; CI/CD pipeline security; code signing and integrity (SLSA concept); memory safety; sanitization vs. validation; OWASP ASVS as a build checklist.
- **Practical lab scenarios:**
  1. *Vulnerable app remediation:* take a small intentionally vulnerable app (e.g., NodeGoat-style or instructor-provided seed repo) and fix 8 seeded weaknesses; show before/after tests.
  2. *Pipeline gates:* wire `semgrep` (or equivalent), `gitleaks`, and `npm audit`/`pip-audit`/`trivy` into a local script/CI workflow; demonstrate the pipeline failing on a planted issue and passing after the fix.
  3. *Memory-safety explainer:* compile/run a tiny C program demonstrating a bounds error (in a local VM, educational only) and write a 200-word mitigation note.
- **Tools & estimated cost:** Any local language toolchain (free), Semgrep Community (free), Gitleaks (free), Trivy (free), OWASP SAMM checklists. **$0.**
- **Evidence / deliverables:** Patch set (diffs) for 8 fixes + CI gate log showing fail-then-pass + short supply-chain security note.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 code-review questions). ≥ 80%.
- **Estimated study time:** 18–20 hours.
- **Completion criteria:** All 8 fixes verified by tests/scans; pipeline demonstrably fails on a planted flaw; quiz ≥ 80%.
- **Further reading:** CWE Top 25 (cwe.mitre.org/top25); OWASP SAMM (owaspsamm.org); OWASP *Input Validation* & *Software Supply Chain Security* Cheat Sheets; SLSA framework (slsa.dev).

---

### M11 — Threat Modeling and Security Architecture

- **Level / Difficulty:** Level 2 · Intermediate
- **Prerequisites:** M01–M10 (esp. M05, M07, M09).
- **Measurable learning outcomes:**
  1. Produce a data-flow diagram (DFD) with trust boundaries for a given application scenario. *(Apply)*
  2. Apply STRIDE to every element of the DFD and elicit ≥ 15 distinct threats. *(Analyze)*
  3. Prioritize threats and select mitigations using risk reasoning; document residual risk. *(Evaluate)*
  4. Evaluate a simple architecture against zero-trust principles (never trust, always verify; least privilege; assume breach). *(Evaluate)*
- **Core concepts:** threat modeling frameworks (STRIDE, PASTA awareness, LINDDUN for privacy awareness); DFD elements (process, data store, data flow, external entity, trust boundary); attack trees; risk-based prioritization; security architecture patterns (segmentation, gateways, brokered auth); zero trust architecture (NIST SP 800-207 concept); least privilege in design; abuse/misuse cases; threat-informed defense with MITRE ATT&CK.
- **Practical lab scenarios:**
  1. *Full STRIDE model:* model a familiar system (online food ordering, LMS, or library system): DFD → 15+ threats → mitigations → risk ranking.
  2. *Abuse cases:* write 5 abuse/misuse cases for the same system's auth and payment-adjacent flows; map each to a design change.
  3. *Architecture review:* take a provided reference architecture (2-tier vs. 3-tier with API) and identify design weaknesses using zero-trust principles.
- **Tools & estimated cost:** Draw.io/diagrams.net (free) or pen-and-paper photos; MITRE ATT&CK website (free). **$0.**
- **Evidence / deliverables:** DFD image + threat table (threat, STRIDE category, likelihood/impact, mitigation, residual risk) + 1-page architecture review memo.
- **Knowledge-check format:** 10-question quiz (6 MCQ + 4 applied) + threat-model quality checklist (self-assessed). ≥ 80%.
- **Estimated study time:** 12–14 hours.
- **Completion criteria:** DFD includes trust boundaries; ≥ 15 threats each with mitigation decision; checklist satisfied; quiz ≥ 80%.
- **Further reading:** NIST SP 800-154, *Guide to Data-Centric System Threat Modeling*; Microsoft STRIDE (learn.microsoft.com); NIST SP 800-207, *Zero Trust Architecture*; OWASP *Threat Modeling* documentation (owasp.org/www-project-threat-modeling).

---

# Level 3: Practical Security Assessment and Defense

*Goal: operate like a practitioner — assess authorized targets professionally, run detection and response, and analyze offensive artifacts defensively. All testing stays inside your isolated lab per the [Lab Safety Policy](./lab-safety-policy.md).*

---

### M12 — Vulnerability Assessment and Authorized Security Testing

- **Level / Difficulty:** Level 3 · Intermediate
- **Prerequisites:** M04, M05, M08, M09.
- **Measurable learning outcomes:**
  1. Write a rules-of-engagement document (scope, authorization, timing, exclusions, stop conditions) for a lab assessment. *(Apply)*
  2. Conduct a structured, authorized vulnerability assessment against isolated lab targets using reconnaissance → scanning → validation → reporting phases. *(Apply)*
  3. Validate scanner findings manually to eliminate false positives and prioritize by CVSS v4.0 plus business context. *(Analyze)*
  4. Produce a client-quality assessment report with executive summary, findings, evidence, and remediation roadmap. *(Create)*
- **Core concepts:** VA vs. penetration testing vs. red teaming; authorization and rules of engagement; PTES/OSSTMM awareness and WSTG methodology; information gathering (passive vs. active — active restricted to lab); vulnerability scanning; manual validation; false positives; risk rating (CVSS v4.0 + context); reporting standards; remediation tracking; retesting.
- **Practical lab scenarios:**
  1. *Scoped lab engagement:* assess a multi-VM lab (e.g., Metasploitable-class target + Juice Shop) **inside an isolated network**: written RoE first, then scan (Nmap/Greenbone or OpenVAS if resources allow), validate manually, and rate findings.
  2. *False-positive clinic:* review 8 raw scanner outputs; validate each; mark TP/FP with evidence.
  3. *Report delivery:* produce a full report and a 1-page remediation roadmap with a retest plan.
- **Tools & estimated cost:** Nmap (free), OWASP ZAP (free), Nuclei (free), Greenbone/OpenVAS (free; needs RAM) or Nessus Essentials (free personal license, optional), local VMs as targets. All targets are owned/isolated labs. **$0** (optional tools remain free).
- **Evidence / deliverables:** RoE document + raw scan artifacts (sanitized) + finding validation sheet (8 items) + full assessment report.
- **Knowledge-check format:** 12-question quiz (7 MCQ + 5 scenario/ethics questions, incl. at least 2 scope-boundary questions). ≥ 80%.
- **Estimated study time:** 16–18 hours.
- **Completion criteria:** RoE written **before** any scanning (timestamped); ≥ 6 validated findings reported; false-positive clinic ≥ 6/8 correct; quiz ≥ 80%.
- **Further reading:** NIST SP 800-115, *Technical Guide to Information Security Testing and Assessment*; OWASP WSTG v4.2; PTES standard (pentest-standard.org); CVSS v4.0 (first.org).

---

### M13 — Logging, Monitoring, and Security Operations

- **Level / Difficulty:** Level 3 · Intermediate
- **Prerequisites:** M04, M05. M08 recommended.
- **Measurable learning outcomes:**
  1. Configure meaningful logging (syslog/journald, Windows Event Log, application logs) and justify what to log and retention limits. *(Apply)*
  2. Write detection rules (Sigma-style or native) for ≥ 6 attack behaviors mapped to MITRE ATT&CK v19.x techniques. *(Apply)*
  3. Triage 5 simulated security alerts: classify true/false positive, severity, and next actions using a documented playbook. *(Analyze)*
  4. Explain SOC tiers, the alert lifecycle (collect → correlate → detect → triage → respond), and MTTD/MTTR metrics. *(Understand)*
- **Core concepts:** log sources and log quality (timestamps, normalization, timezone traps); centralized logging and SIEM concepts; detection engineering (rules, Sigma, detection-as-code); MITRE ATT&CK technique mapping; alert triage and tuning; false-positive management; use cases (brute force, privilege escalation, persistence, C2 beaconing); SOC roles and processes; metrics (MTTD/MTTR); log privacy and retention.
- **Practical lab scenarios:**
  1. *Log pipeline:* collect Linux auth/web logs into a searchable store and demonstrate retention/rotation settings. Two tiers: (a) full — Wazuh or Elastic community stack, if your machine allows; (b) lightweight — `journalctl`/`auditd` plus a small scripted analyzer that parses and reports on failed logins and sudo events. Both tiers satisfy the requirement.
  2. *Detection pack:* author 6 detection rules (e.g., repeated failed logins, new SUID binary, unusual outbound DNS volume, web 404 burst, sudo misuse, scheduled-task creation) mapped to ATT&CK; test each by triggering it **in the lab**.
  3. *Triage shift:* process 5 pre-generated alert cases (provided data); fill a triage worksheet with verdict and escalation decision.
- **Tools & estimated cost:** Linux VM (free), Wazuh or Elastic community (free; resource-heavy — optional tier), Sigma rules (free), `journald`/`auditd` (free), Splunk free tier or Graylog (free) as alternatives. **$0.**
- **Evidence / deliverables:** Logging architecture note (sources, retention, rationale) + 6 tested detection rules with ATT&CK mapping + completed triage worksheets (5 cases).
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 triage scenarios). ≥ 80%.
- **Estimated study time:** 16–18 hours.
- **Completion criteria:** All 6 rules fire on their trigger and stay quiet on baseline; 5 triage cases ≥ 4 correct; quiz ≥ 80%.
- **Further reading:** NIST SP 800-92, *Guide to Computer Security Log Management*; MITRE ATT&CK (attack.mitre.org); Sigma rule repo (SigmaHQ); CISA *Detection Playbooks* / *USCCD* resources.

---

### M14 — Incident Response and Digital Forensics

- **Level / Difficulty:** Level 3 · Advanced
- **Prerequisites:** M13, M05.
- **Measurable learning outcomes:**
  1. Write an incident response plan aligned with NIST SP 800-61 Rev. 3 (prepare, detect & analyze, contain/eradicate/recover, post-incident) including roles, comms, and escalation. *(Create)*
  2. Execute the collection of volatile and non-volatile digital evidence in correct order and document chain of custody. *(Apply)*
  3. Reconstruct a timeline from disk, log, and filesystem artifacts (timestamps, prefetch/journal/shell-history equivalents) to answer investigation questions. *(Analyze)*
  4. Run a tabletop exercise for a given scenario and produce a lessons-learned report. *(Apply)*
- **Core concepts:** incident response lifecycle (NIST SP 800-61r3, CSF 2.0 Respond/Recover); incident classification and severity; evidence handling and chain of custody; order of volatility; disk/memory/filesystem forensics (imaging, hashing, metadata, timestamps — NTFS MFT/USN, Linux inode/`ext4` journal awareness); timeline analysis; log correlation; containment strategies; legal/privacy considerations; post-incident learning; business continuity/DR basics (RTO/RPO).
- **Practical lab scenarios:**
  1. *IR plan:* write a 2–3 page IR plan for a small organization (10 users) covering preparation through post-incident, with a contact/escalation table.
  2. *Forensic timeline:* receive a provided (benign, synthetic) evidence bundle — disk image + logs; image, hash (SHA-256), carve, and build a chronological timeline answering 5 investigation questions.
  3. *Tabletop:* run a ransomware-in-lab tabletop (written exercise): decisions at each phase documented, including containment trade-offs and recovery validation.
- **Tools & estimated cost:** Autopsy/The Sleuth Kit (free), `fls`/`mactime`/`icat` CLI (free), Volatility-free alternatives noted where applicable, Wireshark, log analysis scripts. Provided synthetic evidence bundles only. **$0.**
- **Evidence / deliverables:** IR plan document + forensic report (chain of custody, hash values, timeline table, answers to 5 questions) + tabletop action log.
- **Knowledge-check format:** 14-question quiz (9 MCQ + 5 applied sequencing questions, e.g., correct evidence order). ≥ 80%.
- **Estimated study time:** 18–20 hours.
- **Completion criteria:** Timeline answers ≥ 4/5 correct with cited artifacts; IR plan passes provided completeness checklist; quiz ≥ 80%.
- **Further reading:** NIST SP 800-61r3 (Apr 2025); NIST SP 800-86, *Guide to Integrating Forensic Techniques*; NIST SP 800-101 (mobile forensics awareness); CISA *Incident Response Playbook* templates (cisa.gov).

---

### M15 — Malware Concepts and Defensive Analysis

- **Level / Difficulty:** Level 3 · Advanced
- **Prerequisites:** M05, M06, M14.
- **Measurable learning outcomes:**
  1. Classify malware by vector, payload, propagation, and business model, and explain how modern malware uses encryption/packing. *(Understand)*
  2. Perform **static** triage of a benign/controlled sample: hashing, strings, imports, packer detection, YARA rule matching. *(Apply)*
  3. Perform **dynamic** analysis of a controlled sample inside an isolated sandbox VM and document observed behavior (files, registry/config, network attempts). *(Apply)*
  4. Translate observations into defensive actions: detection rules (YARA/Sigma), IOCs, and IR playbook updates. *(Apply)*
- **Core concepts:** malware families (ransomware, trojans, worms, infostealers, botnets, fileless techniques); attack chain (delivery → execution → persistence → C2 → actions); packing/obfuscation; hashes and IOC types (hashes, domains, paths, behavioral); YARA rules; sandboxing and detonation safety; MITRE ATT&CK for malware behaviors; mapping analysis output to detection engineering; safe sample handling.
- **Practical lab scenarios:**
  1. *Safe triage:* analyze 2 benign "training" binaries you build yourself (a small program you compile that exhibits marker behaviors — e.g., writes a file, sets a startup entry **in the VM only**, and performs a harmless DNS lookup to a domain you control or `localtest`-style local target): hash, strings, imports, behavior.
  2. *YARA authoring:* write 3 YARA rules matching your training binaries' features; verify with `yara` CLI; iterate to avoid false positives on system files.
  3. *IOC handoff:* produce an IOC package (STIX-lite JSON or simple CSV) + 2 Sigma rules mapping behaviors to ATT&CK techniques; feed them into your M13 detection setup and trigger them in-lab.
- **Tools & estimated cost:** Isolated VM with snapshots (free), YARA (free), `file`/`sha256sum`/`strings`/`ssdeep` (free), Sysmon (free) in the analysis VM, optionally Ghidra (free) for statics. **No real-world malware required** — self-built training binaries + documented benign samples from course materials. **$0.**
- **Evidence / deliverables:** Two triage reports (static + dynamic) with evidence + 3 verified YARA rules + IOC package + 2 Sigma rules integrated with M13.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 analysis scenarios). ≥ 80%.
- **Estimated study time:** 16–18 hours.
- **Completion criteria:** Both triage reports include observed-behavior evidence from the sandbox; YARA rules match targets and not clean files; IOC/Sigma handoff demonstrated; quiz ≥ 80%.
- **Further reading:** MITRE ATT&CK software/technique pages for malware behaviors (attack.mitre.org); YARA documentation (virustotal.github.io/yara); CISA #StopRansomware guidance and joint government malware-analysis guidance (cisa.gov); OWASP *Malware* awareness documentation.

---

# Level 4: Advanced Security and Capstone

*Goal: operate at program level — cloud, privacy/compliance, automation, and an integrated capstone that demonstrates the whole pathway. Difficulty: Advanced.*

---

### M16 — Cloud and Infrastructure Security

- **Level / Difficulty:** Level 4 · Advanced
- **Prerequisites:** M05, M08, M11.
- **Measurable learning outcomes:**
  1. Explain the shared responsibility model across IaaS/PaaS/SaaS and assign responsibility correctly for 10 given scenarios. *(Understand)*
  2. Secure a container workload: hardened image, non-root user, no secrets in images, resource limits, and vulnerability scanning. *(Apply)*
  3. Apply infrastructure-as-code security: IaC misconfiguration scanning and least-privilege identity for cloud-like services (local emulated or provider free tier, optional). *(Apply)*
  4. Evaluate cloud-specific risks (misconfiguration, over-permissive storage/roles, shadow IT, logging gaps) against CIS cloud-adapted controls. *(Evaluate)*
- **Core concepts:** cloud service/deployment models; shared responsibility; IAM in cloud; security groups vs. NACLs (conceptual); object storage security; container security (image provenance, runtime, registry scanning); Kubernetes basics and its attack surface (awareness); IaC security (Terraform/Compose scanning); cloud logging/audit trails; CWPP/CSPM/CASB awareness; infrastructure-as-code drift; secrets in CI; resilience and backup in cloud.
- **Practical lab scenarios:**
  1. *Container hardening:* take a vulnerable container image (e.g., a DVWA container or course-provided image), produce a hardened derivative, scan it with Trivy, and show a clean/near-clean scan; run as non-root with a read-only filesystem where feasible.
  2. *Compose/IaC review:* audit a provided Docker Compose / Terraform config for 8 issues (privileged mode, host mounts, plaintext secrets, open ports, missing resource limits); fix and rescan.
  3. *Cloud design review:* assess a provided reference architecture (static website + API + storage) for misconfigurations using a CIS-inspired checklist; optional: reproduce one item on a free-tier provider **only if you control the account**.
- **Tools & estimated cost:** Docker Engine/Podman (free), Trivy/Checkov (free), local Kubernetes (kind/k3s, free) optional. Optional provider free tiers only — **no paid cloud required. $0.**
- **Evidence / deliverables:** Hardened image + before/after scans + IaC audit sheet (8 issues) + architecture review memo.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 scenario/shared-responsibility questions). ≥ 80%.
- **Estimated study time:** 16–18 hours.
- **Completion criteria:** Container runs hardened and scanned; 8 IaC issues fixed and verified; quiz ≥ 80%.
- **Further reading:** AWS/azure/gcp shared-responsibility documentation (official docs); CIS Benchmarks for Docker/Kubernetes (cisecurity.org); NIST SP 800-204 series (container security awareness); Trivy & Checkov documentation.

---

### M17 — Privacy, Data Protection, Risk Management, and Compliance

- **Level / Difficulty:** Level 4 · Advanced
- **Prerequisites:** M02, M03. M11 recommended.
- **Measurable learning outcomes:**
  1. Distinguish privacy, confidentiality, and security; classify data (personal, sensitive/special-category, derived) in a given scenario. *(Understand)*
  2. Build a data-flow map and complete a Data Protection Impact Assessment (DPIA)-style worksheet for a small system. *(Apply)*
  3. Select and map controls across two frameworks (e.g., CSF 2.0 Functions ↔ CIS v8.1 ↔ ISO/IEC 27001:2022 Annex A) for a scoped case. *(Apply)*
  4. Explain privacy-by-design principles and evaluate a system design against them. *(Evaluate)*
- **Core concepts:** data minimization, purpose limitation, storage limitation, consent; privacy by design/default; DPIA methodology; de-identification vs. anonymization and re-identification risk; privacy frameworks (NIST Privacy Framework 1.0, ISO/IEC 27701 awareness); GDPR principles overview; Pakistan context (PECA 2016 as amended, Personal Data Protection bill awareness — status noted as evolving); risk management integration (CSF 2.0 Govern function); control frameworks and cross-mapping; audit evidence and compliance artifacts.
- **Practical lab scenarios:**
  1. *DPIA worksheet:* complete a DPIA for a student-health-app scenario: data inventory, flows, risks, mitigations, sign-off fields.
  2. *Control mapping:* map 15 controls for the same scenario across CSF 2.0 functions and CIS v8.1 (spreadsheet) and flag gaps.
  3. *Privacy critique:* analyze 3 real product privacy incidents (public post-mortems) for principle violations and design fixes.
- **Tools & estimated cost:** Spreadsheet or Markdown tables; NIST CSF/CIS resources (free); DPA/DPIA templates (free, e.g., ICO-style template structure). **$0.**
- **Evidence / deliverables:** Data-flow map + completed DPIA + control mapping table with gap analysis.
- **Knowledge-check format:** 12-question quiz (8 MCQ + 4 scenario). ≥ 80%.
- **Estimated study time:** 12–14 hours.
- **Completion criteria:** DPIA covers all worksheet sections; mapping has ≥ 15 rows with 2+ gaps identified; quiz ≥ 80%.
- **Further reading:** NIST Privacy Framework 1.0 (nist.gov/privacy-framework); ICO DPIA guidance template structure (ico.org.uk); ISO/IEC 27001:2022 overview; NIST CSF 2.0 (Govern).

---

### M18 — Security Automation and Emerging Challenges

- **Level / Difficulty:** Level 4 · Advanced
- **Prerequisites:** M10, M13. M16 recommended.
- **Measurable learning outcomes:**
  1. Automate a recurring security task end-to-end (script → schedule → alert → report) with failure handling. *(Apply)*
  2. Build a mini security-pipeline combining scanning, detection, and notification (security-as-code/detection-as-code). *(Apply)*
  3. Analyze an emerging challenge — AI/ML security (prompt injection, model/data poisoning, AI-assisted attacks and AI-assisted defense), supply-chain attacks, or ransomware trends — and produce an evidence-based brief. *(Analyze)*
  4. Evaluate automation failure modes: alert fatigue, silent failure, and unsafe automation. *(Evaluate)*
- **Core concepts:** automation for security (Python/Bash/PowerShell; schedulers; webhooks); IaC and policy-as-code; detection-as-code; SOAR concepts; CI/CD security gates; AI/ML security fundamentals (adversarial ML, data poisoning, LLM/app-sec risks — OWASP LLM Top 10 awareness); AI use policy in security work; supply-chain attacks (conceptual case studies); ransomware trends and initial-access brokers (awareness); keeping detections current with evolving ATT&CK.
- **Practical lab scenarios:**
  1. *Automated hygiene bot:* script that (on schedule) checks lab hosts for baseline drift (open ports, package updates, failed logins), writes a report, and emails/logs alerts — demonstrated with a planted drift event.
  2. *Security pipeline:* one local pipeline (shell/Makefile/GitHub-Actions-style YAML run locally) that runs Trivy + Semgrep + Gitleaks + your M13 Sigma tests and fails on findings.
  3. *Emerging-threat brief:* a 600–800-word brief on one emerging topic with ≥ 3 credible sources (vendor/researcher/org), including implications for a small organization and 3 recommended controls.
- **Tools & estimated cost:** Python/stdlib, cron/Task Scheduler (free), Trivy/Semgrep/Gitleaks (free), GitHub Actions minutes only if you already have them (local runner alternative provided). **$0.**
- **Evidence / deliverables:** Automation script + run log with planted-event evidence + pipeline config/log + emerging-threat brief.
- **Knowledge-check format:** 10-question quiz (6 MCQ + 4 short answer). ≥ 80%.
- **Estimated study time:** 14–16 hours.
- **Completion criteria:** Automation demonstrably detects a planted event; pipeline fails-then-passes; brief meets length and sourcing; quiz ≥ 80%.
- **Further reading:** OWASP Top 10 for LLM Applications (owasp.org/www-project-owasp-top-10-for-large-language-model-applications); NIST AI RMF 1.0 (nist.gov/itl/ai-risk-management-framework); Sigma/Trivy/Semgrep docs; CISA secure-by-design guidance (cisa.gov/securebydesign).

---

### M19 — Integrated Capstone Project

- **Level / Difficulty:** Level 4 · Advanced
- **Prerequisites:** M01–M18 (Levels 1–3 required; M16–M18 strongly recommended before starting).
- **Measurable learning outcomes:** *(Synthesis across the course)*
  1. Design and document a security architecture for a realistic small-organization scenario, including threat model (STRIDE) and control selection mapped to CSF 2.0/CIS v8.1. *(Create/Evaluate)*
  2. Implement and evidence baseline hardening (host + network + access control) in a reproducible lab. *(Apply)*
  3. Execute an authorized assessment of the implemented environment and deliver a professional report. *(Apply/Analyze)*
  4. Deploy monitoring, write ≥ 4 detections, and demonstrate detect → triage → respond through a simulated incident with forensic evidence. *(Apply/Analyze)*
  5. Produce a final package: architecture docs, threat model, assessment report, detection/IR evidence, privacy/compliance note, and lessons learned. *(Create)*
- **Core concepts:** security program integration; documentation and reproducibility; stakeholder communication; risk communication; portfolio presentation; professional reporting standards; retrospective/self-assessment.
- **Practical lab scenario (integrated):**
  1. *Scenario:* secure a fictional 15-person startup's web application + internal network (provided scenario brief with business constraints and budget = $0). Deliverables in five stages:
     - **Stage A — Architecture & threat model** (DFD, STRIDE, controls).
     - **Stage B — Implementation** (hardened hosts, segmentation, IAM, TLS).
     - **Stage C — Assessment** (authorized VA report against the built environment).
     - **Stage D — Defend** (logging, 4 detections, simulated incident + forensic timeline).
     - **Stage E — Privacy & close-out** (data-flow/DPIA-lite note + lessons learned + reflection).
- **Tools & estimated cost:** Everything from prior modules (all free); VM snapshots; provided templates. **$0.**
- **Project brief:** the full capstone package in [docs/capstone](./capstone/README.md) — alternative scenario briefs, a seven-stage workflow with milestone gates (the seven workflow stages roll up to the five graded stages below), report/risk-register/threat-model/findings templates, a seven-dimension rubric, and completion/submission checklists.
- **Evidence / deliverables:** Capstone portfolio (5 stages) + 5-minute-style written walkthrough (README index) + reflection (500 words).
- **Knowledge-check format:** No separate quiz — the **capstone rubric** in the [Assessment Guide](./assessment-guide.md) is the evaluation instrument (self-assessed against rubric; optional peer review).
- **Estimated study time:** 30–40 hours (staged over ≥ 4 weeks recommended).
- **Completion criteria:** All 5 stages submitted; rubric ≥ "Proficient" overall and no stage below "Developing"; every stage traces to prior module skills; safety policy followed throughout (authorization statements included).
- **Further reading:** NIST SP 800-61r3 + CSF 2.0 (program integration); CIS v8.1 IG1 as the baseline set; SANS reading room / public post-mortems for report style; your own course notes as primary source.

---

## Progression rules and course completion

1. **Sequential by default.** Skipping ahead is allowed only when a module's prerequisites are demonstrably met (evidence: prior quiz ≥ 80% or an equivalent work sample).
2. **Level gates.** Before starting a level, complete all prior-level modules (quiz ≥ 80% + deliverables submitted).
3. **Course completion** requires:
   - All 19 modules completed to their stated completion criteria;
   - Overall assessment standing per the [Assessment Guide](./assessment-guide.md): portfolio + scenario exercises + investigations + capstone each ≥ 60%, and the capstone meeting its stage standard (≥ Proficient on 4 of 5 rubric criteria in every stage, no stage below Developing);
   - Lab Safety Policy acknowledgment on file (see [Lab Safety Policy](./lab-safety-policy.md));
   - A complete, indexed `portfolio/` of evidence.
4. **Re-entry after a break:** repeat the last module's knowledge check to reactivate context.

## Cross-references

- Program-level (course) learning outcomes and module mappings: [learning-outcomes.md](./learning-outcomes.md)
- Entry requirements, hardware/software, and pacing: [prerequisites.md](./prerequisites.md)
- Formative vs. graded components, weights, rubrics: [assessment-guide.md](./assessment-guide.md)
- Authorization, isolation, tool rules, prohibited activities: [lab-safety-policy.md](./lab-safety-policy.md)
- Curated standards and official documentation (NIST, OWASP, CISA, MITRE), tools directory, glossary, learning pathways, and the troubleshooting/independent-study guide: [Reference Library](./reference/README.md)
