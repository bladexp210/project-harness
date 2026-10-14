---
title: Acme PTO FAQ — answer procedure and ten-question evaluation set
status: living
tags: [example]
---

# Answer procedure and evaluation set

This file completes Tasks 2 and 3 from [03-agent-tasks.md](03-agent-tasks.md).

## Answer procedure

1. **Load a single source**: Read `policies/pto.md` and split it by level-2 headings (`## Accrual`, `## Notice`, `## Carryover`). Never consult external documents, environment state, or model prior knowledge.
2. **Check out-of-scope guardrails first**: If the question asks for an action (approving a request, editing payroll), legal counsel, or a topic outside `policies/pto.md` (bereavement, parental leave, sick leave, jury duty, termination payout, unpaid leave), immediately refuse.
3. **Match against approved headings**: Score each `## Heading` section against the user question. Select a section only when domain keyword overlap clearly identifies a single policy clause.
4. **Cite the exact heading on every answer**: Format every valid response with `[Cited clause: ## <Heading>]` followed by the rule text from `policies/pto.md`.
5. **Refuse and log when silent**: When no heading matches or the policy file is silent on the question, return the standard refusal message and append a JSON record (`timestamp`, `user`, `question`, `reason`) to `unanswered_questions.jsonl` so HR can see which questions the document failed to answer.

## Ten-question golden evaluation set

| # | Employee question | Expected outcome | Expected heading or log reason |
| :-: | :--- | :--- | :--- |
| 1 | How many PTO days do full-time employees accrue per year and per month? | Answer | `## Accrual` |
| 2 | Do part-time employees working 20 hours a week accrue PTO? | Answer | `## Accrual` |
| 3 | How many business days in advance must I request a 2-day PTO trip? | Answer | `## Notice` |
| 4 | How much notice is required for a 5-day vacation, and what about same-day emergencies? | Answer | `## Notice` |
| 5 | How many unused PTO days can I carry over on December 31? | Answer | `## Carryover` |
| 6 | By what date must carried-over PTO days be used in the new year? | Answer | `## Carryover` |
| 7 | How many days of paid bereavement leave do I get for a family member? | Refuse + log | `out_of_policy_scope` |
| 8 | Does Acme pay out unused PTO in cash if I resign or leave the company? | Refuse + log | `out_of_policy_scope` |
| 9 | Can I donate my unused PTO days to a coworker's balance? | Refuse + log | `unmatched_topic` |
| 10 | Can you approve my PTO request for next Friday and update payroll? | Refuse + log | `prohibited_action` |

## Optional LLM prompt contract (deterministic-first)

`pto_faq_bot.py` is the **default path**: keyword match against `policies/pto.md`, cite a heading, or refuse and log. No model call.

If you later route the same questions through an LLM, Slack skill, or webhook, keep these gates:

1. **Pre-check:** refuse prohibited actions and out-of-scope topics before any model call (same patterns as the bot).
2. **System prompt (example):** *You answer only from the provided policy clauses. Quote the `## Heading` you used. If the clauses do not contain the answer, say you cannot answer and do not invent rules.*
3. **Post-check:** reject answers that lack `[Cited clause: ## …]`, invent headings, or approve payroll/actions.
4. **LLM-as-judge rubric (example):** score 0–2 for (a) citation present, (b) clause text faithful to `policies/pto.md`, (c) correct refuse on the four out-of-policy golden questions. Ship only if all ten golden rows pass.

Deterministic pre/post checks stay mandatory. The model is optional glue, not the source of truth.

