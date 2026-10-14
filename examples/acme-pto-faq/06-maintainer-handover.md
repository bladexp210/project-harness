---
title: Acme PTO FAQ — maintainer handover and HR guide
status: living
tags: [example, runbook]
---

# Maintainer handover and HR update guide

This guide completes Task 5 from [03-agent-tasks.md](03-agent-tasks.md) so a new teammate or HR editor can update policy rules and verify the assistant without needing prior chat history.

## How HR updates a PTO rule (no code changes required)

1. Open [`policies/pto.md`](policies/pto.md) in GitHub or your text editor.
2. Edit the text under `## Accrual`, `## Notice`, or `## Carryover`, or add a new `## Heading` section if a new PTO topic is approved.
3. Run the verification suite from the repository root to confirm all golden tests pass:

```bash
python -m unittest discover -s examples/acme-pto-faq -p "test_*.py" -v
```

4. If you intentionally changed a number (such as increasing carryover from `5` days to `8` days), update the expected phrase in [`test_pto_faq_bot.py`](test_pto_faq_bot.py) so the test suite reflects the new rule.

## How to review refused questions and close policy gaps

When an employee asks a question that [`policies/pto.md`](policies/pto.md) does not cover, [`pto_faq_bot.py`](pto_faq_bot.py) refuses to guess and appends a JSON entry to `examples/acme-pto-faq/unanswered_questions.jsonl`:

```json
{"timestamp": "2026-10-14T09:00:00+00:00", "user": "employee@example.com", "question": "How many days of paid bereavement leave do I get?", "reason": "out_of_policy_scope"}
```

- **Weekly triage**: Check `unanswered_questions.jsonl` once a week.
- **Three-strike rule**: When the same unanswered question appears three times, decide with HR whether to add an approved `## Heading` section to [`policies/pto.md`](policies/pto.md) or keep it explicitly refused, and record that choice in [`05-answer-procedure-and-eval-set.md`](05-answer-procedure-and-eval-set.md).
- **Retirement trigger**: Decommission this assistant when the main HR portal integrates direct, single-source clause citations from [`policies/pto.md`](policies/pto.md).
