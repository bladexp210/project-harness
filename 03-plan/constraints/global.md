---
title: Global Constraints
chapter: 03
status: in-progress
audience: [novice, seasoned, both]
tags: [constraint]
---

# Global constraints

> [!TEACH] Teach
> Pre-filled guardrails. You inherit these; you do not write them. Project-specific
> rules go in [[project|constraints/project]] instead. Every constraint here exists
> because skipping it has a documented failure mode.

## Repository discipline

- Atomic commits — one logical change per commit, revertible in isolation.
- Conventional Commits format, enforced at commit-msg stage.
- No secrets in the repo, ever — gitleaks runs on every commit.
- Every markdown file carries valid YAML frontmatter — `validate_md.py` runs on every commit.

## Scope discipline

- Agents modify only files listed under "Scope — modify" in their TASK.md.
- A task-level decision that would touch a Layer 1 or Layer 2 context file is no
  longer task-level — escalate before proceeding.

## Budgets (split / renegotiate triggers)

> [!TEACH] Teach
> Budgets make drift visible before it becomes architecture. Hitting a trigger
> means: split, or renegotiate with explicit human approval plus a
> [[DEBT-LEDGER]] entry. Never silently exceed.

| Artifact | Budget | Trigger action |
|----------|--------|----------------|
| Source module | ≤ 300 lines | Decompose at natural seam |
| Layer 1 context file | ≤ 200 lines | Move detail to Layer 2 |
| TASK.md | ≤ 100 lines | Task too big — decompose the task, not the file |
| Agent definition (yaml) | ≤ 60 lines | Role doing too much — fork a specialist |

> [!TEACH] Teach
> These budgets are machine-enforced. `validate_md.py` checks each file against
> its budget (path→budget map declared at the top of the script) and the
> ≤ 20-node Mermaid limit from ADR-002, applying a **grace band**: a file over
> budget by ≤ 5% is a **warning** (drift is visible, commit still passes); over by
> > 5% is a **failure** (the commit is blocked until you split or renegotiate).
> Renegotiating still requires explicit human approval plus a [[DEBT-LEDGER]]
> entry — the grace band buys a margin, not an exemption.

## AI execution discipline

Generated output is untrusted input entering a controlled system. Hard rules:

- No AI-generated change reaches a protected branch directly — review path
  always, no exceptions for "trivial" changes.
- No secrets, customer data, or regulated records in prompts or context
  files — what enters a prompt leaves your control.
- No new dependency without provenance, license, and policy review.
- No schema change without migration notes and a tested rollback path.
- No user-visible behavior change without acceptance criteria and release
  notes.
- Critical-path logic requires human review *plus* automated verification —
  neither substitutes for the other.

## Decision discipline

- Significant decisions produce an ADR (`02-design/decisions/ADR-NNN.md`); the
  red-team agent challenges before the decision is final.
- Pruned branches in PROJECT-PLAN.md cite their ADR — `[PRUNED: reason]`.
- Known compromises are logged in [[DEBT-LEDGER]] with a trigger, at the moment
  they are taken — not when they hurt.
