# IntelligentDocumentProcessing (Jev + Haiku)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hybrid invoice/document processing: TypeSafe Jev makes typed decisions (document type, supplier, completeness), Claude Haiku extracts, n8n orchestrates, Supabase stores; benchmarked against 7 models on 250 documents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DanielHuette/IntelligentDocumentProcessing) |
| Maintainer | [DanielHuette](https://github.com/DanielHuette). Independently curated. |
| Format | Python package + n8n workflow |
| Requirements | Python; n8n; Supabase; TypeSafe and Anthropic keys. |
| License | [MIT](https://github.com/DanielHuette/IntelligentDocumentProcessing/blob/b0dd927c295ea6cbde88a83b64bdfdffcf5f3cc1/LICENSE) |
| Jev evidence | [`src/idp`](https://github.com/DanielHuette/IntelligentDocumentProcessing/tree/b0dd927c295ea6cbde88a83b64bdfdffcf5f3cc1/src/idp) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Pattern for splitting document decisions (Jev) from extraction (LLM) with a review path.
- Mismatch: synthetic/benchmark corpus; adapt before production.

## How it works

Jev answers typed questions per document; Haiku extracts fields; the n8n workflow routes uncertain items to a person. (Summarized from the upstream [README](https://github.com/DanielHuette/IntelligentDocumentProcessing/blob/b0dd927c295ea6cbde88a83b64bdfdffcf5f3cc1/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): follow the README to run the benchmark CLI or import the n8n workflow.

## Limits and data handling

Document content goes to TypeSafe and Anthropic. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit b0dd927c295e](https://github.com/DanielHuette/IntelligentDocumentProcessing/tree/b0dd927c295ea6cbde88a83b64bdfdffcf5f3cc1). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
