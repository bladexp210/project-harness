"""Langfuse ingestion API client (stdlib-only, fail-open)."""

from __future__ import annotations

import base64
import json
import os
import uuid
from datetime import datetime, timezone
from pathlib import Path
from typing import Any
from urllib import error, request

REPO_ROOT = Path(__file__).resolve().parents[2]
QUEUE_DIR = REPO_ROOT / ".cursor" / "langfuse-queue"
TRACK_A_ENV = REPO_ROOT / "05-build" / "execution-tools" / "track-a" / ".env"


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"


def new_id() -> str:
    return str(uuid.uuid4())


def load_track_a_env() -> None:
    if not TRACK_A_ENV.is_file():
        return
    for raw in TRACK_A_ENV.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, value = line.partition("=")
        key = key.strip()
        if key and key not in os.environ:
            os.environ[key] = value.strip().strip('"').strip("'")


def langfuse_host() -> str:
    for key in ("LANGFUSE_HOST", "LANGFUSE_BASE_URL"):
        val = os.environ.get(key, "").strip()
        if val:
            return val.rstrip("/")
    return "http://127.0.0.1:3001"


def langfuse_configured() -> bool:
    return bool(os.environ.get("LANGFUSE_PUBLIC_KEY") and os.environ.get("LANGFUSE_SECRET_KEY"))


def build_batch_item(event_type: str, body: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": new_id(),
        "timestamp": utc_now_iso(),
        "type": event_type,
        "body": body,
    }


def ingest_batch(batch: list[dict[str, Any]]) -> bool:
    if not batch or not langfuse_configured():
        return False

    public = os.environ["LANGFUSE_PUBLIC_KEY"]
    secret = os.environ["LANGFUSE_SECRET_KEY"]
    token = base64.b64encode(f"{public}:{secret}".encode("utf-8")).decode("ascii")
    payload = json.dumps({"batch": batch}).encode("utf-8")
    url = f"{langfuse_host()}/api/public/ingestion"
    req = request.Request(
        url,
        data=payload,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Basic {token}",
        },
        method="POST",
    )
    try:
        with request.urlopen(req, timeout=2.0) as resp:
            return 200 <= resp.status < 300
    except (error.URLError, error.HTTPError, TimeoutError, OSError):
        return False


def queue_batch(batch: list[dict[str, Any]]) -> None:
    QUEUE_DIR.mkdir(parents=True, exist_ok=True)
    queue_file = QUEUE_DIR / "pending.jsonl"
    with queue_file.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps({"batch": batch}) + "\n")


def flush_queue() -> None:
    queue_file = QUEUE_DIR / "pending.jsonl"
    if not queue_file.is_file() or not langfuse_configured():
        return
    lines = queue_file.read_text(encoding="utf-8").splitlines()
    remaining: list[str] = []
    for line in lines:
        if not line.strip():
            continue
        try:
            item = json.loads(line)
            batch = item.get("batch", [])
        except json.JSONDecodeError:
            remaining.append(line)
            continue
        if not ingest_batch(batch):
            remaining.append(line)
    if remaining:
        queue_file.write_text("\n".join(remaining) + "\n", encoding="utf-8")
    else:
        queue_file.unlink(missing_ok=True)


def send_batch(batch: list[dict[str, Any]]) -> None:
    if not batch:
        return
    if ingest_batch(batch):
        return
    queue_batch(batch)
