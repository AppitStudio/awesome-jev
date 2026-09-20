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
| [JevOnly](jevonly.md) | Drive a browser with pure Jev choices over code-built options—no planner or helper LLM. | Python · CLI, local viewer and Playwright |
| [Jev Ultrafast](jev-ultrafast.md) | Select browser operations and targets from the current page. | Python · browser agent and inspector |
| [Jev Voice Browser](jev-voice-browser.md) | Study partial speech, target disambiguation, and browser actions with an inspectable decision policy. | JavaScript · Playwright voice-control reference |
| [Jev-cu](jev-cu.md) | Study experimental Jev decisions over macOS Accessibility text in Codex; review the execution-policy limitations before use. | JavaScript · Codex skill and runtime |
| [jev-macos-loop](jev-macos-loop.md) | Automate native macOS GUI apps with local OmniParser/Vision perception and text-only Jev action choice. | TypeScript/Node · Apple silicon CLI |
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
| [doc-router](doc-router.md) | Select which PDF pages need OCR using optional Jev judgments, then merge local extraction and provider results. | Rust · library and CLI, Python bindings |
| [Distill](distill.md) | Route coding-agent model/effort and utility/retention choices with TypeSafe Jev (or OpenRouter decisions) inside a local TUI harness. | Rust · coding agent CLI/TUI (Distill 2.0) |
| [fast-jev-compaction](fast-jev-compaction.md) | Select which old tool calls and results remain in agent context. | TypeScript · library and Claude Code plugin |
| [Foreman](foreman.md) | Experiment with Jev supervision of Codex workers and inspect steering, retry, and verification decisions. | Python · CLI and supervision runtime |
| [Grok Bot Jev](grok-bot-jev.md) | Gate Grok Bot research/browser/retry/subagent work with TypeSafe Jev actions (shadow or active skill mode). | Python · router, skill template and dry-run CLI |
| [Hermes Jev Skills](hermes-jev-skills.md) | Add Jev model routing, memory filter, compaction, skill pick, triage, and computer/browser choices to Hermes, Claude Code, and Codex. | Python · skills, `jev` CLI and Hermes plugin |
| [invalidate](invalidate.md) | Check every stored agent memory against new evidence with TypeSafe Jev; mark superseded facts without rewriting text. | Python · library, CLI and memory adapters |
| [Jev Logs](jevlogs.md) | Prioritize logs for deeper analysis alongside your archive. | TypeScript · library, CLI and OpenTelemetry integration |
| [Jev Model Router](jev-model-router.md) | Route Claude Code subagent models and main-conversation reasoning effort using Jev assessments; requires early-access function hooks. | TypeScript · Claude Code mod |
| [Jev Review](jev-review.md) | Add experimental quality judgments to a coding agent's review loop. | Node.js · MCP server |
| [Jev Review (Dev Agrawal)](jev-review-devagrawal.md) | Screen JavaScript/TypeScript diffs or codebases and inspect staged review findings. | TypeScript · CLI and local dashboard |
| [Jev Sift](jev-sift.md) | Screen candidate content before reading it into agent context; requires a TypeSafe key, with upstream licensing unspecified. | Node.js · MCP server and agent plugin |
| [JevScope](jevscope.md) | Edit Jev projects visually, batch JSONL regression cases, and compare definitions locally. | TypeScript · Studio + local API (pnpm) |
| [Jev Trader](jev-trader.md) | Study Jev market-direction choices, simulated fills, and on-chain order execution through a Bun trading experiment. | TypeScript / Bun · trading reference and dashboard |
| [JevLint](jevlint.md) | Lint source against plain-English conventions with file-level TypeSafe Jev Noul judgments (magic-strings, descriptive-names). | TypeScript · npm CLI (`@jevlint/cli`) |
| [jev-codex-router](jev-codex-router.md) | Route each Codex turn's model and thinking depth with Jev via a Codex Router generic provider. | Python · local server and Codex Router integration |
| [jev-gateway](jev-gateway.md) | Let Jev choose each tool call for Codex, Claude Code, OpenCode, or Gemini through a local LLM gateway. | TypeScript · npm launchers and dashboard |
| [jev-oas-sentinel](jev-oas-sentinel.md) | Compare OpenAPI specs with structural diffs plus TypeSafe Jev semantic contract questions. | Python · CLI (`jev-oas-sentinel`) |
| [jev-pr-judge](jev-pr-judge.md) | Typed PR verdicts with one parallel TypeSafe Jev call, TypeScript policy, Next.js UI, and GitHub Action sticky comments. | TypeScript · Next.js app and Action |
| [jev-pruner](jev-pruner.md) | Prune eligible Bash stdout with Jev before Claude Code or an opt-in Codex wrapper returns it to the model. | TypeScript · library, Claude Code plugin and Codex wrapper |
| [jev-router](jev-router.md) | Route Claude Code and Codex turns through Jev model selection and inspect stored routing exchanges. | JavaScript · CLI launchers and HTTP proxies |
| [jev-rules](jev-rules.md) | Select project rules and codebase-map documents for Claude Code prompts and file changes. | JavaScript · Claude Code plugin |
| [jev-shell-history](jev-shell-history.md) | Recall zsh history commands with optional acceptance of Jev-ranked inline suggestions; selected history is sent to TypeSafe. | TypeScript / zsh · shell plugin and CLI |
| [jev-use (shitianfang)](jev-use.md) | Route the no-text steps of a Claude Code, Codex or pi loop to Jev, with an opt-in PreToolUse gate and typed handbacks to the LLM. | TypeScript · MCP server, CLI and agent plugin |
| [Moongate](moongate.md) | Evaluate PR diffs against JSON semantic rules with TypeSafe Jev and emit CI annotations. | MoonBit / GitHub Action (`brickfrog/moongate`) |
| [patdown](patdown.md) | Lint a tree against fuzzy markdown rules with a swappable judge; default backend is TypeSafe Jev. | TypeScript · npm CLI (`patdown`) and Effect packages |
| [pi-jev](pi-jev.md) | Add a Jev pre-tool gate, output judge, and jev_ask tool to the Pi coding agent (shadow mode default, fail-open). | TypeScript · Pi extension (npm) |
| [pi-jev-sentinel](pi-jev-sentinel.md) | Check Pi/Claude/Codex tool calls, outputs, and replies with Jev intent/risk and injection screens (fail-closed without a key). | TypeScript · Pi extension and host hooks |
| [pi-warden](pi-warden.md) | Add configurable action holds, project-rule feedback and context checks to Pi using local policy and Jev judgments. | TypeScript · Pi extension |
| [SkillRanker](skillranker.md) | Rank which agent skills fit the next step from live session context using Jev wide/re-rank stages. | Rust · CLI (`sr`), hooks and TUI |
| [Skillbox](skillbox.md) | Share versioned agent skills and use optional Jev scores to recommend authorized skills for a task. | TypeScript / Bun / PostgreSQL · skill library, MCP and CLI |
| [SmartMoney-Cub](smartmoney-cub.md) | Capture offline trading-journal evidence packs and optionally ask TypeSafe Jev typed review questions (read-only; no orders). | Python · `smcub` CLI and harness |
| [Stanley Code](stanley-code.md) | Review code changes, triage failures, and extend Jev workflows; optional Pi delegation can edit the repository. | TypeScript · source-built CLI and workflow runtime |
| [Supercov](supercov.md) | Code quality and test coverage for coding agents: Jev scores each source file so the agent knows what to fix first. | Rust · CLI via npm, Homebrew, Go or crates.io |
| [super-jev](super-jev.md) | Run evidence → typed Jev judgments → permitted actions → verified outcomes with local JSONL traces. | TypeScript · harness (Node ≥ 24) |
| [toolgate](toolgate.md) | Gate Claude Code and MCP tool calls with static rules plus TypeSafe Jev risk judgments and a local audit log. | TypeScript · CLI, Claude Code hook and MCP proxy |
| [typesafe-agent-gates](typesafe-agent-gates.md) | Gate unattended LangChain/Deep Agents shell commands and triage with TypeSafe Jev middleware. | Python · LangChain middleware |
| [VexJoy Agent](vexjoy-agent.md) | Route plain-English requests to specialist agents/skills; optional `/d` uses TypeSafe Jev classification and intent gates. | Python · agent toolkit (Claude Code / Codex hooks) |

