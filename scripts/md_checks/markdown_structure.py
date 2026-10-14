"""Markdown structure checks — tables and fenced blocks.

GFM/Obsidian tables require consecutive pipe rows; a blank line between rows
ends the table and each row renders as plain text. Some editors also insert
blank lines inside YAML frontmatter or mermaid fences — tables and diagrams
break silently.
"""
from __future__ import annotations

import re

TABLE_ROW = re.compile(r"^\|.+\|$")
SEPARATOR_ROW = re.compile(r"^\|[\s:|\-]+\|$")
MERMAID_BLOCK = re.compile(r"```mermaid\s*\n(.*?)```", re.S)
FENCE = re.compile(r"^```", re.M)
WIKI_LINK = re.compile(r"\[\[[^\]]+\]\]")
UNESCAPED_ALIAS_PIPE = re.compile(r"(?<!\\)\|")


def check_markdown_structure(text: str) -> list[str]:
    """Return error strings for table / mermaid formatting defects."""
    errors: list[str] = []
    errors.extend(_check_table_continuity(text))
    errors.extend(_check_table_wikilink_aliases(text))
    errors.extend(_check_mermaid_blank_lines(text))
    return errors


def _check_table_continuity(text: str) -> list[str]:
    """Blank lines *inside* one table break GFM/Obsidian rendering.

    Two separate tables may sit back-to-back; we only fail when the row after
    the blank is an alignment separator, or the row before is a separator.
    """
    errors: list[str] = []
    lines = text.splitlines()
    for i in range(len(lines) - 2):
        if lines[i + 1].strip() != "":
            continue
        prev_row = lines[i]
        next_row = lines[i + 2]
        if not TABLE_ROW.match(prev_row) or not TABLE_ROW.match(next_row):
            continue
        prev_sep = bool(SEPARATOR_ROW.match(prev_row))
        next_sep = bool(SEPARATOR_ROW.match(next_row))
        if prev_sep or next_sep:
            line_no = i + 2
            errors.append(
                "blank line inside markdown table (near line {}) breaks rendering "
                "in Obsidian/GFM — table rows must be consecutive".format(line_no)
            )
            break
    return errors


def _check_table_wikilink_aliases(text: str) -> list[str]:
    """Aliased wiki-links in GFM tables need an escaped pipe (Obsidian rule).

    ``[[target|alias]]`` on a table row splits the cell at ``|``; use
    ``[[target\\|alias]]`` or ``[[target]]`` without an alias.
    """
    errors: list[str] = []
    in_fence = False
    for i, line in enumerate(text.splitlines(), 1):
        if FENCE.match(line.strip()):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        stripped = line.strip()
        if not TABLE_ROW.match(stripped):
            continue
        for match in WIKI_LINK.finditer(line):
            inner = match.group(0)[2:-2]
            if UNESCAPED_ALIAS_PIPE.search(inner):
                errors.append(
                    "line {}: aliased wiki-link in table row — use [[stem]] or "
                    "[[stem\\|alias]] (Obsidian table rule)".format(i)
                )
                break
    return errors


def _check_mermaid_blank_lines(text: str) -> list[str]:
    errors: list[str] = []
    for idx, block in enumerate(MERMAID_BLOCK.findall(text), 1):
        lines = block.splitlines()
        if len(lines) < 3:
            continue
        blank = sum(1 for ln in lines if not ln.strip())
        content = len(lines) - blank
        if content >= 3 and blank >= 2 and blank >= content - 1:
            errors.append(
                "mermaid block {} has blank lines between most syntax lines "
                "— diagram may not render; remove empty lines inside fence".format(idx)
            )
    return errors
