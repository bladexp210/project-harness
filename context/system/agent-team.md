---
title: Agent Team
layer: 1-system
status: reference
tags: [agents, team, composition]
---

# Agent Team Reference

Load this file when working on agents/*.yaml or the 04-your-agents chapter.

---

## Critical: k Is a Margin, Not a Count

**k = the required margin by which the winning solution must beat second place.** k is NOT the number of agents.

With 5 agents and k=4: the winner must receive 4 more votes than second place — near-unanimity. If no candidate clears k, the evaluator agent runs as tiebreaker.

Three independent dimensions driven by criticality:

- Number of parallel runs (1 → 5+)  
- k threshold (1 → 5)  
- Specialist roles activated (general → full battery)

---

## Core Team (permanent, every project)

| Role | File | Model axis | Mandate |
| :---- | :---- | :---- | :---- |
| Dev Agent | agents/dev-agent.yaml | complexity | Execute bounded tasks |
| General Tester | agents/tester-agent.yaml | fast | "Your job is to break this" |
| Security Tester | agents/security-tester.yaml | capable | Injection, auth bypass, CVE patterns |
| Evaluator | agents/evaluator.yaml | cheap/fast | Score options against criteria. Find what each costs. Bias mitigations required — see [[evaluator]]. |
| Red-team | agents/red-team-agent.yaml | frontier | Challenge decisions before they are made. Holds the security/compliance seat: runs ADR pre-mortems, owns the threat model (trust boundaries, abuse cases, AI-specific threats), challenges use-case must-have lane omissions. Fork a specialist if post-mortems show the charter overloaded. |

**Post-mortem support:** rohansx/reflect MCP — not an agent, infrastructure.

### Orchestration and Brooks positioning

Every agent run is bound to **one task file** with named Executor, Supervisor,
and scope. Agents do not spawn follow-on tasks or invoke sibling agents unless
the active task's Outputs explicitly hand off to the next task file.

AI agents reduce **accidental** complexity — boilerplate, test scaffolding,
trace plumbing — not **essential** complexity in your domain model, compliance
rules, or user workflows. If a difficulty would survive a vendor or framework
change, it deserves design time (ADR, layer decision), not a larger prompt. See
the Brooks test in [[02-design/README|Ch. 02]] five-paper checklist.

---

## Specialist Team (forked on demand)

All are forks of tester-agent.yaml. Change role + goal + specialization + model alias. ~5 minutes.

| Role | File | Focus |
| :---- | :---- | :---- |
| Performance Tester | agents/perf-tester.yaml | Throughput, latency, load scenarios |
| Data Validator | agents/data-validator.yaml | Schema, migration integrity, consistency |
| API Contract Tester | agents/api-tester.yaml | Endpoint contracts, payload validation |

New specialists emerge from the learning loop — when post-mortems reveal a systematic gap, create a new specialist seeded from that lesson.

---

## LLM Assignment (via LiteLLM aliases)

Agent definitions reference aliases, never specific model names. All model assignments live in litellm config.yaml — one place, one change.

```
# agents/security-tester.yaml (excerpt)
model: security-llm    ← alias, not "anthropic/claude-opus-4-6"

# litellm config.yaml
model_list:
  - model_name: security-llm
    litellm_params:
      model: openrouter/anthropic/claude-opus-4-6
```

Changing the model behind an alias: edit one line in litellm config. Zero agent files touched.

---

## Seed Repositories

### Run directly (infrastructure)

| Tool | Repo |
| :---- | :---- |
| OpenHands | github.com/all-hands-ai/OpenHands |
| rohansx/reflect | github.com/rohansx/reflect |
| LiteLLM | github.com/BerriAI/litellm |
| Langfuse | github.com/langfuse/langfuse |

### Study and adapt — extract patterns

| Purpose | Repo |
| :---- | :---- |
| Dev agent loop pattern | github.com/SWE-agent/mini-swe-agent |
| TDD separation (programmer/test-designer/executor) | github.com/huangd1999/AgentCoder |
| Test generation approach | github.com/Codium-ai/AlphaCodium |
| Dev agent definition structure | github.com/automagik-dev/genie |
| Test-based evaluation and ranking | github.com/OpenAutoCoder/Agentless |
| YAML role templates (80+ to adapt) | github.com/crewAIInc/crewAI-examples |
| Post-mortem pattern foundation | github.com/noahshinn/reflexion |

### External guidelines

| Purpose | Source |
| :---- | :---- |
| Security tester prompts | owasp.org/www-project-web-security-testing-guide |

---

## TASK.md Structure (reference)

```
## Complexity: [simple / moderate / complex]
## Criticality: [low / medium / high / critical]
## k threshold: [1 / 2 / 4 / 5]
## Model: [fast-llm / capable-llm / frontier-llm]

## Exploration loops (if applicable)
1. Research option A
2. Red-team option A
3. Document decision → docs/decisions/ADR-NNN.md

## Boilerplate to use
- boilerplate/code/...

## Context
- System:  context/system/overview.md
- Arch:    context/architecture/<domain>/...
- Impl:    context/implementation/<feature>/...

## Scope — modify
## Scope — read only
## Acceptance criteria
## Constraints
```

