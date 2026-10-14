---
title: Host profile (reader skeleton)
chapter: 06
status: template
audience: [novice, seasoned, both]
tags: [constraint, host, environment, skeleton]
updated: YYYY-MM-DD
---

# Host profile — reader product

Trimmed mirror of `03-plan/constraints/host.md`. **Copy and fill** before
session work — agents need your OS and shell, not the book author's.

## Host map

| Concern | Your value | Notes |
| :------ | :--------- | :---- |
| **OS family** | | |
| **OS version** | | |
| **Default shell** | | |
| **Copy-paste block language** | | `powershell`, `bash`, … |
| **Path style** | | |
| **Workspace root (typical)** | | |
| **Line endings** | | |
| **Git write shell** | | D-001 instance |
| **Agent terminal sandbox** | | |
| **Python invocation** | | |
| **Package managers** | | |
| **Container host** | | |
| **Locale / clock** | | |
| **Account / auth quirks** | | |

## Git write policy (D-001)

| Field | Your value |
| :---- | :--------- |
| **Human runs** | commit · merge · push |
| **Agent supplies** | blocks in your copy-paste block language |
| **Known failure mode** | |

## Reference in this book

| Topic | Harness path |
| :---- | :----------- |
| Full template | `_templates/host-profile.md` |
| ADR-011 | `02-design/decisions/ADR-011-host-profile-seam.md` |
