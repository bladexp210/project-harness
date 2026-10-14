---
title: Review gates — HTML review surfaces
chapter: meta
status: living
updated: 2026-07-02 23:50
tags: [review, html-gate, human-in-the-loop]
---

# Review gates

Single-file **HTML review surfaces** for human–agent gates. Not canon — Markdown
in `context/system/sessions/` and [[STATE]] stay the source of truth.

## Pattern (S40.5 → S41 pilot)

| Layer | Role |
| :---- | :--- |
| **HTML** (`_views/gates/*.html`) | Browser UI — drag, sort, comment, scan |
| **Markdown export** | Agent-readable `## Human decisions` block |
| **Session artifact** | Committed table + pasted export |

Legacy path `review/*.html` redirects to `_views/gates/` where applicable.

## Workflow

1. Agent drafts the triage table in the session artifact.
2. You open the matching HTML file in a browser (refresh after agent edits).
3. Adjust in the UI → **Copy as markdown**.
4. Paste into `## Human decisions` in the session artifact (or say **proceed** with the export in chat).
5. Merge only when Markdown table + export + STATE agree.

## Files

| File | Gate | Session artifact |
| :--- | :--- | :--------------- |
| `_views/gates/proceed.html` | Session plan scope (Proceed) | Session open / plan chat |
| `_views/gates/validate.html` | Work diff + handoff docs (Validate) | Session close artifact |
| `_views/gates/merge.html` | Merge approval (validator + git D-001) | Session close artifact |
| `_views/gates/inbox-triage.html` | `_inbox/` promote / strip / archive / defer | [[session-41-inbox-triage]] |
| `review/inbox-triage-board.html` | Legacy redirect → `_views/gates/inbox-triage.html` | — |

## Rules

- HTML is **git-tracked** and portable (not vendor-locked Canvas).
- Do not promote HTML into chapter paths without an ADR or session decision.
- Export schema: table under `## Human decisions` with `<!-- exported-from -->` comments.
