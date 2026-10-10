---
title: "Module 08 Quiz — Network Security: Perimeter, Segmentation, and Secure Protocols"
layout: default
---

# Module 08 Quiz — Network Security: Perimeter, Segmentation, and Secure Protocols

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 rule-review scenarios) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. In rule-review scenarios, state the verdict (allow/block/modify), the reason, and — where a rule is wrong — the corrected rule.

**Coverage.** Maps to Module 08 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m08--network-security-perimeter-segmentation-and-secure-protocols)): segmentation design, firewall rules, IDS alert reading, secure protocol evaluation.

**Related:** [Module 08 lesson](../../modules/module-08-network-security/README.md) · [LAB-08 firewall config audit](../../labs/lab-08-firewall-config-audit/README.md) · [LAB-07 packet analysis](../../labs/lab-07-packet-analysis/README.md) · [CS-2 case study](../case-studies/cs-2-product-launch-crypto-identity.md)

> **Safety reminder:** all scanning, IDS triggering, and rule testing happens against **lab IPs only**, inside an isolated network. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** The primary security benefit of network segmentation is:

- (a) Faster network throughput
- (b) Containing lateral movement: a compromised workstation cannot freely reach unrelated sensitive zones
- (c) Eliminating the need for endpoint protection
- (d) Hiding the network from all scanning

**Q2.** A stateful packet-filtering firewall differs from a simple ACL in that it:

- (a) Inspects packet payloads for malware
- (b) Tracks connection state, allowing return traffic for established flows without a static inbound rule
- (c) Terminates TLS connections
- (d) Applies per-user permissions

**Q3.** An IDS alert fires on "TCP port scan — 20 ports in 2 seconds from 192.168.1.50." Your lab topology says .50 is your own scanner host running an authorized Nmap sweep. The correct classification is:

- (a) True positive, severity critical — isolate the host immediately
- (b) Expected activity in an authorized window: true positive detection, contextually benign (log and close, note in RoE window)
- (c) False positive — the IDS is broken and rules should be disabled
- (d) Cannot be determined without a packet capture

**Q4.** Replacing Telnet with SSH primarily gains:

- (a) Encryption of the session plus server authentication, so credentials and commands aren't readable/modifiable on the wire
- (b) Faster file transfer
- (c) Intrusion detection
- (d) Web browsing support

**Q5.** Which protocol replacement pairing is correct?

- (a) HTTP → FTP for confidentiality
- (b) DNS (plain) → DoH/DoT to encrypt DNS queries between stub and resolver
- (c) WPA2 → WPA3 to remove the need for a passphrase
- (d) SSH → Telnet to reduce attack surface

**Q6.** A VPN (WireGuard/IPsec) primarily provides:

- (a) An encrypted tunnel with endpoint authentication between tunnel peers — traffic beyond the endpoints is still visible to them
- (b) Full anonymity on the internet
- (c) Malware scanning of tunnelled traffic
- (d) Automatic patching of the tunnel hosts

**Q7.** "Deny by default; allow only what the business requires" describes:

- (a) An allowlist/deny-by-default rule base
- (b) A black-list firewall that must enumerate every attack
- (c) An IDS in promiscuous mode
- (d) NAT traversal

**Q8.** In firewall rule ordering on most engines, rules are evaluated top-down and the first match wins. Therefore the safest ordering principle is:

- (a) Broad allow rules first, specific denies later
- (b) Specific denies first, then narrowly scoped allows, implicit deny at the end
- (c) Random order — order does not matter
- (d) Logging rules only, with no permits

## Part B — Rule-review scenarios (4)

**Q9. (Outcome 2 — configuration analysis)** A rule base for a three-zone lab (management, workstations, target lab) contains: `1) allow mgmt → * any port; 2) allow workstation → target-lab any; 3) allow * → * any; 4) deny * → * any`. Identify every problem, give the impact of each, and write a corrected minimal rule set.

