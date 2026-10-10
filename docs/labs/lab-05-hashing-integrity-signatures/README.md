---
title: "LAB-05 — Cryptographic Hashing, Integrity Verification, and Digital Signatures"
layout: default
---

# LAB-05 — Cryptographic Hashing, Integrity, and Digital Signatures

**Lab ID:** LAB-05 · **Difficulty:** Intermediate · **Estimated duration:** 2 hours · **Module:** M06 · **Mode:** Hands-on, offline, own machine

## Scenario

The **Sunrise University IT office** distributes a "scholarship application template" file to students via a notice board. Last semester someone swapped it for a lookalike containing a phishing form, and nobody noticed for two weeks. Management wants three things demonstrated: (1) how to let anyone *detect* tampering, (2) how to prove a file came from the IT office, and (3) why a plain hash alone proves integrity but not *origin*. You will build both mechanisms locally with free tools and document the procedure for the office.

## Learning Objectives

1. Compute and verify cryptographic hashes; explain collision resistance in plain language.
2. Demonstrate tamper detection: modify one byte and show the hash avalanche effect.
3. Use HMAC to show shared-secret message authentication and why it differs from a plain hash.
4. Create a key pair, sign a file, verify the signature, and articulate what the signature proves (integrity + authenticity + non-repudiation) vs what it does not.
5. Distinguish MD5/SHA-1 status (broken/weak for signatures) from SHA-2/SHA-3 recommendations.

## Prerequisites and Required Skills

- Module 06 concepts (hashes, symmetric/asymmetric, PKI basics). Terminal comfort from M04/M05.
- No network needed after tool installation; everything runs locally.

## Tools, Operating Systems, and Versions

| Tool | Use | Install (free) |
|---|---|---|
| `sha256sum` / `sha1sum` / `md5sum` | File hashing | preinstalled (coreutils) |
| Python 3 (`hashlib`, `hmac`) | Hash/HMAC demos | preinstalled or python.org |
| GnuPG (GPG) | Key generation, signing, verification | `sudo apt install gnupg` (current 2.2/2.4.x series) |
| Optional: OpenSSL 3.x | Cross-check signatures | preinstalled on most systems |

