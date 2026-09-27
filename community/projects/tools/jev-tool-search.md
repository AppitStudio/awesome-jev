# jev-tool-search

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Benchmark and experimental engine comparing BM25, embeddings, rerankers, and TypeSafe Jev for selecting among 525 real MCP tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kachar/jev-tool-search) |
| Maintainer | [kachar](https://github.com/kachar). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Benchmark harness + experimental search engine. |
| Requirements | Python; TypeSafe/provider keys for live arms per upstream docs. |
| License | [MIT](https://github.com/kachar/jev-tool-search/blob/a23f61bb02ddd9381a22166db2986c6ffe0b3675/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when evaluating tool-selection strategies for MCP/agent catalogs. Prefer production routers once you have a chosen policy.

## How it works

Runs retrieval/ranking arms over a fixed MCP-tool corpus and records comparisons; optional Jev-backed search path documented upstream. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/kachar/jev-tool-search.git
cd jev-tool-search
git checkout a23f61bb02ddd9381a22166db2986c6ffe0b3675
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `a23f61bb02ddd9381a22166db2986c6ffe0b3675` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream).  Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit a23f61bb02dd](https://github.com/kachar/jev-tool-search/tree/a23f61bb02ddd9381a22166db2986c6ffe0b3675). AI-assisted README and LICENSE inspection; install/live paths not executed.
