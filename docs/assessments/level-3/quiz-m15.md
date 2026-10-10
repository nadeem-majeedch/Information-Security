---
title: "Module 15 Quiz — Malware Concepts and Defensive Analysis"
layout: default
---

# Module 15 Quiz — Malware Concepts and Defensive Analysis

**Type:** Formative knowledge check (completion gate) · **Questions:** 12 (8 multiple choice + 4 analysis scenarios) · **Pass mark:** ≥ 80% (10 of 12) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. Analysis scenarios: classify, justify from evidence, and end with a *defensive* action (rule, IOC, or playbook change).

**Coverage.** Maps to Module 15 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m15--malware-concepts-and-defensive-analysis)): classification dimensions, static triage, sandboxed dynamic analysis, translating observations into defenses.

**Related:** [Module 15 lesson](../../modules/module-15-malware-and-defensive-analysis/README.md) · [LAB-16 malware behavior](../../labs/lab-16-malware-behavior/README.md) · [LAB-13 log analysis](../../labs/lab-13-log-analysis/README.md) · [CS-3 case study](../case-studies/cs-3-detection-to-response.md)

> **Safety reminder:** all analysis in this course uses **benign training binaries you compile yourself** or provided synthetic artifacts, inside an **isolated sandbox VM** (no shared clipboard/folders, host-only networking). Never analyze unknown real malware on a normal machine. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (8)

**Q1.** The four classification dimensions for malware are:

- (a) Color, size, price, age
- (b) Vector (how it arrives), payload (what it does), propagation (how it spreads), business model (why it exists)
- (c) Author, country, language, license
- (d) Filename, extension, icon, signature

**Q2.** **Packing/encryption** of a malware sample primarily defeats:

- (a) Hashing
- (b) Static signature/feature analysis — content is obfuscated until unpacked in memory, so static tools see little until dynamic analysis or unpacking
- (c) Network monitoring
- (d) File size limits

**Q3.** In **static triage** you would *not*:

- (a) Compute hashes (MD5/SHA-256)
- (b) Extract strings and imports
- (c) Run the sample to watch its behavior
- (d) Match YARA rules against the file

**Q4.** A sandbox VM for dynamic analysis must be:

- (a) Your daily-driver laptop with antivirus on
- (b) Isolated (host-only/no real internet egress), snapshot-able, with no shared folders/clipboard to the host
- (c) Connected to your home Wi-Fi so callbacks reach real servers
- (d) Running as a domain-joined machine with your real credentials

**Q5.** Which is the strongest IOC for *retroactively* hunting a specific sample across logs?

- (a) The file's size in bytes
- (b) A cryptographic hash of the sample (SHA-256) plus its C2 domain/IP when observed
- (c) The file's creation timestamp
- (d) The analyst's notes

**Q6.** A **YARA rule** is best described as:

- (a) A firewall
- (b) A pattern-matching rule over file/memory content (strings, byte patterns, conditions) used to detect related samples
- (c) An encryption standard
- (d) A sandboxing hypervisor

**Q7.** "Living-off-the-land" malware is dangerous mainly because it:

- (a) Uses large files
- (b) Executes with trusted OS binaries (PowerShell, WMI, certutil), so activity blends with admin behavior and signature detection struggles — behavior and context become the detectors
- (c) Avoids the network entirely
- (d) Cannot be hashed

**Q8.** Translating analysis into defense means producing:

- (a) A longer malware essay
- (b) Concrete IOCs (hashes, domains, IPs), detection rules (YARA/Sigma mapped to ATT&CK), and IR playbook updates — artifacts other controls consume
- (c) Only a severity label
- (d) A new sandbox VM

## Part B — Analysis scenarios (4)

**Q9. (Outcome 1 — classification).** Classify along all four dimensions: *"A Word document arrives by email carrying an embedded macro that, when enabled, downloads a DLL that encrypts local files and spreads to shared drives; the authors offer a paid unlock service."* Name the vector, payload, propagation, and business model — and one preventive control per dimension.

