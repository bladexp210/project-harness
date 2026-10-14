"""Redaction helpers for Path C Langfuse bridge."""

from __future__ import annotations

import hashlib
import re
from typing import Any

MAX_FIELD_LEN = 500
REDACT_PATTERNS = (
    re.compile(r"(?i)(api[_-]?key|secret|password|token|authorization)\s*[:=]\s*\S+"),
    re.compile(r"\bsk-[A-Za-z0-9_-]{8,}\b"),
    re.compile(r"\bpk-[A-Za-z0-9_-]{8,}\b"),
    re.compile(r"\bBearer\s+[A-Za-z0-9._-]+\b"),
)


def redact_value(value: Any) -> Any:
    if value is None or isinstance(value, (bool, int, float)):
        return value
    if isinstance(value, dict):
        return {k: redact_value(v) for k, v in value.items()}
    if isinstance(value, list):
        return [redact_value(v) for v in value]
    text = str(value)
    for pattern in REDACT_PATTERNS:
        text = pattern.sub("[REDACTED]", text)
    if len(text) > MAX_FIELD_LEN:
        digest = hashlib.sha256(text.encode("utf-8")).hexdigest()[:12]
        text = text[:MAX_FIELD_LEN] + f"...[truncated sha256:{digest}]"
    return text
