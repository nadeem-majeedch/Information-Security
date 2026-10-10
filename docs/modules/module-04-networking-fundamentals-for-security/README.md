---
title: "Module 04 — Networking Fundamentals for Security"
layout: default
---

# Module 04 — Networking Fundamentals for Security

> **Level 1 · Foundations · Beginner · Estimated study time: 12–14 hours**
> **Prerequisites:** [Module 01](../module-01-information-security-foundations/README.md). Basic comfort installing software.

**⚠ First hands-on module.** Before any capture or scanning activity, complete the isolation checklist in the [Lab Safety Policy](../../lab-safety-policy.md) (§4.3). Everything active in this module targets **your own isolated lab network only**.

## Why This Module Matters

Firewalls, intrusion detection, VPNs, "the attack came over DNS" — none of it makes sense until you can read what computers actually put on the wire. Networking is the language of this entire discipline: Level 2's network defense (M08), web security (M09), detection engineering (M13), and forensics (M14) all assume you can look at a capture and say *"that's a DNS query, that's the TCP handshake, that's TLS starting."* This module builds that literacy from zero, using only free tools and a lab you own. Students who shortcut it later spend hours debugging firewalls they don't understand.

## Prerequisites and Estimated Study Time

- **Prerequisites:** [Module 01](../module-01-information-security-foundations/README.md). No prior networking needed — this module starts at zero.
- **Estimated study time:** 12–14 hours — ~4 h reading, ~6 h labs (captures + isolation proof), ~2 h knowledge check.
- **Tools:** Wireshark (free), VirtualBox or VMware Workstation Player (free), an Ubuntu/Debian ISO (free). No cost; setup steps in the lab.

## Learning Outcomes

By the end of this module, you can:

1. Map data across the TCP/IP model layers and identify where common security controls sit (TLS, firewall, VPN, DNS security). *(Understand)*
2. Read a packet capture and identify ARP, DNS, TCP handshake, HTTP, and TLS ClientHello without assistance. *(Apply)*
3. Explain IP addressing, subnetting (prefix /24 and smaller), NAT, ports, and common services (DNS, DHCP, HTTP/S, SSH). *(Understand)*
4. Capture and analyze traffic **only on your own isolated lab network** using Wireshark filters. *(Apply)*

---

## Core Concepts

### 1. Why layers? The TCP/IP model and the OSI model

**Plain language.** Sending a web page across the world is like mailing a book: you write content, the publisher binds it, the post office boxes it, a truck moves the box. Each stage only cares about its own job. Network protocols work the same way — **layers**, each wrapping the layer above.

**Technical detail.** Two models describe this. **TCP/IP** is what the internet actually uses (4 layers); the **OSI** model (7 layers) is the teaching/reference language — practitioners still say "Layer 2" or "Layer 7."

```text
  Data you send
  ──────────────────────────────────────────────────────
  OSI 7  Application     │  TCP/IP      Application     │  HTTP, DNS, SSH, SMTP
  OSI 6  Presentation    │             (same layer)     │  TLS (encryption lives here)
  OSI 5  Session         │                             │  session setup
  ──────────────────────────────────────────────────────
  OSI 4  Transport       │             Transport       │  TCP (reliable), UDP (fast)
  ──────────────────────────────────────────────────────
  OSI 3  Network         │             Internet        │  IP addresses, routing, ICMP
  ──────────────────────────────────────────────────────
  OSI 2  Data Link       │             (Network Access)│  Ethernet, MAC addresses, ARP
  OSI 1  Physical        │                             │  cables, radio, signals
  ──────────────────────────────────────────────────────
```

**Encapsulation:** as data travels down, each layer adds its own header (like nested envelopes):

```text
 [ HTTP request ]                      ← what the app wants
 [ TCP header | HTTP request ]         ← ports + reliability (segment)
 [ IP  header | TCP header | … ]       ← source/dest addresses (packet)
 [ Eth hdr | IP hdr | … | Eth trailer ]← MAC addresses + error check (frame)
```

**Where security controls sit** — memorize this table; it reappears in every later module:

