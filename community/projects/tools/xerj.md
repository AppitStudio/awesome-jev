# XERJ

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Elasticsearch-compatible local search engine for AI agents (single Rust binary, MCP) with an opt-in `rerank` stage that sends top hits to TypeSafe Jev and reorders them by its relevance probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xerj-org/xerj) |
| Product homepage | [xerj.org](https://xerj.org) |
| Maintainer | [xerj-org](https://github.com/xerj-org). Independently curated. |
| Format | Self-hosted search engine binary with MCP server and agent skill; Jev reranking is an optional search stage |
| Requirements | The XERJ binary (install script or release download). Reranking needs a TypeSafe key in `xerj.toml` (`[rerank] api_key`) or `TYPESAFE_API_KEY`; the default endpoint is `https://api.typesafe.ai/v1/systemone`. |
| License | [Apache-2.0](https://github.com/xerj-org/xerj/blob/642dfa969114c6adb3353d7ece123b6b6ea97cef/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give a coding agent a local index of its own repo and reference repos, and rerank ambiguous queries by Jev's per-document relevance probability.
- Keep the fast path local (BM25/vector/hybrid) and pay for Jev only on searches that ask for `rerank`.
- Mismatch: if documents must never leave the machine, leave reranking unconfigured or set `[rerank] enabled = false`; the local `_decide` endpoint only works when you have labelled examples.

## How it works

Search runs locally as usual; a request carrying a `rerank` block POSTs the question and the text of up to `window` hits (default 30, max 300) to Jev, which returns a probability per document that it answers the question. Hits are reordered by that probability. Upstream warns the probabilities are useful for ordering but not calibrated for thresholds, and that reranking is the only search-time feature that sends document text off the node ([docs/RERANK.md](https://github.com/xerj-org/xerj/blob/642dfa969114c6adb3353d7ece123b6b6ea97cef/docs/RERANK.md)). Separately, `POST /v1/systemone` and `/_decide` accept the same request format but are answered locally by nearest labelled examples under the model name `xerj-history-vote-1`; that endpoint is not Jev.

## Get started

Install and index a project per the README, then configure a key and request a reranked search (live Jev call for reranked searches only):

```sh
curl -fsSL https://xerj.org/get | sh
xerj --insecure --data-dir ./data &   # dev-only: disables TLS and auth on 127.0.0.1
xerj autoindex ~/my-project
# xerj.toml: [rerank] enabled = true, api_key = "..." (or TYPESAFE_API_KEY)
# POST /<index>/_search with {"query": ..., "rerank": {}}
```

Only searches that include `rerank` contact TypeSafe and incur usage charges; plain search and `_decide` run locally.

## Examples and demos

- [docs/RERANK.md](https://github.com/xerj-org/xerj/blob/642dfa969114c6adb3353d7ece123b6b6ea97cef/docs/RERANK.md): setup, data-egress list, failure policy, and maintainer-measured BEIR results (FiQA nDCG@10 0.24 → 0.36 with `jev-1.13.0`; SciFact pilot 0.775 → 0.830). Numbers are upstream-reported and were not reproduced here.
- README section *Score results with Jev* and the `benchmarks/` directory for reproduction scripts.

## Limits and data handling

Reranking sends the question and hit text to TypeSafe and is billed per search. Jev probabilities are not calibrated against BEIR relevance (upstream ECE 0.10–0.31), so rank by them rather than thresholding. The `--insecure` quick-start mode disables TLS and API-key auth and is meant for a single-user dev machine. Upstream also asks users for optional field-report PRs; that is unrelated to Jev.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 642dfa969114](https://github.com/xerj-org/xerj/tree/642dfa969114c6adb3353d7ece123b6b6ea97cef). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
