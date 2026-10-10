---
title: "Module 06 Quiz — Cryptography and Applied Cryptography"
layout: default
---

# Module 06 Quiz — Cryptography and Applied Cryptography

**Type:** Formative knowledge check (completion gate) · **Questions:** 14 (10 multiple choice + 4 applied short answer) · **Pass mark:** ≥ 80% (12 of 14) · **Unlimited retakes**

**Instructions.** Answer everything first, then reveal the worked answers. For applied questions, name the algorithm/mode/tool *and* say in one line why it fits. Score: 1 point each; ≥ 12 passes.

**Coverage.** Maps to Module 06 learning outcomes 1–4 ([roadmap](../../course-roadmap.md#m06--cryptography-and-applied-cryptography)): algorithm families, key handling, misuse detection, certificates/TLS.

**Related:** [Module 06 lesson](../../modules/module-06-cryptography/README.md) · [LAB-05 hashing & signatures](../../labs/lab-05-hashing-integrity-signatures/README.md) · [LAB-03 password hashes](../../labs/lab-03-password-hashes/README.md) · [CS-2 case study](../case-studies/cs-2-product-launch-crypto-identity.md)

> **Safety reminder:** run every cryptographic command only on your own files inside the lab VM. See the [Lab Safety Policy](../../lab-safety-policy.md).

---

## Part A — Multiple choice (10)

**Q1.** A colleague proposes using **MD5** to verify that a downloaded software package is authentic. The core problem is:

- (a) MD5 is too slow for large files
- (b) MD5 is not a hash function
- (c) MD5 collisions can be constructed, so an attacker can forge a matching hash for malicious content
- (d) MD5 requires a secret key to compute

**Q2.** In **ECB mode**, encrypting a file has the property that:

- (a) Identical plaintext blocks produce identical ciphertext blocks, revealing patterns
- (b) Each block depends on all previous blocks
- (c) A nonce is required for every message
- (d) It is authenticated, so tampering is detected

**Q3.** Which statement correctly distinguishes the three families?

- (a) Symmetric uses one shared key; asymmetric uses a key pair; hashes use no key
- (b) Symmetric is only for signatures; asymmetric is only for confidentiality
- (c) Hashes are a form of encryption that can be reversed with the right key
- (d) Asymmetric is always faster than symmetric for bulk data

**Q4.** You must store user passwords so that a database leak does not immediately expose them. Best choice:

- (a) SHA-256 of the password, unsalted
- (b) bcrypt/scrypt/Argon2 with a per-user salt
- (c) AES-encrypt the password with a server-side key
- (d) Base64-encode the password

**Q5.** A digital signature over a message primarily provides:

- (a) Confidentiality of the message
- (b) Integrity, authenticity, and non-repudiation — but not confidentiality
- (c) Compression of the message
- (d) Replay protection by itself

**Q6.** In TLS, the server's certificate is used by the client to:

- (a) Encrypt the application data directly
- (b) Verify the server's identity against a trusted CA chain, then obtain the public key for the handshake
- (c) Compress headers before transmission
- (d) Authenticate the *client* to the server

**Q7.** Which is the strongest practical password for a user today (assume a site with rate limiting)?

- (a) `Password1!`
- (b) `correct-horse-battery-staple-42-xkcd`
- (c) `Tr0ub4dor&3`
- (d) `aaaa1111`

**Q8.** Which is a correctly chosen IV/nonce requirement for AES-GCM?

- (a) The IV must be unique per key per encryption; reusing it catastrophically weakens authentication
- (b) The IV should always be zero for reproducibility
- (c) The IV must be secret, like the key
- (d) The IV may repeat as long as the plaintext differs

**Q9.** Post-quantum cryptography matters because:

- (a) Quantum computers make all encryption impossible
- (b) Shor's algorithm breaks RSA/ECC key exchange, while symmetric ciphers with adequate key sizes largely survive (Grover merely reduces effective strength)
- (c) Quantum computers only speed up hashing
- (d) PQC is only relevant to TLS certificates

**Q10.** Which best states **Kerckhoffs's principle**?

- (a) Security should depend on a secret algorithm design
- (b) The system must be secure even if everything about it except the key is public
- (c) Keys should be as short as possible
- (d) Encryption should be performed only by hardware

## Part B — Applied short answer (4)

**Q11. (Outcome 2)** Write the OpenSSL command pair to (i) encrypt a file with a passphrase using AES-256-GCM or AES-256-CBC, and (ii) decrypt it. Say in one line what the IV/salt contributes.

**Q12. (Outcome 3 — misuse hunt)** For each snippet, name the weakness class and the fix, using a CWE or short name:
- (a) `hash = md5(password)` stored in the database
- (b) `cipher = AES.new(key, AES.MODE_ECB)` used for a JSON config file
- (c) `iv = b'\x00' * 16` used for every message with the same key
- (d) `API_KEY = "sk-live-..."` committed in source code

**Q13. (Outcome 4)** Explain what a browser checks when it validates `https://example.com`'s certificate chain, listing three checks. What does the chain *not* prove?

**Q14. (Outcome 1–2)** You need to send a confidential, signed message to a colleague using asymmetric crypto only (no pre-shared secret). Describe the correct sequence of operations on both sides, naming which key does what.

---

## Worked answers

<details>
<summary><b>Part A answers</b></summary>

**Q1 — (c).** Practical MD5 collisions let an attacker craft different content with the same hash, defeating integrity/authenticity. Misconception: (a) confuses performance with security — MD5 is fast, and speed is not the flaw; (b) is simply false; (d) describes MACs/hashes with keys — hashing needs no key, which is exactly why it cannot prove authenticity alone.

**Q2 — (a).** ECB encrypts each block independently, so identical plaintext blocks map to identical ciphertext blocks (the classic "encrypted bitmap still shows a pattern" demo). Misconception: (b) describes CBC/CTR; (c) describes stream/nonce modes; (d) is wrong — ECB provides no integrity at all.

**Q3 — (a).** One shared key vs. a mathematically linked key pair vs. a one-way fixed-size digest with no key. Misconceptions: (b) inverts the roles (symmetric = bulk confidentiality, asymmetric = key exchange/signatures); (c) hashes are one-way, not encryption; (d) asymmetric (public-key ops) is typically *slower*, which is why hybrid TLS uses it only to establish a symmetric session key.

**Q4 — (b).** A memory-hard password hash (bcrypt/scrypt/Argon2) with a unique salt resists GPU/ASIC cracking. Misconceptions: (a) unsalted fast hashes fall to rainbow tables and brute force; (c) reversible encryption means the key leak exposes everything, and the server must decrypt anyway; (d) encoding is not protection at all.

**Q5 — (b).** Signing with the private key lets anyone verify with the public key: integrity (hash bound in), authenticity (only key holder signed), non-repudiation (holder cannot plausibly deny). Misconception: (a) signing does not hide the message — add encryption for that; (c) irrelevant; (d) signatures alone don't stop replay — bind a nonce/timestamp.

**Q6 — (b).** The certificate binds the hostname to a public key, chained to a trusted CA; the client validates signatures up to a trust-store root, then uses the public key in the (EC)DHE handshake. Misconceptions: (a) application data uses session keys derived in the handshake; (c) unrelated; (d) client certificates, if used at all, are a separate optional mechanism.

**Q7 — (b).** A long random passphrase (~44 bits of charset entropy × length) resists both guessing and cracking far better than short complexity tricks. Misconceptions: (a)/(c) are short and follow predictable mutation patterns — exactly what rules produce and crackers model; (d) has tiny keyspace despite meeting "complexity" rules.

**Q8 — (a).** GCM's security proof collapses on nonce reuse under the same key (the authentication key can be recovered, forgeries become possible). Misconceptions: (b) fixed zero IV repeats across messages — the exact failure; (c) IVs are public by design, that's fine; (d) repetition is safe for random IVs in *some* modes but never acceptable for GCM per-key uniqueness.

**Q9 — (b).** Shor's algorithm efficiently factors/discrete-logs, breaking RSA, DHE, ECDHE — i.e., today's key establishment. Grover only gives a quadratic speedup against symmetric ciphers/hashes, halving effective key length (hence AES-256). Misconceptions: (a) overstates — symmetric crypto survives with larger keys; (c) hashing isn't the target; (d) PQC covers key exchange *and* signatures everywhere, not just certificates.

**Q10 — (b).** The design must not rely on obscurity; only the key is secret. This is what lets algorithms be standardized, publicly scrutinized, and safely reused. Misconceptions: (a) is security through obscurity, the opposite; (c) key length policy, not the principle; (d) irrelevant.

</details>

<details>
<summary><b>Part B model answers</b></summary>

**Q11.** Encrypt: `openssl enc -aes-256-cbc -salt -in plain.txt -out plain.enc` (prompts for passphrase) — or with GCM via `openssl enc -aes-256-gcm` where supported / Python `cryptography` for authenticated encryption. Decrypt: `openssl enc -d -aes-256-cbc -salt -in plain.enc -out plain.out`. The salt (stored in the file header) makes each encryption of the same passphrase produce a different key/IV, defeating precomputation; the IV ensures identical plaintexts encrypt differently. *Point if:* correct commands **and** IV/salt role stated. → [Module 06 lesson](../../modules/module-06-cryptography/README.md), [LAB-05](../../labs/lab-05-hashing-integrity-signatures/README.md)

**Q12.** (a) **Plaintext/fast hash for passwords** — CWE-916 (use of password hash with insufficient work factor); fix: Argon2id/bcrypt with unique salt. (b) **ECB mode** — CWE-327/CWE-328; fix: AES-GCM (authenticated) or CBC/CTR with HMAC, random IV. (c) **Static/reused IV (nonce)** — CWE-329 (not generated uniquely); fix: random 96-bit nonce per encryption, never reused per key. (d) **Hard-coded secret** — CWE-798; fix: remove from history, revoke/rotate, inject via environment/secret manager. *Point each: name + fix.*

**Q13.** Browser checks: (1) signature on the leaf certificate validates using the issuer's public key; (2) chain walks up to a root in the trust store (intermediates valid, not expired/revoked — CRL/OCSP or stapling); (3) hostname matches the certificate's SAN, and validity dates cover *now*. What it does **not** prove: that the *site content* is safe, that the private key hasn't leaked (a valid cert can belong to an attacker who obtained it), or anything about the client's identity. → [Module 06 lesson](../../modules/module-06-cryptography/README.md)

**Q14.** Sender: hash the message; **sign the hash with own private key**; **encrypt the message (or the hash+message) with recipient's public key**. Receiver: **decrypt with own private key** to recover the message; recompute the hash; **verify the signature with sender's public key**. Confidentiality comes from the recipient's public key (only their private key opens it); authenticity/integrity from the sender's signature. Misconception to avoid: encrypting with your *own* public key gives anyone — not just the recipient — the ability to decrypt.

</details>

---

## Module-end review exercises (ungraded, harder)

1. **Misuse hunt (configuration analysis).** Given 6 code/config snippets (ECB image, MD5 passwords, fixed IV, hard-coded key, weak RNG, homemade XOR), write the flaw, CWE, and fix for each — the M06 lab deliverable. Target: 5/6 correct.
2. **Log/data interpretation.** Given two ciphertext files produced by the same key, design a quick test that distinguishes ECB from CBC (hint: block repetition statistics) and explain what an attacker learns in each case.
3. **Risk prioritization.** A small org stores passwords with SHA-256 (no salt), uses TLS 1.0 on an internal portal, and keeps SSH root keys on shared laptops. Rank these three by risk with a one-line justification each, then give a remediation order.
4. **Practical investigation.** Capture your own local TLS handshake (browser to a local HTTPS server), identify the negotiated cipher suite and certificate details, and answer: was forward secrecy in play, and how do you know?

*Review guidance:* exercise 1 is portfolio evidence; exercise 3 mirrors how the capstone scores risk trade-offs — rank with reasons, not feelings.

**Next:** [M07 quiz](./quiz-m07.md) · **Previous:** [M05](../level-1/quiz-m05.md) · **Hub:** [Assessment Hub](../README.md)
