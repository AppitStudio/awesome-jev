# searxng-jev-mcp

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

MCP server that gives coding agents one search tool over your own SearXNG: it cleans the query, picks vertical engines, merges duplicates, ranks with BM25F and can rerank results with a Jev-compatible decision model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arashbehmand/searxng-jev-mcp) |
| Maintainer | [arashbehmand](https://github.com/arashbehmand). Independently curated. |
| Format | Python MCP server (uv) |
| Requirements | Python with uv, a self-hosted SearXNG, optionally a TypeSafe, OpenRouter or Ollaya key for reranking. |
| License | [MIT](https://github.com/arashbehmand/searxng-jev-mcp/blob/4cb1c2d907fbf632a363b1f1e884c7f11836e229/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/searxng_jev_mcp/decide/providers.py`](https://github.com/arashbehmand/searxng-jev-mcp/blob/4cb1c2d907fbf632a363b1f1e884c7f11836e229/src/searxng_jev_mcp/decide/providers.py) at the pinned commit. |

## When to use

- Give Claude Code or another agent web search that returns about 1.5K tokens for 8 ranked results.
- Compare decision-model reranking with cheaper BM25F and cross-encoder options on a published evaluation.
- Mismatch: needs your own SearXNG; reranking does not beat cheaper options everywhere (see the evaluation).

## How it works

Provider profiles in `decide/providers.py` set the `/v1/systemone` base URL, model (for example `jev-1.13.0` on TypeSafe) and per-model thresholds. With a key, the scrubbed query and public snippets are scored for how likely each result answers the query; with no key or `mode=fast` it falls back to BM25F plus SearXNG scores. Integration evidence: [`src/searxng_jev_mcp/decide/providers.py`](https://github.com/arashbehmand/searxng-jev-mcp/blob/4cb1c2d907fbf632a363b1f1e884c7f11836e229/src/searxng_jev_mcp/decide/providers.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/arashbehmand/searxng-jev-mcp.git && cd searxng-jev-mcp
uv sync
mkdir -p ~/.config/searxng-jev-mcp
cp .env.example ~/.config/searxng-jev-mcp/env   # set SEARXNG_URL, DECISION_PROVIDER, keys
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Evaluation write-up: `docs/evaluation.md`.

## Limits and data handling

Scrubbed queries and public result snippets go to the decision provider on your key; paths, usernames and keys are removed from queries first.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 4cb1c2d907fb](https://github.com/arashbehmand/searxng-jev-mcp/tree/4cb1c2d907fbf632a363b1f1e884c7f11836e229). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
