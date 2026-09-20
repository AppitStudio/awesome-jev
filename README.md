# Awesome Jev [![Awesome](https://awesome.re/badge.svg)](https://awesome.re)

> Discover Jev-powered apps, developer resources, and runnable decision examples.

[Jev](https://docs.typesafe.ai/introduction) is TypeSafe AI's System One model: give it state and typed questions, then use the returned choices, scores, and probabilities in your code. This independent community directory collects applications that use Jev, resources for developers, and small, inspectable workflows to learn from.

**[Explore Jev-powered apps](community/projects/apps/README.md)** · **[Share your app](CONTRIBUTING.md#list-a-jev-powered-app)**

**Try the beta web UI at [JevList](https://jevlist.ai/).** Explore the projects in this directory through a searchable web interface. We're continually improving the experience—take a look and let us know what you think!

## Contents

- [Explore Jev with our skill](#explore-jev-with-our-skill)
- [Start here](#start-here)
  - [Explore practical use cases](docs/explore-use-cases.md)
- [Official SDKs and tools](#official-sdks-and-tools)
- [Community projects](#community-projects)
  - [Apps powered by Jev](#apps-powered-by-jev)
  - [Browse the project directory](community/projects/README.md)
  - [Tools and integrations](community/projects/tools/README.md)
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

**[Browse the project directory](community/projects/README.md)** for separate app and tool directories, each with full project pages covering use cases, setup, examples, limitations, and review evidence. The links below still take you directly to the upstream projects.

Checks are tied to reviewed versions; see each page and the [validation scope](docs/validation.md#community-project-checks). Mocked tests and reported live smoke checks do not establish model quality on your workload.

### Apps powered by Jev

Applications with a user-facing workflow powered in part or entirely by Jev. The [full app directory](community/projects/apps/README.md) shows platforms, access requirements, and Jev's specific role. [Tags](community/APP_TAGS.md) distinguish source access from pricing; commercial and closed-source apps can qualify. Makers are welcome to [submit their own apps](CONTRIBUTING.md#list-a-jev-powered-app).

- [Jev Anti-Spam Bot](https://github.com/backmeupplz/jev_antispam_bot) - `Open source` · `Free source build` · `BYOK`. Self-hosted Telegram bot that deletes high-confidence spam using TypeSafe Jev Noul signals, with fail-open errors. [Project guide](community/projects/apps/jev-antispam-bot.md).
- [Jev Mail Classifier](https://github.com/parth-kp/jev-mail-classifier) - `Open source` · `Free source build` · `BYOK`. Classifies IMAP inbox messages with Jev category judgments, then tags, moves, flags, or notifies from a local Textual TUI and CLI. [Project guide](community/projects/apps/jev-mail-classifier.md).
- [Jevmail](https://github.com/fazlerocks/jevmail) - `Open source` · `Free source build` · `BYOK`. Local read-only Gmail triage into Needs reply/Updates/Promos/Sales/Spam with TypeSafe Jev over the Vercel AI Gateway. [Project guide](community/projects/apps/jevmail.md).
- [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) - `Source unverified` · `Pricing unverified` · `BYOK`. Self-hosted Discord bot using Jev message classifications for automatic deletion, escalating timeouts and moderator-requested activity profiles. [Project guide](community/projects/apps/jev-moderation-bot.md).
- [Jev Radar](https://github.com/Eliovp-BV/Jev-Radar) - `Open source` · `Free source build` · `BYOK`. Local research workspace where Jev steers investigation over public sources with inspectable decisions and optional text-model drafting. [Project guide](community/projects/apps/jev-radar.md).
- [Jev Search](https://github.com/superagents-lab/jev-search) - `Open source` · `Pricing unverified` · `BYOK`. Selects search sources and filters, then ranks retrieved links using Jev and Search1API. [Try app](https://jev.s1.dev/) · [Project guide](community/projects/apps/jev-search.md).
- [Jevmeter](https://github.com/ChetasLua/jevmeter) - `Open source` · `Free source build` · `BYOK`. Renders video captions, gauges and highlights from Jev judgments about transcript sentences; these judgments are not fact-checks. [Project guide](community/projects/apps/jevmeter.md).
- [Jev Voice](https://github.com/kevinbadi/jev-voice) - `Open source` · `Free source build` · `BYOK`. Hands-free macOS voice assistant: local whisper.cpp plus one Jev call per command to select typed actions and arguments. [Project guide](community/projects/apps/jev-voice.md).
- [Live Jev](https://github.com/okinaaudio/live-jev) - `Open source` · `Free source build` · `BYOK`. Early macOS Ableton Live controller: hotkey bar + TypeSafe Jev picks typed mixer/device actions from short EN/JP phrases. [Project guide](community/projects/apps/live-jev.md).
- [macbrow](https://github.com/timpratim/macbrow) - `Open source` · `Free source build` · `BYOK`. Experimental macOS voice assistant using Jev to route commands to AppleScript tools and Chrome browser tasks. [Project guide](community/projects/apps/macbrow.md).
- [Notra](https://github.com/usenotra/notra) - `Open source` · `Commercial` · `Paid`. Uses Jev judgments within a broader application for tracking brand mentions and placement in AI answers. [Product](https://www.usenotra.com) · [Pricing](https://www.usenotra.com/pricing) · [Project guide](community/projects/apps/notra.md).
- [Smart Paste](https://github.com/nomanjack/smart-paste) - `Open source` · `Free source build` · `BYOK`. Experimental Chrome extension that uses Jev to select and verify exact source text for web form fields, with paste and undo. [Project guide](community/projects/apps/smart-paste.md).
- [Sponsor Skip](https://github.com/trungdq88/youtube-sponsor-detection) - `Source unverified` · `Pricing unverified` · `BYOK`. Locates YouTube sponsor reads with Jev-selected transcript boundaries and optional Deepgram audio analysis, with playback skipping. [Project guide](community/projects/apps/sponsor-skip.md).
- [TipTour](https://github.com/milind-soni/tiptour-macos) - `Open source` · `Free source build` · `BYOK`. macOS menu bar app that uses Jev to select desktop click targets from typed requests, alongside a separate Gemini voice mode. [Project guide](community/projects/apps/tiptour.md).
- [TypeSafe Fun AdBlocker](https://github.com/realZachi/typesafe-adblock) - `Open source` · `Free source build` · `BYOK`. Experimental Chrome extension that asks Jev whether heuristically selected DOM elements are ads, then removes or highlights matches. [Project guide](community/projects/apps/typesafe-adblock.md).
- [Unclutter](https://github.com/kitze/unclutter) - `Open source` · `Free source build` · `BYOK`. Classifies page clutter with Jev and saves reversible hiding rules for similar pages, with manual analysis by default. [Project guide](community/projects/apps/unclutter.md).
- [Vibe Check for X](https://github.com/RafalWilinski/vibecheck) - `Source unverified` · `Pricing unverified` · `BYOK`. Chrome extension that uses Jev to score draft X posts and display a verdict, with optional OpenAI media descriptions. [Project guide](community/projects/apps/vibecheck.md).

### Developer projects and integrations

The [independent model research](community/projects/tools/README.md#independent-model-research) category explores related typed-decision interfaces with other models. Their local inference uses those models, and they do not provide official Jev weights.

- [Advocaat](https://github.com/pithings/advocaat) - TypeScript `ask` client that batches typed Jev choice, score, and yes/no questions about structured data, with optional Vercel AI Gateway support. [Project guide](community/projects/tools/advocaat.md).
- [Cua jev-use](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use) - Composes a bounded Jev chooser with Cua Driver and an independently verified browser fixture. [Project guide](community/projects/tools/cua-jev-use.md).
- [doc-router](https://github.com/misbahsy/doc-router) - Routes PDF pages between local text extraction and OCR using optional Jev judgments, with a Rust CLI and Python bindings. [Project guide](community/projects/tools/doc-router.md).
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Selects tool-call/result pairs to keep, truncate, or remove while preserving retained conversation content verbatim. [Project guide](community/projects/tools/fast-jev-compaction.md).
- [Foreman](https://github.com/thruwire/foreman) - Supervises Codex workers with Jev assessments and deterministic steering, retry, and verification policy, with a synthetic demo. [Project guide](community/projects/tools/foreman.md).
- [Jev Browser (tontoko)](https://github.com/tontoko/jev-browser) - Integrates Jev field selection and source-backed extraction with a Playwright SDK, CLI, MCP server, and explicit assertions. [Project guide](community/projects/tools/jev-browser-tontoko.md).
- [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev) - Turns judgments over selected Home Assistant state into sensors and automation responses, with usage accounting. [Project guide](community/projects/tools/ha-jev.md).
- [Jev Logs](https://github.com/reachjalil/jevlogs) - Scores OpenTelemetry logs for a separate analysis branch, with mock mode and conservative error handling. [Project guide](community/projects/tools/jevlogs.md).
- [Jev Model Router](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-model-router) - Early-access Claude Code mod that uses Jev task assessments and configurable confidence thresholds to route subagent models and main-conversation reasoning effort. [Project guide](community/projects/tools/jev-model-router.md).
- [Jev Review](https://github.com/NiazMorshed2007/jev-review) - MCP server for experimental software-quality rubric scores and comparisons; requires `JEV_API_KEY` and sends supplied code context to TypeSafe. [Project guide](community/projects/tools/jev-review.md).
- [Jev Review (Dev Agrawal)](https://github.com/devagrawal09/jev-review) - Screens JavaScript and TypeScript changes or source files with staged Jev judgments and displays evidence-linked findings in a local dashboard. [Project guide](community/projects/tools/jev-review-devagrawal.md).
- [Jev Sift](https://github.com/kbhuw/jev-sift) - Screens files, public webpages, and tool descriptions with Jev before an agent reads selected content; requires a TypeSafe key, and upstream licensing is unspecified. [Project guide](community/projects/tools/jev-sift.md).
- [JevScope](https://github.com/jeiel85/jevscope) - Local-first visual workbench and JSONL regression testbench for TypeSafe Jev projects. [Project guide](community/projects/tools/jevscope.md).
- [Jev Trader](https://github.com/jarrodwatts/jev-trader) - Studies Jev market-direction choices, simulated fills, and on-chain order execution through a Bun trading experiment. [Project guide](community/projects/tools/jev-trader.md).
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - Selects browser operations and observed targets with Jev, using a separate text model for text entry. [Project guide](community/projects/tools/jev-ultrafast.md).
- [Jev Voice Browser](https://github.com/moritzkremb/jev-voice-browser) - Experiments with typed Jev decisions over partial voice transcripts and page elements to control Playwright, with a local decision inspector. [Project guide](community/projects/tools/jev-voice-browser.md).
- [Jev-cu](https://github.com/Sac-Y/Jev-cu) - Experimental Codex skill and JavaScript runtime for selecting macOS Accessibility targets with Jev, with action previews and optional result verification; execution-policy limitations require review. [Project guide](community/projects/tools/jev-cu.md).
- [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) - Routes each Codex turn through Jev tier and thinking-depth selection via a local Codex Router generic provider, with fail-open fallbacks and an optional Codex-dry tandem. [Project guide](community/projects/tools/jev-codex-router.md).
- [jev-gateway](https://github.com/vinilana/jev-gateway) - Local LLM gateway that asks TypeSafe Jev which tool to call for Codex, Claude Code, OpenCode, or Gemini while other traffic uses your usual LLM. [Project guide](community/projects/tools/jev-gateway.md).
- [jev-drone](https://github.com/RomanSlack/jev-drone) - Explores Jev tactical judgments in a MuJoCo quadrotor simulation, with local flight control and a separate experimental tunnel policy. [Project guide](community/projects/tools/jev-drone.md).
- [jev-pruner](https://github.com/tamaratran/jev-pruner) - Prunes eligible Bash stdout with Jev before it reaches Claude Code or an opt-in Codex wrapper, while archiving the original output locally. [Project guide](community/projects/tools/jev-pruner.md).
- [jev-router](https://github.com/gargpratyush/jev-router) - Routes fresh Claude Code and Codex turns through Jev model selection and deterministic fallback policy, with locally inspectable routing exchanges. [Project guide](community/projects/tools/jev-router.md).
- [jev-rules](https://github.com/EliaAlberti/jev-rules) - Selects Claude Code project rules and map documents with Jev judgments over prompts and file paths, with session caching and fallback context. [Project guide](community/projects/tools/jev-rules.md).
- [jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Ranks recent zsh commands with Jev for inline suggestions; sends selected history to TypeSafe and requires a user-supplied API key. [Project guide](community/projects/tools/jev-shell-history.md).
- [jev-use (shitianfang)](https://github.com/shitianfang/jev-use) - Hands the Claude Code, Codex and pi steps that need no text output to Jev, returning anything it should not decide to the LLM under a typed escalation contract. [Project guide](community/projects/tools/jev-use.md).
- [Jevlike](https://github.com/vinnylarouge/jevlike) - Trains a small option-attention scorer with synthetic data and optional frozen encoders; independent of official Jev. [Project guide](community/projects/tools/jevlike.md).
- [JevOnly](https://github.com/buluoray/JevOnly) - Pure-Jev browser agent: code enumerates page/goal options, Jev only picks, with verify/undo and an irreversible-action gate. [Project guide](community/projects/tools/jevonly.md).
- [JevPilot](https://github.com/standardagents/jevpilot) - Demonstrates Jev maneuver selection in a browser driving simulation with local collision checks; application licensing is unspecified. [Project guide](community/projects/tools/jevpilot.md).
- [JevSQL](https://github.com/EugeneBoondock/jevsql) - Adds TypeSafe Jev natural-language predicates and decision tables to SQLite SQL with batching, caching, and review queues; distinct from pg-jev. [Project guide](community/projects/tools/jevsql.md).
- [Laravel AI](https://github.com/laravel/ai) - Provides typed classification and a TypeSafe provider for Laravel applications, with fake responses for application testing. [Project guide](community/projects/tools/laravel-ai.md).
- [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) - Python integrations for LlamaIndex passage reranking and query-engine selection, with configurable error and selection behavior. [Project guide](community/projects/tools/llama-index-jev.md).
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Selects Android actions and exact input text through Mobilerun, with a local studio and task-specific verification demo. [Project guide](community/projects/tools/mobile-jev.md).
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - Studies independent Qwen-based typed decision heads, local serving, and game controllers with recorded comparisons. [Project guide](community/projects/tools/nanojev.md).
- [neo4jev](https://github.com/jexp/neo4jev) - Explores Neo4j paths using next-hop choices and goal judgments, with notebooks and a Streamlit interface. [Project guide](community/projects/tools/neo4jev.md).
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Implements a Jev-shaped HTTP decision API using Qwen and SGLang; independent model behavior and unspecified code licensing. [Project guide](community/projects/tools/openjev-sglang.md).
- [pg-jev](https://github.com/realZachi/pg-jev) - Adds semantic predicates, probabilities, choices, and scores to PostgreSQL through a PL/Python extension. [Project guide](community/projects/tools/pg-jev.md).
- [pg_typesafe](https://github.com/giuliosmall/pg_typesafe) - Pre-alpha PostgreSQL C extension for TypeSafe Jev Choice/Noul/Score with batched multi-text helpers; distinct from pg-jev. [Project guide](community/projects/tools/pg-typesafe.md).
- [pi-jev](https://github.com/y0usaf/pi-jev) - Adds a TypeSafe Jev gate, output judge, and jev_ask tool to the Pi coding agent, with shadow mode by default and fail-open errors. [Project guide](community/projects/tools/pi-jev.md).
- [pi-jev-sentinel](https://github.com/harshwasan/pi-jev-sentinel) - Adds TypeSafe Jev checks for Pi, Claude Code, and Codex tool calls, tool outputs, and replies, with secret scrubbing and fail-closed asks when unconfigured. [Project guide](community/projects/tools/pi-jev-sentinel.md).
- [pi-Jev-browser](https://github.com/laihenyi/pi-Jev-browser) - Pi extension where TypeSafe Jev chooses each Playwright browser action over a structured DOM observation in a bounded loop. [Project guide](community/projects/tools/pi-jev-browser.md).
- [pi-warden](https://github.com/DevMortimer/pi-warden) - Combines local Pi guard checks with Jev action and rule judgments, configurable holds, corrective feedback and context retention. [Project guide](community/projects/tools/pi-warden.md).
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) - Stdlib-lean Ruby client for Noul/Choice/Score decision models via Typesafe or OpenRouter. [Project guide](community/projects/tools/ruby-decision-model.md).
- [SemIf](https://github.com/TheoLeeCJ/SemIf) - Explores typed option scoring and shared-state reuse with local open models; independent of official Jev. [Project guide](community/projects/tools/semif.md).
- [SkillRanker](https://github.com/Dicklesworthstone/skillranker) - Ranks agent skills for the next step from live session context using TypeSafe Jev, with offline demos and a Claude Code hook; MIT plus an OpenAI/Anthropic license rider. [Project guide](community/projects/tools/skillranker.md).
- [Skillbox](https://github.com/kitze/skillbox) - Self-hosts a versioned agent skill library with optional Jev recommendations over authorized skills and explicit search fallback. [Project guide](community/projects/tools/skillbox.md).
- [Stanley Code](https://github.com/devagrawal09/stanley-code) - Routes coding requests into bounded Jev review and triage workflows, with trusted repository extensions and an optional Pi coding-agent fallback. [Project guide](community/projects/tools/stanley-code.md).
- [Supercov](https://github.com/supercorp-ai/supercov) - Code quality and test coverage for coding agents: Jev scores each source file so the agent knows what to fix first. [Project guide](community/projects/tools/supercov.md).
- [super-jev](https://github.com/Kevthetech143/super-jev) - Evidence-to-action TypeScript harness: typed Jev judgments, permitted tools, verified outcomes, and JSONL journals. [Project guide](community/projects/tools/super-jev.md).
- [Testimonial miner](https://github.com/AppitStudio/testimonial-miner) - Python CLI that finds quotable user praise in Gmail mailboxes with one Jev request per email (message kind, app, praise quality, and a Noul per sentence) and stores verbatim quotes for review; requires a TypeSafe key and Google app passwords, and sends cleaned email text to TypeSafe. [Project guide](community/projects/tools/testimonial-miner.md).
- [toolgate](https://github.com/RiskAverseTech/toolgate) - Open Claude Code PreToolUse and MCP tool-call firewall with static rules, TypeSafe Jev judgments, YAML policy, and a local audit log. [Project guide](community/projects/tools/toolgate.md).
- [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) - Selects emulator controller inputs with Jev from structured Mario telemetry; includes a synthetic state demo, with upstream licensing unspecified. [Project guide](community/projects/tools/typesafe-mario.md).
- [TypeSafe MCP](https://github.com/itsmostafa/typesafe-mcp) - Exposes typed Jev questions to MCP clients and pi, preserving provider responses with configurable direct or OpenRouter access. [Project guide](community/projects/tools/typesafe-mcp.md).
- [typesafeai-cli](https://github.com/maddygoround/typesafeai-cli) - Python `typesafe` CLI for TypeSafe Jev ask/decide/screen/verify flows for humans and agents. [Project guide](community/projects/tools/typesafeai-cli.md).
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - Combines local OCR and Accessibility observations with Jev decisions to operate macOS, with an optional writing model. [Project guide](community/projects/tools/typesafe-computer-use.md).
- [TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net) - Community .NET client with typed questions, dependency injection, and Microsoft.Extensions.AI adapters. [Project guide](community/projects/tools/typesafeai-net.md).

## Computer and browser use

**[Explore computer-use solutions](docs/computer-use.md)** for browser navigation, form filling, data extraction, macOS/Android control, and iOS Simulator experiments. The guide compares inspected implementations, explains their testing boundaries, and develops a practical observe → choose → act → verify design.

Start with [Jev Browser (tontoko)](community/projects/tools/jev-browser-tontoko.md) for Playwright forms, extraction, and app tests, or [Jev Ultrafast](community/projects/tools/jev-ultrafast.md) to study a compact browser loop. Native macOS and Android have separate implementations; the iOS Jev + AXe work is documented as a public demonstration with an unverified release path.

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
