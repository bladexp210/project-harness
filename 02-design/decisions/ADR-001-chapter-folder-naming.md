---
title: "ADR-001: Chapter folder naming"
chapter: 02
status: accepted
date: 2026-06-10
tags: [decision]
---

# ADR-001 — Chapter folder naming

**Status:** accepted — 2026-06-10, by commit.

## Context

Chapters are folders; every internal reference is a wiki-link. Folder renames
break links across the whole vault, so the naming scheme must be decided once,
before more chapters materialize. Two folders already exist (`03-plan/`,
`06-learn/`) and forced the question.

## Decision

Kebab-case, zero-padded number plus short title, derived from the chapter
titles in [Agents](../../Agents.md):

```
00-start-here/   01-understand/   02-design/   03-plan/
04-your-agents/  05-build/        06-learn/
```

`07-ship-operate/` and `08-sunset/` are reserved for the planned product-lifecycle
extension.

## Why

[agent-team](../../context/system/agent-team.md) already referred to "the 04-your-agents chapter" — the scheme
existed implicitly; this ADR makes it official. Numbers preserve reading order
in every file browser. Kebab-case survives git, URLs, CLIs, and Quartz
publishing without escaping. Short titles keep the graph view legible.

## Alternatives considered (red-teamed)

- **Bare numbers** (`00/`, `01/`) — opaque in graph view and link autocomplete;
  rejected.
- **Full titles with spaces/em-dashes** (`00 — Start Here/`) — encoding pain in
  git, terminals, and URLs; rejected.
- **No numbers** (`start-here/`) — loses reading order, the book's spine;
  rejected.

## Pre-mortem

*If this decision fails a year from now, why?* (1) A chapter title changed and
the folder was renamed, silently breaking links → mitigation: chapter titles
are frozen in [Agents](../../Agents.md); any rename requires a superseding ADR plus a
vault-wide link audit. (2) The book outgrew 9 chapters → zero-padding holds to
99; no action needed. (3) A publishing tool dislikes leading digits → Quartz
handles them today; if a future tool does not, slugs can be remapped at the
publish layer without touching the vault.

## Left on the table

Johnny Decimal numbering (`10-19 understand…`) — more room for insertion, but
overkill for a fixed spine of ~9 chapters.
