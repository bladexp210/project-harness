---
title: "Mockup: UML Activity"
status: experiment
tags: [mockup, uml, dynamic, L3]
---

# UML — Activity diagram (L3)

> **FICTITIOUS** — refund approval branch. **Family:** dynamic.

```mermaid
flowchart TD
    Start([Start]) --> Check{Amount over limit?}
    Check -->|yes| Manager[Manager approve]
    Check -->|no| Auto[Auto approve]
    Manager --> Issue[Issue refund]
    Auto --> Issue
    Issue --> End([End])
```

**Shows well:** control flow with forks.  
**Poor at:** cross-org message contracts (use BPMN2 choreography).
