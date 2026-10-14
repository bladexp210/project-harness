"""Temporal awareness — canon freshness, human-gate detection, metrics."""

from __future__ import annotations

import re
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

REPO_ROOT = Path(__file__).resolve().parents[2]

CANON_FILES = (
    REPO_ROOT / "STATE.md",
    REPO_ROOT / "_index" / "dashboard" / "01-context.md",
    REPO_ROOT / "_index" / "dashboard" / "02-containers.md",
    REPO_ROOT / "_index" / "dashboard" / "03-components.md",
)

STALE_THRESHOLD = timedelta(hours=24)

PROCEED_PATTERN = re.compile(r"\bproceed\b", re.IGNORECASE)
MERGE_PROMPT_PATTERN = re.compile(
    r"\b(merge|merged|merging)\b.*\b(main|branch|session)\b|\bgit\s+merge\b",
    re.IGNORECASE,
)
MERGE_SHELL_PATTERN = re.compile(r"\bgit\s+merge\b", re.IGNORECASE)

TEMPORAL_EVENTS = frozenset(
    {
        "sessionStart",
        "beforeSubmitPrompt",
        "afterAgentResponse",
        "stop",
        "sessionEnd",
    }
)


@dataclass
class FreshnessReport:
    checked_at: str
    stale_files: list[str]
    banner: str | None

    def to_dict(self) -> dict[str, Any]:
        return {
            "checked_at": self.checked_at,
            "stale_files": self.stale_files,
            "banner": self.banner,
        }


def parse_frontmatter_updated(path: Path) -> datetime | None:
    if not path.is_file():
        return None
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return None
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return None
    block = text[3:end]
    for line in block.splitlines():
        if line.strip().lower().startswith("updated:"):
            raw = line.split(":", 1)[1].strip()
            try:
                return datetime.strptime(raw, "%Y-%m-%d %H:%M").replace(
                    tzinfo=timezone.utc
                )
            except ValueError:
                return None
    return None


def _path_label(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.name


def check_canon_freshness(at: datetime | None = None) -> FreshnessReport:
    now = at or datetime.now(timezone.utc)
    checked_at = now.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    stale: list[str] = []
    for path in CANON_FILES:
        updated = parse_frontmatter_updated(path)
        if updated is None:
            stale.append(_path_label(path))
            continue
        age = now - updated
        if age > STALE_THRESHOLD:
            stale.append(_path_label(path))
    banner = None
    if stale:
        names = ", ".join(stale)
        banner = (
            f"[canon-freshness] Stale handoff docs (>{int(STALE_THRESHOLD.total_seconds() // 3600)}h): "
            f"{names}. Refresh STATE + dashboard before merge."
        )
    return FreshnessReport(checked_at=checked_at, stale_files=stale, banner=banner)


def extract_prompt_text(hook_input: dict[str, Any]) -> str:
    for key in ("prompt", "text", "message", "content"):
        val = hook_input.get(key)
        if isinstance(val, str):
            return val
    return ""


def extract_shell_command(hook_input: dict[str, Any]) -> str:
    for key in ("command", "cmd", "shell_command"):
        val = hook_input.get(key)
        if isinstance(val, str):
            return val
    return ""


def detect_human_gate(hook_event: str, hook_input: dict[str, Any]) -> str | None:
    if hook_event == "beforeSubmitPrompt":
        text = extract_prompt_text(hook_input)
        if PROCEED_PATTERN.search(text):
            return "proceed"
        if MERGE_PROMPT_PATTERN.search(text):
            return "merge"
    if hook_event == "beforeShellExecution":
        cmd = extract_shell_command(hook_input)
        if MERGE_SHELL_PATTERN.search(cmd):
            return "merge"
    return None


def compute_metrics(events: list[dict[str, Any]]) -> dict[str, Any]:
    """Derive duration, mean human latency, and decision count from timeline rows."""
    by_event: dict[str, list[str]] = {}
    gate_times: list[str] = []
    latencies_ms: list[float] = []
    last_stop: str | None = None

    for row in events:
        event = row.get("event", "")
        at = row.get("at", "")
        if not at:
            continue
        by_event.setdefault(event, []).append(at)
        if event in {"afterAgentResponse", "stop"}:
            last_stop = at
        if event == "beforeSubmitPrompt" and last_stop:
            latencies_ms.append(_delta_ms(last_stop, at))
            last_stop = None
        if event.startswith("human_gate."):
            gate_times.append(at)

    started = (by_event.get("sessionStart") or [None])[0]
    ended = (by_event.get("sessionEnd") or [None])[-1]
    duration_ms = _delta_ms(started, ended) if started and ended else None

    mean_latency = None
    if latencies_ms:
        mean_latency = sum(latencies_ms) / len(latencies_ms)

    return {
        "session_duration_ms": duration_ms,
        "mean_human_latency_ms": mean_latency,
        "decision_count": len(gate_times),
        "prompt_count": len(by_event.get("beforeSubmitPrompt", [])),
    }


def _delta_ms(start: str | None, end: str | None) -> float | None:
    if not start or not end:
        return None
    try:
        a = datetime.fromisoformat(start.replace("Z", "+00:00"))
        b = datetime.fromisoformat(end.replace("Z", "+00:00"))
        return (b - a).total_seconds() * 1000.0
    except ValueError:
        return None
