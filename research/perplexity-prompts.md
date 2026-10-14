---
title: "Perplexity deep-research prompts for thin coverage areas"
status: reference
date: 2026-06-10
tags: [research, prompts]
---

# Perplexity prompts — thin-coverage research

Three gaps identified after the company-framework and system-design seeds:
UX/UI (thin in all backend-centric sources), product sunset (zero coverage
anywhere), and requirements discovery (Ch. 01; the company framework assumes
requirements arrive pre-made). **Prompt 4** (2026-06-12): modeling notation
selection, combination rules, and session visualization — see
[[model-visualization-research-brief]]. Paste each prompt into Perplexity deep
research. Results land in `_inbox/`, then get distilled into `research/`
seeds with provenance.

---

## Prompt 1 — UX/UI best-in-class practices

```text
I'm writing a methodology guide for building software with AI assistance.
The audience includes complete novices. I need a research report on
best-in-class UX and UI design practices, with a focus on DECISION
HEURISTICS (when to choose X over Y, and what tips the decision) rather
than visual trends.

Cover:
1. Foundational frameworks with strong evidence bases: Nielsen's usability
   heuristics, Norman's design principles, WCAG 2.1 AA accessibility, Fitts's
   and Hick's laws and their practical thresholds.
2. Design-system thinking: when to adopt an existing component library vs
   build one; design tokens; consistency rules that survive scaling.
3. UX patterns for system states: loading, empty, error, success, offline,
   optimistic UI; perceived performance techniques and the latency
   thresholds users actually notice (cite the research, e.g. 100ms/1s/10s).
4. Information architecture and user-flow design: how experts decide
   navigation depth, progressive disclosure, and form design rules.
5. UX specifically for AI-powered products: designing for non-deterministic
   outputs, confidence display, human-in-the-loop interfaces, undo/recovery
   as first-class citizens. Reference published guidelines from major AI
   product teams (e.g. Google PAIR, Microsoft HAX, Apple HIG for ML).
6. How modern teams validate UX cheaply: usability test sizes (5-user
   rule and its criticisms), A/B vs qualitative, accessibility audits.

For each practice: state the rule, the evidence or source behind it, when
it does NOT apply, and the trade-off it resolves. Prefer primary sources
(NN/g, W3C, published research, vendor design guidelines) over blog
aggregators. Include a source list with links. Exclude: visual trend
articles, tool tutorials, listicles without sources.
```

## Prompt 2 — Product sunset, decommissioning, end-of-life

```text
I'm writing a methodology guide covering the FULL software lifecycle,
including the phase almost nobody documents: sunsetting a product. I need
a research report on best practices for software product end-of-life,
decommissioning, and graceful shutdown.

Cover:
1. Deciding WHEN to sunset: cost/usage signals, portfolio review
   frameworks, kill criteria defined at launch ("pre-registered" shutdown
   conditions). How companies like Google, Microsoft, Atlassian, and SaaS
   vendors structure end-of-life policies and deprecation timelines.
2. User obligations: notice periods (legal and contractual norms by
   region), data export rights (GDPR data portability and equivalents),
   migration paths, refund handling, API deprecation best practices
   (versioning, sunset HTTP headers, RFC 8594).
3. Technical decommissioning: data retention vs deletion schedules,
   credential and secret revocation, DNS and certificate cleanup,
   archive formats that stay readable, license cleanup for dependencies.
4. Organizational: final post-mortem / retrospective practices, knowledge
   preservation, what to keep for legal hold, communicating internally.
5. Designing FOR sunset from day one: architecture choices that make
   export and shutdown cheap (data portability by design, avoiding
   vendor lock-in for the customer's data).
6. Documented case studies of well-handled and badly-handled product
   shutdowns and what each did right or wrong.

For each practice: the rule, the source, the trade-off, and any concrete
numbers (notice period norms, retention durations). Prefer primary sources:
RFCs, regulator guidance, vendor EOL policy pages, engineering blog
retrospectives. Include a source list with links.
```

