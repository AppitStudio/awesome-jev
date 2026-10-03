# jev-gateway (TexasOct)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenAI-compatible session-aware model-routing gateway with optional typed Choice decision providers (AGPL; distinct from vinilana/jev-gateway).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TexasOct/jev-gateway) |
| Maintainer | [TexasOct](https://github.com/TexasOct). Independently curated. |
| Format | Python OpenAI-compatible model-routing gateway (AGPL-3.0) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [AGPL-3.0](https://github.com/TexasOct/jev-gateway/blob/e5cdf2b9418624ccd95a302a65beda6f41b0d443/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. AGPL-3.0. Distinct from vinilana/jev-gateway (coding-agent tool router) and from mavericksxx/jev-gateway (planning Claude proxy). Live install/inference not run on the review host. |

## When to use

Use when you want an OpenAI-compatible multi-provider gateway with task-aware routing and optional Jev-compatible decision providers. Prefer vinilana/jev-gateway when you need coding-agent tool selection launchers.

## How it works

Serves POST /v1/chat/completions; strategies (e.g. task_aware) classify work and select model pools; optional decision providers answer typed Choice questions with deterministic fallback.

## Get started

```sh
git clone https://github.com/TexasOct/jev-gateway.git
cd jev-gateway
git checkout e5cdf2b9418624ccd95a302a65beda6f41b0d443
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit e5cdf2b94186](https://github.com/TexasOct/jev-gateway/tree/e5cdf2b9418624ccd95a302a65beda6f41b0d443). AI-assisted README and license inspection; install/live paths not executed.
