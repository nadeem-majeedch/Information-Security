---
title: "LAB-07 — Packet Analysis of Authorized Local Traffic"
layout: default
---

# LAB-07 — Packet Analysis of Authorized Local Traffic

**Lab ID:** LAB-07 · **Difficulty:** Introductory · **Estimated duration:** 2.5 hours · **Module:** M04 · **Mode:** Capture on **your own isolated lab network / own machine**

## Scenario

**Delta ISP's NOC** (fictional) trains new analysts by having them "read the wire" before touching any tool. Your trainer hands you a folder and says: *"Capture your own lab's traffic, find the five landmarks — ARP, DNS, TCP handshake, HTTP, TLS ClientHello — annotate them, and explain what an eavesdropper on this link could still learn."* Everything you capture is traffic **you generate on systems you own**, inside your isolated lab.

## Learning Objectives

1. Operate Wireshark: choose the correct interface, capture, filter (display-filter syntax), and follow streams.
2. Identify and annotate five protocol landmarks in a real capture: ARP, DNS query/response, TCP 3-way handshake, plain HTTP, TLS ClientHello.
3. Derive what metadata remains visible under HTTPS (destination IP, DNS, SNI) versus what is protected.
4. Export a capture (`.pcapng`) and reproduce findings from the saved file — evidence that survives re-grading.
5. Apply capture-scope discipline: only own/isolated systems, per the safety policy.

## Prerequisites and Required Skills

- M04 module (layer model, handshake, DNS/TLS) — do the M04 Lab first if brand new; M04 isolation proof **required**.
- Skills: installing software, running a local web server, basic filter syntax.

## Tools, Operating Systems, and Versions

| Tool | Purpose | Source |
|---|---|---|
| Wireshark (current stable, 4.x) | Capture + analysis | wireshark.org (free); Linux: `sudo apt install wireshark` (adds your user to the `wireshark` group — log out/in) |
| Python 3 (`http.server`) | Local HTTP origin you own | preinstalled |
| Browser | HTTPS test traffic | any |
| Optional larger dataset | Pre-made captures | **Wireshark Sample Captures** (documented, free): `https://wiki.wireshark.org/SampleCaptures/` — use for the challenge; local capture is the core task |

**$0.**

## Setup (Free) and Required Permissions

1. Isolation proof (M04 §4.3): host-only adapter; public ping must **fail**.
2. Install Wireshark; ensure your user can capture (group membership, re-login).
3. Authorization scope: your host's own traffic + your lab VMs. Visiting ordinary websites in a browser is normal user traffic (allowed for capture); **no scanners, no tools pointed at anyone else.**
4. Snapshot `pre-lab07` (recommended).

## Lab Environment and Starting State

