---
title: "Lab Safety Policy"
layout: default
---

# Information Security — Lab Safety Policy

**Course:** Information Security: A Self-Study Course from Beginner to Advanced
**Instructor:** Engr. Dr. Muhammad Nadeem Majeed — Professor, Department of Data Science (PUCIT), University of the Punjab, Lahore, Pakistan
**Status:** DRAFT for instructor review · **Version:** 0.1 · **Last verified:** 2026-10-09
**Companion documents:** [Course Roadmap](./course-roadmap.md) · [Learning Outcomes](./learning-outcomes.md) · [Prerequisites](./prerequisites.md) · [Assessment Guide](./assessment-guide.md)

> **Read this before any hands-on module (M04 onward). By attempting any lab in this course, you agree to be bound by this policy.**

---

## 1. Purpose and scope

This course teaches offensive *and* defensive security skills. The same techniques that protect systems can harm them when used without permission. This policy exists to keep every learner — and every stranger on the internet — safe.

**Scope:** every practical activity in this course, including scanning, exploitation attempts, packet capture, malware handling, credential testing, fuzzing, denial-of-service simulations, and any use of the tools listed in the [Prerequisites](./prerequisites.md) and module pages.

**Applies to:** you, your devices, your VMs, and any system you touch while following this course — regardless of intent.

## 2. The five non-negotiable rules

1. **Authorization first.** Test only systems you **own** or have **explicit, documented authorization** to test. No exceptions, no "just a quick scan," no "they won't notice."
2. **Isolate.** All offensive labs run on isolated lab networks (host-only/internal VM networks) or on deliberately vulnerable apps you run locally — never routed to your home LAN or the public internet as targets.
3. **No public targets.** Never scan, probe, log into, or exploit random public systems: not "example.com," not your ISP's equipment, not a neighbor's Wi-Fi, not a friend's site without written permission, not any host you found on Shodan/Censys.
4. **Defensive-only malware handling.** Real malware never leaves an isolated sandbox VM; this course is designed so you **do not need real-world malware samples** — training binaries you build yourself and course-provided benign samples are sufficient.
5. **Synthetic data only.** Never use real personal data (yours or others') in labs, submissions, or datasets.

**When in doubt: stop.** If an activity might affect a system outside your lab, do not proceed until you have re-read this policy and confirmed authorization in writing.

## 3. Authorized target list (what you MAY test)

| Target class | Allowed? | Conditions |
|---|---|---|
| VMs you created (VirtualBox/VMware/etc.) | ✅ Yes | On host-only/internal network per §4 |
| Deliberately vulnerable apps you run locally (Juice Shop, DVWA, WebGoat, Metasploitable-class images, custom training binaries) | ✅ Yes | Local or host-only; not exposed to the internet |
| Your own physical devices (your laptop, your phone, your router admin page) | ✅ Yes, with care | Non-destructive tests only; keep recovery paths (§7) |
| A system with **written** authorization naming you, the scope, and the dates | ✅ Yes | Follow the written scope exactly; keep the document |
| Course-provided synthetic evidence bundles and datasets | ✅ Yes | As designed |
| Employer / university / client production systems | ❌ No (this course) | This course does not authorize testing; if you are formally engaged at work, that engagement — not this course — must document scope |
| Third-party websites, APIs, or infrastructure found online | ❌ Never | Including "only recon," "only a 443 scan," or "low-and-slow" |
| Other people's devices, Wi-Fi, or accounts (family, friends, roommates) | ❌ Never | Even with verbal permission — this course requires written, scoped authorization |
| Public "practice" targets you don't own (random intentionally-vulnerable hostlists, shared instances) | ❌ No | Run the same target locally instead (all recommended apps are free) |
| Cloud accounts belonging to an organization | ❌ No | Only accounts **you personally created** and only free tiers |
| Any target for DoS/flood testing | ❌ Never | Even in labs, simulate load gently; never flood, and never touch anything outside your VMs |

**Written authorization template** (keep the signed copy with your work):

```text
AUTHORIZATION TO TEST — [Lab / Engagement name]
I, [name], owner/authorized representative of [system(s), IPs/hostnames, ranges],
authorize [your name] to perform security testing on the systems above,
from [date] to [date], using the scope and methods described in the attached scope note.
Out of scope: [list].
Emergency contact: [name, phone/email].
Signature: ____________________  Date: __________
```

For course labs, the "owner" is you; complete the template for your own lab as a discipline exercise (it is required evidence in M12).

## 4. Isolation requirements (how your lab must be built)

Required for every module from M04 onward:

1. **Host-only or internal network.** Lab VMs communicate with each other and the host — not with your home LAN. In VirtualBox: *Host-only Adapter*; in VMware: *Host-only*. Verify isolation before scanning (see §4.3).
2. **Never bridge lab VMs to your physical network.** Bridged mode puts vulnerable VMs on your home/office LAN where other devices — and your router — can be affected. Avoid bridged adapters for attack labs entirely.
3. **Isolation proof (mandatory evidence):** from the lab VM, confirm (a) it can reach other lab VMs, and (b) it **cannot** reach an internet address or a real LAN host. Screenshot the test (e.g., successful ping to lab peer + failed ping/curl to a public IP).
4. **Internet use by lab VMs** is fine for *updates and downloads* on a NAT adapter — but switch to host-only before any scanning/exploitation activity, or use two adapters (NAT for updates, host-only for the attack range) and only test on host-only addresses.
5. **Firewall safety net:** keep your host OS firewall on; do not share host folders with vulnerable VMs beyond what a lab needs; disable drag-and-drop and clipboard sharing for VMs that will run malware-analysis exercises (M15).
6. **Router rule:** never point scans from your lab at your own router's WAN side or your public IP. Test router settings through its admin UI only, non-destructively.
7. **Reset discipline:** snapshot VMs before each module so you can always roll back instead of escalating a problem.

### 4.3 Isolation checklist (run before every offensive lab)

- [ ] Lab network = host-only/internal (not bridged, not public)
- [ ] Ping/HTTP from lab VM to a public IP **fails**
- [ ] Ping/HTTP from lab VM to a real LAN device **fails**
- [ ] Lab VM → lab target connectivity **works**
- [ ] Only intended target IPs (the list you wrote down) will be scanned
- [ ] Snapshot taken

## 5. Tool usage rules

| Tool class | Rule |
|---|---|
| Scanners (Nmap, OpenVAS, nuclei, ZAP crawl) | Targets restricted to the authorized list; rate-limit; no stealth/DoS-ish flags needed in labs — and never against non-lab hosts |
| Exploit frameworks (Metasploit etc.) | Only against lab VMs; never against your host OS, router, or any shared system |
| Intercepting proxies (Burp/ZAP) | Point only at local lab apps or sites you own |
| Packet capture (Wireshark) | Capture on your own machine/lab interfaces only — never on networks you don't own (capturing others' traffic is illegal in many jurisdictions) |
| Password/credential tools (hydra, john, hashcat) | Lab-generated hashes/credentials only; never against real accounts, logins, or Wi-Fi you don't own |
| Denial-of-service / flood / stress tools | Not used in this course; simulate "availability" concepts via configuration review, not traffic generation |
| Malware tools (YARA, debuggers, sandboxes) | Inside the isolated analysis VM only; no live samples on the host |
| Cloud/automation tools | Only in accounts you personally own; free tiers; never against employer/organization tenants |
| Remote-access tooling (SSH, reverse shells) | Only to/from your own lab VMs |

