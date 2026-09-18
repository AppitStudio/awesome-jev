# SPDX-License-Identifier: MIT
"""Offline behavior tests; no measured model-quality assertions."""

import copy
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import unittest
from unittest.mock import Mock, patch
import urllib.error

EXAMPLES = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXAMPLES))

from jev_examples.client import (  # noqa: E402
    ENDPOINT, JevError, NoRedirects, evaluate, retry_delay, validate_response,
)
from jev_examples.recipes import RECIPES, build_request, decide  # noqa: E402
import run as runner  # noqa: E402


def fixture(name):
    data = json.loads((EXAMPLES / name / "input.json").read_text())
    response = json.loads((EXAMPLES / name / "mock-response.json").read_text())
    return build_request(name, data), response


def response_stream(response):
    return io.BytesIO(json.dumps(response).encode())


def http_error(status, headers=None):
    return urllib.error.HTTPError(ENDPOINT, status, "secret-response-body", headers or {}, io.BytesIO(b"private content"))


class RecipeTests(unittest.TestCase):
    def test_all_fixtures_obey_contract_and_produce_decisions(self):
        for name in RECIPES:
            with self.subTest(recipe=name):
                request, response = fixture(name)
                answers = validate_response(request, response)
                self.assertIsInstance(decide(name, request, answers), dict)

    def test_answers_are_resolved_by_name_even_when_reordered(self):
        request, response = fixture("support-routing")
        answers = dict(reversed(list(response["answers"].items())))
        self.assertEqual(decide("support-routing", request, answers)["route"], "technical")

    def test_low_choice_confidence_abstains_at_boundary(self):
        request, response = fixture("support-routing")
        answers = response["answers"]
        for confidence, expected in [(0.799, "human_review"), (0.8, "technical")]:
            with self.subTest(confidence=confidence):
                answers["department"]["confidence"] = confidence
                self.assertEqual(decide("support-routing", request, answers)["route"], expected)

    def test_out_of_scope_department_abstains_despite_high_confidence(self):
        request, response = fixture("support-routing")
        response["answers"]["department"].update(choice="other", confidence=0.99)
        self.assertEqual(decide("support-routing", request, response["answers"])["route"], "human_review")

    def test_middle_noul_value_preserves_uncertainty(self):
        request, response = fixture("support-routing")
        response["answers"]["explicit_urgency"]["noul"] = 0.5
        self.assertEqual(decide("support-routing", request, response["answers"])["urgency"], "review")

    def test_scores_are_normalized_by_each_rubric_length(self):
        request, response = fixture("quality-rubric")
        result = decide("quality-rubric", request, response["answers"])
        self.assertAlmostEqual(result["normalized"]["usefulness"], 0.9)
        self.assertAlmostEqual(result["normalized"]["clarity"], 2.6 / 3)
        self.assertEqual(result["weighted_score"], 0.8867)

    def test_uncertain_score_withholds_composite(self):
        request, response = fixture("quality-rubric")
        response["answers"]["clarity"]["confidence"] = 0.1
        result = decide("quality-rubric", request, response["answers"])
        self.assertEqual(result["status"], "human_review")
        self.assertIsNone(result["weighted_score"])

    def test_span_offsets_return_original_text_with_unicode_prefix(self):
        data = {"text": "📩 Help: help@example.org. Billing: invoices@example.org."}
        request = build_request("span-selection", data)
        _, response = fixture("span-selection")
        result = decide("span-selection", request, response["answers"])
        selected = result["selection"]
        self.assertEqual(selected["value"], "invoices@example.org")
        self.assertEqual(data["text"][selected["start"]:selected["end"]], selected["value"])

    def test_no_matching_span_and_uncertainty_do_not_invent_value(self):
        request, response = fixture("span-selection")
        answer = response["answers"]["billing_contact"]
        answer["choice"] = "none"
        self.assertEqual(decide("span-selection", request, response["answers"]), {"status": "not_found", "selection": None})
        answer["confidence"] = 0.5
        self.assertEqual(decide("span-selection", request, response["answers"]), {"status": "human_review", "selection": None})

    def test_empty_and_excessive_candidate_sets_stop_locally(self):
        for text in ("No contact listed.", " ".join(f"person{i}@example.org" for i in range(255))):
            with self.subTest(length=len(text)), self.assertRaises(JevError):
                build_request("span-selection", {"text": text})
        request = build_request("span-selection", {"text": " ".join(f"person{i}@example.org" for i in range(254))})
        self.assertEqual(len(request["questions"]["billing_contact"]["criteria"]), 255)

    def test_rag_policy_prioritizes_conflict_then_exclusion_then_review(self):
        request, response = fixture("rag-triage")
        cases = [
            ({"relevant": 0.95, "evidence": 0.95, "contradiction": 0.01}, "candidate_evidence"),
            ({"relevant": 0.05, "evidence": 0.95, "contradiction": 0.01}, "exclude"),
            ({"relevant": 0.95, "evidence": 0.5, "contradiction": 0.01}, "human_review"),
            ({"relevant": 0.05, "evidence": 0.5, "contradiction": 0.9}, "conflict_review"),
        ]
        for values, expected in cases:
            with self.subTest(expected=expected):
                for key, value in values.items():
                    response["answers"][key]["noul"] = value
                self.assertEqual(decide("rag-triage", request, response["answers"])["status"], expected)


