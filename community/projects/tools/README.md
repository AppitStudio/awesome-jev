# Tools and integrations

[All projects](../README.md) · [Apps powered by Jev](../apps/README.md) · [Share a tool](../../../CONTRIBUTING.md#add-a-community-project)

Developer tools, libraries, SDKs, integrations, and reference implementations for building with Jev. Each full guide explains how to use the project, what needs adapting, and what was checked. For an application with its own user-facing workflow, visit the separate [app directory](../apps/README.md).

## Categories

- [Browser and computer use](#browser-and-computer-use)
- [Customer feedback and marketing](#customer-feedback-and-marketing)
- [Developer tools](#developer-tools)
- [Games and simulation](#games-and-simulation)
- [Home automation](#home-automation)
- [Independent model research](#independent-model-research)
- [SDKs and integrations](#sdks-and-integrations)
- [Search and retrieval](#search-and-retrieval)

## Browser and computer use

See the [computer-use guide](../../../docs/computer-use.md) for a comparison, form/extraction examples, native-app testing designs, and the evidence boundary around iOS demonstrations.

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Cua jev-use](cua-jev-use.md) | Compose a bounded chooser with Driver and independent fixture verification. | Python / TypeScript · integration recipe |
| [Jev Browser (tontoko)](jev-browser-tontoko.md) | Fill forms, extract records with evidence, and add semantic selection to Playwright tests. | TypeScript · SDK, CLI and MCP |
| [Jev Browser (Ying-Kai-Liao)](jev-browser-ying-kai-liao.md) | Run small browser goals with Jev action/target selection and direct inspection; page data and supplied values reach TypeSafe. | JavaScript · Playwright library, CLI and MCP |
| [Jev Browser Skill](jev-browser-skill.md) | Learn a minimal Jev-driven browser loop as a Claude Code/Codex skill (reference; see Ultrafast for fuller agents). | Agent skill + CDP scripts (`scripts/*.mjs`); explainer site |
| [JevOnly](jevonly.md) | Drive a browser with pure Jev choices over code-built options—no planner or helper LLM. | Python · CLI, local viewer and Playwright |
| [Jev Ultrafast](jev-ultrafast.md) | Select browser operations and targets from the current page. | Python · browser agent and inspector |
| [Jev Voice Browser](jev-voice-browser.md) | Study partial speech, target disambiguation, and browser actions with an inspectable decision policy. | JavaScript · Playwright voice-control reference |
| [Jev-cu](jev-cu.md) | Study experimental Jev decisions over macOS Accessibility text in Codex; review the execution-policy limitations before use. | JavaScript · Codex skill and runtime |
| [jev-macos-loop](jev-macos-loop.md) | Automate native macOS GUI apps with local OmniParser/Vision perception and text-only Jev action choice. | TypeScript/Node · Apple silicon CLI |
| [jev-android](jev-android.md) | Drive Android UI via accessibility with TypeSafe Jev or DeepSeek action choice (Kotlin SDK + sample). | Kotlin · Android SDK (`core`/`sdk`/`sample` 0.2.0) |
| [Mobile Jev](mobile-jev.md) | Navigate an Android device and verify a dark-theme task. | JavaScript / React · Mobilerun agent and studio |
| [pi-Jev-browser](pi-jev-browser.md) | Let Jev choose each Playwright browser action over a structured DOM observation inside Pi. | TypeScript · Pi extension (npm) |
| [typesafe-computer-use](typesafe-computer-use.md) | Study OCR and Accessibility driven native macOS control. | Python · desktop CLI |

## Customer feedback and marketing

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Testimonial miner](testimonial-miner.md) | Find and review verbatim praise in email, grouped by product. | Python · CLI and local dashboard |
| [jev-seo](jev-seo.md) | Local SEO/GEO CLI and MCP: DuckDuckGo SERP/audits plus optional TypeSafe Jev intent and visibility judgments. | Rust · CLI (`jev-seo`) and MCP |

## Developer tools

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Agent Router](agent-router.md) | Quota-aware Herdr launcher: local eligibility then TypeSafe System One (Jev) picks agent/model/effort. | TypeScript · CLI (`@agent-router/router` 0.1.0) |
| [ask-jev-skill](ask-jev-skill.md) | Call TypeSafe Jev as a Hermes typed tiebreaker (Choice/Score/Noul) when multiple paths remain. | Python · Hermes skill + stdlib CLI |
| [beam-cli](beam-cli.md) | Local AgentBeam hooks/policy for coding agents; optional TypeSafe Jev Noul/Score action judging (off by default). | TypeScript · npm CLI (`@agent-beam/beam` 0.2.16, AGPL-3.0) |
| [bitrate-advisor](bitrate-advisor.md) | Choose live-stream encoder bitrate/resolution/next-step with TypeSafe Jev via OpenRouter inside deterministic guardrails. | TypeScript · Deno/Node library (`@affirmi/bitrate-advisor` 0.2.7) |
| [Canny](canny.md) | Stop Claude Code/Codex “done” claims without ledger evidence; TypeSafe Jev advises, only facts block. | TypeScript · CLI (`canny-warden` 0.1.0), zero runtime deps |
| [clear-head](clear-head.md) | Claude Code Stop hook: TypeSafe Jev checks answer claims against what was read this session. | Python · Stop hook + install scripts |
| [daf-jev](daf-jev.md) | Build typed Jev questions, gates, batch evaluation, and optional MCP tools in Python. | Python · library/CLI (`daf-jev` 0.3.0) |
| [dbt_jev](dbt-jev.md) | Classify SQL values with TypeSafe Jev (or OpenRouter→Jev) from dbt macros on DuckDB/ClickHouse. | Python · dbt package + DuckDB/ClickHouse runtime |
| [decision-first](decision-first.md) | Spot bounded judgments, try TypeSafe Jev first, and log adopt/decline cases for reuse. | Python · agent skill + stdlib scripts |
| [doc-router](doc-router.md) | Select which PDF pages need OCR using optional Jev judgments, then merge local extraction and provider results. | Rust · library and CLI, Python bindings |
| [demo-expanso-jev](demo-expanso-jev.md) | Run Expanso Edge pipelines that bypass routine lines and ask TypeSafe Jev only on the rest (boards + mock server). | Demo suite · Expanso YAML, Python boards, `just` recipes |
| [Distill](distill.md) | Route coding-agent model/effort and utility/retention choices with TypeSafe Jev (or OpenRouter decisions) inside a local TUI harness. | Rust · coding agent CLI/TUI (Distill 2.0) |
| [ExcelPilot](excelpilot.md) | Drive live Excel workbooks with Qwen planning and TypeSafe Jev intent/tool gates (cascade to OpenRouter/offline). | Python · Office.js add-in + FastMCP agent (`excelpilot` 1.0.0) |
| [Eutrya](eutrya.md) | Run a CLI agent loop where TypeSafe Jev picks attention modes and scores candidates; text model proposes; offline demo included (alpha). | Node.js · CLI (`eutrya` 0.4.9) |
| [fast-jev-compaction](fast-jev-compaction.md) | Select which old tool calls and results remain in agent context. | TypeScript · library and Claude Code plugin |
| [Foreman](foreman.md) | Experiment with Jev supervision of Codex workers and inspect steering, retry, and verification decisions. | Python · CLI and supervision runtime |
| [Graphlin](graphlin.md) | Live architecture/activity diagrams for Claude Code or Codex; optional TypeSafe Jev classification of graph evidence. | Node.js · CLI/viewer (`npx graphlin`), plugins |
| [Grok Bot Jev](grok-bot-jev.md) | Gate Grok Bot research/browser/retry/subagent work with TypeSafe Jev actions (shadow or active skill mode). | Python · router, skill template and dry-run CLI |
| [Hermes Jev Skills](hermes-jev-skills.md) | Add Jev model routing, memory filter, compaction, skill pick, triage, and computer/browser choices to Hermes, Claude Code, and Codex. | Python · skills, `jev` CLI and Hermes plugin |
| [invalidate](invalidate.md) | Check every stored agent memory against new evidence with TypeSafe Jev; mark superseded facts without rewriting text. | Python · library, CLI and memory adapters |
| [is-malicious](is-malicious.md) | Scan a codebase for deceptive or data-stealing behavior with TypeSafe Jev file/line findings. | TypeScript · npm CLI (`is-malicious` 0.1.0) |
| [JCR](jcr.md) | Resolve deterministic commands from a nested capability tree with TypeSafe Jev (MCP + Claude/Codex harnesses). | TypeScript · resolver, MCP and harnesses (`jcr` 1.0.0) |
| [jev-align](jev-align.md) | Build calibrated classifiers/AI Functions from human feedback with TypeSafe Jev + GEPA (`jeva`). | Python · CLI (`jev-align` / `jeva`) |
| [Typed Evals](typed-evals.md) | Evaluate RAG/agent outputs and guard tools with TypeSafe Jev judges and optional calibration. | Python · library/CLI (`typed_evals`) |
| [Jev Logs](jevlogs.md) | Prioritize logs for deeper analysis alongside your archive. | TypeScript · library, CLI and OpenTelemetry integration |
| [jevmetrics](jevmetrics.md) | Assess unfamiliar OTel metrics for retention with TypeSafe Jev, then apply deterministic keep/reduce policy. | Go · OpenTelemetry Collector processor (0.1.0-dev alpha) |
| [Jev Model Router](jev-model-router.md) | Route Claude Code subagent models and main-conversation reasoning effort using Jev assessments; requires early-access function hooks. | TypeScript · Claude Code mod |
| [tokengate](jev-model-tokengate.md) | Buffer streamed LLM tokens and gate each window with TypeSafe Jev before the client sees them. | Node.js · OpenAI-compatible proxy (`tokengate` 0.1.0) |
| [Jev Review](jev-review.md) | Add experimental quality judgments to a coding agent's review loop. | Node.js · MCP server |
| [Jev Review (Dev Agrawal)](jev-review-devagrawal.md) | Screen JavaScript/TypeScript diffs or codebases and inspect staged review findings. | TypeScript · CLI and local dashboard |
| [Jev Review Action](jev-review-action.md) | Review catalog submissions or PR diffs with TypeSafe Jev only; one template PR comment (GitHub Action). | Node.js · GitHub Action (`jev-review-action` 0.2.0) |
| [Jev Sift](jev-sift.md) | Screen candidate content before reading it into agent context; requires a TypeSafe key, with upstream licensing unspecified. | Node.js · MCP server and agent plugin |
| [JevScope](jevscope.md) | Edit Jev projects visually, batch JSONL regression cases, and compare definitions locally. | TypeScript · Studio + local API (pnpm) |
| [Jev Trader](jev-trader.md) | Study Jev market-direction choices, simulated fills, and on-chain order execution through a Bun trading experiment. | TypeScript / Bun · trading reference and dashboard |
| [jev-lint](jev-lint.md) | Ast-grep selects subjects; TypeSafe Jev Noul scores one-sentence semantic rules (distinct from huntedman/JevLint). | TypeScript · npm CLI (`jev-lint` 0.4.1) |
| [JevLint](jevlint.md) | Lint source against plain-English conventions with file-level TypeSafe Jev Noul judgments (magic-strings, descriptive-names). | TypeScript · npm CLI (`@jevlint/cli`) |
| [jev-codex-router](jev-codex-router.md) | Route each Codex turn's model and thinking depth with Jev via a Codex Router generic provider. | Python · local server and Codex Router integration |
| [jev-codex-token-saver](jev-codex-token-saver.md) | Gather local workspace/log evidence and let TypeSafe Jev select exact excerpts for Codex (MCP plugin; local fallback). | Node.js · Codex plugin + MCP (`jev-codex-token-saver` 0.3.2) |
| [jev-gateway](jev-gateway.md) | Let Jev choose each tool call for Codex, Claude Code, OpenCode, or Gemini through a local LLM gateway. | TypeScript · npm launchers and dashboard |
| [jev-guard](jev-guard.md) | Risk-score coding-agent tool calls with TypeSafe Jev (deny/ask/allow), flag injection in results, and scan skills across many agents. | Node.js · npm CLI/hooks (`jev-guard` 0.3.1) |
| [jev-in-codex](jev-in-codex.md) | Rank Codex capabilities, search hits, and output excerpts with TypeSafe Jev via local MCP. | TypeScript · MCP server + Codex plugin (0.1.0) |
| [jev-issue-radar](jev-issue-radar.md) | Find duplicate/related GitHub issues with TypeSafe Jev evidence choices in a local read-only dashboard. | Node.js · loopback server + static UI (0.1.1) |
| [jev-layer](jev-layer.md) | Route harness capability choices with receipts/replay; host keeps execution (demo/OpenRouter/TypeSafe). | TypeScript · CLI, MCP and harness installers (`jev-layer` 0.1.0) |
| [jev-oas-sentinel](jev-oas-sentinel.md) | Compare OpenAPI specs with structural diffs plus TypeSafe Jev semantic contract questions. | Python · CLI (`jev-oas-sentinel`) |
| [jev-pii-checker](jev-pii-checker.md) | Scan text/files for PII with TypeSafe Jev presence/sensitivity judgments plus regex and segmentation layers. | TypeScript/Bun · CLI (`@coo-quack/jev-pii-checker` 0.3.1) |
| [jev-pr-judge](jev-pr-judge.md) | Typed PR verdicts with one parallel TypeSafe Jev call, TypeScript policy, Next.js UI, and GitHub Action sticky comments. | TypeScript · Next.js app and Action |
| [jev-preflight](jev-preflight.md) | Score eight risk axes on a Claude Code turn diff with one TypeSafe Jev request; optional assist reinspection. | Go · Claude Code plugin (v0.1.0) |
| [jev-pruner](jev-pruner.md) | Prune eligible Bash stdout with Jev before Claude Code or an opt-in Codex wrapper returns it to the model. | TypeScript · library, Claude Code plugin and Codex wrapper |
| [jev-router](jev-router.md) | Route Claude Code and Codex turns through Jev model selection and inspect stored routing exchanges. | JavaScript · CLI launchers and HTTP proxies |
| [jev-rules](jev-rules.md) | Select project rules and codebase-map documents for Claude Code prompts and file changes. | JavaScript · Claude Code plugin |
| [jev-shell-history](jev-shell-history.md) | Recall zsh history commands with optional acceptance of Jev-ranked inline suggestions; selected history is sent to TypeSafe. | TypeScript / zsh · shell plugin and CLI |
| [jev-shield](jev-shield.md) | Semantic MCP firewall: screen tool calls/results/descriptions with TypeSafe Jev via Vercel AI Gateway. | Node.js · CLI, MCP wrap, opt-in hooks (`jev-shield` 0.1.0) |
| [jev-skill-gate](jev-skill-gate.md) | Score Claude Code skills with TypeSafe Jev and write `skillOverrides` so only relevant skills reach context. | Node.js · CLI (`jev-skill-gate` 0.2.0) |
| [jev-use (shitianfang)](jev-use.md) | Route the no-text steps of a Claude Code, Codex or pi loop to Jev, with an opt-in PreToolUse gate and typed handbacks to the LLM. | TypeScript · MCP server, CLI and agent plugin |
| [jevc](jevc.md) | Compile agent rules/JSON Schema into TypeSafe Jev programs (typed questions + code reducers) with offline fixture checks. | TypeScript · npm CLI (`jevc` 0.1.0, Apache-2.0) |
| [jevcache](jevcache.md) | Reuse chat completions when TypeSafe Jev (via OpenRouter) admits paraphrased prompts as same-intent. | TypeScript · OpenAI-compatible proxy CLI (`@kushalicious/jevcache` 0.1.5) |
| [jeval](jeval.md) | Measure classifier confidence calibration and set cost-optimal human hand-off thresholds (Jev-motivated, provider-neutral). | Python · CLI (`jeval` 0.1.0, Apache-2.0) |
| [Metis](metis.md) | Triage new GitHub issues with TypeSafe Jev labels and missing-detail comments via a reusable Action/CLI. | Python · GitHub Action + `metis-triage` 0.1.0 |
| [Moongate](moongate.md) | Evaluate PR diffs against JSON semantic rules with TypeSafe Jev and emit CI annotations. | MoonBit / GitHub Action (`brickfrog/moongate`) |
| [patdown](patdown.md) | Lint a tree against fuzzy markdown rules with a swappable judge; default backend is TypeSafe Jev. | TypeScript · npm CLI (`patdown`) and Effect packages |
| [pi-jev](pi-jev.md) | Add a Jev pre-tool gate, output judge, and jev_ask tool to the Pi coding agent (shadow mode default, fail-open). | TypeScript · Pi extension (npm) |
| [pi-jev-router](pi-jev-router.md) | Route pi tasks across OpenRouter models with TypeSafe Jev classification and local Pareto/role policy (shadow default). | TypeScript · Pi extension (`pi-jev-router` 0.1.0) |
| [pi-jev-sentinel](pi-jev-sentinel.md) | Check Pi/Claude/Codex tool calls, outputs, and replies with Jev intent/risk and injection screens (fail-closed without a key). | TypeScript · Pi extension and host hooks |
| [pi-typesafe-bash-guard](pi-typesafe-bash-guard.md) | Classify Pi bash tool calls and user `!` shells with TypeSafe Jev before execution. | TypeScript · Pi extension (npm `@gowthamgts/pi-typesafe-bash-guard` 0.1.0) |
| [pi-warden](pi-warden.md) | Add configurable action holds, project-rule feedback and context checks to Pi using local policy and Jev judgments. | TypeScript · Pi extension |
| [Responsible AI Harness](responsible-ai-harness.md) | Assess AI systems with hard rules plus optional TypeSafe Jev judge; checksummed evidence bundles and offline report UI. | TypeScript · assessment harness + static UI (`responsible-ai-harness` 0.1.0) |
| [SemDecide](semdecide.md) | Run TypeSafe Jev predicates, routes, scores, and JSONL filters as Unix CLI exit codes for pipelines and CI. | Python · CLI (`semdecide` 0.2.1) |
| [SkillRanker](skillranker.md) | Rank which agent skills fit the next step from live session context using Jev wide/re-rank stages. | Rust · CLI (`sr`), hooks and TUI |
| [Skillbox](skillbox.md) | Share versioned agent skills and use optional Jev scores to recommend authorized skills for a task. | TypeScript / Bun / PostgreSQL · skill library, MCP and CLI |
| [Sniff Test](snifftest.md) | Lint Markdown/prose with local countable rules plus optional confirmed TypeSafe Jev judgment rules. | TypeScript/Bun · CLI (`snifftest` 0.1.0) |
| [SlidePilot](slidepilot.md) | Advance Slidev decks from presenter voice when TypeSafe Jev and TypeScript policy agree the slide is complete. | TypeScript · Slidev addon + Cloudflare Worker (0.1.0) |
| [SmartMoney-Cub](smartmoney-cub.md) | Capture offline trading-journal evidence packs and optionally ask TypeSafe Jev typed review questions (read-only; no orders). | Python · `smcub` CLI and harness |
| [Stanley Code](stanley-code.md) | Review code changes, triage failures, and extend Jev workflows; optional Pi delegation can edit the repository. | TypeScript · source-built CLI and workflow runtime |
| [Supercov](supercov.md) | Code quality and test coverage for coding agents: Jev scores each source file so the agent knows what to fix first. | Rust · CLI via npm, Homebrew, Go or crates.io |
| [super-jev](super-jev.md) | Run evidence → typed Jev judgments → permitted actions → verified outcomes with local JSONL traces. | TypeScript · harness (Node ≥ 24) |
| [tax-doc-classifier](tax-doc-classifier.md) | Classify tax PDF page text into IRS form ids and page kinds with TypeSafe Jev Choice over shipped criteria. | TypeScript · library (`tax-doc-classifier`) |
| [The Jev-enator](the-jev-enator.md) | Claude Code hooks: TypeSafe Jev danger gate, failure notice, and log-only completion check. | Python · stdlib hooks + install scripts |
| [todo-jev](todo-jev.md) | Classify requests into a 3-tier path (local rule / Jev skill / foundation model) with skill profiles and preflight. | Python · Typer CLI (`todo-jev` 0.1.0) |
| [toolgate](toolgate.md) | Gate Claude Code and MCP tool calls with static rules plus TypeSafe Jev risk judgments and a local audit log. | TypeScript · CLI, Claude Code hook and MCP proxy |
| [typesafe-agent-gates](typesafe-agent-gates.md) | Gate unattended LangChain/Deep Agents shell commands and triage with TypeSafe Jev middleware. | Python · LangChain middleware |
| [VexJoy Agent](vexjoy-agent.md) | Route plain-English requests to specialist agents/skills; optional `/d` uses TypeSafe Jev classification and intent gates. | Python · agent toolkit (Claude Code / Codex hooks) |
| [winnow](winnow.md) | Hide confident-irrelevant Claude Code tool-result blocks with TypeSafe Jev (or adapter) judgments; recall stubs on demand. | Python · Claude Code hooks + sidecar CLI (`winnow` 0.5.0) |
| [Yoshi](yoshi.md) | Local Claude Code/Codex context-pruning proxy: TypeSafe Jev via AI Gateway judges omit/keep spans (experimental POC). | Bun/TypeScript · loopback proxy (`yoshi` 0.1.0) |

## Games and simulation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [jev-drone](jev-drone.md) | Study typed maneuver judgments alongside deterministic simulated flight control and inspect a separate tunnel experiment. | Python / MuJoCo · simulation and replay |
| [jev-libero](jev-libero.md) | Study fine-grained LIBERO robot actions with TypeSafe Jev layered choices and local physics previews. | Python · CLI and MuJoCo/LIBERO extras |
| [quackd](quackd.md) | Drive multi-robot goals with LLM pilots; optional `--jev` TypeSafe stepper for closed-set verb choices. | Python · CLI (`quackd`) and robot extras |
| [JevPilot](jevpilot.md) | Inspect sampled driving paths, Jev choices and local braking in a browser simulation; application licensing is unspecified. | JavaScript / Three.js · simulation demo |
| [TypeSafe Mario](typesafe-mario.md) | Study Jev action choices over emulator telemetry with a synthetic state demo and decision logs; licensing is unspecified. | Python · emulator controller and dashboard |
| [Jev Lab](jev-lab.md) | Run Hundred NPC-town and Jev Shogi labs where Jev picks the next legal action (Rules mode offline). | TypeScript · pnpm monorepo (`jev-lab` 0.2.0) |

## Home automation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Jev for Home Assistant](ha-jev.md) | Turn household context into judgment sensors and automation responses. | Python · Home Assistant integration |

## Independent model research

These projects study related typed-decision patterns using other models. They are independent research implementations, not official Jev releases or validated substitutes; their guides separate code, model and dataset licensing, and reported benchmarks from catalog checks.

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Jevlike](jevlike.md) | Train a small option-attention scorer with synthetic data and optional frozen encoders; independent of official Jev. | Python / PyTorch · research starter |
| [NanoJev](nanojev.md) | Study independent Qwen-based typed decision heads, local serving, and game controllers with recorded comparisons. | Python / PyTorch · model research and replay |
| [Open Alternative to Jev](open-alternative-jev.md) | Compare packed and separate typed decisions from open models and fit calibration on labeled data; not a Jev reproduction. | Python · Transformers/vLLM research library |
| [openjev-sglang](openjev-sglang.md) | Inspect a Jev-shaped HTTP decision API using Qwen and SGLang; independent model behavior and unspecified code licensing. | Python / FastAPI / SGLang · inference research |
| [PlayJev](playjev.md) | Study a 0.8B model that picks a game's next move from the frame alone, one forward pass, probability per listed move; independent of official Jev. | Python / PyTorch · model research and browser demo |
| [SemIf](semif.md) | Explore typed option scoring and shared-state reuse with local open models; independent of official Jev. | Python / PyTorch / MLX · research and browser lab |

## SDKs and integrations

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Advocaat](advocaat.md) | Batch typed Jev choice, score, and yes/no questions about structured data from TypeScript. | TypeScript · client library and agent skill |
| [feelings](feelings.md) | Add typed `.feels()` / `.how()` / `.matches<T>()` methods on any BAML value using TypeSafe Jev (license unspecified). | BAML · library (`baml_src/vibes.baml`) |
| [jev-prompt-sentry](jev-prompt-sentry.md) | Reverse-proxy Anthropic Messages through one batched TypeSafe Jev jailbreak/injection/exfil screen (PolyForm Noncommercial). | Python · FastAPI proxy |
| [Laravel AI](laravel-ai.md) | Add typed classification through Laravel’s TypeSafe provider. | PHP · Laravel package |
| [n8n-nodes-typesafe](n8n-nodes-typesafe.md) | Ask TypeSafe Jev noul/choice/score questions about workflow text or JSON inside n8n. | TypeScript · n8n community node |
| [nf-jev](nf-jev.md) | Call TypeSafe Jev noul/choice/score from Nextflow pipelines and gate on returned probabilities. | Groovy · Nextflow plugin (`nf-jev` 0.1.0, Apache-2.0) |
| [ruby_decision_model](ruby-decision-model.md) | Ask Noul, Choice, and Score questions from Ruby via Typesafe or OpenRouter. | Ruby · gem (stdlib HTTP) |
| [hono-jev-router](hono-jev-router.md) | Route Hono HTTP requests by plain-English meaning with TypeSafe Jev Noul judgments (experimental). | TypeScript · Hono router (`hono-jev-router`) |
| [semgate](semgate.md) | Filter and route Go HTTP requests with TypeSafe Jev noul/choice/score middlewares. | Go · net/http middleware |
| [jear](jear.md) | Route NEAR AI Cloud / IronClaw choices by budget, quality, and sensitivity using TypeSafe Jev structured decisions. | Rust · CLI/library (`jear` 0.1.0) |
| [jev-mcp](jev-mcp.md) | Give agents ten purpose-built TypeSafe Jev judgment MCP tools (verify, screen, find, classify, review, gate, …). | TypeScript · npm MCP server (`@jkudish/jev-mcp`) |
| [Jev Studio](jev-studio.md) | Experiment with TypeSafe Jev via a `jev` CLI (verify/screen/classify/…) and an MCP server with cookbook tools. | Python · CLI + MCP (`jev-studio` 0.1.0 Alpha) |
| [TypeSafe MCP](typesafe-mcp.md) | Give agents a general-purpose Jev evaluation tool with raw provider responses. | Go · MCP server and pi extension |
| [TypeSafe AI for Agent Zero](a0-typesafe-ai.md) | Ask TypeSafe Jev Choice/Noul/Score from Agent Zero chat with probability cards; bundles the official agent skill. | Python · Agent Zero plugin (`typesafe_ai` 1.0.0) |
| [TypeSafe (Swift)](typesafe-swift.md) | Call System One Noul/Choice/Score from SwiftPM apps and servers. | Swift · SwiftPM library (`TypeSafe`) |
| [typesafe-cli](typesafe-cli.md) | Ask Jev noul/choice/score questions from the shell (`jev`); answers are numbers, not prose. | TypeScript · npm CLI / Nix |
| [typesafe-api (Rust)](typesafe-api-rs.md) | Call System One from Rust with typed questions/answers (`typesafe-api` 0.1.0, MSRV 1.88). | Rust · crates.io client |
| [typesafeai-cli](typesafeai-cli.md) | Run TypeSafe Jev ask/decide/screen/verify flows from a Python `typesafe` CLI for humans or agents. | Python · CLI (`typesafe`) |
| [TypeSafeAI.Net](typesafeai-net.md) | Add typed Jev judgments to .NET applications and Microsoft.Extensions.AI pipelines. | C# · client library |
| [TypeSafe.AI (.NET SDK)](typesafe-sdk-csharp.md) | Call System One from .NET with DI, resilience, and OTel (NuGet TypeSafe.AI; distinct from TypeSafeAI.Net). | C# · NuGet client (`TypeSafe.AI` v1.0.0) |

## Search and retrieval

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [blink](blink.md) | Search a local codebase with TypeSafe Jev via ensemble directory walkers that Choice-pick the next file or folder. | Bun · CLI (`./blink`); license unspecified |
| [jegrep](jegrep.md) | Find code by natural-language intent using TypeSafe Jev (or OpenRouter→Jev) without embeddings. | Rust · CLI (`jegrep`) and release binaries |
| [jev-corrective-rag](jev-corrective-rag.md) | Corrective RAG with TypeSafe Jev typed gates for triage, chunk grading, and answer verification (LLM only generates). | Python · Streamlit app, CLI and bench |
| [jev-reranker](jev-reranker.md) | Rerank, filter, or compress JSON search candidates with TypeSafe Jev via a stdin/stdout Rust CLI. | Rust · npm CLI (`jev-reranker` 0.1.1) |
| [jev-semgrep](jev-semgrep.md) | Filter lines by whether a plain-language proposition holds, with AND/OR/NOT meanings via TypeSafe Jev (not Semgrep Inc). | Node.js · CLI (`@uehaj/semgrep`) |
| [JevSQL](jevsql.md) | Add TypeSafe Jev match/pick/rank/bool/choice helpers to SQLite SQL with batching, caches, and review queues. | TypeScript · library and CLI |
| [jgrep](jgrep.md) | Filters text, structured records, functions, and diff hunks against plain-English descriptions using Jev Noul judgments. | Python · library and CLI (`jev-grep`) |
| [jlink](jlink.md) | Links records under a plain-English match rule using Jev Noul pair judgments, with local candidate blocking and match resolution. | Python · library and CLI (`jlink`) |
| [jselect](jselect.md) | Selects source-linked evidence within a token budget using Jev Noul relevance judgments and local diversity-aware selection. | Python · library and CLI (`jev-select`) |
| [jsort](jsort.md) | Order lines/paragraphs/files along a plain-English dimension using pairwise TypeSafe Jev comparisons. | Python · CLI (`jsort` / jev-sort) |
| [llama-index-jev](llama-index-jev.md) | Rerank retrieved passages or choose a query engine in LlamaIndex. | Python · integration packages |
| [mysql-ailike](mysql-ailike.md) | Filter and join MySQL rows with natural-language conditions via TypeSafe Jev (`AILIKE`). | MySQL · native UDF/plugin (v0.2.0, GPL-2.0) |
| [neo4jev](neo4jev.md) | Explore graph paths with typed next-hop and goal judgments. | Python · Neo4j, notebooks and Streamlit |
| [pg-jev](pg-jev.md) | Ask semantic questions from SQL over database rows. | PostgreSQL · PL/Python extension |
| [pg_typesafe](pg-typesafe.md) | Call Choice/Noul/Score from SQL via a C+libcurl extension with batched multi-text helpers (pre-alpha; distinct from pg-jev). | PostgreSQL · C extension |
| [sgrep](sgrep.md) | Semantic grep: chunk a repo and ask TypeSafe Jev which chunks match a plain-English query (mock offline). | Python · CLI (`sgrep`) |
| [webctl](webctl.md) | Agent web-search CLI: multi-provider results scored/judged (and optionally chunk-scored) with TypeSafe Jev. | Go · CLI (`webctl`) |

## Try a smaller example

The repository also maintains its own [teaching examples](../../../examples/README.md), [Support Router](../../../projects/support-router/README.md), and [routing evaluation runner](../../../evaluations/README.md). These are useful when you want a small offline starting point before adopting a community project.

## Share or improve a tool

Follow [Add a community project](../../../CONTRIBUTING.md#add-a-community-project) and the [project-page template](../../PROJECT_TEMPLATE.md). Put the full guide in this folder, list it once in a category above, and keep its upstream and guide links in the root README. Corrections to setup instructions and limitations are welcome.

Upstream maintainers own their code and licenses. Check each page's reviewed version and [validation scope](../../../docs/validation.md#community-project-checks); a listing does not establish production quality or endorsement.
