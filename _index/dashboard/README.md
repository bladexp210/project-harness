---
title: Project Dashboard
chapter: index
status: living
updated: 2026-06-19 09:11
tags: [dashboard, orientation]
---

# Project dashboard — three zoom levels

Provider-agnostic status view for humans and agents. Plain markdown + Mermaid
per [[ADR-002-modeling-conventions|ADR-002]]; no Dataview or tool-specific
queries required.

Read in order when orienting:

| Zoom | File | C4 analogue | Question it answers |
| :---- | :---- | :---- | :---- |
| 1 | [[01-context]] | Context | Where is the *book project* in its product lifecycle? |
| 2 | [[02-containers]] | Containers | What is the status of each *chapter / major artifact*? |
| 3 | [[03-components]] | Components | What is *this session* doing next? |

**Chapter gaps ([[02-containers]]):** **Harness Gap (Type A)** = this harness
repo has not filled a slot; **Canon Gap (Type B)** = chapter canon still
incomplete for all readers.

**Update rule:** agent refreshes all three files at every session close
(see [[session-workflow]]). Each file carries a timestamped **History** table
(**When** column: `YYYY-MM-DD HH:mm` host local time; last 10 sessions; older
rows archived).

**Related:** [[STATE]] (read first after Agents) ·
[[session-docs]] (full prose history)
