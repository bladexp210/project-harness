---
title: Tooling manifest
chapter: 00
status: template
audience: [novice, seasoned, both]
tags: [setup, execution, track-b, tooling]
updated: YYYY-MM-DD
---

# Tooling manifest — reader product

**Barbell seam (reader-owned).** The book owns the harness core — session
workflow, task files, validators, `task_context.py`, hook contract. **You** own
this file: map stable **concerns** to the product names you run today.

> [!LEARN] Learn It
> Vendor features rename often. When Cursor renames "Rules" or VS Code ships a
> new extension API, update **this manifest** — not the book chapters. The book
> stops at concerns; you fill product columns.

> [!TIP] Fast Track
> Copy this file to your repo root or `setup/`. Fill the **Your product** column
> for each row. Link adapter lines in [[project|constraints/project]] § Tool
> adapters. Re-read when you change IDE, CLI agent, or MCP stack.

## How to use

| Step | Action |
| :--: | :----- |
| 1 | Pick your **shell** — typically VS Code or a VS Code–compatible IDE |
| 2 | Fill every row below with your current product + where to configure it |
| 3 | Mirror one-line adapters into `constraints/project.md` (checklist §7) |
| 4 | Re-approve at session **Proceed** when you swap a major tool |
| 5 | Keep extension IDs accurate — stale names fail silently |

**Research duty:** When an agent fills product names, it must verify against
**current** vendor docs. You approve the filled manifest before build sessions.

## Concern map

| Concern (book-stable) | Your product | Configure at | Notes |
| :-------------------- | :----------- | :----------- | :---- |
| **IDE shell** | | | Workspace root = session worktree |
| **Persistent rules** | | | e.g. `AGENTS.md`, `.cursor/rules/`, Copilot instructions |
| **Scoped files** | | | @-mentions, file picks, codebase search |
| **Stripped context** | | | Output of `task_context.py` — paste or attach |
| **Diff review** | | | Source control panel, inline diff |
| **Model choice** | | | Subscription tier, API key, LiteLLM alias |
| **Linters / formatters** | | | ESLint, Ruff, Prettier — extension or CLI |
| **Git integration** | | | Built-in SCM; confirm D-001 if sandboxed terminal |
| **MCP servers** | | | Obsidian, browser, issue tracker — list enabled |
| **CLI agent (terminal)** | | | Claude Code, Codex, OpenCode — integrated terminal |
| **Automation hooks** | | | Pre/post tool, session start/end — Path C (S44+) |
| **Observability export** | | | Langfuse bridge when wired; fail open if down |

## CLI agents in integrated terminal

Track B often pairs a **VS Code shell** with a **CLI agent** in the integrated
terminal. Same harness contract; different surface.

| Pattern | When | Example |
| :------ | :--- | :------ |
| IDE chat agent | Single sitting, diff in SCM panel | Cursor Composer, Copilot Chat |
| CLI in terminal | Scriptable, headless-friendly | Claude Code, Codex CLI |
| Both | Design in chat; batch ops in terminal | Document both rows above |

## Extension inventory (optional)

List extensions you require on a fresh machine. Update when the vendor renames.

| Extension / package | Purpose | Required |
| :------------------ | :------ | :------- |
| | Git, lint, MCP host, … | yes / optional |

## Change log

| When | Change | Approved |
| :---- | :----- | :------- |
| YYYY-MM-DD | Initial fill from `_templates/tooling-manifest.md` | |

## Reference (book harness)

| Topic | Path |
| :---- | :--- |
| VS Code hub pattern | [[vscode-hub]] |
| Track B checklist | [[track-b-checklist]] |
| Execution track decision | [[ADR-007-dual-execution-tracks]] |
| Hub barbell ADR | [[ADR-010-vscode-hub-barbell]] |
| Host profile ADR | [[ADR-011-host-profile-seam]] |
| Host profile (this harness) | [[host\|constraints/host]] |
| This harness instance | [[project|constraints/project]] |
