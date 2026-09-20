# jev-layer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Portable System-1 decision layer for agent harnesses: host-owned routing over candidate capabilities, receipts/replay, optional supervision judgments, and fail-open integrations (Hermes, OMP, Codex, generic MCP).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/typakon4/jev-layer) |
| Maintainer | [typakon4](https://github.com/typakon4). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js package **jev-layer 0.1.0** — CLI (`jev`), stdio MCP server, harness installers, and offline `demo` provider. Published on npm. |
| Requirements | Node.js **20+**. Live TypeSafe mode needs `TYPESAFE_API_KEY` (or OpenRouter Decisions with `OPENROUTER_API_KEY`). Default `demo` provider is offline and deterministic. |
| License | [MIT](https://github.com/typakon4/jev-layer/blob/05d3cdf1f1d925d7c0bf0749caebc232f749c613/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `npm test` inspected; live TypeSafe/OpenRouter provider calls were not run. |

## When to use

Use it when an agent harness should ask a bounded chooser which capability to try next, while the host keeps permissions, execution, retries, and final results. Prefer [jev-router](jev-router.md) / [Jev Model Router](jev-model-router.md) when the goal is coding-CLI model selection rather than capability routing with receipts. Prefer [toolgate](toolgate.md) / [jev-guard](jev-guard.md) when you need tool-call firewalls rather than a portable decision MCP.

## How it works

`jev_route` selects one capability id from a host-supplied candidate set (advisory; the host validates). `jev_record_execution` joins host results to a `correlation_id` for JSONL replay under `.jev/replay/`. `jev_supervise` returns bounded work-state judgments mapped by host policy. Providers: deterministic `demo`, OpenRouter Decisions (`typesafe/jev-1.13`), or direct TypeSafe (`https://api.typesafe.ai/v1/systemone`, `jev-latest`). See [docs/PROVIDERS.md](https://github.com/typakon4/jev-layer/blob/05d3cdf1f1d925d7c0bf0749caebc232f749c613/docs/PROVIDERS.md) and [docs/AGENT-IMPLEMENTATION.md](https://github.com/typakon4/jev-layer/blob/05d3cdf1f1d925d7c0bf0749caebc232f749c613/docs/AGENT-IMPLEMENTATION.md).

## Get started

```sh
npm install --global jev-layer
# or from source at the reviewed tip:
git clone https://github.com/typakon4/jev-layer.git
cd jev-layer
git checkout 05d3cdf1f1d925d7c0bf0749caebc232f749c613
npm install
npm test
jev doctor --project /path/to/workspace
```

`jev add generic --project …` (or Hermes/OMP/Codex) wires harness config. Live TypeSafe/OpenRouter modes send states and Choice questions to the configured provider and can incur charges; this listing used the offline test suite only.

## Examples and demos

- Offline `npm test` (92 tests passed on the review host).
- `examples/` request fixtures and provider docs.
- Replay evaluation via `npm run replay:evaluate` (not re-run beyond unit tests here).

## Limits and data handling

Jev never executes a selected capability—the host must validate ids and permissions. Fail-open and supervision defaults are intentional; misconfigured hosts can still act wrongly. Remote providers receive route/supervise state text. Upstream latency/accuracy claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 05d3cdf](https://github.com/typakon4/jev-layer/tree/05d3cdf1f1d925d7c0bf0749caebc232f749c613): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, provider docs, and CLI/MCP surfaces. Ran `npm test` (92 pass). No live TypeSafe calls.

Related: [jev-router](jev-router.md), [toolgate](toolgate.md), [jev-mcp](jev-mcp.md).