class ContractTests(unittest.TestCase):
    def setUp(self):
        self.request, self.response = fixture("support-routing")

    def test_missing_or_unexpected_answers_stop_processing(self):
        for key in ("department", "unexpected"):
            response = copy.deepcopy(self.response)
            if key == "department":
                del response["answers"][key]
            else:
                response["answers"][key] = {"type": "noul", "noul": 0.5}
            with self.subTest(key=key), self.assertRaises(JevError):
                validate_response(self.request, response)

    def test_wrong_answer_type_stops_processing(self):
        self.response["answers"]["department"]["type"] = "noul"
        with self.assertRaises(JevError):
            validate_response(self.request, self.response)

    def test_noul_must_be_finite_bounded_number_not_boolean(self):
        for invalid in (float("nan"), float("inf"), 10 ** 400, -0.1, 1.1, True, "0.8", None):
            with self.subTest(invalid=invalid), self.assertRaises(JevError):
                self.response["answers"]["explicit_urgency"]["noul"] = invalid
                validate_response(self.request, self.response)

    def test_unknown_choice_or_nonwinning_choice_stops_processing(self):
        for invalid in ("invented_department", "billing", []):
            with self.subTest(invalid=invalid), self.assertRaises(JevError):
                self.response["answers"]["department"]["choice"] = invalid
                validate_response(self.request, self.response)

    def test_invalid_distribution_stops_processing(self):
        original = self.response["answers"]["department"]["probabilities"]
        for invalid in ({"technical": 1}, {**original, "billing": 0.8}, {**original, "billing": float("nan")}):
            with self.subTest(invalid=invalid), self.assertRaises(JevError):
                self.response["answers"]["department"]["probabilities"] = invalid
                validate_response(self.request, self.response)

    def test_score_cannot_disagree_with_distribution_or_legend(self):
        request, response = fixture("quality-rubric")
        for change in ({"score": 0.2}, {"score": 20}, {"legend": {"0": "Wrong rubric"}}):
            modified = copy.deepcopy(response)
            modified["answers"]["usefulness"].update(change)
            with self.subTest(change=change), self.assertRaises(JevError):
                validate_response(request, modified)


