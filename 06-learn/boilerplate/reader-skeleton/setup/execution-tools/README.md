---
title: Execution tools (reader skeleton)
chapter: 06
status: template
audience: [novice, seasoned, both]
tags: [setup, execution, skeleton]
---

# Execution tools — reader product

Trimmed mirror of Ch. 00/05 VS Code hub pattern. **Track B default:** VS Code
shell + your filled tooling manifest. Full hub doc and ADR live in the book
harness.

## Tracks (choose one for build phase)

| Track | When | Book path |
| :---- | :--- | :-------- |
| **B — VS Code hub** | IDE subscription, solo POC, harness meta-work | `05-build/execution-tools/vscode-hub.md` |
| **A — OpenHands** | Docker + LiteLLM ready; sandboxed multi-file builds | `05-build/execution-tools/openhands.md` |

## Your checklist

| Step | Action |
| :--: | :----- |
| 1 | Copy `_templates/tooling-manifest.md` from the book (or this skeleton) to your repo |
| 2 | Fill every concern row with your IDE, extensions, and CLI agent names |
| 3 | Mirror one-line adapters into `constraints/project.md` |
| 4 | Open workspace at session **worktree** root — see `setup/README.md` |
| 5 | Run build tasks via `task_context.py` + agent — same contract as the book |
| 6 | Optional: copy `.cursor/hooks.json` + enable Path C — see book `path-c-hook-contract.md` |

## Barbell reminder

| Zone | You own | Book owns |
| :---- | :-------- | :-------- |
| Manifest + adapters | Product names, extension IDs | Concern rows in template |
| Core ritual | Follow it | Session workflow, validators, task files |

When a vendor renames a feature, update **your manifest** — not the book chapters.

## Reference in this book

| Topic | Harness path |
| :---- | :----------- |
| VS Code hub | `05-build/execution-tools/vscode-hub.md` |
| Track B checklist | `05-build/execution-tools/track-b-checklist.md` |
| Tooling manifest template | `_templates/tooling-manifest.md` |
| ADR-010 barbell | `02-design/decisions/ADR-010-vscode-hub-barbell.md` |
| Execution index | `00-start-here/setup/execution-tools/README.md` |
| Path C hooks | `05-build/execution-tools/path-c-hook-contract.md` |
