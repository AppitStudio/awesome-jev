# RepoFinder

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Find your way around a large open-source repo: architecture map plus "where is X implemented?" answers with line citations; optional TypeSafe Jev rerank of BM25 results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SelmanBoray/RepoFinder) |
| Maintainer | [SelmanBoray](https://github.com/SelmanBoray). Independently curated. |
| Format | Python CLI |
| Requirements | Python 3.10+, git; optional TypeSafe key; Claude API key or subscription for answers. |
| License | [MIT](https://github.com/SelmanBoray/RepoFinder/blob/ecfb9fa9cd772b13268973cf5bb39f09c26dd177/LICENSE) |
| Jev evidence | [`repofinder/decisions.py`](https://github.com/SelmanBoray/RepoFinder/blob/ecfb9fa9cd772b13268973cf5bb39f09c26dd177/repofinder/decisions.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Locate the implementation of a feature before contributing to an unfamiliar project.
- Mismatch: Jev is optional (one rerank call per search).

## How it works

`index` builds a local index, `search` ranks chunks by BM25 and, with Jev configured, one Jev call reranks them; `ask` sends top chunks to Claude for a cited answer. (Summarized from the upstream [README](https://github.com/SelmanBoray/RepoFinder/blob/ecfb9fa9cd772b13268973cf5bb39f09c26dd177/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `pip install -e .`, then `repofinder index <repo>` and `repofinder search "..."`.

## Limits and data handling

Code snippets go to TypeSafe (rerank) and Anthropic (answers) when enabled. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit ecfb9fa9cd77](https://github.com/SelmanBoray/RepoFinder/tree/ecfb9fa9cd772b13268973cf5bb39f09c26dd177). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
