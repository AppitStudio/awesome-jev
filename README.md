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

- [Agent skill](https://docs.typesafe.ai/agent-skill) - Official docs for giving a coding agent API context and guidance when designing narrow System One / Jev decision questions (Claude Code plugin and skills.sh install paths).
- [JavaScript SDK](https://github.com/typesafe-ai/typesafe-sdk-js) - JavaScript and TypeScript client that infers answer types from the supplied questions.
- [Python SDK](https://github.com/typesafe-ai/typesafe-sdk-python) - Synchronous and asynchronous clients with typed answers and configurable retries.
- [System One Adapter](https://github.com/typesafe-ai/system-one-adapter-python) - Run a similar typed-question interface against other LLM providers for comparisons; those responses do not come from Jev.
- [TypeSafe Agent Skills](https://github.com/typesafe-ai/skills) - Official Claude Code / skills.sh agent skill for designing typed System One / Jev decisions; [docs](https://docs.typesafe.ai/agent-skill).

## Community projects

**[Browse the project directory](community/projects/README.md)** for separate app and tool directories, each with full project pages covering use cases, setup, examples, limitations, and review evidence. The links below still take you directly to the upstream projects.

Checks are tied to reviewed versions; see each page and the [validation scope](docs/validation.md#community-project-checks). Mocked tests and reported live smoke checks do not establish model quality on your workload.

### Apps powered by Jev

Applications with a user-facing workflow powered in part or entirely by Jev. The [full app directory](community/projects/apps/README.md) shows platforms, access requirements, and Jev's specific role. [Tags](community/APP_TAGS.md) distinguish source access from pricing; commercial and closed-source apps can qualify. Makers are welcome to [submit their own apps](CONTRIBUTING.md#list-a-jev-powered-app).

- [Apparite (jev2ui)](https://github.com/dglazkov/jev2ui) - `Open source` · `Free source build` · `BYOK`. Local design-mock lab: TypeSafe Jev chooses IA/anatomy; Gemini writes copy; code assembles A2UI-inspired mocks. [Project guide](community/projects/apps/jev2ui.md).
- [Call Coach](https://github.com/ZeroGold/call-coach-ai) - `Open source` · `Free source build` · `BYOK`. Local live sales-call coach: TypeSafe Jev picks next actions and buying stage from transcript turns (mic or sample call). [Project guide](community/projects/apps/call-coach-ai.md).
- [Clean Code Review](https://github.com/frostney/clean-code-review) - `Open source` · `Free source build` · `BYOK`. Hosted/source PR reviewer: TypeSafe Jev judges files on Clean Code questions; Luna writes evidence-first prose (MCP included). [Try app](https://clean-code-review.vercel.app) · [Project guide](community/projects/apps/clean-code-review.md).
- [Crush Monitor](https://github.com/FerryCorleone/crush-monitor) - `Open source` · `Free source build` · `BYOK`. Local WeChat-style chat analyzer: TypeSafe Jev labels emotion/intent, scores affinity, and rates replies (BYOK). [Project guide](community/projects/apps/crush-monitor.md).
- [Focus](https://github.com/bramtechs/Focus) - `Open source` · `Free source build` · `BYOK`. Browser extension that classifies domains as productive or distracting with TypeSafe Jev via OpenRouter Decisions and blocks distracting navigations. [Project guide](community/projects/apps/focus.md).
- [Fotocopiatrice](https://github.com/bnistor4/fotocopiatrice) - `Open source` · `Free source build` · `BYOK`. Italian Camera amendment explorer: code dedupes identical texts; TypeSafe Jev judges attributes and near-duplicate pairs (static site). [Try app](https://fotocopiatrice.vercel.app/) · [Project guide](community/projects/apps/fotocopiatrice.md).
- [Hearth](https://github.com/Nancy-Chauhan/hearth-jev-rental-search) - `Open source` · `Free source build` · `BYOK`. Local Chrome agent that searches four rental marketplaces with TypeSafe Jev action choice and returns a shortlist (read-only). [Project guide](community/projects/apps/hearth.md).
- [HookMeter](https://github.com/ehui1226/hookmeter-jev) - `Open source` · `Free source build` · `BYOK`. Chrome extension that scores social drafts as you type with TypeSafe Jev (curiosity/arousal/pattern/clickbait) via optional worker/backend. [Project guide](community/projects/apps/hookmeter.md).
- [Hx](https://github.com/doitrous/hx) - `Open source` · `Free source build` · `BYOK`. Clinical note checklist that ticks items against clauses from the note using TypeSafe Jev (never generates text). [Project guide](community/projects/apps/hx.md).
- [Jev Anti-Spam Bot](https://github.com/backmeupplz/jev_antispam_bot) - `Open source` · `Free source build` · `BYOK`. Self-hosted Telegram bot that deletes high-confidence spam using TypeSafe Jev Noul signals, with fail-open errors. [Project guide](community/projects/apps/jev-antispam-bot.md).
- [Jev Call Screener](https://github.com/SuchintK/jev-call-screener) - `Open source` · `Free source build` · `BYOK`. Self-hosted call screening: TypeSafe Jev classifies caller transcripts; Go policy forwards or rejects (Twilio adapter; fail-open defaults). [Project guide](community/projects/apps/jev-call-screener.md).
- [Jev Chat Assistant](https://github.com/Finderchangchang/jev-chat-JARVIS) - `Open source` · `Free source build` · `BYOK`. Android overlay: Accessibility reads chat; TypeSafe Jev (OpenRouter) judges intent/danger and ranks fill-only reply candidates (WeChat first). [Project guide](community/projects/apps/jev-chat-jarvis.md).
- [Jev demos](https://github.com/mayank953/Jev) - `Open source` · `Free source build` · `BYOK`. Six local side-by-side TypeSafe Jev demos with Claude/Kimi switcher and simulated mode without keys. [Project guide](community/projects/apps/jev-demos.md).
- [Jev for Chrome](https://github.com/chy4pro/jev-for-chrome) - `Open source` · `Free source build` · `BYOK`. Chrome extension that drives your current tab with TypeSafe Jev (community port of jev-ultrafast); separate text model for typing. [Project guide](community/projects/apps/jev-for-chrome.md).
- [Jev Grand Prix](https://github.com/enoyola/jev-grand-prix) - `Open source` · `Free source build` · `BYOK`. Local F1 race: TypeSafe Jev picks line and pedals; code steers and plans next laps. [Project guide](community/projects/apps/jev-grand-prix.md).
- [Jevfill](https://github.com/imohitmayank/jevfill) - `Open source` · `Free source build` · `BYOK`. Chrome extension that autofills forms from unstructured notes with TypeSafe Jev field matching (skips password/payment). Distinct from Smart Paste. [Project guide](community/projects/apps/jevfill.md).
- [jevx](https://github.com/hawkyre/jevx) - `Open source` · `Free source build` · `BYOK`. Chrome/Firefox extension: find relevant X posts and score drafts with TypeSafe Jev (BYOK; no backend). [Project guide](community/projects/apps/jevx.md).
- [Jev Mail Classifier](https://github.com/parth-kp/jev-mail-classifier) - `Open source` · `Free source build` · `BYOK`. Classifies IMAP inbox messages with Jev category judgments, then tags, moves, flags, or notifies from a local Textual TUI and CLI. [Project guide](community/projects/apps/jev-mail-classifier.md).
- [Jevmail](https://github.com/fazlerocks/jevmail) - `Open source` · `Free source build` · `BYOK`. Local read-only Gmail triage into Needs reply/Updates/Promos/Sales/Spam with TypeSafe Jev over the Vercel AI Gateway. [Project guide](community/projects/apps/jevmail.md).
- [JevZero](https://github.com/jayozer/jevzero) - `Open source` · `Free source build` · `BYOK`. Local Gmail triage with TypeSafe Jev: review proposed labels, apply with receipts, and undo. [Project guide](community/projects/apps/jevzero.md).
- [Jev Moderation Bot](https://github.com/brainstormity/Jev-Moderation-Bot) - `Source unverified` · `Pricing unverified` · `BYOK`. Self-hosted Discord bot using Jev message classifications for automatic deletion, escalating timeouts and moderator-requested activity profiles. [Project guide](community/projects/apps/jev-moderation-bot.md).
- [JevEye](https://github.com/Adityakhalkar/JevEye) - `Open source` · `Free source build` · `BYOK`. Browser vision probes report calibrated facts; TypeSafe Jev plans probes and judges the text fact sheet (never pixels). [Project guide](community/projects/apps/jeveye.md).
- [Jev Radar](https://github.com/Eliovp-BV/Jev-Radar) - `Open source` · `Free source build` · `BYOK`. Local research workspace where Jev steers investigation over public sources with inspectable decisions and optional text-model drafting. [Project guide](community/projects/apps/jev-radar.md).
- [Jev Search](https://github.com/superagents-lab/jev-search) - `Open source` · `Pricing unverified` · `BYOK`. Selects search sources and filters, then ranks retrieved links using Jev and Search1API. [Try app](https://jev.s1.dev/) · [Project guide](community/projects/apps/jev-search.md).
- [Jev Social](https://github.com/socai-io/jev-social) - `Open source` · `Free source build` · `BYOK`. Local UI/CLI where TypeSafe Jev (via OpenRouter) chooses read-only Instagram/TikTok/LinkedIn research ops executed by socai in Chrome. [Project guide](community/projects/apps/jev-social.md).
- [JevSlop](https://github.com/TKY-27/JevSlop) - `Open source` · `Free source build` · `BYOK`. Scores note articles for AI-slop writing patterns with TypeSafe Jev (BYOK). [Try app](https://jevslop.pages.dev/) · [Project guide](community/projects/apps/jevslop.md).
- [JEV Document Classification](https://github.com/Charlyhno-eng/jev-document-classification) - `Open source` · `Free source build` · `BYOK`. Local-first folder filer: TypeSafe Jev (Vercel AI Gateway) chooses category/confidentiality/injection/subject; audit preview and undo. [Project guide](community/projects/apps/jev-document-classification.md).
- [Jevmeter](https://github.com/ChetasLua/jevmeter) - `Open source` · `Free source build` · `BYOK`. Renders video captions, gauges and highlights from Jev judgments about transcript sentences; these judgments are not fact-checks. [Project guide](community/projects/apps/jevmeter.md).
- [Jev Voice](https://github.com/kevinbadi/jev-voice) - `Open source` · `Free source build` · `BYOK`. Hands-free macOS voice assistant: local whisper.cpp plus one Jev call per command to select typed actions and arguments. [Project guide](community/projects/apps/jev-voice.md).
- [Live Jev](https://github.com/okinaaudio/live-jev) - `Open source` · `Free source build` · `BYOK`. Early macOS Ableton Live controller: hotkey bar + TypeSafe Jev picks typed mixer/device actions from short EN/JP phrases. [Project guide](community/projects/apps/live-jev.md).
- [macbrow](https://github.com/timpratim/macbrow) - `Open source` · `Free source build` · `BYOK`. Experimental macOS voice assistant using Jev to route commands to AppleScript tools and Chrome browser tasks. [Project guide](community/projects/apps/macbrow.md).
- [Notra](https://github.com/usenotra/notra) - `Open source` · `Commercial` · `Paid`. Uses Jev judgments within a broader application for tracking brand mentions and placement in AI answers. [Product](https://www.usenotra.com) · [Pricing](https://www.usenotra.com/pricing) · [Project guide](community/projects/apps/notra.md).
- [PageGrade](https://github.com/kitze/pagegrade) - `Open source` · `Free source build` · `BYOK`. Chrome extension that grades page sections for clarity, writing, and on-page SEO with TypeSafe Jev via Vercel AI Gateway. [Project guide](community/projects/apps/pagegrade.md).
- [Polymorph](https://github.com/moomooskycow/polymorph) - `Open source` · `Free source build` · `BYOK`. Chrome extension that collapses posts matching English rules judged by TypeSafe Jev via OpenRouter Decisions; replace with your media or restore. [Project guide](community/projects/apps/polymorph.md).
- [QuantDinger](https://github.com/OpenByteInc/QuantDinger) - `Open source` · `Free source build` · `BYOK`. Self-hosted AI trading OS with optional TypeSafe Jev pre-trade entry gates; hosted app also available. [Product](https://www.quantdinger.com) · [Try app](https://ai.quantdinger.com) · [Project guide](community/projects/apps/quantdinger.md).
- [RefGarden](https://github.com/AlbionaHoti/refgarden) - `Open source` · `Free source build` · `BYOK`. Local spatial reference gallery where TypeSafe Jev chooses search phrases and highlights Met/NASA/Cosmos/Archive items from text metadata. [Project guide](community/projects/apps/refgarden.md).
- [Smart Paste](https://github.com/nomanjack/smart-paste) - `Open source` · `Free source build` · `BYOK`. Experimental Chrome extension that uses Jev to select and verify exact source text for web form fields, with paste and undo. [Project guide](community/projects/apps/smart-paste.md).
- [Sponsor Skip](https://github.com/trungdq88/youtube-sponsor-detection) - `Source unverified` · `Pricing unverified` · `BYOK`. Locates YouTube sponsor reads with Jev-selected transcript boundaries and optional Deepgram audio analysis, with playback skipping. [Project guide](community/projects/apps/sponsor-skip.md).
- [Tab Bouncer](https://github.com/MANISH007700/tab-bouncer) - `Open source` · `Free source build` · `BYOK`. Chrome extension that rates open tabs for a typed task with TypeSafe Jev (keep noul + kind choice; batches of 120), then closes mismatches. Distinct from Jev for Chrome. [Project guide](community/projects/apps/tab-bouncer.md).
- [TipTour](https://github.com/milind-soni/tiptour-macos) - `Open source` · `Free source build` · `BYOK`. macOS menu bar app that uses Jev to select desktop click targets from typed requests, alongside a separate Gemini voice mode. [Project guide](community/projects/apps/tiptour.md).
- [Transcript Lens](https://github.com/sensahin/transcript-lens) - `Open source` · `Free source build` · `BYOK`. Next.js (Türkçe UI) YouTube transcript explorer: TypeSafe Jev classifies blocks for kind/value/signals without rewriting text. [Project guide](community/projects/apps/transcript-lens.md).
- [TypeSafe Fun AdBlocker](https://github.com/realZachi/typesafe-adblock) - `Open source` · `Free source build` · `BYOK`. Experimental Chrome extension that asks Jev whether heuristically selected DOM elements are ads, then removes or highlights matches. [Project guide](community/projects/apps/typesafe-adblock.md).
- [Unclutter](https://github.com/kitze/unclutter) - `Open source` · `Free source build` · `BYOK`. Classifies page clutter with Jev and saves reversible hiding rules for similar pages, with manual analysis by default. [Project guide](community/projects/apps/unclutter.md).
- [Vibe Check for X](https://github.com/RafalWilinski/vibecheck) - `Source unverified` · `Pricing unverified` · `BYOK`. Chrome extension that uses Jev to score draft X posts and display a verdict, with optional OpenAI media descriptions. [Project guide](community/projects/apps/vibecheck.md).
- [Watermelon](https://github.com/shashwatc12/watermelon) - `Open source` · `Free source build` · `BYOK`. Status-update honesty auditor: TypeSafe Jev judges language while code parses slip signals; live demo available. [Try app](https://watermelon.shashwatchavan.com) · [Project guide](community/projects/apps/watermelon.md).
- [Xtags](https://github.com/manifoldor/xtags) - `Open source` · `Free source build` · `BYOK`. Chrome extension/userscript that tags X posts with TypeSafe Jev intent and risk signals for personal local browsing. [Project guide](community/projects/apps/xtags.md).

### Developer projects and integrations

The [independent model research](community/projects/tools/README.md#independent-model-research) category explores related typed-decision interfaces with other models. Their local inference uses those models, and they do not provide official Jev weights.

- [Advocaat](https://github.com/pithings/advocaat) - TypeScript `ask` client that batches typed Jev choice, score, and yes/no questions about structured data, with optional Vercel AI Gateway support. [Project guide](community/projects/tools/advocaat.md).
- [Agent Router](https://github.com/nidhi-singh02/agent-router) - Quota-aware Herdr launcher that uses TypeSafe System One (Jev) to pick Cursor/Claude Code/Codex/OpenCode model and effort after local eligibility rules. [Project guide](community/projects/tools/agent-router.md).
- [agent-chaperone](https://github.com/agent-chaperone/agent-chaperone) - Calibrated firewall for agent tool calls: MCP proxy plus hooks adapter; TypeSafe Jev screening with shadow mode and a local judgment log. [Project guide](community/projects/tools/agent-chaperone.md).
- [agent-desktop](https://github.com/lahfir/agent-desktop) - Rust macOS accessibility CLI for desktop computer use; optional jev-desktop skill/scripts use TypeSafe Jev for target/command choice without putting the a11y tree in agent context (BYOK). [Project guide](community/projects/tools/agent-desktop.md).
- [feelings](https://github.com/BoundaryML/feelings) - BAML `.feels()` / `.how()` / `.matches<T>()` typed AI-if methods powered by TypeSafe Jev; upstream licensing unspecified. [Project guide](community/projects/tools/feelings.md).
- [jev-feels](https://github.com/Qew7/jev-feels) - Ruby gem for TypeSafe Jev as `feels?` / `decide` / `score` and Rails validations (distinct from BAML feelings and ruby_decision_model). [Project guide](community/projects/tools/jev-feels.md).
- [jev-foundation-models](https://github.com/peterfriese/jev-foundation-models) - Swift 6 bridge: TypeSafe Jev as an Apple Foundation Models `LanguageModel` for `@Generable` decisions (distinct from TypeSafe Swift client). [Project guide](community/projects/tools/jev-foundation-models.md).
- [ask-jev-skill](https://github.com/shantanugoel/ask-jev-skill) - Hermes skill that asks TypeSafe Jev for typed Choice/Score/Noul tiebreaks when paths remain plausible. [Project guide](community/projects/tools/ask-jev-skill.md).
- [askjev](https://github.com/pZacca/askjev) - Unofficial MCP server for TypeSafe Jev (local stdio or hosted Worker): agents get calibrated Noul/Choice/Score answers over held context. [Project guide](community/projects/tools/askjev.md).
- [beam-cli](https://github.com/whyashthakker/beam-cli) - AgentBeam local monitoring/safety CLI for coding agents, with optional TypeSafe Jev action judging (disabled by default; AGPL-3.0). [Project guide](community/projects/tools/beam-cli.md).
- [bitrate-advisor](https://github.com/affirmitv/bitrate-advisor) - Live-stream encoder settings from telemetry/history using TypeSafe Jev (OpenRouter) inside a deterministic safety envelope. [Project guide](community/projects/tools/bitrate-advisor.md).
- [Canny](https://github.com/qkal/Canny) - Claude Code/Codex warden: append-only ledger and deterministic done-gate; optional TypeSafe Jev advises but never alone blocks. [Project guide](community/projects/tools/canny.md).
- [chinese-workflow-decision-bench](https://github.com/Adkid-Zephyr/chinese-workflow-decision-bench) - Feishu-style Chinese message classification bench: 64 frozen scenarios, Choice/four-Noul workflows, published TypeSafe Jev vs Laya results. [Project guide](community/projects/tools/chinese-workflow-decision-bench.md).
- [claude-code-jev](https://github.com/RahulBalakavi/claude-code-jev) - Claude Code PreToolUse permission gate: TypeSafe Jev via OpenRouter Decisions classifies allow/block/ask, with fixture latency/cost benchmarks. [Project guide](community/projects/tools/claude-code-jev.md).
- [clear-head](https://github.com/VladyslavHontar/clear-head) - Claude Code Stop hook that judges answer claims against session tool evidence with TypeSafe Jev. [Project guide](community/projects/tools/clear-head.md).
- [Clay JEV People Ranker](https://github.com/promptgtm-shared/clay-jev-people-ranker) - Clay CLI people search plus TypeSafe Jev Choice/Noul qualification for semantic role fit (bundled operating-founder example). [Project guide](community/projects/tools/clay-jev-people-ranker.md).
- [codex-jev-router](https://github.com/tiandee/codex-jev-router) - Local Codex CLI bridge: TypeSafe Jev selects model and reasoning effort per turn via a loopback Responses proxy (fail-open without a key). [Project guide](community/projects/tools/codex-jev-router.md).
- [Cua jev-use](https://github.com/trycua/cua/tree/main/libs/cua-driver/examples/jev-use) - Composes a bounded Jev chooser with Cua Driver and an independently verified browser fixture. [Project guide](community/projects/tools/cua-jev-use.md).
- [daf-jev](https://github.com/docxology/daf-jev) - Composable Python toolkit for TypeSafe Jev: question builders, confidence gates, evaluator, calibration, CLI, and optional MCP server. [Project guide](community/projects/tools/daf-jev.md).
- [DataJev](https://github.com/zzz1YAO/DataJev) - Data-analysis agent loop where an LLM analyzes, Python executes, and TypeSafe Jev chooses CONTINUE/SWITCH/VERIFY/STOP (heuristic offline path). [Project guide](community/projects/tools/datajev.md).
- [dbt_jev](https://github.com/smithclay/dbt_jev) - Classify warehouse SQL values with TypeSafe Jev (or OpenRouter→Jev) from dbt macros on DuckDB and ClickHouse. [Project guide](community/projects/tools/dbt-jev.md).
- [decision-first](https://github.com/harrymunro/decision-first) - Agent skill that tries TypeSafe Jev on bounded-judgment steps first and documents every attempt in a reusable decision lab. [Project guide](community/projects/tools/decision-first.md).
- [doc-router](https://github.com/misbahsy/doc-router) - Routes PDF pages between local text extraction and OCR using optional Jev judgments, with a Rust CLI and Python bindings. [Project guide](community/projects/tools/doc-router.md).
- [DocJev](https://github.com/jerryjliu/docjev) - Document classification and splitting with TypeSafe Jev over LiteParse (optional LlamaParse) page text. [Project guide](community/projects/tools/docjev.md).
- [dsh-jev](https://github.com/noetion/dsh-jev) - DeepSeek Harness plugin registering `jev_ask` for TypeSafe Jev noul/choice/score (pin GitHub commit; npm name `dsh-jev` collides with another package). [Project guide](community/projects/tools/dsh-jev.md).
- [dsh-jev-prune](https://github.com/yangyu666/dsh-jev-prune) - DeepSeek Harness plugin: TypeSafe Jev keep/drop pruning plus deterministic receipt compaction (distinct from dsh-jev / dsh-jev-verify). [Project guide](community/projects/tools/dsh-jev-prune.md).
- [dsh-jev-verify](https://github.com/xienda/dsh-jev-verify) - DeepSeek Harness plugin with TypeSafe Jev `jev_decision` plus live `jev_verify` benchmark (no mock fallback; distinct from dsh-jev). [Project guide](community/projects/tools/dsh-jev-verify.md).
- [duckdb-jev](https://github.com/prasanthj/duckdb-jev) - Native DuckDB C++ extension for TypeSafe Jev semantic predicates, Choice classification, and Score rubrics in SQL. [Project guide](community/projects/tools/duckdb-jev.md).
- [demo-expanso-jev](https://github.com/expanso-io/demo-expanso-jev) - Expanso Edge × TypeSafe Jev demos: fingerprint routine logs locally, ask Jev only on the remainder, route with hold-on-failure and live boards. [Project guide](community/projects/tools/demo-expanso-jev.md).
- [Discern](https://github.com/doeixd/discern) - Effect Decision/DecisionModel patterns, policies, and procedures with an optional TypeSafe Jev provider (`@doeixd/discern`). [Project guide](community/projects/tools/discern.md).
- [Distill](https://github.com/samuelfaj/distill) - Lightweight coding-agent TUI with TypeSafe Jev (or OpenRouter decisions) for model/effort routing, utility tasks, and retention. [Project guide](community/projects/tools/distill.md).
- [discoprint](https://github.com/lirantal/discoprint) - Classify an artist discography for theme, mood, and lyrical complexity with TypeSafe Jev and an Ink terminal dashboard. [Project guide](community/projects/tools/discoprint.md).
- [ExcelPilot](https://github.com/vikramlingam/excelpilot) - Live Excel agent with Qwen planning and TypeSafe Jev for intent routing, tool gating, and claim checks. [Project guide](community/projects/tools/excelpilot.md).
- [Eutrya](https://github.com/hellozenstrategist-lab/eutrya) - CLI-first agent (public alpha) with TypeSafe Jev in the decision loop for attention, candidate rubrics, and research micro-steps; offline `eutrya demo`. [Project guide](community/projects/tools/eutrya.md).
- [fast-jev-compaction](https://github.com/tamaratran/fast-jev-compaction) - Selects tool-call/result pairs to keep, truncate, or remove while preserving retained conversation content verbatim. [Project guide](community/projects/tools/fast-jev-compaction.md).
- [Footwork](https://github.com/Tom-R-Main/Footwork) - Dual-process browser agent: TypeSafe Jev as System 1 in front of browser-use System 2, with a code-owned arbiter and evidence verification (`jevdual`). [Project guide](community/projects/tools/footwork.md).
- [Foreman](https://github.com/thruwire/foreman) - Supervises Codex workers with Jev assessments and deterministic steering, retry, and verification policy, with a synthetic demo. [Project guide](community/projects/tools/foreman.md).
- [Formanator](https://github.com/timrogers/formanator) - CLI/MCP for Forma benefit claims; optional TypeSafe Jev chooses benefit/category when you supply claim fields (receipt inference stays on LLM). [Project guide](community/projects/tools/formanator.md).
- [git-jev-stage](https://github.com/ibrahemid/git-jev-stage) - Classifies Git hunks against a one-sentence staging intent with TypeSafe Jev, then stages confirmed blocks. [Project guide](community/projects/tools/git-jev-stage.md).
- [Graphlin](https://github.com/royosherove/graphlin) - Live architecture and activity diagrams for Claude Code or Codex while they explore code, with optional TypeSafe Jev classification. [Project guide](community/projects/tools/graphlin.md).
- [Grok Bot Jev](https://github.com/Bodila51/grok-bot-jev) - Reference router and skill that use TypeSafe Jev to choose reuse/stop/cap/ask-human actions before expensive Grok Bot work. [Project guide](community/projects/tools/grok-bot-jev.md).
- [Hermes Jev Skills](https://github.com/kerpopule/hermes-jev-skills) - Agent skills and `jev` CLI using TypeSafe Jev for model routing, memory filtering, compaction, skill selection, triage, and computer/browser action choice on Hermes, Claude Code, and Codex. [Project guide](community/projects/tools/hermes-jev-skills.md).
- [hono-jev-router](https://github.com/yusukebe/hono-jev-router) - Experimental Hono router that matches HTTP requests to plain-English descriptions with TypeSafe Jev Noul judgments. [Project guide](community/projects/tools/hono-jev-router.md).
- [hunch](https://github.com/steven-shoemaker/hunch) - Python verbs (`classify`/`score`/`check`/`pick`/`rank`/`where`) over scalars, lists, and pandas columns backed by TypeSafe Jev (`hunch-jev`). [Project guide](community/projects/tools/hunch.md).
- [jevframe](https://github.com/ktaletsk/jevframe) - Semantic AI for pandas and Polars: TypeSafe Jev `.jev` accessor returns structured answers with full probabilities. [Project guide](community/projects/tools/jevframe.md).
- [invalidate](https://github.com/chopratejas/invalidate) - Semantic TTL for agent memory: TypeSafe Jev checks every stored fact against new evidence; code marks superseded memories without rewriting text. [Project guide](community/projects/tools/invalidate.md).
- [PerfectRecall](https://github.com/arslanr-com/perfectrecall) - Hermes/Python agent memory using TypeSafe or OpenRouter Jev evidence questions over local SQLite (Mnemosyne-compatible; no embeddings). [Project guide](community/projects/tools/perfectrecall.md).
- [prompt2jev](https://github.com/sumleo/prompt2jev) - Agent skill and CLI that convert natural language, an LLM prompt, or prompt-running code into a TypeSafe Jev decision (typed questions + runnable script). [Project guide](community/projects/tools/prompt2jev.md).
- [Prompt Rejector](https://github.com/revsmoke/promptrejectormcp) - MCP/HTTPS screening for prompts, skills, and tool descriptions with TypeSafe Jev plus deterministic checks. [Project guide](community/projects/tools/prompt-rejector.md).
- [pytest-jev](https://github.com/allebee/pytest-jev) - Pytest plugin for semantic assertions: TypeSafe Jev judges whether text holds or lacks plain-language claims. [Project guide](community/projects/tools/pytest-jev.md).
- [is-malicious](https://github.com/luantak/is-malicious) - Scans source/config/CI files with TypeSafe Jev for deceptive or data-stealing behavior and points to suspicious lines. [Project guide](community/projects/tools/is-malicious.md).
- [japanese-jev-lint](https://github.com/pankona/japanese-jev-lint) - Go CLI (`jjl`) that flags Japanese sentences with TypeSafe Jev Noul probabilities (plus local です/ます regex); no rewrite generation. [Project guide](community/projects/tools/japanese-jev-lint.md).
- [jev-sec-bench](https://github.com/Gaurav-Gosain/jev-sec-bench) - Blind TypeSafe Jev security benchmarks (prompt injection + vulnerable code) on public corpora, with a results TUI (built on jev-go). [Project guide](community/projects/tools/jev-sec-bench.md).
- [J++](https://github.com/Towow-ai/jpp) - Experimental language and Rust runtime for composing semantic Jev questions with exact methods as values; offline fixtures included. [Project guide](community/projects/tools/jpp.md).
- [JCR](https://github.com/NiazMorshed2007/jcr) - Jev Capability Resolver: TypeSafe Jev searches a nested capability tree and returns deterministic command documentation for agents (MCP + harnesses). [Project guide](community/projects/tools/jcr.md).
- [jear](https://github.com/iJ03l/jear) - Rust Jev-routed client for NEAR AI Cloud inference and IronClaw agents using budget/quality/sensitivity decisions. [Project guide](community/projects/tools/jear.md).
- [jev-java](https://github.com/gudcks0305/jev-java) - Unofficial Java 17+ SDK for TypeSafe Jev with OpenRouter/Vercel adapters and optional Spring Boot starter (`jev-typesafe` 0.1.1). [Project guide](community/projects/tools/jev-java.md).
- [jevonian](https://github.com/xinyao27/jevonian) - Local OpenAI/Anthropic/Responses proxy for coding agents where one Jev call answers both the model route and the thinking level for `jevonian/auto`, after code has filtered candidates by protocol, context window, effort floor, and spent quota windows; a pinned model or explicit `jevonian/<route>` skips Jev entirely, and costs in the ledger are estimates. [Project guide](community/projects/tools/jevonian.md).
- [jev4k](https://github.com/pambrose/jev4k) - Kotlin DSL/client for TypeSafe Jev Noul/Choice/Score (Maven Central `com.pambrose:jev4k`; distinct from jev-java / jev-android). [Project guide](community/projects/tools/jev4k.md).
- [jevgo](https://github.com/devbackend/jevgo) - Unofficial Go client for TypeSafe System One: typed Noul/Choice/Score in one call (stdlib HTTP). [Project guide](community/projects/tools/jevgo.md).
- [jev-align](https://github.com/sutro-sh/jev-align) - CLI to build calibrated AI Functions from human labels using TypeSafe Jev evaluation and GEPA optimization. [Project guide](community/projects/tools/jev-align.md).
- [Jev Atlas](https://github.com/v60samurai/jev-atlas) - Claude Code/Codex skill that maps where a codebase should (and should not) use TypeSafe Jev, then validates/implements survivors. [Project guide](community/projects/tools/jev-atlas.md).
- [jev-calibrate](https://github.com/smkrv/jev-calibrate) - Calibrate TypeSafe Jev questions against labelled examples and get per-question gate/ranker/unusable verdicts. [Project guide](community/projects/tools/jev-calibrate.md).
- [Jev Checkpoint](https://github.com/ashishakkumar/Jev-Checkpoint) - Local MCP server that confidence-gates a bounded next-step Choice with TypeSafe Jev and returns an advisory route only. [Project guide](community/projects/tools/jev-checkpoint.md).
- [jev-ci-selector](https://github.com/guilhem/jev-ci-selector) - GitHub Action that asks TypeSafe Jev which described CI tasks apply to the current PR diff and exports boolean job outputs. [Project guide](community/projects/tools/jev-ci-selector.md).
- [jev-debtgate](https://github.com/smlayero/jev-debtgate) - Technical-debt gate for coding agents and CI: local metrics plus TypeSafe Jev typed questions and confidence policy (BYOK). [Project guide](community/projects/tools/jev-debtgate.md).
- [jev-android](https://github.com/dougsong/jev-android) - Kotlin Android UI-agent SDK: TypeSafe Jev or DeepSeek selects accessibility actions; local Maven sample (not on Maven Central). [Project guide](community/projects/tools/jev-android.md).
- [jevdevice](https://github.com/Xopher00/jevdevice) - MCP harness for Android (adb) or local shell: TypeSafe Jev (or local Laya) picks one runtime-discovered target per goal; code gates and executes. [Project guide](community/projects/tools/jevdevice.md).
- [blink](https://github.com/ellipsis-dev/blink) - Bun CLI that searches a codebase with TypeSafe Jev walkers (Choice over directory entries via `@typesafe-ai/sdk`); upstream licensing unspecified. [Project guide](community/projects/tools/blink.md).
- [jegrep](https://github.com/can1357/jegrep) - Semantic grep CLI: describe code intent and get Jev-ranked matches via TypeSafe or OpenRouter, without an embedding index. [Project guide](community/projects/tools/jegrep.md).
- [jev-corrective-rag](https://github.com/sudeshkar/jev-corrective-rag) - Corrective RAG demo: TypeSafe Jev typed gates for triage/grading/verify; generative LLM only writes answers. [Project guide](community/projects/tools/jev-corrective-rag.md).
- [jev-semgrep](https://github.com/uehaj/jev-semgrep) - Meaning-grep CLI: TypeSafe Jev scores each line against a proposition (AND/OR/NOT); multilingual; npm `@uehaj/semgrep` (not Semgrep Inc). [Project guide](community/projects/tools/jev-semgrep.md).
- [Jev Second Brain](https://github.com/fellowship-dev/jev-second-brain) - Local-first Markdown vault CLI: FTS index, source-linked related-note suggestions, optional TypeSafe Jev judgments via Vercel AI Gateway. [Project guide](community/projects/tools/jev-second-brain.md).
- [AnchorLint](https://github.com/prantikmedhi/anchorlint) - Audits internal links in built HTML sites with deterministic checks plus optional TypeSafe Jev promise/relevance judgments. [Project guide](community/projects/tools/anchorlint.md).
- [jev-seo](https://github.com/AkashPriyadarshii/jev-seo) - Agent-oriented SEO/GEO CLI and MCP with local DuckDuckGo helpers and optional TypeSafe Jev scoring. [Project guide](community/projects/tools/jev-seo.md).
- [Jev Browser (tontoko)](https://github.com/tontoko/jev-browser) - Integrates Jev field selection and source-backed extraction with a Playwright SDK, CLI, MCP server, and explicit assertions. [Project guide](community/projects/tools/jev-browser-tontoko.md).
- [Jev Browser (Ying-Kai-Liao)](https://github.com/Ying-Kai-Liao/jev-browser) - Turns caller-defined browser goals into Jev-selected Playwright actions with a library, CLI, and MCP server. [Project guide](community/projects/tools/jev-browser-ying-kai-liao.md).
- [Jev Browser Skill](https://github.com/zurfyx/jev-browser-skill) - Claude Code/Codex skill where TypeSafe Jev chooses browser operations and targets from a code-built element table (reference implementation; explainer site included). [Project guide](community/projects/tools/jev-browser-skill.md).
- [Jev Classification for n8n](https://github.com/khmuhtadin/n8n-nodes-jev-classification) - Adds typed classification, scoring, yes/no checks, and batched questions to self-hosted n8n, with configurable review routing. [Project guide](community/projects/tools/jev-classification-n8n.md).
- [Jev for Home Assistant](https://github.com/AboveColin/HA-Jev) - Turns judgments over selected Home Assistant state into sensors and automation responses, with usage accounting. [Project guide](community/projects/tools/ha-jev.md).
- [Jev Logs](https://github.com/reachjalil/jevlogs) - Scores OpenTelemetry logs for a separate analysis branch, with mock mode and conservative error handling. [Project guide](community/projects/tools/jevlogs.md).
- [jevmetrics](https://github.com/ishantanu/jevmetrics) - Experimental OpenTelemetry Collector metrics processor: TypeSafe Jev assesses instrument metadata for retention; deterministic keep/reduce policy with caching (alpha). [Project guide](community/projects/tools/jevmetrics.md).
- [jevmory](https://github.com/romiluz13/jevmory) - Local coding-agent memory with verbatim quotes graded by TypeSafe Jev confidence and receipt-backed MEMORY.md audits. [Project guide](community/projects/tools/jevmory.md).
- [Jev-Mem](https://github.com/libingzheren/Jev-Mem) - System-One–controlled agentic memory: TypeSafe Jev steers admission, multi-relational linking, and adaptive retrieval before a text model answers. [Project guide](community/projects/tools/jev-mem.md).
- [Jev Model Router](https://github.com/davila7/claude-code-templates/tree/main/cli-tool/components/mods/productivity/jev-model-router) - Early-access Claude Code mod that uses Jev task assessments and configurable confidence thresholds to route subagent models and main-conversation reasoning effort. [Project guide](community/projects/tools/jev-model-router.md).
- [Jev Review](https://github.com/NiazMorshed2007/jev-review) - MCP server for experimental software-quality rubric scores and comparisons; requires `JEV_API_KEY` and sends supplied code context to TypeSafe. [Project guide](community/projects/tools/jev-review.md).
- [Jev Review (Dev Agrawal)](https://github.com/devagrawal09/jev-review) - Screens JavaScript and TypeScript changes or source files with staged Jev judgments and displays evidence-linked findings in a local dashboard. [Project guide](community/projects/tools/jev-review-devagrawal.md).
- [Jev Review Action](https://github.com/fatwang2/jev-review-action) - Configurable GitHub Action: catalog or PR classification with TypeSafe Jev only (no text-gen), one template comment. [Project guide](community/projects/tools/jev-review-action.md).
- [Jev Sift](https://github.com/kbhuw/jev-sift) - Screens files, public webpages, and tool descriptions with Jev before an agent reads selected content; requires a TypeSafe key, and upstream licensing is unspecified. [Project guide](community/projects/tools/jev-sift.md).
- [Jev Score](https://github.com/a-Fig/jev-score) - Local CLI/web scoreboard that grades document revisions against your criteria with TypeSafe Jev via OpenRouter Decisions. [Project guide](community/projects/tools/jev-score.md).
- [JevScope](https://github.com/jeiel85/jevscope) - Local-first visual workbench and JSONL regression testbench for TypeSafe Jev projects. [Project guide](community/projects/tools/jevscope.md).
- [JevTape](https://github.com/Hugo-DDT/JevTape) - Record/replay/inspect TypeSafe Jev decisions as JSON cassettes with Decision Contract fingerprints for offline CI. [Project guide](community/projects/tools/jevtape.md).
- [Jev Trader](https://github.com/jarrodwatts/jev-trader) - Studies Jev market-direction choices, simulated fills, and on-chain order execution through a Bun trading experiment. [Project guide](community/projects/tools/jev-trader.md).
- [Jev Ultrafast](https://github.com/browser-use/jev-ultrafast) - Selects browser operations and observed targets with Jev, using a separate text model for text entry. [Project guide](community/projects/tools/jev-ultrafast.md).
- [jev-ra](https://github.com/brnyxx/jev-ra) - MCP/CLI browser-use layer for coding agents: TypeSafe Jev picks each Chrome operation and target in one round trip (OpenRouter or TypeSafe key). [Project guide](community/projects/tools/jev-ra.md).
- [JMP](https://github.com/morcoan/JMP) - Local coding workspace where TypeSafe Jev selects the next tool action and DeepSeek/Codex/Bonsai supply arguments for OpenHands/MCP execution. [Project guide](community/projects/tools/jmp.md).
- [Jev Lab](https://github.com/jammaru/jev-lab) - Local Hundred NPC-town and Jev Shogi labs where TypeSafe Jev chooses the next legal action (Rules mode without a key). [Project guide](community/projects/tools/jev-lab.md).
- [Jev Voice Browser](https://github.com/moritzkremb/jev-voice-browser) - Experiments with typed Jev decisions over partial voice transcripts and page elements to control Playwright, with a local decision inspector. [Project guide](community/projects/tools/jev-voice-browser.md).
- [Jev-cu](https://github.com/Sac-Y/Jev-cu) - Experimental Codex skill and JavaScript runtime for selecting macOS Accessibility targets with Jev, with action previews and optional result verification; execution-policy limitations require review. [Project guide](community/projects/tools/jev-cu.md).
- [jev-macos-loop](https://github.com/jcpsimmons/jev-macos-loop) - Native Apple silicon macOS computer-use agent: local OmniParser/Vision/Accessibility perception with text-only Jev action choice (BYOK Vercel/OpenRouter/TypesafeAI). [Project guide](community/projects/tools/jev-macos-loop.md).
- [jev-codex-router](https://github.com/0xNatoshi/jev-codex-router) - Routes each Codex turn through Jev tier and thinking-depth selection via a local Codex Router generic provider, with fail-open fallbacks and an optional Codex-dry tandem. [Project guide](community/projects/tools/jev-codex-router.md).
- [jev-codex-token-saver](https://github.com/jcressler/jev-codex-token-saver) - Codex plugin/MCP that scores bounded local evidence with TypeSafe Jev and returns selected exact excerpts (local fallback when Jev is unavailable). [Project guide](community/projects/tools/jev-codex-token-saver.md).
- [jev-compact](https://github.com/fatelei/jev-compact) - Codex CLI plugin: TypeSafe Jev scores tool calls before compaction and restores critical outputs verbatim afterward (distinct from fast-jev-compaction for Claude Code). [Project guide](community/projects/tools/jev-compact.md).
- [jev-gateway](https://github.com/vinilana/jev-gateway) - Local LLM gateway that asks TypeSafe Jev which tool to call for Codex, Claude Code, OpenCode, or Gemini while other traffic uses your usual LLM. [Project guide](community/projects/tools/jev-gateway.md).
- [jev-gates](https://github.com/carlchou0dailyfresh/jev-gates) - Composable three-valued semantic logic circuits from TypeSafe Jev judgments and exact rules, with mock/offline demos (distinct from typesafe-agent-gates). [Project guide](community/projects/tools/jev-gates.md).
- [jev-harness](https://github.com/AntonioCoppe/jev-harness) - TypeScript decision harness: confidence-gated TypeSafe Jev policies, shadow mode, recipes, and `jev-eval` (distinct from super-jev / jev-layer). [Project guide](community/projects/tools/jev-harness.md).
- [jev-guard](https://github.com/leepokai/jev-guard) - Coding-agent security hooks: TypeSafe Jev risk-scores tool calls with session context (deny/ask/allow), flags prompt injection, and scans skills across Claude Code, Codex, Cursor, and more. [Project guide](community/projects/tools/jev-guard.md).
- [jev-drone](https://github.com/RomanSlack/jev-drone) - Explores Jev tactical judgments in a MuJoCo quadrotor simulation, with local flight control and a separate experimental tunnel policy. [Project guide](community/projects/tools/jev-drone.md).
- [jev-evolve](https://github.com/novaleolin/jev-evolve) - Self-improving agents whose every decision is a typed TypeSafe Jev question, with reports separating real gains from selection noise. [Project guide](community/projects/tools/jev-evolve.md).
- [jev-eyes](https://github.com/LeddoEngano/jev-eyes) - Local OCR/layout `see()` (and optional `ask()`) so TypeSafe Jev decides over inspectable image-derived text state. [Project guide](community/projects/tools/jev-eyes.md).
- [jev-in-codex](https://github.com/teempai/jev-in-codex) - Codex MCP tools for TypeSafe Jev-ranked capability selection, workspace search, and output triage (experimental MVP). [Project guide](community/projects/tools/jev-in-codex.md).
- [jev-issue-radar](https://github.com/Patrick-SCH03/jev-issue-radar) - Local read-only dashboard: TypeSafe Jev (OpenRouter) classifies GitHub issue duplicates with evidence passages for maintainer review. [Project guide](community/projects/tools/jev-issue-radar.md).
- [jev-layer](https://github.com/typakon4/jev-layer) - Portable System-1 decision layer for agent harnesses: host-owned capability routing, receipts/replay, optional supervision, demo/OpenRouter/TypeSafe providers. [Project guide](community/projects/tools/jev-layer.md).
- [jev-libero](https://github.com/Dimweaker/jev-libero) - Fine-grained LIBERO robot control study loop: TypeSafe Jev layered decisions with local physics previews and inspectable records. [Project guide](community/projects/tools/jev-libero.md).
- [quackd](https://github.com/rokbenko/quackd) - Multi-robot CLI with LLM pilots and an optional TypeSafe Jev discrete stepper for closed-set skill choices. [Project guide](community/projects/tools/quackd.md).
- [Responsible AI Harness](https://github.com/syabdulr/responsible-ai-harness) - Model-agnostic safety assessment harness: hard rules plus optional TypeSafe Jev judge for injection, leakage, unsafe tools, and policy bypass; checksummed evidence + report UI. [Project guide](community/projects/tools/responsible-ai-harness.md).
- [jev-mcp](https://github.com/jkudish/jev-mcp) - MCP server with ten purpose-built TypeSafe Jev judgment tools (verify, screen, find, classify, review, gate, and more). [Project guide](community/projects/tools/jev-mcp.md).
- [Jev MCP (Freepik)](https://github.com/freepik-company/jev-mcp) - Go MCP server for typed decide/classify/verify/rerank with Jev via OpenRouter or TypeSafe (binary/container releases). [Project guide](community/projects/tools/freepik-jev-mcp.md).
- [tokengate (jev-model-tokengate)](https://github.com/Thanh-Mathieu95/jev-model-tokengate) - Streaming OpenAI-compatible proxy that buffers tokens and runs TypeSafe Jev safety criteria before release, aiming for zero UI leakage vs post-hoc redaction. [Project guide](community/projects/tools/jev-model-tokengate.md).
- [jev-oas-sentinel](https://github.com/ShuhanSun/jev-oas-sentinel) - Compares OpenAPI documents with deterministic structural checks plus TypeSafe Jev semantic questions; policy code owns pass/review/block. [Project guide](community/projects/tools/jev-oas-sentinel.md).
- [jev-packs](https://github.com/dtduc-git/jev-packs) - Evidence-gated Jev question-pack registry with golden cases and a reproducible offline multi-backend scoreboard. [Project guide](community/projects/tools/jev-packs.md).
- [jev-pii-checker](https://github.com/coo-quack/jev-pii-checker) - CLI that finds PII spans and sensitivity with TypeSafe Jev plus regex/segmentation layers (scanned text leaves the host). [Project guide](community/projects/tools/jev-pii-checker.md).
- [jev-pr-judge](https://github.com/juanegido/jev-pr-judge) - Typed pull-request verdicts via one parallel TypeSafe Jev call, code-owned policy profiles, Next.js UI, and a sticky-comment GitHub Action. [Project guide](community/projects/tools/jev-pr-judge.md).
- [jev-preflight](https://github.com/muse0509/jev-preflight) - Claude Code Stop-hook risk check: TypeSafe Jev scores eight axes over a redacted turn diff, with optional one-shot reinspection. [Project guide](community/projects/tools/jev-preflight.md).
- [jev-prompt-sentry](https://github.com/ca7ai/jev-prompt-sentry) - Anthropic Messages reverse proxy that screens jailbreaks/injections with one batched TypeSafe Jev call (PolyForm Noncommercial). [Project guide](community/projects/tools/jev-prompt-sentry.md).
- [jev-pruner](https://github.com/tamaratran/jev-pruner) - Prunes eligible Bash stdout with Jev before it reaches Claude Code or an opt-in Codex wrapper, while archiving the original output locally. [Project guide](community/projects/tools/jev-pruner.md).
- [jev-reranker](https://github.com/shinpr/jev-reranker) - Pipe JSON search candidates through TypeSafe Jev to rerank, filter evidence, or compress passages for LLM context. [Project guide](community/projects/tools/jev-reranker.md).
- [jev-reranker (hotchpotch)](https://github.com/hotchpotch/jev-reranker) - Python RAG relevance filter/reranker with TypeSafe Jev (listwise/pointwise/pairwise); distinct from the shinpr Rust CLI. [Project guide](community/projects/tools/hotchpotch-jev-reranker.md).
- [jev-router](https://github.com/gargpratyush/jev-router) - Routes fresh Claude Code and Codex turns through Jev model selection and deterministic fallback policy, with locally inspectable routing exchanges. [Project guide](community/projects/tools/jev-router.md).
- [JevRouter](https://github.com/BillionsBobby/JevRouter) - Capability router: TypeSafe Jev (or OpenRouter Decisions) picks among models/subagents/skills/MCP/CLIs while code enforces permissions, risk, confirmation, and receipts. [Project guide](community/projects/tools/jevrouter.md).
- [jev-rules](https://github.com/EliaAlberti/jev-rules) - Selects Claude Code project rules and map documents with Jev judgments over prompts and file paths, with session caching and fallback context. [Project guide](community/projects/tools/jev-rules.md).
- [jev-shell-history](https://github.com/mrnugget/jev-shell-history) - Ranks recent zsh commands with Jev for inline suggestions; sends selected history to TypeSafe and requires a user-supplied API key. [Project guide](community/projects/tools/jev-shell-history.md).
- [jev-shield](https://github.com/caiovicentino/jev-shield) - Semantic MCP firewall and skill: TypeSafe Jev (Vercel AI Gateway) screens tool calls, results, and descriptions. [Project guide](community/projects/tools/jev-shield.md).
- [JevShield](https://github.com/lgy1027/jevshield) - Python/LangChain tool-call security gate using TypeSafe Jev Choice/Noul/Score with local heuristic fallback (distinct from Node jev-shield). [Project guide](community/projects/tools/jevshield.md).
- [jev-skill-gate](https://github.com/ShivamPansuriya/jev-skill-gate) - Gates Claude Code skill manifests with TypeSafe Jev relevance scores and `skillOverrides` so irrelevant skills stay out of context. [Project guide](community/projects/tools/jev-skill-gate.md).
- [jev-skill-scout](https://github.com/karanb192/jev-skill-scout) - Finds Claude Code turns where a skill should have loaded and did not (TypeSafe Jev audit CLI + live suggest mod). [Project guide](community/projects/tools/jev-skill-scout.md).
- [jev-studio](https://github.com/utk2103/jev-studio) - Python CLI (`jev`) plus MCP server kit for TypeSafe Jev verify/screen/classify/extract flows and cookbook tools (Alpha 0.1.0). [Project guide](community/projects/tools/jev-studio.md).
- [Jev Symfony Bundle](https://github.com/vbcherepanov/jev-symfony-bundle) - Unofficial Symfony bundle for TypeSafe Jev: typed client, validator constraints, Messenger, Workflow guards, and profiler. [Project guide](community/projects/tools/jev-symfony-bundle.md).
- [jev-table](https://github.com/dtduc-git/jev-table) - Local-first CLI that adds TypeSafe Jev AI columns to CSV/JSONL with confidence, review queue, resume, and dry-run cost preview. [Project guide](community/projects/tools/jev-table.md).
- [jev-test-filter](https://github.com/mizchi/jev-test-filter) - Scores each test against a git diff with TypeSafe Jev and emits filter args for vitest, Jest, node:test, Playwright, cargo, and go test. [Project guide](community/projects/tools/jev-test-filter.md).
- [jev-toolkit](https://github.com/jbt95/jev-toolkit) - MCP-first TypeSafe/Jev toolkit: `jev mcp` plus CLI triage/audit/label/route and optional Prometheus impact metrics. [Project guide](community/projects/tools/jev-toolkit.md).
- [jevtriage](https://github.com/sathariels/jevtriage) - GitHub Action + CLI: triage PRs with TypeSafe Jev (`ready` / `needs_review` / `risky`) and confidence-gated exits. [Project guide](community/projects/tools/jevtriage.md).
- [jev-use (shitianfang)](https://github.com/shitianfang/jev-use) - Hands the Claude Code, Codex and pi steps that need no text output to Jev, returning anything it should not decide to the LLM under a typed escalation contract. [Project guide](community/projects/tools/jev-use.md).
- [jevc](https://github.com/doronp/jevc) - Compiles natural-language agent rules and JSON Schemas into TypeSafe Jev programs (typed questions + code reducers) you can test offline. [Project guide](community/projects/tools/jevc.md).
- [jevkit](https://github.com/ariel-frischer/jevkit) - Rust CLI for TypeSafe Jev typed decisions plus offline `jev lint` before paid calls (distinct from Hermes's internal Python `jevkit` client). [Project guide](community/projects/tools/jevkit.md).
- [jevcache](https://github.com/kushals256/jevcache) - OpenAI-compatible local cache proxy: TypeSafe Jev (OpenRouter Decisions) admits same-intent paraphrases so expensive chat completions can be skipped (fail-open on Jev errors). [Project guide](community/projects/tools/jevcache.md).
- [jeval](https://github.com/rlaope/jeval) - Measures probabilistic classifier calibration (incl. Jev confidence) and cost-optimal human hand-off thresholds; offline demo included. [Project guide](community/projects/tools/jeval.md).
- [jevals](https://github.com/dayhaysoos/jevals) - Local TypeSafe Jev evaluation workbench: author Noul/Choice/Score cases with expected answers, run them, and compare saved results. [Project guide](community/projects/tools/jevals.md).
- [jevbus](https://github.com/zkjoie/jevbus) - Rust streaming event bus: TypeSafe Jev (or any Judge) decides route/subscribe/deliver dispositions with policy thresholds. [Project guide](community/projects/tools/jevbus.md).
- [jev-agent-browser](https://github.com/mhingston/jev-agent-browser) - Confidence-gated browser actions for `agent-browser` with TypeSafe Jev (or Gateway/Cloudflare/custom providers). [Project guide](community/projects/tools/jev-agent-browser.md).
- [jev-agent-failure-benchmark](https://github.com/TokenTrim/jev-agent-failure-benchmark) - Benchmarks TypeSafe Jev on Who&When Pro agent-failure attribution (who/when/what) against published LLM baselines. [Project guide](community/projects/tools/jev-agent-failure-benchmark.md).
- [jev-agent-kit](https://github.com/walidboulanouar/jev-agent-kit) - Zero-dependency CLI + MCP tools (route/triage/guard/grep/rank/compact/judge/…) on TypeSafe Jev (`@walidboulanouar/jevkit`; distinct from Rust jevkit). [Project guide](community/projects/tools/jev-agent-kit.md).
- [Jevaluate](https://github.com/ElshinQ/jevaluate) - Confidence-gated web-app walkthroughs with TypeSafe Jev (optional DeepSeek vision) plus eval/judge scripts and an agent skill. [Project guide](community/projects/tools/jevaluate.md).
- [jevtok](https://github.com/LabGuy94/jevtok) - Exact token counting and request-cost prediction for TypeSafe Jev (tiktoken-style encoder reconstructed from API usage). [Project guide](community/projects/tools/jevtok.md).
- [jevlens](https://github.com/k4its1t/jevlens) - Evaluate, calibrate, replay, and monitor TypeSafe Jev decisions from labeled datasets with threshold suggestions and optional Streamlit/CI. [Project guide](community/projects/tools/jevlens.md).
- [jevernetes](https://github.com/sunil-sadasivan/jevernetes) - Live Kubernetes log analysis (CLI/dashboard) with optional TypeSafe Jev judgments or offline keyword rules and agent handoff prompts. [Project guide](community/projects/tools/jevernetes.md).
- [Jevlike](https://github.com/vinnylarouge/jevlike) - Trains a small option-attention scorer with synthetic data and optional frozen encoders; independent of official Jev. [Project guide](community/projects/tools/jevlike.md).
- [jev-lint](https://github.com/mizchi/jev-lint) - Ast-grep + TypeSafe Jev natural-language semantic linter (name/body drift, stale comments, weak tests); distinct from huntedman/JevLint. [Project guide](community/projects/tools/jev-lint.md).
- [jev-linter-action](https://github.com/sable-inc/jev-linter-action) - GitHub Action: configurable TypeSafe Jev yes/no suites over repo files with probability thresholds (distinct from jev-ci-selector and jev-lint CLIs). [Project guide](community/projects/tools/jev-linter-action.md).
- [JevLint](https://github.com/huntedman/JevLint) - Semantic lint CLI: plain-English conventions scored as file-level TypeSafe Jev Noul judgments (`@jevlint/cli`). [Project guide](community/projects/tools/jevlint.md).
- [jevmod](https://github.com/ohernandezdev/jevmod) - Moderation CLI/SDK/API/MCP and optional chat bots with per-category TypeSafe Jev probabilities and thresholds you own. [Project guide](community/projects/tools/jevmod.md).
- [JevOnly](https://github.com/buluoray/JevOnly) - Pure-Jev browser agent: code enumerates page/goal options, Jev only picks, with verify/undo and an irreversible-action gate. [Project guide](community/projects/tools/jevonly.md).
- [jevnav](https://github.com/dtduc-git/jevnav) - Browser automation with TypeSafe Jev element choice, JSONL decision traces, risk gates, and offline CI replay (distinct from Ultrafast). [Project guide](community/projects/tools/jevnav.md).
- [JevPilot](https://github.com/standardagents/jevpilot) - Demonstrates Jev maneuver selection in a browser driving simulation with local collision checks; application licensing is unspecified. [Project guide](community/projects/tools/jevpilot.md).
- [JevPokerBench](https://github.com/Prophetlab/JevPokerBench) - Texas Hold'em benchmark/playground with official TypeSafe Jev, cash/SNG boards, and BYOK agents. [Project guide](community/projects/tools/jev-poker-bench.md).
- [JevSQL](https://github.com/EugeneBoondock/jevsql) - Adds TypeSafe Jev natural-language predicates and decision tables to SQLite SQL with batching, caching, and review queues; distinct from pg-jev. [Project guide](community/projects/tools/jevsql.md).
- [jgrep](https://github.com/keltokhy/jgrep) - Filters text, structured records, functions, and diff hunks against plain-English descriptions using Jev Noul judgments. [Project guide](community/projects/tools/jgrep.md).
- [jlink](https://github.com/keltokhy/jlink) - Links records under a plain-English match rule using Jev Noul pair judgments, with local candidate blocking and match resolution. [Project guide](community/projects/tools/jlink.md).
- [jselect](https://github.com/keltokhy/jselect) - Selects source-linked evidence within a token budget using Jev Noul relevance judgments and local diversity-aware selection. [Project guide](community/projects/tools/jselect.md).
- [jsort](https://github.com/keltokhy/jsort) - Semantic sort CLI: order lines along a plain-English dimension via pairwise TypeSafe Jev comparisons and a Bradley–Terry scale. [Project guide](community/projects/tools/jsort.md).
- [Laravel AI](https://github.com/laravel/ai) - Provides typed classification and a TypeSafe provider for Laravel applications, with fake responses for application testing. [Project guide](community/projects/tools/laravel-ai.md).
- [llama-index-jev](https://github.com/WiktorB2004/llama-index-jev) - Python integrations for LlamaIndex passage reranking and query-engine selection, with configurable error and selection behavior. [Project guide](community/projects/tools/llama-index-jev.md).
- [Mobile Jev](https://github.com/droidrun/mobile-jev) - Selects Android actions and exact input text through Mobilerun, with a local studio and task-specific verification demo. [Project guide](community/projects/tools/mobile-jev.md).
- [mysql-ailike](https://github.com/maayanlevy/mysql-ailike) - MySQL native `AILIKE` / `ailike` UDFs for natural-language row filters and joins via TypeSafe Jev (Linux plugin; GPL-2.0). [Project guide](community/projects/tools/mysql-ailike.md).
- [NanoJev](https://github.com/TianyuCodings/NanoJev) - Studies independent Qwen-based typed decision heads, local serving, and game controllers with recorded comparisons. [Project guide](community/projects/tools/nanojev.md).
- [n8n-nodes-typesafe](https://github.com/Biztactix/n8n-nodes-typesafe) - n8n community node for TypeSafe System One noul/choice/score questions over workflow text or JSON. [Project guide](community/projects/tools/n8n-nodes-typesafe.md).
- [nf-jev](https://github.com/nextflow-io/nf-jev) - Nextflow plugin exposing TypeSafe Jev noul/choice/score as pipeline functions (beta). [Project guide](community/projects/tools/nf-jev.md).
- [neo4jev](https://github.com/jexp/neo4jev) - Explores Neo4j paths using next-hop choices and goal judgments, with notebooks and a Streamlit interface. [Project guide](community/projects/tools/neo4jev.md).
- [NeuroLink](https://github.com/juspay/neurolink) - TypeScript multi-provider AI SDK with a `decide`/`tryDecide` inference type powered by TypeSafe Jev for routing and gating. [Project guide](community/projects/tools/neurolink.md).
- [Note Filer](https://github.com/someka-vrc/obsidian-note-filer) - Obsidian plugin that classifies notes with TypeSafe Jev and moves them into Thema/IAB taxonomy folders after review. [Project guide](community/projects/tools/obsidian-note-filer.md).
- [Open Alternative to Jev](https://github.com/ikermoel/open-alternative-jev) - Studies typed decisions from open models using packed or separate inference and optional calibration; independent of TypeSafe Jev. [Project guide](community/projects/tools/open-alternative-jev.md).
- [open-jev](https://github.com/nico-martin/open-jev) - Runs independent Kev and DeBERTa typed-decision models locally through Transformers.js, with browser WebGPU/WASM support; does not use official Jev weights. [Project guide](community/projects/tools/open-jev.md).
- [openclaw-typesafe-ai](https://github.com/Olli0103/openclaw-typesafe-ai) - OpenClaw plugin registering optional `typesafe_decide` for explicit TypeSafe Jev decisions (SecretRef credentials; no hooks). [Project guide](community/projects/tools/openclaw-typesafe-ai.md).
- [omp-jev-compaction](https://github.com/jerryfane/omp-jev-compaction) - omp plugin: verbatim TypeSafe/OpenRouter Jev-scored tool-context reduction with sticky cache-friendly rewrites (distinct from fast-jev-compaction / jev-compact). [Project guide](community/projects/tools/omp-jev-compaction.md).
- [openjev-sglang](https://github.com/ekzhang/openjev-sglang) - Implements a Jev-shaped HTTP decision API using Qwen and SGLang; independent model behavior and unspecified code licensing. [Project guide](community/projects/tools/openjev-sglang.md).
- [Metis](https://github.com/Ayush0054/metis) - GitHub Action and Python CLI that triage new issues with TypeSafe Jev category labels and missing-detail follow-ups. [Project guide](community/projects/tools/metis.md).
- [Moongate](https://github.com/brickfrog/moongate) - GitHub Action that evaluates committed diffs against JSON semantic rules with TypeSafe Jev and reports annotations from your thresholds. [Project guide](community/projects/tools/moongate.md).
- [patdown](https://github.com/tyler-dot-earth/patdown) - Fuzzy markdown-rule linter CLI with a swappable judge; default backend posts typed questions to TypeSafe Jev. [Project guide](community/projects/tools/patdown.md).
- [pi-follow-through](https://github.com/Nabsku/pi-follow-through) - Pi extension that asks TypeSafe Jev whether useful work remains after a run and nudges only with verifiable unfinished evidence. [Project guide](community/projects/tools/pi-follow-through.md).
- [pi-heed](https://github.com/Nyarlathoteppppp/pi-heed) - Pi extension that keeps conversational user constraints as structured policy and checks side-effecting tool calls with TypeSafe Jev help. [Project guide](community/projects/tools/pi-heed.md).
- [pg-jev](https://github.com/realZachi/pg-jev) - Adds semantic predicates, probabilities, choices, and scores to PostgreSQL through a PL/Python extension. [Project guide](community/projects/tools/pg-jev.md).
- [pg_typesafe](https://github.com/giuliosmall/pg_typesafe) - Pre-alpha PostgreSQL C extension for TypeSafe Jev Choice/Noul/Score with batched multi-text helpers; distinct from pg-jev. [Project guide](community/projects/tools/pg-typesafe.md).
- [pi-jev](https://github.com/y0usaf/pi-jev) - Adds a TypeSafe Jev gate, output judge, and jev_ask tool to the Pi coding agent, with shadow mode by default and fail-open errors. [Project guide](community/projects/tools/pi-jev.md).
- [pi-jev-context](https://github.com/Nyarlathoteppppp/pi-jev-context) - Pi extension: cache-neutral write-time trimming of long tool outputs with TypeSafe Jev only when comparison cannot decide, plus lossless context_recall. [Project guide](community/projects/tools/pi-jev-context.md).
- [pi-jev-effort](https://github.com/namenu/pi-jev-effort) - Pi extension: TypeSafe Jev scores prompt difficulty and sets thinking level, capped by remaining quota/burn (distinct from pi-jev-router). [Project guide](community/projects/tools/pi-jev-effort.md).
- [pi-jev-permit](https://github.com/kurihada/pi-jev-permit) - Pi extension: TypeSafe Jev judges each bash/write/edit call after local hard-deny and read-only fast paths. [Project guide](community/projects/tools/pi-jev-permit.md).
- [pi-jev-router](https://github.com/philippdubach/pi-jev-router) - Pi extension: TypeSafe Jev classifies tasks and local policy routes OpenRouter models (Pareto profiles; shadow mode default). [Project guide](community/projects/tools/pi-jev-router.md).
- [pi-jev-sentinel](https://github.com/harshwasan/pi-jev-sentinel) - Adds TypeSafe Jev checks for Pi, Claude Code, and Codex tool calls, tool outputs, and replies, with secret scrubbing and fail-closed asks when unconfigured. [Project guide](community/projects/tools/pi-jev-sentinel.md).
- [pi-Jev-browser](https://github.com/laihenyi/pi-Jev-browser) - Pi extension where TypeSafe Jev chooses each Playwright browser action over a structured DOM observation in a bounded loop. [Project guide](community/projects/tools/pi-jev-browser.md).
- [pi-typesafe-bash-guard](https://github.com/gowthamgts/pi-stuff/tree/main/extensions/typesafe-bash-guard) - Pi extension that classifies bash tool calls and `!` shells with TypeSafe Jev before execution; supports 1Password `op://` API-key references. [Project guide](community/projects/tools/pi-typesafe-bash-guard.md).
- [pi-warden](https://github.com/DevMortimer/pi-warden) - Combines local Pi guard checks with Jev action and rule judgments, configurable holds, corrective feedback and context retention. [Project guide](community/projects/tools/pi-warden.md).
- [PlayJev](https://github.com/OmniJev/PlayJev) - Plays ten browser games from the frame alone with an open 0.8B model that scores the moves the game lists in one forward pass; independent of official Jev. [Project guide](community/projects/tools/playjev.md)
- [ruby_decision_model](https://github.com/obie/ruby_decision_model) - Stdlib-lean Ruby client for Noul/Choice/Score decision models via Typesafe or OpenRouter. [Project guide](community/projects/tools/ruby-decision-model.md).
- [SemDecide](https://github.com/sharziki/semdecide) - Typed semantic decisions for Unix pipelines and CI with TypeSafe Jev predicates, routes, scores, and filters. [Project guide](community/projects/tools/semdecide.md).
- [semantic-assert](https://github.com/mondaychen/semantic-assert) - Assert plain-English claims about captured UI/text state with TypeSafe Jev (Playwright helpers; thresholds in code). [Project guide](community/projects/tools/semantic-assert.md).
- [semgate](https://github.com/m-mizutani/semgate) - Go net/http middlewares that ask TypeSafe Jev typed questions about each request, then allow, block, or route. [Project guide](community/projects/tools/semgate.md).
- [SemIf](https://github.com/TheoLeeCJ/SemIf) - Explores typed option scoring and shared-state reuse with local open models; independent of official Jev. [Project guide](community/projects/tools/semif.md).
- [Skill Dash](https://github.com/48Nauts-Operator/skill-dash) - Local dashboard that judges Claude Code/Codex skills with TypeSafe Jev (usefulness, redundancy, clarity, action) plus transcript evidence. [Project guide](community/projects/tools/skill-dash.md).
- [SkillRanker](https://github.com/Dicklesworthstone/skillranker) - Ranks agent skills for the next step from live session context using TypeSafe Jev, with offline demos and a Claude Code hook; MIT plus an OpenAI/Anthropic license rider. [Project guide](community/projects/tools/skillranker.md).
- [sgrep](https://github.com/Lagnajit09/sgrep) - Semantic grep for codebases: chunk files and ask TypeSafe Jev which chunks match a plain-English query (includes offline mock). [Project guide](community/projects/tools/sgrep.md).
- [Skillbox](https://github.com/kitze/skillbox) - Self-hosts a versioned agent skill library with optional Jev recommendations over authorized skills and explicit search fallback. [Project guide](community/projects/tools/skillbox.md).
- [Sniff Test](https://github.com/DanRWilloughby/snifftest) - Prose linter with free local countable rules and optional TypeSafe Jev judgment rules after confirmation. [Project guide](community/projects/tools/snifftest.md).
- [SlidePilot](https://github.com/harshil1712/slidepilot) - Experimental Slidev addon that uses presenter voice, Cloudflare STT, and TypeSafe Jev to auto-advance when policy agrees. [Project guide](community/projects/tools/slidepilot.md).
- [SmartMoney-Cub](https://github.com/myc0576/SmartMoney-Cub) - Read-only trading journal and review harness with optional TypeSafe Jev typed judgments and a frozen finance-jev offline benchmark (no orders). [Project guide](community/projects/tools/smartmoney-cub.md).
- [Stanley Code](https://github.com/devagrawal09/stanley-code) - Routes coding requests into bounded Jev review and triage workflows, with trusted repository extensions and an optional Pi coding-agent fallback. [Project guide](community/projects/tools/stanley-code.md).
- [Supercov](https://github.com/supercorp-ai/supercov) - Code quality and test coverage for coding agents: Jev scores each source file so the agent knows what to fix first. [Project guide](community/projects/tools/supercov.md).
- [super-jev](https://github.com/Kevthetech143/super-jev) - Evidence-to-action TypeScript harness: typed Jev judgments, permitted tools, verified outcomes, and JSONL journals. [Project guide](community/projects/tools/super-jev.md).
- [System One Harness](https://github.com/HarnessRouter/SystemOneHarness) - Python controller: finite-action agent loops with TypeSafe Jev (OpenRouter or TypeSafe), confidence gates, and step traces. [Project guide](community/projects/tools/systemone-harness.md).
- [tax-doc-classifier](https://github.com/kyotofin/tax-doc-classifier) - Classifies tax PDF pages into IRS forms and page kinds with TypeSafe Jev Choice over a shipped criteria JSON (261 forms). [Project guide](community/projects/tools/tax-doc-classifier.md).
- [The Jev-enator](https://github.com/jakenbear/the-jev-enator) - Claude Code hooks using TypeSafe Jev for a danger gate, failure notice, and optional completion check (cassette-tested offline). [Project guide](community/projects/tools/the-jev-enator.md).
- [todo-jev](https://github.com/maker-KK/todo-jev) - Task classifier and 3-tier router (local rule / Jev skill / foundation model) with skill profiles and offline fallback. [Project guide](community/projects/tools/todo-jev.md).
- [Testimonial miner](https://github.com/AppitStudio/testimonial-miner) - Python CLI that finds quotable user praise in Gmail mailboxes with one Jev request per email (message kind, app, praise quality, and a Noul per sentence) and stores verbatim quotes for review; requires a TypeSafe key and Google app passwords, and sends cleaned email text to TypeSafe. [Project guide](community/projects/tools/testimonial-miner.md).
- [toolgate](https://github.com/RiskAverseTech/toolgate) - Open Claude Code PreToolUse and MCP tool-call firewall with static rules, TypeSafe Jev judgments, YAML policy, and a local audit log. [Project guide](community/projects/tools/toolgate.md).
- [Tripwire](https://github.com/anuran-de/tripwire) - Streaming proxy that trips on partial LLM output and can abort upstream mid-flight, with TypeSafe Jev or a heuristic detector. [Project guide](community/projects/tools/tripwire.md).
- [triagedy](https://github.com/m0rphtail/triagedy) - UNIX-filter security-alert triage: JSONL in, typed TypeSafe Jev decisions out; policy routing stays in Rust code. [Project guide](community/projects/tools/triagedy.md).
- [typesafe-agent-gates](https://github.com/ThiagaoBR/typesafe_agent_gates) - LangChain/Deep Agents middleware using TypeSafe Jev for shell gates, issue triage, MR detection, and test-spec review. [Project guide](community/projects/tools/typesafe-agent-gates.md).
- [TypeSafe Mario](https://github.com/fhshaik/typesafe-mario) - Selects emulator controller inputs with Jev from structured Mario telemetry; includes a synthetic state demo, with upstream licensing unspecified. [Project guide](community/projects/tools/typesafe-mario.md).
- [TypeSafe MCP](https://github.com/itsmostafa/typesafe-mcp) - Exposes typed Jev questions to MCP clients and pi, preserving provider responses with configurable direct or OpenRouter access. [Project guide](community/projects/tools/typesafe-mcp.md).
- [TypeSafe-as-a-Judge](https://github.com/E-FL/typesafe-as-a-judge) - Unofficial Codex/Claude Code MCP plugin for bounded TypeSafe Jev route/rank/extract/verify/judge tools with proceed/review gates. [Project guide](community/projects/tools/typesafe-as-a-judge.md).
- [TypeSafe AI for Agent Zero](https://github.com/3clyp50/a0-typesafe-ai) - Agent Zero plugin for typed Jev Choice/Noul/Score judgments with probability cards; bundles the official TypeSafe agent skill. [Project guide](community/projects/tools/a0-typesafe-ai.md).
- [Spring AI TypeSafe](https://github.com/spring-ai-community/spring-ai-typesafe) - Unofficial Java/Spring AI System One client with JevJudge, guardrail/RAG advisors, and starter (Maven `org.springaicommunity`; distinct from jev-java). [Project guide](community/projects/tools/spring-ai-typesafe.md).
- [TypeSafe Go](https://github.com/stacklok/typesafe-go) - Unofficial Go System One client (Stacklok): explicit auth options, no implicit env reads; distinct from jevgo. [Project guide](community/projects/tools/typesafe-go.md).
- [TypeSafe (Swift)](https://github.com/krzyzanowskim/TypeSafe) - SwiftPM client for TypeSafe System One Noul/Choice/Score questions, aligned with the official JS SDK shape. [Project guide](community/projects/tools/typesafe-swift.md).
- [jev (okooo5km)](https://github.com/okooo5km/jev) - Stdlib Python CLI + Agent Skill for TypeSafe Jev `yes`/`pick`/`score` via TypeSafe API or OpenRouter (distinct from typesafe-cli / typesafeai-cli). [Project guide](community/projects/tools/okooo5km-jev.md).
- [jev-cli (tumf)](https://github.com/tumf/jev-cli) - Unofficial PyPI CLI + stdio MCP for TypeSafe Jev noul/choice/score (distinct from okooo5km/jev, typesafe-cli, typesafeai-cli). [Project guide](community/projects/tools/tumf-jev-cli.md).
- [typesafe-cli](https://github.com/y0usaf/typesafe-cli) - Shell `jev` CLI for TypeSafe Jev noul/choice/score answers as numbers (distinct from Python typesafeai-cli). [Project guide](community/projects/tools/typesafe-cli.md).
- [typesafe-api (Rust)](https://github.com/noahbclarkson/typesafe-api-rs) - Ergonomic Rust client for TypeSafe System One typed questions and answers (`typesafe-api` 0.1.0). [Project guide](community/projects/tools/typesafe-api-rs.md).
- [typesafeai-cli](https://github.com/maddygoround/typesafeai-cli) - Python `typesafe` CLI for TypeSafe Jev ask/decide/screen/verify flows for humans and agents. [Project guide](community/projects/tools/typesafeai-cli.md).
- [typesafe-computer-use](https://github.com/awlevin/typesafe-computer-use) - Combines local OCR and Accessibility observations with Jev decisions to operate macOS, with an optional writing model. [Project guide](community/projects/tools/typesafe-computer-use.md).
- [TypeSafeAI.Net](https://github.com/Hawxy/TypeSafeAI.Net) - Community .NET client with typed questions, dependency injection, and Microsoft.Extensions.AI adapters. [Project guide](community/projects/tools/typesafeai-net.md).
- [TypeSafe.AI (.NET SDK)](https://github.com/typesafe-sdk-csharp/typesafe-sdk) - Unofficial .NET System One client (NuGet TypeSafe.AI) with DI, resilience, and OTel; distinct from TypeSafeAI.Net. [Project guide](community/projects/tools/typesafe-sdk-csharp.md).
- [Typed Evals](https://github.com/TrustifAI/typed_evals) - Evaluate LLM/RAG/agent outputs with TypeSafe Jev judges, optional calibration, and tool guards. [Project guide](community/projects/tools/typed-evals.md).
- [VexJoy Agent](https://github.com/notque/vexjoy-agent) - Agent toolkit for Claude Code/Codex: `/do` routes work to specialist agents/skills; optional `/d` uses TypeSafe Jev to classify and gate intent before dispatch. [Project guide](community/projects/tools/vexjoy-agent.md).
- [winnow](https://github.com/GhalebDweikat/winnow) - Claude Code context sieve: TypeSafe Jev (or System One adapter) judges tool-result blocks before they enter context; hidden text stays recallable. [Project guide](community/projects/tools/winnow.md).
- [webctl](https://github.com/dorkitude/webctl) - Agent web-search CLI that scores and judges multi-provider results (optional scrape chunks) with TypeSafe Jev. [Project guide](community/projects/tools/webctl.md).
- [Yoshi](https://github.com/compozy/yoshi) - Experimental local context-pruning proxy for Claude Code and Codex; TypeSafe Jev (Vercel AI Gateway) judges which history spans to omit. [Project guide](community/projects/tools/yoshi.md).

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