**Q10. (Outcome 1 — segmentation design)** Justify rules for a small office: web server (public), office workstations, and an accounting VLAN that must reach the internet only for updates. What traffic flows do you permit, what do you explicitly deny, and what one rule would be an unacceptable risk?

**Q11. (Outcome 3 — IDS triage).** You receive three Suricata alerts: (a) `ET SCAN Nmap -sS window scan`, (b) `ET EXPLOIT Apache Log4j jndi payload`, (c) `ET POLICY Cisco Webex login`. The scan source is your scanner (authorized window); (b) originates from an office workstation to your web server; (c) is from a colleague's desk phone. Give verdict (TP/FP), severity, and next action for each.

**Q12. (Outcome 4 — protocol evaluation)** For each pair, say what an eavesdropper on the wire learns and whether it should be replaced: (a) HTTP vs HTTPS; (b) FTP vs SFTP; (c) SNMPv1 vs SNMPv3 with authPriv; (d) Wi-Fi WPA2-Personal vs WPA3-Personal in a café scenario.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Segmentation shrinks blast radius and blocks lateral movement — the core of zero-trust networking. Misconceptions: (a) may be true incidentally, not the security purpose; (c) segmentation is *complementary* to endpoint protection, never a replacement; (d) scanning still works where allowed — segmentation controls reachability, not visibility.

**Q2 — (b).** It tracks state tables (e.g., outbound SYN → permitted return packets), so it doesn't need permissive "allow all inbound ephemeral" rules. Misconceptions: (a) describes DPI/NGFW; (c) describes TLS interception proxies; (d) describes identity-aware proxies, not stateful filtering.

**Q3 — (b).** The *detection* is correct (a scan really happened — true positive), but context (authorized window, known scanner, RoE) makes it an expected event: log, correlate with RoE, close. Misconception: (c) confuses "benign by authorization" with "sensor malfunction" — disabling rules destroys coverage; (a) skips triage/context entirely; (d) context here comes from the asset inventory and RoE, not a new capture.

**Q4 — (a).** SSH encrypts the session and authenticates the server (host key), so passwords/commands are neither eavesdropped nor MITM'd. Misconceptions: (b) SSH isn't about throughput; (c) neither Telnet nor SSH detects intrusions; (d) Telnet is terminal, not web.