| Control | Layer(s) | What it can see/do |
|---|---|---|
| Cable lock / Faraday bag | 1 (physical) | Stop signals entirely |
| MAC filtering, VLANs | 2 (data link) | Segment by device identity |
| **Firewall** (packet/stateful) | 3–4 | Permit/deny by IP, port, connection state |
| **VPN** (IPsec/WireGuard) | 3 (IPsec) or 4–6 (SSL-VPN) | Tunnel traffic between sites/devices |
| **TLS** | 6–7 (wraps app data) | Encrypt + authenticate server to client |
| **IDS/IPS** (Suricata) | 4–7 (reads patterns) | Alert/block on signatures in traffic |
| **DNS security** (DoH/DoT) | 7 | Encrypt/protect the naming system itself |

### 2. Addresses: MAC, IP, ports, and NAT

**Plain language.** A device has a permanent-ish ID stamped by the manufacturer (**MAC address**, e.g. `a4:5e:60:c1:2f:19`), a network location assigned when it joins (**IP address**, e.g. `192.168.1.24`), and services on it are numbered (**ports**). Routers move packets toward the right network; switches deliver frames to the right device.

**Technical detail.**

- **IPv4 addresses** are 32-bit numbers written as four 0–255 octets. The **prefix/ CIDR notation** tells you how many bits identify the *network*: `192.168.1.0/24` = first 24 bits are the network → addresses `192.168.1.0`–`192.168.1.255` (256 addresses, ~254 usable hosts). Smaller prefixes = bigger networks: `/25` → 126 hosts, `/26` → 62, `/27` → 30, `/28` → 14, `/29` → 6, `/30` → 2 hosts (classic point-to-point link). **Home routers default to /24.** Private ranges (not routed on the internet): `10.0.0.0/8`, `172.16.0.0/12`, `192.168.0.0/16`.
- **Ports** (0–65535) identify the service. Ports 0–1023 are *well-known*: 

  | Port | Service | Port | Service |
  |---|---|---|---|
  | 20/21 | FTP (legacy, plaintext) | 443 | HTTPS (HTTP over TLS) |
  | 22 | SSH (and SCP/SFTP) | 3306 | MySQL |
  | 23 | Telnet (legacy, plaintext) | 3389 | RDP (remote desktop) |
  | 25 | SMTP (mail transfer) | 53 | DNS |
  | 67/68 | DHCP (server/client) | 69 | TFTP |
  | 80 | HTTP | 8080 | HTTP-alt (proxies/apps) |
  | 110/995 | POP3(/S) | 143/993 | IMAP(/S) |

  A **socket** = (protocol, IP, port) — the full address of one conversation: `192.168.1.24:51544 → 93.184.216.34:443`.
- **NAT (Network Address Translation):** your home router has *one* public IP; devices behind it share it, with the router remembering which private IP:port maps to which public port (`192.168.1.24:51544 → 203.0.113.7:51544`). NAT hides internal addresses (incidental privacy, **not** a security control — never rely on it) and stretches the private IPv4 range.

### 3. The TCP handshake and UDP

**Plain language.** TCP is the careful courier: before sending data, two computers check they can both talk — a three-way handshake. UDP is the postcard: fire and forget, fast but no guarantees.

**Technical detail.** TCP connection setup uses flags in its header — **SYN** (synchronize), **SYN-ACK** (acknowledge), **ACK**:

```text
   Client                         Server
     │  1. SYN (seq=x)               │
     │──────────────────────────────►│
     │  2. SYN-ACK (seq=y, ack=x+1)  │
     │◄──────────────────────────────│
     │  3. ACK (ack=y+1)             │
     │──────────────────────────────►│
     │        connection established  │
     │  … data (HTTP, TLS…) …         │
     │  FIN / FIN-ACK … close         │
```

This exchange is your first capture landmark. UDP (no handshake) carries DNS queries, video, DHCP — cheap and simple, which is also why **UDP reflection DDoS** exists (attackers spoof source addresses to bounce traffic at victims). TCP vs UDP: TCP = ordered, reliable, connection-oriented; UDP = minimal, low-latency, no delivery guarantee.

### 4. DNS: the internet's phone book (and its attack surface)

**Plain language.** You type a name; DNS (**Domain Name System**) returns the number. Every step below is attacker-interesting — that's why it appears in Modules 8, 9, and 13.

