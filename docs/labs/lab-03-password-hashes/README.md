---
title: "LAB-03 — Password Security and Offline Hash Demonstrations"
layout: default
---

# LAB-03 — Password Security and Offline Hash Demonstrations

**Lab ID:** LAB-03 · **Difficulty:** Intermediate · **Estimated duration:** 2–2.5 hours · **Modules:** M06, M07 · **Mode:** Offline cracking of **provided synthetic hashes only**

## Scenario

Your security team inherited a legacy staff portal whose user database was exported *before* the company migrated to a better system. The export contains only username + password hashes (a common breach shape). Leadership wants to know: *"How badly would we be exposed if this export leaked?"* You will demonstrate the answer using **the provided synthetic dataset** — offline, on your own machine — and write recommendations grounded in current password guidance.

## Learning Objectives

1. Explain what a password hash is and why systems store hashes rather than passwords.
2. Demonstrate unsalted fast-hash weakness by recovering provided synthetic passwords with a wordlist.
3. Show, measurably, how salting and slow hashing change the attacker's economics.
4. Distinguish rainbow-table/precomputation attacks from dictionary attacks.
5. Translate results into policy recommendations aligned with NIST SP 800-63-4 password guidance.

## Prerequisites and Required Skills

- Module 06 (hashing) recommended; M07 helpful. Basic terminal use (M04/M05).
- **Scope rule:** crack **only** `data/users-hashes.csv` from this lab. Real hash lists, Wi-Fi handshakes, or any data you didn't generate are out of scope (Safety Policy §2/§6).

## Tools, Operating Systems, and Versions

| Tool | Purpose | Notes |
|---|---|---|
| John the Ripper (jumbo build) | Wordlist cracking | Free: `sudo apt install john` (Linux) or download from openwall.com. Current builds auto-detect formats. |
| *or* Hashcat | Wordlist cracking | Free; GPU optional. CPU works for this tiny set. |
| Python 3 (stdlib `hashlib`) | Verify hashes, salting demo | Free, preinstalled on most systems |
| `sha256sum` / `sha1sum` | File integrity check (ties to LAB-05) | Free |

No network access is required after installing the tools. **$0.**

## Setup (Free) and Required Permissions

1. Create `portfolio/LAB-03/`.
2. Copy the lab's `data/` files locally: `users-hashes.csv`, `wordlist-small.txt` (and keep `ANSWERS-hashes.txt` **closed** until Task 6).
3. Install John the Ripper (`sudo apt install john` — explains it installs the password-auditing tool to your machine only) or hashcat.
4. Permissions: your own machine only; no accounts, no targets, no authorization needed.

## Lab Environment and Starting State

One directory with three files. `users-hashes.csv` = 16 synthetic users; columns `username,md5,sha1,sha256`. Fifteen use well-known weak training passwords; one (`quokka`) uses a strong password whose SHA-256 entry is **salted** (salt `k7Qx9Lm2` prepended server-side — the CSV documents this). Starting state: no passwords recovered.

## Tasks

1. **Understand the target:** open the CSV. Run one manual check: `echo -n "password" | md5sum` (`echo -n` avoids a trailing newline; `md5sum` prints the MD5 of the input). Compare with alice's MD5 — confirm hashing is a deterministic one-way fingerprint.
2. **Extract crackable hashes:** produce `hashes-md5.txt` lines of `username:hash`, e.g. with `awk -F, 'NR>1{print $1":"$2}' users-hashes.csv > hashes-md5.txt` (`awk` prints fields 1 and 2 separated by a colon; `-F,` sets comma as the field separator).
3. **Dictionary attack:** `john --wordlist=wordlist-small.txt hashes-md5.txt` — John tries each wordlist entry as a candidate password against the hash until matches are found. Show progress; wait for it to exhaust the list (`john --show hashes-md5.txt` prints recovered credentials).
4. **Same attack, stronger hashes:** extract the SHA-256 column (`awk -F, 'NR>1{print $1":"$4}' …`) and repeat. Observe: same result, similar speed — SHA-256 is *fast*, and offline attackers like fast.
5. **Salting reality:** compute `quokka`'s expected salted hash in Python:
   `python3 -c "import hashlib; print(hashlib.sha256(b'k7Qx9Lm2'+'H0use-Starlight!42'.encode()).hexdigest())"` — confirm it matches the CSV. Then run John against the SHA-256 list **with the same wordlist**. `quokka` must **not** be recovered (the password is absent from the wordlist and the salt defeats precomputed tables).
6. **Self-grade:** now open `ANSWERS-hashes.txt` and confirm your recovered set. Record any misses and why.
7. **Policy memo (the real deliverable):** 150–250 words: (a) what an attacker gains from this export, quantified (how many of 16 recovered, in what time); (b) two engineering fixes (salt + slow KDF — bcrypt/scrypt/Argon2/PBKDF2; never store plaintext), one detection idea (breach-list screening), and one policy line referencing NIST SP 800-63-4 (length over composition puzzles; no forced periodic rotation without cause; screen against breached lists).

## Expected Observations

