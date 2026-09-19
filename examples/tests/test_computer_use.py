# SPDX-License-Identifier: MIT
"""Synthetic policy and fixture checks, not a browser or model evaluation."""

import copy
import importlib.util
import io
import json
from pathlib import Path
import sys
import unittest
from unittest.mock import patch

EXAMPLES = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(EXAMPLES))
from jev_examples.client import JevError  # noqa: E402
from jev_examples.computer_use import apply_to_fixture, build_request, fingerprint, prepare, verify_fixture  # noqa: E402

spec = importlib.util.spec_from_file_location("computer_use_runner", EXAMPLES / "computer-use/run.py")
runner = importlib.util.module_from_spec(spec)
spec.loader.exec_module(runner)


class ComputerUseTests(unittest.TestCase):
    def setUp(self):
        self.case = json.loads((EXAMPLES / "computer-use/input.json").read_text())
        self.response = json.loads((EXAMPLES / "computer-use/mock-response.json").read_text())
        self.request = build_request(self.case)

    def choose(self, name, value, confidence=0.95):
        answer = self.response["answers"][name]
        answer.update(choice=value, confidence=confidence)
        answer["probabilities"] = {key: float(key == value) for key in answer["probabilities"]}

    def apply(self, proposal, current=None, allowed_fields=None):
        return apply_to_fixture(proposal, current or self.case["snapshot"], self.case["values"],
                                allowed_surface=self.case["snapshot"]["surface"],
                                allowed_fields={"e1", "e2"} if allowed_fields is None else allowed_fields)

    def test_fill_and_verbatim_extraction_pass_independent_fixture_oracle(self):
        before = copy.deepcopy(self.case)
        proposal = prepare(self.request, self.response)
        after = self.apply(proposal)
        self.assertEqual(proposal["extracted"]["value"], "€120.00")
        self.assertEqual(verify_fixture(self.case, after, proposal)["status"], "simulated_verified")
        self.assertEqual(self.case, before)

    def test_oracle_and_supplied_literal_are_not_in_model_state(self):
        self.assertNotIn("expected", self.request["state"])
        self.assertNotIn(self.case["values"]["billing_contact"], json.dumps(self.request))
        self.assertNotIn("e3", self.request["questions"]["field"]["criteria"])
        self.assertNotIn("submit", self.request["questions"]["operation"]["criteria"])

    def test_wrong_semantic_field_and_wrong_amount_fail_oracle(self):
        for head, selection, failed_check in [("field", "e1", "billing_value"), ("amount", "t1", "amount_source")]:
            with self.subTest(head=head):
                self.setUp()
                self.choose(head, selection)
                proposal = prepare(self.request, self.response)
                result = verify_fixture(self.case, self.apply(proposal), proposal)
                self.assertEqual(result["status"], "failed")
                self.assertFalse(result["checks"][failed_check])

    def test_done_cannot_pass_with_empty_required_field(self):
        self.choose("operation", "done")
        self.response["answers"]["field"]["confidence"] = 0.01
        proposal = prepare(self.request, self.response)
        self.assertEqual(proposal["status"], "ready")  # Unused field uncertainty is irrelevant.
        self.assertEqual(verify_fixture(self.case, self.apply(proposal), proposal)["status"], "failed")

    def test_done_can_pass_when_independent_state_already_satisfies_goal(self):
        self.case["snapshot"]["elements"][1]["value"] = self.case["values"]["billing_contact"]
        self.request = build_request(self.case)
        self.choose("operation", "done")
        proposal = prepare(self.request, self.response)
        self.assertEqual(verify_fixture(self.case, self.apply(proposal), proposal)["status"], "simulated_verified")

    def test_uncertain_or_missing_used_answers_do_not_propose_an_action(self):
        for head in ("operation", "field", "amount"):
            with self.subTest(head=head):
                self.setUp()
                self.response["answers"][head]["confidence"] = 0.799
                self.assertEqual(prepare(self.request, self.response)["status"], "human_review")
        for head in ("field", "amount"):
            self.setUp()
            self.choose(head, "none")
            self.assertEqual(prepare(self.request, self.response)["status"], "human_review")

    def test_wait_and_blocked_stop_without_using_speculative_targets(self):
        for operation in ("wait", "blocked"):
            self.choose("operation", operation)
            self.response["answers"]["field"]["confidence"] = 0.01
            self.assertEqual(prepare(self.request, self.response)["status"], operation)

    def test_stale_state_and_surface_change_refuse_execution(self):
        proposal = prepare(self.request, self.response)
        for key, value in [("revision", 2), ("surface", "https://other.example.invalid")]:
            current = copy.deepcopy(self.case["snapshot"])
            current[key] = value
            with self.assertRaises(JevError):
                self.apply(proposal, current)

    def test_permissions_are_rechecked_by_executor(self):
        proposal = prepare(self.request, self.response)
        with self.assertRaises(JevError):
            self.apply(proposal, allowed_fields=set())
        for action in [{"kind": "submit", "target_id": "e3"}, {"kind": "fill", "target_id": "e3"}]:
            proposal["action"] = action
            with self.assertRaises(JevError):
                self.apply(proposal)

    def test_disabled_field_never_reaches_executor(self):
        self.case["snapshot"]["elements"][1]["enabled"] = False
        proposal = prepare(self.request, self.response)
        with self.assertRaisesRegex(JevError, "Stale observation"):
            self.apply(proposal)
        # Even a proposal tied to this snapshot cannot edit a disabled control.
        proposal["snapshot_hash"] = fingerprint(self.case["snapshot"])
        with self.assertRaisesRegex(JevError, "missing, disabled or not editable"):
            self.apply(proposal)

    def test_malformed_or_missing_answers_are_rejected(self):
        for change in ("missing", "unknown", "nonfinite"):
            self.setUp()
            if change == "missing":
                del self.response["answers"]["field"]
            elif change == "unknown":
                self.response["answers"]["operation"]["choice"] = "submit"
            else:
                self.response["answers"]["amount"]["confidence"] = float("nan")
            with self.assertRaises(JevError):
                prepare(self.request, self.response)

    def test_default_and_payload_preview_cannot_call_provider(self):
        with patch.object(runner, "evaluate", side_effect=AssertionError("Unexpected network")), patch("sys.stdout", new_callable=io.StringIO):
            self.assertEqual(runner.main([]), 0)
            self.assertEqual(runner.main(["--show-request", "--live"]), 0)

    def test_live_is_one_attempt_and_service_failure_cannot_act(self):
        with patch.object(runner, "evaluate", side_effect=JevError("Unavailable")) as call, \
                patch.object(runner, "apply_to_fixture") as execute, patch("sys.stderr", new_callable=io.StringIO):
            self.assertEqual(runner.main(["--live"]), 1)
            self.assertEqual(call.call_args.kwargs["max_attempts"], 1)
            execute.assert_not_called()


if __name__ == "__main__":
    unittest.main()
