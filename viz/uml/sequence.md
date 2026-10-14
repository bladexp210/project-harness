---
title: UML Sequence — harness examples
status: reference
audience: [novice, seasoned, both]
tags: [viz, uml, dynamic, L3, L4, harness]
---

# UML Sequence — harness examples

**Question answered:** In what order do actors and systems exchange messages
during a harness scenario?

> [!NOTE] REAL — harness-meta
> Two worked examples — **different questions**, same file. **Variant A** =
> session close handoff (Track B). **Variant B** = Task 02 message trace on Track A.
> Mermaid `sequenceDiagram` syntax (UML sequence subset).

> [!TIP] When to use which
> Use **Variant A** for session Plan → Validate message order. Use **Variant B**
> for OpenHands + LiteLLM + repo edits during Task 02.

---

## Variant A — session workflow handoff

**Question answered:** Who messages whom during session close validation?

```mermaid
sequenceDiagram
    autonumber
    actor Reader
    participant Agent
    participant STATE as STATE + dashboard
    participant Scripts as validate_md.py

    Reader->>Agent: start session N
    Agent->>Reader: session plan
    Reader->>Agent: proceed
    Agent->>STATE: boot line + L3 row
    Agent->>Agent: build on branch
    Agent->>STATE: close draft
    Agent->>Scripts: validate_md --all
    Scripts-->>Agent: pass / fail
    Agent->>Reader: merge offer + git blocks
    Reader->>Reader: commit + merge D-001
```

**Legend**

| Symbol | Role |
| :----- | :---- |
| `actor` | Human outside the system |
| `participant` | Logical system or script |
| `autonumber` | Ordered messages for this scenario |
| Solid arrow | Request; dashed = return |

### Field guide — Variant A

| Message | Meaning |
| :------ | :------ |
| Session plan | Plan phase — no edits yet |
| Proceed | Human gate unlocks Execute |
| Close draft | Handoff trio before merge offer |
| validate_md | Evidence gate — zero failures |
| D-001 | Git on Windows host only |

### ESL checklist — Variant A

| Rule | Pass |
| :---- | :---- |
| Title = question | Session close message order |
| Labels ≤ 5 words | Yes |
| Embedded legend | Above |
| L3/L4 boundary | Session ops (Track B) |

---

## Variant B — Task 02 Track A trace

**Question answered:** What messages flow when OpenHands runs Task 02?

```mermaid
sequenceDiagram
    autonumber
    actor Reader
    participant OH as OpenHands
    participant LLM as LiteLLM
    participant OR as OpenRouter
    participant Repo as Harness repo

    Reader->>OH: start task 02
    OH->>LLM: chat completion
    LLM->>OR: route model alias
    OR-->>LLM: model response
    LLM-->>OH: proxied response
    OH->>Repo: edit scope files only
    OH-->>Reader: diff for review
    Reader->>Repo: commit after approve
```

**Legend**

| Symbol | Role |
| :----- | :---- |
| OpenHands | Track A executor container |
| LiteLLM | Proxy — never bypass |
| OpenRouter | External LLM routing |
| Repo | Scope — modify files only |

### Field guide — Variant B

| Message | Meaning |
| :------ | :------ |
| LiteLLM health | Prerequisite before step 1 (see [[task-box]]) |
| Scope files only | `openhands.md` log + `project.md` Models |
| Diff for review | Human gate — no agent commit |
| Virtual key | OpenHands uses LiteLLM virtual key |

### ESL checklist — Variant B

| Rule | Pass |
| :---- | :---- |
| Title = question | Task 02 message trace |
| Labels ≤ 5 words | Yes |
| Embedded legend | Above |
| Pairs with ICOM | [[../icom/task-box]] |

---

## Pairing

| Also draw when | Diagram |
| :------------- | :------ |
| C4 runtime on boxes | [[../c4/dynamic]] |
| Gateway branching | [[../bpmn/process-subset]] |
| State machines | [[state]] |
| Deployment nodes | [[../c4/deployment]] |

## Where to go next

- **UML section index:** [[README]]
- **C4 Dynamic alternative:** [[../c4/dynamic]]
- **Track A setup:** [[track-a-setup]]
