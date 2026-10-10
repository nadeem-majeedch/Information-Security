---
title: "Module 04 Quiz — Networking Fundamentals for Security"
layout: default
---

# Module 04 Quiz — Networking Fundamentals for Security

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 packet-reading short answer) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. For the packet-reading questions, reason from what a capture *would* show — you do not need to run a tool to answer, but LAB-07 lets you verify on your own isolated lab.

**Coverage.** Maps to Module 04 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m04--networking-fundamentals-for-security)).

**Related:** [Module 04 lesson](../../modules/module-04-networking-fundamentals-for-security/README.md) · [LAB-07](../../labs/lab-07-packet-analysis/README.md) · [CS-1 case study](../case-studies/cs-1-breach-at-meridian.md)

> **Safety reminder:** every capture in this course is taken on systems you own or an isolated lab network. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** In which layer of the TCP/IP model do **routers** primarily forward packets?

- (a) Application
- (b) Transport
- (c) Internet
- (d) Link

**Q2.** The TCP three-way handshake exchanges flags in which order?

- (a) SYN → SYN-ACK → ACK
- (b) ACK → SYN → SYN-ACK
- (c) SYN → ACK → FIN
- (d) FIN → ACK → SYN

**Q3.** What does **DNS** primarily do?

- (a) Assigns IP addresses to devices automatically
- (b) Translates human-readable names to IP addresses
- (c) Encrypts web traffic
- (d) Filters malicious websites by default

**Q4.** Which protocol is connectionless and does **not** perform a handshake?

- (a) TCP
- (b) UDP
- (c) TLS
- (d) SSH

**Q5.** What is the primary purpose of **NAT**?

- (a) Encrypt traffic
- (b) Map many private internal addresses to one (or a few) public address(es)
- (c) Assign static IPs
- (d) Detect intruders

**Q6.** Which port is **HTTPS** traditionally associated with?

- (a) 80
- (b) 443
- (c) 22
- (d) 53

**Q7.** In a Wireshark capture, what does the filter `tcp.flags.syn==1 and tcp.flags.ack==0` isolate?

- (a) The final ACK of a handshake
- (b) The initial SYN (connection request)
- (c) Only encrypted application data
- (d) DNS queries

**Q8.** Which statement about **ARP** is correct?

- (a) It resolves IP addresses to MAC addresses on a local link
- (b) It encrypts LAN traffic
- (c) It is a routing protocol used across the internet
- (d) It assigns IP addresses dynamically

## Part B — Packet-reading short answer (4)

**Q9.** You capture a TCP connection. Describe the three packets of the handshake and the flag combination you would look for in each, using Wireshark filter syntax.

**Q10.** In a capture you see a DNS query for `example.test` followed by a response containing an A record. Explain, in order, what happens between typing a URL and the TCP handshake beginning.

**Q11.** A capture shows a TLS connection where, after the handshake, you can only see "Application Data." Explain what an eavesdropper on that link can still learn, and what they cannot.

**Q12.** Explain why ARP appears in a capture taken *inside* your lab LAN but would not appear if you captured on a link beyond your local segment — and what that implies about the scope of ARP-spoofing attacks.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (c) Internet layer.** Routers forward IP packets hop-by-hop at the Internet (network) layer. *Misconception:* (d) link-layer devices move frames on the *local* segment only — routers work above it; (b) transport is end-to-end between hosts (TCP/UDP), not hop-by-hop forwarding.

**Q2 — (a) SYN → SYN-ACK → ACK.** Client SYN, server SYN-ACK, client ACK — any other order is not the TCP handshake. *Misconception:* (b) reverses the parties (the server does not speak first); (c)/(d) mix in FIN, which belongs to connection *teardown*, not establishment.

**Q3 — (b).** DNS translates human-readable names to IP addresses. *Misconception:* (a) is **DHCP's** job — the names-vs-numbers distinction is the tell; (c) TLS encrypts traffic rather than resolving names; (d) filtering is a separate service that may *use* DNS but is not its function.

**Q4 — (b) UDP.** Connectionless, no handshake. *Misconception:* (a) TCP is the opposite of the stem — its handshake is its defining feature; (c) TLS and (d) SSH typically run *over* a TCP connection; SSH negotiates its own transport handshake, but it is not the textbook connectionless protocol.

