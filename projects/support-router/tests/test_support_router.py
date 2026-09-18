# SPDX-License-Identifier: MIT
"""Offline checks for policy boundaries, replay binding, and batch failure handling."""

import copy
import importlib.util
import io
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

PROJECT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT))

import support_router as router  # noqa: E402

spec = importlib.util.spec_from_file_location("support_router_runner", PROJECT / "run.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


def fixture(index=0):
    rows = runner.read_jsonl(PROJECT / "demo" / "responses.jsonl")
    row = rows[index]
    return row["request"], row["response"]["answers"]


class PolicyTests(unittest.TestCase):
    def test_department_boundary_is_inclusive(self):
        request, answers = fixture()
        for confidence, expected in [(0.79999, "human_review"), (0.8, "billing")]:
            with self.subTest(confidence=confidence):
                answers["department"]["confidence"] = confidence
                self.assertEqual(router.decide(request, answers)["route"], expected)

    def test_urgency_boundaries_are_inclusive_and_middle_requires_review(self):
        request, answers = fixture()
        for noul, urgency, review in [(.15, "ordinary", False), (.15001, "review", True), (.84999, "review", True), (.85, "high", False)]:
            with self.subTest(noul=noul):
                answers["explicit_urgency"]["noul"] = noul
                decision = router.decide(request, answers)
                self.assertEqual(decision["urgency"], urgency)
                self.assertEqual(decision["needs_review"], review)

    def test_policy_can_allow_unknown_urgency_but_preserves_it(self):
        request, answers = fixture(4)
        config = router.load_config()
        config["policy"]["review_uncertain_urgency"] = False
        decision = router.decide(request, answers, config)
        self.assertEqual(decision["route"], "technical")
        self.assertEqual(decision["urgency"], "review")
        self.assertFalse(decision["needs_review"])

    def test_other_always_requires_review_even_when_confident(self):
        request, answers = fixture(3)
        answers["department"]["confidence"] = 1
        decision = router.decide(request, answers)
        self.assertEqual(decision["department"], "other")
        self.assertEqual(decision["route"], "human_review")
        self.assertEqual(decision["review_reasons"], ["department_out_of_scope"])

    def test_multiple_review_reasons_are_preserved(self):
        request, answers = fixture(3)
        answers["department"]["confidence"] = .2
        answers["explicit_urgency"]["noul"] = .5
        self.assertEqual(router.decide(request, answers)["review_reasons"], [
            "department_uncertain", "department_out_of_scope", "urgency_uncertain",
        ])

    def test_evaluation_labels_and_ids_do_not_reach_model(self):
        ticket = {"id": "test-101", "message": "Please help.", "expected_department": "other", "private_notes": "do not send"}
        self.assertEqual(router.build_request(ticket)["state"], {"ticket": {"message": "Please help."}})

    def test_custom_departments_work_and_mismatched_definitions_are_rejected(self):
        config = router.load_config()
        config["departments"] = {"shipping": "Shipping status and delivery problems", "other": "Anything else"}
        request = router.build_request({"id": "x", "message": "Where is my package?"}, config)
        answers = {"department": {"type": "choice", "choice": "shipping", "confidence": .99, "probabilities": {"shipping": .99, "other": .01}}, "explicit_urgency": {"type": "noul", "noul": .02}}
        self.assertEqual(router.decide(request, answers, config)["route"], "shipping")
        config["departments"]["shipping"] = "A different meaning"
        with self.assertRaises(router.JevError):
            router.decide(request, answers, config)

    def test_malformed_answers_never_produce_a_routing_decision(self):
        request, original = fixture()
        invalid = [None, {}, {**original, "explicit_urgency": {"type": "noul", "noul": float("nan")}}]
        for answers in invalid:
            with self.subTest(answers=answers), self.assertRaises(router.JevError):
                router.decide(request, answers)


class ConfigTests(unittest.TestCase):
    def test_reject_invalid_or_ambiguous_thresholds(self):
        for field, value in [("department_confidence_min", True), ("department_confidence_min", -1), ("urgency_low_max", float("nan")), ("urgency_high_min", .15), ("review_uncertain_urgency", "true")]:
            config = router.load_config()
            config["policy"][field] = value
            with self.subTest(field=field, value=value), self.assertRaises(router.JevError):
                router.validate_config(config)

    def test_reject_unknown_settings_missing_other_and_reserved_name(self):
        configs = []
        config = router.load_config()
        config["policy"]["typo"] = .2
        configs.append(config)
        config = router.load_config()
        del config["departments"]["other"]
        configs.append(config)
        config = router.load_config()
        config["departments"]["human_review"] = "Reserved"
        configs.append(config)
        for config in configs:
            with self.subTest(config=config), self.assertRaises(router.JevError):
                router.validate_config(config)


class RunnerTests(unittest.TestCase):
    def call(self, args, evaluate=None):
        with patch("sys.stdout", new_callable=io.StringIO) as output, patch("sys.stderr", new_callable=io.StringIO) as errors, patch.object(runner, "evaluate", evaluate or unittest.mock.Mock(side_effect=AssertionError("Network must not be called"))):
            status = runner.main(args)
        return status, output.getvalue(), errors.getvalue()

    def test_default_is_offline_even_if_key_exists(self):
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "unused-test-key"}):
            status, output, errors = self.call([])
        self.assertEqual(status, 0, errors)
        records = [json.loads(line) for line in output.splitlines()]
        self.assertEqual(len(records), 6)
        self.assertTrue(all(record["mode"] == "demo_synthetic" for record in records))
        self.assertEqual(json.loads(errors)["human_review"], 3)

    def test_live_dry_run_never_needs_key_or_calls_api(self):
        with patch.dict(os.environ, {}, clear=True):
            status, output, errors = self.call(["--live", "--dry-run"])
        self.assertEqual(status, 0, errors)
        self.assertEqual(len(output.splitlines()), 6)
        self.assertIn("request", json.loads(output.splitlines()[0]))

    def test_saved_review_queue_matches_all_review_decisions_and_capture_replays(self):
        with tempfile.TemporaryDirectory() as temporary:
            directory = Path(temporary) / "run"
            status, output, errors = self.call(["--output-dir", str(directory)])
            self.assertEqual(status, 0, errors)
            records = runner.read_jsonl(directory / "decisions.jsonl")
            review = runner.read_jsonl(directory / "review-queue.jsonl")
            self.assertEqual(review, [record for record in records if record["decision"]["needs_review"]])
            status, replay, errors = self.call(["--replay", str(directory / "decisions.jsonl")])
            self.assertEqual(status, 0, errors)
            self.assertEqual([row["decision"] for row in records], [json.loads(row)["decision"] for row in replay.splitlines()])
            self.assertFalse(json.loads(errors)["quality_evidence"])
            self.assertTrue(all(json.loads(row)["source_mode"] == "demo_synthetic" for row in replay.splitlines()))
            self.assertTrue(all(json.loads(row)["quality_evidence"] is False for row in replay.splitlines()))
            self.assertEqual(self.call(["--output-dir", str(directory)])[0], 1)

    def test_replay_rejects_changed_text_model_or_questions(self):
        tickets = runner.load_tickets(PROJECT / "demo" / "tickets.jsonl")
        original = {ticket["id"]: router.build_request(ticket) for ticket in tickets}
        for field in ("message", "model", "criteria"):
            requests = copy.deepcopy(original)
            request = requests[tickets[0]["id"]]
            if field == "message":
                request["state"]["ticket"]["message"] = "Different input"
            elif field == "model":
                request["model"] = "another-model"
            else:
                request["questions"]["department"]["criteria"]["billing"] = "Different definition"
            with self.subTest(field=field), self.assertRaises(router.JevError):
                runner.load_replay(PROJECT / "demo" / "responses.jsonl", requests)

    def test_replay_allows_threshold_changes_without_inference(self):
        with tempfile.TemporaryDirectory() as temporary:
            config = router.load_config()
            config["policy"]["department_confidence_min"] = 1
            path = Path(temporary) / "config.json"
            path.write_text(json.dumps(config))
            status, output, errors = self.call(["--config", str(path)])
            self.assertEqual(status, 0, errors)
            self.assertTrue(all(json.loads(row)["decision"]["needs_review"] for row in output.splitlines()))

    def test_nonfinite_replay_is_rejected_before_output_files_are_created(self):
        with tempfile.TemporaryDirectory() as temporary:
            rows = runner.read_jsonl(PROJECT / "demo" / "responses.jsonl")
            rows[0]["response"]["unexpected_optional_statistic"] = float("nan")
            path = Path(temporary) / "responses.jsonl"
            path.write_text("".join(json.dumps(row) + "\n" for row in rows))
            destination = Path(temporary) / "output"
            status, output, errors = self.call(["--replay", str(path), "--output-dir", str(destination)])
            self.assertEqual(status, 1)
            self.assertIn("Invalid JSON", errors)
            self.assertFalse(destination.exists())

    def test_direct_synthetic_replay_preserves_provenance(self):
        status, output, errors = self.call(["--replay", str(PROJECT / "demo" / "responses.jsonl")])
        self.assertEqual(status, 0, errors)
        rows = [json.loads(line) for line in output.splitlines()]
        self.assertTrue(all(row["quality_evidence"] is False for row in rows))
        self.assertTrue(all("synthetic" in row["source_provenance"] for row in rows))

    def test_live_origin_replay_rejects_output_inside_repo(self):
        with tempfile.TemporaryDirectory() as temporary:
            rows = runner.read_jsonl(PROJECT / "demo" / "responses.jsonl")
            for row in rows:
                row["quality_evidence"] = True
                row["mode"] = "live"
            path = Path(temporary) / "capture.jsonl"
            path.write_text("".join(json.dumps(row) + "\n" for row in rows))
            status, output, errors = self.call(["--replay", str(path), "--output-dir", str(PROJECT / "output" / "replayed")])
            self.assertEqual(status, 1)
            self.assertIn("outside the public repository", errors)

    def test_service_error_queues_failed_and_remaining_tickets_without_retrying(self):
        evaluate = unittest.mock.Mock(side_effect=router.JevError("HTTP 529: provider overloaded"))
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "private-test-key"}):
            status, output, errors = self.call(["--live"], evaluate)
        self.assertEqual(status, 1)
        evaluate.assert_called_once()
        self.assertEqual(evaluate.call_args.kwargs["max_attempts"], 1)
        records = [json.loads(row) for row in output.splitlines()]
        self.assertEqual([row["status"] for row in records], ["error"] + ["not_processed"] * 5)
        self.assertTrue(all(row["decision"]["route"] == "human_review" for row in records))
        self.assertNotIn("private-test-key", output + errors)

    def test_live_budget_is_checked_before_network(self):
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "unused"}):
            status, output, errors = self.call(["--live", "--max-tickets", "5"])
        self.assertEqual(status, 1)
        self.assertEqual(output, "")
        self.assertIn("exceeds --max-tickets", errors)

    def test_all_modes_reject_output_inside_repo_including_symlinks(self):
        with tempfile.TemporaryDirectory() as temporary:
            link = Path(temporary) / "repo"
            link.symlink_to(PROJECT, target_is_directory=True)
            for mode in [[], ["--live"], ["--replay", str(PROJECT / "demo" / "responses.jsonl")]]:
                for directory in [PROJECT / "output" / "live", link / "output" / "live"]:
                    with self.subTest(directory=directory, mode=mode), patch.dict(os.environ, {"TYPESAFE_API_KEY": "unused"}):
                        status, output, errors = self.call([*mode, "--output-dir", str(directory)])
                    self.assertEqual(status, 1)
                    self.assertIn("outside the public repository", errors)

    def test_duplicate_input_ids_fail_before_live_call(self):
        with tempfile.TemporaryDirectory() as temporary:
            path = Path(temporary) / "tickets.jsonl"
            path.write_text('{"id":"same","message":"one"}\n{"id":"same","message":"two"}\n')
            status, output, errors = self.call(["--live", "--input", str(path)])
        self.assertEqual(status, 1)
        self.assertIn("unique", errors)

    def test_cli_runs_from_another_working_directory(self):
        with tempfile.TemporaryDirectory() as temporary:
            result = subprocess.run([sys.executable, str(PROJECT / "run.py")], cwd=temporary, text=True, capture_output=True)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(len(result.stdout.splitlines()), 6)


if __name__ == "__main__":
    unittest.main()
