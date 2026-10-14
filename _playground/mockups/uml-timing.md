---
title: "Mockup: UML Timing"
status: experiment
tags: [mockup, uml, dynamic, L4]
---

# UML — Timing diagram (L4)

> **FICTITIOUS** — payment timeout constraint. **Family:** dynamic.

```mermaid
sequenceDiagram
    participant API
    participant Pay as Payment
    Note over API,Pay: t=0s authorize sent
    Pay--xAPI: no response by t=30s
    API->>API: cancel order (timeout rule)
```

**Shows well:** time constraints on interactions.  
**Poor at:** business policy prose (use DMN table).

*Note: full UML timing uses time-axis notation; Mermaid approximates with notes.*
