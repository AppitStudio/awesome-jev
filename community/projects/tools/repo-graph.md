# Repo Graph

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local repository architecture diagrams and semantic search packaged for Pi, Codex and Claude Code, with an optional, off-by-default TypeSafe Jev reranker that judges a shortlist in one bounded batched request.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fakoli/repo-graph) |
| Maintainer | [fakoli](https://github.com/fakoli). Independently curated. |
| Format | CLI + local browser viewer + agent plugins (v0.6.0 tag at review) |
| Requirements | Python with uv; the `semantic` extra for search; `TYPESAFE_API_KEY` only for `--rerank jev` / `--allow-jev` / `map --jev`. |
| License | [MIT](https://github.com/fakoli/repo-graph/blob/b21a7c19fc3f068d3b0227ba1fa6acd5eda17280/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give a coding agent a structural map and semantic search over a repo without sending it to a model.
- Opt in to Jev reranking for hard queries, with receipts recording model, calls and usage.
- Mismatch: semantic search is experimental; Jev cannot recover files missing from the shortlist.

## How it works

The scanner builds `graph.json`, diagrams and a SQLite vector index locally. With `--rerank jev` the query and up to 32 paths with 900 bytes of evidence each (48 KiB cap) go to Jev pinned at `jev-1.13.0`; failures keep local order and show `fallback`. Research and measurements: [`docs/jev-research.md`](https://github.com/fakoli/repo-graph/blob/b21a7c19fc3f068d3b0227ba1fa6acd5eda17280/docs/jev-research.md).

## Get started

Install, map and search; add Jev reranking explicitly:

```sh
uv tool install 'repo-graph-agent[semantic] @ git+https://github.com/fakoli/repo-graph@v0.6.0'
repo-graph map /path/to/repository
repo-graph index OUTPUT --semantic
export TYPESAFE_API_KEY=...
repo-graph search OUTPUT 'where are access permissions checked?' --rerank jev
```

Only the explicit Jev options contact TypeSafe (billed to your key).

## Examples and demos

- [Jev research and measured comparison](https://github.com/fakoli/repo-graph/blob/b21a7c19fc3f068d3b0227ba1fa6acd5eda17280/docs/jev-research.md): maintainer reports hit@5 10/16 → 14/16 on new queries, no gain on the old Kubernetes set.
- `evaluations/` query sets, probes and result JSON.

## Limits and data handling

Jev options export bounded source evidence to TypeSafe; nothing is sent by default. Measurements are upstream. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit b21a7c19fc3f](https://github.com/fakoli/repo-graph/tree/b21a7c19fc3f068d3b0227ba1fa6acd5eda17280). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
