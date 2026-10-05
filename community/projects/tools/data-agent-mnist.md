# Data Agent MNIST (ClickHouse)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

ClickHouse's harness for building an agentic-analytics benchmark from your own data warehouse, with two optional Jev tools: schema-retrieval ranking (one yes/no per table) and failure-mode labeling of graded runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ClickHouse/data-agent-mnist) |
| Product homepage | [clickhouse.com](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) |
| Maintainer | [ClickHouse](https://github.com/ClickHouse). Independently curated. |
| Format | Benchmark harness (scripts + config), not a fixed benchmark |
| Requirements | Python with `uv`, access to a ClickHouse warehouse (or the examples), model-provider keys for candidate agents; `TYPESAFE_API_KEY` for the optional Jev tools (`TYPESAFE_BASE_URL` for a gateway). |
| License | [Apache-2.0](https://github.com/ClickHouse/data-agent-mnist/blob/35fc27e7d8f3ad9f6ad61db9b488e97e18855ce6/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Measure whether a data agent picks the right tables, and whether a Jev-ranked schema shortlist helps it.
- Label why graded agent runs failed without spending an LLM call per cell.
- Mismatch: the Jev tools are optional add-ons; the core benchmark runs without them.

## How it works

`schema_retrieval.py` asks Jev one yes/no question per table about whether it is needed for a question and scores the ranking against the gold SQL's tables (nDCG@10, recall@k); `schema_retrieval_agent.py` feeds the ranking to the agent up front or when it diverges onto a low-ranked table. `label_failure_modes.py` labels each failed cell with a sub-mode, the stated rule that would have prevented it, and whether the grader erred, using rules from `config/rules.example.yaml` ([README](https://github.com/ClickHouse/data-agent-mnist/blob/35fc27e7d8f3ad9f6ad61db9b488e97e18855ce6/README.md#optional-ranking-and-labeling-with-jev)).

## Get started

Install with the Jev extra and run the schema-retrieval scorer (live TypeSafe calls):

```sh
git clone https://github.com/ClickHouse/data-agent-mnist.git && cd data-agent-mnist
uv sync --extra jev
export TYPESAFE_API_KEY=...
uv run schema_retrieval.py --table-namespaces marts,crm
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README sections *Optional: ranking and labeling with Jev* and *What a run checks before it spends money*.
- [ClickHouse blog post](https://clickhouse.com/blog/agentic-analytics-benchmark-data-agent-mnist) introducing the harness.

## Limits and data handling

Table schemas and graded-run details are sent to TypeSafe when the Jev tools run. No results for the Jev tools are claimed in this listing; run them on your own warehouse. Not executed on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 35fc27e7d8f3](https://github.com/ClickHouse/data-agent-mnist/tree/35fc27e7d8f3ad9f6ad61db9b488e97e18855ce6). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
