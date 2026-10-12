# agent-doc-search

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Point coding agents at the right docs in large codebases: local BM25 and a TypeSafe Jev Choice search propose documents, then a Jev yes/no check drops ones that only share words (author reports ~9 in 10 irrelevant hints removed).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/beqaux/agent-doc-search) |
| Maintainer | [beqaux](https://github.com/beqaux). Independently curated. |
| Format | Node.js tool |
| Requirements | Node.js; TypeSafe key. |
| License | [MIT](https://github.com/beqaux/agent-doc-search/blob/d5987c3bd005e3497abc04020d4f912010a336f7/LICENSE) |
| Jev evidence | [`src/jev.mjs`](https://github.com/beqaux/agent-doc-search/blob/d5987c3bd005e3497abc04020d4f912010a336f7/src/jev.mjs) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Give agents fewer, more relevant doc hints in big repos.
- Mismatch: needs a docs corpus in the repo.

## How it works

BM25 and one Jev Choice over all documents propose candidates; each candidate gets a Jev Noul relevance check before being suggested. (Summarized from the upstream [README](https://github.com/beqaux/agent-doc-search/blob/d5987c3bd005e3497abc04020d4f912010a336f7/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install per the README and wire it into your agent.

## Limits and data handling

Requests and doc excerpts go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit d5987c3bd005](https://github.com/beqaux/agent-doc-search/tree/d5987c3bd005e3497abc04020d4f912010a336f7). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
