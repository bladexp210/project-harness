---
title: Host profile
chapter: 03
status: template
audience: [novice, seasoned, both]
tags: [constraint, host, environment, shell]
updated: YYYY-MM-DD
---

# Host profile — reader machine

**Barbell seam (reader-owned).** The book owns OS-agnostic rules in
[[global|constraints/global]]. **You** own this file: the machine, shell, and
copy-paste dialect agents must use when talking to **your** environment.

> [!LEARN] Learn It
> `tooling-manifest.md` names **which products** (Cursor, Docker, MCP).
> **Host profile** names **how commands are written** (PowerShell vs bash,
> path style, where git writes run). Without it, agents assume the author's
> machine — wrong blocks, wrong paths, corrupted `.git`.

> [!TIP] Fast Track
> Copy to `03-plan/constraints/host.md`. Fill every row. Agents load host
> before supplying shell blocks or session git steps. Re-approve at **Proceed**
> when you change laptop, OS, shell, or WSL vs native.

## How to use

| Step | Action |
| :--: | :----- |
| 1 | Fill the table below — verify against your actual terminal (`$PSVersionTable`, `uname -a`, etc.) |
| 2 | Set **copy-paste block language** — agents fence commands in that language only |
| 3 | Document **git write policy** — which shell runs commit/merge (D-001) |
| 4 | Link from [[project|constraints/project]] — host before project identity |
| 5 | Add to agent `context_load` for session work and shell-heavy tasks |

IDE-injected OS hints (Cursor `user_info`) **confirm** this file; they do not
replace it.

## Host map

| Concern (book-stable) | Your value | Notes |
| :-------------------- | :--------- | :---- |
| **OS family** | | e.g. Windows, macOS, Linux |
| **OS version** | | Build or kernel — matters for path/sandbox quirks |
| **Default shell** | | e.g. PowerShell 7, bash, zsh |
| **Copy-paste block language** | | `powershell`, `bash`, `sh`, `zsh` — for fenced commands |
| **Path style** | | Windows `C:\...` vs POSIX `/home/...` |
| **Workspace root (typical)** | | Where the repo clone lives |
| **Line endings** | | CRLF vs LF — affects git and editors |
| **Git write shell** | | Where human runs commit/merge/push (D-001) |
| **Agent terminal sandbox** | | Can agent run git write? If no, say why |
| **Python invocation** | | e.g. `python` vs `python3` |
| **Package managers** | | winget, brew, apt, npm global policy |
| **Container host** | | Docker Desktop; bridge hostname for compose |
| **Locale / clock** | | Local timezone for STATE timestamps |
| **Account / auth quirks** | | Multi GitHub accounts, `gh` profiles, SSH agent |

## Git write policy (D-001)

| Field | Your value |
| :---- | :--------- |
| **Human runs** | commit · merge · push |
| **Agent supplies** | copy-paste blocks in **copy-paste block language** only |
| **Agent must not** | run git write in sandbox when policy says host-only |
| **Known failure mode** | e.g. NUL-corrupted `.git` from sandbox git on Windows |

## Example blocks (your dialect)

Agents mirror this style — not the book author's.

**Git (one line):**

```text
(paste one representative git commit one-liner in your shell dialect)
```

**Git (multi-line):**

```text
(paste a representative multi-line add/commit block)
```

**Validator:**

```text
(paste how you run validate_md.py)
```

## Change log

| When | Change | Approved |
| :---- | :----- | :------- |
| YYYY-MM-DD | Initial fill from `_templates/host-profile.md` | |

## Reference (book harness)

| Topic | Path |
| :---- | :--- |
| Global constraints | [[global|constraints/global]] |
| Project identity + tools | [[project|constraints/project]] |
| Tooling manifest | [[tooling-manifest|_templates/tooling-manifest.md]] |
| D-001 / git handoff | [[handoff-and-git]] |
| Host profile ADR | [[ADR-011-host-profile-seam]] |
