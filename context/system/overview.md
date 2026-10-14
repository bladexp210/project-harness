---
title: System Overview
layer: 1-system
status: reference
tags: [system, overview, dimensions]
---

# The System Being Documented

This file is the concise reference for AI agents writing any chapter of the book. For full architectural detail see [session-docs](session-docs.md).

---

## Core Principles

- **Human-supervised, design-first** — the human orchestrates and approves; agents execute bounded tasks  
- **Vendor-agnostic** — no lock-in to any provider, tool, or CLI  
- **Antifragile** — failures feed back into system improvement; the system gets harder to fail the same way twice  
- **Layered context** — agents load only what their task requires, not everything

---

## The Nine Dimensions

**1 — LLM Routing** LiteLLM (proxy) + OpenRouter (provider). Per-agent virtual keys with hard token budgets. Automatic fallbacks. One config line routes all traces to Langfuse. Model selection is on the **complexity axis**: simple task → cheap model, complex → frontier.

**2 — Tracing** Langfuse (self-hosted). Every LLM call, tool use, and agent decision captured as spans. Cost attribution per agent. Feeds A/B testing. Integrates with LiteLLM via one config line.

**3 — Isolation** OpenHands (Docker runtime) + git bare repo + worktrees. Two independent layers: Docker isolates process/filesystem; worktrees isolate git state (own branch, own index, own HEAD). A branch cannot be checked out in two worktrees simultaneously — git enforces this.

**4 — Blast Radius** Six-layer stack: (1) deep task decomposition (scope), (2) worktrees (git), (3) Docker containers (runtime), (4) LiteLLM budget (financial), (5) OpenHands max_iterations (loops), (6) atomic commits (recovery). Each layer addresses a different moment in the failure path.

**5 — Hooks** pre-commit framework + LiteLLM callbacks. Most hooks already exist as community plugins (gitleaks, ruff, conventional-pre-commit). One custom script: scope-enforcement (~15 lines bash). Git hooks fire at commit time regardless of which process triggers the commit — no bypass possible.

**6 — Post-mortems** Langfuse (forensics) + rohansx/reflect MCP (cross-session memory) + committed template. Langfuse shows what happened. reflect stores lessons in SQLite, retrieved automatically on similar future tasks. The human is the post-mortem agent in this human-supervised system.

**7 — Composability** YAML agent definitions in agents/. LLM assignment via LiteLLM model aliases — decoupled from role definitions. Forking a role = copy YAML, change 3 fields, ~5 minutes. Specialist roles fork from tester-agent.yaml.

**8 — A/B Testing** Langfuse experiment runner. Selective — not systematic. Two triggers: judgment ("I cannot articulate why A beats B") and process (flagged in TASK.md at planning time). Evaluator agent scores options. Results feed ADRs. Used as k-voting tiebreaker when margin is insufficient.

**9 — Design-first Workflow** The most important dimension. Everything downstream depends on its quality.

Core structure: **Exploration-Execution loops**. Design tasks have many exploration loops (expensive models, produce ADRs). Implementation tasks have minimal exploration (boilerplate covers it, cheap models, produce code).

Two independent axes:

- **Complexity axis** → model selection (simple: fast-llm, complex: frontier-llm)  
- **Criticality axis** → k threshold (k = required winning margin, not number of agents)

**WhiteBoxMAKER** (ahead-by-k voting + red-teaming): k is the margin by which the winning solution must beat second place. k=1: any lead wins. k=5: near-unanimity. Red-team agent challenges decisions before they are made.

**Three-layer context** (C4 × Depth of Knowledge):

- Layer 1 — System (always loaded, all agents, small)  
- Layer 2 — Architecture (loaded by domain, deterministic)  
- Layer 3 — Task (TASK.md + specific files + reflect lessons) Context loaded deterministically — TASK.md lists exactly which files to load.

---

## The Book's Audience

Anyone who wants to build a software product using AI, regardless of technical background. The structure compensates for varying expertise — guardrails for novices, flexibility for experts.

## The Dual Path

Every technically demanding section offers:

- **Scaffold path** (default): what, why, step-by-step, what's happening underneath  
- **Fast track**: brief + command + "You own the outcome"

See [book-architecture](book-architecture.md) for Obsidian callout implementation.  
