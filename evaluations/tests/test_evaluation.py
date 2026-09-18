# SPDX-License-Identifier: MIT
"""Offline checks for evaluation accounting and isolation; no API requests."""

import argparse
import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch
import urllib.error

EVALUATIONS = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("evaluation_runner", EVALUATIONS / "run.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def record(department="billing", urgency="ordinary", *, review=False, expected_department="billing", expected_urgency="ordinary", require_review=False, error=None):
    return {"expected": {"department": expected_department, "urgency": expected_urgency, "require_review": require_review},
            "decision": None if error else {"department": department, "urgency": urgency, "needs_review": review},
            "error": {"category": error, "message": "failure"} if error else None, "latency_ms": None, "usage": None}


class MetricsTests(unittest.TestCase):
    def test_empty_denominators_are_null(self):
        metrics = runner.summarize([])
        self.assertEqual(metrics["counts"]["total"], 0)
        for name in ("department_accuracy", "automatic_coverage", "wrong_automatic_assignments", "urgency_errors"):
            self.assertEqual(metrics[name], {"numerator": 0, "denominator": 0, "value": None})

    def test_failures_stay_in_coverage_and_not_accuracy(self):
        metrics = runner.summarize([
            record(), record("technical", "ordinary", expected_urgency="high"),
            record("other", "review", review=True, expected_department="other", require_review=True),
            record(error="service"),
        ])
        self.assertEqual(metrics["department_accuracy"], runner.rate(2, 3))
        self.assertEqual(metrics["automatic_coverage"], runner.rate(2, 4))
        self.assertEqual(metrics["review_rate"], runner.rate(1, 4))
        self.assertEqual(metrics["unresolved_rate"], runner.rate(1, 4))
        self.assertEqual(metrics["wrong_automatic_assignments"], runner.rate(1, 2))
        self.assertEqual(metrics["urgency_errors"], runner.rate(1, 2))
        self.assertEqual(metrics["high_urgency_downgraded"], runner.rate(1, 1))
        self.assertEqual(metrics["service_error_rate"], runner.rate(1, 4))
        self.assertEqual(metrics["department_confusion"], {"billing": {"billing": 1, "technical": 1}, "other": {"other": 1}})

    def test_matching_department_can_still_miss_required_review(self):
        metrics = runner.summarize([record(require_review=True)])
        self.assertEqual(metrics["wrong_automatic_assignments"], runner.rate(0, 1))
        self.assertEqual(metrics["unsafe_automatic_decisions"], runner.rate(1, 1))
        self.assertEqual(metrics["required_review_missed"], runner.rate(1, 1))

    def test_all_review_has_no_claim_of_automatic_accuracy(self):
        metrics = runner.summarize([record(urgency="review", review=True)])
        self.assertEqual(metrics["wrong_automatic_assignments"], runner.rate(0, 0))
        self.assertEqual(metrics["urgency_errors"], runner.rate(0, 0))
        self.assertEqual(metrics["urgency_review"], runner.rate(1, 1))


class RunnerTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.dataset = self.directory / "dataset.jsonl"
        self.cases = [
            {"id": "a", "split": "development", "slice": "clear", "message": "Please send my invoice", "expected_department": "billing", "expected_urgency": "ordinary", "require_review": False},
            {"id": "b", "split": "holdout", "slice": "unclear", "message": "Help with that thing", "expected_department": "other", "expected_urgency": "ordinary", "require_review": True},
        ]
        self.write_cases()

    def write_cases(self):
        self.dataset.write_text("".join(json.dumps(case) + "\n" for case in self.cases))

    def args(self, **changes):
        values = {"dataset": self.dataset, "output_dir": self.directory / "output", "split": "development", "mode": "mock", "config": None, "model": runner.MODEL, "max_calls": 50, "replay_from": None}
        values.update(changes)
        return argparse.Namespace(**values)

    def test_default_mock_does_not_use_credentials_and_is_not_quality_evidence(self):
        live = Mock(side_effect=AssertionError("No network"))
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "must-not-be-used"}):
            result = runner.run(self.args(), live_call=live)
        live.assert_not_called()
        self.assertFalse(result["quality_evidence"])
        record = runner.read_jsonl(self.directory / "output/records.jsonl")[0]
        self.assertEqual(record["model_returned"], "synthetic-uniform-baseline")
        self.assertEqual(record["request"]["state"], {"ticket": {"message": self.cases[0]["message"]}})
        self.assertNotIn("expected_department", json.dumps(record["request"]))
        self.assertEqual(record["expected"]["department"], "billing")

    def test_mock_response_is_independent_of_expected_labels(self):
        first = runner.ticket_only(self.cases[0])
        changed = {**self.cases[0], "expected_department": "technical", "expected_urgency": "high", "slice": "changed"}
        self.assertEqual(first, runner.ticket_only(changed))

    def test_budget_fails_before_any_http_attempt(self):
        live = Mock()
        with self.assertRaisesRegex(ValueError, "exceed"):
            runner.run(self.args(mode="live", split="all", max_calls=1), live_call=live)
        live.assert_not_called()
        self.assertFalse((self.directory / "output").exists())

    def test_missing_key_is_rejected_before_http(self):
        live = Mock()
        with patch.dict(os.environ, {}, clear=True), self.assertRaisesRegex(ValueError, "TYPESAFE_API_KEY"):
            runner.run(self.args(mode="live"), live_call=live)
        live.assert_not_called()

    def test_all_modes_reject_repo_output_paths_and_symlinks(self):
        link = self.directory / "repo-link"
        link.symlink_to(runner.ROOT, target_is_directory=True)
        for mode in ("mock", "live", "replay"):
            for directory in (runner.ROOT / "evaluation-output", link / "evaluation-output"):
                with self.subTest(mode=mode, directory=str(directory)), self.assertRaisesRegex(ValueError, "outside"):
                    runner.run(self.args(mode=mode, output_dir=directory), live_call=Mock())

    def test_one_attempt_per_case_and_service_errors_are_separate(self):
        live = Mock(side_effect=runner.ServiceError("HTTP 429; no retry attempted"))
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "test-key"}):
            summary = runner.run(self.args(mode="live", split="all", max_calls=2), live_call=live)
        self.assertEqual(live.call_count, 2)
        self.assertEqual(summary["overall"]["counts"]["errors_by_category"], {"service": 2})
        manifest = json.loads((self.directory / "output/manifest.json").read_text())
        self.assertEqual(manifest["http_attempts"], 2)
        self.assertNotIn("test-key", (self.directory / "output/records.jsonl").read_text())

    def test_invalid_response_preserves_returned_model_as_contract_error(self):
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "test-key"}):
            summary = runner.run(self.args(mode="live"), live_call=Mock(return_value={"model": "unexpected-model", "answers": {}}))
        self.assertEqual(summary["overall"]["counts"]["errors_by_category"], {"contract": 1})
        result = runner.read_jsonl(self.directory / "output/records.jsonl")[0]
        self.assertEqual(result["model_returned"], "unexpected-model")
        self.assertEqual(result["model_requested"], runner.MODEL)

    def test_replay_preserves_evidence_and_never_calls_network(self):
        original = runner.run(self.args(split="all"))
        live = Mock(side_effect=AssertionError("No network"))
        replay = runner.run(self.args(mode="replay", split="all", replay_from=self.directory / "output/records.jsonl", output_dir=self.directory / "replayed"), live_call=live)
        live.assert_not_called()
        self.assertEqual(original["overall"], replay["overall"])
        self.assertFalse(replay["quality_evidence"])

    def test_replay_rejects_changed_labels_before_output(self):
        runner.run(self.args())
        self.cases[0]["expected_department"] = "technical"
        self.write_cases()
        with self.assertRaisesRegex(ValueError, "labels or split"):
            runner.run(self.args(mode="replay", replay_from=self.directory / "output/records.jsonl", output_dir=self.directory / "replayed"))
        self.assertFalse((self.directory / "replayed").exists())

    def test_holdout_replay_rejects_policy_changes(self):
        runner.run(self.args(split="all"))
        router = runner.load_router()
        config = router.load_config()
        config["policy"]["department_confidence_min"] = 0.9
        path = self.directory / "config.json"
        path.write_text(json.dumps(config))
        with self.assertRaisesRegex(ValueError, "Holdout replay"):
            runner.run(self.args(mode="replay", split="holdout", config=path, replay_from=self.directory / "output/records.jsonl", output_dir=self.directory / "replayed"))
        # The same policy-only change is allowed on development data.
        runner.run(self.args(mode="replay", config=path, replay_from=self.directory / "output/records.jsonl", output_dir=self.directory / "replayed-development"))

    def test_duplicate_ids_and_invalid_labels_fail_locally(self):
        for modify in (lambda: self.cases.append(copy.deepcopy(self.cases[0])), lambda: self.cases[0].update(expected_urgency="maybe")):
            with self.subTest(modify=modify):
                original = copy.deepcopy(self.cases)
                modify()
                self.write_cases()
                with self.assertRaises(ValueError):
                    runner.run(self.args())
                self.cases = original

    def test_existing_results_are_not_overwritten(self):
        runner.run(self.args())
        with self.assertRaisesRegex(ValueError, "never overwritten"):
            runner.run(self.args())


class HttpTests(unittest.TestCase):
    def test_429_is_redacted_and_never_retried(self):
        opener = Mock(side_effect=urllib.error.HTTPError(runner.ENDPOINT, 429, "private message", {}, io.BytesIO(b"private body")))
        with self.assertRaises(runner.ServiceError) as caught:
            runner.live_response({"model": runner.MODEL}, "test-key", opener)
        self.assertEqual(opener.call_count, 1)
        self.assertNotIn("private", str(caught.exception))
        self.assertNotIn("test-key", str(caught.exception))

    def test_key_validation_happens_before_network(self):
        opener = Mock()
        for key in ("", "secret-key\n", "secret-key snow"):
            with self.subTest(key=key), self.assertRaises(ValueError) as caught:
                runner.live_response({}, key, opener)
            self.assertNotIn("secret-key", str(caught.exception))
        opener.assert_not_called()

    def test_nonfinite_json_is_rejected(self):
        opener = Mock(return_value=io.BytesIO(b'{"model":"x","value":NaN}'))
        with self.assertRaisesRegex(runner.ServiceError, "valid JSON"):
            runner.live_response({}, "test-key", opener)


if __name__ == "__main__":
    unittest.main()
