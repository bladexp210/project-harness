"""Smallest reader and FAQ assistant for Acme PTO policy (Task 4)."""
from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
import json
import pathlib
import re
import sys
from typing import Dict, List, Optional

DEFAULT_POLICY_PATH = pathlib.Path(__file__).resolve().parent / "policies" / "pto.md"
DEFAULT_LOG_PATH = pathlib.Path(__file__).resolve().parent / "unanswered_questions.jsonl"
DEFAULT_USER = "employee@example.com"

REFUSAL_MESSAGE = (
    "REFUSAL: The approved PTO policy (policies/pto.md) does not cover this question "
    "or prohibits this action. Your question has been logged for HR review."
)

PROHIBITED_ACTION_PATTERNS = (
    r"\bapprove\s+my\b",
    r"\bupdate\s+payroll\b",
    r"\bwrite\s+to\s+payroll\b",
    r"\blegal\s+advice\b",
)

OUT_OF_SCOPE_PATTERNS = (
    r"\bbereavement\b",
    r"\bparental\s+leave\b",
    r"\bmaternity\b",
    r"\bpaternity\b",
    r"\bsick\s+leave\b",
    r"\bjury\s+duty\b",
    r"\bresign\b",
    r"\btermination\b",
    r"\bseverance\b",
    r"\b401k\b",
    r"\bhealth\s+insurance\b",
)

STOPWORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "can", "do", "does", "for",
    "from", "get", "how", "i", "if", "in", "is", "it", "many", "much", "must",
    "my", "of", "on", "or", "out", "pto", "paid", "time", "off", "policy", "acme",
    "the", "to", "what", "when", "week", "year", "employees", "employee", "days", "day",
}


@dataclass(frozen=True)
class FAQResponse:
    """Structured result returned by the Acme PTO FAQ assistant."""

    status: str  # "answered" or "refused"
    cited_heading: Optional[str]
    answer: str
    log_reason: Optional[str] = None


def load_policy_sections(policy_path: pathlib.Path = DEFAULT_POLICY_PATH) -> Dict[str, str]:
    """Parse level-2 markdown headings (## Heading) from policies/pto.md."""
    raw = policy_path.read_text(encoding="utf-8")
    if raw.startswith("---\n"):
        parts = raw.split("\n---\n", 1)
        if len(parts) == 2:
            raw = parts[1]
    sections: Dict[str, List[str]] = {}
    current_heading: Optional[str] = None
    for line in raw.splitlines():
        if line.startswith("## "):
            current_heading = line[3:].strip()
            sections[current_heading] = []
        elif current_heading is not None:
            sections[current_heading].append(line)
    return {
        heading: "\n".join(body).strip()
        for heading, body in sections.items()
        if "\n".join(body).strip()
    }


def _tokenize(text: str) -> List[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    stemmed: List[str] = []
    for w in words:
        if w in STOPWORDS:
            continue
        if w.endswith("ing") and len(w) > 5:
            w = w[:-3]
        elif w.endswith("ed") and len(w) > 4:
            w = w[:-2]
        elif w.endswith("s") and len(w) > 4:
            w = w[:-1]
        stemmed.append(w)
    return stemmed


def _log_unanswered(
    question: str,
    reason: str,
    user: str,
    log_path: pathlib.Path,
) -> None:
    entry = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "user": user,
        "question": question,
        "reason": reason,
    }
    with log_path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(entry, ensure_ascii=True) + "\n")


def answer_question(
    question: str,
    policy_path: pathlib.Path = DEFAULT_POLICY_PATH,
    log_path: pathlib.Path = DEFAULT_LOG_PATH,
    user: str = DEFAULT_USER,
) -> FAQResponse:
    """Answer a PTO question strictly from policies/pto.md or refuse and log."""
    sections = load_policy_sections(policy_path)
    q_lower = question.lower()

    for pattern in PROHIBITED_ACTION_PATTERNS:
        if re.search(pattern, q_lower):
            _log_unanswered(question, "prohibited_action", user, log_path)
            return FAQResponse("refused", None, REFUSAL_MESSAGE, "prohibited_action")

    for pattern in OUT_OF_SCOPE_PATTERNS:
        if re.search(pattern, q_lower):
            _log_unanswered(question, "out_of_policy_scope", user, log_path)
            return FAQResponse("refused", None, REFUSAL_MESSAGE, "out_of_policy_scope")

    q_tokens = set(_tokenize(question))
    best_heading: Optional[str] = None
    best_score = 0

    for heading, body in sections.items():
        section_tokens = set(_tokenize(f"{heading} {body}"))
        heading_tokens = set(_tokenize(heading))
        overlap = len(q_tokens & section_tokens) + (2 * len(q_tokens & heading_tokens))
        if overlap > best_score:
            best_score = overlap
            best_heading = heading

    if best_heading is None or best_score < 2 or best_heading not in sections:
        _log_unanswered(question, "unmatched_topic", user, log_path)
        return FAQResponse("refused", None, REFUSAL_MESSAGE, "unmatched_topic")

    clause_body = sections[best_heading]
    formatted = f"[Cited clause: ## {best_heading}]\n{clause_body}"
    return FAQResponse("answered", f"## {best_heading}", formatted, None)


def main(argv: Optional[List[str]] = None) -> int:
    args = argv if argv is not None else sys.argv[1:]
    if not args:
        print('Usage: python pto_faq_bot.py "<question>"')
        return 2
    res = answer_question(" ".join(args))
    print(res.answer)
    return 0 if res.status == "answered" else 1


if __name__ == "__main__":
    raise SystemExit(main())
