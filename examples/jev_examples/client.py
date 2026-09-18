# SPDX-License-Identifier: MIT
"""Minimal HTTP teaching client; see TypeSafe's SDK for a full client."""

import email.utils
import json
import math
import random
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone

ENDPOINT = "https://api.typesafe.ai/v1/systemone"
MODEL = "jev-1.13.0"
MAX_RESPONSE_BYTES = 1_000_000


class JevError(Exception):
    """A request or response cannot be used safely by the example."""


def reject_nonfinite_json(_value):
    raise ValueError("Non-finite constants are not valid JSON")


class NoRedirects(urllib.request.HTTPRedirectHandler):
    """Do not forward an API key through HTTP redirects."""

    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def number(value, label, low=0, high=1):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise JevError(f"{label} must be a number")
    # Bound integers before math.isfinite converts them to floats.
    if not low <= value <= high or not math.isfinite(value):
        raise JevError(f"{label} must be finite and between {low} and {high}")
    return value


def validate_response(request, response):
    """Validate only the contract needed by these recipes, allowing extra fields."""
    if not isinstance(response, dict) or not isinstance(response.get("model"), str):
        raise JevError("Response must contain a model name")
    answers = response.get("answers")
    questions = request["questions"]
    if not isinstance(answers, dict) or set(answers) != set(questions):
        raise JevError("Response answer IDs must match the requested question IDs")
    for name, question in questions.items():
        answer = answers[name]
        kind = question["type"]
        if not isinstance(answer, dict) or answer.get("type") != kind:
            raise JevError(f"{name}: answer type does not match the question")
        if kind == "noul":
            number(answer.get("noul"), f"{name}.noul")
            continue
        number(answer.get("confidence"), f"{name}.confidence")
        criteria = question["criteria"]
        expected_keys = set(criteria) if kind == "choice" else {str(i) for i in range(len(criteria))}
        probabilities = answer.get("probabilities")
        if not isinstance(probabilities, dict) or set(probabilities) != expected_keys:
            raise JevError(f"{name}: probabilities do not match the criteria")
        for key, value in probabilities.items():
            number(value, f"{name}.probabilities.{key}")
        if not math.isclose(sum(probabilities.values()), 1, abs_tol=0.001):
            raise JevError(f"{name}: probabilities must sum to one")
        if kind == "choice":
            choice = answer.get("choice")
            if not isinstance(choice, str) or choice not in expected_keys:
                raise JevError(f"{name}: choice is not one of the offered options")
            if probabilities[choice] + 0.001 < max(probabilities.values()):
                raise JevError(f"{name}: choice is not a highest-probability option")
        elif kind == "score":
            expected_legend = {str(i): label for i, label in enumerate(criteria)}
            if answer.get("legend") != expected_legend:
                raise JevError(f"{name}: score legend does not match the rubric")
            score = number(answer.get("score"), f"{name}.score", high=len(criteria) - 1)
            expected_score = sum(int(key) * value for key, value in probabilities.items())
            if not math.isclose(score, expected_score, abs_tol=0.001):
                raise JevError(f"{name}: score does not match its weighted probabilities")
        else:
            raise JevError(f"Unsupported question type: {kind}")
    usage = response.get("usage")
    if not isinstance(usage, dict):
        raise JevError("Response must contain token usage")
    for key in ("input_tokens", "output_tokens"):
        value = usage.get(key)
        if isinstance(value, bool) or not isinstance(value, int) or value < 0:
            raise JevError(f"usage.{key} must be a non-negative integer")
    return answers


def retry_delay(header, attempt):
    """Honor Retry-After when present; refuse waits over 30 seconds."""
    if header:
        try:
            delay = float(header)
        except ValueError:
            try:
                when = email.utils.parsedate_to_datetime(header)
                if when.tzinfo is None:
                    when = when.replace(tzinfo=timezone.utc)
                delay = (when - datetime.now(timezone.utc)).total_seconds()
            except (ValueError, TypeError, OverflowError):
                delay = 2 ** attempt + random.uniform(0, 0.25)
        if not math.isfinite(delay) or delay > 30:
            raise JevError("Server requested a long retry delay; try again later")
        return max(0, delay)
    return 2 ** attempt + random.uniform(0, 0.25)


def evaluate(request, api_key, *, open_url=None, sleep=time.sleep, max_attempts=3):
    """Make one to three attempts; only 429/529 receive automatic retries."""
    if isinstance(max_attempts, bool) or not isinstance(max_attempts, int) or not 1 <= max_attempts <= 3:
        raise JevError("max_attempts must be an integer between one and three")
    if not isinstance(api_key, str) or not api_key.strip():
        raise JevError("Live mode requires TYPESAFE_API_KEY")
    if any(ord(character) < 33 or ord(character) > 126 for character in api_key):
        # urllib can include the raw Authorization value in invalid-header errors.
        raise JevError("TYPESAFE_API_KEY must contain only printable ASCII token characters without spaces")
    if open_url is None:
        open_url = urllib.request.build_opener(NoRedirects()).open
    http_request = urllib.request.Request(
        ENDPOINT,
        data=json.dumps(request, allow_nan=False).encode("utf-8"),
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
        method="POST",
    )
    for attempt in range(max_attempts):
        try:
            with open_url(http_request, timeout=30) as response:
                body = response.read(MAX_RESPONSE_BYTES + 1)
            if len(body) > MAX_RESPONSE_BYTES:
                raise JevError("Response exceeded the example client's size limit")
            try:
                result = json.loads(body, parse_constant=reject_nonfinite_json)
            except (ValueError, UnicodeError) as error:
                raise JevError("API returned invalid JSON") from error
            validate_response(request, result)
            return result
        except urllib.error.HTTPError as error:
            status = error.code
            header = error.headers.get("Retry-After") if error.headers else None
            error.close()
            if status in (429, 529) and attempt < max_attempts - 1:
                sleep(retry_delay(header, attempt))
                continue
            advice = {
                401: "check the API key",
                422: "check the request against the API reference",
                429: "rate limit reached; try again later",
                529: "provider overloaded; try again later",
            }.get(status, "consult the provider's API documentation")
            # Do not echo response bodies, which can contain submitted content.
            raise JevError(f"HTTP {status}: {advice}") from None
        except (urllib.error.URLError, TimeoutError, OSError):
            # A lost response may already have been processed; avoid blind retries.
            raise JevError("Network request failed; no automatic retry was attempted") from None
    raise JevError("Retry limit reached")
