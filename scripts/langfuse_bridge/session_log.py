"""Dual-write session log — `logs/sessions/<id>.md` (gitignored runtime)."""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from langfuse_bridge.ingest import utc_now_iso
from langfuse_bridge.temporal import FreshnessReport, compute_metrics

REPO_ROOT = Path(__file__).resolve().parents[2]
LOGS_DIR = REPO_ROOT / "logs" / "sessions"
META_SUFFIX = ".meta.json"


def safe_log_stem(session_id: str) -> str:
    cleaned = re.sub(r"[^\w\-]", "_", session_id.strip())
    return cleaned[:64] or "unknown"


def log_path(session_id: str) -> Path:
    return LOGS_DIR / f"{safe_log_stem(session_id)}.md"


def meta_path(session_id: str) -> Path:
    return LOGS_DIR / f"{safe_log_stem(session_id)}{META_SUFFIX}"


def _read_meta(session_id: str) -> dict[str, Any]:
    path = meta_path(session_id)
    if not path.is_file():
        return {"timeline": [], "gates": []}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return {"timeline": [], "gates": []}


def _write_meta(session_id: str, meta: dict[str, Any]) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    meta_path(session_id).write_text(json.dumps(meta, indent=2), encoding="utf-8")


def init_log(session_id: str, started_at: str, freshness: FreshnessReport) -> None:
    LOGS_DIR.mkdir(parents=True, exist_ok=True)
    meta = {
        "session_id": session_id,
        "started_at": started_at,
        "timeline": [
            {
                "at": started_at,
                "event": "sessionStart",
                "source": "hook",
                "detail": "session opened",
            }
        ],
        "gates": [],
        "canon_freshness": freshness.to_dict(),
    }
    _write_meta(session_id, meta)
    _render(session_id, meta)


def append_timeline(
    session_id: str,
    event: str,
    source: str = "hook",
    detail: str = "",
    at: str | None = None,
) -> None:
    meta = _read_meta(session_id)
    if not meta.get("session_id"):
        meta["session_id"] = session_id
    ts = at or utc_now_iso()
    meta.setdefault("timeline", []).append(
        {"at": ts, "event": event, "source": source, "detail": detail}
    )
    _write_meta(session_id, meta)
    _render(session_id, meta)


def append_human_gate(
    session_id: str,
    gate: str,
    source: str,
    note: str = "",
    at: str | None = None,
) -> None:
    meta = _read_meta(session_id)
    ts = at or utc_now_iso()
    gate_row = {"at": ts, "gate": gate, "source": source, "note": note}
    meta.setdefault("gates", []).append(gate_row)
    meta.setdefault("timeline", []).append(
        {
            "at": ts,
            "event": f"human_gate.{gate}",
            "source": source,
            "detail": note or gate,
        }
    )
    _write_meta(session_id, meta)
    _render(session_id, meta)


def finalize_log(session_id: str, ended_at: str | None = None) -> dict[str, Any]:
    meta = _read_meta(session_id)
    end = ended_at or utc_now_iso()
    meta["ended_at"] = end
    meta.setdefault("timeline", []).append(
        {
            "at": end,
            "event": "sessionEnd",
            "source": "hook",
            "detail": "session closed",
        }
    )
    metrics = compute_metrics(meta.get("timeline", []))
    meta["metrics"] = metrics
    _write_meta(session_id, meta)
    _render(session_id, meta)
    return metrics


def _render(session_id: str, meta: dict[str, Any]) -> None:
    freshness = meta.get("canon_freshness") or {}
    metrics = meta.get("metrics") or {}
    lines = [
        "---",
        "status: runtime",
        f"session_id: {meta.get('session_id', session_id)}",
        f"started_at: {meta.get('started_at', '')}",
        f"ended_at: {meta.get('ended_at', '')}",
        "canon_freshness:",
        f"  checked_at: {freshness.get('checked_at', '')}",
        f"  stale_files: {json.dumps(freshness.get('stale_files', []))}",
        f"  banner: {json.dumps(freshness.get('banner'))}",
        "metrics:",
        f"  session_duration_ms: {metrics.get('session_duration_ms')}",
        f"  mean_human_latency_ms: {metrics.get('mean_human_latency_ms')}",
        f"  decision_count: {metrics.get('decision_count', 0)}",
        f"  prompt_count: {metrics.get('prompt_count', 0)}",
        "---",
        "",
        f"# Session log — {safe_log_stem(session_id)}",
        "",
    ]
    banner = freshness.get("banner")
    if banner:
        lines.extend(["## Canon freshness banner", "", f"> {banner}", ""])

    lines.extend(["## Timeline", "", "| At (UTC) | Event | Source | Detail |", "| :---- | :---- | :---- | :---- |"])
    for row in meta.get("timeline", []):
        detail = str(row.get("detail", "")).replace("|", "\\|")
        lines.append(
            f"| {row.get('at', '')} | {row.get('event', '')} | "
            f"{row.get('source', '')} | {detail} |"
        )

    lines.extend(["", "## Human gates", "", "| At (UTC) | Gate | Source | Note |", "| :---- | :---- | :---- | :---- |"])
    gates = meta.get("gates", [])
    if gates:
        for row in gates:
            note = str(row.get("note", "")).replace("|", "\\|")
            lines.append(
                f"| {row.get('at', '')} | {row.get('gate', '')} | "
                f"{row.get('source', '')} | {note} |"
            )
    else:
        lines.append("| — | — | — | — |")

    if metrics:
        lines.extend(
            [
                "",
                "## Metrics",
                "",
                f"- **Session duration (ms):** {metrics.get('session_duration_ms')}",
                f"- **Mean human latency (ms):** {metrics.get('mean_human_latency_ms')}",
                f"- **Decision count:** {metrics.get('decision_count', 0)}",
                f"- **Prompt count:** {metrics.get('prompt_count', 0)}",
            ]
        )

    log_path(session_id).write_text("\n".join(lines) + "\n", encoding="utf-8")
