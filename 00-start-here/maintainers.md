---
title: For book maintainers
chapter: 00
status: reference
audience: [seasoned]
tags: [orientation, harness, session-workflow]
updated: 2026-07-03
---

# For book maintainers

**Purpose:** Operational map for people who **author or maintain this harness
repo** — not for first-time readers. New adopters start at
[[getting-started|Getting started]].

---

## Session workflow

| Step | Rule |
| :--: | :--- |
| Open | **Plan → Proceed → Execute** — agent plans; human says proceed before edits |
| Branch | `session-NN/<topic>` per task or session |
| Git writes | Human runs git on host shell (D-001) — see [[host\|constraints/host]] |
| Close | Update [[STATE]], dashboard L1–L3, bootstrap next session |

Full procedure: [[context/system/session-workflow|session-workflow]].
Agent rules: [[Agents.md]].

---

## Harness meta artifacts

| Artifact | Path | Role |
| :------- | :--- | :--- |
| Session truth | `STATE.md` | Current session, bootstrap, open threads |
| Visual status | `_index/dashboard/` | L1 Context · L2 Containers · L3 Components |
| System context | `context/system/` | Workflow, notation, agent-team |
| Diagrams | `viz/` | C4, BPMN, UML, DMN, ICOM+ harness examples |
| Validator | `scripts/validate_md.py` | Markdown structure, budgets, wiki-link rules |
| Templates | `_templates/` | New task, ADR, post-mortem, runbook |

---

## Tooling commands

| Step | Command |
| :---- | :------ |
| Validate all markdown | `python scripts/validate_md.py --all` |
| Assemble task context | `python scripts/task_context.py <path-to-task.md>` |
| Golden-task regression | `python scripts/test_golden_tasks.py` |

Pre-commit hooks run the validator on commit when installed.

---

## Execution tracks (this repo)

| Track | Use | Entry |
| :---- | :-- | :---- |
| **Track B** | Authoring canon, session meta-work (default) | [[Agents.md]], [[05-build/execution-tools/track-b-checklist\|track-b-checklist]] |
| **Track A** | Build tasks via OpenHands + LiteLLM | [[05-build/execution-tools/track-a-setup\|track-a-setup]] |

Decision: [[02-design/decisions/ADR-007-dual-execution-tracks|ADR-007]].

---

## Not canon

| Path | Rule |
| :--- | :--- |
| `_inbox/` | Intake — promote into chapter paths before treating as canon |
| `_playground/` | Experiments — not loaded into agent context unless named |
| `outputs/` | Generated or scratch — not source of truth |
| `.history/` | Local editor history — ignore |

Known compromises: [[06-learn/DEBT-LEDGER|DEBT-LEDGER]].

---

## Publish a reader site later

GitHub does not render `[[wiki-links]]`. This public copy does not ship a
live site, deploy token, or sync script. See
[[../07-ship-operate/publish/README|Publish later]] when you want a static site.
