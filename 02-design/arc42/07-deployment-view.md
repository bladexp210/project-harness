---
title: "arc42 §7 — Deployment View"
chapter: 02
status: reference
audience: [novice, seasoned, both]
tags: [arc42, design, harness]
---

# arc42 §7 — Deployment View

**Question answered:** How is software mapped to infrastructure?

> [!NOTE] REAL — harness-meta
> **Book-repo logical deployment** — where harness containers from §5 run on
> physical nodes. Draw [container](../../viz/c4/container.md) first; this section links
> [deployment](../../viz/c4/deployment.md) as the single source. Track A Docker detail is a
> cross-link only — not a second deployment canvas here.

## Scope statement

| In scope | Out of scope |
| :------- | :----------- |
| Reader Windows host (git, markdown, validator) | Reader's product cloud topology |
| Optional Docker host for Track A compose | Full Ch. 07 production runbooks |
| External LLM API and optional Langfuse | `_playground/` until promoted |

## Deployment diagram

arc42 §7 maps to **C4 Deployment** (supplementary to Container). The worked
harness diagram lives in [deployment](../../viz/c4/deployment.md) — link it rather than
duplicating the canvas.

Open: [C4 Deployment — harness example](../../viz/c4/deployment.md)

## Node mapping (this harness)

| Deployment node | Containers / artifacts hosted | Notes |
| :-------------- | :---------------------------- | :---- |
| Reader Windows host | Git repo, chapter spine, STATE, dashboard, validator | Primary dev surface (D-001 git) |
| Obsidian vault | May share disk with git clone | Read/sync — not a harness container |
| Docker host (optional) | Track A stack — LiteLLM, OpenHands | See [track-a-setup](../../05-build/execution-tools/track-a-setup.md) for compose |
| External cloud | LLM API provider | Outbound from Track A proxy |
| External cloud (optional) | Langfuse UI | Traces from LiteLLM Path A callbacks |

Logical dependencies between modules remain on [container](../../viz/c4/container.md) — deployment
shows **where** artifacts live, not **what depends on what**.

## Track A cross-link

Physical services, ports, secrets, and smoke-trace steps for the compose
stack are documented in [track-a-setup](../../05-build/execution-tools/track-a-setup.md) — not repeated in this arc42
section. Use §7 for the harness-wide node map; use track-a-setup when you
are operating Track A.

| Topic | Where |
| :---- | :---- |
| Compose file, env vars | `05-build/execution-tools/track-a/` |
| Langfuse wiring | [track-a-setup](../../05-build/execution-tools/track-a-setup.md) steps 3b–4b |
| Runtime message order | §6 secondary — [sequence](../../viz/uml/sequence.md) Variant B |

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| Deployment ≠ Container | Separate canvas from [container](../../viz/c4/container.md) |
| Diagram linked not pasted | [deployment](../../viz/c4/deployment.md) |
| Environments named | Windows host · Docker optional · cloud external |
| Static mapping only | Runtime sequence → §6 |
| Product fork reminder | Reader replaces nodes for their ship target |

## Where to go next

- **Logical containers (§5):** [05-building-block-view](05-building-block-view.md)
- **Runtime (§6):** [06-runtime-view](06-runtime-view.md)
- **Track A operations:** [track-a-setup](../../05-build/execution-tools/track-a-setup.md)
- **Ship chapter:** [07-ship-operate](../../07-ship-operate/README.md)
- **Section index:** [README](README.md)