**Technical detail.** Resolution chain for `example.edu`:

```text
 You ─► 1. Resolver (your ISP's or 1.1.1.1 / 8.8.8.8): "example.edu?"
        2. Root servers      → "ask the .edu servers"
        3. TLD (.edu) server → "ask these authoritative servers"
        4. Authoritative NS  → A/AAAA record: 93.184.216.34
        5. Answer cached (TTL) ─► browser connects to the IP
```

Records you'll meet: **A** (name→IPv4), **AAAA** (→IPv6), **CNAME** (alias), **MX** (mail), **TXT** (verification, SPF), **PTR** (reverse). **DNSSEC** signs answers against forgery; **DoH/DoT** encrypt resolver traffic (privacy vs. your org's visibility — a real trade-off). Spoofed DNS answers → phishing at the IP level; poisoned caches → everyone is redirected. Queries themselves are plaintext over UDP/53 by default — visible to anyone on path (you'll see this in the lab).

### 5. DHCP and ICMP

**DHCP** gives devices their IP automatically — the **DORA** sequence: **D**iscover (client shouts) → **O**ffer (server offers address) → **R**equest (client accepts) → **A**ck (server confirms), plus gateway and DNS details. Rogue DHCP servers (a fake one on your network) can hand out attacker-controlled gateway/DNS — a real "evil twin" technique you'll defend against in M08.

**ICMP** is the diagnostic protocol behind **ping** (echo request/reply) and "destination unreachable" messages. Ping proves *reachability*, not service health — a host can ping and still block every port. Firewalls commonly rate-limit or drop ICMP; "ping fails" ≠ "host down."

### 6. HTTP, TLS, and what "secure" actually means

**HTTP** is the request/response language of the web: a request line (`GET /index.html HTTP/1.1`, headers, optional body) and a response (status code + headers + body). Status codes you'll read in captures and tools: **200** OK, **301/302** redirect, **403** forbidden (exists, refused), **404** not found, **500** server error. HTTP alone is plaintext — anyone on path sees URLs, headers, cookies.

**TLS (Transport Layer Security)** wraps the conversation: it **authenticates** the server (and optionally the client) via **certificates** signed by trusted **Certificate Authorities (CAs)** in your device's trust store, and **encrypts** everything after the handshake. Current version: **TLS 1.3** (RFC 8446, 2018) — fewer round-trips, modern cipher suites only. TLS 1.0/1.1 are formally **deprecated — MUST NOT be used** (RFC 8996, 2021), and SSLv3 is likewise prohibited (RFC 7568). In a capture you'll see the order: TCP handshake → **TLS ClientHello** (supported versions/ciphers, SNI hostname in plaintext unless ECH is used) → ServerHello + certificate → encrypted application data. *HTTPS = HTTP inside TLS* — the lock icon means the *channel* is protected and the *server's certificate matched the name* — not that the site itself is honest.

### 7. Wireless in two paragraphs

Wi-Fi associations open with an unencrypted handshake to find and join networks — which enables the **evil twin** attack: a strong fake access point with your café's name, onto which victims connect and hand over credentials. **WPA2** (2004-era, still common) was superseded by **WPA3** (2018), which removes weak password-based handshakes (downgrade attacks become far harder) — enable WPA3 where all your devices support it, WPA2-AES minimum otherwise, and never WEP or open networks for anything personal. Wireless security details continue in M08.

---

## Worked Example: One Page Load, End to End

**Scenario.** You type `https://courses.example.edu/notes` and press Enter. Trace every layer — this is outcome 1 in action:

| Step | Layer | What happens | Visible in a capture as… |
|---|---|---|---|
| 1 | App/DNS | Resolver chain (§4) returns the IP, cached or fresh | `dns` packets: query + response, A record |
| 2 | L2/L3 | Your MAC resolves the gateway's MAC; packet routed toward the IP | `arp` who-has gateway; IP header `you → 93.184.x.x` |
| 3 | L4 | TCP three-way handshake on port 443 | `tcp` flags SYN → SYN-ACK → ACK |
| 4 | L6/L7 | TLS ClientHello (versions, cipher suites, server name) | `tls` record type 1; server name in SNI field |
| 5 | L6/L7 | ServerHello + certificate chain; keys agreed | certificate visible pre-encryption; handshake complete |
| 6 | L7 | Encrypted HTTP: `GET /notes` inside TLS | `Application Data` records — contents unreadable without keys |
| 7 | L7 | Response streams back (200 OK, HTML) | more Application Data, then TCP FIN teardown |

**Read the security story in it:** DNS answered in plaintext (step 1 — why DoH exists); your real IP and the server's are visible (step 2 — VPN territory); ports visible (step 3 — firewall territory); hostname visible in ClientHello (step 4 — SNI privacy limitation); *everything after step 5 is confidential and tamper-evident* (TLS — M06/M08). **Apply it:** open any site, then predict — which steps would disappear if the site were plain `http://`? (Steps 4–5 entirely; step 6 becomes readable `GET /notes`.) **Check yourself:** you've understood this section if you can explain *why* an attacker on café Wi-Fi can still see *which* sites you visit even with TLS everywhere (DNS query + SNI + destination IP are unencrypted by default).

---

## Step-by-Step Procedures

### Procedure A — Capture and annotate traffic (Wireshark)

*Target: your own machine/lab only, on an isolated network (Procedure B first).* 

1. Install Wireshark (free: <https://www.wireshark.org/download.html>). On Linux: `sudo apt install wireshark` and add your user to the `wireshark` group (log out/in for it to apply).
2. Start Wireshark, pick the **correct interface** — the one carrying traffic (the lab host-only adapter for lab work; look for the one with the moving packet-count bar). Wrong interface = empty capture; this is the #1 beginner issue.
3. Start capture; in a browser visit any `https://` page you own or a public site; wait for it to finish; stop capture.
4. Apply filters (type in the filter bar; syntax is Wireshark's display-filter language):
   - `dns` — name lookups (query and response pairs)
   - `tcp` and `tcp.flags.syn==1 and tcp.flags.ack==0` — isolate SYN starts (handshake step 1)
   - `tcp.flags.syn==1 and tcp.flags.ack==1` — SYN-ACKs (step 2)
   - `tls` — handshake and application data; find `Client Hello`
   - `http` — plaintext HTTP only (HTTPS sites produce nothing here — expected!)
   - `arp` — local-network address resolution
5. **Follow the stream:** right-click a packet → *Follow* → *TCP Stream* (or *TLS* where available) to see a conversation assembled in order.
6. Annotate five screenshots into your notebook: DNS query/response; the three handshake packets; the ClientHello; one `Application Data` exchange; teardown (FIN). For each: record interface, filter used, and one sentence explaining what it shows.
7. Save the capture file (`*.pcapng`) alongside your notes — evidence must be re-openable.

### Procedure B — Prove your lab is isolated (mandatory before any scanning)

*From the [Lab Safety Policy](../../lab-safety-policy.md) §4.3 — run and screenshot before every offensive lab:* 

1. Set the VM network to **Host-only** (VirtualBox: Settings → Network → Adapter 1 → Host-only Adapter; VMware: VM Settings → Network → Host-only). Not Bridged. Not NAT for test traffic.
2. Inside the lab VM, get addresses: `ip addr` (Linux) / `ipconfig` (Windows).
3. **Positive test:** ping your lab peer or host-only gateway — must **succeed**.
4. **Negative test 1:** ping a public IP (e.g. `ping 1.1.1.1`) — must **fail** (timeout/unreachable).
5. **Negative test 2:** ping a real LAN device's private IP — must **fail**.
6. Screenshot all three results in one image; label it `isolation-proof.png` into your portfolio.
7. Only now run any Nmap/scan exercise — against **host-only addresses you listed**, never others (Safety Policy §3).

---

## Common Mistakes, Misconceptions, and Troubleshooting

| Mistake / misconception | Why it is wrong | Correction |
|---|---|---|
| Capturing on the wrong interface (VPN adapter, idle NIC) | Wireshark shows nothing or the wrong traffic | Watch which interface's counter is moving *while you browse* |
| "Ping works, so the service works" | ICMP reachability ≠ port listening/service healthy | Test the actual port (`curl`, `nc -zv`, service logs) |
| Thinking HTTPS hides *everything* | DNS query, IPs, timing, and SNI hostname are visible pre-encryption | Name the leaks precisely (worked example step 4) |
| Confusing bits and bytes (or Mbps vs MB/s) | 100 Mbps ≠ 100 MB/s (÷8 → ~12.5 MB/s) | Divide by 8; check units in captures (Wireshark shows bytes) |
| Using `http` filter on an HTTPS site and concluding "nothing happened" | HTTP is *inside* TLS — invisible | Filter `tls` instead |
| Subnetting by memorizing tables | Binary rules don't memorize well under pressure | Derive: each extra prefix bit halves hosts (`/24`→254, `/25`→126, `/26`→62…) |
| Assuming 192.168.x.x "can't be attacked" | Private ranges only skip *internet routing*; attackers land inside via Wi-Fi/VPN/phishing | Isolation + authentication, not address obscurity |
| Testing from a bridged VM "just for the demo" | Puts your lab on the real LAN | Re-run Procedure B; bridge only for downloads, never for tests |
| Trusting Wi-Fi by SSID name | SSIDs are attacker-controlled strings (evil twin) | Verify by login page/TLS behavior; prefer WPA3/personal networks |

**Troubleshooting:** *Empty capture* → wrong interface or filter too narrow (clear the filter; if bars still don't move, you're offline). *No `http` packets on a modern site* → expected; use `tls`. *DNS filter shows your resolver only* → your OS used DoH (encrypted DNS); disable it temporarily in browser settings for the exercise, or capture the lab VM's plain DNS instead. *Ping to public IP succeeds in VM* → you are **not** isolated: stop, switch to host-only, re-run Procedure B before continuing (this is a safety stop, not a debugging nicety).

---

## Lab 4 — Packet Capture Notebook and Isolation Proof

*First active lab — restricted to your own isolated network. Overview: [Lab Collection](../../labs/README.md); rules: [Lab Safety Policy](../../lab-safety-policy.md).*

**Dedicated lab worksheet:** [LAB-07 — Packet Analysis of Authorized Local Traffic](../../labs/lab-07-packet-analysis/README.md) · [Full lab collection](../../labs/README.md).

**Objective:** annotated capture notebook + mandatory isolation proof.

**Steps:**

1. Create `portfolio/M04/`.
2. Build two lab VMs (host-only): host (your machine) + one Ubuntu VM — or reuse a single VM plus the host-only gateway.
3. Run **Procedure B** → `isolation-proof.png` (three tests in one image).
4. Run **Procedure A** inside the lab path: capture DNS, TCP handshake, TLS ClientHello, application data, teardown — five annotated screenshots + filters + one-line explanations in `capture-notebook.md`.
5. **Protocol hunt (write answers):** (a) From your capture, which IP:port pairs did your browser use? (b) Locate the SYN/SYN-ACK/ACK triple with frame numbers. (c) Which DNS record types appeared? (d) Find one ARP exchange. (e) Show that the HTTP request line is *not* visible for an HTTPS site (which filter proves it?).
6. **Bonus:** capture the same page over `http://` (any site that still serves plain HTTP for testing) and contrast: what's now readable that wasn't?
7. Safety statement: targets used = *own host + own lab VM on host-only network*; isolation = *Procedure B image attached*.

**Completion check:** isolation proof with all 3 tests; 5 annotated captures; protocol-hunt answers (a)–(e) each supported by a frame reference.

---

## Knowledge Check

*Formative — self-graded; retake until ≥ 80% (10 of 12).*

**Extend your practice:** [Module 04 quiz — more questions, worked answers, and outcome mapping](../../assessments/level-1/quiz-m04.md) · module-end review exercises are on the same page · [Assessment Hub](../../assessments/README.md)

**Multiple choice (8):**

1. Which layer pairing is correct?
   - (a) TCP handshake — Layer 3  (b) TLS — application/session layer wrapping HTTP  (c) ARP — Layer 4  (d) Firewall rules — Layer 1
2. `192.168.1.0/24` provides roughly how many usable host addresses?
   - (a) 2  (b) 30  (c) 254  (d) 65,534
3. In the TCP three-way handshake, the second packet is:
   - (a) SYN  (b) ACK  (c) SYN-ACK  (d) FIN
4. Why can an on-path observer still see *which* site you visit when using HTTPS?
   - (a) TLS is broken  (b) DNS queries and the destination IP/SNI hostname are not encrypted by default  (c) HTTPS only encrypts bodies, not headers  (d) They cannot — HTTPS hides everything
5. NAT's security value is:
   - (a) A real security boundary you should rely on  (b) Incidental address hiding only — not a control  (c) Encryption of internal traffic  (d) Malware filtering
6. Which is a **UDP** service?
   - (a) SSH  (b) HTTPS  (c) DNS (default)  (d) RDP
7. In DNS resolution, who ultimately holds the authoritative answer for `example.edu`?
   - (a) The root servers  (b) The .edu TLD servers  (c) The domain's authoritative name servers  (d) Your browser cache
8. Which statement about TLS versions is correct in 2026?
   - (a) SSLv3 is recommended for compatibility  (b) TLS 1.0/1.1 are deprecated by RFC 8996  (c) TLS 1.2 is the maximum possible version  (d) TLS provides anonymity by hiding the destination IP

**Short answer / packet-reading (4):**

9. List the exact steps of a TCP connection to port 443, naming each packet's flags, and state which layer adds ports.
10. Your capture shows `who-has 192.168.1.1 tell 192.168.1.24`. Explain what is happening, which protocol it is, and which layer it operates at.
11. Explain DORA in one sentence and describe one attack a rogue DHCP server enables.
12. A classmate says "our firewall can read every message, so we don't need TLS." Using the layer table, give two rebuttals.

<details>
<summary><b>Answer key</b> — attempt the questions first</summary>

1. **(b)** — TLS sits at the session/presentation region wrapping application data; TCP handshake is L4; ARP is L2; firewalls span L3–4.
2. **(c)** — 256 addresses minus network and broadcast = 254.
3. **(c)** — SYN → SYN-ACK → ACK (client's SYN, server's SYN+ACK, client's ACK).
4. **(b)** — plaintext DNS (unless DoH/DoT), destination IP, timing, and SNI hostname in ClientHello leak metadata; body stays encrypted.
5. **(b)** — NAT hides internal addressing as a side effect; it authenticates nothing and encrypts nothing.
6. **(c)** — DNS defaults to UDP/53 (large answers use TCP; DNS over TLS/HTTPS use other paths). SSH/TLS-over-TCP; RDP typically TCP.
7. **(c)** — roots delegate → TLD delegates → the domain's authoritative NS answers; resolvers cache along the way.
8. **(b)** — RFC 8996 (2021) deprecates TLS 1.0/1.1; SSLv3 prohibited (RFC 7568); TLS 1.3 exists; TLS hides content, not destination metadata.
9. Client → SYN (L4 adds ports… ports are actually added at L4 by TCP itself, headers at each layer as data descends) ; Server → SYN-ACK; Client → ACK. Ports are added by TCP at the transport layer; IP addresses are added at L3. *(Full credit: SYN, SYN-ACK, ACK; transport layer.)*
10. ARP (Address Resolution Protocol, Layer 2): host 192.168.1.24 is asking "who owns 192.168.1.1?" so it can build Ethernet frames to the gateway — IP-to-MAC mapping on the local segment.
11. DORA = DHCP Discover → Offer → Request → Ack, the four-message lease negotiation. A rogue DHCP server can hand victims an attacker-controlled gateway/DNS, silently redirecting all their traffic (phishing/man-in-the-middle on a grand scale).
12. (1) A firewall sees plaintext only *before* TLS — if traffic is end-to-end TLS, the firewall either terminates TLS (becoming a trusted, high-value proxy needing its own controls) or sees ciphertext; (2) TLS also protects *beyond* the firewall — after traffic leaves its perimeter — and authenticates the server, preventing on-path impersonation that a perimeter device can't stop outside its walls.

</details>

## Scenario Exercises (Practice)

1. **Filter writing.** For each intent, write the Wireshark display filter: (a) only DNS traffic; (b) packets with the SYN flag set; (c) TLS records; (d) traffic to/from a single lab IP `192.168.56.10`.
2. **Leak analysis.** Your friend uses only HTTPS everywhere and claims nobody can see anything. List four pieces of metadata still visible to an on-path observer and, for each, one technique from this course that reduces the leak.
3. **Design the subnet.** A small lab needs: a student network (60 devices), a target range (10 devices), and a management segment (4 devices), all inside `10.10.0.0/24`. Propose prefixes for each segment and calculate host counts. (Hint: split from the top: /26 → 62 hosts.)

## Key Takeaways

1. **Layered models** (TCP/IP 4-layer in practice, OSI 7-layer in conversation) explain how data travels and **where each security control sits** — firewall L3–4, TLS above, IDS across, DNS security at the resolver.
2. **Addresses have three identities:** MAC (L2), IP (L3, with CIDR prefixes defining network size), port (L4 service number). **NAT** is convenience, not security.
3. **TCP's three-way handshake (SYN → SYN-ACK → ACK)** is the first landmark in any capture; UDP trades reliability for speed and powers DNS/DHCP/DDoS reflection.
4. **DNS** resolves names through root → TLD → authoritative servers; its plaintext nature (queries + cache poisoning risk) motivates DNSSEC and DoH/DoT.
5. **DHCP (DORA)** automates configuration — and a rogue server is a full traffic-hijack tool.
6. **TLS 1.3 is current; TLS 1.0/1.1 and SSLv3 are prohibited** (RFC 8996/7568). HTTPS protects content and server identity — **not** destination metadata (DNS, IP, SNI).
7. **Capture skills are safety-bound:** correct interface, correct filter, and **isolation proof first — never scan anything but your own lab ranges.**

## Self-Assessment Checklist

- [ ] I can draw the TCP/IP and OSI layers and map five security controls to their layers.
- [ ] I can explain encapsulation (frame/packet/segment nesting) in my own words.
- [ ] I can compute hosts in /24 … /30 prefixes without a cheat sheet (or derive quickly).
- [ ] I can name 8+ well-known ports and what plaintext vs TLS versions exist for each service.
- [ ] I can sketch the TCP handshake with flags and the DNS resolution chain.
- [ ] I explained DORA and one rogue-DHCP attack.
- [ ] I captured and annotated: DNS, handshake, ClientHello, application data, teardown — with filters.
- [ ] I produced `isolation-proof.png` (3 tests) and re-run it before any scanning lab.
- [ ] I scored ≥ 80% on the knowledge check.

*If the isolation proof is missing, **stop** — no further active lab anywhere in this course until it exists.*

## Further Reading

Verified as of 2026-10-09.

- **RFC 1122** — Requirements for Internet Hosts (layer model): <https://www.rfc-editor.org/rfc/rfc1122>.
- **RFC 9293** — Transmission Control Protocol (the current TCP spec, 2022): <https://www.rfc-editor.org/rfc/rfc9293>.
- **RFC 8446** — TLS 1.3 (2018): <https://www.rfc-editor.org/rfc/rfc8446>; **RFC 8996** — Deprecating TLS 1.0/1.1 (2021): <https://www.rfc-editor.org/rfc/rfc8996>.
- **RFC 1035** — DNS (names, records, messages): <https://www.rfc-editor.org/rfc/rfc1035>; **RFC 2131** — DHCP: <https://www.rfc-editor.org/rfc/rfc2131>.
- **RFC 9110** — HTTP Semantics (2022): <https://www.rfc-editor.org/rfc/rfc9110>.
- **Wireshark Documentation / Display Filter Reference** — <https://wiki.wireshark.org>.
- **NIST SP 800-41 Rev. 1, *Guidelines on Firewalls and Firewall Policy*** (2009): <https://csrc.nist.gov/pubs/sp/800/41/r1/final>.
- **Cloudflare Learning Center** — accessible explainers for DNS/TLS/HTTP: <https://www.cloudflare.com/learning/>.
- **Wi-Fi Alliance, WPA3** — <https://www.wi-fi.org/discover-wi-fi/security>.

---

**Navigation:** [← Previous: Module 03](../module-03-governance-policy-ethics-and-law/README.md) · [Module index](../README.md) · [Next: Module 05 →](../module-05-operating-system-and-endpoint-security/README.md) · [Lab collection](../../labs/README.md) · [Reference Library](../../reference/README.md)
