# tf-jev

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Experimental natural-language compiler for native Text-Fabric search queries, using Jev for bounded structured decisions instead of free-form query generation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexsosn/tf-jev) |
| Maintainer | [alexsosn](https://github.com/alexsosn). Independently curated. |
| Format | Python library (research prototype) |
| Requirements | Python; Text-Fabric corpus; optional Jev access via TypeSafe. |
| License | [MIT](https://github.com/alexsosn/tf-jev/blob/488351d010a98db30c01497a8ea5c76aa8cb799e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Explore typed, corpus-restricted NL-to-query compilation for Text-Fabric corpora.
- Mismatch: early research prototype; end-to-end natural-language parsing is not yet implemented (per upstream README).

## How it works

Corpus schema extraction and candidate retrieval narrow the options, Jev makes bounded structured decisions into a typed query IR, and a deterministic compiler emits Text-Fabric search syntax. (Summarized from the upstream [README](https://github.com/alexsosn/tf-jev/blob/488351d010a98db30c01497a8ea5c76aa8cb799e/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Install from a checkout with `python -m pip install -e '.[dev,jev]'`.

## Limits and data handling

With the Jev adapter enabled, request text and candidate options are sent to the hosted Jev API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit 488351d010a9](https://github.com/alexsosn/tf-jev/tree/488351d010a98db30c01497a8ea5c76aa8cb799e). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
