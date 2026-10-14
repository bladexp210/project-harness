---
title: Post-mortems
chapter: 06
status: living
tags: [post-mortem, learning-loop]
---

# Post-mortems

One filled post-mortem per significant failure, surprise, or near-miss after a
build cycle. Blameless: analyze the **system** (spec quality, context load,
review gates) — not the model or the human in isolation.

## How to file

1. Copy `_templates/post-mortem.md` to this folder:
   `POSTMORTEM-YYYY-MM-DD-<task-or-session-id>.md`
2. Fill every section before the next task on the same scope starts.
3. Carry **Action items** into PROJECT-PLAN, constraints, context files, or
   [[DEBT-LEDGER]] — untracked action items do not reduce recurrence.
4. Promote reusable fixes to [[06-learn/boilerplate/README|boilerplate/]].

## When to write

| Trigger | Example |
| :---- | :---- |
| Task acceptance failed twice | Agent missed scope boundary |
| Human caught regression post-merge | Review gate too thin |
| Unexpected cost or latency | Wrong model axis for complexity |
| Near-miss (caught pre-merge) | Log anyway — cheaper than a repeat |

## Worked harness example

See [[example-harness-doc-only-gap]] — fictional S22-style gap analysis showing
how to quote Gherkin evidence and file constraint updates.

## RCA technique picker

Distilled from inbox RCA research (archived `research/archive/`). Two failure
domains stay separate — conflating them is the primary error in new AI-assisted
teams:

| Domain | What failed | Evidence type | Default technique | When NOT to apply |
| :---- | :---- | :---- | :---- | :---- |
| **Product** | Software you are building (bug, regression, design defect) | Tests, git diff, user report | Fishbone → 5 Whys | Agent-only tooling misconfig with no product impact |
| **Agent execution** | AI agent during a bounded task (hallucination, tool misuse, context overflow) | Execution trace, Langfuse Path C, session log | Trace analysis → 5 Whys | Human-only process failure with no agent run |

**Agent Fishbone categories** (replace manufacturing 4M1E): Model · Context ·
Tool · Process · Environment · Human review gate.

### Pick by severity and recurrence

| Severity | Single occurrence | Recurring | When NOT to apply |
| :---- | :---- | :---- | :---- |
| **Low** (wrong output, no commit) | 5 Whys | Fishbone + 5 Whys | Trivial typo with obvious one-line fix |
| **Medium** (committed, caught in CI) | Timeline + 5 Whys | 8D | First-time environmental flake |
| **High** (merged, deployed, or client-facing) | FTA + Apollo | Apollo + bow-tie + 8D | Known accepted risk with signed waiver |

**First-occurrence rule:** start at L4 (single task trace); escalate to L1
(cross-session Apollo/PROACT) only when 5 Whys reaches "policy gap" without an
actionable fix. **Recurring rule:** start at L1 before per-task traces.

### Allowed combinations

| Primary | Secondary | Pattern | When NOT to apply |
| :---- | :---- | :---- | :---- |
| Fishbone | 5 Whys | Breadth first, depth on top 2–3 branches | Single obvious linear cause |
| Trace analysis | 5 Whys | Trace localizes step; 5 Whys finds systemic gap | No execution log or trace exists |
| Timeline | Change analysis | Parallel — *when* vs *what changed* (git + logs) | Failure predates version control |
| FMEA | Gherkin | High-RPN rows become acceptance criteria | One-off script, not a task type |
| Blameless postmortem | Any RCA | Postmortem *contains* RCA — not a substitute | — |

**Track B trace primitive:** reconstruct agent steps from `logs/sessions/`,
Langfuse Path C, and git timestamps before choosing a deeper technique. See
[[path-c-hook-contract]] and [[harness-session-close-checklist]].

Provenance: `research/archive/Root Cause Analysis Techniques for AI-Assisted Software Development.md`.
