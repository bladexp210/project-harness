---
title: Acme PTO FAQ — worked example
status: living
audience: [novice, seasoned, both]
tags: [example]
---

# Acme PTO FAQ

Fictional internal tool: problem and constraints first, then a small **stdlib Python** reader (not an LLM product), a 10-question golden suite, and an HR handover guide.

| Step | File | Purpose |
| :--- | :--- | :--- |
| 1. Problem | [01-problem.md](01-problem.md) | Why employees guess and why HR needs refusal logging |
| 2. Spec and constraints | [02-spec-and-constraints.md](02-spec-and-constraints.md) | Single-file source of truth, citation rules, failure bounds |
| 3. Agent tasks | [03-agent-tasks.md](03-agent-tasks.md) | Five bounded tasks |
| 4. Definition of done | [04-definition-of-done.md](04-definition-of-done.md) | Release gates |
| 5. Approved policy | [policies/pto.md](policies/pto.md) | Task 1: Accrual / Notice / Carryover |
| 6. Procedure and evals | [05-answer-procedure-and-eval-set.md](05-answer-procedure-and-eval-set.md) | Tasks 2–3 |
| 7. Working reader and tests | [pto_faq_bot.py](pto_faq_bot.py) / [test_pto_faq_bot.py](test_pto_faq_bot.py) | Task 4 |
| 8. Maintainer handover | [06-maintainer-handover.md](06-maintainer-handover.md) | Task 5 |

## Quick verification

From the repository root:

```bash
python -m unittest discover -s examples/acme-pto-faq -p "test_*.py" -v
```

```bash
python examples/acme-pto-faq/pto_faq_bot.py "How many unused PTO days can I carry over?"
```
