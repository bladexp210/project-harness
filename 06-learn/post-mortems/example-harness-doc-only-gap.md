---
title: "Example: document-only task scope drift"
chapter: 06
status: reference
tags: [post-mortem, example, harness-meta]
date: 2026-06-23
incident_type: near-miss
---

# Post-mortem — example (harness-meta, fictional)

> **Training artifact only** — illustrates `_templates/post-mortem.md` filled
> for a document-only harness task. Not a real incident.

## Summary

Agent expanded task 03 scope to edit `scripts/context_loader.py` during a
document-only session; human caught diff before commit.

## Timeline

| When | Event |
| :---- | :---- |
| T+0 | Task 03 opened — scope lists `context/**/*.md` only |
| T+15m | Agent proposes loader refactor "to match new tree" |
| T+20m | Human review — scope violation flagged |
| T+25m | Agent reverted loader edits; doc-only diff retained |

## Root cause

Task file did not explicitly state **Mechanisms → Not run** for both tracks;
agent defaulted to "fix code when docs mention code."

## What we learned

Explicit Track A/B **Not run** rows (see [[harness-task-spec-example]]) prevent
scope creep in canon sessions.

## Action items

| Item | Owner | Status |
| :---- | :---- | :---- |
| Add Track table to task 03 template example | harness | done (S23) |
| Quote scope list in post-mortem when near-miss | human | ongoing |

## Artifacts updated

- `06-learn/boilerplate/specs/harness-task-spec-example.md` — Track table row
- No [[DEBT-LEDGER]] entry — caught pre-commit

## Gherkin evidence (would-have-failed)

```
Then validate_md.py --all reports 0 failures
And test_context_loader.py passes
```

Loader change was out of scope; keeping it would have invalidated the
document-only closure story.
