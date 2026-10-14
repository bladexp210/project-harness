---
title: Cursor
chapter: 00
status: stub
audience: [novice, seasoned, both]
tags: [setup, design, cursor]
---

# Cursor — alternative design tool (stub)

Cursor is an **IDE-integrated** agent environment. Use it as your design-phase
tool if you already live in an editor daily and want design work (Ch. 01–04)
in the same window as code review.

> [!NOTE] Stub
> Full Cursor setup scaffold is deferred. This page records the **key
> differentiator** vs. the primary tool ([cowork](cowork.md)) so you can choose
> honestly.

## Key differentiator vs. Cowork

| Aspect | Cursor | [Cowork](cowork.md) (primary) |
| :----- | :----- | :------------------------- |
| Surface | IDE (VS Code fork) | Desktop agent app |
| Best when | You want design + code in one editor | You want folder-first / Obsidian-first design |
| Project memory | Rules, `.cursorrules`, @-mentions | Cowork project folders + memory |

## Where to go next

- **Primary path:** [cowork](cowork.md)
- **Design tools index:** [README](README.md)
- **Track B execution (if Cursor is also your build tool):** [track-b-checklist](../../../05-build/execution-tools/track-b-checklist.md)

## Connector stub (fictional)

This public book does not wire agents to a private wiki, ticket system, or employer source of truth. When you connect a tool, use a stub like this and replace the values yourself:

| Field | Example value |
| :--- | :--- |
| Source name | `acme-policy-docs` |
| Base URL | `https://docs.example.internal` |
| Auth | Local secret named `YOUR_DOCS_TOKEN` — never commit the value |
| Allowed reads | `/policies/pto.md` only |
| Procedure | Cite the clause. If the source and the question disagree, stop and ask a human. |
