# ToolDiscoveryBench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark of how accurately and quickly a router picks the right MCP tool: the same golden questions run against real MCP tool catalogs (with seeded distractors at several catalog sizes) through TypeSafe Jev (flat, factored and hierarchical strategies), Strands Agents LLM tool calling, BM25 and embeddings, reporting accuracy, latency, cost and Jev calibration (ECE, Brier).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SarathChandraBellam/ToolDiscoveryBench) |
| Maintainer | [SarathChandraBellam](https://github.com/SarathChandraBellam). Independently curated. |
| Format | Python benchmark CLI (`uv run tdb ...`) |
| Requirements | Python 3.12 with uv; `TYPESAFE_API_KEY` for Jev routers, AWS credentials for Strands; baselines run free. |
| License | [MIT](https://github.com/SarathChandraBellam/ToolDiscoveryBench/blob/e8e81886734f3d965972200a28a546267c6582bf/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Decide whether Jev should route tools in your agent at your catalog size.
- Mismatch: results depend on the bundled golden set; missing routers are skipped, not scored.

## How it works

[`src/tooldiscoverybench/routers/jev/router.py`](https://github.com/SarathChandraBellam/ToolDiscoveryBench/blob/e8e81886734f3d965972200a28a546267c6582bf/src/tooldiscoverybench/routers/jev/router.py) implements the Jev strategies; [`docs/metrics.md`](https://github.com/SarathChandraBellam/ToolDiscoveryBench/blob/e8e81886734f3d965972200a28a546267c6582bf/docs/metrics.md) defines the metrics; golden set in [`data/golden/public_v1.jsonl`](https://github.com/SarathChandraBellam/ToolDiscoveryBench/blob/e8e81886734f3d965972200a28a546267c6582bf/data/golden/public_v1.jsonl).

## Get started

Run a smoke test (README *Quick start*):

```sh
git clone https://github.com/SarathChandraBellam/ToolDiscoveryBench.git && cd ToolDiscoveryBench
uv sync --extra strands
cp .env.example .env   # add keys
uv run tdb run --limit 5
```

Jev and Strands routers bill your keys; BM25/embeddings are free.

## Examples and demos

- Router docs: [`docs/routers.md`](https://github.com/SarathChandraBellam/ToolDiscoveryBench/blob/e8e81886734f3d965972200a28a546267c6582bf/docs/routers.md).

## Limits and data handling

Questions and tool descriptions go to TypeSafe / AWS. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit e8e81886734f](https://github.com/SarathChandraBellam/ToolDiscoveryBench/tree/e8e81886734f3d965972200a28a546267c6582bf). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