| Step | Expected outcome |
|---|---|
| Task 1 | `echo -n "password" \| md5sum` equals alice's MD5 exactly |
| Task 3 | ≥ 14/15 weak users recovered in **seconds**; `--show` lists `user:password` |
| Task 4 | SHA-256 also falls — hash strength ≠ password strength |
| Task 5 | `quokka` **not** recovered from the small wordlist; salted hash matches Python computation |
| Interpretation | MD5/SHA-256 are unsuitable password storage: no salt (precomputation) and no work factor (GPU-fast) |

## Investigation Questions

1. Why does salting not slow down a *single* password guess but cripples precomputed tables and forces per-hash work? (Explain both halves.)
2. Hashcat/GPU speeds are commonly quoted in billions of guesses/sec for MD5: what does that imply for an 8-character lowercase password vs a 4-word passphrase? Use M06 trade-off reasoning.
3. The export leaked *hashes, not passwords* — is that "no harm"? Argue both sides in 4 sentences, then state your verdict.
4. NIST SP 800-63-4 dropped several legacy password rules. Which two recommendations from your memo would have been controversial 10 years ago, and why are they better now?
5. Where does rate-limiting (server-side) fail to help in this scenario? (Think offline.)

## Troubleshooting

| Symptom | Cause | Fix |
|---|---|---|
| `john: command not found` | Not installed / not in PATH | `sudo apt install john`, or add the downloaded `run/` directory to PATH; on Windows use WSL |
| John says "no password hashes loaded" | Format not auto-detected (some builds disable raw formats) | Name the format: `john --format=raw-md5 hashes-md5.txt` (find valid names via `john --list=formats \| grep -i md5`) |
| Zero recovered in Task 3 | Wrong extraction (header row included, wrong column) | Re-run awk from Task 2; `head hashes-md5.txt` must show `alice:<32 hex>` |
| `quokka` recovered | Wrong task (unsalted hash was fed) or wordlist edited | Use the CSV's salted column; restore `wordlist-small.txt` |
| Hash mismatch in Task 5 | `echo` added a newline or shell quoting mangled `!` | Use the exact Python one-liner (it encodes bytes explicitly) |
| Tool flags downloading wordlists | Temptation to grab huge public lists | **Stop** — the lab's point is economics, not volume; large lists are an *optional* documented extension only, against your own synthetic data |

## Evidence to Collect

- Screenshots: Task 3 cracking + `john --show` output; Task 5 non-recovery of `quokka`.
- `recovered.md` — your recovered table (username → password) from self-grade.
- Timing note (start/finish of Task 3) to quantify "seconds."
- `policy-memo.md` (Task 7).
- Safety statement: *targets = provided synthetic hashes only; no live systems, no real credentials.*

## Deliverable and Report Structure

`portfolio/LAB-03/`: (1) method (commands used, why), (2) results table + timing, (3) salted vs unsalted comparison, (4) policy memo with NIST references, (5) safety statement. 1–2 pages.

## Completion Checklist

- [ ] Manual hash verification (Task 1) matches
- [ ] ≥ 14 of 15 weak hashes recovered with the provided wordlist
- [ ] SHA-256 set also cracked, with the "fast hash" insight stated
- [ ] `quokka` salted hash verified in Python and **not** recovered by wordlist
- [ ] Self-grade done against ANSWERS file
- [ ] Policy memo cites salt + slow KDF + SP 800-63-4 points
- [ ] Safety statement written

## Cleanup and Reset

1. Delete `hashes-*.txt` and any recovered-password scratch files when the report is saved (`rm hashes-md5.txt hashes-sha256.txt` — removes only the derived lab files you created; nothing else).
2. Uninstall the cracking tool if you don't want it (`sudo apt remove john`) — optional.
3. Confirm your portfolio contains no plaintext beyond the synthetic training answers file.

## Optional Challenges

- Time a brute-force run for a 4-char lowercase space (`john --incremental`) and graph why length matters.
- Re-run Task 3 after adding 100 lines of salt-prefixed hashes to a copy of the CSV — measure how per-hash salt changes bookkeeping (attackers must attack each hash separately).
- Write the "storage" half of the fix as M07 design notes: how a modern login flow stores passwords (slow KDF + per-user salt + breach screening).

## References and Safety Notes

- John the Ripper documentation: <https://www.openwall.com/john/>; hashcat wiki: <https://hashcat.net/wiki/>.
- NIST SP 800-63-4 (July 2025), *Digital Identity Guidelines* (800-63B covers authenticators/passwords): <https://pages.nist.gov/800-63-4/>.
- OWASP *Password Storage Cheat Sheet*: <https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html>.
- Course: [M06](../../modules/module-06-cryptography/README.md) · [M07](../../modules/module-07-identity-and-access-management/README.md) · [Lab Safety Policy](../../lab-safety-policy.md) — **§5: credential tools only against course-provided lab data.**
- **Safety:** cracking real credentials, Wi-Fi handshakes, or any data outside this lab's `data/` folder is prohibited. Nothing here touches a network; the demonstration is legal because the data is synthetic and ours.

**Navigation:** · [← Previous: LAB-02](../lab-02-threat-model-risk-register/README.md) · [Lab index](../README.md) · [Next: LAB-04 →](../lab-04-permissions-hardening/README.md)
