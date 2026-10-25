# Google ADK TypesafeClassifier (route ADK agent workflows with Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Built-in integration in Google's Agent Development Kit for Python (v2.13.0+): `TypesafeClassifier` answers Choice, Binary and Score questions with TypeSafe's Jev, and the experimental `ClassifierNode` routes a workflow on the answer, with route labels checked against the graph when the workflow is built.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/google/adk-python) |
| Maintainer | [google](https://github.com/google). Independently curated. |
| Format | Python library feature (google-adk 2.13.0+) |
| Requirements | Python with `google-adk` 2.13.0 or later; a TypeSafe API key in `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/google/adk-python/blob/da35ca77d71f7d74c8b7d7550f6e1b591a6690e0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/christopherbaer/status/2114152309332873366)). |
| Jev evidence | [`src/google/adk/integrations/typesafe/_typesafe_classifier.py`](https://github.com/google/adk-python/blob/da35ca77d71f7d74c8b7d7550f6e1b591a6690e0/src/google/adk/integrations/typesafe/_typesafe_classifier.py) at the pinned commit. |

## When to use

- Branch an ADK workflow (for example, ticket triage) on a typed Jev answer instead of an LLM agent that returns a label.
- Gate tool calls in a `before_tool_callback` with a Jev yes/no question.
- Mismatch: `google.adk.labs.classifiers` is experimental and its interface may change between releases.

## How it works

`_typesafe_classifier.py` posts the input and questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default; `TYPESAFE_BASE_URL` can override) over httpx and retries rate-limited responses with backoff. `ClassifierNode` raises a `WorkflowDataError` on a missing or out-of-schema answer instead of guessing a route. Integration evidence: [`src/google/adk/integrations/typesafe/_typesafe_classifier.py`](https://github.com/google/adk-python/blob/da35ca77d71f7d74c8b7d7550f6e1b591a6690e0/src/google/adk/integrations/typesafe/_typesafe_classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -U "google-adk>=2.13.0"
export TYPESAFE_API_KEY=...
# from google.adk.integrations.typesafe import TypesafeClassifier
# from google.adk.labs.classifiers import Choice, ClassifierNode
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- TypesafeClassifier guide: [github.com/google/adk-python/blob/main/docs/guides/integrations/typesafe/typesafe_classifier/index.md](https://github.com/google/adk-python/blob/main/docs/guides/integrations/typesafe/typesafe_classifier/index.md)
- ClassifierNode guide: [github.com/google/adk-python/blob/main/docs/guides/labs/classifiers/classifier_node/index.md](https://github.com/google/adk-python/blob/main/docs/guides/labs/classifiers/classifier_node/index.md)
- Workflow routing sample: [github.com/google/adk-python/tree/main/contributing/samples/workflows/classifier_node](https://github.com/google/adk-python/tree/main/contributing/samples/workflows/classifier_node)
- v2.13.0 release notes: [github.com/google/adk-python/releases/tag/v2.13.0](https://github.com/google/adk-python/releases/tag/v2.13.0)

## Limits and data handling

The classifier input is sent to TypeSafe. Maintained by Google in the ADK repository; this listing covers only the Jev classifier feature. Distinct from the listed adk-go-typesafe and JEV ADK community projects.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit da35ca77d71f](https://github.com/google/adk-python/tree/da35ca77d71f7d74c8b7d7550f6e1b591a6690e0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