**Q5 — (b).** NAT maps many private internal addresses onto one (or a few) public addresses — conserving addresses; hiding internal topology is a *side effect*, not its purpose. *Misconception:* (a) is encryption's job; (c) describes address assignment (DHCP/static); (d) intrusion detection is unrelated — NAT is a translation mechanism, not really a security control.

**Q6 — (b) 443.** *Misconception:* 80 is plain HTTP — the protocol HTTPS *replaces*, which is the common confusion; 22 is SSH; 53 is DNS. Learn 80→443 as a pair, then 22 and 53 alongside them.

**Q7 — (b) The initial SYN.** SYN=1, ACK=0 marks a connection request; SYN with ACK=1 is the SYN-ACK; a lone ACK has SYN=0. *Misconception:* (a) the final ACK has ACK=1 and is excluded by the filter's `ack==0`; (c)/(d) concern other protocols entirely — the filter decodes TCP flags only.

**Q8 — (a).** ARP resolves a known IP to a MAC address *on the local link*. *Misconception:* (b) ARP traffic is plaintext — it performs no encryption; (c) ARP is link-local and never routes across the internet; (d) address *assignment* is DHCP's role — ARP only asks who already owns a known address.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** (1) **SYN** — `tcp.flags.syn==1 and tcp.flags.ack==0` (client → server request). (2) **SYN-ACK** — `tcp.flags.syn==1 and tcp.flags.ack==1` (server acknowledges and requests). (3) **ACK** — `tcp.flags.syn==0 and tcp.flags.ack==1` (client confirms). The connection is now established; record the client's ephemeral port and the server's fixed port. → [LAB-07 Task on handshake](../../labs/lab-07-packet-analysis/README.md)

**Q10.** (1) The resolver sends a **DNS query** (usually UDP/53) for the name. (2) The DNS server replies with an **A record** mapping the name to an IP. (3) The client uses that IP as the destination and begins the **TCP handshake** to port 443 (for HTTPS). DNS resolution *precedes* the transport handshake; if DNS is plaintext, the *name* is visible even though the later HTTPS content is encrypted.

**Q11.** After the handshake the payload is encrypted, so the eavesdropper **cannot** read the plaintext content, but they **can** still see metadata: the destination IP/hostname (from SNI or DNS), port, packet sizes, timing, and volume — enough to infer *what service* and *how much* data moved. Encryption hides content, not traffic analysis. → [Lesson: TLS and metadata](../../modules/module-04-networking-fundamentals-for-security/README.md)

**Q12.** ARP maps IP→MAC **only on the local link**; it is not routed beyond the local segment, so it never appears in a capture taken further away. Implication: **ARP spoofing/poisoning is a local-link attack** — it can target hosts on your own LAN (or VLAN) but cannot be mounted from across the internet. This is a direct argument for network segmentation (M08): confining a LAN limits who can even reach the ARP domain.

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Capture & annotate (hands-on, isolated lab only).** In LAB-07, record traffic while browsing a local server, then filter and annotate: ARP, a DNS query/response, the full TCP handshake, plain HTTP, and a TLS ClientHello. Export the `.pcapng` and re-verify your filters reproduce.
2. **Handshake reconstruction.** Draw the sequence diagram of a full TCP handshake plus TLS negotiation for one connection, labelling each step and the flags/messages exchanged.
3. **Isolated subnet proof.** Build a host-only network with two VMs, assign static IPs, verify connectivity between them, and produce evidence that the VMs are isolated from your real LAN.
4. **Protocol upgrade comparison.** Serve the same local service once over plain HTTP and once over TLS; capture both and document exactly what an eavesdropper learns in each case.

*Review guidance:* 1 and 4 are the "what does the wire reveal" spine of M04 — every later module (M08 secure protocols, M11 threat modeling) reuses this reasoning. If your isolated-subnet proof cannot show a *blocked* path to your real LAN, you have not demonstrated isolation.

**Next:** [Module 05 quiz](./quiz-m05.md) · [Previous: M03](./quiz-m03.md) · [Assessment Hub](../README.md)
