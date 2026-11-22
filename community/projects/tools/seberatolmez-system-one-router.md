# System One Router by Berat Ölmez (self-hosted OpenRouter-compatible gateway where Jev picks the model tier for each request)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An OpenRouter-compatible LLM gateway you host yourself. Explicit model IDs pass through to OpenRouter; the virtual models `system-one/auto`, `fast`, `balanced` and `reasoning` resolve through the Jev decision engine, a deterministic policy engine and a model registry to a concrete model. SSE streaming is supported, and an evaluation runner compares routing strategies on the same JSONL dataset.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/seberatolmez/system-one-router) |
| Maintainer | [seberatolmez](https://github.com/seberatolmez). Independently curated. |
| Format | Python service (FastAPI) + evaluation CLI |
| Requirements | Python with uv (or Docker); an OpenRouter key, which also serves Jev through OpenRouter's decisions API. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/system_one/routing/decision/jev.py`](https://github.com/seberatolmez/system-one-router/blob/dd2a8758230f7eae420157e0e05759bf3794d31f/src/system_one/routing/decision/jev.py) at the pinned commit. |

## When to use

- Route chat requests to a cheap or a reasoning model automatically, with the decision logged and testable.
- Mismatch: hosted routing; you run and secure this gateway yourself.

## How it works

`src/system_one/routing/decision/jev.py` posts a code-owned decision request to `<JEV_BASE_URL>/decisions` (default `https://openrouter.ai/api/alpha`, model `~typesafe/jev-latest`) and maps the answers to a validated tier; policies in `policies/` and the registry in `registry/models.yaml` choose the concrete model. Integration evidence: [`src/system_one/routing/decision/jev.py`](https://github.com/seberatolmez/system-one-router/blob/dd2a8758230f7eae420157e0e05759bf3794d31f/src/system_one/routing/decision/jev.py).

## Get started

Install, add your OpenRouter key and a gateway key to `.env`, run the service and send the example request.

```sh
git clone https://github.com/seberatolmez/system-one-router && cd system-one-router
uv sync
cp .env.example .env   # OPENROUTER_API_KEY, SYSTEM_ONE_API_KEY
uv run uvicorn system_one.main:app --reload
sh examples/curl/chat-completion.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model registry: [github.com/seberatolmez/system-one-router/blob/dd2a8758230f7eae420157e0e05759bf3794d31f/registry/models.yaml](https://github.com/seberatolmez/system-one-router/blob/dd2a8758230f7eae420157e0e05759bf3794d31f/registry/models.yaml)
- Evaluation reports: [github.com/seberatolmez/system-one-router/tree/dd2a8758230f7eae420157e0e05759bf3794d31f/evaluations/reports](https://github.com/seberatolmez/system-one-router/tree/dd2a8758230f7eae420157e0e05759bf3794d31f/evaluations/reports)

## Limits and data handling

Prompts go to OpenRouter (and to Jev via OpenRouter for the routing decision). Early project. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit dd2a8758230f](https://github.com/seberatolmez/system-one-router/tree/dd2a8758230f7eae420157e0e05759bf3794d31f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
