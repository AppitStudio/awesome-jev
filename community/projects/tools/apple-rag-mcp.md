# Apple RAG MCP

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

MCP server for Apple developer documentation and WWDC transcripts: hybrid keyword + semantic retrieval, then TypeSafe Jev ranks the merged candidates against the question's API, platform and version requirements, with a Qwen3 reranker fallback. Offered as a hosted service (free tier and a paid Pro plan) and as self-hostable MIT source.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BingoWon/apple-rag-mcp) |
| Maintainer | [BingoWon](https://github.com/BingoWon). Independently curated. |
| Format | Hosted Streamable HTTP MCP endpoint + Cloudflare Worker source |
| Requirements | An MCP client supporting the documented protocol; hosted use needs no key to start (an MCP token raises limits). Self-hosting needs your own database, corpus pipeline, `TYPESAFE_API_KEY` and fallback reranker credentials. |
| License | [MIT](https://github.com/BingoWon/apple-rag-mcp/blob/32a48b839cfad311316b753b12fec5fbcdaddb07/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Hosted service has a free tier and a paid Pro plan (commercial). Install and live inference not run on the review host. |

## When to use

- Give a coding agent current Apple platform docs with relevance-ranked results instead of raw search hits.
- Mismatch: if queries must not go to a third-party hosted service, self-host (and operate the corpus) instead.

## How it works

[`worker/mcp-services/reranker.ts`](https://github.com/BingoWon/apple-rag-mcp/blob/32a48b839cfad311316b753b12fec5fbcdaddb07/worker/mcp-services/reranker.ts) calls `https://api.typesafe.ai/v1/systemone` with `jev-latest` to score candidates; on failure it logs the error and falls back to Qwen3-Reranker-8B, and if both fail the original candidate order is returned. The maintainer's offline replay scripts and an evaluation report live in [`ops/jev/`](https://github.com/BingoWon/apple-rag-mcp/blob/32a48b839cfad311316b753b12fec5fbcdaddb07/ops/jev/report-2026-10-08.md) (their results; not reproduced here).

## Get started

From the upstream README (not run on the review host):

```sh
# Hosted: add this MCP server to your client
#   type: http   url: https://mcp.apple-rag.com
# Optional MCP token from https://apple-rag.com raises limits
```

## Limits and data handling

Commercial disclosure: the hosted service has a free tier and a paid Pro plan (the README lists Pro at $1/week for higher limits; see [pricing](https://apple-rag.com/#pricing), checked 2026-10-09). Hosted queries are processed by the operator, who runs embeddings, Jev ranking and the fallback reranker on its own credentials. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 32a48b839cfa](https://github.com/BingoWon/apple-rag-mcp/tree/32a48b839cfad311316b753b12fec5fbcdaddb07). Inspected the upstream README, LICENSE status, and the Jev-related source files linked above at the pinned commit; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
