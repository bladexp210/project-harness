"""Golden evaluation test suite for the Acme PTO FAQ assistant (Tasks 3 & 4)."""
import json
import pathlib
import tempfile
import unittest

from pto_faq_bot import DEFAULT_POLICY_PATH, answer_question, load_policy_sections


class TestAcmePtoFaqBot(unittest.TestCase):
    """Verifies the 10 golden questions and HR live-edit workflow."""

    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.log_path = pathlib.Path(self.temp_dir.name) / "unanswered_questions.jsonl"

    def tearDown(self) -> None:
        self.temp_dir.cleanup()

    def test_policy_has_three_required_headings(self) -> None:
        sections = load_policy_sections(DEFAULT_POLICY_PATH)
        self.assertEqual(list(sections.keys()), ["Accrual", "Notice", "Carryover"])

    def test_six_answerable_questions_cite_exact_headings(self) -> None:
        cases = [
            (
                "How many PTO days do full-time employees accrue per year and per month?",
                "## Accrual",
                "15 days",
            ),
            (
                "Do part-time employees working 20 hours a week accrue PTO?",
                "## Accrual",
                "pro-rated basis",
            ),
            (
                "How many business days in advance must I request a 2-day PTO trip?",
                "## Notice",
                "5 business days",
            ),
            (
                "How much notice is required for a 5-day vacation, and what about same-day emergencies?",
                "## Notice",
                "10 business days",
            ),
            (
                "How many unused PTO days can I carry over on December 31?",
                "## Carryover",
                "5 unused PTO days",
            ),
            (
                "By what date must carried-over PTO days be used in the new year?",
                "## Carryover",
                "March 31",
            ),
        ]
        for question, expected_heading, expected_phrase in cases:
            with self.subTest(question=question):
                res = answer_question(question, log_path=self.log_path)
                self.assertEqual(res.status, "answered")
                self.assertEqual(res.cited_heading, expected_heading)
                self.assertIn(f"[Cited clause: {expected_heading}]", res.answer)
                self.assertIn(expected_phrase, res.answer)

        self.assertFalse(self.log_path.exists(), "Answered questions must not be logged as refusals")

    def test_four_out_of_policy_questions_refuse_and_log(self) -> None:
        refusal_cases = [
            ("How many days of paid bereavement leave do I get for a family member?", "out_of_policy_scope"),
            ("Does Acme pay out unused PTO in cash if I resign or leave the company?", "out_of_policy_scope"),
            ("Can I donate my unused PTO days to a coworker's balance?", "unmatched_topic"),
            ("Can you approve my PTO request for next Friday and update payroll?", "prohibited_action"),
        ]
        for question, expected_reason in refusal_cases:
            with self.subTest(question=question):
                res = answer_question(question, log_path=self.log_path)
                self.assertEqual(res.status, "refused")
                self.assertIsNone(res.cited_heading)
                self.assertEqual(res.log_reason, expected_reason)

        logged_lines = self.log_path.read_text(encoding="utf-8").strip().splitlines()
        self.assertEqual(len(logged_lines), 4)
        for line in logged_lines:
            record = json.loads(line)
            self.assertEqual(record["user"], "employee@example.com")
            self.assertIn("question", record)

    def test_hr_can_edit_policy_file_without_code_changes(self) -> None:
        custom_policy = pathlib.Path(self.temp_dir.name) / "pto.md"
        custom_policy.write_text(
            "---\ntitle: Custom PTO\nstatus: living\n---\n# Custom\n\n"
            "## Carryover\n\nEmployees may carry over up to 8 unused PTO days.\n",
            encoding="utf-8",
        )
        res = answer_question(
            "How many unused PTO days can I carry over?",
            policy_path=custom_policy,
            log_path=self.log_path,
        )
        self.assertEqual(res.status, "answered")
        self.assertEqual(res.cited_heading, "## Carryover")
        self.assertIn("8 unused PTO days", res.answer)


if __name__ == "__main__":
    unittest.main()
