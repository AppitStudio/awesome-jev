# Runport (local-first benchmarking of LLMs, prompts and workflows, with a strict Jev adapter and hard spend caps)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first platform that benchmarks any API or workflow (OpenRouter, OpenAI-compatible, local models, Dify, n8n, custom HTTP) on your own labelled dataset, scoring only against human-approved ground truth, with fail-closed spend caps and typed approval before live calls. It includes a dedicated adapter for Jev on OpenRouter's Decisions API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sudharsanselvaraj/Runport) |
| Maintainer | [Sudharsanselvaraj](https://github.com/Sudharsanselvaraj). Independently curated. |
| Format | Python CLI + terminal UI |
| Requirements | Python 3.11 or 3.12 with uv; `OPENROUTER_API_KEY` for the Jev adapter and keys for any other targets. |
| License | [Apache-2.0](https://github.com/Sudharsanselvaraj/Runport/blob/42e8a81db620b20c807549169b7b27524e769957/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/runport/classification/jev_adapter.py`](https://github.com/Sudharsanselvaraj/Runport/blob/42e8a81db620b20c807549169b7b27524e769957/src/runport/classification/jev_adapter.py) at the pinned commit. |

## When to use

- Compare Jev with chat models or workflows on your own labelled classification set without runaway spend.
- Mismatch: needs human-approved annotations; live runs require typing an approval phrase.

## How it works

`src/runport/classification/jev_adapter.py` posts `model`, `state` and `questions` to `https://openrouter.ai/api/alpha/decisions` (`typesafe/jev-1.14`) and parses the response strictly, failing a case rather than guessing; results feed Runport's metrics and its spend ledger. Integration evidence: [`src/runport/classification/jev_adapter.py`](https://github.com/Sudharsanselvaraj/Runport/blob/42e8a81db620b20c807549169b7b27524e769957/src/runport/classification/jev_adapter.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Sudharsanselvaraj/runport.git
cd runport
uv sync
uv run runport smoke-test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev Decisions API plugin example: [github.com/Sudharsanselvaraj/Runport/tree/main/examples/plugins/jev_decisions_api](https://github.com/Sudharsanselvaraj/Runport/tree/main/examples/plugins/jev_decisions_api)

## Limits and data handling

Benchmark inputs are sent to OpenRouter (Jev) and the other targets you configure, only after live authorization. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 42e8a81db620](https://github.com/Sudharsanselvaraj/Runport/tree/42e8a81db620b20c807549169b7b27524e769957). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
