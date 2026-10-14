---
title: "Harness example: session close checklist"
chapter: 06
status: reference
tags: [boilerplate, handoff, harness-meta]
---

# Harness session close — checklist pattern

Worked **harness-meta** example: handoff after a spine session. Matches
[[session-workflow]] close order. Use at session close before offering merge.

## When to use

- Every session on the book harness repo
- Human validates work diff **and** handoff docs in one gate (D-001)

## Checklist

| # | Owner | Action | Pass when |
| :-: | :---- | :------- | :-------- |
| A | Agent | Work complete on session branch | Acceptance criteria evidenced |
| B | Agent | Update `STATE.md` — position, threads, last 3 decisions, S(N+1) bootstrap | Bootstrap matches next roadmap row |
| C | Agent | Update `_index/dashboard/01-context.md` L1 | Session + open threads current |
| D | Agent | Update `_index/dashboard/02-containers.md` L2 | Chapter gaps reflect diff |
| E | Agent | Update `_index/dashboard/03-components.md` L3 | Active row → closed; next actions set |
| F | Agent | `validate_md.py --all` | 0 failures |
| G | Human | Review diff + STATE + dashboard | Approve or request edits |
| H | Human | PowerShell commit + merge to `main` | Branch deleted after merge |

## Bootstrap block shape (STATE)

```markdown
**Branch:** `session-NN/<topic>` (create from `main`)
**Primary:** [thread ID] — [one line]
**Load first:** [file list]
**Defer:** [explicit deferrals]
**Human gate:** [what human reviews before merge]
```

## Thread closure rule

Close an open thread in STATE only when the session's primary deliverable
shipped — not when work merely started. Renumber closed threads as C* with
date and one-line note.
