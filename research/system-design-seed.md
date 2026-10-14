---
title: "Seed: system-design repos distillation (KDnuggets top-10)"
status: reference
date: 2026-06-10
tags: [research, seed, provenance]
---

# Seed — System-Design GitHub Repos

Distilled 2026-06-10 from 8 of the KDnuggets top-10 repos (the two
interview-handbook repos skipped as out of scope) by three parallel research
agents. Everything reworded; provenance is `repo → section`. Use under
[ADR-002-modeling-conventions](../02-design/decisions/ADR-002-modeling-conventions.md) when pulling into chapters. Companion:
[[company-framework-seed]].

## License matrix — read before citing anything

| Source | License | Rule for the book |
| :---- | :---- | :---- |
| donnemartin/system-design-primer | CC BY 4.0 | **Backbone source.** Adapt freely with attribution + change notes. |
| binhnguyennus/awesome-scalability | MIT | Quote/adapt with attribution. |
| ByteByteGoHq/system-design-101 | CC BY-NC-ND | Ideas only, independently re-expressed and re-verified. No adapted text/diagrams. |
| karanpratapsingh/system-design | CC BY-NC-ND | Same — idea checklist only. |
| ashishps1 / InterviewReady lists | GPL-3.0 | Research input only; cite the third-party resources they link, not the lists' text. |
| sarwarbeing-ai/Agentic_Design_Patterns | **DMCA-disabled (Springer, 2026-02-27)** — pirated book mirror | **Never cite the repo.** Cite A. Gulli, *Agentic Design Patterns* (Springer 2025) directly. |
| chiphuyen/machine-learning-systems-design | No license (all rights reserved) | Ideas with attribution; no verbatim. Prefer citing her O'Reilly book (2022), which supersedes it. |

The book is internal, but NC/ND/GPL discipline still applies — reword
independently, attribute ideas, copy nothing.

## Meta-finding

All lists independently converge on the same taxonomy: data (DB + cache),
communication (API + queue + LB), application (services + consensus +
resilience), operations (observability + availability) — **external
validation of the four-layer Ch. 02 split**. UX is near-absent everywhere;
the UX layer file needs different sources. The primer's recurring thesis is
the book's Ch. 02 framing verbatim-in-spirit: *every de-bottlenecking device
(LB, cache, replica, queue) is itself a future bottleneck and failure mode.*

---

## Ch. 02 — data layer

- **SQL vs NoSQL two-column checklist** — toward SQL: relational data,
  multi-row transactions, joins, mature tooling; toward NoSQL: fluid
  schema, little inter-record reference, TB–PB scale, raw IOPS. Workloads
  that suit NoSQL: clickstream ingest, leaderboards, throwaway carts, hot
  lookups. *Decision-table ready.* `primer → SQL or NoSQL`
- **NoSQL flavor picker** — key-value (O(1) lookups, caches) / document
  (self-contained semi-structured) / wide column (huge data, availability
  over query richness) / graph (dense many-to-many). `primer → NoSQL`
- **ACID vs BASE** — money/inventory → ACID; massive scale + staleness
  tolerance → BASE (consistency burden moves into app code).
  `karanpratapsingh → ACID and BASE`
- **Normalize vs denormalize** — the tipping number: reads typically
  outnumber writes 100:1–1000:1; distribution itself argues for
  denormalizing (cross-node joins). `primer → Denormalization`
- **Relational scaling ladder** (an order-of-operations heuristic): tune
  queries → read replicas → federation → shard — cheapest reversible step
  first. `primer → Database`
- **Replication** — single-primary (simple, write bottleneck, promotion
  logic) vs multi-primary (write-survivable, conflict resolution).
  Sync replica = current but writes wait; async = fast but a loss window.
  `primer → Master-slave/Master-master`
- **Sharding strategies** — range (simple, hotspots), hash (even, expensive
  topology changes unless consistent hashing), composite buckets. Failure
  modes: lopsided shards, cross-shard joins, rebalancing.
  `primer → Sharding`
- **CAP → PACELC** — the better novice framing: even with nothing broken,
  you trade latency vs consistency. CAP alone is a conversation-opener,
  not a decision procedure. `karanpratapsingh → CAP/PACELC`
- **Cross-service consistency: exactly two patterns worth teaching** —
  transactional outbox and sagas (choreography vs orchestration as the
  sub-decision); 2PC only for few nodes + hard atomicity.
  `InterviewReady → Distributed Transactions` · `karanpratapsingh → Distributed Transactions`
- **Cache write strategies** — cache-aside / write-through / write-behind /
  write-around / refresh-ahead × (staleness, write latency, loss risk,
  complexity). When NOT to cache: source as fast as cache, low repetition,
  rapid change. Users tolerate slow writes more than slow reads.
  *Best single decision-table candidate.* `primer → Cache` · `karanpratapsingh → Caching`
- **Cache failure modes** (verify against vendor docs before publishing;
  NC-ND origin): mass TTL expiry stampede → jitter; nonexistent-key
  hammering → cache nulls / bloom filter; hot-key expiry → don't expire
  hot keys; cache death → circuit breaker + clustering.
  `bytebytego → How Can Cache Systems Go Wrong (idea-only)`

## Ch. 02 — application layer

- **Vertical vs horizontal scaling** — the hidden cost: horizontal forces
  *architectural* change (statelessness, shared sessions), not just more
  hardware. `primer → Horizontal scaling`
- **Availability math** — the nines table (99.9% ≈ 8.8 h/yr; 99.99% ≈ 53
  min/yr); sequential components multiply availability *down* (two 99.9%
  in series = 99.8%), parallel multiply failure away (= 99.9999%).
  *Quantified, formulaic — feeds Ch. 02 choices and Ch. 07 SLOs.*
  `primer → Availability in numbers`
- **Failover** — active-passive (idle capacity, hot vs cold standby decides
  recovery time) vs active-active (throughput + routing complexity); the
  failover window can lose unreplicated writes. `primer → Fail-over`
- **Monolith vs services** — split on team size and deployment cadence more
  than raw traffic; the price is service discovery and operational
  complexity. Antipattern catalog worth citing: Uber's "nanoservices"
  cautionary tale. `primer → Application layer` · `InterviewReady → Microservices`
- **Internal code structure** (only InterviewReady covers it): hexagonal /
  clean architecture / CQRS / DDD as the module-boundary vocabulary.
  `InterviewReady → Software Architectures`
- **LB vs reverse proxy heuristic** — an LB earns its keep only with
  multiple servers; a reverse proxy is useful even with one. L4 cheap and
  content-blind; L7 content-aware. DNS balancing's failure: no health
  checks. `primer → Load balancer vs reverse proxy`

## Ch. 02 — communication layer

- **Sync vs async** — queue only what the caller doesn't need to proceed;
  cheap fast real-time ops are better synchronous. Back-pressure rule: cap
  the queue, reject with 503 + exponential backoff. `primer → Asynchronism`
- **Delivery semantics as a coding constraint** — at-least-once ⇒ consumers
  must be idempotent. Idempotency is a *fundamental*, not advanced: over a
  network, every operation can be retried. Canonical walkthrough: Airbnb
  double-payments post (cited by two lists independently).
  `karanpratapsingh → Message Queues` · `ashishps1 → API Fundamentals`
- **REST vs RPC vs GraphQL** — REST: public, resource-shaped, cacheable;
  pain at non-hierarchical verbs and mobile round-trips. RPC: internal,
  behavior-shaped, performance-tight. GraphQL: diverse fast-moving clients
  picking field slices; costs caching and abuse surface.
  `primer → RPC/REST` · `bytebytego (idea-only)`
- **Realtime updates** — WebSockets for frequent bidirectional; polling for
  occasional (persistent connections are a continuously-paid resource).
  Push: low latency, you manage fan-out/offline. Pull: simple,
  self-throttling, delayed. `ashishps1 → Tradeoffs`
- **CDN push vs pull** — push for low-traffic/rarely-changing; pull for
  heavy traffic with hot content; staleness-until-TTL is the failure mode.
  `primer → CDN`
- **Never use the database as a message queue** — an entire list section
  devoted to this one rule (lock contention, poor scaling).
  `InterviewReady → Message Queue Antipattern`

## Ch. 02 — ux layer (thin everywhere — flag)

- **Latency budget physics** — memory ~100 ns · SSD ~100 µs ·
  intra-datacenter RTT ~500 µs · disk seek ~10 ms · transcontinental RTT
  ~150 ms. Every ocean-crossing call the UI waits on costs ~150 ms — the
  bottom-up bridge from physics to perceived snappiness. CC BY, directly
  adaptable. `primer → Latency numbers`
- **Optimistic UI** — show the action immediately, finish async; the queue
  trade-off is a UX decision about perceived vs actual completion.
  `primer → Message queues`
- **Consistency level as UX choice** — weak where humans tolerate gaps
  (calls, games), eventual for feeds, strong where users must see their own
  write. `primer → Consistency patterns`
- **Performance is UX** — page-load case studies (Pinterest, BBC, LinkedIn
  Brotli). `awesome-scalability → Performance`

## Ch. 03 — plan

- **Constraint-gathering checklist** (interview framing stripped): who uses
  it, read/write ratio, request volume, data volume, inputs/outputs —
  estimate *before* designing; the latency/powers-of-two tables make it
  minutes. `primer → How to approach / Appendix`
- **Capacity estimation as a named discipline** — canonical source: Jeff
  Dean's numbers; Norvig's latency table. `InterviewReady → Capacity Estimation`
- **Scalability vs performance diagnostic** — slow for one user =
  performance problem; fast for one, slow under load = scalability problem.
  Different fixes; diagnose first. `awesome-scalability → intro`
- **Boring technology scales further** — failure modes already documented;
  avoid over-engineering. `awesome-scalability → Principle`

## Ch. 04 / 05 — agentic patterns (cite Gulli, Springer 2025 — NOT the repo)

