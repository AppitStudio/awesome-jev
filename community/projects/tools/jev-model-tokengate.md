# tokengate (jev-model-tokengate)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Streaming LLM proxy that holds tokens in a sliding buffer, runs semantic safety criteria (TypeSafe Jev by default) on each window, and releases or aborts **before** violating tokens reach the client—demonstrating inline interception versus post-hoc redaction.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Thanh-Mathieu95/jev-model-tokengate) |
| Maintainer | [Thanh-Mathieu95](https://github.com/Thanh-Mathieu95). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js **tokengate 0.1.0** — OpenAI-compatible streaming proxy (`server.js` / Docker), local heuristic fallback, optional Claude evaluator path. |
| Requirements | Node.js **18+** (review host used 22); `JEV_API_KEY` for the Jev engine (falls back to local heuristics without a key). Optional Anthropic SDK path for alternate evaluator. |
| License | [MIT](https://github.com/Thanh-Mathieu95/jev-model-tokengate/blob/6eafc9a87740a717a6812740675347b00eafdb40/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `node test.js` inspected; live TypeSafe calls and Docker upstream demos were not run. README is primarily Vietnamese; behavior summarized from code and docs. |

## When to use

Use it to study **pre-release** streaming moderation: secrets/PII must not paint to the UI while a slower classifier thinks. Prefer [jev-shield](jev-shield.md) / [toolgate](toolgate.md) / [jev-guard](jev-guard.md) for agent tool-call firewalls rather than token-stream proxies. Prefer [jev-prompt-sentry](jev-prompt-sentry.md) for Anthropic Messages reverse-proxy screening of full prompts.

## How it works

Upstream chat-completions chunks enter a sliding buffer. When the window is full, [`evaluator.js`](https://github.com/Thanh-Mathieu95/jev-model-tokengate/blob/6eafc9a87740a717a6812740675347b00eafdb40/evaluator.js) posts one batched TypeSafe `POST https://api.typesafe.ai/v1/systemone` request (`jev-latest` by default) with multiple noul safety criteria. All-pass releases the batch; failure aborts the client stream (`finish_reason: content_filter`) and can signal upstream abort. Without `JEV_API_KEY` (or on timeout), a local heuristic path is used—the stream stays closed until evaluation returns rather than leaking tokens. `tool_calls` argument text is also screened.

## Get started

```sh
git clone https://github.com/Thanh-Mathieu95/jev-model-tokengate.git
cd jev-model-tokengate
git checkout 6eafc9a87740a717a6812740675347b00eafdb40
npm ci
# offline checks (no live key required for the default suite):
node test.js
```

Docker form (live): build the image, set `JEV_API_KEY` and `UPSTREAM_URL`, point an OpenAI client `base_url` at `http://localhost:8787/v1`. Live Jev sends buffered text windows to TypeSafe and can incur charges; this listing did not run Docker or live Jev.

## Examples and demos

- Offline `node test.js` — zero-leakage scenarios, sliding window, and local-latency checks (passed on the review host with deps installed).
- README race-benchmark figure comparing post-hoc redaction vs tokengate (author-reported; not re-measured here).
- `test-proxy.js` / `test-config.js` additional offline suites (not all re-run beyond `test.js`).

## Limits and data handling

Upstream positions this as an architecture demonstration, not a production guardrail (no multi-tenant auth/rate-limit story). Inline latency to a remote Jev endpoint is network-bound; author-reported ~300ms vs a ≤35ms KPI is disclosed as unmet without edge co-location. Buffered stream text leaves the host when Jev runs. Accuracy/cost figures in the README were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 6eafc9a](https://github.com/Thanh-Mathieu95/jev-model-tokengate/tree/6eafc9a87740a717a6812740675347b00eafdb40): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `evaluator.js`, and proxy entrypoints. Ran `npm ci` and `node test.js` (pass). No live TypeSafe calls.

Related: [jev-shield](jev-shield.md), [jev-prompt-sentry](jev-prompt-sentry.md), [toolgate](toolgate.md).