## Prompt 3 — Requirements discovery and user research for builders

```text
I'm writing a methodology guide for building software with AI assistance;
its first chapter teaches readers (including non-technical founders) to
discover user roles and use cases BEFORE designing anything. I need a
research report on evidence-based requirements-discovery and early user
research methods.

Cover:
1. The canonical frameworks and their decision boundaries: Jobs-to-be-Done
   vs personas vs user-role modeling — when each works and when each
   misleads; user story mapping (Patton); impact mapping; event storming
   for domain discovery.
2. Prioritization methods compared with their failure modes: RICE, MoSCoW,
   Kano model, weighted shortest job first, frequency × importance
   matrices. What does research and practitioner consensus say about which
   work at small scale?
3. Validation before building: Mom Test interviewing rules, problem vs
   solution interviews, signal strength hierarchies (interest <
   commitment < payment), minimum viable tests and smoke tests.
4. Common failure modes: confirmation bias in interviews, listening to
   loudest users, feature-request laundering, over-segmentation.
5. How AI changes discovery: using LLMs to synthesize interview data,
   simulate user segments (and the documented risks of synthetic users),
   accelerate competitive analysis — with published evaluations where
   they exist.
6. Operational and non-functional roles people forget: the operator,
   the support agent, the data-deletion requester — how mature teams
   capture non-feature requirements (compliance, accessibility,
   operability) as first-class use cases.

For each method: what it is, the evidence or origin, when NOT to use it,
and the trade-off it resolves. Prefer primary sources (original books,
published studies, well-documented practitioner writing). Include a source
list with links. Exclude: generic agile ceremony descriptions, tool ads.
```

---

## Prompt 4 — Modeling notation selection, combinations, and session visualization

**Brief:** [[model-visualization-research-brief]] · playground catalog:
`_playground/diagram-taxonomy.md` v0.2.

