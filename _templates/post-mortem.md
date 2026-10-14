---
title: "Post-mortem: [task or session id]"
chapter: 06
status: draft
date: YYYY-MM-DD
incident_type: failure | near-miss | surprise-success
failure_domain: product | agent-execution | both
rca_technique: "[e.g. trace + 5 Whys, Fishbone + 5 Whys]"
tags: [post-mortem]
task_ref: "[optional — link to tasks/NN-*.md]"
session_ref: "[optional — session NN]"
---

# Post-mortem — [short title]

## Summary

[Two to four sentences: what happened, impact, current state. Past tense.]

## Timeline

| When | Event |
| :---- | :---- |
| | [Agent action, tool call, human decision, or system event] |
| | |

Sources: git log, Track A run log, session dashboard history, agent transcript.

## Root cause

**Failure domain:** product · agent-execution · both

**Technique used:** [e.g. trace analysis + 5 Whys — see [RCA picker](../06-learn/post-mortems/README.md)]

[Primary cause in plain English. Optional numbered **5 Whys** chain if helpful.]

1. Why … → …
2. Why … → …

Focus on systemic causes: spec quality, context load design, review gate gaps —
not individual blame.

## What we learned

[Bullet list of durable lessons an future agent or human can act on.]

-

## Action items

| Item | Owner | Target | Status |
| :---- | :---- | :---- | :---- |
| | human / agent | file or date | todo |

Untracked items do not close this post-mortem. Carry into [PROJECT-PLAN](../03-plan/PROJECT-PLAN.md),
[constraints](../03-plan/constraints/global.md), `context/`, [DEBT-LEDGER](../06-learn/DEBT-LEDGER.md), or [boilerplate/](../06-learn/boilerplate/README.md).

## Artifacts updated

[List paths changed as a result of this post-mortem. Write "none" if analysis only.]

-

## Acceptance evidence (if task-related)

[Paste or quote each relevant Gherkin `Then`/`And` with pointer to proof —
commit hash, test output, or file path. Required when closing a failed task
per [ADR-002](../02-design/decisions/ADR-002-modeling-conventions.md).]

```gherkin
Scenario:
  Then ...
```

Evidence:
