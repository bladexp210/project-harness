#!/usr/bin/env python3
"""Assemble ADR-006-stripped agent context for a TASK.md execution path.

Merge order: agent yaml context_load_default, then task frontmatter
context_load (deduped, first wins).

Usage:
  python scripts/task_context.py 04-your-agents/tasks/01-threat-model-premortem.md
  python -c "from task_context import build_task_context; ..."
"""
from __future__ import annotations

import pathlib
import re
import sys

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

from context_loader import load_task_context

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

FRONTMATTER_RE = re.compile(r"^---\s*\n(.*?)\n---", re.S)


def _repo_root() -> pathlib.Path:
    return pathlib.Path(__file__).resolve().parents[1]


def parse_frontmatter(text: str) -> dict:
    """Return yaml mapping from leading frontmatter, or {}."""
    m = FRONTMATTER_RE.match(text)
    if not m or yaml is None:
        return {}
    data = yaml.safe_load(m.group(1))
    return data if isinstance(data, dict) else {}


def parse_yaml_file(text: str) -> dict:
    """Parse a .yaml agent definition (no markdown frontmatter fences)."""
    if yaml is None:
        return {}
    data = yaml.safe_load(text)
    return data if isinstance(data, dict) else {}


def resolve_agent_yaml(agent: str, root: pathlib.Path) -> pathlib.Path:
    """Map task `agent` field to agents/*.yaml (e.g. red-team → red-team-agent.yaml)."""
    agents_dir = root / "04-your-agents" / "agents"
    for name in (f"{agent}.yaml", f"{agent}-agent.yaml"):
        path = agents_dir / name
        if path.is_file():
            return path
    raise FileNotFoundError(
        "no agent yaml for {!r} under {}".format(agent, agents_dir.as_posix())
    )


def merge_context_paths(agent_paths: list[str], task_paths: list[str]) -> list[str]:
    """Union with stable order: agent defaults first, task paths append."""
    seen: set[str] = set()
    merged: list[str] = []
    for path in list(agent_paths) + list(task_paths):
        norm = path.replace("\\", "/")
        if norm not in seen:
            seen.add(norm)
            merged.append(norm)
    return merged


def resolve_context_paths(
    task_path: str | pathlib.Path,
    root: str | pathlib.Path | None = None,
) -> list[str]:
    """Return merged context_load paths for a task file."""
    root_path = pathlib.Path(root) if root is not None else _repo_root()
    task_file = pathlib.Path(task_path)
    if not task_file.is_absolute():
        task_file = root_path / task_file
    text = task_file.read_text(encoding="utf-8")
    meta = parse_frontmatter(text)

    agent_key = meta.get("agent")
    if not agent_key:
        raise ValueError("task frontmatter missing 'agent': {}".format(task_file))

    agent_yaml = resolve_agent_yaml(str(agent_key), root_path)
    agent_meta = parse_yaml_file(agent_yaml.read_text(encoding="utf-8"))
    agent_paths = agent_meta.get("context_load_default") or []
    if not isinstance(agent_paths, list):
        agent_paths = []

    task_paths = meta.get("context_load") or []
    if not isinstance(task_paths, list):
        task_paths = []

    return merge_context_paths(agent_paths, task_paths)


def build_task_context(
    task_path: str | pathlib.Path,
    root: str | pathlib.Path | None = None,
) -> str:
    """Read agent + task context_load lists; return stripped prompt markdown."""
    root_path = pathlib.Path(root) if root is not None else _repo_root()
    paths = resolve_context_paths(task_path, root_path)
    return load_task_context(paths, root_path)


def main(argv: list[str] | None = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if not args:
        print(
            "usage: task_context.py <task.md> [task2.md ...]",
            file=sys.stderr,
        )
        return 2
    if yaml is None:
        print("task_context.py requires PyYAML (pip install pyyaml)", file=sys.stderr)
        return 2
    root = _repo_root()
    for arg in args:
        sys.stdout.write(build_task_context(arg, root))
        if len(args) > 1:
            sys.stdout.write("\n\n===\n\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