The 21-pattern catalog splits cleanly across our chapters. Ch. 04 (team
config): tool use, multi-agent topologies (**coordinator / sequential /
parallel / loop** — a complete minimal vocabulary for team shapes), memory
(session vs persistent; stale memory worse than none), MCP, A2A/agent
cards, human-in-the-loop (design the escalation *trigger*), guardrails
(cheap validators first, LLM-as-guardrail for fuzzy policy), RAG. Ch. 05
(execution): prompt chaining (default decomposable-task pattern), routing
(<2 paths = an if-statement), parallelization, reflection (separate critic
beats self-critique; cap iterations), planning (planner-executor split;
hardcode known workflows), reasoning techniques, learning/adaptation (needs
a fitness signal or it's drift), prioritization, exploration. Ch. 05/07:
evaluation & monitoring (LLM-as-judge — calibrate against human labels
before trusting it as a gate), goal setting (the goal check turns an
infinite loop into a converging one), exception handling (agent-with-
fallback), resource-aware optimization (route by difficulty, budget per
task).

**The book's own mechanism is a composition of three catalog patterns:**
ahead-by-k voting = Parallelization × LLM-as-Judge; the red-team agent =
LLM-as-Guardrail pointed offensively. Reflection is *cooperative* critique;
red-teaming is *adversarial* — same loop, different critic objective.
Honest counterweight to include: ensembles buy small accuracy at large
cost (Huyen) — k and candidate count are cost dials.

## Ch. 02 / 05 / 07 — ML systems thinking (attribute Huyen; no verbatim)

- **Lifecycle is a loop:** setup → data → model → serve, with backward
  edges; design docs should anticipate them. The six setup questions
  (business goal, UX walkthrough of consumption, FP-vs-FN cost, offline +
  online evaluation, personalization granularity, real-world constraints)
  are a ready ADR checklist mapping onto our four layers.
- **Three baselines before any model:** random, human, simple heuristic —
  whatever you build must beat the heuristic by enough to justify its
  complexity. Agent-era translation: a prompt before an agent, an agent
  before a multi-agent system.
- **I/O-schema stability test:** if adding one entity forces full
  retraining, the schema is wrong — reframe (e.g., classify (user, context,
  item) → yes/no instead of softmax over all items).
- **Debugging discipline:** add components one at a time; prove the
  pipeline can overfit 10 examples before trusting it; pin seeds. Eval-era
  analog: *prove the harness can detect a deliberately broken agent before
  trusting green.*
- **Confidence-gated serving:** act on high confidence, escalate the rest —
  the classical ancestor of "ship only when ahead-by-k, escalate ties."
- **Gate launches on controlled experiments, not offline metrics**
  (Booking.com lessons) — the strongest external precedent for eval-gated
  deploys. Model performance ≠ business performance.

## Ch. 07 — ship & operate

- **Deployment strategy menu** (write trade-offs from neutral sources):
  big bang / rolling / blue-green / canary / feature toggle — rollout speed
  vs blast radius vs infra cost vs rollback ease.
- **Resilience pattern canon:** circuit breaker (Fowler's bliki is the
  reference), timeouts, bulkheads, throttling. Case studies: Netflix fault
  tolerance, Shopify's misconfigured circuit breaker.
  `awesome-scalability → Stability`
- **Test the design's failure claims** — Jepsen, TLA+, deterministic
  testing: verify failure behavior, don't hope.
  `InterviewReady → Testing Distributed Systems`
- **Autoscaling** reactive vs predictive (Netflix Scryer; Square's
  queue-depth signal). `awesome-scalability → Autoscaling`

## Canonical further-reading shortlist (per layer)

Data: Kleppmann *DDIA* (the convergence book) · Dynamo paper · Bigtable ·
LSM-tree · Spanner. Communication: Kafka paper · Kreps "The Log" · Airbnb
idempotency · Stripe rate limiters. Application: Raft · Kleppmann on
distributed locking (a model trade-off analysis — teaches *how to reason*).
Ch. 03: Norvig latency numbers · MapReduce. Ch. 07: Fowler CircuitBreaker ·
Twelve-Factor App · Sagas (1987) + transactional outbox.

## Case-study themes for "further reading" boxes

Sharding when one box runs out (Pinterest, Instagram, Notion, Figma) ·
caching fleets and failures (Netflix EVCache, Etsy, DoorDash) · Kafka at
scale (LinkedIn, Uber DLQs, NYT) · monolith→services migrations (Uber,
Tinder, Snap) · observability (Zipkin, Uber, SoundCloud SLO alerting) ·
migrations as cautionary tales / Ch. 06 material (Uber Postgres→MySQL,
Discord on Cassandra, GitHub off Redis). All links in
`awesome-scalability` (MIT).

## Coverage notes

awesome-scalability only ~35% retrievable (fetch cap) — Books/Architecture
sections unverified. karanpratapsingh truncated after Message Queues —
GraphQL/gRPC/websockets/rate-limiting chapters not captured (covered by
other sources above). UX layer: under-served by all repos; seed from
design-specific sources later.
