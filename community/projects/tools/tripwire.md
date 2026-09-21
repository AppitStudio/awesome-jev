# Tripwire

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenAI-compatible streaming proxy that watches partial LLM completions and can abort the upstream generation mid-flight. The flagship detector is TypeSafe Jev (System One); a local heuristic detector supports keyless demos.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/anuran-de/tripwire) |
| Maintainer | [anuran-de](https://github.com/anuran-de). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package **tripwire** 0.1.0 (proxy, detectors, policy engine). |
| Requirements | Python ≥ 3.11; for live Jev set `TYPESAFE_API_KEY` (default API `https://api.typesafe.ai/v1`, model `jev-latest`); upstream OpenAI-compatible chat endpoint optional for full proxy demos. |
| License | [MIT](https://github.com/anuran-de/tripwire/blob/4fa52822bab3633a36b212347819230e1067ab62/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline heuristic demo OK; pytest **53 passed**. Live TypeSafe smoke not run. Distinct from [tokengate](jev-model-tokengate.md) (client-side window gating). |

## When to use

Use it when you want to cancel a bad streaming completion early (jailbreak, policy trip) instead of paying for the full answer. Prefer [tokengate](jev-model-tokengate.md) when you only need to filter tokens before the client without cancelling upstream. Heuristic mode is for offline demos, not a neural judgment.

## How it works

A proxy sits between client and upstream chat completions. Rolling windows of the partial response go to a detector; [`src/tripwire/detectors/jev.py`](https://github.com/anuran-de/tripwire/blob/4fa52822bab3633a36b212347819230e1067ab62/src/tripwire/detectors/jev.py) POSTs typed questions to `/v1/systemone`. Policy can abort and cancel the upstream stream. Partial completion text reaches TypeSafe when the Jev detector is enabled.

## Get started

```sh
git clone https://github.com/anuran-de/tripwire.git
cd tripwire
git checkout 4fa52822bab3633a36b212347819230e1067ab62
python3 -m pip install -e ".[dev]"
python3 examples/demo_attack.py   # heuristic detector; no API keys
python3 -m pytest -q
```

For live Jev, copy `.env.example`, set `TYPESAFE_API_KEY` and an upstream chat key, then run the documented CLI/proxy entry points (billed).

## Examples and demos

- `examples/demo_attack.py`: benign stream completes; adversarial stream aborts under the heuristic detector.
- This listing: demo OK; pytest **53 passed**. No live TypeSafe call.

## Limits and data handling

Stream snippets leave the host when using the Jev detector. ~150 ms latency and token-savings figures are upstream claims, not independently measured here. Heuristic thresholds are illustrative.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 4fa5282](https://github.com/anuran-de/tripwire/tree/4fa52822bab3633a36b212347819230e1067ab62): MIT; AI-assisted source review of README, LICENSE, `src/tripwire/`, offline demo, and pytest. No live TypeSafe call.

Related: [tokengate](jev-model-tokengate.md), [toolgate](toolgate.md), [jev-shield](jev-shield.md).