class HttpTests(unittest.TestCase):
    def setUp(self):
        self.request, self.response = fixture("support-routing")

    def test_live_request_uses_documented_endpoint_and_body(self):
        opener = Mock(return_value=response_stream(self.response))
        result = evaluate(self.request, "test-key", open_url=opener)
        sent = opener.call_args.args[0]
        self.assertEqual(sent.full_url, ENDPOINT)
        self.assertEqual(sent.method, "POST")
        self.assertEqual(sent.get_header("Authorization"), "Bearer test-key")
        self.assertEqual(json.loads(sent.data), self.request)
        self.assertEqual(opener.call_args.kwargs["timeout"], 30)
        self.assertEqual(result, self.response)

    def test_missing_key_stops_before_network(self):
        opener = Mock()
        with self.assertRaises(JevError):
            evaluate(self.request, "", open_url=opener)
        opener.assert_not_called()

    def test_429_and_529_retry_with_bounded_backoff(self):
        opener = Mock(side_effect=[http_error(429, {"Retry-After": "2"}), http_error(529), response_stream(self.response)])
        sleep = Mock()
        evaluate(self.request, "test-key", open_url=opener, sleep=sleep)
        self.assertEqual(opener.call_count, 3)
        self.assertEqual(sleep.call_count, 2)
        self.assertEqual(sleep.call_args_list[0].args[0], 2)
        self.assertGreaterEqual(sleep.call_args_list[1].args[0], 2)

    def test_retry_attempts_are_bounded(self):
        opener = Mock(side_effect=[http_error(429), http_error(429), http_error(429)])
        with self.assertRaises(JevError):
            evaluate(self.request, "test-key", open_url=opener, sleep=Mock())
        self.assertEqual(opener.call_count, 3)

    def test_single_attempt_budget_disables_retries(self):
        opener = Mock(side_effect=http_error(429))
        sleeper = Mock()
        with self.assertRaises(JevError):
            evaluate(self.request, "test-key", open_url=opener, sleep=sleeper, max_attempts=1)
        self.assertEqual(opener.call_count, 1)
        sleeper.assert_not_called()

    def test_invalid_attempt_budget_stops_before_network(self):
        for value in (0, 4, True, 1.5):
            opener = Mock()
            with self.subTest(value=value), self.assertRaises(JevError):
                evaluate(self.request, "test-key", open_url=opener, max_attempts=value)
            opener.assert_not_called()

    def test_nonretryable_errors_are_redacted_and_not_retried(self):
        for status in (401, 422, 500, 302):
            opener = Mock(side_effect=http_error(status))
            with self.subTest(status=status), self.assertRaises(JevError) as caught:
                evaluate(self.request, "test-key", open_url=opener)
            self.assertEqual(opener.call_count, 1)
            self.assertNotIn("private content", str(caught.exception))
            self.assertNotIn("secret-response-body", str(caught.exception))
            self.assertNotIn("test-key", str(caught.exception))

    def test_network_failures_are_not_blindly_retried(self):
        for error in (TimeoutError(), urllib.error.URLError("private details")):
            opener = Mock(side_effect=error)
            with self.subTest(error=error), self.assertRaises(JevError) as caught:
                evaluate(self.request, "test-key", open_url=opener)
            self.assertEqual(opener.call_count, 1)
            self.assertNotIn("private details", str(caught.exception))

    def test_invalid_json_stops_without_a_decision(self):
        with self.assertRaises(JevError):
            evaluate(self.request, "test-key", open_url=Mock(return_value=io.BytesIO(b"not json")))

    def test_nonfinite_extra_response_fields_are_rejected(self):
        for value in (float("nan"), float("inf"), -float("inf")):
            response = {**self.response, "extra": value}
            with self.subTest(value=value), self.assertRaises(JevError):
                evaluate(self.request, "test-key", open_url=Mock(return_value=response_stream(response)))

    def test_long_retry_after_stops_instead_of_retrying_too_early(self):
        with self.assertRaises(JevError):
            retry_delay("120", 0)

    def test_redirects_are_not_followed(self):
        self.assertIsNone(NoRedirects().redirect_request(None, None, 302, "redirect", {}, "https://elsewhere.invalid"))


class CliTests(unittest.TestCase):
    def test_default_and_explicit_mock_ignore_available_credentials(self):
        for extra in ([], ["--mock"]):
            with self.subTest(extra=extra), patch.object(sys, "argv", ["run.py", "support-routing", *extra]), \
                    patch.dict(os.environ, {"TYPESAFE_API_KEY": "do-not-use"}), \
                    patch.object(runner, "evaluate", side_effect=AssertionError("Network must not be called")), \
                    patch("sys.stdout", new_callable=io.StringIO) as output:
                self.assertEqual(runner.main(), 0)
                self.assertIn("synthetic", json.loads(output.getvalue())["mode"])

    def test_show_request_never_calls_network_even_with_live(self):
        with patch.object(sys, "argv", ["run.py", "support-routing", "--live", "--show-request"]), \
                patch.object(runner, "evaluate", side_effect=AssertionError("Network must not be called")), \
                patch("sys.stdout", new_callable=io.StringIO) as output:
            self.assertEqual(runner.main(), 0)
            self.assertIn("questions", json.loads(output.getvalue()))

    def test_invalid_header_key_is_redacted_before_network(self):
        for key in ("sensitive-key\r\n", "sensitive-key\x01", "sensitive-key\u2603"):
            with self.subTest(key=repr(key)), \
                    patch.object(sys, "argv", ["run.py", "support-routing", "--live"]), \
                    patch.dict(os.environ, {"TYPESAFE_API_KEY": key}), \
                    patch("urllib.request.build_opener", side_effect=AssertionError("Network must not be reached")), \
                    patch("sys.stderr", new_callable=io.StringIO) as output:
                self.assertEqual(runner.main(), 1)
                self.assertNotIn("sensitive-key", output.getvalue())

    def test_cli_works_from_another_working_directory(self):
        result = subprocess.run([sys.executable, str(EXAMPLES / "run.py"), "span-selection"], cwd=EXAMPLES.parent.parent, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(json.loads(result.stdout)["decision"]["selection"]["value"], "invoices@example.org")


if __name__ == "__main__":
    unittest.main()
