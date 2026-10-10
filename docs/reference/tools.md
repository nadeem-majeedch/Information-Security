---
title: "Tools Directory — Free Security Tooling by Purpose"
layout: default
---

# Tools Directory — Free Security Tooling by Purpose

**Part of:** [Reference Library](README.md) · Every tool here is **free or free-tier** and is used (or explicitly offered as an alternative) in a required lab — **no paid product is necessary to complete any core lab or the capstone.** Entries: what it's for → where the course uses it → official docs → access notes.

> **Standing rule:** tools are only run against **your own lab** or **course-provided artifacts**, inside your RoE. Dual-use tools (scanners, proxies) are lawful-by-scope, not by intent. See the [Lab Safety Policy](../lab-safety-policy.md).

## 1. Network analysis and packet capture

| Tool | Purpose (why it's here) | Course use | Official docs | Access |
|---|---|---|---|---|
| **Wireshark** | Interactive packet capture/analysis — see what the wire actually carried; the "ground truth" view | M04, M07 · [LAB-07](../labs/lab-07-packet-analysis/README.md) | [wireshark.org/docs](https://www.wireshark.org/docs/) | Free (open source) |
| **tcpdump** | Headless capture when Wireshark's GUI can't fit (servers, VMs) | M04, LAB-07 alternates | [github.com/the-tcpdump-group/tcpdump](https://github.com/the-tcpdump-group/tcpdump) (official repo; man page source included — tcpdump.org was unreachable from our checker 2026-10-10, see [flagged](README.md#flagged-for-review-version-sensitive-or-blocked)) | Free |
| **Zeek (optional)** | Network monitor that *derives* logs (conn/http/ssl records) — closer to real SOC network data | M13 enrichment | [docs.zeek.org](https://docs.zeek.org/) | Free (open source) |

## 2. Discovery and scanning (lab targets only)

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **Nmap** | Host/port/service discovery and version detection — the reconnaissance phase of an authorized assessment | M08, M12 · [LAB-08](../labs/lab-08-firewall-config-audit/README.md), [LAB-12](../labs/lab-12-vuln-scan-interpretation/README.md) | [nmap.org/book/man.html](https://nmap.org/book/man.html) | Free |
| **Greenbone/OpenVAS (optional Tier)** | Full vuln-scanner alternative when you want CVE-level output at scale | M12 alternative | [greenbone.net](https://www.greenbone.net/) / [docs.greenbone.net](https://docs.greenbone.net/) | Free (open source; heavy — 8 GB+ RAM) |
| **masscan (optional)** | Large-range speed scanner — *learn what it does so you understand rate/impact limits*, then never point it outside your lab | M12 concept | [github.com/robertdavidgraham/masscan](https://github.com/robertdavidgraham/masscan) | Free |

## 3. Authentication, log, and data analysis

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **journalctl / dmesg** | Read systemd journals — first place to look on a Linux host | M05, M13 | [systemd.io](https://systemd.io/) (or `man journalctl` locally) | Free (built in) |
| **auditd** | Kernel-level file/access auditing for high-value targets | M13 Tier-b | [audit-userspace](https://github.com/linux-audit/audit-userspace) | Free |
| **grep / awk / sed + jq** | The log-analysis workhorses; `jq` makes JSON logs (cloud, app) usable | M13, LAB-13, M17 | [jqlang.github.io/jq](https://jqlang.github.io/jq/) | Free |
| **Python 3 (stdlib)** | Timelines, analyzers, bot scripts — the course standardizes on stdlib so nothing needs installing | M13, M14, M18 | [docs.python.org/3/](https://docs.python.org/3/) | Free |
| **Sigma + your SIEM of choice** | Portable detection rules converted to your backend | M13, M15, M19 | [github.com/SigmaHQ/sigma](https://github.com/SigmaHQ/sigma) | Free |

## 4. Vulnerability and exposure management

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **NVD / CVE lookups** | Validate scanner claims against authoritative records | M10, M12 | [nvd.nist.gov](https://nvd.nist.gov/) · [cve.org](https://www.cve.org/) | Free (NVD API: free key) |
| **CISA KEV catalog** | "Is it exploited in the wild?" — prioritization evidence | M12, M19 | [cisa.gov/known-exploited-vulnerabilities-catalog](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) | Free |
| **FIRST CVSS calculators** | Produce the vector strings your findings must cite | M09, M12, M19 | [first.org/cvss/calculator/4.0](https://www.first.org/cvss/calculator/4.0) | Free |

## 5. Web application testing (local apps only)

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **OWASP ZAP** | Intercepting proxy: watch/modify your local app's traffic; passive scan | M09, M12 · [LAB-10](../labs/lab-10-web-security/README.md) | [zaproxy.org](https://www.zaproxy.org/) | Free (open source) |
| **Browser dev tools** | Request inspection, storage/cookie review, header checks — the zero-install baseline | M09, [LAB-11](../labs/lab-11-headers-tls-analysis/README.md) | vendor docs (any modern browser) | Free (built in) |
| **OWASP Juice Shop / DVWA / WebGoat** | Deliberately vulnerable targets — *the only things you may attack* | M09, M12, M19 | [juice-shop](https://owasp.org/www-project-juice-shop/) · [DVWA](https://github.com/digininja/DVWA) · [WebGoat](https://owasp.org/www-project-webgoat/) | Free |
| **Burp Suite Community (optional)** | Industry-standard proxy; the tool you'll meet at work | M09 alternative | [portswigger.net/burp/documentation](https://portswigger.net/burp/documentation) | Free edition (registration); Pro is paid — **never required** |

## 6. Code, secrets, and supply-chain analysis

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **Semgrep (Community)** | SAST with readable rules — finds "user input → sink" patterns in *your* code | M10, M18 · [LAB-09](../labs/lab-09-secure-coding/README.md) | [semgrep.dev/docs](https://semgrep.dev/docs/) | Free CE (registry extras paid — not needed) |
| **Gitleaks** | Secret detection in code and git history | M10, M18 | [github.com/gitleaks/gitleaks](https://github.com/gitleaks/gitleaks) | Free |
| **pip-audit / npm audit** | Dependency CVE checking for your stack | M10, M18 | [pypi.org/project/pip-audit](https://pypi.org/project/pip-audit/) · [docs.npmjs.com](https://docs.npmjs.com/) | Free |
| **Trivy** | Container image + IaC misconfiguration scanning | M10, M16, M18 | [trivy.dev](https://trivy.dev/) | Free (open source) |
| **Dependency-Check / CycloneDX (optional)** | OWASP-native dependency scanning + SBOM generation | M10 enrichment | [OWASP dependency-check](https://owasp.org/www-project-dependency-check/) · [cyclonedx.org](https://cyclonedx.org/) | Free |

## 7. Cryptography, secrets, and identity tooling

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **OpenSSL** | Encrypt/decrypt, keypair and CSR generation, TLS inspection (`s_client`) | M06, M11 · [LAB-05](../labs/lab-05-hashing-integrity-signatures/README.md) | [docs.openssl.org](https://docs.openssl.org/) | Free |
| **GnuPG** | Asymmetric signing/encryption workflow | M06, LAB-05 | [gnupg.org/documentation](https://gnupg.org/documentation/) | Free |
| **Python `cryptography`** | Correct primitives in scripts (AES-GCM, signing, Argon2 via `argon2-cffi`) | M06, M10 | [cryptography.io](https://cryptography.io/) | Free |
| **hashcat / John the Rimaster (offline, course hashes only)** | Demonstrate password-cracking cost against **course-provided hash files** | M03, [LAB-03](../labs/lab-03-password-hashes/README.md) | [hashcat.net/wiki](https://hashcat.net/wiki/) · [openwall.com/john](https://openwall.com/john/) | Free |
| **KeePassXC / Bitwarden (free tier)** | Password-manager hygiene practice (M07 deliverable) | M07 | [keepassxc.org](https://keepassxc.org/) · [bitwarden.com/help](https://bitwarden.com/help/) | Free / freemium |
| **Vault (community)** — optional | Real secrets-management concepts at small scale | M07, M18 enrichment | [developer.hashicorp.com/vault/docs](https://developer.hashicorp.com/vault/docs) | Free (open source) |

> Cracking tools run **only** against course datasets on your machine. Pointing them at any hash you don't own is out of scope — no exceptions.

## 8. Detection engineering, monitoring, and SIEM

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **Suricata** | IDS/IPS with signature rules — alert generation for the detection labs | M08, M13 | [docs.suricata.io](https://docs.suricata.io/) | Free (open source) |
| **Wazuh** (Tier-a option) | Full stack: log indexing, rules, dashboards | M13, [LAB-18](../labs/lab-18-security-automation/README.md) | [documentation.wazuh.com](https://documentation.wazuh.com/) | Free (open source) |
| **Elastic Stack (optional Tier)** | The classic open SIEM path (Elasticsearch/Logstash/Kibana) | M13 alternative | [elastic.co/guide](https://www.elastic.co/guide/) | Free (license tiers — basic features free) |
| **scripted analyzer + cron (Tier-b)** | The lightweight path: parse, report, alert — zero stack | M13, LAB-18 | [Python docs](https://docs.python.org/3/) | Free |
| **fail2ban (optional)** | Auto-ban repeated auth failures at the host | M13 quick win | [github.com/fail2ban/fail2ban](https://github.com/fail2ban/fail2ban) | Free |

## 9. Forensics and incident response

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **The Sleuth Kit / Autopsy** | Disk-image parsing, timeline, file recovery | M14 · [LAB-15](../labs/lab-15-digital-forensics/README.md) | [sleuthkit.org](https://www.sleuthkit.org/) · [autopsy.com](https://www.autopsy.com/) | Free |
| **Volatility 3** | Memory analysis (processes, injected code, connections) | M14 | [volatility3.readthedocs.io](https://volatility3.readthedocs.io/) | Free |
| **plaso/log2timeline** (optional) | Super-timeline generation from many artifact types | M14 depth | [plaso.readthedocs.io](https://plaso.readthedocs.io/) | Free |
| **sha256sum / certutil** | Evidence integrity hashing — first step of every collection | M14 (chain of custody) | OS built-ins | Free (built in) |
| **CISA IR playbooks (template)** | Structure for your incident plan | M14, M19 | [cisa.gov playbooks](https://www.cisa.gov/resources-tools/resources/federal-government-cybersecurity-incident-and-vulnerability-response-playbooks) | Free (PDF) |

## 10. Malware triage (benign samples only — isolated VM)

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **YARA** | Pattern rules over files/memory for sample family matching | M15 · [LAB-16](../labs/lab-16-malware-behavior/README.md) | [yara.readthedocs.io](https://yara.readthedocs.io/) | Free |
| **strings / file / sha256sum** | First-minute static triage | M15 | OS built-ins | Free (built in) |
| **REMnux / FLARE-VM (optional distros)** | Purpose-built analysis VM images | M15 depth | [remnux.org](https://remnux.org/) · [github.com/mandiant/flare-vm](https://github.com/mandiant/flare-vm) | Free (VM image + some tools) |

> Analysis discipline: **self-built benign binaries or provided report artifacts only**, in an isolated VM with no shared folders. Live malware handling is out of scope for this course.

## 11. Cloud, container, and IaC

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **Docker / Podman** | Containerized lab targets; hardened images | M10, M16, M19 | [docs.docker.com](https://docs.docker.com/) · [podman.io](https://podman.io/) | Free (Podman fully free; Docker Desktop may need a license for large orgs) |
| **Terraform (CLI) + Checkov/tfsec** | IaC authoring and misconfiguration scanning | M16 · [LAB-17](../labs/lab-17-cloud-config-review/README.md) | [developer.hashicorp.com/terraform/docs](https://developer.hashicorp.com/terraform/docs) · [github.com/bridgecrewio/checkov](https://github.com/bridgecrewio/checkov) | Free |
| **Prowler (optional)** | Cloud security posture assessment — run on a cloud account **you own** | M16 depth | [docs.prowler.com](https://docs.prowler.com/) | Free (open source) |
| **draw.io / diagrams.net** | DFDs, trust boundaries, network diagrams | M11, M19 | [app.diagrams.net](https://app.diagrams.net/) | Free (incl. offline) |

## 12. Documentation, versioning, and study workflow

| Tool | Purpose | Course use | Official docs | Access |
|---|---|---|---|---|
| **Git + GitHub/GitLab (free tier)** | Version your portfolio; hooks for secret scanning; detection-as-code | M10, M18, M19 | [git-scm.com/doc](https://git-scm.com/doc/) | Free |
| **Markdown editor / VS Code (free)** | Portfolio authoring; Mermaid for diagrams | all | [code.visualstudio.com/docs](https://code.visualstudio.com/docs/) | Free |
| **Make / cron / systemd timers** | Scheduling the automation deliverables | M18 | [systemd.io](https://systemd.io/) | Free (built in) |

---

**Choosing a path:** every "Purpose" above has exactly one *default* tool in the course — use it unless a lab offers a tier choice (M13 does). Alternatives are marked *(optional)* and are for learners who want breadth. When you meet a paid tool at work, the concepts transfer: the [tools directory](tools.md) is organized by *job*, not by vendor.

**Next:** [Glossary](glossary.md) · [Learning pathways](pathways.md) · [Reference library](README.md)
