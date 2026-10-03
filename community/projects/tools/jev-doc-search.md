# jev-doc-search

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Find answering pages in long PDFs with TypeSafe Jev Choice over a PageIndex tree (no vector DB).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VectifyAI/jev-doc-search) |
| Maintainer | [VectifyAI](https://github.com/VectifyAI). Independently curated. |
| Format | Python · long-document search (Apache-2.0) |
| Requirements | See upstream README; TypeSafe or local decision backends as documented. |
| License | [`Apache-2.0`](https://github.com/VectifyAI/jev-doc-search/blob/f255651838fcd831c659899bb80e0289033e45f5/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement.  Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Find answering pages in long PDFs with TypeSafe Jev Choice over a PageIndex tree (no vector DB). Jev (or a disclosed local/open System One substitute) supplies typed judgments where configured; ordinary application code owns orchestration, I/O, and side effects. See upstream for schemas and failure handling.

## Get started

```sh
git clone https://github.com/VectifyAI/jev-doc-search.git
cd jev-doc-search
git checkout f255651838fcd831c659899bb80e0289033e45f5
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.
- Jev evidence: README + `page_search.py` use `typesafe_sdk.Choice` / `TypeSafeClient` for page selection. ([upstream evidence](https://github.com/VectifyAI/jev-doc-search/blob/f255651838fcd831c659899bb80e0289033e45f5/page_search.py)).

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit f255651838fc](https://github.com/VectifyAI/jev-doc-search/tree/f255651838fcd831c659899bb80e0289033e45f5). AI-assisted README and license inspection; install/live paths not executed.
