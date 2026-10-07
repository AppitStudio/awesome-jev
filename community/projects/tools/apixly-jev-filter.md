# Jev Filter (Apixly)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Semantic filtering for AI agent tools: npm package `@apixly/jev-filter` (CLI, Python library, MCP server) turns large tool outputs, retrieved records, code and logs into compact typed TypeSafe Jev decisions with source IDs, local originals and receipts before they enter an agent's context; batched requests and maintainer-run A/B benchmarks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/apixly-ai/jev-filter) |
| Product homepage | [apixly-ai.github.io](https://apixly-ai.github.io/jev-filter/) |
| Maintainer | [Apixly](https://github.com/apixly-ai). Independently curated. |
| Format | npm package `@apixly/jev-filter` (0.4.1 at review) bundling the Python `jev_context` library, CLI and MCP server; docs site |
| Requirements | Node.js 22+ on macOS/Linux (WSL on Windows; Python included in the npm distribution) and a `TYPESAFE_API_KEY` for inference. |
| License | [MIT](https://github.com/apixly-ai/jev-filter/blob/122efb3faa45f37ae4ad7c574bdf18591b03a857/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Filter search results, logs or diffs against a task before handing them to Claude Code, Codex or another agent.
- Keep a traceable receipt of which source IDs were selected and why.
- Mismatch: benchmark claims (speed, context reduction) are the maintainer's paid A/B runs.

## How it works

Programs collect candidates; [`batch.py`](https://github.com/apixly-ai/jev-filter/blob/122efb3faa45f37ae4ad7c574bdf18591b03a857/src/jev_context/batch.py) shares task context across bounded batches and [`provider.py`](https://github.com/apixly-ai/jev-filter/blob/122efb3faa45f37ae4ad7c574bdf18591b03a857/src/jev_context/provider.py) calls Jev; [`mcp.py`](https://github.com/apixly-ai/jev-filter/blob/122efb3faa45f37ae4ad7c574bdf18591b03a857/src/jev_context/mcp.py) exposes the same contract to agents. Results return typed answers and source IDs while originals stay local.

## Get started

Install and run a query (README *Quick start*):

```sh
npm install -g @apixly/jev-filter
jev-filter doctor
export TYPESAFE_API_KEY=...
jev-filter query --input records.json --mode choose --task 'Choose the CURRENT unresolved DNS failure'
```

Each batch is a Jev request billed to your TypeSafe key; `doctor` and installation are offline.

## Examples and demos

- Docs: [apixly-ai.github.io/jev-filter](https://apixly-ai.github.io/jev-filter/) (practical tutorials).
- Benchmark results: [`benchmarks/results/`](https://github.com/apixly-ai/jev-filter/tree/122efb3faa45f37ae4ad7c574bdf18591b03a857/benchmarks/results).

## Limits and data handling

Candidate records are sent to TypeSafe; originals stay local. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 122efb3faa45](https://github.com/apixly-ai/jev-filter/tree/122efb3faa45f37ae4ad7c574bdf18591b03a857). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