## Games and simulation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [jev-drone](jev-drone.md) | Study typed maneuver judgments alongside deterministic simulated flight control and inspect a separate tunnel experiment. | Python / MuJoCo · simulation and replay |
| [jev-libero](jev-libero.md) | Study fine-grained LIBERO robot actions with TypeSafe Jev layered choices and local physics previews. | Python · CLI and MuJoCo/LIBERO extras |
| [JevPilot](jevpilot.md) | Inspect sampled driving paths, Jev choices and local braking in a browser simulation; application licensing is unspecified. | JavaScript / Three.js · simulation demo |
| [TypeSafe Mario](typesafe-mario.md) | Study Jev action choices over emulator telemetry with a synthetic state demo and decision logs; licensing is unspecified. | Python · emulator controller and dashboard |

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
| [openjev-sglang](openjev-sglang.md) | Inspect a Jev-shaped HTTP decision API using Qwen and SGLang; independent model behavior and unspecified code licensing. | Python / FastAPI / SGLang · inference research |
| [SemIf](semif.md) | Explore typed option scoring and shared-state reuse with local open models; independent of official Jev. | Python / PyTorch / MLX · research and browser lab |

## SDKs and integrations

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Advocaat](advocaat.md) | Batch typed Jev choice, score, and yes/no questions about structured data from TypeScript. | TypeScript · client library and agent skill |
| [jev-prompt-sentry](jev-prompt-sentry.md) | Reverse-proxy Anthropic Messages through one batched TypeSafe Jev jailbreak/injection/exfil screen (PolyForm Noncommercial). | Python · FastAPI proxy |
| [Laravel AI](laravel-ai.md) | Add typed classification through Laravel’s TypeSafe provider. | PHP · Laravel package |
| [n8n-nodes-typesafe](n8n-nodes-typesafe.md) | Ask TypeSafe Jev noul/choice/score questions about workflow text or JSON inside n8n. | TypeScript · n8n community node |
| [ruby_decision_model](ruby-decision-model.md) | Ask Noul, Choice, and Score questions from Ruby via Typesafe or OpenRouter. | Ruby · gem (stdlib HTTP) |
| [hono-jev-router](hono-jev-router.md) | Route Hono HTTP requests by plain-English meaning with TypeSafe Jev Noul judgments (experimental). | TypeScript · Hono router (`hono-jev-router`) |
| [semgate](semgate.md) | Filter and route Go HTTP requests with TypeSafe Jev noul/choice/score middlewares. | Go · net/http middleware |
| [jev-mcp](jev-mcp.md) | Give agents ten purpose-built TypeSafe Jev judgment MCP tools (verify, screen, find, classify, review, gate, …). | TypeScript · npm MCP server (`@jkudish/jev-mcp`) |
| [TypeSafe MCP](typesafe-mcp.md) | Give agents a general-purpose Jev evaluation tool with raw provider responses. | Go · MCP server and pi extension |
| [TypeSafe (Swift)](typesafe-swift.md) | Call System One Noul/Choice/Score from SwiftPM apps and servers. | Swift · SwiftPM library (`TypeSafe`) |
| [typesafe-cli](typesafe-cli.md) | Ask Jev noul/choice/score questions from the shell (`jev`); answers are numbers, not prose. | TypeScript · npm CLI / Nix |
| [typesafeai-cli](typesafeai-cli.md) | Run TypeSafe Jev ask/decide/screen/verify flows from a Python `typesafe` CLI for humans or agents. | Python · CLI (`typesafe`) |
| [TypeSafeAI.Net](typesafeai-net.md) | Add typed Jev judgments to .NET applications and Microsoft.Extensions.AI pipelines. | C# · client library |

