---
title: Debt Ledger
chapter: 06
status: living
tags: [debt, learning-loop]
---

# Debt ledger

Every entry is a *trigger-based contract*: a known compromise, the condition that
makes it unacceptable, and the planned mitigation. Logged when a trigger fires or
a shortcut is taken knowingly. Pattern inherited from WhiteBoxMAKER, where it
proved to be the working core of the antifragility loop.

Rules: debts are numbered and never reused. Resolving a debt gets a dated note,
not a deletion. Renegotiating a budget or trigger requires explicit human
approval and an entry here.

| ID | Date | Trigger | Debt | Mitigation |
|----|------|---------|------|------------|
| D-001 | 2026-06-10 | Cowork sandbox mount serves stale bytes (NUL-padded / truncated) for files written from the Windows side | git operations from the sandbox can snapshot corrupt content — observed: corrupted `.git/config` on `git init` | All git operations run on Windows only. Sandbox writes go through the shell. `validate_md.py` fails files containing NUL bytes. *Fired 2026-06-11: trailing NUL padding on 4 files (ADR-002/003/004, ux-heuristics-seed); content intact, padding stripped, validator re-run clean.* |
| D-002 | 2026-06-10 | Session-1 docs imported verbatim — sub-structure below `##` level left as plain text | Sub-sections not targetable by outline or `vault_patch` | Promote sub-labels to `###` on first deep edit of each doc. |
| D-003 | 2026-06-10 | `validate_md.py` checks syntax only | Wiki-links to nonexistent notes pass the commit gate | Add link-resolution check when chapters begin cross-linking (Ch. 01 onward). *Resolved 2026-06-11 (S9): `scripts/md_checks/link_resolution.py` resolves `[[wiki-links]]` (incl. `\|alias`, `#heading`) against note stems case-insensitively; skips code fences and placeholder stems. Runs on `--all` only (full note index built once per run); pre-commit fast path unchanged. Verified clean on active corpus.* |
| D-004 | 2026-06-10 | STATE.md is updated manually at session close | One skipped update = disoriented next session | If two sessions close without an update, automate (scheduled task or commit hook reminder). |
| D-005 | 2026-06-11 | Cache failure modes in `02-design/layers/data.md` derive from an NC-ND source (idea-only re-expression) | Specifics (stampede/jitter, bloom filters, hot keys) not yet re-verified against primary vendor docs | Acceptable for internal use; re-verify against vendor documentation before any external publication of Ch. 02. Inline note present in data.md. |
| D-007 | 2026-06-11 | The now-live budget enforcement (D-006) immediately flagged `context/system/book-architecture.md` at 201 lines vs the 150-line Layer-1 budget — over by 34%, a hard FAIL | `validate_md.py --all` reported one failure on the enforcement's first run | **Budget renegotiated, not suppressed (S8, Alex-approved — this entry is the required record):** Layer-1 line budget raised 150 → 200 in `constraints/global.md` and `validate_md.py`. Rationale: book-architecture.md is the structural-conventions reference and is legitimately the densest active context file (others are 71/86/119); 200 is the natural next step in the 60/100/150/300 budget family. Effect: book-architecture.md (201) now sits in the ≤5% grace band → WARN, so `--all` is green while the file stays visibly at the edge. Trade-off accepted: this loosens the ceiling for *all* Layer-1 files to 200. Decomposition remains the cleaner long-term fix if the file grows further. |
| D-006 | 2026-06-11 | `constraints/global.md` declares line/node budgets (task ≤100, layer ≤150, module ≤300, agent-yaml ≤60, Mermaid ≤20) but `validate_md.py` enforces none of them | A file can silently exceed a budget — the "split/renegotiate trigger" never fires; same flavor as D-003 (link resolution). Surfaced by the S7 critical analysis | Add budget + unfilled-placeholder checks to the validator with the ≤5%-warn / >5%-block rule (thread T7); until shipped, budgets are review-enforced. *Resolved 2026-06-11 (S8): `validate_md.py` now enforces all four line budgets + the ≤20-node Mermaid budget with the grace band; path→budget glob map declared at the top of the script; grace-band note added to `constraints/global.md` in the same commit; fixtures (3% warn / 10% block / 21-node flag) pass. The unfilled-`[placeholder]` check stays open under T7.* |
