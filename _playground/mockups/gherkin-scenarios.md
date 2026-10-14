---
title: "Mockup: Gherkin"
status: experiment
tags: [mockup, gherkin, decision, L4]
---

# Gherkin — Acceptance scenarios (L4)

> **FICTITIOUS** — task completion contract. **Family:** decision/spec (not a diagram).

```gherkin
Scenario: Order ships after payment
  Given a paid order with valid address
  When the warehouse confirms pick
  Then the order status is Shipped
  And the customer receives a tracking id
```

**Shows well:** observable, testable outcomes.  
**Poor at:** architecture; message order (pair with sequence if needed).
