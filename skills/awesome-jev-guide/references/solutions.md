# Match a workflow to a starting point

Use this when choosing a resource. Verify the current [catalog](https://github.com/AppitStudio/awesome-jev/blob/main/README.md) and the selected artifact's instructions before recommending installation. A linked recipe is not automatically a complete application.

## Existing repository resources

The four teaching examples use Python 3.10+ and the standard library. Their question design and application policy can be adapted to another language; do not force a Python migration.

| User's need | Starting point | What it provides and what remains |
| --- | --- | --- |
| Learn the interface or route a single request | [Support-routing example](https://github.com/AppitStudio/awesome-jev/blob/main/examples/support-routing/README.md) | Choice + urgency Noul with synthetic fixtures; adapt department definitions and policy. |
| Route a batch and inspect uncertain cases | [Support Router](https://github.com/AppitStudio/awesome-jev/blob/main/projects/support-router/README.md) | Configurable routing, review queue, replay, bounded live CLI; ticket-system integration remains separate. |
| Rate content on several dimensions | [Quality rubric](https://github.com/AppitStudio/awesome-jev/blob/main/examples/quality-rubric/README.md) | Independent Score judgments and code-side weights; define domain-specific rubric levels and evaluate them. |
| Pick an exact value from source text | [Span selection](https://github.com/AppitStudio/awesome-jev/blob/main/examples/span-selection/README.md) | Selects a parser-provided candidate and returns its original span; extend candidate generation for new fields. |
| Judge retrieved passages before answering | [RAG triage](https://github.com/AppitStudio/awesome-jev/blob/main/examples/rag-triage/README.md) | Relevance, evidence, and contradiction judgments; retrieval and answer generation are separate components. |
| Evaluate support-routing questions and policy | [Evaluation runner](https://github.com/AppitStudio/awesome-jev/blob/main/evaluations/README.md) | Development/holdout, coverage/errors, and replay for the Support Router; other tasks need their own labels, request adapter, and metrics. |

## Community applications and integrations

Browse the current [community directory](https://github.com/AppitStudio/awesome-jev/blob/main/community/README.md) for categorized project pages. Each page provides fit, setup, examples, and review evidence; verify its upstream source before giving version-sensitive instructions.

| User's need | Project guide | What to check before setup |
| --- | --- | --- |
| Find praise in customer emails | [Testimonial miner](https://github.com/AppitStudio/awesome-jev/blob/main/community/projects/testimonial-miner.md) | Python/Gmail workflow; a Gmail dry run still reads the mailbox, and publishing selected text needs separate permission. |
| Add quality feedback to an AI coding workflow | [Jev Review](https://github.com/AppitStudio/awesome-jev/blob/main/community/projects/jev-review.md) | Experimental MCP server; uses `JEV_API_KEY`; scores need interpretation and are not proof of correctness. |
| Integrate typed judgments in a .NET application | [TypeSafeAI.Net](https://github.com/AppitStudio/awesome-jev/blob/main/community/projects/typesafeai-net.md) | Community client; runtime support differs from sample prerequisites; key configuration is explicit in application code. |
| Rerank retrieved passages or route LlamaIndex queries | [llama-index-jev](https://github.com/AppitStudio/awesome-jev/blob/main/community/projects/llama-index-jev.md) | Separate reranker and selector packages; upstream OpenRouter examples make live calls even with mocked embeddings or answer generation. |

Check the actual revision, runtime, key variable, license, data handling, and fallback behavior. Inclusion and mocked tests do not establish live behavior or quality on the user's data; use each page's evidence scope.

## When a custom starter fits better

Use official SDKs in the user's stack, and borrow the nearest example's decision structure. For Python, read the [Python SDK](https://docs.typesafe.ai/sdk/python); for JavaScript/TypeScript, read the [JavaScript SDK](https://docs.typesafe.ai/sdk/javascript). For another stack, inspect a suitable community client or the [HTTP API](https://docs.typesafe.ai/api). Do not promise an official SDK where there is none.

Useful directions beyond the bundled examples:

| Need | Current primary resource | Likely missing application work |
| --- | --- | --- |
| Sort documents through a deep taxonomy | [Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) | Taxonomy loading, candidate selection, traversal policy, and review. |
| Check a claim against a cited source | [Citation checking](https://docs.typesafe.ai/cookbooks/citation_check) | Fetch/parse source evidence and present uncertain cases; Jev does not browse for missing evidence. |
| Rank a shortlist for a search query | [Reranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) | Existing retrieval, candidate limits, scoring/comparison policy, and task-specific evaluation. |
| Pick a handler and known arguments | [Function calling](https://docs.typesafe.ai/cookbooks/function_calling) | Allowlisted handlers, argument validation, permissions, and execution in code. |
| Combine several judgments efficiently | [Independent fan-out](https://docs.typesafe.ai/patterns/fan-out) and [composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) | Batch genuinely independent questions; combine weights and policy in code. |
| Explore an unfamiliar domain | [Use-case map](https://docs.typesafe.ai/concepts/use-case-map) and [documentation index](https://docs.typesafe.ai/llms.txt) | Identify one narrow decision, then choose the relevant cookbook. |

These are provider guides, not additional starter projects maintained by this repository. Describe any new kit as work to build. Prefer reusing a small verified piece over adding a large framework that the workflow does not need.

## Decision rules to bring into the recommendation

- **Choice** selects one known option. Include no-match when nothing may fit; use independent Nouls for labels that can coexist.
- **Noul** estimates whether a defined condition holds. It has no separate confidence field; values near 0.5 express uncertainty, not medium severity.
- **Score** locates content on concrete ordered rubric levels. It is a probability-weighted zero-based position, not inherently a percentage. Normalize and combine in code.
- Confidence summarizes a distribution; it does not prove correctness or authorize an action. Choose review behavior according to the consequence, then evaluate it.
- Source selection requires candidates that include the intended value. More questions cannot recover evidence absent from the state.

For every recommendation, link only what helps the next decision: the selected artifact, relevant TypeSafe primitive/cookbook, and setup or evaluation guidance. Avoid handing a beginner the whole documentation catalog.
