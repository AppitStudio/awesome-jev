# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Discover Jev-powered apps, developer resources, and runnable decision examples.

[Jev](https://docs.typesafe.ai/introduction) is TypeSafe AI's System One model: give it state and typed questions, then use the returned choices, scores, and probabilities in your code. This independent community directory collects applications that use Jev, resources for developers, and small, inspectable workflows to learn from.

**[Explore Jev-powered apps](community/README.md#apps-powered-by-jev)** · **[Share your app](CONTRIBUTING.md#list-a-jev-powered-app)**

## Contents

- [Explore Jev with our skill](#explore-jev-with-our-skill)
- [Start here](#start-here)
  - [Explore practical use cases](docs/explore-use-cases.md)
- [Official SDKs and tools](#official-sdks-and-tools)
- [Community projects](#community-projects)
  - [Apps powered by Jev](#apps-powered-by-jev)
  - [Browse the project directory](community/README.md)
- [Computer and browser use](#computer-and-browser-use)
- [Starter projects](#starter-projects)
- [Reference project](#reference-project)
- [Patterns and cookbooks](#patterns-and-cookbooks)
  - [Routing and classification](#routing-and-classification)
  - [Retrieval and verification](#retrieval-and-verification)
  - [Extraction and structured data](#extraction-and-structured-data)
- [Model behavior and evaluation](#model-behavior-and-evaluation)
- [Contributing](#contributing)

## Explore Jev with our skill

Use **Awesome Jev Guide** to understand Jev and explore solutions that fit your needs. Describe your workflow in plain language, and your coding agent will help you choose an example, adapt a project, or build a suitable starter—with guided setup along the way.

**1. Install the skill.** With Node.js 22+ installed, run this in your project directory:

```sh
npx skills add AppitStudio/awesome-jev --skill awesome-jev-guide
```

Select your coding agent when prompted. For Codex, you can add `--agent codex`. No TypeSafe account or API key is needed to explore ideas or run the offline examples.

**2. Open your coding agent in that project and try a prompt.**

New to Jev? Start here:

```text
Use awesome-jev-guide. Explain Jev simply, help me understand what I can
build with it, and walk me through the easiest example. I don't have
an API key yet.
```

Have a workflow in mind? Fill in the brackets:

```text
Use awesome-jev-guide. Today I [describe the work I do manually].
I want to [describe the result]. I use [language, framework, or tools].
Help me find the best starting point in this repo and explain what
needs adapting. Ask me anything essential that's missing.
```

Ready to build?

```text
Use awesome-jev-guide to build a small starter for [my workflow] using
[my stack]. Start with a working offline demo, explain what I should
customize, then guide me through API-key setup and a first live check
when I'm ready.
```

**3. Follow the next step together.** The guide uses current TypeSafe documentation and explains what already works, what needs building, and how to handle uncertain results. When you want live access, it walks you through private key setup—never paste a key into chat.

See the [full onboarding guide](docs/using-the-guide.md) for installation options, demos, and setup details.

## Start here

**[Explore what you can build](docs/explore-use-cases.md)** — choose a real implementation by the result you want, then follow its guide, worked example, and setup path.

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

**[Browse projects by category](community/README.md)** for dedicated pages with use cases, setup, examples, limitations, and review evidence. The links below still take you directly to the upstream projects.

Checks are tied to reviewed versions; see each page and the [validation scope](docs/validation.md#community-project-checks). Mocked tests and reported live smoke checks do not establish model quality on your workload.

### Apps powered by Jev

Applications with a user-facing workflow powered in part or entirely by Jev. The [app directory](community/README.md#apps-powered-by-jev) shows platforms, access requirements, and Jev's specific role. Makers are welcome to [submit their own apps](CONTRIBUTING.md#list-a-jev-powered-app).

- [Jev Search](https://github.com/superagents-lab/jev-search) - Selects search sources and filters, then ranks retrieved links using Jev and Search1API. [Project guide](community/projects/jev-search.md).
- [Notra](https://github.com/usenotra/notra) - Uses Jev judgments within a broader application for tracking brand mentions and placement in AI answers. [Project guide](community/projects/notra.md).
- [TipTour](https://github.com/milind-soni/tiptour-macos) - macOS menu bar app that uses Jev to select desktop click targets from typed requests, alongside a separate Gemini voice mode. [Project guide](community/projects/tiptour.md).

### Developer projects and integrations

- [Cua jev-use](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use) - Composes a bounded Jev chooser with Cua Driver and an independently verified browser fixture. [Project guide](community/projects/cua-jev-use.md).
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Selects tool-call/result pairs to keep, truncate, or remove while preserving retained conversation content verbatim. [Project guide](community/projects/fast-jev-compaction.md).
- [Jev Browser (tontoko)](https://github.com/tontoko/jev-browser) - Integrates Jev field selection and source-backed extraction with a Playwright SDK, CLI, MCP server, and explicit assertions. [Project guide](community/projects/jev-browser-tontoko.md).
- [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev) - Turns judgments over selected Home Assistant state into sensors and automation responses, with usage accounting. [Project guide](community/projects/ha-jev.md).
- [Jev Logs](https://github.com/reachjalil/jevlogs) - Scores OpenTelemetry logs for a separate analysis branch, with mock mode and conservative error handling. [Project guide](community/projects/jevlogs.md).
- [Jev Review](https://github.com/NiazMorshed2007/jev-review) - MCP server for experimental software-quality rubric scores and comparisons; requires `JEV_API_KEY` and sends supplied code context to TypeSafe. [Project guide](community/projects/jev-review.md).
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - Selects browser operations and observed targets with Jev, using a separate text model for text entry. [Project guide](community/projects/jev-ultrafast.md).
- [Laravel AI](https://github.com/laravel/ai) - Provides typed classification and a TypeSafe provider for Laravel applications, with fake responses for application testing. [Project guide](community/projects/laravel-ai.md).
- [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) - Python integrations for LlamaIndex passage reranking and query-engine selection, with configurable error and selection behavior. [Project guide](community/projects/llama-index-jev.md).
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Selects Android actions and exact input text through Mobilerun, with a local studio and task-specific verification demo. [Project guide](community/projects/mobile-jev.md).
- [neo4jev](https://github.com/jexp/neo4jev) - Explores Neo4j paths using next-hop choices and goal judgments, with notebooks and a Streamlit interface. [Project guide](community/projects/neo4jev.md).
- [pg-jev](https://github.com/realZachi/pg-jev) - Adds semantic predicates, probabilities, choices, and scores to PostgreSQL through a PL/Python extension. [Project guide](community/projects/pg-jev.md).
- [Testimonial miner](https://github.com/AppitStudio/testimonial-miner) - Python CLI that finds quotable user praise in Gmail mailboxes with one Jev request per email (message kind, app, praise quality, and a Noul per sentence) and stores verbatim quotes for review; requires a TypeSafe key and Google app passwords, and sends cleaned email text to TypeSafe. [Project guide](community/projects/testimonial-miner.md).
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - Combines local OCR and Accessibility observations with Jev decisions to operate macOS, with an optional writing model. [Project guide](community/projects/typesafe-computer-use.md).
- [TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net) - Community .NET client with typed questions, dependency injection, and Microsoft.Extensions.AI adapters. [Project guide](community/projects/typesafeai-net.md).

## Computer and browser use

**[Explore computer-use solutions](docs/computer-use.md)** for browser navigation, form filling, data extraction, macOS/Android control, and iOS Simulator experiments. The guide compares inspected implementations, explains their testing boundaries, and develops a practical observe → choose → act → verify design.

Start with [Jev Browser (tontoko)](community/projects/jev-browser-tontoko.md) for Playwright forms, extraction, and app tests, or [Jev Ultrafast](community/projects/jev-ultrafast.md) to study a compact browser loop. Native macOS and Android have separate implementations; the iOS Jev + AXe work is documented as a public demonstration with an unverified release path.

Try the [offline computer-use example](examples/computer-use/README.md) to see field selection, exact source extraction, freshness checks, and independent assertions without controlling a real device:

```sh
python3 examples/computer-use/run.py
```

## Starter projects

Original examples maintained in this repository. Each includes readable questions, application policy, synthetic responses, tests, and an optional live mode. **Mock results demonstrate code behavior, not Jev accuracy.**

- [Computer-use decision cycle](examples/computer-use/README.md) - Select a form field and source value, then check a simulated action with independent assertions; uses its own runner.
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

App makers can [share a Jev-powered app](CONTRIBUTING.md#list-a-jev-powered-app), including commercial and closed-source products with clear access terms. Use the [contributor skill](CONTRIBUTING.md#use-the-contributor-skill) to have a coding agent check your app, project, or starter kit and prepare a focused submission with evidence.

This repository was produced with AI agents using primary documentation, source review, offline tests, and explicit live checks. See [validation scope](docs/validation.md) and [maintenance and provenance](docs/maintaining.md) for the review process and its boundaries. This project is not affiliated with or endorsed by TypeSafe AI or the central Awesome directory.

The list and documentation use CC0; original code uses MIT. See [licensing](LICENSE.md).
