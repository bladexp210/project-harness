#!/usr/bin/env python3
"""Strip ADR-006 teaching blocks from dual-purpose markdown (Ch. 04 spec).

Spec: 04-your-agents/context-loader.md
Usage:
  python scripts/context_loader.py path/to/file.md
  python -c "from context_loader import strip_teaching_blocks; ..."
"""
from __future__ import annotations

import pathlib
import re
import sys

TEACHING_MARKERS = ("[!LEARN]", "[!TIP]", "[!TEACH]")
CALLOUT_RE = re.compile(r"^>\s*\[!(\w+)\]")


def _posix_path(path: str | pathlib.Path) -> str:
    return str(path).replace("\\", "/")


def _is_exempt(path: str | pathlib.Path) -> bool:
    """Pure-orientation or pure-decision files pass through unchanged."""
    p = _posix_path(path)
    if "/00-start-here/" in p or p.startswith("00-start-here/"):
        return True
    if "/context/system/sessions/" in p or p.startswith("context/system/sessions/"):
        return True
    if "/decisions/ADR-" in p or re.search(r"(^|/)decisions/ADR-\d+", p):
        return True
    return False


def _is_teaching_callout(line: str) -> bool:
    m = CALLOUT_RE.match(line)
    if not m:
        return False
    marker = "[!{}]".format(m.group(1).upper())
    return marker in TEACHING_MARKERS


def _in_code_fence(line: str, inside_fence: bool) -> bool:
    stripped = line.strip()
    if stripped.startswith("```"):
        return not inside_fence
    return inside_fence


def strip_teaching_blocks(path: str | pathlib.Path, text: str) -> str:
    """Return artifact-only markdown for agent prompts."""
    if _is_exempt(path):
        return text

    lines = text.splitlines(keepends=True)
    out: list[str] = []
    i = 0
    inside_fence = False

    while i < len(lines):
        line = lines[i]
        inside_fence = _in_code_fence(line, inside_fence)

        if not inside_fence and _is_teaching_callout(line):
            i += 1
            while i < len(lines) and lines[i].startswith(">"):
                i += 1
            continue

        out.append(line)
        i += 1

    return "".join(out)


def load_and_strip(path: str | pathlib.Path, root: str | pathlib.Path | None = None) -> str:
    """Read a file from disk and strip teaching blocks."""
    p = pathlib.Path(path)
    if root is not None:
        p = pathlib.Path(root) / p
    text = p.read_text(encoding="utf-8")
    rel = p.as_posix()
    if root is not None:
        try:
            rel = p.relative_to(pathlib.Path(root)).as_posix()
        except ValueError:
            pass
    return strip_teaching_blocks(rel, text)


def load_task_context(
    paths: list[str | pathlib.Path],
    root: str | pathlib.Path | None = None,
    *,
    separator: str = "\n\n---\n\n",
) -> str:
    """Batch-read paths and return artifact-only markdown for agent prompts.

    Matches task.context_load[] in 04-your-agents/context-loader.md: each path
    is read, teaching blocks stripped, then joined with a file delimiter.
    """
    if not paths:
        return ""
    chunks = [load_and_strip(path, root) for path in paths]
    return separator.join(chunks)


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if not args:
        print("usage: context_loader.py <file.md> [file2.md ...]", file=sys.stderr)
        return 2
    for arg in args:
        text = load_and_strip(arg)
        sys.stdout.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