**Q10. (Outcome 2 — static triage).** Your static pass on a training binary shows: SHA-256 recorded; strings include `UpdaterTask`, `C:\ProgramData\syscache.dat`, `powershell -enc`; imports include registry functions and `CreateProcess`; YARA matches your own rule `Training_BehaviorMarkers`. State what each artifact *suggests* (three sentences max), what it does NOT prove yet, and the next analysis step.

**Q11. (Outcome 3 — dynamic analysis).** In the isolated sandbox, the sample: writes `C:\ProgramData\syscache.dat`, adds `Run` key `SysCache`, spawns `powershell -enc …`, and attempts DNS query `cdn-check.example` (blocked by host-only networking). Document the behavior in IOC terms: 3 IOCs (typed: file, registry, network), 2 ATT&CK techniques, and one detection (Sigma) you could write.

**Q12. (Outcome 4 — defensive translation).** Your Sigma rule for the Run-key persistence fires *twice a week* — both times it's a legitimate software updater. Tweak the rule so it stays useful: what would you add to reduce these false positives without hiding real malware (two options), and what's the risk of over-tuning?

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (b).** Vector/payload/propagation/business model give a complete "how it got in, what it does, how it moves, who profits" picture. Misconceptions: (a)/(c)/(d) are metadata, not behavior — they don't inform defenses.

**Q2 — (b).** Packers compress/encrypt content; static signatures can't see through them until the sample unpacks at runtime — which is why dynamic analysis (or unpacking) complements static. Misconceptions: (a) hashing works on ciphertext — the hash is still a valid locator; (c) network monitoring sees behavior, not file content; (d) unrelated.

**Q3 — (c).** Running it is *dynamic* analysis — different tools, different environment, different risk profile. Misconceptions: (a)/(b)/(d) are core static triage steps (hash, strings/imports, YARA).

**Q4 — (b).** Isolation + snapshot + no host sharing = you can observe safely and reset. Misconceptions: (a) endangers your real data/credentials; (c) real callbacks reach criminal infrastructure *from your IP* — legal and safety problem; (d) domain creds in a malware sandbox is catastrophic.

**Q5 — (b).** Hashes (sample) + network indicators (C2) are stable, greppable identifiers you can search across endpoints, mail gateways, and logs. Misconceptions: (a) sizes collide trivially; (c) timestamps are per-file and spoofable; (d) notes don't index across systems.

**Q6 — (b).** YARA = pattern/condition rules over content; "the malware signature language" for files and memory. Misconceptions: (a) enforcement happens elsewhere (EDR/AV consumes YARA); (c)/(d) unrelated technologies.

**Q7 — (b).** LOLBins inherit trust: `powershell.exe` is supposed to run on Windows, so file reputation fails — you detect by *argument patterns, parent-child chains, and context* (e.g., `winword.exe → powershell -enc`). Misconceptions: (a) often tiny; (c) usually networks; (d) hashing still works — it just doesn't help identify *intent*.

**Q8 — (b).** Analysis that doesn't end in a consumable artifact (IOC, rule, playbook edit) is academic — defense needs feeds other controls use. Misconceptions: (a) prose without artifacts doesn't detect anything; (c) severity alone doesn't help hunt; (d) infrastructure, not output.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q9.** **Vector:** email with weaponized document (phishing/macro dropper) → *prevent:* mail filtering + macro policy (block internet-sourced macros / disable with例外 controlled via GPO/ASR rules), user reporting path. **Payload:** DLL drops and encrypts local files (ransomware) → *prevent:* application allowlisting/EDR to block unknown DLL execution, and least privilege to limit reach. **Propagation:** spreads to shared drives (worm-like lateral movement over SMB shares) → *prevent:* network segmentation + share permissions (M08) and disable unnecessary SMB; also offline/3-2-1 backups (recovery). **Business model:** ransomware-as-a-service, paid unlock → *prevent* (reduce viability): never pay posture + tested offline backups + cyber-insurance consideration (transfer) — business-model controls are about making the crime unprofitable *for you*. → [Module 15 lesson](../../modules/module-15-malware-and-defensive-analysis/README.md)

