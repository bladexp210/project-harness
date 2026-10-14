---
title: DMN Decision table — harness examples
status: reference
audience: [novice, seasoned, both]
tags: [viz, dmn, decision, L3, L4, harness]
---

# DMN Decision table — harness examples

**Question answered:** Given inputs at a gateway, which outcome path applies?

> [!NOTE] REAL — harness-meta
> Two worked examples — **different questions**, same file. **Variant A** =
> Proceed gate at session open. **Variant B** = Track A vs Track B for Task 02.
> Markdown tables stand in for DMN notation (tool-agnostic).

> [!TIP] When to use which
> Use **Variant A** at the Plan → Execute gateway. Use **Variant B** at Task 02
> mechanism selection (see [task-box](../icom/task-box.md) Controls).

---

## Variant A — Proceed gate (session open)

**Question answered:** When may the agent leave Plan and bootstrap the branch?

| Input: human signal | Input: scope clear | Input: defer list OK | Outcome |
| :------------------ | :----------------- | :------------------- | :------ |
| `proceed` | yes | yes | **Execute** — create branch, boot STATE |
| `proceed` | yes | no | **Revise plan** — agent adjusts defer list |
| `proceed` | no | — | **Clarify** — answer open questions first |
| scope change | — | — | **Re-plan** — new session plan shape |
| silence / wait | — | — | **Stay in Plan** — no branch or edits |

**Legend**

| Column | Role |
| :----- | :---- |
| Input columns | Facts at gateway evaluation time |
| Outcome | Single selected path (XOR) |
| `—` | Don't care for that row |

### Field guide — Variant A

| Outcome | Next artifact |
| :------ | :------------ |
| Execute | Boot line + `_index/dashboard/03-components.md` |
| Revise plan | Updated chat plan; still no branch |
| Clarify | Human answers Q1–Qn from session plan |
| Re-plan | New defer/primary lists |
| Stay in Plan | Agent waits — per [session-workflow](../../context/system/session-workflow.md) |

### ESL checklist — Variant A

| Rule | Pass |
| :---- | :---- |
| Title = question | When to leave Plan |
| Labels ≤ 5 words | Yes |
| Embedded legend | Above |
| Pairs with BPMN A | [process-subset](../bpmn/process-subset.md) Variant A |

---

## Variant B — Track A vs Track B (Task 02)

**Question answered:** Which execution track should Task 02 use?

| Input: Docker available | Input: API keys configured | Input: LiteLLM health | Outcome |
| :---------------------- | :------------------------- | :-------------------- | :------ |
| yes | yes | 200 | **Track A** — OpenHands golden path |
| yes | yes | fail | **Block** — fix stack; log blocker |
| yes | no | — | **Block** — configure keys; no secrets in git |
| no | — | — | **Track B** — document blocker per task 02 |
| partial | — | — | **Block** — evidence required before fallback |

**Legend**

| Column | Role |
| :----- | :---- |
| Docker available | Compose can start on documented host |
| API keys configured | `.env` per [track-a-setup](../../05-build/execution-tools/track-a-setup.md) — not committed |
| LiteLLM health | HTTP 200 before OpenHands |
| Outcome | Track selection or blocked state |

### Field guide — Variant B

| Outcome | Canon reference |
| :------ | :-------------- |
| Track A | Task 02 Mechanisms table — ideal path |
| Track B | [track-b-checklist](../../05-build/execution-tools/track-b-checklist.md) — fallback only with blocker note |
| Block | Second Gherkin scenario in task 02 |

### ESL checklist — Variant B

| Rule | Pass |
| :---- | :---- |
| Title = question | Track A or B for task 02 |
| Labels ≤ 5 words | Yes |
| Embedded legend | Above |
| Pairs with ICOM | [task-box](../icom/task-box.md) |

---

## Pairing

| Also draw when | Diagram |
| :------------- | :------ |
| Process flow around gateway | [process-subset](../bpmn/process-subset.md) |
| State after decision | [state](../uml/state.md) |
| ICOM Controls column | [task-box](../icom/task-box.md) |
| Irreversible gate Hoare fields | [icom-plus-irreversible-gates](../../context/system/icom-plus-irreversible-gates.md) |

## Where to go next

- **DMN section index:** [README](README.md)
- **Task 02 acceptance:** `04-your-agents/tasks/02-track-a-golden-path.md`
- **ADR dual tracks:** [ADR-007-dual-execution-tracks](../../02-design/decisions/ADR-007-dual-execution-tracks.md)
