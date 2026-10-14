---
title: "Mockup: DMN Decision Table"
status: experiment
tags: [mockup, dmn, decision, L3]
---

# DMN — Decision table (L1/L3/L4)

> **FICTITIOUS** — escalate rule. **Family:** decision (third type).

| Rule | Order value | Customer tier | → Action |
| :--- | :---------- | :------------ | :------- |
| 1 | &gt; 1000 | any | Manual review |
| 2 | * | VIP | Auto approve |
| 3 | * | * | Standard path |

**Shows well:** which outcome for which inputs — no layout or time.  
**Poor at:** who sends messages when (use BPMN2 + link DMN at gateway).