**Tool intent is not a defense.** Legality is judged by *what you touched and whether you were authorized*, not by why you did it. "I was only practicing" is not authorization.

## 6. Prohibited activities (course-wide)

The following are never part of this course and may not be performed "while learning":

1. Scanning/probing/exploiting any system outside the authorized list (§3).
2. Accessing, downloading, or exfiltrating data from systems you don't own — even if "it was open."
3. Buying, trading, or requesting real stolen credentials, zero-day exploits, or malware from underground sources.
4. Testing on public targets "to be sure it works" before or after lab exercises.
5. Bypassing security controls of SaaS accounts (yours or others'), paywalls, DRM, or anti-cheat systems.
6. Disrupting services: flooding, resource exhaustion, jamming, or sustained high-rate scanning — anywhere.
7. Real-world social engineering of any person (phishing colleagues/family "as a demo," pretexting, vishing). Course social-engineering modules are **design-and-analysis exercises** using provided samples, never live campaigns against people.
8. Releasing malware, worms, or ransomware — including "harmless" ones — outside an isolated VM (no self-propagating code, ever).
9. Modifying or tampering with evidence in investigation exercises, or fabricating lab evidence.
10. Teaching these techniques to others for unauthorized use, or reselling course lab access to run attacks.

Violating §6 while submitted work depends on it triggers the safety gate in the [Assessment Guide](./assessment-guide.md) §7.

---

## 7. Protecting yourself (learner safety)

1. **Backups first.** Any lab that touches your real machine requires a current backup (3-2-1 rule from M05). Prefer VMs so rollback is a snapshot away.
2. **No destructive tests on daily drivers.** Password cracking, registry/config surgery, and malware-adjacent work happen in VMs — never on the OS you need for work/school.
3. **Account safety.** Use dedicated lab accounts/emails for registrations; never reuse your real passwords in lab apps; keep your primary email/2FA untouched by exercises.
4. **Disk-image hygiene.** Downloaded VM images and evidence bundles: verify checksums/signatures when published; scan downloads before opening.
5. **Suspicious sample rule.** If any sample or file seems genuinely dangerous (unexpected family, no course provenance), do not open it outside a disposable VM; delete and use the course-provided alternative.
6. **Legal self-protection.** Keep your isolation screenshots, authorization templates, and this policy acknowledgment with your portfolio. If anyone ever asks what you were doing, this documentation is your answer.
7. **Well-being.** Security content can include unsettling material (breach data, threat cases). Course case studies use public/summaries; skip graphic detail as needed.

## 8. Data handling rules

| Rule | Detail |
|---|---|
| Synthetic only | Labs use course-provided or self-generated datasets; never real customer/patient/student/personal records |
| No real credentials | Invent lab credentials; never paste your own real passwords, API keys, or tokens into exercises |
| Redact evidence | Screenshots must not expose your real emails, phone numbers, IDs, home addresses, or keys — blur/mask before submitting |
| Dispose properly | Reset lab VMs to snapshots after malware/attack modules; delete extracted artifacts from your host when the module is done |
| Public repos | Never commit live credentials, private keys, real personal data, or malware samples to GitHub (or anywhere public) |
| Privacy in reports | Investigation reports use aliases for any named individuals in provided scenarios |

## 9. Incidents and mistakes — what to do

**If you accidentally touched a non-lab system (wrong IP, misconfigured range, a scan escaped the lab):**
1. **Stop immediately.** Terminate the tool; do not "check one more thing."
2. **Do not panic-delete.** Note the time, tool, target(s), and what was sent — this is evidence you'll need if asked.
3. **Contain:** disconnect the lab network (host-only should already prevent most exposure — verify).
4. **Assess:** did data change or was anything accessed? Misdirected scans are usually visible only in logs.
5. **If harm was possible:** contact the system owner through their public security contact / abuse address and disclose honestly — most laws and all ethical codes treat prompt good-faith disclosure far better than concealment. Course staff/instructor channels apply for course-run environments.
6. **Document** the incident as a short write-up; use it in your M13/M14 learning (incident handling is part of this course) — and re-run the §4.3 isolation checklist before continuing.

**If you suspect malware escaped the analysis VM:** disconnect the VM (host-only means no network to exfiltrate through — this is why isolation is mandatory), take no files out of the VM, snapshot-delete the VM, and run a scan on your host. This is also why §2 rule 4 exists: the course never requires samples dangerous enough for this to be likely.

**Report course-environment issues** (a provided lab behaving unexpectedly, a leaked credential in course materials, a bad default config) to the instructor/repository issue tracker with the tag `safety` — fixes to shared labs protect every learner.

## 10. Responsible disclosure (when you find something real)

Sometimes you notice a genuine vulnerability in a service you legitimately use (a bug in your bank's app, a misconfigured bucket belonging to a company). This course **never** authorizes you to test it further — but it does teach you to behave responsibly:

1. **Do not exploit, copy, or exfiltrate data** — even to "prove it."
2. **Minimize interaction:** note the URL/endpoint, stop.
3. **Report privately** via the vendor's published security contact or a documented vulnerability-disclosure program (many publish `security.txt` — see RFC 9116).
4. **Give reasonable time**; do not publicly disclose before remediation or agreed timeline.
5. **Never demand reward** or threaten publication.

Useful templates and rules of engagement appear in M03 (ethics) and M12 (RoE). Reference: OWASP *Responsible Disclosure* guidance; vendor `security.txt` files.

## 11. Acknowledgment

Complete once, before Module 04, and keep it in your portfolio:

```text
LAB SAFETY POLICY ACKNOWLEDGMENT
I have read the Information Security Lab Safety Policy (v0.1).
I understand that I may test only systems I own or have written authorization to test,
that all offensive labs run on isolated networks, that I will use synthetic data only,
and that violations end my participation in this course.
Name: ____________________   Date: __________
Signature: ____________________
Isolation checklist completed for my lab: [ ] yes  (see §4.3)
```

## 12. Policy review

This policy is reviewed whenever a module adds a new tool class or when cited standards change. Current version: **v0.1 (2026-10-09)**. Later versions supersede earlier ones; learners mid-course must re-acknowledge if §2 or §6 changes materially.
