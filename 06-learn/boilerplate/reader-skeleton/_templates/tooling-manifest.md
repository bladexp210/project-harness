---
title: Tooling manifest (reader skeleton)
chapter: 06
status: template
audience: [novice, seasoned, both]
tags: [setup, execution, track-b, tooling, skeleton]
updated: YYYY-MM-DD
---

# Tooling manifest — reader product

**Copy of the book template.** Canonical version:
`_templates/tooling-manifest.md` in the harness repo. Keep this file in sync when
the book updates concern rows.

> [!TIP] Fast Track
> Fill the **Your product** column below. Link adapters in your product's
> `constraints/project.md`. See `setup/execution-tools/README.md`.

## Concern map

| Concern (book-stable) | Your product | Configure at | Notes |
| :-------------------- | :----------- | :----------- | :---- |
| **IDE shell** | | | Workspace root = session worktree |
| **Persistent rules** | | | |
| **Scoped files** | | | |
| **Stripped context** | | | `task_context.py` output |
| **Diff review** | | | |
| **Model choice** | | | |
| **Linters / formatters** | | | |
| **Git integration** | | | D-001: git on Windows if sandboxed |
| **MCP servers** | | | |
| **CLI agent (terminal)** | | | |
| **Automation hooks** | | | Path C when wired |
| **Observability export** | | | Langfuse bridge; fail open |

## Change log

| When | Change | Approved |
| :---- | :----- | :------- |
| YYYY-MM-DD | Initial fill | |

## Reference in this book

| Topic | Harness path |
| :---- | :----------- |
| Full template + guidance | `_templates/tooling-manifest.md` |
| VS Code hub | `05-build/execution-tools/vscode-hub.md` |
