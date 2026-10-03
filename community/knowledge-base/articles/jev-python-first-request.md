# Jev Python SDK: install and inspect your first request

To make a first Jev request in Python, install `typesafe-sdk`, give it focused state and independent typed questions, then inspect the returned answers before adding actions. Start with an offline fixture; enable one live request only after you have provider access and understand where the state goes.

Based on [Moysei’s full setup article](https://x.com/0xMoysei/article/2102828260996362471), published **23 September 2026** by [Moysei](https://x.com/0xMoysei). This is an original Appit Studio guide, with AI assistance, verified on **3 October 2026**. The code, fixture, failure handling and catalog suggestions are editorial additions, not the author’s endorsement.

## Key takeaways

- One support message can support a team Choice, a frustration Score and an urgency Noul in the same request. Put the full judgment in each question; its key is only a lookup name.
- Choice and Score expose confidence; Noul exposes a yes probability. A Score is a weighted position on a zero-based rubric, so `1.2` is valid on three levels.
- Add `other` to the team options. A valid label can still be the wrong decision.
- Pin the model and retain raw answers. Missing answers, SDK errors and version surprises should produce a visible review record.
- This first program only inspects. It does not move tickets, send replies or authorize an action.

For batch economics, read [Jev setup and API costs](jev-api-cost-setup.md). For choosing and evaluating a deployment, read [the first-pilot guide](jev-system-one-first-pilot.md). This guide focuses on the installation-to-response handoff.

## Choose access before changing the client

The article recommends the [TypeSafe Playground](https://console.typesafe.ai/playground), direct Python access, or a gateway. Try synthetic text in the Playground if your account has access; do not paste a private customer ticket simply because the article suggests it. Our console visit reached sign-in, so account provisioning and Playground execution were not tested.

The code below uses TypeSafe direct access: an account, an API key and billable inference when `--live` is passed. Keep the key in `TYPESAFE_API_KEY` or your runtime secret store, outside source control. State and questions go to TypeSafe in live mode; offline mode constructs a local authored response and sends nothing.

[Vercel’s TypeSafe-compatible endpoint](https://vercel.com/docs/ai-gateway/sdks-and-apis/typesafe) is a separate access path. The [official Python usage docs](https://docs.typesafe.ai/sdk/python/usage) specify its own key, base URL and model ID. Do not assume a direct key or version ID works on every gateway. Gateway availability, pricing and version resolution need their own check; this recipe does not test them.

## Install and inspect one synthetic ticket

Requires Python **3.10+**. The recipe was executed with Python 3.12 and SDK **0.7.2**, the current [documented release](https://docs.typesafe.ai/sdk/python/changelog) at verification. Create these files in your own project, outside the catalog.

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install typesafe-sdk==0.7.2
```

Save the following as `first_request.py`. The fixture’s answers, confidence and 500-token usage are authored values, not a measurement. The three questions deliberately keep emotional frustration separate from explicit urgency.

```python
import argparse
import json

from pydantic import ValidationError
from typesafe_sdk import (
    Choice, Noul, Score, RetryPolicy, SystemOneResponse,
    TypeSafeClient, TypeSafeError,
)

MODEL = "jev-1.13.0"
STATE = "The payment integration keeps failing. Please help today."
QUESTIONS = {
    "department": Choice(
        instructions="Which team should investigate this support message?",
        criteria={
            "billing": "Charges, invoices or subscription problems",
            "technical": "Bugs or integration failures",
            "sales": "Pre-purchase pricing or product questions",
            "other": "No listed team fits, or multiple teams fit equally",
        },
    ),
    "frustration": Score(
        instructions="How frustrated does the writer sound?",
        criteria=["Calm", "Frustrated but civil", "Very angry"],
    ),
    "is_urgent": Noul(
        instructions="Does the writer explicitly request time-sensitive help?",
    ),
}

# Authored fixture: it demonstrates response reading, not model quality.
FIXTURE = {
    "model": MODEL,
    "usage": {"input_tokens": 500, "output_tokens": 0},
    "answers": {
        "department": {"type": "choice", "choice": "technical",
                       "confidence": 0.8, "probabilities": {
                           "billing": 0.05, "technical": 0.85,
                           "sales": 0.05, "other": 0.05}},
        "frustration": {"type": "score", "score": 1.2,
                        "confidence": 0.7,
                        "legend": {"0": "Calm", "1": "Frustrated but civil",
                                   "2": "Very angry"},
                        "probabilities": {"0": 0.1, "1": 0.6, "2": 0.3}},
        "is_urgent": {"type": "noul", "noul": 0.9},
    },
}


def inspect_result(result):
    if result.model != MODEL:
        raise ValueError("Unexpected model version")
    department = result.choices["department"]
    frustration = result.scores["frustration"]
    urgent = result.nouls["is_urgent"]
    if department.choice not in QUESTIONS["department"].criteria:
        raise ValueError("Unexpected department")
    return {
        "status": "inspection_only",
        "department": department.choice,
        "department_confidence": department.confidence,
        "frustration": frustration.score,
        "frustration_confidence": frustration.confidence,
        "urgent_probability": urgent.noul,
        "raw": result.model_dump(mode="json"),
    }


def run(client=None):
    try:
        result = (
            SystemOneResponse.model_validate_json(json.dumps(FIXTURE))
            if client is None else client.system_one(STATE, QUESTIONS)
        )
        return inspect_result(result)
    except (TypeSafeError, ValidationError, KeyError, ValueError):
        return {"status": "review", "reason": "request_or_response_failed"}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--live", action="store_true")
    args = parser.parse_args()
    if args.live:
        try:
            with TypeSafeClient(
                model=MODEL, timeout=5,
                retry=RetryPolicy(max_retries=0),
            ) as client:
                output = run(client)
        except TypeSafeError:
            output = {"status": "review", "reason": "client_setup_failed"}
    else:
        output = run()
    print(json.dumps(output, indent=2))
```

Run `python first_request.py`. Expect `inspection_only`, department `technical`, frustration `1.2`, urgency probability `0.9`, and a full raw response. No client or API key is needed for that fixture path. Only after you deliberately provide a key, run `python first_request.py --live`: it sends one synthetic message in one request with retries disabled and a five-second request timeout. The real answer may differ from the fixture. Client setup failure returns `review`; inference or response failure also returns `review` without pretending a decision was obtained.

The [SDK response docs](https://docs.typesafe.ai/sdk/python/api/types/responses) support the type-specific accessors used here. The [exception hierarchy](https://docs.typesafe.ai/sdk/python/api/exceptions) puts connection and timeout errors under `TypeSafeError`, alongside HTTP errors. Catching only an HTTP exception would leave some service failures outside the review path. The code intentionally reports a short reason rather than printing potentially sensitive error bodies.

Treat this as an inspection handoff. Before adding a route, define what `other`, low confidence, ambiguous urgency and missing context mean in your application. Choose thresholds on representative labeled cases and test them on untouched cases. Keep exact dates, arithmetic, permissions and ticket mutations in code; use a generative model separately if you later need a drafted reply.

## Lint the request, then study a review queue

[Wellposed](../../projects/tools/wellposed.md) is a **JevList suggestion**, not source-mentioned. Its MIT structural linter runs locally with Node 18+ and no provider key. The pinned 0.4.0 structural module returned zero findings for this recipe’s request, including its `other` option. This only establishes that its heuristics found no structural issue; it does not establish whether Jev will select the right team. Optional semantic evaluations transmit state to TypeSafe and may cost money.

The [Support Router](../../../projects/support-router/README.md) is another **JevList suggestion**, a repository-owned MIT teaching resource rather than a community Project record. Run `python3 projects/support-router/run.py` from an Awesome Jev checkout to inspect six authored tickets, three suggestions and three review entries. Its default demo needs no packages or key. Its Choice/Noul implementation and local recording policy differ from this SDK recipe; use it to learn the next handoff, not as evidence that our three-question pilot ran live. Its live mode sends messages to TypeSafe and incurs provider charges.

## Copyable build prompt

```text
Build an inspection-only Jev Python support-ticket pilot in my own project.
Inputs I will edit: synthetic ticket text, team labels/descriptions, frustration
rubric, urgency definition, model ID, and output directory. Default to Python
3.10+, typesafe-sdk==0.7.2, model jev-1.13.0 and offline authored fixtures.

Read the current primary docs first:
https://docs.typesafe.ai/sdk/python/usage
https://docs.typesafe.ai/sdk/python/api/types/responses
https://docs.typesafe.ai/sdk/python/api/exceptions
https://docs.typesafe.ai/models
https://docs.typesafe.ai/confidence

1. Create first_request.py and tests. Send only the authorized text needed by
   three independent questions: team Choice with other, frustration Score,
   explicit time-sensitive-help Noul. Fully describe each question.
2. Parse offline fixtures using SystemOneResponse.model_validate_json. Preserve
   model, distributions, raw answers and usage. Read the typed accessors. Noul
   has no confidence field; Score can be fractional. Never invent live answers.
3. Produce inspection_only records. Missing/wrong-type answers, unlisted labels,
   unexpected model versions, validation, HTTP, connection and timeout failures
   produce visible review records. Do not change tickets or send messages.
4. Wellposed is an independently suggested structural linter, not Moysei's tool:
   https://github.com/suraj-phanindra/wellposed/tree/86e6f8cb17e464eab33dcf44a0015fdb616b1fc2
   Use only its local structural path. Report heuristics separately from tests.
5. Study the MIT Support Router as a later review-queue teaching example:
   https://github.com/AppitStudio/awesome-jev/tree/main/projects/support-router
   Do not claim it implements this three-question SDK example unchanged.
6. Test normal and fractional responses, missing answers, other/unlisted labels,
   unexpected versions and service failures offline. Report exact results.
7. Keep live execution behind --live, use TYPESAFE_API_KEY from the environment,
   one synthetic ticket, no retries and a five-second request timeout. Do not
   execute it without explicit opt-in. It transmits state and may incur charges.
Deliver code, offline tests, example output, prerequisites and data-flow notes.
Record SDK/model/question versions. Future routing thresholds need labeled
validation and untouched tests; preserve authorization/actions in code. Any
reply writing belongs to a separate LLM, not the typed decision model.
```

## Validation and limits

The guide’s fixture and eight injected failure cases ran offline with SDK 0.7.2: missing Choice, Score and Noul answers, unexpected model, unlisted label, a general SDK failure, a connection failure and a timeout. Wellposed’s inspected structural module found zero issues on the request. Support Router’s separate six-fixture demo produced three suggestions, three review entries and zero errors. These checks establish response handling and local example behavior. No TypeSafe or gateway call, Playground run, billed cost, latency or model-quality evaluation was performed. The build prompt was reviewed; an agent was not run against it.

Current [TypeSafe model docs](https://docs.typesafe.ai/models), checked 3 October, list input at **$0.042 per million tokens** and free output. At an assumed 1,000 input tokens per request, 100,000 requests would therefore cost $4.20 for direct inference alone. This is arithmetic, not a bill; it excludes reviews, retries, hosting and other models. Extra questions still add input tokens, even though state is shared. The source’s “261 fixed tokens” is not a universal billing contract established here.

The article’s rate card lists 1,200 requests/minute and 250,000 tokens/second. The current official page instead lists **80 requests/second and 100,000 tokens/second**, explicitly warning that limits change dynamically. It retains a 64k total-request budget and 32k for state plus the longest question. Check your provider’s current limits and handle 429; do not size a system from the article’s dated card.

Moysei repeats vendor adoption and speed/cost claims and mentions paper judging, sponsor detection and a calibration study without outbound source identities. Those examples were not independently traced or reproduced, so their figures are not evidence for this pilot. The “no hallucinated options” argument concerns answer shape: a schema cannot guarantee the right answer. Confidence describes distribution concentration, not permission or a universal probability of correctness.

## Adoption questions

### How do I install the Jev Python SDK?

Use Python 3.10 or newer and install typesafe-sdk in an isolated environment. This guide checks version 0.7.2. Import typesafe_sdk, and supply a TypeSafe key through TYPESAFE_API_KEY only when you explicitly enable a live request.

### How do I read Choice, Score and Noul answers?

Read result.choices[name].choice, result.scores[name].score and result.nouls[name].noul. Choice and Score also have confidence and probability distributions. Noul has a yes probability without a separate confidence field; a Score can fall between rubric levels.

### Can I test the Jev SDK without an API key?

Yes. Construct authored SystemOneResponse fixtures and test response handling locally. This checks your program and SDK compatibility, not Jev accuracy, latency or billing. A real model request needs provider access and can incur charges.

### Why should my Choice include an other option?

A closed set forces a selection even when none of its categories fits. Add an explicit other or no-match option and retain it for review. A high confidence value cannot repair a missing category.

### Does a valid Jev response mean I can act on it?

No. Typed output establishes its shape, not semantic correctness or permission. Inspect raw answers, evaluate a local policy on labeled cases, and keep authorization and ticket changes in deterministic code.

## Sources, credits and corrections

- [Original article by Moysei](https://x.com/0xMoysei/article/2102828260996362471), 23 September 2026: read all 15 sections in logged-in Chrome on 3 October. Only the console was linked in the body; the unnamed benchmark projects were not matched by guesswork. Exact-title/phrase searches and the public author profile found no verified republication.
- [TypeSafe quick start](https://docs.typesafe.ai/introduction/quickstart), [Python usage](https://docs.typesafe.ai/sdk/python/usage), [responses](https://docs.typesafe.ai/sdk/python/api/types/responses), [exceptions](https://docs.typesafe.ai/sdk/python/api/exceptions), [models](https://docs.typesafe.ai/models) and [confidence](https://docs.typesafe.ai/confidence): primary references checked on 3 October. The installed SDK confirmed the recipe’s constructors and answer fields.
- [Pinned Wellposed source](https://github.com/suraj-phanindra/wellposed/tree/86e6f8cb17e464eab33dcf44a0015fdb616b1fc2), including README, MIT license and structural implementation; local Support Router README and implementation. Connections are editorial suggestions, not source-author endorsements.
- Search intent: considered “Jev Python SDK”, “install typesafe-sdk”, “Jev first request” and “Choice Score Noul Python”. Current search results emphasize setup/tutorial pages. Ahrefs was at sign-in, so no entitlement, volume or difficulty was established. JevList Search Console Web data through 29 September showed “jev install” (0 clicks, 24 impressions) and “jev sdk” (0 clicks, 6 impressions) among the first 500 rows, all countries. This small observed signal supports an installation question, not a forecast of demand. Existing broad setup and first-pilot guides are linked above.
- Guide and original CC0 diagram: Appit Studio, AI-assisted. No human reviewer recorded. The source cover was not reused: no reusable license or written permission was established. Corrections should distinguish changes in SDK/model documentation from the article’s dated claims.
