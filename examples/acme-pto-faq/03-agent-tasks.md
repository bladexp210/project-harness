---
title: Acme PTO FAQ — agent tasks
status: living
tags: [example]
---

# Agent tasks

The human writes the policy file and accepts or rejects each task. Agents do not widen the scope.

| # | Task | Owner | Done when |
| :-: | :--- | :--- | :--- |
| 1 | Draft `policies/pto.md` as a fictional one-page policy with three headings (accrual, notice, carryover) | Human with an agent draft | HR editor can point at each heading |
| 2 | Write the answer procedure: cite a heading, or refuse and log | Agent drafts, human accepts | Procedure fits on one page |
| 3 | List ten questions: six answerable from the file, four that must be refused | Agent | Each row says expected behavior |
| 4 | Implement the smallest reader that loads the policy file and follows the procedure | Agent | Tests in task 3 pass locally |
| 5 | Add a maintainer note: how HR updates the file and how to re-run tests | Agent drafts, human edits | A new teammate can follow it without chat history |

Stop after task 4 if a test expects the bot to invent a rule that is not in the file. That is a spec bug, not a prompt tweak.
