"""Contract tests for _views/_shared/export.js markdown output."""
import re
import unittest
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
FIXTURE_PROCEED = REPO_ROOT / "_views" / "gates" / "_fixtures" / "proceed-export.md"


def export_body(content: str) -> str:
    """Strip YAML frontmatter so fixture matches live export shape."""
    if content.startswith("---\n"):
        end = content.find("\n---", 4)
        if end != -1:
            return content[end + 4 :].lstrip("\n")
    return content


EXPORT_HEADER_RE = re.compile(
    r"^## Human decisions\n\n"
    r"<!-- exported-from: .+ -->\n"
    r"<!-- exported-at: \d{4}-\d{2}-\d{2} \d{2}:\d{2} -->\n"
    r"(<!-- gate: .+ -->\n)?"
    r"(<!-- arc: .+ -->\n)?"
    r"(<!-- session: .+ -->\n)?",
    re.MULTILINE,
)


class TestViewsExportContract(unittest.TestCase):
    def test_minimal_header_shape(self):
        sample = """## Human decisions

<!-- exported-from: _views/gates/proceed.html -->
<!-- exported-at: 2026-07-02 23:00 -->
<!-- gate: proceed -->
<!-- arc: s48-html-views -->
<!-- session: 48 -->

| Question | Answer |
| :---- | :---- |
| Primary goal correct? | yes |
"""
        self.assertRegex(sample, EXPORT_HEADER_RE)

    def test_proceed_fixture_matches_header(self):
        content = export_body(FIXTURE_PROCEED.read_text(encoding="utf-8"))
        self.assertRegex(content, EXPORT_HEADER_RE)
        self.assertIn("## Scope confirmation", content)
        self.assertIn("<!-- gate: proceed -->", content)
        self.assertIn("<!-- arc: s48-html-views -->", content)
        self.assertIn("<!-- session: 48 -->", content)

    def test_table_row_pipe_escape_documented(self):
        row = "| What | a \\| b |"
        self.assertIn("\\|", row)


if __name__ == "__main__":
    unittest.main()
