---
title: "Prerequisites"
layout: default
---

# Information Security — Prerequisites

**Course:** Information Security: A Self-Study Course from Beginner to Advanced
**Instructor:** Engr. Dr. Muhammad Nadeem Majeed — Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore, Pakistan
**Status:** DRAFT for instructor review · **Version:** 0.1 · **Last verified:** 2026-10-09
**Companion documents:** [Course Roadmap](./course-roadmap.md) · [Learning Outcomes](./learning-outcomes.md) · [Assessment Guide](./assessment-guide.md) · [Lab Safety Policy](./lab-safety-policy.md) · [Reference Library](./reference/README.md)

---

## 1. Who this course is for

- **Primary audience:** self-study learners — students, early-career IT staff, and career-changers — with no prior information-security background.
- **Also suitable for:** instructors adopting the material, and security-adjacent professionals (developers, data engineers, network admins) who want a structured path from foundations to applied assessment and defense.
- **Not required:** enrollment in a university program, classroom attendance, instructor demonstrations, paid software, or access to organizational infrastructure.

## 2. Academic / knowledge prerequisites

| Area | Requirement | Notes |
|---|---|---|
| General computing | Comfortable using a computer: files/folders, installing software, web browsing, basic troubleshooting | Assumed for all modules |
| English reading | Intermediate (B1+) reading ability | All references and documentation are in English |
| Mathematics | None beyond secondary-school algebra | Risk scoring and crypto are taught as applied skills, not proofs |
| Programming | **None to start.** Basic programming in any language becomes **required by M10** (Secure Programming) | If new to programming, complete a free intro-to-programming course (e.g., Python) before M10; see §4 |
| Networking | None — M04 builds from zero | — |
| Operating systems | None — M05 builds from zero, but comfort with a terminal helps | Prior Linux use is a bonus, not a requirement |
| Prior security courses | None | M01 assumes no security vocabulary |

**Self-check before enrolling (should all be "yes"):**
1. I can install software and manage files without assistance.
2. I can read technical documentation in English at a tutorial level.
3. I can commit to 8–12 hours per week for roughly 7–9 months.
4. I have (or can obtain) a computer meeting §3 hardware requirements.
5. I have read and agree to abide by the [Lab Safety Policy](./lab-safety-policy.md).

## 3. Hardware requirements

| Item | Minimum | Recommended | Why |
|---|---|---|---|
| CPU | 64-bit, 4 cores | 6+ cores with hardware virtualization (Intel VT-x / AMD-V) | Multiple VMs for labs (M04 onward); check BIOS/UEFI virtualization is enabled |
| RAM | 8 GB | 16 GB | Level 2–3 labs run 2–3 VMs (target, attacker, analysis) concurrently; 8 GB works with sequential VM use |
| Storage | 60 GB free | 100+ GB free, SSD | VM images, containers, forensic images (M14 disk images are GBs) |
| Network | Broadband internet | — | Downloading ISOs/tools; **lab traffic itself stays offline/host-only** (see safety policy) |
| Optional but useful | USB flash drive 8 GB+ (ISO writing, evidence transport), second monitor or large screen (packet/terminal work) | — | Total optional spend ≤ ~$10 |

**Total required cost: $0.** No cloud servers, no paid tools, no course fee.

## 4. Software prerequisites

All free and installable before Module 04 (earlier modules need only a Markdown editor and browser):

