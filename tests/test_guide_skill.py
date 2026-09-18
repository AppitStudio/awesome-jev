# SPDX-License-Identifier: MIT
"""Exercise the onboarding helper without any provider requests or real credentials."""

from contextlib import redirect_stderr, redirect_stdout
import getpass
import importlib.util
import io
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import warnings


ROOT = Path(__file__).resolve().parents[1]
HELPER = ROOT / "skills/awesome-jev-guide/scripts/try_example.py"
spec = importlib.util.spec_from_file_location("guide_example", HELPER)
guide = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guide)
client, recipes = guide.load_runtime(ROOT)


class GuideExampleTests(unittest.TestCase):
    def run_helper(self, *arguments):
        stdout, stderr = io.StringIO(), io.StringIO()
        with redirect_stdout(stdout), redirect_stderr(stderr):
            status = guide.main(["support-routing", "--repo", str(ROOT), *arguments])
        return status, stdout.getvalue(), stderr.getvalue()

    def test_every_mock_recipe_runs_without_key_or_network(self):
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "unused-private-value"}), \
                patch.object(guide, "private_key", side_effect=AssertionError("Key read")), \
                patch.object(client, "evaluate", side_effect=AssertionError("Network call")):
            for recipe in guide.RECIPES:
                with self.subTest(recipe=recipe):
                    output = io.StringIO()
                    with redirect_stdout(output):
                        self.assertEqual(guide.main([recipe, "--repo", str(ROOT)]), 0)
                    result = json.loads(output.getvalue())
                    self.assertIn("synthetic", result["mode"])
                    self.assertEqual(result["http_attempt_budget"], 0)
                    self.assertNotIn("unused-private-value", output.getvalue())

    def test_request_preview_overrides_live_without_key_or_network(self):
        with patch.object(guide, "private_key", side_effect=AssertionError("Key read")), \
                patch.object(client, "evaluate", side_effect=AssertionError("Network call")):
            status, output, error = self.run_helper("--live", "--show-request", "--model", "explicit-test-model")
        self.assertEqual(status, 0)
        self.assertEqual(json.loads(output)["model"], "explicit-test-model")
        self.assertEqual(error, "")

    def test_live_uses_one_attempt_and_reports_versions_without_key(self):
        fixture = json.loads((ROOT / "examples/support-routing/mock-response.json").read_text())
        with patch.dict(os.environ, {"TYPESAFE_API_KEY": "private-sentinel"}), \
                patch.object(guide.getpass, "getpass", side_effect=AssertionError("Unexpected prompt")), \
                patch.object(client, "evaluate", return_value=fixture) as evaluate:
            status, output, error = self.run_helper("--live", "--model", "deliberate-model")
        self.assertEqual(status, 0)
        self.assertEqual(evaluate.call_count, 1)
        self.assertEqual(evaluate.call_args.kwargs, {"max_attempts": 1})
        self.assertEqual(evaluate.call_args.args[1], "private-sentinel")
        result = json.loads(output)
        self.assertEqual(result["requested_model"], "deliberate-model")
        self.assertEqual(result["returned_model"], fixture["model"])
        self.assertNotIn("private-sentinel", output + error)

    def test_missing_key_noninteractive_stops_without_prompt_or_network(self):
        with patch.dict(os.environ, {}, clear=True), \
                patch.object(guide.sys.stdin, "isatty", return_value=False), \
                patch.object(guide.getpass, "getpass", side_effect=AssertionError("Unexpected prompt")), \
                patch.object(client, "evaluate") as evaluate:
            status, output, error = self.run_helper("--live")
        self.assertEqual(status, 1)
        evaluate.assert_not_called()
        self.assertEqual(output, "")
        self.assertIn("interactive terminal", error)

    def test_hidden_prompt_does_not_persist_key(self):
        with patch.dict(os.environ, {}, clear=True), \
                patch.object(guide.sys.stdin, "isatty", return_value=True), \
                patch.object(guide.getpass, "getpass", return_value="entered-secret"):
            self.assertEqual(guide.private_key(), "entered-secret")
            self.assertNotIn("TYPESAFE_API_KEY", os.environ)

    def test_echo_fallback_is_refused(self):
        def unavailable_prompt(*_args):
            warnings.warn("Cannot disable echo", getpass.GetPassWarning)
            raise AssertionError("Echo fallback must never run")

        with patch.dict(os.environ, {}, clear=True), \
                patch.object(guide.sys.stdin, "isatty", return_value=True), \
                patch.object(guide.getpass, "getpass", side_effect=unavailable_prompt):
            with self.assertRaisesRegex(ValueError, "hidden key prompt is unavailable"):
                guide.private_key()

    def test_service_error_stops_without_retry_or_success_output(self):
        with patch.object(guide, "private_key", return_value="private-sentinel"), \
                patch.object(client, "evaluate", side_effect=client.JevError("TypeSafe request failed (HTTP 429).")) as evaluate:
            status, output, error = self.run_helper("--live")
        self.assertEqual(status, 1)
        self.assertEqual(evaluate.call_count, 1)
        self.assertEqual(evaluate.call_args.kwargs, {"max_attempts": 1})
        self.assertEqual(output, "")
        self.assertNotIn("private-sentinel", error)

    def test_malformed_response_is_not_used_for_a_decision(self):
        with patch.object(guide, "private_key", return_value="fake-key"), \
                patch.object(client, "evaluate", return_value={}), \
                patch.object(recipes, "decide") as decide:
            status, output, _error = self.run_helper("--live")
        self.assertEqual(status, 1)
        self.assertEqual(output, "")
        decide.assert_not_called()

    def test_missing_checkout_stops_before_reading_key(self):
        with tempfile.TemporaryDirectory() as directory, \
                patch.object(guide, "private_key", side_effect=AssertionError("Key read")), \
                redirect_stderr(io.StringIO()):
            self.assertEqual(guide.main(["support-routing", "--repo", directory, "--live"]), 1)

    def test_installed_script_works_outside_the_checkout(self):
        with tempfile.TemporaryDirectory() as directory:
            copied = Path(directory) / "try_example.py"
            shutil.copy2(HELPER, copied)
            result = subprocess.run(
                [sys.executable, str(copied), "span-selection", "--repo", str(ROOT)],
                cwd=directory, capture_output=True, text=True, timeout=10,
            )
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("synthetic", json.loads(result.stdout)["mode"])


if __name__ == "__main__":
    unittest.main()
