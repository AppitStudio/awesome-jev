# SlopSearX

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Stateless, AI-agent-first SearXNG-compatible meta search engine (50 engines, MCP server) with optional TypeSafe Jev specialist-engine routing and bounded result reranking when `TYPESAFE_API_KEY` is set; deterministic routing/RRF order otherwise.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/magnus919/SlopSearX) |
| Maintainer | [magnus919](https://github.com/magnus919). Independently curated. |
| Format | Self-hosted search service with Docker images, Kubernetes manifests and an MCP server |
| Requirements | Python or Docker; Valkey for rate limiting/caching. `TYPESAFE_API_KEY` opts into Jev routing and reranking. |
| License | [MIT](https://github.com/magnus919/SlopSearX/blob/112c0e15d84c61da01a045f9ca2c630842328633/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give agents a SearXNG drop-in that picks medical, legal, security or package-registry engines only when they add evidence for the query.
- Rerank a capped set of result cards across source tiers with calibrated scores.
- Mismatch: explicit engine/category scopes bypass Jev, and sensitive-engine scopes are never sent.

## How it works

SlopSearX keeps its general-engine base and asks Jev which eligible specialist engines can add distinctive evidence; every specialist at or above 0.65 is added (no arbitrary cap). After retrieval Jev orders a bounded shortlist with Score questions. Without a key, or on invalid/unavailable advice, the deterministic presence/RRF path is used unchanged. Payload bounds, timeouts, caching and privacy are documented in [`docs/JEV_ROUTING.md`](https://github.com/magnus919/SlopSearX/blob/112c0e15d84c61da01a045f9ca2c630842328633/docs/JEV_ROUTING.md) and `docs/JEV_RERANKING.md`.

## Get started

Run from a checkout (or the published Docker image per README) and set the key to opt in (live TypeSafe calls per query):

```sh
git clone https://github.com/magnus919/SlopSearX.git
cd SlopSearX
pip install -e ".[dev]"
export TYPESAFE_API_KEY=...      # opt-in Jev routing + reranking
slopsearx-mcp                    # MCP over stdio
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- Experiment write-ups `docs/experiments/EXP-004…007` on Jev reranking, fusion and robustness (maintainer-reported).
- MCP server modes: stdio, HTTP with token, remote gateway, OAuth.

## Limits and data handling

Providing the key sends the query, bounded titles, sanitized URLs and snippets to TypeSafe. Results still come from third-party search engines. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 112c0e15d84c](https://github.com/magnus919/SlopSearX/tree/112c0e15d84c61da01a045f9ca2c630842328633). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