- Host machine (browser, Wireshark) + one Ubuntu lab VM (host-only), IP like `192.168.56.x`.
- You will start a local HTTP server in the VM: `python3 -m http.server 8000` (serves the VM's current folder over HTTP on port 8000 — a file server you own).
- Starting state: no capture yet; no Wireshark group membership confirmed.

## Tasks

1. **Interface sanity:** open Wireshark; note interfaces with live counters. Start a capture on the interface that carries your traffic (for VM-internal tests, capture *inside* the VM; for browser tests, on your host NIC). **Wrong interface = empty capture** — verify by generating one packet and watching the counter.
2. **ARP:** inside the VM: `ping -c 2 <gateway-or-peer-IP>` then filter `arp` — first the VM asks "who has <IP>?" (who-has/tell pair), then the reply maps IP→MAC. Annotate both frames (L2 resolving L3 — M04 §2).
3. **DNS:** filter `dns` while the browser loads any site. Find one query/response pair: read the QNAME, record type (A/AAAA), the response IP, and the resolver's IP. Note: if nothing appears, your OS/browser uses encrypted DNS (DoH) — either disable DoH *in the browser for this exercise* or resolve from the VM (`dig example.com @1.1.1.1` after allowing the VM brief NAT access for the download step — then re-isolate). Document which path you took.
4. **TCP handshake:** browse to `http://<VM-IP>:8000/` (your local server) from the host — but host→VM on host-only works; capture on whichever side you can see both. Filter `tcp.flags.syn==1 and tcp.flags.ack==0` (SYNs), then `tcp.flags.syn==1 and tcp.flags.ack==1` (SYN-ACKs), then the final ACK. Record frame numbers of the triple and the ports (client ephemeral → 8000).
5. **HTTP (plaintext):** same request, filter `http` — right-click → *Follow → TCP Stream*: the full `GET /`, `Host:` header, and `HTTP/1.1 200` response are **readable**. Save one stream screenshot. This is what "no TLS" costs.
6. **TLS ClientHello:** visit any `https://` site in the normal browser. Filter `tls` → find *Client Hello*: note offered versions (should include TLS 1.3), cipher suites, and the **SNI** hostname field (visible in plaintext). Follow into *Server Hello* + certificate. Then note subsequent records are just `Application Data`.
7. **Metadata ledger:** fill a table: *visible to eavesdropper* (DNS QNAME, destination IP, SNI, timing, sizes) vs *protected by TLS* (URLs/paths, bodies, cookies, headers). This is your core finding.
8. **Export + re-verify:** `File → Save As → lab07.pcapng`; close Wireshark, reopen the file, re-apply your filters — confirm the evidence reproduces. Copy into the portfolio.

## Expected Observations

| Landmark | Filter | Expected signature |
|---|---|---|
| ARP | `arp` | who-has/tell pair, only on local segment (never crosses router) |
| DNS | `dns` | QNAME + A/AAAA answer; resolver IP visible (or DoH → no plaintext — document) |
| Handshake | `tcp.flags.syn==1` | SYN (client→server), SYN-ACK, ACK within milliseconds, ports visible |
| HTTP | `http` | Fully readable request/response when served plain |
| TLS | `tls` | Client Hello with TLS 1.3 + SNI; then opaque `Application Data` |

Investigation-level insight: **HTTPS hides content, not destination metadata** (worked example in M04).

## Investigation Questions

1. Why does ARP never appear in a capture taken beyond your local segment? What does that imply about ARP spoofing scope (M08 preview)?
2. Your handshake capture: what exact tuple (srcIP, srcPort, dstIP, dstPort, proto) defines this connection? Why is port 8000 fixed but the client port random?
3. From the metadata ledger alone (no payload), how could an observer infer *what kind* of site you visited? Name two mitigations from the course (DoH/VPN — and their trade-offs).
4. The HTTP stream contained a cookie in plaintext (if your local server logged/sent one — otherwise imagine one): state the impact and the TLS fix.
5. If the capture showed *only* Application Data with no Client Hello, what must have happened? (Capture started mid-connection — handshake missed. What should an analyst do? Restart capture, capture from session start.)

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| No packets | Wrong interface / capture permission | Watch counters while generating traffic; join `wireshark` group + re-login (`sudo usermod -aG wireshark $USER`) |
| `http` filter shows nothing for modern sites | Site is HTTPS | Use `tls`; plaintext HTTP only appears for plain sites (your `:8000` server!) |
| No DNS rows | OS/browser using DoH | Disable DoH in browser settings temporarily, or resolve from VM (Task 3 note) |
| Can't reach `:8000` from host | Capturing/serving on wrong side, or server bound to VM-only | Serve in VM, capture in VM; or bind `0.0.0.0` **inside the host-only network only** |
| Filters red/error | Display-filter syntax | Wireshark uses `tcp.flags.syn`, not BPF `tcp-syn`; check autocomplete |
| Client Hello missing SNI | Encrypted Client Hello (ECH) rollout | Note it — a modern development; use the certificate record instead |

## Evidence to Collect

- `lab07.pcapng` (re-openable; graders re-run your filters).
- Screenshots: each of the five landmarks with its filter visible in the bar and your annotation.
- `metadata-ledger.md` (visible vs protected table).
- `handshake-frames.md` (frame numbers + tuple).
- Safety statement: *captured own host/lab traffic only on host-only network; isolation proof attached; no scanning tools used.*

## Deliverable and Report Structure

`portfolio/LAB-07/`: (1) environment + isolation proof reference, (2) five annotated landmarks (screenshot + 2 sentences each: what/why), (3) metadata ledger, (4) saved capture, (5) safety statement. 2 pages.

## Completion Checklist

- [ ] Isolation proof current for this VM
- [ ] Five landmarks captured and annotated (ARP, DNS, handshake, HTTP, TLS ClientHello)
- [ ] Handshake frame numbers + 4-tuple recorded
- [ ] Plaintext HTTP stream screenshot (readable content)
- [ ] Metadata ledger: visible vs protected, with 2 mitigations named
- [ ] `.pcapng` exported and re-verified from file
- [ ] Safety statement written

## Cleanup and Reset

1. Stop all captures; close Wireshark.
2. Stop the local server: `Ctrl+C` in its terminal (its process exits; nothing else changes).
3. If you disabled browser DoH, re-enable it.
4. Keep `lab07.pcapng` in the portfolio; delete stray capture temp files.
5. Revert to `pre-lab07` snapshot if you changed VM state — or keep going to LAB-08 on the same VM.

## Optional Challenges

- Download 2–3 **Wireshark Sample Captures** (documented free source) and repeat Tasks 4–6 on someone else's *published, meant-for-training* files — no live capture needed.
- Capture a full `wget http://<vm-ip>:8000/<file>` transfer and compute throughput from frame timestamps.
- Write display filters without looking them up: "TLS records to port 443 from one IP" — then verify (`tls && tcp.port==443 && ip.addr==…`).
- Sketch how Suricata (M08) would alert on your HTTP stream's content — what would a signature match?

## References and Safety Notes

- Wireshark Display Filter Reference: <https://wiki.wireshark.org/DisplayFilters>; User's Guide: <https://wiki.wireshark.org>.
- Wireshark Sample Captures (documented training PCAPs): <https://wiki.wireshark.org/SampleCaptures/>.
- RFC 9110 (HTTP semantics), RFC 8446 (TLS 1.3), RFC 1035 (DNS) — see M04 readings.
- Course: [M04](../../modules/module-04-networking-fundamentals-for-security/README.md) · [Lab Safety Policy](../../lab-safety-policy.md) (§4 isolation, §5 tool rules).
- **Safety:** capture interfaces are your own; targets are your lab VM and your own browser sessions. No packet capture on networks you don't own (Safety Policy §5) — café/office/uni networks are out of scope even passively beyond your own device's ordinary traffic.

**Navigation:** · [← Previous: LAB-06](../lab-06-auth-access-control/README.md) · [Lab index](../README.md) · [Next: LAB-08 →](../lab-08-firewall-config-audit/README.md)
