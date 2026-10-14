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
> physical nodes. Draw [[viz/c4/container]] first; this section links
> [[viz/c4/deployment]] as the single source. Track A Docker detail is a
> cross-link only — not a second deployment canvas here.

## Scope statement

| In scope | Out of scope |
| :------- | :----------- |
| Reader Windows host (git, markdown, validator) | Reader's product cloud topology |
| Optional Docker host for Track A compose | Full Ch. 07 production runbooks |
| External LLM API and optional Langfuse | `_playground/` until promoted |

## Deployment diagram

arc42 §7 maps to **C4 Deployment** (supplementary to Container). The worked
harness diagram lives in [[viz/c4/deployment]] — link it rather than
duplicating the canvas.

Open: [[viz/c4/deployment|C4 Deployment — harness example]]

## Node mapping (this harness)

| Deployment node | Containers / artifacts hosted | Notes |
| :-------------- | :---------------------------- | :---- |
| Reader Windows host | Git repo, chapter spine, STATE, dashboard, validator | Primary dev surface (D-001 git) |
| Obsidian vault | May share disk with git clone | Read/sync — not a harness container |
| Docker host (optional) | Track A stack — LiteLLM, OpenHands | See [[track-a-setup]] for compose |
| External cloud | LLM API provider | Outbound from Track A proxy |
| External cloud (optional) | Langfuse UI | Traces from LiteLLM Path A callbacks |

Logical dependencies between modules remain on [[viz/c4/container]] — deployment
shows **where** artifacts live, not **what depends on what**.

## Track A cross-link

Physical services, ports, secrets, and smoke-trace steps for the compose
stack are documented in [[track-a-setup]] — not repeated in this arc42
section. Use §7 for the harness-wide node map; use track-a-setup when you
are operating Track A.

| Topic | Where |
| :---- | :---- |
| Compose file, env vars | `05-build/execution-tools/track-a/` |
| Langfuse wiring | [[track-a-setup]] steps 3b–4b |
| Runtime message order | §6 secondary — [[viz/uml/sequence]] Variant B |

## ESL checklist (this section)

| Rule | Pass |
| :---- | :---- |
| Deployment ≠ Container | Separate canvas from [[viz/c4/container]] |
| Diagram linked not pasted | [[viz/c4/deployment]] |
| Environments named | Windows host · Docker optional · cloud external |
| Static mapping only | Runtime sequence → §6 |
| Product fork reminder | Reader replaces nodes for their ship target |

## Where to go next

- **Logical containers (§5):** [[05-building-block-view]]
- **Runtime (§6):** [[06-runtime-view]]
- **Track A operations:** [[track-a-setup]]
- **Ship chapter:** [[07-ship-operate]]
- **Section index:** [[README]]
