---
title: Context Loader
chapter: 04
status: reference
tags: [agents, context, adr-006]
---

# Context loader — teaching-block strip (ADR-006)

The Ch. 04 context loader is the named consumer of the teaching-block
convention from [[ADR-006-teaching-block-convention|ADR-006]]. When an agent
loads a dual-purpose file as **task context**, strip instructional callouts;
pass only artifact markdown to the model.

## Strip rule (v1 spec)

**Input:** file path + raw markdown text (already read from disk).

**Output:** artifact-only text for the prompt.

**Algorithm:**

1. If the file is a pure-orientation or pure-decision file (ADR, `00-start-here/`,
   `context/system/sessions/`), return unchanged — no strip.
2. Remove fenced code blocks from consideration only when detecting callouts
   (do not delete code blocks from output).
3. Drop consecutive lines that form an Obsidian callout whose marker is one of:
   - `> [!LEARN]`
   - `> [!TIP]`
   - `> [!TEACH]`
   Include all continuation lines (`> ...`) until a non-`>` line or EOF.
4. Leave all other markdown intact — tables, headings, plain prose, `[!NOTE]`
   and other callout types stay (they are not teaching blocks per ADR-006).

**False-positive guard:** only the three markers above trigger strip. A
`> [!NOTE] Ask your AI agent` prompt stays — it is operational, not bulk
instruction.

## Integration point (v1.5 + Ch. 05)

```
agents/*.yaml context_load_default[]
        +
tasks/*.md  context_load[]
        →  scripts/task_context.py
        →  load_task_context(paths, root)
        →  agent prompt (OpenHands or other execution tool)
```

`scripts/context_loader.py` ships v1.5:

- `strip_teaching_blocks(path, text)` — single-file strip (v1).
- `load_and_strip(path, root=None)` — read from disk + strip.
- `load_task_context(paths[], root=None)` — batch read, strip each file, join
  with `\n\n---\n\n` delimiters for multi-file agent prompts.

`scripts/task_context.py` (Ch. 05) resolves paths from the assigned agent yaml
and the task frontmatter, merges lists (agent defaults first, task paths
append, deduped), then calls `load_task_context`. Documented in
[[openhands]].

```powershell
python scripts/task_context.py 04-your-agents/tasks/01-threat-model-premortem.md
```

Task frontmatter carries `context_load:` — the Layer-3 list beyond agent
defaults. The **Inputs** section in the task body remains human-readable;
keep both in sync when you add or remove inputs.

**Status:** v1.5 live (S11); Ch. 05 wiring live (S12) — eight dual-purpose
files retrofitted with `[!TEACH]` / `[!LEARN]` / `[!TIP]`; golden fixtures in
`scripts/test_context_loader.py`, `scripts/test_task_context.py`, and
`scripts/test_golden_tasks.py` assert loader strip and evaluator path.

## Verification

Given a dual-purpose file with one `[!LEARN]` block and one artifact table,
the stripped output contains the table and none of the callout lines. Given
an ADR, output equals input.