**Q5 — (b).** DoH (DNS over HTTPS) / DoT (DNS over TLS) encrypt DNS between client and resolver, preventing on-path snooping/spoofing of queries. Misconceptions: (a) FTP sends credentials in clear — upgrade to SFTP/FTPS; (c) WPA3 still uses a passphrase (SAE improves handshake security, doesn't remove it); (d) backwards — SSH replaces Telnet.

**Q6 — (a).** VPN = encrypted tunnel + authenticated peers (keys/certs). Misconceptions: (b) the VPN provider can still see traffic — it's confidentiality from on-path networks, not anonymity; (c) unless you add TLS inspection, the VPN doesn't scan; (d) patching is unrelated.

**Q7 — (a).** Default-deny with explicit allows is the canonical firewall posture. Misconceptions: (b) deny-every-attack enumeration is impossible by construction — that's why allowlisting exists; (c) IDS observes but doesn't enforce; (d) NAT address translation, not policy.

**Q8 — (b).** Specific denies first (so exceptions aren't shadowed), then narrow allows, with an implicit/explicit deny-any at the end. Misconception: (a) a broad allow first shadows every later deny — a classic misconfiguration; (c) order absolutely matters on first-match engines; (d) rules without permits break the service.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** Problems: **Rule 1** `mgmt → * any port` over-permits — management should reach only *specific services* on specific zones (SSH/web-UI), not every port everywhere; impact: a compromised management host can reach the target lab directly at will. **Rule 2** `workstation → target-lab any` allows *any* port/protocol to the attack lab — should be limited to the intended test traffic (e.g., HTTP/HTTPS to the web target); impact: uncontrolled paths into the lab. **Rule 3** `allow * → * any` is a full any-any allow that renders rules 4 (and the whole policy) meaningless — impact: zero segmentation. **Rule 4** is correct in intent but unreachable while 3 exists. Corrected minimal set: `1) deny mgmt → target-lab any (except explicit SSH/HTTP needs); 2) allow mgmt → servers tcp 22,443; 3) allow workstation → target-lab tcp 80,443; 4) allow workstation → internet tcp 443 (update path, if required); 5) allow * → * established (state return); 6) deny * → * any; log 1,3,5,6`. → [LAB-08](../../labs/lab-08-firewall-config-audit/README.md)

**Q10.** Permit: **internet → web server tcp 80/443** (or 443 only, with 80→443 redirect); **web server → internal DB** on one port if needed (and prefer DB on a separate non-routable zone); **workstations → internet tcp 80/443** (browsing) plus DNS; **accounting VLAN → vendor update servers tcp 443 only** (FQDN/IP allow-list) — *not* general internet, *not* to office zones. Return/state traffic allowed by the stateful firewall only for these flows. Explicitly deny: internet → any internal; workstation zones → accounting VLAN; accounting → office workstations; any → any (implicit deny at end). **Unacceptable rule:** `allow * → accounting-vlan any` (or any broad any-any touching the accounting zone) — it voids segmentation and puts payment-adjacent data in reach of any compromised host.

**Q11.** (a) **TP detection / benign by context** — expected scan in the authorized window from the known scanner: severity informational under RoE, action: log, confirm against RoE window, close with note. (b) **True positive, critical** — a Log4j `jndi` exploit attempt from an internal host to your web server: immediate action: capture source host evidence, isolate/network-quarantine, check the server for callback/C2, escalate to IR (M14 process). (c) **False positive by business context** (policy trigger from an approved Webex/colleague device) — severity low: whitelist by asset inventory/device identity, keep the rule for unknown sources. Key idea: *verdict = detection quality; action = triage with context.*

**Q12.** (a) **HTTP:** eavesdropper sees full URL, cookies, form data, credentials — replace with HTTPS (TLS). (b) **FTP:** clear-text username/password and file contents — replace with SFTP (SSH) or FTPS. (c) **SNMPv1:** community strings (effectively passwords) sent in clear, no encryption — replace with SNMPv3 `authPriv` (authentication + encryption). (d) **WPA2-Personal:** four-way handshake can be captured and offline-cracked if the passphrase is weak (handshake capture risk in a café) — WPA3-Personal (SAE) resists offline dictionary attacks and forward-secrecies the session; in a café also prefer WPA3/enterprise where available, and treat any open/evil-twin SSID as hostile. → [Module 08 lesson](../../modules/module-08-network-security/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Build the segmented lab (practical).** Three zones on host-only networks, firewall rules permitting only intended flows — record *both* a blocked-flow and an allowed-flow test per zone pair. This is the M08 portfolio deliverable.
2. **IDS alert pack (log interpretation).** From 5 IDS alerts (mix of scans, policy events, one exploit), produce a triage table: verdict, ATT&CK technique, severity, next action — same format as the triage worksheet in M13.
3. **Risk prioritization.** An org runs: SSH with password auth on port 22 open to 0.0.0.0/0; HTTP admin panel on an internal VLAN; WPA2 with `password123` on the office AP. Rank by risk and give the single highest-value fix for each.
4. **Practical investigation.** Generate an authorized Nmap scan against a lab IP, read the resulting Suricata `fast.log` alerts, and write three sentences on why one alert was expected and another wasn't.

*Review guidance:* in rule reviews, "it's too open" is incomplete — always name the required flow, the rule action, and the test that proves it. Blocked-flow evidence is required, not optional.

**Next:** [M09 quiz](./quiz-m09.md) · **Previous:** [M07](./quiz-m07.md) · **Hub:** [Assessment Hub](../README.md)