**Q10.** Artifacts *suggest*: `UpdaterTask` + `CreateProcess` + registry imports → **persistence + process execution** (task/Run-key style loader); `powershell -enc` → **encoded command execution** (common loader/second-stage step); `syscache.dat` (ProgramData) + YARA match on your own behavior markers → **known training sample consistent with your planted behaviors**. **What it does NOT prove:** static presence ≠ runtime use — strings may be decoys/unreferenced, the enc blob may be benign, imports don't prove which path executes; intent requires observed execution. **Next step:** dynamic analysis in the isolated sandbox (snapshot → run → capture files/registry/process tree/network attempts) to confirm which suggestions were real. → [LAB-16](../../labs/lab-16-malware-behavior/README.md)

**Q11.** **IOCs (typed):** (1) *File:* SHA-256 of the dropped `C:\ProgramData\syscache.dat` (and its own hash) — exact-file hunting; (2) *Registry:* value/data `HKCU\Software\Microsoft\Windows\CurrentVersion\Run\SysCache = C:\ProgramData\syscache.dat` — persistence detection; (3) *Network:* domain `cdn-check.example` (DNS query) — resolver/proxy blocking and hunting. **ATT&CK techniques:** **T1547.001** (Boot/Logon Autostart: Registry Run Keys) and **T1059.001** (Command/Scripting: PowerShell) — plus **T1071.004** for the DNS beacon attempt. **Sigma detection (Run-key creation):**
```yaml
title: SysCache Run Key Persistence
logsource: { product: windows, category: registry_set }
detection:
  selection:
    TargetObject|endswith: '\CurrentVersion\Run\SysCache'
    Details|contains: 'syscache.dat'
  condition: selection
level: high
```
(with `status: stable`, ATT&CK tags `T1547.001`, and falsepositives noted as "legitimate updater with identical naming — rare"). → [LAB-16](../../labs/lab-16-malware-behavior/README.md)

**Q12.** **Reduce FPs without hiding real malware:** (1) **Narrow the *combination*, not the single signal:** require *both* the Run-key *and* an unusual parent process or an unsigned/odd-path binary — a legit updater has a known parent (its installer) and signed binary, so add conditions: `Image` not signed OR parent not in expected set; use near/sequence logic if the backend supports it. (2) **Allow-list by *identity*, not by suppressing the rule:** exclude the specific signed binary's hash/publisher + expected install path *with documented owner and expiry* — an exclusion entry is auditable; a deleted rule is not. Also add context fields (integrity level, user) so triage gets faster. **Risk of over-tuning:** each exclusion is a hiding place — attackers name files `SysCache` deliberately; exclusions keyed on mutable attributes (filename, path) can be mimicked, and exclusions without expiry silently widen. Guard: prefer cryptographic identity (hash/signer) over names, every exclusion needs owner + review date, and measure *precision before/after* (if your rule now fires only when you already know, you've bought silence, not detection). → [M13 lesson](../../modules/module-13-logging-monitoring-and-security-operations/README.md) · [M15 lesson](../../modules/module-15-malware-and-defensive-analysis/README.md)

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Safe triage (practical).** Analyze 2 **self-built benign training binaries** (marker behaviors: writes a file, sets a startup entry *in the VM only*, harmless local DNS): hash → strings/imports → YARA match → documented behavior. M15 deliverable — self-built only, sandboxed.
2. **YARA authoring.** Write 3 YARA rules matching your training binaries' features; verify with `yara` CLI; iterate until they do **not** match system files (test against `C:\Windows\System32` — measure false positives).
3. **IOC handoff (investigation).** Produce an IOC package (STIX-lite JSON or CSV) + 2 Sigma rules mapped to ATT&CK, then **feed them into your M13 detection setup and trigger them in-lab** — the handoff loop is the point.
4. **Risk prioritization.** Given 4 samples (packed banker, unsigned script dropper, signed LOLBin abuse, benign updater with cloud lookup), order your analysis time by expected defensive value and justify in one line each — insight: *the sample's rarity matters less than your visibility gap.*

*Review guidance:* every scenario answer ends with a **defensive artifact** (IOC, rule, playbook line). "It's malicious, probably" is a start, not a finish — the grader counts artifacts produced.

**Next:** [Level 3 case study CS-3](../case-studies/cs-3-detection-to-response.md) · **Previous:** [M14 quiz](./quiz-m14.md) · **Hub:** [Assessment Hub](../README.md)
