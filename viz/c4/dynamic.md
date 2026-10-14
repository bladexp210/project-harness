---
title: C4 Dynamic — harness example
status: reference
audience: [novice, seasoned, both]
tags: [viz, c4, dynamic, L2, L3, harness]
---

# C4 Dynamic — harness example

**Question answered:** How do harness containers collaborate when a reader
closes a session and merges to `main`?

> [!NOTE] REAL — harness-meta
> Numbered runtime collaboration on **static C4 elements** from [[container]].
> Track B session operations — not product L1–L4 behaviour.

## Diagram

```mermaid
flowchart LR
    Reader([Reader])
    Meta[Harness meta]
    Agents[Agent pack]
    Scripts[Validator scripts]
    Spine[Chapter spine]

    Reader -->|"1. validate diff"| Meta
    Meta -->|"2. request close draft"| Agents
    Agents -->|"3. edit STATE dashboard"| Meta
    Agents -->|"4. run validate_md"| Scripts
    Scripts -->|"5. report pass fail"| Agents
    Reader -->|"6. commit merge git"| Meta
    Meta -->|"7. archive session"| Spine
```

**Legend**

| Symbol | Role |
| :----- | :---- |
| Numbered arrow | Order of collaboration for this scenario |
| Box | Same containers as [[container]] — not new elements |
| Person | Human gate (D-001 git on Windows) |

## Field guide

| Step | In this harness | In your product |
| :---- | :-------------- | :-------------- |
| 1 | Human reviews work diff + handoff docs | Code review / PR approval |
| 2 | Agent runs close checklist on session branch | CI pipeline or release bot |
| 3 | STATE + dashboard L1–L3 updated | Status page, changelog |
| 4 | `python scripts/validate_md.py --all` | Test + lint suite |
| 5 | Zero failures required before merge offered | Green build gate |
| 6 | Human runs git commit + merge (D-001) | Deploy or merge to trunk |
| 7 | Session prose may land in chapter or session-docs | Release notes |
| Not shown here | BPMN gateways — see [[../bpmn/process-subset]] | Full workflow notation |

## ESL checklist (this file)

| Rule | Pass |
| :---- | :---- |
| Title = question | Session close collaboration |
| Labels ≤ 5 words | Yes |
| Embedded legend | Table above |
| Uses existing C4 elements | Yes — from [[container]] |
| Supplementary only | Does not replace static Container |
| Node budget | 5 containers + 1 actor |

## Pairing

| Also draw when | Diagram |
| :------------- | :------ |
| Structure not drawn yet | [[container]] |
| Full gateway logic needed | [[../bpmn/process-subset]] Variant A |
| Message-level timing | [[../uml/sequence]] Variant A |
| Irreversible gate rules | [[../dmn/decision-table]] Variant A |

## Where to go next

- **Static containers:** [[container]]
- **Session procedure:** [[session-workflow]]
- **C4 section index:** [[README]]
- **UML sequence alternative:** [[../uml/sequence]]
