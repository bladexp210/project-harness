---
title: Host profile — fictional example
chapter: 03
status: template
audience: [novice, seasoned, both]
tags: [constraint, host, example]
---

# Host profile — fictional example

This is a **made-up** Windows laptop. It matches the book's D-001 note (git writes happen in the host shell, not in a sandbox) without recording a real machine. Copy it to `host.md` locally and replace every row. Do not commit a real OS build, home folder, VPN, or account list.

## Host map

| Concern | Value | Notes |
| :--- | :--- | :--- |
| **OS family** | Windows | Fictional |
| **OS version** | Windows 11 | No real build number |
| **Default shell** | PowerShell | |
| **Copy-paste block language** | `powershell` | Agent-supplied command fences |
| **Path style** | Windows | `C:\Users\you\...` placeholders only |
| **Workspace root (typical)** | `C:\Users\you\src\project-harness` | Example path |
| **Line endings** | CRLF or LF via git | |
| **Git write shell** | PowerShell on the host | Human runs git writes |
| **Python invocation** | `python` | |
| **Package managers** | winget, pip | As needed per task |
| **Container host** | Docker Desktop | |
| **Locale / clock** | UTC | |
| **Account / auth quirks** | One example GitHub user `YOUR_USER` | |

## Git write policy

| Field | Value |
| :--- | :--- |
| **Human runs** | `git add`, `git commit`, `git merge`, `git push` |
| **Agent supplies** | PowerShell blocks for the human to copy |
| **Agent must not** | Commit, merge, or push unless the human asks |
