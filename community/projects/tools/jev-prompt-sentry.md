# jev-prompt-sentry

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Ingress reverse proxy for Anthropic Messages: one batched TypeSafe Jev call screens jailbreaks, indirect injections, and exfil risk before the request reaches an expensive chat model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ca7ai/jev-prompt-sentry) |
| Maintainer | [ca7ai](https://github.com/ca7ai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **jev-prompt-sentry 0.1.0** (FastAPI/uvicorn app `jev_prompt_sentry.app:app`). |
| Requirements | Python ≥ 3.12; `TYPESAFE_API_KEY`; run via `uv run … uvicorn … --env-file .env`. Proxies `POST /v1/messages` and forwards the caller’s Anthropic auth headers unchanged. |
| License | [PolyForm Noncommercial 1.0.0](https://github.com/ca7ai/jev-prompt-sentry/blob/b5128299fc811810af8c6a99ac60787709217689/LICENSE) (source-available; commercial use restricted—read the license). |

## When to use

Use it when you want a local/guardrail proxy in front of Anthropic’s Messages API that returns typed Jev probabilities into a code-owned block policy. Prefer [semgate](semgate.md) for Go `net/http` middlewares over arbitrary handlers, or [toolgate](toolgate.md) / [pi-jev-sentinel](pi-jev-sentinel.md) for coding-agent tool/result gates. This is not a general OpenAI-compatible gateway.

## How it works

The guard builds a structured `state` with trust zones and asks four parallel System One questions (`is_jailbreak`, `is_indirect_injection`, `data_exfil_risk`, `is_guard_manipulation`) via `typesafe-sdk`, then applies configurable thresholds (OR logic). Blocked requests never hit Anthropic; allowed ones are forwarded with the original API key headers. Design and calibration notes live in [`docs/design.md`](https://github.com/ca7ai/jev-prompt-sentry/blob/b5128299fc811810af8c6a99ac60787709217689/docs/design.md). Upstream publishes recorded corpus metrics; treat them as author-reported, not independently reproduced here.

## Get started

```sh
git clone https://github.com/ca7ai/jev-prompt-sentry.git
cd jev-prompt-sentry
git checkout b5128299fc811810af8c6a99ac60787709217689
cp .env.example .env   # set TYPESAFE_API_KEY
uv run --python 3.12 uvicorn jev_prompt_sentry.app:app --env-file .env --port 8000
# Point Anthropic SDK base_url at http://localhost:8000
```

Live guarding sends prompt/content excerpts to TypeSafe and can incur charges; forwarding still uses the caller’s Anthropic credentials. This listing did not start the proxy or call providers.

## Examples and demos

- README threshold tables and SDK `base_url` snippet.
- Offline tests under [`tests/`](https://github.com/ca7ai/jev-prompt-sentry/tree/b5128299fc811810af8c6a99ac60787709217689/tests) (policy, extract, app, bench fixtures).
- Benchmark harness under `bench/` (optional datasets; live).

## Limits and data handling

User/untrusted content leaves the proxy for TypeSafe on each guarded request. PolyForm Noncommercial limits commercial deployment—confirm terms before production. Upstream documents missed-attack rates and that the 150ms latency target was not met at publish time. Thresholds are tunable; defaults are not a security guarantee.

## Review and maintenance

Reviewed on **2026-09-20** at [commit b512829](https://github.com/ca7ai/jev-prompt-sentry/tree/b5128299fc811810af8c6a99ac60787709217689): **0.1.0**, PolyForm Noncommercial 1.0.0. AI-assisted source review of README, `pyproject.toml`, license, and tests layout. No `pytest`, no live TypeSafe/Anthropic traffic on the review host.

Related: [semgate](semgate.md), [toolgate](toolgate.md), [pi-jev-sentinel](pi-jev-sentinel.md).