```text
I'm writing a methodology guide ("book-as-folder-structure") for building
software with AI assistance. The audience includes complete novices, seasoned
developers, and many readers for whom English is a third language — visuals
must reduce cognitive load, not add prose to parse.

We are designing WHICH modeling notations to teach and WHEN to combine them.
We are NOT obliged to use every diagram from every standard — we want a
minimal, evidence-based set plus explicit combination rules. Separate two
tracks in your answer:

  A) PRODUCT visuals — the reader's software (design → plan → build → learn)
  B) SESSION visuals — human+AI work on the methodology repo itself
     (bootstrap, build, review, close, handoff). These must NOT be confused
     with product BPMN/workflow diagrams.

CONTEXT WE ALREADY USE (challenge or confirm — do not assume all are correct):

  • C4 Model: four STATIC diagrams only (System Context, Container,
    Component, Code) — C4 is NOT flowcharts
  • UML 2: sequence and state in layer files; class/component where needed
  • BPMN 2.0: process, collaboration, choreography, conversation (full BPMN2,
    not informal "lite" unless you justify a subset with evidence)
  • IDEF0 / IDEF3: function decomposition and process precedence
  • ER diagrams: data layer
  • DMN: decision tables and decision requirements
  • Book conventions: ICOM frame (Inputs/Controls/Mechanisms/Outputs) + Gherkin
    for single-sitting tasks; one task = one agent/human/script execution
  • Zoom levels for product work: L1 system context → L2 containers →
    L3 component OR multi-step workflow → L4 code/task (one sitting)
  • Three diagram families: static (structure), dynamic (behaviour/process),
    decision (rules)

RESEARCH QUESTIONS — cover all:

1. INVENTORY AND SELECTION
   For each major notation family (C4, UML, BPMN2, IDEF, ER, DMN, plus
   credible alternatives: event storming, user story mapping as visual,
   ArchiMate, SysML, Wardley maps, Petri nets, DDD context maps, etc.):
   - What question does it answer best?
   - What is it bad at or misleading for?
   - Minimum audience skill to read it?
   - Primary sources (books, OMG specs, Simon Brown C4, etc.)

2. MINIMAL SUFFICIENT SET
   For a methodology book teaching design-first, agent-executed, bounded
   tasks with human review gates: which 5–8 diagram TYPES (not necessarily
   5–8 models) should be default, and which should be "appendix / optional"?
   Justify with practitioner consensus or studies where they exist.

3. COMBINATION RULES
   When is it correct to place TWO diagram types on the same view or page?
   Provide a combination matrix with:
   - Allowed pairs (e.g. BPMN2 process + DMN at gateway; C4 Container + ER)
   - Forbidden or noisy pairs and why
   - "Primary + inset" patterns (main diagram + small secondary)
   Cite examples from published architecture docs or standards if available.

4. LEVEL PLACEMENT
   At which zoom/granularity does each diagram type belong?
   Explicitly address: task-level (one sitting) vs workflow-level (many tasks)
   vs container-level vs system context. We place tasks at the finest grain
   (L4) and multi-task workflows at L3 — validate or challenge this with
   evidence.

5. AI-ASSISTED DEVELOPMENT
   How do teams document agent/human pair work, context loading, review
   gates, and bounded task execution visually? Search for: AI pair
   programming workflows, human-in-the-loop diagrams, LLM agent orchestration
   visuals, "spec-driven" or "contract-first" agent task specs. What transfers
   to a book where agents read markdown context files and humans commit on
   Windows?

6. SESSION / HANDOFF VISUALIZATION (track B)
   Separate from product BPMN: how do effective teams visualize
   - sprint/session status
   - work-in-progress limits
   - handoff between people or agents
   - "where am I in the doc/repo" orientation
   Consider: Kanban, cumulative flow, status tables, C4 misapplied to
   sessions, roadmap vs operational dashboard. Recommend a session visual
   model for: bootstrap → build → validate → human review → merge → close.
   Audience includes readers who lose place between tasks.

7. ESL, NOVICE, AND COGNITIVE LOAD
   What does UX/visualization research say about diagram complexity for
   non-native English readers and novices? Short labels vs sentences,
   dual coding (visual + text), progressive disclosure of notation.
   Recommend rules for maximum label length, legend requirements, and
   when to use HTML/interactive vs static figures.

8. HYBRID AND NON-STANDARD VIEWS
   When do teams invent hybrid notations (C4 + icons, BPMN + ADR links,
   ICOM + IDEF0 on one page) successfully? When does hybrid fail?
   We may define book-specific views if standards are too heavy — what
   are precedents?

9. RENDERING AND TOOLING (secondary — brief)
   We publish Obsidian markdown + optional static HTML; Mermaid renders many
   but not IDEF0 four-sided boxes or full BPMN2. Summarize trade-offs only;
   do not make tool choice the main answer.

10. FAILURE MODES AND CRITICISM
    For each recommended practice: failure condition (when it misleads),
    known criticism, and lighter alternative.

OUTPUT FORMAT:

  • Executive summary (≤ 15 bullets)
  • Track A: product visualization recommendations
  • Track B: session visualization recommendations
  • Combination matrix (table)
  • Minimal default set vs optional appendix (table)
  • Annotated bibliography with links (prefer primary: OMG, W3C, NN/g,
    Simon Brown, Fowler, BPMN spec, academic surveys)
  • Explicit list of recommendations we should DROP from our current catalog
    if evidence says they add noise

Exclude: tool marketing, "best diagrams" listicles without sources, generic
Agile ceremony posters. Include: evidence-based UX for technical diagrams,
architecture-as-code community practice, and AI agent workflow documentation
where published.
```

**After run:** raw → `_inbox/` → distill to `research/model-visualization-seed.md`.

---

## Red-team note

For the separate red-team seed you're generating: consider appending this
line to whichever prompt you use — "Then, acting as a critic, list the
strongest published arguments AGAINST the practices above: where have these
methods failed, what do their critics say, and which have weak evidence
bases?" That turns each report into its own adversarial source, which is
what the red-team agent will want when challenging the layer files.
