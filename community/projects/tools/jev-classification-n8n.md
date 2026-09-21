# Jev Classification for n8n

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Use Jev's typed decisions inside self-hosted n8n workflows to route tickets, score reviews, or ask several independent questions about each item.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/khmuhtadin/n8n-nodes-jev-classification) |
| Maintainer | [khmuhtadin](https://github.com/khmuhtadin); submitted as the maintainer's own project through JevList in [issue #209](https://github.com/AppitStudio/awesome-jev/issues/209). |
| Format | TypeScript n8n community node with an AI Agent Tool variant. |
| Availability | Published [npm package](https://www.npmjs.com/package/n8n-nodes-jev-classification), reviewed at v0.2.0. Self-hosted only; upstream reports n8n declined Cloud verification because of overlap with built-in functionality. |
| Jev's role | Supplies Choice, Score, and Noul answers; node code applies thresholds, shapes results, and selects output branches. |
| Requirements | Self-hosted n8n with community packages enabled; package declares Node.js 20+, subject to the installed n8n version's runtime requirements; TypeSafe account and API key. |
| License and costs | [MIT](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/bf5bf031885a03c24d38d243eb47a04d91b06679/LICENSE). Hosting/n8n access and [TypeSafe inference charges](https://docs.typesafe.ai/models) are separate from the source license. |
| Disclosure | Maintainer self-submission with disclosed AI assistance; this catalog review and guide were also AI-assisted. No additional commercial relationship was stated. Inclusion is not endorsement by this directory, n8n, or TypeSafe. |

## When to use

Use this when an existing n8n automation needs semantic routing or scoring without writing its own HTTP integration. It provides per-category outputs, configurable review handling, parallel requests, and multi-item batching. Dynamic categories can come from preceding workflow items or an AI Agent.

It is a workflow building block, not a complete support application. Keep arithmetic, exact parsing, permissions, and consequential downstream actions in ordinary workflow code.

## How it works

The [node implementation](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/bf5bf031885a03c24d38d243eb47a04d91b06679/nodes/JevClassification/JevClassification.node.ts) sends selected text or JSON and typed questions to `POST https://api.typesafe.ai/v1/systemone`. It defaults to `jev-latest`, with `jev-preview` and custom model IDs available. The request shape matches the [TypeSafe API](https://docs.typesafe.ai/api) inspected during review.

| Operation | Result and routing |
| --- | --- |
| Classify, fixed categories | Choice, probabilities, confidence, and `needsReview`; one output per category, plus a default Needs Review output below the configured confidence threshold. Choosing “Send to Best Category Anyway” removes that review branch. |
| Classify, dynamic categories | Categories are evaluated per item; one Result output carries `category` and `needsReview`. Add a Switch/IF node for review or category routing. |
| Score | Weighted score, most probable level, distribution, legend, confidence, and `needsReview`; one output, with review routing left to the workflow. |
| Check | Noul probability becomes a boolean using the configured threshold; Yes and No outputs, with no separate uncertainty interval. |
| Ask Questions | Raw typed answers, model, and usage for mixed questions; one output, with interpretation left to the workflow. |

Successful items retain input fields by default and add a configurable `jev` field, with binary data and item pairing preserved. [Batch helpers](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/bf5bf031885a03c24d38d243eb47a04d91b06679/nodes/JevClassification/helpers.ts) place multiple items in shared state, scope each question's instructions to its item, and split answers back into item results. Batched Ask Questions usage describes the whole request, not each item's individual cost.

## Get started

Follow the [upstream installation and credential instructions](https://github.com/khmuhtadin/n8n-nodes-jev-classification#installation):

1. In self-hosted n8n, open **Settings → Community Nodes → Install** and enter `n8n-nodes-jev-classification`. Restart n8n if needed.
2. Create a TypeSafe key privately and add an n8n credential of type **Jev (TypeSafe) API**. Its Test action contacts TypeSafe's `GET /v1/models` endpoint.
3. Download [route-support-tickets.json](https://github.com/khmuhtadin/n8n-nodes-jev-classification/blob/bf5bf031885a03c24d38d243eb47a04d91b06679/examples/route-support-tickets.json), import it using the workflow menu's **Import from File**, and select that credential on the Jev node.
4. Inspect the synthetic tickets, categories, and illustrative `0.6` confidence threshold. Executing the manual trigger sends five synthetic tickets to TypeSafe and may incur inference charges. Inspect `jev.category`, `jev.confidence`, `jev.probabilities`, and `jev.needsReview` on the category/Needs Review outputs; results depend on the model.

The sample ends in NoOp nodes, so it demonstrates routing without issuing refunds or contacting customers. It has no `other` category: off-topic messages still receive one of the listed categories and are not guaranteed to enter Needs Review. Add a suitable fallback category and evaluate the policy before adapting it.

For the optional AI Agent Tool variant, upstream requires `N8N_COMMUNITY_PACKAGES_ALLOW_TOOL_USAGE=true`. An agent's separate model, credentials, and data handling remain part of that workflow's setup.

## Examples and demos

The [example directory](https://github.com/khmuhtadin/n8n-nodes-jev-classification/tree/bf5bf031885a03c24d38d243eb47a04d91b06679/examples) contains four importable workflows:

- `route-support-tickets.json`: fixed categories and a Needs Review branch over five sample tickets.
- `score-and-check.json`: sentiment scoring with three items per request, plus a separate defect check and Yes/No branches.
- `dynamic-categories.json`: different category lists per item, followed by explicit review routing.
- `ask-questions-batch.json`: Choice, Score, and Noul questions over ten sample messages in one request.

These workflows use synthetic input but require live inference when executed. The [unit tests](https://github.com/khmuhtadin/n8n-nodes-jev-classification/tree/bf5bf031885a03c24d38d243eb47a04d91b06679/test) instead use fabricated provider responses. Upstream's README includes screenshots; no separate hosted interactive demo was identified.

## Limits and data handling

- Selected text/JSON, instructions, and criteria go to TypeSafe. Whole-item input sends all JSON fields; binary attachments are passed through locally rather than submitted for inference. Workflow outputs enter n8n's execution data, with retention controlled by the instance.
- Fixed Classify and Score compare provider confidence to a threshold; Check instead compares the probability of yes. These are different quantities. The default `0.5` is an application setting, not a validated policy for your data.
- HTTP 429 and 5xx responses receive configurable retries; transport exceptions are not retried. The default is three retries with a 60-second timeout per attempt, not a total execution deadline.
- With **On Error → Continue**, request failures become `{ error: ... }` items on the **first output**, which can otherwise mean the first category or Yes. They retain pairing but lose the original JSON/binary content. Handle errors explicitly before downstream actions; they do not enter Needs Review automatically.
- Successful HTTP bodies are cast to expected types without complete runtime validation. Missing/malformed answers can throw or produce incomplete results; Check can turn a missing probability into a No decision. Do not assume malformed responses safely abstain.
- Text/JSON decisions do not provide text generation. Multi-item requests share context; keep unrelated fields out and evaluate batch size and thresholds on representative data. This review establishes neither calibration, accuracy, latency, nor cost savings.

## Review and maintenance

Reviewed September 21, 2026 at [commit bf5bf03](https://github.com/khmuhtadin/n8n-nodes-jev-classification/commit/bf5bf031885a03c24d38d243eb47a04d91b06679), package v0.2.0. The public npm registry's v0.2.0 metadata identifies that same commit. Inspected the README, MIT license, package metadata, credential handling, request/retry code, output shaping, tests, and all four workflow JSON files.

Independently ran `npm ci --ignore-scripts --no-audit --no-fund`, `npm test` (**43 tests passed**), `npm run lint`, `npm run typecheck`, and `npm run build` successfully under Node.js 24.19.0 in a separate checkout with an isolated home and no inherited provider credentials. Installation emitted dependency deprecation and npm-version warnings; tests emitted missing dependency sourcemap warnings. The tests use a fake n8n context and synthetic HTTP responses, not an installed n8n instance or live Jev. The catalog's `npm run check` also passed.

The [submission](https://github.com/AppitStudio/awesome-jev/issues/209) reports 36 passing tests at v0.1.1 (`e7f03b6`). This guide reviews the newer version and corrects the submission's older “Cloud verification pending” wording using upstream's current self-hosted-only disclosure.

No n8n UI installation, credential test, live workflow, smoke script, or model-quality evaluation was performed during this review.

Related: [Support Router](../../../projects/support-router/README.md) for a standalone offline routing example, or [Laravel AI](laravel-ai.md) for application-level PHP integration.
