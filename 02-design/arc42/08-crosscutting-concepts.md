---
title: "arc42 §8 — Crosscutting Concepts"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, harness]
---

# arc42 §8 — Crosscutting Concepts

**Question answered:** Which concepts apply across many building blocks?

> [!NOTE] REAL — harness-meta
> Patterns that span multiple §5 containers in **this repo**. Your product
> fork replaces examples — keep one subsection per concept and link to layer
> files or ADRs for full text.

## Concept index

| Concept | Applies across | Deep reference |
| :------ | :------------- | :------------- |
| Observability | Execution tools, Track A stack, Track B hooks | [ADR-009-observability-paths-abc](../decisions/ADR-009-observability-paths-abc.md), [track-a-setup](../../05-build/execution-tools/track-a-setup.md) |
| Agent context loading | Agent pack, Context tree, tasks | [context/](../../context/README.md), [Agents](../../Agents.md) |
| Reader-facing prose | All chapters, session gates | [ADR-008-reader-facing-language-and-visuals](../decisions/ADR-008-reader-facing-language-and-visuals.md) |
| Failure conditions | Tasks, ADRs, teaching patterns | [ADR-005-failure-condition-convention](../decisions/ADR-005-failure-condition-convention.md) |

## Observability

**What:** Three **Langfuse integration paths** (A / B / C) plus mandatory
**process trace** (STATE, dashboard, git, session gates). Path A is live in
Track A compose; Path B is documented only; Path C is live via
[hook contract](../../05-build/execution-tools/path-c-hook-contract.md).

Full decision: [ADR-009](../decisions/ADR-009-observability-paths-abc.md).

### Path comparison

| Dimension | Path A — LiteLLM callbacks | Path B — OpenHands OTEL | Path C — IDE hooks |
| :---- | :---- | :---- | :---- |
| Track | A | A | B |
| Captures | Model calls, cost, routing | Agent steps, tool I/O | Session, tools, edits, MCP |
| Harness status | **Live** (S27) | Documented — not wired | **Live** (S44) |
| POC default | When Docker up | Optional depth | Solo Track B authoring |

### Rules in this harness

| Rule | Detail |
| :---- | :----- |
| Path A source | LiteLLM proxy callbacks — [track-a-setup](../../05-build/execution-tools/track-a-setup.md) |
| Path C source | `.cursor/hooks.json` + `scripts/langfuse_trace_bridge.py` — [path-c-hook-contract](../../05-build/execution-tools/path-c-hook-contract.md) |
| Temporal layer | Session log (`logs/sessions/<id>.md`, gitignored) + canon freshness banner — S45 |
| Langfuse UI | `:3001` when compose is up (§7 deployment) |
| Process trace | [STATE](../../STATE.md), [session-workflow](../../context/system/session-workflow.md), D-001 git — always |
| Anti-patterns | Langfuse-only or STATE-only — see ADR-009 |
| Runtime view | [sequence](../../viz/uml/sequence.md) Variant B (Path A task) |

Do not duplicate ADR-009 prose here — link for decision criteria and failure
conditions.

## Agent context loading

**What:** Deterministic path lists in task frontmatter — no vector search.
Implements Parnas information hiding across three layers.

| Layer | Path pattern | Loaded when |
| :---- | :----------- | :---------- |
| 1 — System | `context/system/` | Most tasks; agent defaults |
| 2 — Architecture | `context/architecture/<domain>/` | Task touches that domain |
| 3 — Implementation | `context/implementation/<feature>/` | Narrow task slice |

Loader rules: [context-loader](../../04-your-agents/context-loader.md) · `scripts/task_context.py` · load table in
[Agents](../../Agents.md). Structural view: [component](../../viz/c4/component.md) (Context loader
component).

## Reader-facing prose

**What:** Plain-language human gates, tables over fog, wiki-link conventions,
and artifact zones separated from teaching callouts ([ADR-006](../decisions/ADR-006-teaching-block-convention.md)
evaluator enforces zones).

| Rule | Example in harness |
| :---- | :----------------- |
| Open/close gates with numbered scope | Session plan shape in [Agents](../../Agents.md) |
| Define terms once | Harness Gap vs Canon Gap in dashboard |
| Low decode cost | arc42 sections link `viz/` — no screenshot dumps |

Full decision: [ADR-008-reader-facing-language-and-visuals](../decisions/ADR-008-reader-facing-language-and-visuals.md)

## Failure conditions

**What:** Every recommended pattern names when **not** to apply it — prevents
silent misfit when the reader forks the harness.

| Where it appears | Example |
| :--------------- | :------ |
| ADR-005 | Failure-condition blocks in layer teaching |
| ICOM+ Controls | Mechanism selection gates on tasks |
| DMN tables | [decision-table](../../viz/dmn/decision-table.md) Variant A/B outcomes |
| Viz pairing tables | "Not shown here" rows in `viz/c4/*` |

Full convention: [ADR-005-failure-condition-convention](../decisions/ADR-005-failure-condition-convention.md)

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| One subsection per concept | Four concepts above |
| Link don't duplicate | ADRs and layer files hold full text |
| Cross-container scope | Each concept spans ≥2 §5 containers |
| Product fork reminder | Reader replaces examples, keeps shape |

## Where to go next

- **Four layers:** [data](../layers/data.md), [application](../layers/application.md), [ux](../layers/ux.md), [communication](../layers/communication.md)
- **Decisions (§9):** [09-architectural-decisions](09-architectural-decisions.md)
- **Section index:** [README](README.md)
