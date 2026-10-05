# Deep Recall

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Answer-aware recall over a folder of Markdown notes (Claude Code plugin + Python CLI/MCP) whose pluggable reranker can be TypeSafe Jev, scoring each passage window by the probability that it states the answer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/turlockmike/deep-recall) |
| Maintainer | [turlockmike](https://github.com/turlockmike). Independently curated. |
| Format | Claude Code plugin (MCP tools, skill, slash commands, SessionStart hook) and Python package/CLI |
| Requirements | `uv` (plugin) or Python with `uv tool install`; optional `ripgrep`. The default `cross-encoder` reranker runs locally; the `jev` reranker needs `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/turlockmike/deep-recall/blob/48748d62ab623f37343a5a2b437f21f1c61e930a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give Claude (or any MCP client) context from your own notes, ranked by whether a passage actually answers the question rather than just matching it.
- Pay for Jev only at the rerank step and cap spend per query and per day.
- Mismatch: for private notes keep the free local `cross-encoder` (or a local OpenAI-compatible server); the hosted Jev reranker sends note text to TypeSafe.

## How it works

First-stage hybrid search (embeddings, BM25 and a rare-term leg) picks candidate files; the reranker scores every ~600-word window with one yes/no question — does this `content` explicitly state the fact that answers the question — and a file takes its best window. Below the backend's threshold Deep Recall widens once to the top 150. With `[recall] question_kinds = true`, one Jev choice request first classifies the question (single fact, latest value, aggregate, temporal, recommendation); aggregate and temporal questions always widen. Reranker errors fail open to first-stage order ([`rerankers/jev.py`](https://github.com/turlockmike/deep-recall/blob/48748d62ab623f37343a5a2b437f21f1c61e930a/src/deeprecall/rerankers/jev.py)).

## Get started

Install the CLI, index a folder, and switch the reranker to Jev in the config (live TypeSafe calls on recall):

```sh
uv tool install 'git+https://github.com/turlockmike/deep-recall[mcp]'
deeprecall init --root ~/notes
deeprecall index
# config: [reranker] backend = "jev"   (needs TYPESAFE_API_KEY)
deeprecall recall "When is the lawn service scheduled?"
```

Only the `jev` reranker contacts TypeSafe; upstream estimates about 0.3–1.5¢ per question, records every paid call in `spend.jsonl`, and enforces `[budget] max_usd_per_query` / `daily_cap_usd`.

## Examples and demos

- README: LongMemEval-S retrieval results (maintainer-reported: evidence in the top 5 files for 498 of 500 questions with the reranker; 87.2% → 97.4% for *all* evidence sessions) with the method in `bench/longmemeval/`. These measure retrieved context, not answers, and were not reproduced here.
- Claude Code plugin: `/deep-recall:setup ~/notes`, `/deep-recall:recall <question>`, and MCP tools `recall`, `search`, `reindex`.

## Limits and data handling

Markdown files only. Hosted rerankers (Jev or another API) receive note windows; use the local cross-encoder for private notes. The first index is CPU-bound. Cost estimates and caps are upstream features; actual TypeSafe pricing may change.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 48748d62ab62](https://github.com/turlockmike/deep-recall/tree/48748d62ab623f37343a5a2b437f21f1c61e930a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
