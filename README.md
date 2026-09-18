# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Curated resources and runnable examples for building typed decisions with Jev.

[Jev](https://docs.typesafe.ai/introduction) is TypeSafe AI's System One model: give it state and typed questions, then use the returned choices, scores, and probabilities in your code. This independent community list focuses on understanding that interface and building small, inspectable workflows.

## Contents

- [Start here](#start-here)
- [Official SDKs and tools](#official-sdks-and-tools)
- [Community projects](#community-projects)
- [Starter projects](#starter-projects)
- [Reference project](#reference-project)
- [Patterns and cookbooks](#patterns-and-cookbooks)
  - [Routing and classification](#routing-and-classification)
  - [Retrieval and verification](#retrieval-and-verification)
  - [Extraction and structured data](#extraction-and-structured-data)
- [Model behavior and evaluation](#model-behavior-and-evaluation)
- [Contributing](#contributing)

## Start here

- [Introduction](https://docs.typesafe.ai/introduction) - Understand Jev's state-and-questions interface and its three decision primitives.
- [Official quick start](https://docs.typesafe.ai/introduction/quickstart) - Make a first request using Python or HTTP.
- [Run an example locally](docs/getting-started.md) - Try a complete workflow with synthetic mock responses, without an account, an API key, or package installation.
- [Choose a decision pattern](docs/decision-patterns.md) - Match a task to Choice, Score, or Noul and define what happens when the result is uncertain.
- [HTTP API reference](https://docs.typesafe.ai/api) - Check the wire format, authentication, answer fields, and error responses.

## Official SDKs and tools

These resources are maintained by TypeSafe.

- [Agent skill](https://docs.typesafe.ai/agent-skill) - Give a coding agent the official API context and guidance for designing narrow decision questions.
- [JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - JavaScript and TypeScript client that infers answer types from the supplied questions.
- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - Synchronous and asynchronous clients with typed answers and configurable retries.
- [System One Adapter](https://github.com/typesafe-ai/system-one-adapter-python) - Run a similar typed-question interface against other LLM providers for comparisons; those responses do not come from Jev.

## Community projects

These projects were reviewed from source and their upstream tests with mocked responses passed on 2026-09-18. Their live behavior and model quality were not evaluated here. Check each project's prerequisites, license, and fallback behavior before adopting it.

- [Jev Review](https://github.com/NiazMorshed2007/jev-review) - MCP server for experimental software-quality rubric scores and comparisons; requires `JEV_API_KEY` and sends supplied code context to TypeSafe.
- [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) - Python integrations for LlamaIndex passage reranking and query-engine selection, with configurable error and selection behavior.
- [TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net) - Community .NET client with typed questions, dependency injection, and Microsoft.Extensions.AI adapters.

## Starter projects

Original examples maintained in this repository. Each includes readable questions, application policy, synthetic responses, tests, and an optional live mode. **Mock results demonstrate code behavior, not Jev accuracy.**

- [Quality rubric](examples/quality-rubric/README.md) - Evaluate independent dimensions and combine scores with visible weights in code.
- [RAG triage](examples/rag-triage/README.md) - Check a retrieved passage for relevance, evidence, and contradictory information before selecting context.
- [Span selection](examples/span-selection/README.md) - Extract candidate values in code, select one with Jev, and return the exact source value.
- [Support routing](examples/support-routing/README.md) - Select a department and assess explicit urgency, with review paths for uncertain answers.

With Python 3.10 or newer, from a checkout:

```bash
python3 examples/run.py support-routing --mock
```

See the [example guide](examples/README.md) for all commands and live-mode setup. The examples print decisions; they do not execute downstream actions.

## Reference project

Start with the runnable tool, then evaluate its policy on your own cases.

- [Support Router](projects/support-router/README.md) - Route a batch of tickets with configurable departments and review thresholds, inspect each typed answer, and export a human-review queue.
- [Evaluation runner](evaluations/README.md) - Assess routing and abstention on your own labeled development and holdout cases, with bounded live calls and offline replay.

Both tools are maintained here. Start with the synthetic demo; see [validation scope](docs/validation.md) for what has been checked.

## Patterns and cookbooks

Selected official guides, organized by what you want to build. Cookbook results and benchmarks are the authors' reports, not independent measurements by this repository.

### Routing and classification

- [Confidence-gated routing](https://docs.typesafe.ai/patterns/confidence-routing) - Add review or fallback paths when a selected answer is uncertain.
- [Hierarchical classification](https://docs.typesafe.ai/cookbooks/hierarchical_classification) - Navigate a taxonomy using candidate branches instead of one enormous label set.
- [Intent routing](https://docs.typesafe.ai/patterns/intent-routing) - Select a handler for a request while keeping routing rules in application code.
- [Skill suggestion](https://docs.typesafe.ai/cookbooks/skill_suggestion) - Shortlist agent skills and separately decide whether any of them is appropriate.
- [Speculative fan-out](https://docs.typesafe.ai/patterns/fan-out) - Ask independent questions together and use only the answers relevant to the selected branch.

### Retrieval and verification

- [Classifying RAG passages](https://docs.typesafe.ai/cookbooks/classifying_rag_passages) - Evaluate passage properties before selecting context for an answering model.
- [Double-checking citations](https://docs.typesafe.ai/cookbooks/citation_check) - Judge whether a supplied source supports a claim and flag uncertain decisions for review.
- [Line-by-line search](https://docs.typesafe.ai/cookbooks/semantic_find) - Select relevant source lines and separately check whether the document contains an answer.
- [Re-ranking](https://docs.typesafe.ai/cookbooks/rerank_typesafe) - Apply semantic judgments to a shortlist produced by an existing retriever.

### Extraction and structured data

- [Composite scoring](https://docs.typesafe.ai/patterns/composite-scoring) - Combine separate rubric judgments with application-defined weights.
- [Date extraction](https://docs.typesafe.ai/cookbooks/date_extraction_cookbook) - Select date components, then assemble and validate dates in code.
- [Knowledge graph entity alignment](https://docs.typesafe.ai/cookbooks/entity_alignment) - Map candidate record pairs to merge, separate, or curator-review outcomes.
- [Pre-parsed value extraction](https://docs.typesafe.ai/cookbooks/pre_parsed_value_extraction_cookbook) - Let parsers find possible values and use Jev to select the one matching a semantic request.
- [Structure recovery](https://docs.typesafe.ai/cookbooks/autoformat) - Classify text blocks so code can reconstruct document formatting.

## Model behavior and evaluation

- [Choice self-consistency](https://docs.typesafe.ai/cookbooks/consistency_choice_cookbook) - Explore uncertain outcomes and the difference between agreement and correctness.
- [Confidence](https://docs.typesafe.ai/confidence) - Understand how a distribution summary differs from the selected answer and its probability.
- [Current models](https://docs.typesafe.ai/models) - Find model versions, moving aliases, supported inputs, pricing, and current limits.
- [Jev 1.13 limitations](https://docs.typesafe.ai/model-jaggedness/jev-1.13) - Account for literal interpretation, numerical weaknesses, distracting state, and adversarial inputs.
- [Noul self-consistency](https://docs.typesafe.ai/cookbooks/consistency_noul_cookbook) - Inspect repeated answers and see how a review interval changes automatic-decision coverage.

## Contributing

Suggest a resource you have inspected or used, explain who it helps, and disclose your connection to it. Read the [contribution guide](CONTRIBUTING.md) for inclusion criteria, entry format, and checks. Broken links and corrections are welcome too.

This repository was produced with AI agents using primary documentation, source review, offline tests, and explicit live checks. See [validation scope](docs/validation.md) and [maintenance and provenance](docs/maintaining.md) for the review process and its boundaries. This project is not affiliated with or endorsed by TypeSafe AI or the central Awesome directory.

The list and documentation use CC0; original code uses MIT. See [licensing](LICENSE.md).
