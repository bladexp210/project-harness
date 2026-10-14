---
title: "ADR-009: Observability — Paths A, B, and C"
chapter: 2
status: accepted
date: 2026-07-01
tags:
  - decision
  - observability
  - execution
  - langfuse
---

# ADR-009 — Observability: Paths A, B, and C

**Status:** accepted — 2026-07-01, Session 42.

## Context

Track A shipped **Path A** observability at Session 27: LiteLLM success/failure
callbacks → Langfuse in `track-a/` compose ([[track-a-setup]]). That captures
**model-level** traces (tokens, cost, latency, routing) but not IDE agent tool
spans or harness **process** evidence (Proceed gates, merge, STATE freshness).

The harness is authored on **Track B** (IDE agents) per [[ADR-007-dual-execution-tracks|ADR-007]].
Readers need a decision that names **three integration paths**, states which is
live today, which is deferred, and what complements git-tracked handoff docs.

S41 inbox triage assigned three intake files to this session — **cite, do not
paste**:

| Intake | Use in this ADR |
| :----- | :-------------- |
| Langfuse Integration Report | Path A/B data model; anti-patterns; self-host notes |
| LiteLLM + OpenRouter guide | Stack layering; LiteLLM as control plane |
| PROJECT_EVALUATION_TRACK-A | Gap list (Path B unwired; doc fragmentation closed here) |

Path A is **implemented**. Path B (OpenHands OTEL) and Path C (IDE hooks) were
brainstormed in [[session-roadmap-s40-plus]] before arc42 §8 listed Path A only.

## Decision

Adopt **three named observability paths** plus a **process trace** layer that
is not a Langfuse path but is mandatory for harness handoff.

### Path matrix

| Dimension | **Path A** — LiteLLM callbacks | **Path B** — OpenHands OTEL | **Path C** — IDE hooks → Langfuse |
| :---- | :---- | :---- | :---- |
| **Track** | A (build) | A (build) | B (authoring / POC default) |
| **Captures** | Model calls, tokens, cost, routing | Agent steps, tool I/O in OpenHands | Session, tools, shell, edits, MCP, timestamps |
| **Setup** | `track-a/` compose (S27) | OTEL exporter in OpenHands | VS Code hooks + `langfuse_trace_bridge` (**Live** S44) |
| **Status in harness** | **Live** | **Documented — not wired** | **Live** (S44) |
| **Complements** | Path C when API routed via LiteLLM | Path A (`session_id` correlate) | Path A; STATE/git process evidence |
| **Redundant with** | — | Overlaps Path C tool spans if both run | Overlaps Path B when OTEL wired |
| **Limitation** | No agent "why" without B/C | Docker-only; not POC-blocking | No subscription token/cost; redaction duty |

### Process trace (mandatory — all tracks)

**Not a fourth Langfuse path.** Git-tracked harness artifacts record decisions
agents cannot infer from model traces alone:

| Artifact | Captures |
| :------- | :------- |
| [[STATE]] + `_index/dashboard/` | Session phase, milestones, bootstrap |
| [[session-workflow]] gates | Proceed, validate, merge preconditions |
| Conventional Commits on Windows (D-001) | What shipped, when, on which branch |
| `review/*.html` export blocks (S41+) | Human disposition at structured gates |

Engineering handoff requires **process trace + at least one Langfuse path**
when observability is claimed operational.

### POC default (solo contributor)

| Situation | Default |
| :-------- | :------ |
| Track B authoring (this repo today) | **Path C** + **process trace** |
| Docker + OpenHands viable | **Path A**; add Path B later for agent-depth |
| Engineering needs cost attribution | **Path A required** |
| Langfuse compose not running | Hooks queue locally; **fail open** (S44) |

Path B remains **optional depth** — document in [[track-a-setup]] and Ch. 05;
do not block POC or S47 handoff on OTEL wiring.

### Decision criteria

| If… | Then… |
| :---- | :---- |
| Docker + OpenHands viable | Path A (+ Path B later for depth) |
| VS Code / CLI authoring only | Path C + process trace |
| Multi-day sessions | Path C + temporal layer ([[session-roadmap-s40-plus]] — S45, out of scope here) |
| Langfuse UI down | Agent work continues; traces buffer or drop — never block |

### Stack reference (Path A — cite only)

Directed chain from intake synthesis — full wiring in [[track-a-setup]]:

```text
OpenHands → LiteLLM (proxy) → OpenRouter / direct providers
                │
                └── Langfuse (callbacks — Path A)
```

Langfuse sits on the **observation plane**; it does not intercept traffic
(Langfuse Integration Report §1). LiteLLM is the control plane (budget,
fallback, virtual keys); OpenRouter is one upstream among many (LiteLLM guide §1).

### Anti-patterns

| Anti-pattern | Why it fails |
| :---- | :---- |
| Langfuse-only, no STATE/git | Loses merge gates and handoff docs |
| STATE-only, no Path C | No tool-level replay for engineering |
| Logging full prompts to Langfuse | Secret leakage |
| Blocking hooks on Langfuse timeout | Agent stalls; trace must fail open |
| Bulk `_inbox/` paste into canon | Competing voices; violates ADR-008 |

### Failure conditions

| Path | Do **not** rely on it when… |
| :---- | :---- |
| Path A | Reader will not run Docker; need IDE-only POC |
| Path B | Path C already captures tool spans; OTEL adds ops burden without new signal |
| Path C | Reader needs per-model cost attribution — use Path A |
| Any Langfuse path | Compliance requires air-gapped authoring with no external trace store |

## Consequences

### Positive

- arc42 §8 and Ch. 05 share one vocabulary for observability.
- S44 Path C implementation has an accepted target shape.
- Track A evaluation gaps (Path B unwired, fragmented docs) close at decision
  layer — implementation stays deferred per matrix above.

### Negative / trade-offs

- Three paths increase reader cognitive load — mitigated by POC default table.
- Path B "documented not wired" may confuse until Ch. 05 callout is explicit.
- Path C redaction is reader responsibility; ADR does not prescribe scrub rules.

### Follow-on (not S42)

| Session | Work |
| :------ | :--- |
| S44 | Path C hook bridge + smoke trace | **Done** — see [[path-c-hook-contract]] |
| S45 | Temporal awareness schema (referenced only — not in ADR-009 scope) |
| S47 | Archive consumed `_inbox/` observability reports to `research/` |

## References

- [[track-a-setup]] — Path A compose and Langfuse keys
- [[session-roadmap-s40-plus]] — Paths brainstorm and ship bar
- [[ADR-007-dual-execution-tracks]] — Track A vs B
- arc42 §8 — [[../arc42/08-crosscutting-concepts#Observability]]
- Intake (consumed S42, archive S47): `_inbox/Langfuse Integration Report…`,
  `_inbox/LiteLLM + OpenRouter…`, `_inbox/PROJECT_EVALUATION_TRACK-A.md`

## History

| When | Event |
| :---- | :---- |
| 2026-07-01 | Accepted S42 — human gate; inbox cites consumed |
