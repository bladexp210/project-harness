---
title: "ADR-011: Host profile — machine and shell seam"
chapter: 2
status: accepted
date: 2026-07-01
tags:
  - decision
  - constraint
  - host
  - execution
---

# ADR-011 — Host profile: machine and shell seam

**Status:** accepted — 2026-07-01, Session 43 (host profile patch).

## Context

[[ADR-010-vscode-hub-barbell|ADR-010]] split book-owned execution core from
reader-owned **tooling-manifest** (product names). Host facts — OS, shell,
path style, copy-paste dialect — were still **implicit**: D-001 read as
"Windows PowerShell only" across `session-workflow`, [[Agents.md|Agents]], and
`project.md`. The next reader on macOS or WSL would get wrong command blocks
and unsafe git guidance.

**tooling-manifest** answers *which IDE/MCP*; it does not answer *how to write
`git commit` fences* or *where git writes must run*.

## Decision

Add a third constraints layer — **host profile** — between global and project:

| Layer | File | Owner | Scope |
| :---- | :--- | :---- | :---- |
| Global | `constraints/global.md` | Book | OS-agnostic discipline |
| **Host** | **`constraints/host.md`** | **Reader** | Machine, shell, block language, D-001 instance |
| Project | `constraints/project.md` | Reader | Identity, track, tool adapters |

Template: `_templates/host-profile.md`. Reader-skeleton ships a skeleton copy.

### D-001 (generalized)

**D-001** is no longer "Windows only." It means:

1. **Git write operations** (commit, merge, push) run on the **host shell**
   named in `constraints/host.md`.
2. Agents **supply** copy-paste blocks in the host's **copy-paste block language**.
3. Agents **do not** run git writes in environments where the host profile
   documents a known failure mode (e.g. sandbox NUL corruption on Windows).

Book chapters reference D-001; **host profile holds the instance**.

### Agent loading

| Task | Load host profile |
| :---- | :---------------- |
| Session open / close | Yes |
| Track B build / meta-work with shell blocks | Yes |
| Pure prose / ADR writing | Usually no |

Add row to [[Agents.md|Agents]] load table. Optional later: `task_context.py`
auto-include for `shell:`-tagged tasks.

**Reversibility & blast radius:** Remove `host.md` and revert D-001 wording —
low risk. Wrong profile → wrong copy-paste only; no runtime wire.

## Why

- Completes the S43 barbell: core / host / tooling / project.
- Keeps `global.md` free of one author's OS.
- Engineering handoff: fork fills host + manifest + project on day one.
- Aligns with IDE `user_info` without making chat metadata canon.

## Alternatives considered (red-teamed)

- **Fold host rows into tooling-manifest** — Rejected: mixes product churn with
  OS/shell facts; different update cadence.
- **Fold host rows into project.md only** — Rejected: file already dense; host
  is a distinct concern (machine vs project identity).
- **Keep implicit Windows in book** — Rejected: teachability and fork safety.

### AI-suggested approach considered and rejected

none.

## Pre-mortem

1. **Profile drifts from real machine** → mitigation: Proceed re-approval;
   change log in host.md; agent compares to IDE `user_info` at session open.
2. **Agents skip loading host.md** → mitigation: Agents load table + session-workflow
   pointer; close gate checks host row if blocks were supplied.
3. **Over-long host file** → mitigation: table + three example blocks max; detail
   in project only when tool-specific.

## Left on the table

- `validate_md.py` lint that host.md is filled (non-empty required rows).
- `task_context.py` automatic host include.
- Per-OS appendix chapters — stay out of scope (barbell).

## Reference

- Living instance: [[host|constraints/host]]
- Template: [[host-profile|_templates/host-profile.md]]
- Prior seam: [[ADR-010-vscode-hub-barbell]]
- Git handoff: [[handoff-and-git]]