| Software | Purpose | Modules | License/cost |
|---|---|---|---|
| Markdown editor (VS Code, Obsidian, or even Notepad++) | Notes, deliverables, portfolio | All | Free |
| VirtualBox **or** VMware Workstation Player (personal use) | Lab VMs | M04–M19 | Free |
| Linux distro ISO (Ubuntu/Debian) | Lab VMs | M05 onward | Free |
| Windows: your own OS in a VM, or Microsoft's free developer VM evaluation images | Windows hardening lab | M05, M13–M15 | Free (evaluation images expire — rebuild as needed) |
| Wireshark | Packet analysis | M04 onward | Free |
| Nmap | Scanning (**lab IPs only**) | M04, M08, M12 | Free |
| OpenSSL / GnuPG | Crypto labs | M06 | Free |
| Juice Shop, DVWA, WebGoat (containers or local installs) | Deliberately vulnerable targets | M09, M12 | Free |
| Burp Suite Community **or** OWASP ZAP | Intercepting proxy | M09, M12 | Free |
| Suricata + ET Open rules | IDS | M08, M13 | Free |
| Autopsy / The Sleuth Kit, Volatility (optional) | Forensics | M14, M15 | Free |
| YARA | Malware pattern matching | M15 | Free |
| Docker Engine (or Podman) | Containers | M16, M18 | Free |
| Semgrep Community, Gitleaks, Trivy | Code/secret/container scanning | M10, M16, M18 | Free |
| Python 3 + standard library | Automation scripts | M10, M18 | Free |

Notes:
- **No paid subscriptions are required anywhere in the course.** Optional free tiers (e.g., Nessus Essentials personal license, Splunk Free) are mentioned as alternatives only.
- Install instructions and download sources are given in each module; verify checksums/signatures when the publisher provides them.
- Exact tool versions are pinned per-module at the time each module page is written; standards editions are tracked in the [Course Roadmap version table](./course-roadmap.md#reference-and-version-policy).

## 5. Lab environment and safety prerequisites

Before any hands-on module (M04+), each learner must:

1. **Read and acknowledge** the [Lab Safety Policy](./lab-safety-policy.md).
2. **Prepare an isolated lab network:** a host-only or internal VirtualBox/VMware network that does **not** route lab VMs to your home LAN or the internet for scanning purposes (walkthrough provided in M04).
3. **Confirm authorization scope:** all scanning and exploitation targets are (a) VMs you built, (b) deliberately vulnerable training apps you run locally, or (c) systems with **written** permission — never random public hosts, never an employer's or third party's production systems without a signed engagement.
4. **Use synthetic data only** for exercises involving records, credentials, or datasets.

## 6. Time commitment and pacing

| Pace | Weekly hours | Approx. duration (19 modules, ~300 h total) | Best for |
|---|---|---|---|
| Steady | 8–10 h | ~9 months | Working learners |
| Standard (default) | 10–12 h | ~7 months | Most self-study learners |
| Intensive | 15–20 h | ~5 months | Full-time learners |

Per-module estimates are listed in the [Course Roadmap](./course-roadmap.md). Level gates require all prior-level modules completed — see "Progression rules" at the end of the roadmap.

## 7. Skills gained without prerequisites vs. skills you must build along the way

- **Taught from zero in this course:** networking fundamentals (M04), OS hardening (M05), cryptography usage (M06), web security testing (M09), forensics (M14), malware triage (M15), automation (M18).
- **Bring or build before M10:** basic programming (variables, functions, loops, file I/O) in any language; Python recommended. Suggested free resources: python.org official tutorial, freeCodeCamp, or any university intro programming MOOC. Budget 15–30 hours if completely new.
- **Useful but optional:** prior Linux command-line use, a home router you are allowed to reconfigure, and any prior exposure to HTML/HTTP.

## 8. Language, accessibility, and support

- **Language:** instruction and assessments are in English; concept glossaries are provided in each module.
- **Accessibility:** all deliverables can be produced with free, cross-platform tools; labs can be run sequentially on 8 GB machines (no parallel-VM requirement); screen-reader-friendly Markdown outputs are expected.
- **Support model (self-study):** every module includes completion criteria, self-graded answer keys, and checklists so learners can verify progress without an instructor. Where a learner gets stuck, each module's "Further reading" lists official documentation first.

## 9. What you do NOT need

- No university login, campus network, or lab infrastructure.
- No paid software (all tools in §4 are free/open-source).
- No classroom, study group, or instructor demonstrations.
- No real-world targets, employer systems, or third-party permissions **unless** you are formally engaged — and if so, written authorization precedes any testing.
- No prior security certification (CEH, Security+, etc.) — this course builds toward that knowledge, not away from it.
