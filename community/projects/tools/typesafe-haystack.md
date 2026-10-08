# typesafe-haystack (Haystack integration)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Official Haystack integration (`typesafe-haystack`) adding two pipeline components that call TypeSafe System One models such as Jev: `TypeSafeDocumentClassifier` answers typed `choice` / `score` / `noul` questions about each document and stores the probabilities in its metadata, and a text router sends inputs down pipeline branches by Jev's answer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/deepset-ai/haystack-core-integrations/tree/main/integrations/typesafe) |
| Maintainer | [deepset-ai](https://github.com/deepset-ai) (Haystack core integrations). Independently curated. |
| Format | Python package `typesafe-haystack` (components under `haystack_integrations.components.classifiers.typesafe` and `...routers.typesafe`) |
| Requirements | Python with Haystack; `TYPESAFE_API_KEY` (or `api_key` as a Haystack `Secret`); tests can target a local Ollaya server through `TYPESAFE_BASE_URL`. |
| License | [Apache-2.0](https://github.com/deepset-ai/haystack-core-integrations/blob/16dd28e995e4666bea896a38a36489417310f85b/integrations/typesafe/LICENSE.txt). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Tag documents with calibrated labels (refund request? topic? urgency score?) before a `MetadataRouter` or retriever.
- Branch a Haystack pipeline on a typed decision instead of parsing LLM prose.
- Mismatch: each document is its own request; very large corpora mean many API calls.

## How it works

[`document_classifier.py`](https://github.com/deepset-ai/haystack-core-integrations/blob/16dd28e995e4666bea896a38a36489417310f85b/integrations/typesafe/src/haystack_integrations/components/classifiers/typesafe/document_classifier.py) sends each document's content (or a metadata field) with your question dict and writes answers under `meta["typesafe"]`; failures go to `failed_documents`. [`text_router.py`](https://github.com/deepset-ai/haystack-core-integrations/blob/16dd28e995e4666bea896a38a36489417310f85b/integrations/typesafe/src/haystack_integrations/components/routers/typesafe/text_router.py) routes text to outputs by the answer. `max_workers` bounds concurrency in `run` and `run_async`.

## Get started

Install the package and set your key (integration [README](https://github.com/deepset-ai/haystack-core-integrations/blob/16dd28e995e4666bea896a38a36489417310f85b/integrations/typesafe/README.md)):

```sh
pip install typesafe-haystack
export TYPESAFE_API_KEY=...
```

Each classified document or routed input is a TypeSafe request billed to your key.

## Examples and demos

- Integration page: [haystack.deepset.ai/integrations/typesafe](https://haystack.deepset.ai/integrations/typesafe).
- PyPI: [`typesafe-haystack`](https://pypi.org/project/typesafe-haystack/) (0.1.0).
- Changelog: [`CHANGELOG.md`](https://github.com/deepset-ai/haystack-core-integrations/blob/16dd28e995e4666bea896a38a36489417310f85b/integrations/typesafe/CHANGELOG.md).

## Limits and data handling

Document text (or the chosen metadata field) is sent to TypeSafe or the configured compatible base URL. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 16dd28e995e4](https://github.com/deepset-ai/haystack-core-integrations/tree/16dd28e995e4666bea896a38a36489417310f85b). Inspected the integration README, component source, tests and LICENSE in the monorepo at the pinned commit, plus the Haystack docs page for the classifier; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
