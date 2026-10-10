---
title: "Dataset — LAB-13 Log Analysis"
layout: default
---

# Dataset — LAB-13 Log Analysis

**Part of:** [LAB-13 — Log Analysis, Authentication Anomalies, and Alert Triage](../README.md)

This folder holds the lab's **synthetic** log files (fictional organisation, generated data — no real people or systems). On GitHub, use the folder's file list to download individual files.

| File | What it is |
|---|---|
| `auth.log` | System authentication log (logins, sudo, failures) |
| `auth-attempts.csv` | Flattened authentication attempts for scripted analysis |
| `admin-actions.jsonl` | Privileged/admin action events (one JSON object per line) |

**Analysis tools:** `grep`, `awk`, `jq`, Python stdlib — see the [Tools Directory](../../../reference/tools.md).
**Safety:** synthetic data only; nothing here targets a live system. Back to the [lab README](../README.md) · [Lab collection](../../README.md).
