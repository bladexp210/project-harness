import re

from context_loader import strip_teaching_blocks
from md_checks.placeholders import _is_dual_purpose_md

# ADR-008 industry fog — word-boundary match, case insensitive
FOG_PATTERNS = [
    (re.compile(r"\bleverage\b", re.I), "leverage"),
    (re.compile(r"\bsynergy\b", re.I), "synergy"),
    (re.compile(r"\bbest-in-class\b", re.I), "best-in-class"),
    (re.compile(r"\bbest in class\b", re.I), "best in class"),
]


def _artifact_body(text, relpath):
    """Plain markdown outside teaching callouts on dual-purpose files."""
    if not _is_dual_purpose_md(relpath):
        return ""
    body = strip_teaching_blocks(relpath, text)
    body = re.sub(r"```.*?```", "", body, flags=re.DOTALL)
    return re.sub(r"`[^`\n]+`", "", body)


def check_fog_words(text, relpath):
    """ADR-008 T7: flag industry fog words in artifact zones (dual-purpose files)."""
    if not relpath.endswith(".md"):
        return []
    body = _artifact_body(text, relpath)
    if not body.strip():
        return []

    errors = []
    for pattern, label in FOG_PATTERNS:
        if pattern.search(body):
            errors.append(
                "artifact zone contains ADR-008 fog word {!r} — replace with plain language".format(
                    label
                )
            )
    return errors
