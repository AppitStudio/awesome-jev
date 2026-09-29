# Jev Deep Research

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Deep-research loop where GPT chooses what to investigate and TypeSafe Jev finds evidence in parallel across document regions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sunyasheng/JevDeepResearch) |
| Maintainer | [sunyasheng](https://github.com/sunyasheng). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Research agent harness (Pi-Serini BM25 + Jev batches). |
| Requirements | GPT + TypeSafe Jev credentials for live runs; offline demo path documented. |
| License | [Apache-2.0](https://github.com/sunyasheng/JevDeepResearch/blob/4fe0ff2e27516a58c35c9cdd4c28e21f1e6e3515/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when studying parallel System One evidence finding inside research agents. Prefer simpler search tools for single-query lookup.

## How it works

Search caches ranked docs; `jev_find` fans Choice+Noul questions over regions; code merges verbatim excerpts for GPT’s next step. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/sunyasheng/JevDeepResearch.git
cd JevDeepResearch
git checkout 4fe0ff2e27516a58c35c9cdd4c28e21f1e6e3515
# follow upstream README quick start / offline demo
```

Pin revision `4fe0ff2e27516a58c35c9cdd4c28e21f1e6e3515` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

BrowseComp-Plus tables are author-reported. Live GPT/Jev research not run on the review host. Document text is sent to providers when live.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 4fe0ff2](https://github.com/sunyasheng/JevDeepResearch/tree/4fe0ff2e27516a58c35c9cdd4c28e21f1e6e3515). AI-assisted README and LICENSE inspection; install/live paths not executed.