## Search and retrieval

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [jegrep](jegrep.md) | Find code by natural-language intent using TypeSafe Jev (or OpenRouter→Jev) without embeddings. | Rust · CLI (`jegrep`) and release binaries |
| [jev-semgrep](jev-semgrep.md) | Filter lines by whether a plain-language proposition holds, with AND/OR/NOT meanings via TypeSafe Jev (not Semgrep Inc). | Node.js · CLI (`@uehaj/semgrep`) |
| [JevSQL](jevsql.md) | Add TypeSafe Jev match/pick/rank/bool/choice helpers to SQLite SQL with batching, caches, and review queues. | TypeScript · library and CLI |
| [jsort](jsort.md) | Order lines/paragraphs/files along a plain-English dimension using pairwise TypeSafe Jev comparisons. | Python · CLI (`jsort` / jev-sort) |
| [llama-index-jev](llama-index-jev.md) | Rerank retrieved passages or choose a query engine in LlamaIndex. | Python · integration packages |
| [neo4jev](neo4jev.md) | Explore graph paths with typed next-hop and goal judgments. | Python · Neo4j, notebooks and Streamlit |
| [pg-jev](pg-jev.md) | Ask semantic questions from SQL over database rows. | PostgreSQL · PL/Python extension |
| [pg_typesafe](pg-typesafe.md) | Call Choice/Noul/Score from SQL via a C+libcurl extension with batched multi-text helpers (pre-alpha; distinct from pg-jev). | PostgreSQL · C extension |

## Try a smaller example

The repository also maintains its own [teaching examples](../../../examples/README.md), [Support Router](../../../projects/support-router/README.md), and [routing evaluation runner](../../../evaluations/README.md). These are useful when you want a small offline starting point before adopting a community project.

## Share or improve a tool

Follow [Add a community project](../../../CONTRIBUTING.md#add-a-community-project) and the [project-page template](../../PROJECT_TEMPLATE.md). Put the full guide in this folder, list it once in a category above, and keep its upstream and guide links in the root README. Corrections to setup instructions and limitations are welcome.

Upstream maintainers own their code and licenses. Check each page's reviewed version and [validation scope](../../../docs/validation.md#community-project-checks); a listing does not establish production quality or endorsement.
