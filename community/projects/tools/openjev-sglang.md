# openjev-sglang

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

openjev-sglang serves a Jev-shaped decision API using Qwen on SGLang. Its `jev-latest` alias routes to Qwen, not official Jev, and requests do not go to TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ekzhang/openjev-sglang) |
| Maintainer | [Eric Zhang / ekzhang](https://github.com/ekzhang). |
| Format | FastAPI service, SGLang backend integration, Modal deployment, evaluation scripts. |
| Relationship to Jev | Independent implementation of a similar HTTP interface; model behavior and confidence statistic are not official Jev. |
| Requirements | Python 3.11–3.13 and uv for API tooling; compatible SGLang GPU backend for inference. Default deployment uses a Modal B200 and requires an account. |
| License | No repository license file or license declaration was found at the reviewed commit. Public source access does not establish reuse permission; model/runtime terms are separate. |
| Disclosure | AI-assisted catalog review; contributor affiliation/commercial relationships were not supplied. Listing is not an endorsement. |

## When to use

Use this to study a self-hosted typed-question interface, selected-token probability readout, shared-prefix cache warmup, request admission, and backend failure handling.

It is relevant when comparing serving architectures or examining API migration boundaries. Unspecified code licensing must be resolved before relying on reuse rights.

## How it works

The [evaluation service](https://github.com/ekzhang/openjev-sglang/blob/604664a22b2cf44c6cc499e503092ae4e3c24c03/src/openjev/service.py) prepares shared state plus independent question branches, warms SGLang's prefix cache, and requests selected label probabilities for each branch.

Each request performs one discarded-token warmup plus one one-token request per question. It is not a zero-output-token model. [Scoring code](https://github.com/ekzhang/openjev-sglang/blob/604664a22b2cf44c6cc499e503092ae4e3c24c03/src/openjev/scoring.py) normalizes label log-probabilities, returns Noul's true probability, Choice's argmax/distribution, or Score's expected zero-based index with a legend.

The default [model configuration](https://github.com/ekzhang/openjev-sglang/blob/604664a22b2cf44c6cc499e503092ae4e3c24c03/src/openjev/defaults.py) pins NVIDIA's Qwen3.6-35B-A3B-NVFP4 weights and SGLang 0.5.19. The public model name is `Qwen/Qwen3.6-35B-A3B`; `jev-latest` is only a compatibility alias.

The [TypeSafe API](https://docs.typesafe.ai/api) is the interface reference. Source inspection establishes similar routes and answer fields, not complete semantic or wire compatibility.

## Get started

For schema inspection without GPU inference:

```sh
git clone https://github.com/ekzhang/openjev-sglang.git
cd openjev-sglang
git checkout 604664a22b2cf44c6cc499e503092ae4e3c24c03
uv sync
uv run openjev schema
```

Dependency installation requires network access. The schema command is documented to require no GPU or model download. The default `uv run pytest` selects offline tests; integration-marked tests download the real tokenizer.

For actual inference, follow [local development instructions](https://github.com/ekzhang/openjev-sglang#local-development--existing-sglang). A compatible SGLang backend must already exist, with matching model/tokenizer revision and selected-token log-probability support:

```sh
uv run openjev serve --connect http://127.0.0.1:30000
```

The [Modal instructions](https://github.com/ekzhang/openjev-sglang#run-on-modal) provide a separate hosted GPU path. Both `modal run` and deployment start billable compute; the temporary run also executes inference smoke checks. They are not offline validation commands.

After starting an inference service, submit [examples/request.json](https://github.com/ekzhang/openjev-sglang/blob/604664a22b2cf44c6cc499e503092ae4e3c24c03/examples/request.json) to its `/v1/systemone` route. The response contains typed answers and backend usage counts. `/docs`, `/openapi.json`, and `/v1/limits` expose schema and configured limits.

No install, startup, deployment, or inference command was executed during this review.

## Examples and demos

- [Example request](https://github.com/ekzhang/openjev-sglang/blob/604664a22b2cf44c6cc499e503092ae4e3c24c03/examples/request.json): supplied typed-question payload for an active endpoint.
- [Smoke runner](https://github.com/ekzhang/openjev-sglang/blob/604664a22b2cf44c6cc499e503092ae4e3c24c03/src/openjev/smoke.py): live inference checks, including all primitive types and answer-count boundaries.
- [API tests](https://github.com/ekzhang/openjev-sglang/blob/604664a22b2cf44c6cc499e503092ae4e3c24c03/tests/test_api.py) and [backend tests](https://github.com/ekzhang/openjev-sglang/blob/604664a22b2cf44c6cc499e503092ae4e3c24c03/tests/test_backend.py): synthetic checks for validation, admission, errors, and cancellation.
- [Evaluation material](https://github.com/ekzhang/openjev-sglang/tree/604664a22b2cf44c6cc499e503092ae4e3c24c03/evals): separate upstream experiments; reported quality and timing were not reproduced here.

No hosted endpoint was used for this review.

## Limits and data handling

- Distributions are conditional on selected answer labels and depend on prompt and ordering. The project's entropy-derived `confidence` is its own statistic and is not an empirically validated correctness probability.
- The inspected prompt path hides non-null Choice keys from the model, using descriptions instead. This is a potential semantic difference when option names carry information beyond descriptions.
- Default limits include 64 questions, 2–64 Choice/Score answers, body/token budgets, and concurrency bounds; these differ from other TypeSafe limits.
- Schema/context errors reject before GPU inference. Oversized bodies return 413, overload 529, and timeouts 504. Failed or canceled evaluations cancel sibling requests and attempt backend aborts.
- Prefix cache reuse is opportunistic. Missing backend cache counts remain unknown rather than being reported as zero.
- Local state is sent to your selected SGLang backend. A Modal deployment sends it to hosted infrastructure; model downloads and cached weights also use external services/storage.
- The default Modal endpoint is unauthenticated and has no explicit container cap. Configure authentication and deployment costs deliberately before exposing it; local API settings alone are not all forwarded to Modal.
- API usage counts include cache warmup and all branch prompt/output counts. They are not TypeSafe billing estimates or unique computed-token counts.

## Review and maintenance

Reviewed **2026-09-19**, commit [`604664a22b2cf44c6cc499e503092ae4e3c24c03`](https://github.com/ekzhang/openjev-sglang/tree/604664a22b2cf44c6cc499e503092ae4e3c24c03).

Inspected README, Python manifest, model/runtime pins, evaluation orchestration, scoring, API/backend error paths, and representative API/backend/prompt tests. Searched tracked files for LICENSE/COPYING and found none; `pyproject.toml` also lacked a license declaration.

Source review only: no dependencies, tests, tokenizer/model downloads, GPU service, Modal deployment, official Jev requests, or benchmarks were run. API parity, production suitability, and upstream comparison claims remain unverified.