**$0.** Use whatever versions your OS ships; commands below are stable across them.

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-05/` and a scratch dir `~/sig-lab/`.
2. Install GnuPG if missing (`sudo apt install gnupg` — installs only the encryption tool to your machine).
3. Permissions: your own machine and files only; no accounts, no targets, no authorization needed.

## Lab Environment and Starting State

A scratch directory containing one document you create (`scholarship-template.txt`, a few lines of plausible content) plus your GPG keypair (created in Task 3, **no passphrase reuse — use a fresh passphrase or none for the lab, documented as lab-only**). Starting state: no hashes, no keys.

## Tasks

1. **Baseline hash + tamper detection:**
   ```bash
   printf 'Application deadline: 2026-11-30\n' > scholarship-template.txt
   sha256sum scholarship-template.txt | tee original.sha256
   ```
   *What it does:* writes the file, computes its SHA-256 (64-hex fingerprint), `tee` prints **and** saves the fingerprint. Now edit one character (`sed -i 's/30/31/' scholarship-template.txt` — `sed -i` edits in place, replacing 30 with 31) and run `sha256sum -c original.sha256` (recomputes and compares). **Expected:** `FAILED` — one-character change ⇒ completely different hash (**avalanche effect**). Restore the original (`sed -i 's/31/30/'`) and show `OK` again.
2. **Why not MD5/SHA-1:** run all three digests on the same file (`md5sum; sha1sum; sha256sum`) and record lengths (32/40/64 hex chars). Explain in your notes: MD5's collision resistance is broken (practical collision techniques published since 2004-ish era) and SHA-1 likewise (SHAttered, 2017) — so both are unacceptable for *signatures*; SHA-256 is today's default (NIST SHA-3 exists as an alternative standard).
3. **HMAC (shared-secret authenticity):**
   ```bash
   python3 -c "import hmac,hashlib;k=b'lab-only-shared-key';m=open('scholarship-template.txt','rb').read();print(hmac.new(k,m,hashlib.sha256).hexdigest())" | tee hmac.txt
   ```
   *What it does:* computes HMAC-SHA256 — a keyed fingerprint: only someone with key `k` can *produce* a matching tag, but anyone who steals the file+tag can *verify*. Re-run after your one-byte edit: tag changes (integrity). Then compute with a different key: tag differs entirely (key-dependence). Note the limitation in your report: **shared secret ⇒ both parties can forge** — no non-repudiation.
4. **Asymmetric signatures (the fix):** generate a key pair: `gpg --quick-generate-key "IT Office (LAB-05) <itoffice.lab@example.edu>" default default never` (creates a modern default algo keypair; `never` = no expiry for lab use). Sign the file: `gpg --armor --output scholarship.sig --detach-sign scholarship-template.txt` (detach-sign = signature as a separate file). Verify: `gpg --verify scholarship.sig scholarship-template.txt` → **`Good signature`**.
5. **Break it:** alter one byte of the file, verify again → `BAD signature!`; restore. Also try verifying with the signature file intact but a *different* key absent — explain what error appears and why trust in the public key (fingerprints!) is the root of the whole system.
6. **Fingerprint practice:** `gpg --fingerprint` — record your key fingerprint. In the office scenario, how should students confirm it? (Out-of-band: printed on notice, read over phone — an M01/M06 trust-anchor story.)
7. **Office procedure write-up** (deliverable): 10-step instructions for Sunrise IT: what to publish (SHA-256 + signature), what students verify, and what to do if either check fails.

## Expected Observations

| Step | Expected result |
|---|---|
| 1 | 1-byte edit ⇒ `sha256sum -c` = FAILED; restore = OK |
| 2 | MD5 32 / SHA-1 40 / SHA-256 64 hex chars; one-line rationale for rejecting MD5/SHA-1 in signatures |
| 3 | HMAC stable for identical file+key; changes with file **or** key |
| 4 | `gpg --verify` prints `Good signature` with your name |
| 5 | Tampered file ⇒ `BAD signature!` — deterministic detection |
| 6 | Fingerprint recorded; out-of-band confirmation method described |

## Investigation Questions

1. Alice receives `file` + `sha256.txt` from a compromised website — both consistent. What did the hash *not* protect against? What single addition (signature + trusted key) closes it?
2. Why can HMAC provide non-repudiation... *it can't* — explain precisely which of the CIA/non-repudiation properties it does provide and which party could later deny.
3. A legacy system "only supports SHA-1 signing." Using this lab's evidence, write two sentences of risk language for management (what an attacker could do, and the migration recommendation).
4. If GPG private keys are stolen, what is the blast radius vs a stolen HMAC shared key? (Compare who can forge what.)
5. How does TLS use both mechanisms (certificate signatures = asymmetric; session integrity = symmetric/MAC)? Preview only — confirm in M06 reading.

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `gpg: command not found` | Not installed | `sudo apt install gnupg` (or Gpg4win on Windows — free) |
| `gpg --verify` = "No public key" | Verifying on a machine without the public key | Import first: `gpg --import itoffice.pub.asc` — this *is* the trust step |
| `sha256sum -c` says OK after your edit | File not actually changed (sed pattern missed) | `cat` the file to confirm the edit landed |
| Entropy warnings during keygen | VM lacks activity | Move the mouse / run `rng-tools`-free fix: just re-run; lab keys don't need HSM-grade entropy |
| HMAC python line errors on quotes | Shell quoting | Copy the line exactly; keys/files must exist first |
| "Bad signature" on an unmodified file | Wrong file/signature pair, or CRLF conversion in transfer | Compare with `sha256sum` of the original; move both files in binary mode |

## Evidence to Collect

- Screenshots/outputs: tamper FAILED→OK cycle; three digest lengths; HMAC stability/change tests; `Good signature` and `BAD signature!` pair; key fingerprint.
- `hmac.txt`, `original.sha256`, `scholarship.sig` (small artifacts — keep them).
- `office-procedure.md` (Task 7).
- Safety statement: *local files only; key pair generated for lab purposes.*

## Deliverable and Report Structure

`portfolio/LAB-05/`: (1) method + commands with explanations, (2) results table per task, (3) HMAC-vs-signature comparison paragraph (properties table), (4) the 10-step office procedure, (5) safety statement. 2 pages.

## Completion Checklist

- [ ] Tamper-detection cycle demonstrated (FAILED → restored OK)
- [ ] MD5/SHA-1/SHA-256 lengths recorded with rejection rationale (collision evidence named)
- [ ] HMAC computed; file-change and key-change behavior both shown
- [ ] GPG keypair created; detach-sign + verify = `Good signature`
- [ ] Tampered file = `BAD signature!`; restore shown
- [ ] Fingerprint recorded with out-of-band confirmation method
- [ ] Office procedure written (10 steps)
- [ ] Safety statement written

## Cleanup and Reset

1. Delete lab keys when done: `gpg --delete-secret-keys "IT Office (LAB-05)"` then `--delete-public-keys` (removes only the key you created; confirm the fingerprint prompt). *Purpose: lab keys have lab passphrases — don't leave clutter in your keyring.*
2. Keep artifacts in `portfolio/LAB-05/`; remove `~/sig-lab/` (`rm -rf ~/sig-lab` — path checked first, your own scratch dir only).
3. No network residue; nothing to roll back.

## Optional Challenges

- Verify a **real** published artifact: download Ubuntu's `SHA256SUMS` + `.iso` (documented source, large — use the tiny `SHA256SUMS` against any small official file you download) and run the full out-of-band trust discussion (where do you get the checksum from?).
- Sign with OpenSSL (`openssl dgst -sha256 -sign`) and verify with GPG or vice versa — document interoperability limits.
- Write a 5-line shell script `check.sh` that verifies a file against a stored hash and exits 0/1 — the seed of LAB-18 automation.

## References and Safety Notes

- GnuPG manual: <https://www.gnupg.org/documentation/>; `gpg(1)` man page.
- NIST FIPS 180-4 (SHA-2 family) and FIPS 202 (SHA-3): <https://csrc.nist.gov/publications/fips>.
- NIST SP 800-175B (guidelines for cryptographic use): <https://csrc.nist.gov/pubs/sp/800/175/b/final>.
- OWASP *Cryptographic Storage Cheat Sheet*: <https://cheatsheetseries.owasp.org/cheatsheets/Cryptographic_Storage_Cheat_Sheet.html>.
- Course: [M06](../../modules/module-06-cryptography/README.md) · [Lab Safety Policy](../../lab-safety-policy.md).
- **Safety:** offline lab; keys/files are yours; never reuse the lab passphrase or private key anywhere real; no systems contacted.

**Navigation:** · [← Previous: LAB-04](../lab-04-permissions-hardening/README.md) · [Lab index](../README.md) · [Next: LAB-06 →](../lab-06-auth-access-control/README.md)
