---
title: Acme PTO FAQ — definition of done
status: living
tags: [example]
---

# Definition of done

Ship the example only when all of these are true.

| Check | Pass |
| :--- | :--- |
| Policy file is the only source the assistant reads | Yes |
| Six sample questions cite the correct heading | Yes |
| Four out-of-policy questions are refused and logged | Yes |
| No secrets, personal paths, or real employee names in the repo | Yes |
| HR can edit `policies/pto.md` and re-run the tests without an engineer in the room | Yes |

## Handoff notes for the human maintainer

- You own the policy sentences. The agent does not.
- If HR and the file disagree, fix the file in the open. Do not hide a correction in a prompt.
- When a refused question shows up three times, add a heading or leave it refused on purpose. Write that choice down.
- Engineering adopts the tests, not the chat. If the tests are green and the citation is wrong, the test is wrong.
- Retire the bot when the HR system tooltip and this file would both need updates for every rule. Until then, this file is the source of truth.
