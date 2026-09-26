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
| [agent-desktop](agent-desktop.md) | Drive macOS apps via accessibility refs; optional jev-desktop skill/scripts ask TypeSafe Jev for target/command without putting the a11y tree in agent context (CLI works without Jev). | Rust · CLI/npm (`agent-desktop` 0.9.2) + Node jev scripts |
| [ajevt-browser](ajevt-browser.md) | Bounded System One browser loop for Pi/OpenCode/Amp/MCP via agent-browser (observe→Jev→act). | TypeScript · npm (`ajevt-browser` / `ajevt-browser-mcp`, AGPL-3.0) |
| [Cua jev-use](cua-jev-use.md) | Compose a bounded chooser with Driver and independent fixture verification. | Python / TypeScript · integration recipe |
| [CUA-JEV (ZJU-REAL)](cua-jev-zju.md) | Constrained computer-use loop: Jev selects typed action×channel candidates with guards and verifiers. | Python · framework (Apache-2.0) |
| [DepthJev](depthjev.md) | Embodied navigation with depth/text facts; TypeSafe Jev chooses EB-Navigation actions. | Python · EmbodiedBench agent (Apache-2.0) |
| [firefox-jev-mcp](firefox-jev-mcp.md) | Claude plans; TypeSafe Jev picks Firefox element actions via MCP + WebExtension. | TypeScript · MCP + Firefox extension (MIT) |
| [Flick (flick-computer-use)](flick-computer-use.md) | MCP computer-use: Jev decides browser/macOS actions for whole goals. | TypeScript · MCP (MIT) |
| [Footwork](footwork.md) | Dual-process browser agent: TypeSafe Jev as System 1 in front of browser-use System 2, with a code-owned arbiter and evidence verification. | Python/Rust · package (`jevdual` 0.0.1) |
| [gpui-agent](gpui-agent.md) | Drive instrumented GPUI apps via accessibility: TypeSafe Jev chooses typed actions/targets (no screenshots to the model). | Rust/Python/TypeScript · experimental native toolkit |
| [Jev Browser (openqa-cn)](openqa-jev-browser.md) | Indexed Playwright automation: TypeSafe Jev chooses control/op; replay, generate, explore, HTML reports (CodexQA skill). | TypeScript · CLI (`codexqa-jev-browser` 0.1.0, MIT) |
| [Jev Browser (tontoko)](jev-browser-tontoko.md) | Fill forms, extract records with evidence, and add semantic selection to Playwright tests. | TypeScript · SDK, CLI and MCP |
| [Jev Browser (Ying-Kai-Liao)](jev-browser-ying-kai-liao.md) | Run small browser goals with Jev action/target selection and direct inspection; page data and supplied values reach TypeSafe. | JavaScript · Playwright library, CLI and MCP |
| [Jev Browser Skill](jev-browser-skill.md) | Learn a minimal Jev-driven browser loop as a Claude Code/Codex skill (reference; see Ultrafast for fuller agents). | Agent skill + CDP scripts (`scripts/*.mjs`); explainer site |
| [Jev Ultrafast](jev-ultrafast.md) | Select browser operations and targets from the current page. | Python · browser agent and inspector |
| [Jev Voice Browser](jev-voice-browser.md) | Study partial speech, target disambiguation, and browser actions with an inspectable decision policy. | JavaScript · Playwright voice-control reference |
| [jev-android](jev-android.md) | Drive Android UI via accessibility with TypeSafe Jev or DeepSeek action choice (Kotlin SDK + sample). | Kotlin · Android SDK (`core`/`sdk`/`sample` 0.2.0) |
| [jev-browse (cooper667)](cooper667-jev-browse.md) | Claude Code plain-English Playwright QA checklist judged by TypeSafe Jev on Cloudflare Workers AI. | TypeScript · Claude Code plugin/skill (MIT) |
| [jev-browse (danielnc)](danielnc-jev-browse.md) | Fast Jev browser sub-tasks on browser-harness for coding agents. | Python · harness (MIT) |
| [jev-browser-bridge](jev-browser-bridge.md) | Plug any CDP browser (cloud/local/self-hosted, incl. no-render) into Jev browser automation. | Python · bridge (Apache-2.0) |
| [jev-browser-mcp (bothuany)](bothuany-jev-browser-mcp.md) | MCP browser: host intent → TypeSafe Jev clicks + cheap reader; DOM stays out of agent context. | JavaScript · MCP/Playwright (MIT) |
| [jev-browser-skill (ChenYCL)](chenycl-jev-browser-skill.md) | Browser/computer-use CLI+MCP: TypeSafe Jev action choice (ego lite/Chrome/Safari); distinct from zurfyx/hqman. | Node.js ≥ 22 · CLI/MCP skill (MIT) |
| [jev-browser-skill (hqman)](hqman-jev-browser-skill.md) | Playwright Chromium skill/`jb` CLI: Jev chooses in-page actions (Gateway or TypeSafe); distinct from zurfyx teaching skill. | Node.js ≥ 22.18 · skill + CLI (`jb`, Apache-2.0) |
| [jev-browser-use (AuroraPixel)](aurorapixel-jev-browser-use.md) | Jev browser loops for Codex/Claude: warm Chrome daemon, CLI/MCP/extension, host handoffs. | Bun/TypeScript · CLI/MCP/extension (MIT) |
| [jev-chrome-mcp](jev-chrome-mcp.md) | MCP server wrapping jev-browser-use click loop in Google Chrome for Cursor/Codex. | JavaScript · MCP server (MIT) |
| [Jev-cu](jev-cu.md) | Study experimental Jev decisions over macOS Accessibility text in Codex; review the execution-policy limitations before use. | JavaScript · Codex skill and runtime |
| [jev-dom](jev-dom.md) | Drive any web page via DOM action space with TypeSafe Jev—no WebMCP required (Playwright peer). | TypeScript · research package (`jev-dom` 0.1.0, Apache-2.0) |
| [jev-flight-agent](jev-flight-agent.md) | Natural-language flight search in Chrome: TypeSafe Jev picks DOM actions; tiny LLM only types text. | Python · Playwright/CDP agent (MIT) |
| [jev-macos-loop](jev-macos-loop.md) | Automate native macOS GUI apps with local OmniParser/Vision perception and text-only Jev action choice. | TypeScript/Node · Apple silicon CLI |
| [jev-mcp (legostin)](legostin-jev-mcp.md) | Drive real Chrome via MCP: TypeSafe Jev picks elements/actions with calibrated confidence and HITL asks (distinct from jkudish judgment MCP). | TypeScript · MCP server (MIT) |
| [jev-phone](jev-phone.md) | Drive iOS/Android/cloud phones: TypeSafe Jev picks indexed UI actions; phone-use executes. | Bun/TypeScript · phone agent (MIT) |
| [jev-qa (moonshot-partners)](moonshot-partners-jev-qa.md) | Parallel browser QA: TypeSafe Jev-driven acceptance, adversarial, and smoke checks on web changes. | TypeScript · CLI (MIT) |
| [jev-ra](jev-ra.md) | Drive Chrome from Claude Code/Codex/MCP with TypeSafe Jev choosing each operation and target. | Python · MCP server, CLI and PyPI (`jev-ra` 0.1.1) |
| [jev-sim-use](jev-sim-use.md) | Jev-speed mobile UI navigation on sim-use (iOS/Android). | CLI · mobile (MIT) |
| [jevbrief](jevbrief.md) | Filter Playwright elements with drop reasons; Jev Choice picks next click; local JSONL viewer. | Python · PyPI CLI (MIT) |
| [jevdevice](jevdevice.md) | MCP harness for Android (adb) or local shell: TypeSafe Jev (or local Laya) picks one runtime-discovered target per goal; code gates and executes. | Python · MCP server (`jevdevice` 0.1.0) |
| [jevnav](jevnav.md) | Automate browsers with Jev element choice, JSONL traces, risk gates, and offline CI replay. | Python · CLI/PyPI (`jevnav` 0.1.0, Apache-2.0) |
| [JevOnly](jevonly.md) | Drive a browser with pure Jev choices over code-built options—no planner or helper LLM. | Python · CLI, local viewer and Playwright |
| [JevPaper](jev-paper.md) | Mark arXiv abstract claims, delivering body sentences, and caveats with TypeSafe Jev (no summaries). | Chrome MV3 extension (GPL-3.0) |
| [macos-computer-use-kit](macos-computer-use-kit.md) | AX-first macOS computer use (MCP/CLI/pi/DSH) with optional TypeSafe Jev semantic guards before irreversible actions. | Python · PyPI MCP/CLI (MIT) |
| [Midscene JEV Runner](midscene-jev-runner.md) | Drive a caller-owned Playwright page with TypeSafe Jev via OpenRouter Decisions (`runJev` / Midscene `jevAct`). | TypeScript · npm (`@chlrc/midscene-jev-runner` 0.1.2, MIT) |
| [Mobile Jev](mobile-jev.md) | Navigate an Android device and verify a dark-theme task. | JavaScript / React · Mobilerun agent and studio |
| [pi-Jev-browser](pi-jev-browser.md) | Let Jev choose each Playwright browser action over a structured DOM observation inside Pi. | TypeScript · Pi extension (npm) |
| [typesafe-computer-use](typesafe-computer-use.md) | Study OCR and Accessibility driven native macOS control. | Python · desktop CLI |
| [typesafe-computer-use-win](typesafe-computer-use-win.md) | Study OCR/UI Automation driven native Windows control with TypeSafe Jev decisions (`winclicker`). | Python · Windows desktop CLI |

## Customer feedback and marketing

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Jev Internal Links](jev-internal-links.md) | Claude Code skill: crawl sitemap paragraphs, TypeSafe Jev picks useful internal link targets, local rules + report. | Python · Claude Code skill (MIT) |
| [Testimonial miner](testimonial-miner.md) | Find and review verbatim praise in email, grouped by product. | Python · CLI and local dashboard |
| [AnchorLint](anchorlint.md) | Audit internal links in built HTML: deterministic checks plus optional TypeSafe Jev promise/relevance judgments. | Python · CLI (`anchorlint`) |
| [Clay JEV People Ranker](clay-jev-people-ranker.md) | Qualify Clay people-search candidates with TypeSafe Jev Choice/Noul before enrichment (Agent Skill + Python script). | Python · Agent Skill + CLI script (`rank_clay_people.py`) |
| [jev-seo](jev-seo.md) | Local SEO/GEO CLI and MCP: DuckDuckGo SERP/audits plus optional TypeSafe Jev intent and visibility judgments. | Rust · CLI (`jev-seo`) and MCP |
| [jev-seo (AgriciDaniel)](agrici-jev-seo.md) | Live site SEO audit from one URL: crawl/rules/PageSpeed plus TypeSafe Jev judgments; PDF/XLSX/Markdown (distinct from Rust jev-seo). | Python · CLI (`jevseo` 0.1.1, MIT) + Claude skill |

## Developer tools

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [adecider](adecider.md) | CLI/MCP/HTTP/pi surfaces for multi-question System One judgments (local Laya default; optional Jev). | TypeScript · CLI + MCP + HTTP + pi (MIT) |
| [Agent Router](agent-router.md) | Quota-aware Herdr launcher: local eligibility then TypeSafe System One (Jev) picks agent/model/effort. | TypeScript · CLI (`@agent-router/router` 0.1.0) |
| [agent-chaperone](agent-chaperone.md) | Calibrated MCP + hooks firewall: TypeSafe Jev screens tool calls/results with policy thresholds and a shadow log. | TypeScript · npm CLI (`agent-chaperone` 0.3.1, Apache-2.0) |
| [agent-evals](agent-evals.md) | Deterministic agent eval harness: rule scorers plus optional calibrated TypeSafe Jev judge as a CI gate. | TypeScript · npm CLI (`agent-evals` 0.1.0) |
| [agent-fastpath](agent-fastpath.md) | MCP decision layer: rules then TypeSafe Jev for ship/risk/triage/browser gates (files stay out of agent context). | TypeScript · npm CLI (`agent-fastpath` 0.2.0) |
| [agy-jevgate](agy-jevgate.md) | Fail-closed Antigravity PreToolUse hook: fast-pass + static guard + TypeSafe Jev risk score. | Python · agy plugin |
| [AlphaOptimizer](alphaoptimizer.md) | Compact large Codex/tool outputs locally and optionally rank chunks with TypeSafe Jev. | Node.js · TypeScript package (`alphaoptimizer` 0.1.0) |
| [ask-jev-skill](ask-jev-skill.md) | Call TypeSafe Jev as a Hermes typed tiebreaker (Choice/Score/Noul) when multiple paths remain. | Python · Hermes skill + stdlib CLI |
| [askjev](askjev.md) | Ask TypeSafe Jev via MCP (local or hosted) for calibrated Noul/Choice/Score over agent-held context. | TypeScript · MCP server (`askjev` 0.2.0) |
| [Astra-Ares](astra-ares.md) | Adapt GPT-6 Astra reasoning effort mid-Codex-task with TypeSafe Jev Choice (patched Codex CLI preview). | Node.js ≥ 22 · CLI (`astra-ares` / `ares` 0.2.1) |
| [Auto Mode for Paseo](auto-mode-for-paseo.md) | Paseo plugin: TypeSafe Jev (or local Laya) picks Codex model/effort/mode/speed per turn. | TypeScript · Paseo plugin 0.2.0 |
| [beam-cli](beam-cli.md) | Local AgentBeam hooks/policy for coding agents; optional TypeSafe Jev Noul/Score action judging (off by default). | TypeScript · npm CLI (`@agent-beam/beam` 0.2.16, AGPL-3.0) |
| [bitrate-advisor](bitrate-advisor.md) | Choose live-stream encoder bitrate/resolution/next-step with TypeSafe Jev via OpenRouter inside deterministic guardrails. | TypeScript · Deno/Node library (`@affirmi/bitrate-advisor` 0.2.7) |
| [BoundedCode](boundedcode.md) | Local OpenCode coding on 8 GB GPUs with a required TypeSafe Jev decision plane and Go verification gates. | Go · OpenCode supervisor (Apache-2.0) |
| [Cairn Jev Lab](cairn-jev-lab.md) | Test memory-admission policies with TypeSafe Jev judgments and inspectable save/skip/defer recommendations. | Node.js ≥ 22 · lab/CLI/playground (`cairn-jev-lab` 0.1.0) |
| [Canny](canny.md) | Stop Claude Code/Codex “done” claims without ledger evidence; TypeSafe Jev advises, only facts block. | TypeScript · CLI (`canny-warden` 0.1.0), zero runtime deps |
| [chinese-workflow-decision-bench](chinese-workflow-decision-bench.md) | Benchmark Feishu-style Chinese message triage with frozen Choice/four-Noul tracks and published Jev vs Laya results. | Python · bench harness + adapters |
| [Claude x Jev](claude-x-jev.md) | Claude Code skill: Jev classify/route/gate via OpenRouter; Claude deep-reads only unsure items. | Python/npm · Claude Code skill (`claude-x-jev`, MIT) |
| [claude-code-jev](claude-code-jev.md) | Claude Code PreToolUse gate: TypeSafe Jev via OpenRouter Decisions classifies allow/block/ask with fixture benchmarks. | Python · CLI/hook (`jev-auto-mode` 0.1.0) |
| [claude-jev (darwintechlab)](darwintechlab-claude-jev.md) | Claude Code plugin/MCP: live TypeSafe Jev Choice/Noul/Score with auto/escalate confidence labels. | TypeScript · Claude plugin/MCP (MIT) |
| [claude-jev-funnel](claude-jev-funnel.md) | Bulk TypeSafe Jev funnel for Claude Code: resolve confident YES/NO in code; escalate only the uncertain band. | Python · Claude plugin + CLI (Apache-2.0) |
| [claude-router (alexei-led)](alexei-led-claude-router.md) | Local Anthropic gateway: Jev routes micro/low/medium/high tiers for Claude Code. | TypeScript · npm gateway plugin (MIT) |
| [clear-head](clear-head.md) | Claude Code Stop hook: TypeSafe Jev checks answer claims against what was read this session. | Python · Stop hook + install scripts |
| [cmd-mod-jev-nudge](cmd-mod-jev-nudge.md) | Command Code stop-hook mod: TypeSafe Jev judges whether unfinished work warrants a continue nudge. | TypeScript · Command Code mod (`cmd-mod-jev-nudge` 0.1.0) |
| [Codex Jev Preflight](codex-jev-preflight.md) | Fail-open Codex UserPromptSubmit hook: TypeSafe Jev advisory task_type/complexity/risk/execution_mode. | Python · stdlib hook + installer |
| [Codex Jev Router (suenot)](codex-jev-router-suenot.md) | Choose Codex subagent model and reasoning effort with Jev Choice/Noul decisions and local confidence gates. | Node.js · CLI + installer |
| [codex-jev-router](codex-jev-router.md) | Route OpenAI Codex CLI turns through TypeSafe Jev model/effort selection via a local Responses proxy (fail-open). | Node.js · CLI (`codex-jev` 0.1.0) |
| [codex-triage](codex-triage.md) | Local Codex task triage dashboard with human-reviewed archiving and optional TypeSafe Jev analysis. | TypeScript · local app (MIT) |
| [compact-adviser](compact-adviser.md) | Ask TypeSafe Jev whether a coding session is at a safe `/compact` boundary; hint or optional auto-compact on Pi/Claude Code. | Node.js ≥ 22 · npm plugins (`compact-adviser` 0.1.6) |
| [daf-jev](daf-jev.md) | Build typed Jev questions, gates, batch evaluation, and optional MCP tools in Python. | Python · library/CLI (`daf-jev` 0.3.0) |
| [DataJev](datajev.md) | Control a data-analysis agent trajectory with TypeSafe Jev verbs while an LLM analyst and Python execute steps. | Python · CLI/package (`datajev` 0.1.0; Python 3.12 / uv) |
| [dbt_jev](dbt-jev.md) | Classify SQL values with TypeSafe Jev (or OpenRouter→Jev) from dbt macros on DuckDB/ClickHouse. | Python · dbt package + DuckDB/ClickHouse runtime |
| [DecideKit](decidekit.md) | Define typed decision policies and evaluate them with Jev via OpenRouter or TypeSafe, with offline fixtures and fallbacks. | TypeScript/Python · library/CLI (`decidekit` 0.1.0) |
| [decision-first](decision-first.md) | Spot bounded judgments, try TypeSafe Jev first, and log adopt/decline cases for reuse. | Python · agent skill + stdlib scripts |
| [demo-expanso-jev](demo-expanso-jev.md) | Run Expanso Edge pipelines that bypass routine lines and ask TypeSafe Jev only on the rest (boards + mock server). | Demo suite · Expanso YAML, Python boards, `just` recipes |
| [deslop](deslop.md) | Score page bodies with TypeSafe Jev probabilities for ad/slop/seo/derivative (caller sets thresholds). | Python · agent skill + stdlib CLI |
| [Discern](discern.md) | Build Effect Decision/DecisionModel patterns, policies, and procedures; optional TypeSafe Jev provider. | TypeScript · npm (`@doeixd/discern` 0.4.0) |
| [discoprint](discoprint.md) | Classify an artist discography for theme/mood/lyrical complexity with TypeSafe Jev and render an Ink terminal dashboard. | TypeScript · npm CLI (`discoprint` 0.1.0) |
| [Distill](distill.md) | Route coding-agent model/effort and utility/retention choices with TypeSafe Jev (or OpenRouter decisions) inside a local TUI harness. | Rust · coding agent CLI/TUI (Distill 2.0) |
| [doc-router](doc-router.md) | Select which PDF pages need OCR using optional Jev judgments, then merge local extraction and provider results. | Rust · library and CLI, Python bindings |
| [DocJev](docjev.md) | Classify or split PDF/DOCX/PPTX packets with LiteParse text and TypeSafe Jev category/boundary judgments. | Python · CLI/library (`docjev`, Apache-2.0) |
| [dsh-jev](dsh-jev.md) | Register `jev_ask` on DeepSeek Harness so agents can send typed noul/choice/score questions to TypeSafe Jev (install from GitHub pin). | TypeScript · DSH plugin (`dsh-jev` 0.1.0) |
| [dsh-jev-context-gate](dsh-jev-context-gate.md) | DeepSeek Harness preflight + evidence-aware review/skill gates via TypeSafe Jev. | JavaScript · DSH plugin (MIT) |
| [dsh-jev-decide](dsh-jev-decide.md) | Register DSH agent tool `jev_decide` for TypeSafe Jev noul/choice/score over text state (distinct from dsh-jev / verify / prune). | TypeScript · npm plugin (`dsh-jev-decide` 0.1.1) |
| [dsh-jev-interceptor](dsh-jev-interceptor.md) | DeepSeek Harness: Jev risk classification on tool calls plus optional semantic session-reference retention. | TypeScript · DSH plugin (MIT) |
| [dsh-jev-kit](dsh-jev-kit.md) | DeepSeek Harness plugin: ~23 named TypeSafe Jev advisory judgments (privacy scan, scope, memory/batch triage) without hooks. | TypeScript · DSH plugin (`@dsh-external/dsh-jev-kit` 0.13.0) |
| [dsh-jev-prune](dsh-jev-prune.md) | Replace DSH size-only pruning and model summaries with TypeSafe Jev keep/drop judgments plus deterministic receipts. | JavaScript · DSH plugin (`dsh-jev-prune` 0.1.0) |
| [dsh-jev-verify](dsh-jev-verify.md) | Call TypeSafe Jev choice/score/noul from DSH and run a live labeled verification benchmark (honest, no mock mode). | JavaScript · DSH plugin (`dsh-jev-verify` 0.1.0) |
| [Eutrya](eutrya.md) | Run a CLI agent loop where TypeSafe Jev picks attention modes and scores candidates; text model proposes; offline demo included (alpha). | Node.js · CLI (`eutrya` 0.4.9) |
| [ExcelPilot](excelpilot.md) | Drive live Excel workbooks with Qwen planning and TypeSafe Jev intent/tool gates (cascade to OpenRouter/offline). | Python · Office.js add-in + FastMCP agent (`excelpilot` 1.0.0) |
| [fast-jev-compaction](fast-jev-compaction.md) | Select which old tool calls and results remain in agent context. | TypeScript · library and Claude Code plugin |
| [fast-jev-opencode](fast-jev-opencode.md) | Prune stale OpenCode V2 tool calls/results on the outgoing request with TypeSafe Jev (fail-open; does not rewrite history). | TypeScript · OpenCode plugin (`fast-jev-opencode` 0.1.0) |
| [Foreman](foreman.md) | Experiment with Jev supervision of Codex workers and inspect steering, retry, and verification decisions. | Python · CLI and supervision runtime |
| [Formanator](formanator.md) | Submit Forma benefit claims from CLI/MCP; optional TypeSafe Jev picks benefit/category (receipt LLM separate). | Rust · CLI/MCP (`formanator` 5.4.0) |
| [Gatekeeper](gatekeeper.md) | Route Claude Code prompts to the right skill/agent with YAML rules plus TypeSafe Jev Choice verdicts. | Python · Claude Code hooks (MIT) |
| [ghtriage](ghtriage.md) | Classify GitHub issues with TypeSafe Jev typed labels/confidence and code-owned write guards (`ghtriage`). | Python · CLI (`ghtriage` / `jev-issue-classifier` 0.1.0) |
| [git-jev-stage](git-jev-stage.md) | Classify Git hunks against a plain-language staging intent with TypeSafe Jev, then stage confirmed blocks. | TypeScript · CLI (`git-jev-stage` 0.1.1) + skill |
| [Graphlin](graphlin.md) | Live architecture/activity diagrams for Claude Code or Codex; optional TypeSafe Jev classification of graph evidence. | Node.js · CLI/viewer (`npx graphlin`), plugins |
| [Grok Bot Jev](grok-bot-jev.md) | Gate Grok Bot research/browser/retry/subagent work with TypeSafe Jev actions (shadow or active skill mode). | Python · router, skill template and dry-run CLI |
| [grok-jev-guard](grok-jev-guard.md) | Prefight Grok Bot tool sequences: local hard rules + TypeSafe Jev ambiguity judgments (shadow-first). | Python · CLI + skill (`grok-jev-guard` 0.1.0, MIT) |
| [HearMemory](hearmemory.md) | Share project memory across coding agents; TypeSafe Jev judges claims against tests/diffs/commits. | Python · MCP/hooks (MIT) |
| [HekaJev](hekajev.md) | Ask reproducible Git-history analytics questions; TypeSafe Jev classifies commits with saved evidence/cost. | Python · CLI (`hekajev`, MIT) |
| [Hermes Jev Skills](hermes-jev-skills.md) | Add Jev model routing, memory filter, compaction, skill pick, triage, and computer/browser choices to Hermes, Claude Code, and Codex. | Python · skills, `jev` CLI and Hermes plugin |
| [hermes-jev-curator](hermes-jev-curator.md) | Typed Jev skill-relationship judgments and safe archive/guard plans for Hermes Agent’s background skill curator. | Python · Hermes plugin (experimental 0.1.0) |
| [hermes-jev-helper](hermes-jev-helper.md) | Hermes `pre_llm_call` plugin: TypeSafe Jev (OpenRouter Decisions) classifies intent route before the agent improvises. | Python · Hermes plugin (MIT) |
| [himalaya-jev-mail-classify](himalaya-jev-mail-classify.md) | CLI `mail-classify`: himalaya Gmail threads → TypeSafe Jev labels/colours via OpenRouter (dry-run default). | Python · CLI (`mail-classify` 0.1.0, MIT) |
| [hookgate](hookgate.md) | Gate Claude Code/Codex shell and Stop hooks with TypeSafe Jev (audit mode, fail-open). | Node.js ≥ 18 · CLI/plugin (`hookgate` 0.0.2) |
| [Intent-Router](intent-router.md) | Compile vague agent requests into typed IntentSpec contracts (probe, ask, or halt) before Jev/Laya routing. | Agent Skill (`intent-router` 0.3.0, MIT) |
| [invalidate](invalidate.md) | Check every stored agent memory against new evidence with TypeSafe Jev; mark superseded facts without rewriting text. | Python · library, CLI and memory adapters |
| [is-malicious](is-malicious.md) | Scan a codebase for deceptive or data-stealing behavior with TypeSafe Jev file/line findings. | TypeScript · npm CLI (`is-malicious` 0.1.0) |
| [J++](jpp.md) | Experimental language/Rust runtime composing Jev questions with exact methods; offline fixtures and Towow demos. | Rust · `jpp-cli` + Python reference |
| [japanese-jev-lint](japanese-jev-lint.md) | Lint Japanese prose with TypeSafe Jev Noul flags (typo/twist/length/repeat) plus regex です/ます checks; no rewrites. | Go · CLI (`jjl`) |
| [JCR](jcr.md) | Resolve deterministic commands from a nested capability tree with TypeSafe Jev (MCP + Claude/Codex harnesses). | TypeScript · resolver, MCP and harnesses (`jcr` 1.0.0) |
| [Jev Atlas](jev-atlas.md) | Map a repo’s semantic decisions, reject weak Jev fits with published gates, then validate/implement survivors from `.jev-atlas/` state. | Agent skill + Claude/Codex plugin (`jev-atlas` 0.2.0) |
| [Jev Checkpoint](jev-checkpoint.md) | Ask TypeSafe Jev for an advisory, confidence-gated next-step route over a fixed Choice set (MCP; never executes). | TypeScript · local MCP server (`jev-checkpoint` 0.1.0) |
| [Jev Code Reviewer (egma-ai)](egma-ai-jev-code-reviewer.md) | Local Jev priority + OpenAI NL review overlay for GitHub PRs. | Node · CLI/extension (MIT) |
| [JEV Flaky Detective](jev-flaky-detective.md) | Jev classifies CI test failures without masking or auto-rerun. | TypeScript · Action (MIT) |
| [Jev Flow](jev-flow.md) | Standalone studio for typed Jev workflows (Studio, Compendium, Battle Arena, labs). | Node.js · app (MIT) |
| [Jev Gatehouse (Kinde)](jev-gatehouse.md) | Kinde who/what plus Jev typed gate before each MCP tool call (allow/step-up/stop). | TypeScript · Convex starter (MIT) |
| [Jev GitHub Action](jev-action.md) | Install pinned Jev CLI in Actions; run typed judgments on event/JSON; expose answers (no issue mutation). | GitHub Action (Apache-2.0) |
| [Jev Logs](jevlogs.md) | Prioritize logs for deeper analysis alongside your archive. | TypeScript · library, CLI and OpenTelemetry integration |
| [Jev Model Router](jev-model-router.md) | Route Claude Code subagent models and main-conversation reasoning effort using Jev assessments; requires early-access function hooks. | TypeScript · Claude Code mod |
| [JEV Reasoning Navigator](jev-reasoning-navigator.md) | Supervise agents: TypeSafe Jev semantic judgment ≠ PolicyEngine ≠ capability receipts ≠ sandboxed execution. | Python · middleware runtime (license unspecified) |
| [Jev Review](jev-review.md) | Add experimental quality judgments to a coding agent's review loop. | Node.js · MCP server |
| [Jev Review (Dev Agrawal)](jev-review-devagrawal.md) | Screen JavaScript/TypeScript diffs or codebases and inspect staged review findings. | TypeScript · CLI and local dashboard |
| [Jev Review Action](jev-review-action.md) | Review catalog submissions or PR diffs with TypeSafe Jev only; one template PR comment (GitHub Action). | Node.js · GitHub Action (`jev-review-action` 0.2.0) |
| [Jev Runway](jev-runway.md) | Local Codex proxy: TypeSafe Jev keeps needed tool output and trims the rest between turns. | TypeScript · npm CLI (`jev-runway`, MIT) |
| [Jev Score](jev-score.md) | Score document revisions against criteria with TypeSafe Jev (OpenRouter Decisions) and keep revision history. | Node.js · CLI + local web UI (`jev-score` 1.0.0) |
| [Jev Sift](jev-sift.md) | Screen candidate content before reading it into agent context; requires a TypeSafe key, with upstream licensing unspecified. | Node.js · MCP server and agent plugin |
| [Jev the Janitor](jev-the-janitor.md) | Ask TypeSafe Jev to vote on markdown vault notes; code adds frontmatter or quarantines secrets (dry-run default; offline mode). | Python · CLI (`jev-janitor` 0.1.1) |
| [Jev Trader](jev-trader.md) | Study Jev market-direction choices, simulated fills, and on-chain order execution through a Bun trading experiment. | TypeScript / Bun · trading reference and dashboard |
| [Jev WCAG Auditor](jev-wcag-auditor.md) | Audit public URLs with axe-core plus optional TypeSafe Jev judgement-call adjudication and uncertainty band. | Next.js · web app (`jev-wcag-auditor` 0.1.0, MIT) |
| [jev-agent-browser](jev-agent-browser.md) | Confidence-gated next browser action for `agent-browser` via TypeSafe Jev (or Gateway/Cloudflare/custom). | TypeScript · npm (`@mhingston5/jev-agent-browser` 0.3.1) |
| [jev-agent-failure-benchmark](jev-agent-failure-benchmark.md) | Score TypeSafe Jev on Who&When Pro text traces for responsible agent, step, and error type; compare to paper LLMs. | Python · CLI (`jevbench`, Apache-2.0) |
| [jev-agent-kit](jev-agent-kit.md) | Zero-dependency CLI + MCP tools (check/choose/score/judge/route/triage/guard/grep/rank/compact) on TypeSafe Jev — distinct from the Rust jevkit CLI. | Node.js ≥ 18 · npm (`@walidboulanouar/jevkit` 0.2.0) |
| [jev-ai-use-cases (atliq)](atliq-jev-ai-use-cases.md) | LangChain notebook: TypeSafe Jev triage/routing/guards/tool-select/finance checks. | Jupyter · langchain-typesafe (MIT) |
| [jev-align](jev-align.md) | Build calibrated classifiers/AI Functions from human feedback with TypeSafe Jev + GEPA (`jeva`). | Python · CLI (`jev-align` / `jeva`) |
| [jev-backend-qa](jev-backend-qa.md) | Audit backend surfaces then PAL/Jev risk adjudication to BLOCK/WARN/PASS (CLI + Action). | Python · CLI/Action + Node bridge (MIT) |
| [jev-blindspot](jev-blindspot.md) | Claude Code / Codex side panel: Jev gate then optional blind-spot analysis without editing the session. | TypeScript · npm CLI/hooks (MIT) |
| [jev-calibrate](jev-calibrate.md) | Calibrate Jev questions against labelled examples; per-question gate/ranker/unusable verdicts. | TypeScript · npm CLI (`jev-calibrate` 0.1.11) |
| [jev-certify](jev-certify.md) | Turn Jev probabilities into conformal routing certificates and PPI audits (offline math + OpenRouter Decisions client). | Python · CLI/library (`jev-certify` 0.1.0) |
| [jev-ci-pathfinder](jev-ci-pathfinder.md) | Select allowlisted CI jobs after a change with TypeSafe Jev; deterministic allowlist + dependency closure. | TypeScript · GitHub Action (MIT) |
| [jev-ci-selector](jev-ci-selector.md) | Select which described CI jobs apply to a PR diff with TypeSafe Jev (shadow or enforce). | Node.js · GitHub Action (`jev-ci-selector` 0.1.0) |
| [jev-claude-code (DarioFontanel)](dariofontanel-jev-claude-code.md) | Paste-in Claude Code prompts for TypeSafe Jev model routing, context compaction, and 14-question diff review. | Markdown prompts (MIT) |
| [jev-claude-router (Flam1ngFir3ball)](jev-claude-router.md) | Claude Code plugin: Jev picks tier/effort with cost-aware switches and optional Jev compaction. | TypeScript · Claude Code plugin (MIT) |
| [jev-claw](jev-claw.md) | OpenClaw `jev_route` tool: TypeSafe Jev classifies task type/complexity/risk; code applies routing policy. | OpenClaw plugin (MIT) |
| [jev-cloud-cost-guardian](jev-cloud-cost-guardian.md) | FinOps CI gate: Jev scores proposed cloud spend vs budget; policy never hides cost lines. | TypeScript · GitHub Action (MIT) |
| [jev-cmdline-classifier](jev-cmdline-classifier.md) | Classify shell commands with TypeSafe Jev Choice (`allow`/`prompt`/`forbidden`) plus fail-closed local rules for agent skills. | Python/JS skill + CLI (`jev-command-classifier` 0.1.0) |
| [jev-codex-router](jev-codex-router.md) | Route each Codex turn's model and thinking depth with Jev via a Codex Router generic provider. | Python · local server and Codex Router integration |
| [jev-codex-token-saver](jev-codex-token-saver.md) | Gather local workspace/log evidence and let TypeSafe Jev select exact excerpts for Codex (MCP plugin; local fallback). | Node.js · Codex plugin + MCP (`jev-codex-token-saver` 0.3.2) |
| [jev-compact](jev-compact.md) | Score Codex tool calls with TypeSafe Jev before compaction and re-inject critical outputs the summary dropped. | TypeScript · Codex plugin (`jev-compact` 0.1.0) |
| [jev-compaction (Waxmell114514)](waxmell114514-jev-compaction.md) | Score-only context compaction so memory cannot hold facts absent from the transcript (offline demo). | Python · library/demo (MIT) |
| [jev-debtgate](jev-debtgate.md) | Gate agents/CI on technical-debt risk with TypeSafe Jev over local git/file metrics. | Node.js · CLI/MCP/Action (`jev-debtgate` 0.3.0) |
| [jev-effort](jev-effort.md) | Claude Code: TypeSafe Jev picks per-step reasoning effort + lease (OpenRouter/TypeSafe/Vercel). | Node.js · hooks/setup (MIT) |
| [jev-effort-router](jev-effort-router.md) | Hermes on Ollama:Cloud: TypeSafe Jev picks model **and** reasoning effort per turn and rewrites `llm_request`. | Python · Hermes plugin (`hermes-plugin-jev-effort-router` 0.2.1, MIT) |
| [jev-evolve](jev-evolve.md) | Evolve agent policies with typed Jev decisions and measure how much improvement is selection luck. | Python · library (`jev-evolve` on PyPI) |
| [jev-eyes](jev-eyes.md) | Turn images into inspectable OCR/layout `state` for TypeSafe Jev locally (`see`/`ask`, CLI, optional MCP). | Python · library/CLI/MCP (`jev-eyes` 0.1.0) |
| [jev-for-all](jev-for-all.md) | Shared System One decision contract: Jev picks skill/tool subset/browser moves for OpenCode/Claude Code/Hermes. | TypeScript · OpenCode plugin + adapters (MIT) |
| [jev-fuse](jev-fuse.md) | Governed System One proxy: policy actions, AST guards, singleflight, and WAL audit for TypeSafe Jev/local Laya. | Python · proxy/PyPI (`jev-fuse`, Apache-2.0) |
| [jev-gates](jev-gates.md) | Compose three-valued TRUE/FALSE/UNKNOWN circuits from TypeSafe Jev judgments plus exact rules (auditable traces). | TypeScript · library/CLI (`jev-gates` 0.1.0) |
| [jev-gateway](jev-gateway.md) | Let Jev choose each tool call for Codex, Claude Code, OpenCode, or Gemini through a local LLM gateway. | TypeScript · npm launchers and dashboard |
| [jev-git-graph](jev-git-graph.md) | Evidence-backed TypeSafe Jev relationship graph for Git branch/worktree/PR consolidation (read-only default). | Python · CLI (Apache-2.0) |
| [jev-guard](jev-guard.md) | Risk-score coding-agent tool calls with TypeSafe Jev (deny/ask/allow), flag injection in results, and scan skills across many agents. | Node.js · npm CLI/hooks (`jev-guard` 0.3.1) |
| [jev-guard (CMaintz)](cmaintz-jev-guard.md) | Framework-agnostic allow/block/hold tool-call guard with TypeSafe Jev + LangChain/Vercel adapters (distinct from leepokai jev-guard). | TypeScript · library (`jev-guard` 0.1.0, MIT) |
| [jev-guard (klauswg)](klauswg-jev-guard.md) | Exchange deposit/withdrawal risk triage: TypeSafe Jev answers; Java hard rules and gates decide (distinct from coding-agent jev-guard). | Java · Spring Boot demo (MIT) |
| [jev-guard (muratcakmak)](muratcakmak-jev-guard.md) | Claude Code hooks: regex + TypeSafe Jev rules deny bad edits/deploys; fail-open if scorer down (distinct from leepokai/CMaintz). | TypeScript · Claude Code plugin (MIT) |
| [jev-guardbench](dfranco-projects-jev-guardbench.md) | Benchmark whether System One (Jev/Kev) can replace LLM-as-judge in agent guardrail callbacks. | Python · uv package (license unspecified) |
| [jev-guardrails (deepansh-saxena)](deepansh-saxena-jev-guardrails.md) | Compare LLM-as-judge vs TypeSafe Jev on identical 25 guardrail rules for a mock support agent (cost/latency/calibration). | Python · LangChain/LangGraph eval (license unspecified) |
| [jev-harness](jev-harness.md) | Map TypeSafe Jev answers to actions with confidence gates, shadow mode, recipes, and an eval CLI. | TypeScript · npm library/CLI (`jev-harness` 0.1.0) |
| [jev-harness (TypeSafeAI)](typesafeai-jev-harness.md) | Research proposal-review contract: LLM proposes, Jev answers four narrow questions, code emits host evidence (distinct from AntonioCoppe/jev-harness). | TypeScript · source-only (`jev-harness` 0.0.0, MIT) |
| [jev-healthcare-lab](jev-healthcare-lab.md) | Open Jev vs DeepSeek comparison on 96 healthcare tasks / 12 scenarios (quality/latency/cost). | Python · research lab (MIT) |
| [jev-in-codex](jev-in-codex.md) | Rank Codex capabilities, search hits, and output excerpts with TypeSafe Jev via local MCP. | TypeScript · MCP server + Codex plugin (0.1.0) |
| [jev-issue-radar](jev-issue-radar.md) | Find duplicate/related GitHub issues with TypeSafe Jev evidence choices in a local read-only dashboard. | Node.js · loopback server + static UI (0.1.1) |
| [jev-judge-mcp (PyModel)](pymodel-jev-judge-mcp.md) | MCP typed judgment tools (verify/screen/find/classify/rerank/decide/…); policy owns auto/review/escalate. | Python · MCP (`jev-mcp-python`, MIT) |
| [jev-layer](jev-layer.md) | Route harness capability choices with receipts/replay; host keeps execution (demo/OpenRouter/TypeSafe). | TypeScript · CLI, MCP and harness installers (`jev-layer` 0.1.0) |
| [jev-lint](jev-lint.md) | Ast-grep selects subjects; TypeSafe Jev Noul scores one-sentence semantic rules (distinct from huntedman/JevLint). | TypeScript · npm CLI (`jev-lint` 0.4.1) |
| [jev-linter-action](jev-linter-action.md) | Gate CI on yes/no TypeSafe Jev review questions over selected repo files (thresholds in `.jev-lint.json`). | Node.js · GitHub Action (`jev-linter-action` 1.0.0) |
| [jev-loop (King4s)](king4s-jev-loop.md) | Build loop where TypeSafe Jev decides and Claude Code/Hermes executes (MCP + skill; ≠ lvzhaobo/jev-loop). | Python · MCP/skill (MIT) |
| [Jev-Mem](jev-mem.md) | Control agentic memory admission/linking/retrieval with TypeSafe Jev over a multi-view graph. | Python · library/CLI (`jev-mem` 0.1.0) |
| [jev-oas-sentinel](jev-oas-sentinel.md) | Compare OpenAPI specs with structural diffs plus TypeSafe Jev semantic contract questions. | Python · CLI (`jev-oas-sentinel`) |
| [jev-ood-calibration](jev-ood-calibration.md) | Independent calibration study of TypeSafe Jev with published raw dumps: public benches plus 900 OOD synthetic support tickets. | Node/Python · research scripts + committed results |
| [jev-opus](jev-opus.md) | Re-pick Claude Opus 5.5 effort each step with TypeSafe Jev without breaking the prompt cache. | Node.js · CLI + Claude Code plugin (`jev-opus` 0.3.0, MIT) |
| [jev-packs](jev-packs.md) | Evidence-gated registry of Jev question packs with golden cases and an offline multi-backend scoreboard. | Pack data + Python scripts (CC0-1.0) |
| [jev-pii-checker](jev-pii-checker.md) | Scan text/files for PII with TypeSafe Jev presence/sensitivity judgments plus regex and segmentation layers. | TypeScript/Bun · CLI (`@coo-quack/jev-pii-checker` 0.3.1) |
| [jev-pilot (Akramovic1)](akramovic1-jev-pilot.md) | Claude Code plugin: TypeSafe Jev routes effort, subagent model, strategy advice, and one skill per prompt. | TypeScript · Claude Code plugin (`jev-pilot` 0.4.4, MIT) |
| [jev-playwright (arthurfiorette)](arthurfiorette-jev-playwright.md) | Jev-powered Playwright test selection from changed files. | TypeScript · Playwright (MIT) |
| [jev-pr-judge](jev-pr-judge.md) | Typed PR verdicts with one parallel TypeSafe Jev call, TypeScript policy, Next.js UI, and GitHub Action sticky comments. | TypeScript · Next.js app and Action |
| [jev-pr-profiler](jev-pr-profiler.md) | GitHub Action: TypeSafe Jev PR risk profile + review-depth outputs (never merges alone). | TypeScript · GitHub Action (MIT) |
| [jev-pref](jev-pref.md) | Turn AGENTS.md preferences into a TypeSafe Jev semantic linter for coding-agent diffs (setup/review/tune + Action). | TypeScript · npm (`jev-pref` 0.4.1) |
| [jev-preflight](jev-preflight.md) | Score eight risk axes on a Claude Code turn diff with one TypeSafe Jev request; optional assist reinspection. | Go · Claude Code plugin (v0.1.0) |
| [jev-project-context](jev-project-context.md) | Keep evidence-first experiment memory for coding agents; optional TypeSafe Jev triage on doctor/context loads. | Agent skill + stdlib Python scripts |
| [jev-pruner](jev-pruner.md) | Prune eligible Bash stdout with Jev before Claude Code or an opt-in Codex wrapper returns it to the model. | TypeScript · library, Claude Code plugin and Codex wrapper |
| [jev-reflex (xnuonux)](jev-reflex-xnuonux.md) | Portable Jev decision sidecar: MCP/CLI/pi recipes with durable budgets and source-bound context plans. | Python · MCP/CLI (`jev-reflex`, MIT) |
| [jev-router](jev-router.md) | Route Claude Code and Codex turns through Jev model selection and inspect stored routing exchanges. | JavaScript · CLI launchers and HTTP proxies |
| [jev-router (Ex8-ca)](ex8-ca-jev-router.md) | Hermes Jev skill router + session-start pre-route. | Python · plugin (MIT) |
| [jev-rules](jev-rules.md) | Select project rules and codebase-map documents for Claude Code prompts and file changes. | JavaScript · Claude Code plugin |
| [jev-sap-commerce](emenowicz-jev-sap-commerce.md) | SAP Commerce extension: TypeSafe Jev review moderation + category suggestions (dry runs, audits). | Java · Commerce extension (Apache-2.0) |
| [jev-seatbelts](jev-seatbelts.md) | Seven Claude Code hooks catching expensive agent mistakes; TypeSafe Jev on judgment tiers. | Python · Claude hooks (MIT) |
| [jev-sec-bench](jev-sec-bench.md) | Run or browse blind TypeSafe Jev prompt-injection and vulnerable-code benchmarks (jev-go + results TUI). | Go · CLI/TUI |
| [jev-security-prioritization](jev-security-prioritization.md) | Jev vs severity baselines for SCA/SAST triage. | Python · research (MIT) |
| [jev-security-sentinel](jev-security-sentinel.md) | Security CI gate over SAST/SCA/IaC/secrets/container findings via TypeSafe Jev; findings stay visible. | TypeScript · GitHub Action (MIT) |
| [jev-shell-history](jev-shell-history.md) | Recall zsh history commands with optional acceptance of Jev-ranked inline suggestions; selected history is sent to TypeSafe. | TypeScript / zsh · shell plugin and CLI |
| [jev-shield](jev-shield.md) | Semantic MCP firewall: screen tool calls/results/descriptions with TypeSafe Jev via Vercel AI Gateway. | Node.js · CLI, MCP wrap, opt-in hooks (`jev-shield` 0.1.0) |
| [jev-skill-gate](jev-skill-gate.md) | Score Claude Code skills with TypeSafe Jev and write `skillOverrides` so only relevant skills reach context. | Node.js · CLI (`jev-skill-gate` 0.2.0) |
| [jev-skill-router-bench](jev-skill-router-bench.md) | Independent reproducible scorecard of a Jev skill router on an 84-skill Hermes roster (81 labelled turns). | Python · bench artifacts + scripts |
| [jev-skill-scout](jev-skill-scout.md) | Audit Claude Code skill misses with TypeSafe Jev; optional live mod suggests a skill without changing the roster. | Node.js ≥ 20 · npm CLI/mod (`jev-skill-scout` 0.1.0) |
| [jev-skills](jev-skills.md) | Claude Code/Codex plugin: TypeSafe Jev picks which skills enter context each turn (0 always-on skill-list tokens). | TypeScript · Claude Code/Codex plugin (MIT) |
| [jev-suite](jev-suite.md) | Four Java decision-quality apps on one Jev kernel: structured questions; code keeps thresholds/vetoes. | Java · Maven suite (`jev-suite` 0.1.0, MIT) |
| [jev-support-agents](jev-support-agents.md) | FastAPI support orchestrator: LLM specialists write text; TypeSafe Jev routes and evaluates with retry/escalation. | Python · FastAPI + Ollama reference (MIT) |
| [jev-swap](jev-swap.md) | Find LLM→Jev decision swaps; shadow-test on traffic. | Node · CLI (MIT) |
| [jev-switchboard](jev-switchboard.md) | Gate cross-agent messages with TypeSafe Jev: interrupt vs drop plus selected evidence injection. | Node.js ≥ 20 · CLI/hooks (`jev-switchboard` 0.1.0) |
| [jev-table](jev-table.md) | Add TypeSafe Jev AI columns to CSV/JSONL with confidence, review queue, resume, and dry-run cost preview. | Python · CLI (`jev-table` 0.1.1, Apache-2.0) |
| [jev-test-filter](jev-test-filter.md) | Score repository tests against a git diff with TypeSafe Jev and emit runner-native filter arguments. | TypeScript · npm CLI (`jev-test-filter` 0.1.0; Node ≥ 24) |
| [jev-test-impact](jev-test-impact.md) | Select Vitest/Jest tests impacted by a Git diff using static deps plus optional TypeSafe Jev scoring. | TypeScript · npm CLI + GitHub Action (MIT) |
| [jev-toolkit](jev-toolkit.md) | Serve TypeSafe Jev asks/verify/review over MCP plus CLI triage, audit, skill routing, and local impact metrics. | TypeScript · CLI/MCP (`jev`, Effect; Node ≥ 26) |
| [jev-tree](jev-tree.md) | Recursive TypeSafe Jev Choice over a JSON taxonomy when a flat list exceeds the 255-option cap. | TypeScript · npm (`jev-tree` 0.1.0) |
| [jev-triage](jev-triage.md) | GitHub Action: label issues with TypeSafe/Cloudflare Jev typed answers; low confidence escalates to needs-human. | TypeScript · Action (`cmaintz/jev-triage@v0`, MIT) |
| [jev-use (shitianfang)](jev-use.md) | Route the no-text steps of a Claude Code, Codex or pi loop to Jev, with an opt-in PreToolUse gate and typed handbacks to the LLM. | TypeScript · MCP server, CLI and agent plugin |
| [jev-verify (stillmarcus24)](stillmarcus-jev-verify.md) | Audit published Jev answers against the Yurin confidence identity; flag fixture violations. | JavaScript · CLI (MIT) |
| [Jev_validation_agent](jev-validation-agent.md) | Python Jev Guard validating agent outputs via TypeSafe Jev with reports and a local demo UI. | Python · package + demo (MIT) |
| [jeval](jeval.md) | Measure classifier confidence calibration and set cost-optimal human hand-off thresholds (Jev-motivated, provider-neutral). | Python · CLI (`jeval` 0.1.0, Apache-2.0) |
| [jevals](jevals.md) | Author and run TypeSafe Jev Noul/Choice/Score evaluations locally; compare saved results in a browser workbench. | TypeScript · local server/UI (`jevals` 0.1.1) |
| [Jevals.com](jevals-com.md) | Hosted independent Jev vs LLM boards (accuracy/calibration/cost/latency); open data, private harness (distinct from local jevals). | Hosted boards + [jevals-data](https://github.com/Jevals/jevals-data) (CC BY 4.0) |
| [Jevaluate](jevaluate.md) | Confidence-gated web walkthroughs with TypeSafe Jev; optional DeepSeek vision; eval/judge scripts and skill. | Node/Python · Playwright scripts (MIT) |
| [jevbus](jevbus.md) | Route/subscribe/deliver streaming events with TypeSafe Jev (or any Judge) and policy thresholds. | Rust · crate (`jevbus` 0.1.0) |
| [jevc](jevc.md) | Compile agent rules/JSON Schema into TypeSafe Jev programs (typed questions + code reducers) with offline fixture checks. | TypeScript · npm CLI (`jevc` 0.1.0, Apache-2.0) |
| [jevcache](jevcache.md) | Reuse chat completions when TypeSafe Jev (via OpenRouter) admits paraphrased prompts as same-intent. | TypeScript · OpenAI-compatible proxy CLI (`@kushalicious/jevcache` 0.1.5) |
| [jevcompat](jevcompat.md) | Spec + conformance suite for Jev-compatible `/v1/systemone` servers (proxy, mock, Action). | Python · suite + GitHub Action (MIT) |
| [JevCore Agent](carter1111-jevcore.md) | Coding harness: TypeSafe Jev classifies task/risk/mode; hard-policy Guard; MCP + `npx jevcoreagent`. | JavaScript · npm CLI/MCP (Apache-2.0) |
| [jevdev](jevdev.md) | Rust coding-agent harness centered on TypeSafe Jev System One (HTTP or local transport). | Rust · crate/CLI (Apache-2.0) |
| [jeveloper](jeveloper.md) | Claude Code System-1 reflex layer: TypeSafe Jev route/gate/verify/done plus optional driver mode. | Claude Code plugin (`jeveloper` 0.2.0, MIT) |
| [JeVerifier](jeverifier.md) | Jev reading lists + doc/code checks under Claude sessions. | Python · harness (MIT) |
| [jevernetes](jevernetes.md) | Tail and triage Kubernetes logs with optional TypeSafe Jev analysis, local review rules, and coding-agent prompts. | Python · CLI/dashboard (`jevernetes`, Apache-2.0) |
| [jevgate (craxrev)](craxrev-jevgate.md) | Claude Code Bash/Write gate from Jev risk facts with allow/ask/deny rules. | TypeScript · Claude Code plugin (MIT) |
| [JevGuard](jevguard.md) | Enforce CLAUDE.md/AGENTS.md-derived rules on Claude Code/Codex via TypeSafe Jev PreToolUse/Stop hooks (distinct from jev-guard risk firewall). | TypeScript · Claude/Codex plugin (`jevguard` 0.1.0) |
| [JevGuard (blacksinisterx)](blacksinisterx-jev-guard.md) | Hard-rule prefilter then Jev allow/review/block between agent and tools (mock-first). | TypeScript/Python · FastAPI + Vite demo (no LICENSE) |
| [jevkit](jevkit.md) | Ask TypeSafe Jev from a Rust CLI and lint question sets offline before spending on inference. | Rust · CLI (`jevkit` 0.3.0, rustc ≥ 1.88) |
| [JevLang (TimMikeladze)](timmikeladze-jevlang.md) | Declare routes/gates/actions once; Jev answers only needed questions; signed journal replay. | TypeScript/Python · library `jevlang` (MIT) |
| [JevLangGraph (blacksinisterx)](blacksinisterx-jev-langgraph.md) | LangGraph loop where Jev—not an LLM—chooses the next branch action (mock-first). | TypeScript/Python · FastAPI + Vite demo (no LICENSE) |
| [jevlens](jevlens.md) | Run labeled Choice/Noul/Score evals, store full distributions, calibrate thresholds, and optionally dashboard or CI-gate. | Python · CLI (`jevlens` 0.1.0) + optional Streamlit/Action |
| [JevLint](jevlint.md) | Lint source against plain-English conventions with file-level TypeSafe Jev Noul judgments (magic-strings, descriptive-names). | TypeScript · npm CLI (`@jevlint/cli`) |
| [jevmem](jevmem.md) | Shared JEVMEM.md memory across Claude Code/Cursor/Codex; TypeSafe Jev gates what to save. | Node.js · CLI/hooks/MCP (`jevmem` 0.4.2, MIT) |
| [jevmetrics](jevmetrics.md) | Assess unfamiliar OTel metrics for retention with TypeSafe Jev, then apply deterministic keep/reduce policy. | Go · OpenTelemetry Collector processor (0.1.0-dev alpha) |
| [jevmod](jevmod.md) | Moderation CLI/SDK/API/MCP and optional chat bots with per-category TypeSafe Jev probabilities and owned thresholds. | Python · `jevmod` 0.2.1 (MIT) |
| [jevmory](jevmory.md) | Build quote-backed agent memory with TypeSafe Jev grading and audit MEMORY.md with receipts. | Python · CLI (`jevmory`) + Claude/Codex hooks |
| [JevRepoTriage](jevrepo-triage.md) | Self-hosted GitHub issue/PR triage with TypeSafe Jev classifications and operator-approved actions. | TypeScript · web UI + workers (MIT) |
| [JevRouter](jevrouter.md) | Route among models/subagents/skills/MCP/CLIs with TypeSafe Jev Choice plus permissions, risk, confirmation, and receipts. | TypeScript · SDK/CLI/MCP (`jevrouter` 0.1.0) |
| [JevScope](jevscope.md) | Edit Jev projects visually, batch JSONL regression cases, and compare definitions locally. | TypeScript · Studio + local API (pnpm) |
| [jevseek](jevseek.md) | Let DeepSeek propose tokens and TypeSafe Jev (OpenRouter System One) choose the next one. | Python ≥ 3.11 · CLI (`jevseek` 0.1.0) |
| [JevShield](jevshield.md) | Wrap Python/LangChain tool calls with a TypeSafe Jev dual-factor risk gate and keyless local heuristic fallback. | Python · library/PyPI (`jevshield`, Apache-2.0) |
| [jevskillz](jevskillz.md) | Calibrated multi-phrasing Jev checks (claims/tests/AC/triage) as Claude Code skills + CLI. | JavaScript · CLI + skills (MIT) |
| [JevTape](jevtape.md) | Record and replay TypeSafe Jev HTTP decisions from JSON cassettes with contract fingerprint misses. | Java 21 · Maven CLI (`jevtape` 0.5.0) |
| [jevtok](jevtok.md) | Count Jev tokens and estimate billed request input_tokens offline before calling TypeSafe. | Python · library/CLI (`jevtok` 0.1.0) |
| [JevTree (Chuf-H)](chuf-h-jev-tree.md) | Probability tree/graph runtime: compose TypeSafe Jev action probs into path mass and Pareto picks (distinct from taxonomy jev-tree). | Python · CLI/library (`jev-tree` 0.1.0, Apache-2.0) |
| [jevtriage](jevtriage.md) | Triage PRs with TypeSafe Jev Choice (`ready` / `needs_review` / `risky`) plus confidence-gated exit codes and optional labels. | Python · PyPI/Action (`jevtriage` 0.1.0) |
| [jevtrim](jevtrim.md) | LoCoMo compaction benchmark: Jev judge vs retrieval. | Python · research (MIT) |
| [jevyoumean](jevyoumean.md) | Wrap any CLI so unknown subcommands get TypeSafe Jev intent-based "Did you mean?" suggestions from help text. | Go · CLI (`jym`) |
| [JIS · PARALLELIZE](jis-parallelize.md) | Self-organising swarm: rules first; Jev for verify/adopt/dispute; LLM escalation on low confidence. | TypeScript · swarm harness (Apache-2.0) |
| [JMP](jmp.md) | Local coding workspace: TypeSafe Jev picks the next tool action; DeepSeek/Codex/Bonsai supply arguments; OpenHands/MCP execute. | Python · desktop (pywebview) + CLI (MIT) |
| [Juardrails](juardrails.md) | Manage TypeSafe Jev guardrail policies (YAML/UI), batch questions, apply rules via REST/CLI with audit. | Go · server + CLI (license unspecified at review) |
| [llmbridge](llmbridge.md) | OpenAI-compatible LLM gateway with L1 rules / L2 TypeSafe Jev / L3 fallback routing. | Python/FastAPI + Vue · gateway (Apache-2.0) |
| [mayi](mayi.md) | Tool-call gate for Claude Code/Cursor/Codex: TypeSafe Jev scores each call; dialog on unsafe (fail-deny on errors). | Rust · CLI (`mayi` 0.1.0) |
| [Metis](metis.md) | Triage new GitHub issues with TypeSafe Jev labels and missing-detail comments via a reusable Action/CLI. | Python · GitHub Action + `metis-triage` 0.1.0 |
| [mobai-ci](mobai-ci.md) | Run MobAI `.mob` / Maestro mobile UI flows in CI; `.mobflow` steps are judged/acted by TypeSafe Jev. | CLI · GitHub Action |
| [model-router-python](model-router-python.md) | Filter models by limits/budget, then ask TypeSafe Jev which remaining model should handle the prompt. | Python · PyPI library (MIT) |
| [Moongate](moongate.md) | Evaluate PR diffs against JSON semantic rules with TypeSafe Jev and emit CI annotations. | MoonBit / GitHub Action (`brickfrog/moongate`) |
| [omp-jev-compaction](omp-jev-compaction.md) | Reduce omp tool context with sticky TypeSafe/OpenRouter Jev scores while keeping retained text verbatim. | TypeScript · omp plugin (`omp-jev-compaction` 0.1.0) |
| [Open Jev Bridge](open-jev-bridge.md) | Zero-dep Node MCP + Claude/Codex hooks bridging hosted Jev or local Kev/Laya System One (compaction + completion gates). | Node.js · CLI/MCP (`open-jev-bridge` 0.3.0, MIT) |
| [openclaw-typesafe-ai](openclaw-typesafe-ai.md) | Add an optional OpenClaw `typesafe_decide` tool for explicit TypeSafe Jev judgments without lifecycle hooks. | TypeScript · OpenClaw plugin (`openclaw-typesafe-ai` 0.1.3) |
| [OpenCode Security Guard](opencode-security-guard.md) | Linux OpenCode shell guard: local read-only check + Jev Noul ≥0.90 auto-allow. | TypeScript · OpenCode plugin (MIT) |
| [opencode-jev-guard](opencode-jev-guard.md) | OpenCode 2 plugin: TypeSafe Jev triages every local/FarHand shell command before run. | TypeScript · OpenCode plugin (`opencode-jev-guard` 0.1.0, MIT) |
| [opencode-jev-router](opencode-jev-router.md) | OpenCode Responses proxy: TypeSafe Jev selects reasoning effort for Astra/Luna/Sol with cache lineage. | Node.js 24 · npm CLI (`@robertn702/opencode-jev-router` 0.1.0, MIT) |
| [opencode-smart-reasoning](opencode-smart-reasoning.md) | Route OpenCode per-request reasoning effort with TypeSafe Jev via Zen SystemOne (fail-open). | TypeScript · OpenCode plugin (`opencode-smart-reasoning` 0.2.0) |
| [orca-jev-advisor](orca-jev-advisor.md) | Orca Lab plugin: local rules + TypeSafe Jev gate agent commands (ask before force-push/merge/apply). | TypeScript · Orca/Electron plugin (license unspecified) |
| [patdown](patdown.md) | Lint a tree against fuzzy markdown rules with a swappable judge; default backend is TypeSafe Jev. | TypeScript · npm CLI (`patdown`) and Effect packages |
| [PDF Race](pdf-race.md) | Race Docling→TypeSafe Jev vs Gemini on the same PDFs with committed keyless replays. | Node.js ≥ 20 · local/Vercel bench (`pdf-race` 1.0.0) |
| [PerfectRecall](perfectrecall.md) | Hermes/Python agent memory: TypeSafe/OpenRouter Jev evidence questions over local SQLite (Mnemosyne-compatible; no embeddings). | Python · Hermes provider + library |
| [Pi Adaptive Effort Router (XDeviation)](xdeviation-pi-jev-router.md) | Change Pi thinking level only with TypeSafe Jev (not the model); distinct from philippdubach pi-jev-router. | TypeScript · Pi extension (`pi-jev-router` 0.2.0, MIT) |
| [pi-follow-through](pi-follow-through.md) | Nudge Pi after agent_settled only when TypeSafe Jev cites unfinished work above a probability threshold. | TypeScript · Pi extension (`pi-follow-through`) |
| [pi-heed](pi-heed.md) | Enforce evolving conversational constraints on Pi tool calls; TypeSafe Jev classifies policy changes, code owns the ledger. | TypeScript · Pi extension (`pi-heed`) |
| [pi-jev](pi-jev.md) | Add a Jev pre-tool gate, output judge, and jev_ask tool to the Pi coding agent (shadow mode default, fail-open). | TypeScript · Pi extension (npm) |
| [pi-jev-context](pi-jev-context.md) | Trim long pi tool outputs before they enter context (comparison first; TypeSafe Jev only when needed) with lossless recall. | TypeScript · Pi extension (`pi-jev-context`) |
| [pi-jev-effort](pi-jev-effort.md) | Set Pi thinking level per prompt from a TypeSafe Jev difficulty score, capped by remaining quota. | TypeScript · Pi extension (`pi-jev-effort` 0.1.0) |
| [pi-jev-permit](pi-jev-permit.md) | Gate Pi bash/write/edit calls with TypeSafe Jev allow judgments after local hard-deny and read-only fast paths. | TypeScript · Pi extension (`pi-jev-permit` 0.2.0) |
| [pi-jev-router](pi-jev-router.md) | Route pi tasks across OpenRouter models with TypeSafe Jev classification and local Pareto/role policy (shadow default). | TypeScript · Pi extension (`pi-jev-router` 0.1.0) |
| [pi-jev-sentinel](pi-jev-sentinel.md) | Check Pi/Claude/Codex tool calls, outputs, and replies with Jev intent/risk and injection screens (fail-closed without a key). | TypeScript · Pi extension and host hooks |
| [pi-shift-router](pi-shift-router.md) | Route Pi turns between cheap and strong model tiers; optional TypeSafe Jev probability judge. | TypeScript · Pi npm extension (MIT) |
| [pi-thinking-router-jev](pi-thinking-router-jev.md) | Pi extension: TypeSafe Jev (or local rules) picks thinking level low/medium/high/xhigh from task feedback. | TypeScript · Pi extension (license unspecified) |
| [pi-typesafe-approve](pi-typesafe-approve.md) | Pi extension: System One/Jev triage auto-approves routine Bash; escalates the rest to a human. | TypeScript · Pi extension (MIT) |
| [pi-typesafe-bash-guard](pi-typesafe-bash-guard.md) | Classify Pi bash tool calls and user `!` shells with TypeSafe Jev before execution. | TypeScript · Pi extension (npm `@gowthamgts/pi-typesafe-bash-guard` 0.1.0) |
| [pi-warden](pi-warden.md) | Add configurable action holds, project-rule feedback and context checks to Pi using local policy and Jev judgments. | TypeScript · Pi extension |
| [plain-language-gate](plain-language-gate.md) | Jev plain-language readability gate (six checks → pass/review/rewrite) for agent writing. | Python · skill/CLI (MIT) |
| [prompt2jev](prompt2jev.md) | Convert natural language, an LLM prompt, or prompt-running code into a TypeSafe Jev decision package. | Python · agent skill + stdlib CLI |
| [pytest-jev](pytest-jev.md) | Semantic pytest assertions (holds/lacks/choice/score) judged by TypeSafe Jev via typesafe-sdk. | Python · pytest plugin (`pytest-jev` 0.1.0) |
| [Quicksilver](quicksilver.md) | Hand bulk judgment/shortlist calls from Claude Code to TypeSafe Jev (parallel typed verdicts). | JavaScript · Claude Code skill/plugin (MIT) |
| [Responsible AI Harness](responsible-ai-harness.md) | Assess AI systems with hard rules plus optional TypeSafe Jev judge; checksummed evidence bundles and offline report UI. | TypeScript · assessment harness + static UI (`responsible-ai-harness` 0.1.0) |
| [riff](riff.md) | Lint prose with ruff-style rule codes; deterministic static rules plus optional TypeSafe Jev judgment rules. | Python · CLI (`riff` / `riff-lint` 0.1.0) |
| [RLCD Gateway](rlcd-gateway.md) | Self-hosted Go gateway: LLM routing with context pruning plus Jev/open-rlcd System One audit/calibration dashboard. | Go · binary/npm/PyPI (`rlcd-gateway`, Apache-2.0) |
| [semantic-assert](semantic-assert.md) | Assert plain-English claims about UI/text state with TypeSafe Jev (Playwright helpers; thresholds in code). | TypeScript · npm packages + Playwright adapter |
| [SemDecide](semdecide.md) | Run TypeSafe Jev predicates, routes, scores, and JSONL filters as Unix CLI exit codes for pipelines and CI. | Python · CLI (`semdecide` 0.2.1) |
| [similarity-ts-jev](similarity-ts-jev.md) | Run similarity-ts + fallow on TypeScript, keep only the pairs TypeSafe Jev judges worth merging (with copy/derive/extract shape), and calibrate the cutoff. | TypeScript · npm CLI/library (`@kongyo2/similarity-ts-jev` 0.2.0, MIT) |
| [Skill Dash](skill-dash.md) | Judge Claude Code/Codex skills with TypeSafe Jev (usefulness/redundancy/clarity/action) in a local dashboard. | Python · stdlib loopback server + SQLite |
| [Skillbox](skillbox.md) | Share versioned agent skills and use optional Jev scores to recommend authorized skills for a task. | TypeScript / Bun / PostgreSQL · skill library, MCP and CLI |
| [SkillRanker](skillranker.md) | Rank which agent skills fit the next step from live session context using Jev wide/re-rank stages. | Rust · CLI (`sr`), hooks and TUI |
| [SlidePilot](slidepilot.md) | Advance Slidev decks from presenter voice when TypeSafe Jev and TypeScript policy agree the slide is complete. | TypeScript · Slidev addon + Cloudflare Worker (0.1.0) |
| [SmartMoney-Cub](smartmoney-cub.md) | Capture offline trading-journal evidence packs and optionally ask TypeSafe Jev typed review questions (read-only; no orders). | Python · `smcub` CLI and harness |
| [Sniff Test](snifftest.md) | Lint Markdown/prose with local countable rules plus optional confirmed TypeSafe Jev judgment rules. | TypeScript/Bun · CLI (`snifftest` 0.1.0) |
| [specpi-jev-guard](specpi-jev-guard.md) | Gate risky Pi agent shell/file commands with local rules then TypeSafe Jev danger scores. | TypeScript · Pi npm extension (MIT) |
| [Stanley Code](stanley-code.md) | Review code changes, triage failures, and extend Jev workflows; optional Pi delegation can edit the repository. | TypeScript · source-built CLI and workflow runtime |
| [stingray](stingray.md) | Stop half-done Claude Code/Codex turns with TypeSafe Jev judgments (empty action, broken promise, watch with nothing running). | Shell · Stop hook (MIT) |
| [stop-rules](stop-rules.md) | Coding-agent stop hook: TypeSafe Jev yes/no per changed piece against written team rules (multi-agent + optional team server). | TypeScript · CLI (`stop-rules` 0.1.0) |
| [stuntd](stuntd.md) | Local Jev-compatible proxy: serve/learn typed System One decisions on a Laya head (or zero-shot), optional OpenAI/Jev upstream. | Python ≥ 3.10 · PyPI (`stuntd` 0.1.0, Apache-2.0) |
| [super-jev](super-jev.md) | Run evidence → typed Jev judgments → permitted actions → verified outcomes with local JSONL traces. | TypeScript · harness (Node ≥ 24) |
| [Supercov](supercov.md) | Code quality and test coverage for coding agents: Jev scores each source file so the agent knows what to fix first. | Rust · CLI via npm, Homebrew, Go or crates.io |
| [System One Harness](systemone-harness.md) | Drive finite-action environments with TypeSafe Jev (OpenRouter/TypeSafe): one typed decision per step, confidence gates, full traces. | Python · CLI `s1` (`systemone-harness` 0.4.0) |
| [System One Playground](system-one-playground.md) | Write SysOneScript, use a Go System One client, semlint, and Studio/VS Code—offline first, optional live Jev. | Go · CLI/extension (`sysone`/`sos`) + `typesafe` module |
| [Taste Lint](taste-lint.md) | Catch AI-sloppy UI motion/copy/typography before ship; optional TypeSafe Jev under-review judgments via Gateway or direct. | Node.js ≥ 24.11 · npm CLI (`taste-lint` 0.3.0) |
| [tax-doc-classifier](tax-doc-classifier.md) | Classify tax PDF page text into IRS form ids and page kinds with TypeSafe Jev Choice over shipped criteria. | TypeScript · library (`tax-doc-classifier`) |
| [tdd-gate](tdd-gate.md) | Dual-agent TDD gates: TypeSafe Jev coverage/blame/gaming/weakening/drift judgments; optional isolated orchestrator. | TypeScript · CLI (`tdd-gate` 0.1.0, MIT) |
| [The Jev-enator](the-jev-enator.md) | Claude Code hooks: TypeSafe Jev danger gate, failure notice, and log-only completion check. | Python · stdlib hooks + install scripts |
| [tink-route](tink-route.md) | Gate Agent Skills with TypeSafe Jev (specialist Noul + Choice), then optionally install via Tink. | Python · CLI (`tink-route` 0.3.1) |
| [todo-jev](todo-jev.md) | Classify requests into a 3-tier path (local rule / Jev skill / foundation model) with skill profiles and preflight. | Python · Typer CLI (`todo-jev` 0.1.0) |
| [tokengate](jev-model-tokengate.md) | Buffer streamed LLM tokens and gate each window with TypeSafe Jev before the client sees them. | Node.js · OpenAI-compatible proxy (`tokengate` 0.1.0) |
| [toolgate](toolgate.md) | Gate Claude Code and MCP tool calls with static rules plus TypeSafe Jev risk judgments and a local audit log. | TypeScript · CLI, Claude Code hook and MCP proxy |
| [triagedy](triagedy.md) | Triage JSONL security alerts with TypeSafe Jev typed questions; route outcomes in ordinary Rust code. | Rust · CLI (`triagedy` 0.1.0) |
| [Tripwire](tripwire.md) | Abort bad streaming completions mid-flight using TypeSafe Jev (or an offline heuristic) inside an OpenAI-compatible proxy. | Python · package (`tripwire` 0.1.0) |
| [Typed Evals](typed-evals.md) | Evaluate RAG/agent outputs and guard tools with TypeSafe Jev judges and optional calibration. | Python · library/CLI (`typed_evals`) |
| [typesafe-agent-gates](typesafe-agent-gates.md) | Gate unattended LangChain/Deep Agents shell commands and triage with TypeSafe Jev middleware. | Python · LangChain middleware |
| [unsafe-c-finder](unsafe-c-finder.md) | Classify C/C++ snippets and staged hunks with TypeSafe Jev via OpenRouter (unsafe probability, then CWE when over threshold). | Python · CLI (`unsafe-c-finder`, MPL-2.0) |
| [VexJoy Agent](vexjoy-agent.md) | Route plain-English requests to specialist agents/skills; optional `/d` uses TypeSafe Jev classification and intent gates. | Python · agent toolkit (Claude Code / Codex hooks) |
| [wellposed](wellposed.md) | Lint TypeSafe Jev requests for broken paths, missing Choice escape hatches, and other structural smells before calling the API. | TypeScript · npm CLI (`wellposed` 0.4.0, zero deps) |
| [winnow](winnow.md) | Hide confident-irrelevant Claude Code tool-result blocks with TypeSafe Jev (or adapter) judgments; recall stubs on demand. | Python · Claude Code hooks + sidecar CLI (`winnow` 0.5.0) |
| [Yoshi](yoshi.md) | Local Claude Code/Codex context-pruning proxy: TypeSafe Jev via AI Gateway judges omit/keep spans (experimental POC). | Bun/TypeScript · loopback proxy (`yoshi` 0.1.0) |

## Games and simulation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [jev-drone](jev-drone.md) | Study typed maneuver judgments alongside deterministic simulated flight control and inspect a separate tunnel experiment. | Python / MuJoCo · simulation and replay |
| [jev-libero](jev-libero.md) | Study fine-grained LIBERO robot actions with TypeSafe Jev layered choices and local physics previews. | Python · CLI and MuJoCo/LIBERO extras |
| [jev-plays](jev-plays.md) | Watch TypeSafe Jev play Craftax (macro/raw actions) with optional LLM planner-as-facts and a local web UI. | Python · Craftax harness + viewer |
| [jev-robotics-eval](jev-robotics-eval.md) | Evaluate JEV-compatible robot control on MetaWorld/RoboTwin (text/vision, privilege levels). | Python · eval harness (MIT) |
| [quackd](quackd.md) | Drive multi-robot goals with LLM pilots; optional `--jev` TypeSafe stepper for closed-set verb choices. | Python · CLI (`quackd`) and robot extras |
| [JevPilot](jevpilot.md) | Inspect sampled driving paths, Jev choices and local braking in a browser simulation; application licensing is unspecified. | JavaScript / Three.js · simulation demo |
| [JevPokerBench](jev-poker-bench.md) | Compare official Jev and other agents on Texas Hold'em (cash/SNG boards, replay, BYOK tables). | Python/React · FastAPI playground (`pokerbench` 0.1.0) |
| [TypeSafe Mario](typesafe-mario.md) | Study Jev action choices over emulator telemetry with a synthetic state demo and decision logs; licensing is unspecified. | Python · emulator controller and dashboard |
| [Jev Lab](jev-lab.md) | Run Hundred NPC-town and Jev Shogi labs where Jev picks the next legal action (Rules mode offline). | TypeScript · pnpm monorepo (`jev-lab` 0.2.0) |
| [jev-zork](jev-zork.md) | Watch TypeSafe Jev play Zork I (Choice over Jericho actions) with anti-loop policy and a French replay dashboard. | Python · CLI (`jev-zork` 0.1.0) + replay UI |
| [system-one-chess](system-one-chess.md) | Play chess against TypeSafe Jev (Gateway/OpenRouter) with Stockfish analysis; optional local Laya. | Python ≥ 3.11 · web/Docker (`system-one-chess` 0.5.0, GPL-3.0) |

## Home automation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [HA Jev Autopilot](ha-jev-autopilot.md) | Per-room Jev decisions with deterministic HA actions and phone confirmation for risky devices. | Python · Home Assistant integration (MIT) |
| [Jev for Home Assistant](ha-jev.md) | Turn household context into judgment sensors and automation responses. | Python · Home Assistant integration |

## Independent model research

These projects study related typed-decision patterns using other models. They are independent research implementations, not official Jev releases or validated substitutes; their guides separate code, model and dataset licensing, and reported benchmarks from catalog checks.

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [AnyJev (Nokia Applied Research)](nokia-anyjev.md) | Turn an open LLM into Jev-style typed decisions with probabilities (L0–L2); independent of official Jev. | Python · PyPI (`anyjev` 0.1.0, Apache-2.0) |
| [J3v](j3v.md) | Edge-compiled System One decisions (J3v∶Jev :: k3s∶k8s) with Rust compiler and firmware demos. | Rust · compiler/runtime (MIT) |
| [Jev-LCT](jev-lct.md) | Looped Calibration Transformer System One engine with Jev-shaped Choice/Noul/Score serving; independent of hosted Jev. | Python · research engine + HF weights (Apache-2.0) |
| [Jev-Omni](jev-omni.md) | Run an open multimodal System One–style classifier (text/image/audio/video → option probabilities) on Gemma 4 12B IT; independent of official Jev. | Python / PyTorch · HF weights (CUDA, ~50 GB FP32) |
| [jev-omni.js](jev-omni-js.md) | Run independent Jev-Omni multimodal decisions in-browser on WebGPU (text+images; WIP video/audio). | JavaScript · onnxruntime-web (Apache-2.0) |
| [Jev-Style](jev-style.md) | Local System One–compatible decision models + skills/guard/MCP tooling; independent of hosted Jev. | Python · local server + skills/MCP (Apache-2.0) |
| [JevEmbed](jevembed.md) | Turn embedding models into Choice/Score/Noul decisions via a Jev-shaped Python API/CLI/HTTP server. | Python · framework + HF configs (Apache-2.0) |
| [Jevlet](jevlet.md) | From-scratch System One–style decision model research + Windows command palette; independent of hosted Jev. | Python · research model + desktop app (MIT) |
| [Jevlike](jevlike.md) | Train a small option-attention scorer with synthetic data and optional frozen encoders; independent of official Jev. | Python / PyTorch · research starter |
| [kevala](kevala.md) | Run Laya/Kev/Bruv/SemIf-style typed decisions in-browser via Rust→WASM + WebGPU (no server; independent of official Jev). | JavaScript/WASM · npm/CDN (`kevala`, Apache-2.0) |
| [lev (Abhinavexists)](lev.md) | Run an open Qwen3.5-4B LoRA System One model over `/v1/systemone` (independent of hosted Jev). | Python · model + harness (Apache-2.0) |
| [Malkuth](malkuth.md) | Multilingual open decision models (Choice/Noul/Score) via Kev. | Weights · research (Apache-2.0) |
| [NanoJev](nanojev.md) | Study independent Qwen-based typed decision heads, local serving, and game controllers with recorded comparisons. | Python / PyTorch · model research and replay |
| [Open Alternative to Jev](open-alternative-jev.md) | Compare packed and separate typed decisions from open models and fit calibration on labeled data; not a Jev reproduction. | Python · Transformers/vLLM research library |
| [open-jev](open-jev.md) | Experiment with independent Kev and DeBERTa typed decisions locally in a browser; does not use official Jev weights. | TypeScript · npm library, Transformers.js / ONNX |
| [openjev-sglang](openjev-sglang.md) | Inspect a Jev-shaped HTTP decision API using Qwen and SGLang; independent model behavior and unspecified code licensing. | Python / FastAPI / SGLang · inference research |
| [PlayJev](playjev.md) | Study a 0.8B model that picks a game's next move from the frame alone, one forward pass, probability per listed move; independent of official Jev. | Python / PyTorch · model research and browser demo |
| [RYOTIDE](ryotide.md) | Local LLM one-forward-pass typed decisions (MLX/PyTorch) measured on JevBench; independent of official Jev. | Python · research (MIT) |
| [SemIf](semif.md) | Explore typed option scoring and shared-state reuse with local open models; independent of official Jev. | Python / PyTorch / MLX · research and browser lab |
| [Sureband](sureband.md) | Conformal coverage wrappers for System One outputs (Jev/Laya/…) from labeled calibration sets. | Python · library (`sureband`, Apache-2.0) |
| [TinyJev](tinyjev.md) | Run an offline ~0.6B System One–compatible Choice/Noul/Score model (MLX/PyTorch); independent of hosted Jev. | Python · package + HF weights (MIT) |
| [Valen](valen.md) | Train/serve a multimodal System One–style decision model (text/image/video → probabilities); independent of hosted Jev. | Python · training/inference + HF weights (Apache-2.0) |
| [vLLM Jev](vllm-jev.md) | Serve Jev-compatible decision models through vLLM. | Python · server (Apache-2.0) |
| [vLLM Jev (mode-io)](mode-io-vllm-jev.md) | Serve Jev-style Choice/Noul/Score checkpoints through vLLM (distinct from Egbertjing/vllm-jev). | Python · server (Apache-2.0) |

## SDKs and integrations

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [adk-go-typesafe](adk-go-typesafe.md) | Call System One from Go and Google ADK-Go with OpenAPI-generated types (Choice/Score/Noul). | Go · module + ADK tool (`adk-go-typesafe`) |
| [Advocaat](advocaat.md) | Batch typed Jev choice, score, and yes/no questions about structured data from TypeScript. | TypeScript · client library and agent skill |
| [ask-jev (Aether-254)](aether-254-ask-jev.md) | MCP + Codex/Claude plugin for TypeSafe Jev evaluate/batch/ping (Choice/Score/Noul). | TypeScript · MCP/plugin (MIT) |
| [datafusion-jev](datafusion-jev.md) | DataFusion SQL `prompt_jev` UDF for typed TypeSafe Jev answers over row text (bring HTTP client). | Rust · DataFusion 55 crate (MIT OR Apache-2.0) |
| [feelings](feelings.md) | Add typed `.feels()` / `.how()` / `.matches<T>()` methods on any BAML value using TypeSafe Jev (license unspecified). | BAML · library (`baml_src/vibes.baml`) |
| [go-jev](go-jev.md) | Call TypeSafe Jev from Go (Ask/Evaluate) and UNIX pipelines via jev-cli; explicit API key option. | Go · module + CLI (`github.com/mattn/go-jev`, MIT) |
| [hono-jev-router](hono-jev-router.md) | Route Hono HTTP requests by plain-English meaning with TypeSafe Jev Noul judgments (experimental). | TypeScript · Hono router (`hono-jev-router`) |
| [hunch](hunch.md) | Call TypeSafe Jev classify/score/check/pick/rank/where over scalars, lists, and pandas columns (`hunch-jev`). | Python · PyPI library (`hunch-jev` 0.6.0) |
| [jear](jear.md) | Route NEAR AI Cloud / IronClaw choices by budget, quality, and sensitivity using TypeSafe Jev structured decisions. | Rust · CLI/library (`jear` 0.1.0) |
| [jev (okooo5km)](okooo5km-jev.md) | Stdlib Python CLI + Agent Skill for TypeSafe Jev yes/pick/score via TypeSafe API or OpenRouter (distinct from typesafe-cli / typesafeai-cli). | Python · CLI 0.3.2 + skill |
| [Jev Classification for n8n](jev-classification-n8n.md) | Route workflow items with typed Jev decisions, configurable review handling, and multi-item batching. | TypeScript · self-hosted n8n community node |
| [Jev MCP (Freepik)](freepik-jev-mcp.md) | Go MCP server for typed decide/classify/verify/rerank via OpenRouter or TypeSafe (binary/container). | Go · MCP binary (`jev-mcp` v0.3.0) |
| [Jev Studio](jev-studio.md) | Experiment with TypeSafe Jev via a `jev` CLI (verify/screen/classify/…) and an MCP server with cookbook tools. | Python · CLI + MCP (`jev-studio` 0.1.0 Alpha) |
| [Jev Symfony Bundle](jev-symfony-bundle.md) | Wire TypeSafe Jev into Symfony via typed client, validator attributes, Messenger, Workflow guards, and profiler. | PHP · Symfony bundle (Apache-2.0) |
| [jev-cli (shaharia-lab)](shaharia-lab-jev-cli.md) | Rust `jev` CLI + MCP: typed TypeSafe Jev questions with shell exit codes and JSON (distinct from tumf). | Rust · crates.io CLI/MCP (Apache-2.0 OR MIT) |
| [jev-cli (tumf)](tumf-jev-cli.md) | Ask TypeSafe Jev noul/choice/score from a PyPI CLI plus bundled stdio MCP (`jev` / `jev-mcp`). | Python · PyPI CLI/MCP (`jev-cli` 0.6.2) |
| [jev-feels](jev-feels.md) | Use TypeSafe Jev as Ruby `feels?` / `decide` / `score` and Rails validations (distinct from BAML feelings). | Ruby · gem (`jev-feels` 1.1.0) |
| [jev-foundation-models](jev-foundation-models.md) | Use TypeSafe Jev as an Apple Foundation Models `LanguageModel` for `@Generable` Bool/enum/score fields. | Swift 6 · SwiftPM (`JevFoundationModels` 0.1.0, Apache-2.0) |
| [jev-java](jev-java.md) | Call TypeSafe Jev (or OpenRouter/Vercel adapters) from Java 17+ with typed Choice/Noul/Score and optional Spring. | Java · Maven (`jev-typesafe` 0.1.1) |
| [jev-mcp](jev-mcp.md) | Give agents ten purpose-built TypeSafe Jev judgment MCP tools (verify, screen, find, classify, review, gate, …). | TypeScript · npm MCP server (`@jkudish/jev-mcp`) |
| [jev-mcp-server](jev-mcp-server.md) | MCP for official TypeSafe Jev choice/score/noul plus compare/verify/batch classify and client installer. | Python · PyPI MCP (`jev-mcp-server` 0.2.3) |
| [jev-prompt-sentry](jev-prompt-sentry.md) | Reverse-proxy Anthropic Messages through one batched TypeSafe Jev jailbreak/injection/exfil screen (PolyForm Noncommercial). | Python · FastAPI proxy |
| [jev-recipes](jev-recipes.md) | 66 TypeScript recipes for TypeSafe Jev decisions (rerank/verify/clarify/route/…) via `@typesafe-ai/sdk`. | TypeScript · npm (`jev-recipes` 0.2.0) |
| [jev-sdk-java](jev-sdk-java.md) | Call System One from Java 21 with sealed Question/Answer records (TypeSafe-only; source-build until Central lists 0.1.0). | Java 21 · Maven (`com.luigivismara:jev-sdk-java`) |
| [jev2mcp](jev2mcp.md) | Local companion + Chrome extension: TypeSafe Jev selects ChatGPT MCP/plugin/tool mentions from your catalog. | Node.js · local server + extension (`jev2mcp` 0.2.1) |
| [jev4j](jev4j.md) | Call TypeSafe/OpenRouter Jev from Java (noul/choice/score, multi-question, Spring starter). | Java · Maven (`jev4j-core` 0.1.0, MIT) |
| [jev4k](jev4k.md) | Declare TypeSafe Jev Noul/Choice/Score questions in a Kotlin DSL and read typed answers. | Kotlin · Maven (`com.pambrose:jev4k` 0.1.0) |
| [JevApi](jevapi.md) | .NET 10 TypeSafe.Client + MCP server for typed noul/choice/score evaluate/batch. | C# · .NET library + MCP (MIT) |
| [JevClient.jl](jevclient-jl.md) | Call System One from Julia with Noul/Choice/Score sets and endpoint policy locks to api.typesafe.ai. | Julia · package (`JevClient` 0.1.0) |
| [jevframe](jevframe.md) | Classify/score pandas and Polars rows with TypeSafe Jev via a `.jev` accessor and full probability columns. | Python · PyPI (`jevframe` 0.1.0; pandas/polars extras) |
| [jevgo](jevgo.md) | Call TypeSafe System One from Go with typed Noul/Choice/Score (unofficial stdlib client). | Go · module (`github.com/devbackend/jevgo`) |
| [jevmcp (eaisdevelopment)](eaisdevelopment-jevmcp.md) | One Agent Plugins install: TypeSafe Jev MCP tools for spec-drift, CI triage, and code-audit screening. | Python · Agent Plugins + MCP (Apache-2.0) |
| [jevonian](jevonian.md) | Local OpenAI/Anthropic/Responses proxy: one Jev call picks the model and the thinking level after code has filtered candidates; pinned models skip Jev. | Node.js ≥ 22 · CLI and local server (`jevonian` 0.0.1, AGPL-3.0-only) |
| [jevper](jevper.md) | Jev-shaped System One noul/choice/score over any OpenAI-compatible client (no hosted TypeSafe API). | Python · PyPI (`jevper` 0.1.2, Apache-2.0) |
| [Jevs](jevs.md) | Call TypeSafe Jev classify/score/check/batch from Bun MCP / Codex plugin via the official JS SDK. | TypeScript · Bun MCP / Codex plugin (`jevs` 0.1.0) |
| [JevT++](jevtpp.md) | C++20 typed decision library with optional local Laya (ONNX/ggml) or remote System One backends. | C++20 · library (MIT) |
| [Klassify](klassify.md) | Kotlin Multiplatform DSL/SDK and Native CLI/MCP for TypeSafe System One classification (distinct from jev4k). | Kotlin · KMP SDK + Native CLI (`klassify` v0.1.1, Apache-2.0) |
| [kotlin-jev](kotlin-jev.md) | Kotlin SDK + CLI for TypeSafe Jev (port of mattn/go-jev patterns). | Kotlin/JVM · library + `jev-cli` (MIT) |
| [Laravel AI](laravel-ai.md) | Add typed classification through Laravel’s TypeSafe provider. | PHP · Laravel package |
| [llm-typesafe](llm-typesafe.md) | Call TypeSafe Jev noul/choice/score from the LLM CLI (`typesafe/jev-latest` / `jev`). | Python · LLM plugin (`llm-typesafe` 0.1a0) |
| [Mechanical Jev](mechanical-jev.md) | Ask System One Noul/Choice/Score from Rust (`mjev`) against local Intel Phi Jev or compatible endpoints. | Rust · library/CLI (Apache-2.0) |
| [n8n-nodes-typesafe](n8n-nodes-typesafe.md) | Ask TypeSafe Jev noul/choice/score questions about workflow text or JSON inside n8n. | TypeScript · n8n community node |
| [naturalcodz](naturalcodz.md) | Natural-logic npm helpers (classify/guard/route/score) on TypeSafe Jev with confidence thresholds. | TypeScript · npm (`naturalcodz`, MIT) |
| [NeuroLink](neurolink.md) | Call generate/stream across many providers and use TypeSafe Jev `decide` for typed boolean/choice/score judgments. | TypeScript · SDK/CLI (`@juspay/neurolink`) |
| [nf-jev](nf-jev.md) | Call TypeSafe Jev noul/choice/score from Nextflow pipelines and gate on returned probabilities. | Groovy · Nextflow plugin (`nf-jev` 0.1.0, Apache-2.0) |
| [Prompt Rejector](prompt-rejector.md) | Screen prompts, skills, and MCP tool descriptions via HTTPS/MCP with TypeSafe Jev plus deterministic checks. | TypeScript · npm (`prompt-rejector` 1.2.0, ISC) |
| [ruby_decision_model](ruby-decision-model.md) | Ask Noul, Choice, and Score questions from Ruby via Typesafe or OpenRouter. | Ruby · gem (stdlib HTTP) |
| [s1 (s1-rs)](s1-rs.md) | Derive Choice/Score/Noul question sets in Rust; optional `typesafe-rs` backend (distinct from typesafe-api). | Rust · workspace crates (`s1` 0.1.0, MSRV 1.85) |
| [scala-jev-sdk](scala-jev-sdk.md) | Call System One from Scala 3.3 LTS with typed Question/answer lookup over an sttp 4 backend (Maven Central). | Scala 3 · Maven (`io.github.ticofab:scala-jev-sdk_3` 0.1.0, Apache-2.0) |
| [semgate](semgate.md) | Filter and route Go HTTP requests with TypeSafe Jev noul/choice/score middlewares. | Go · net/http middleware |
| [Spring AI TypeSafe](spring-ai-typesafe.md) | Call System One from Java/Spring AI (client, JevJudge, guardrail/RAG/tool-search advisors). | Java · Maven (`org.springaicommunity`, 0.1.0) |
| [swift-jev](swift-jev.md) | Call TypeSafe Jev Choice/Noul/Score from SwiftPM apps or a JSON CLI (`jev`); no free-form generation. Distinct from TypeSafe (Swift). | Swift 6.2 · SwiftPM library (`Jev`) + CLI |
| [sys1 (alvarobartt)](alvarobartt-sys1.md) | Serve open decision models (e.g. Laya) behind a System One–compatible `/v1/systemone` API in Rust. Distinct from hraness/sys1. | Rust · CLI/server (Apache-2.0) |
| [System One Connector](system-one-connector.md) | MCP `evaluate` tool: typed Jev/Laya/System One judgments with probabilities for supported coding agents. | Go · static binary + MCP setup (MIT) |
| [systemone (justintout)](systemone-justintout.md) | Unofficial Go System One/Jev client with compile-time typed questions (distinct from TypeSafe Go). | Go · module (`github.com/justintout/systemone`, MIT) |
| [taurus-jev-sdk-go](taurus-jev-sdk-go.md) | Hard-failing stdlib Go System One client (unofficial). | Go · library (MIT) |
| [TypeSafe (Swift)](typesafe-swift.md) | Call System One Noul/Choice/Score from SwiftPM apps and servers. | Swift · SwiftPM library (`TypeSafe`) |
| [TypeSafe AI for Agent Zero](a0-typesafe-ai.md) | Ask TypeSafe Jev Choice/Noul/Score from Agent Zero chat with probability cards; bundles the official agent skill. | Python · Agent Zero plugin (`typesafe_ai` 1.0.0) |
| [TypeSafe C++ SDK](typesafe-sdk-cpp.md) | Call TypeSafe System One (Choice/Score/Noul) from C++20 with a builder-configured client. | C++20 · library (MIT) |
| [TypeSafe Go](typesafe-go.md) | Call System One from Go with explicit auth options and no implicit env reads (Stacklok; unofficial). | Go · module (`github.com/stacklok/typesafe-go`) |
| [TypeSafe MCP](typesafe-mcp.md) | Give agents a general-purpose Jev evaluation tool with raw provider responses. | Go · MCP server and pi extension |
| [typesafe-api (Rust)](typesafe-api-rs.md) | Call System One from Rust with typed questions/answers (`typesafe-api` 0.1.0, MSRV 1.88). | Rust · crates.io client |
| [TypeSafe-as-a-Judge](typesafe-as-a-judge.md) | Give Codex/Claude Code bounded TypeSafe Jev route/rank/extract/verify/judge MCP tools (unofficial). | Node.js · MCP plugin + skills (`0.1.0`) |
| [typesafe-cli](typesafe-cli.md) | Ask Jev noul/choice/score questions from the shell (`jev`); answers are numbers, not prose. | TypeScript · npm CLI / Nix |
| [typesafe-sdk-go (jmelahman)](typesafe-sdk-go-jmelahman.md) | Stdlib-only Go client for TypeSafe System One (Noul/Choice/Score helpers). | Go · module (`github.com/jmelahman/typesafe-sdk-go`, MIT) |
| [TypeSafe.AI (.NET SDK)](typesafe-sdk-csharp.md) | Call System One from .NET with DI, resilience, and OTel (NuGet TypeSafe.AI; distinct from TypeSafeAI.Net). | C# · NuGet client (`TypeSafe.AI` v1.0.0) |
| [typesafeai-cli](typesafeai-cli.md) | Run TypeSafe Jev ask/decide/screen/verify flows from a Python `typesafe` CLI for humans or agents. | Python · CLI (`typesafe`) |
| [TypeSafeAI.Net](typesafeai-net.md) | Add typed Jev judgments to .NET applications and Microsoft.Extensions.AI pipelines. | C# · client library |

## Search and retrieval

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Agent Seek](agent-seek.md) | Cheap web recall for agents: You.com discover + TypeSafe Jev cascade ranking (REST/MCP/UI). Does not write answers. | Python 3.12+ · FastAPI/MCP (`agentseek.dev` demo) |
| [blink](blink.md) | Search a local codebase with TypeSafe Jev via ensemble directory walkers that Choice-pick the next file or folder. | Bun · CLI (`./blink`); license unspecified |
| [duckdb-jev](duckdb-jev.md) | Run TypeSafe Jev Noul/Choice/Score predicates natively inside DuckDB SQL (C++ extension; no Python UDF). | C++ · DuckDB extension (Apache-2.0) |
| [jegrep](jegrep.md) | Find code by natural-language intent using TypeSafe Jev (or OpenRouter→Jev) without embeddings. | Rust · CLI (`jegrep`) and release binaries |
| [Jev Second Brain](jev-second-brain.md) | Index a Markdown/Obsidian vault and optionally judge note relationships with TypeSafe Jev (Gateway). | Python · CLI (`secondbrain`) |
| [jev-corrective-rag](jev-corrective-rag.md) | Corrective RAG with TypeSafe Jev typed gates for triage, chunk grading, and answer verification (LLM only generates). | Python · Streamlit app, CLI and bench |
| [jev-rag](jev-rag.md) | Index local files with SQLite BM25, rerank evidence with TypeSafe Jev, optionally stream grounded answers. | Python · local RAG CLI/UI (MIT) |
| [jev-rerank-bench](jev-rerank-bench.md) | Reproduce TypeSafe Jev vs Cohere/zerank reranker experiments on shared BM25 candidate sets. | Python · benchmark suite (MIT) |
| [jev-reranker](jev-reranker.md) | Rerank, filter, or compress JSON search candidates with TypeSafe Jev via a stdin/stdout Rust CLI. | Rust · npm CLI (`jev-reranker` 0.1.1) |
| [jev-reranker (hotchpotch)](hotchpotch-jev-reranker.md) | Score/filter RAG candidates with TypeSafe Jev in Python (listwise/pointwise/pairwise; PyPI). Distinct from the Rust CLI. | Python · library (`jev-reranker` 0.1.2) |
| [jev-semgrep](jev-semgrep.md) | Filter lines by whether a plain-language proposition holds, with AND/OR/NOT meanings via TypeSafe Jev (not Semgrep Inc). | Node.js · CLI (`@uehaj/semgrep`) |
| [jevql](jevql.md) | Add `jev()` / `jev_prob` / `jev_choice` / `jev_score` to queries against vanilla PostgreSQL without an extension, from a psql-style CLI, MCP server, or SDKs. | Go · CLI, MCP server and Go/TypeScript/Python SDKs (MIT) |
| [jevql (hemanth)](hemanth-jevql.md) | npm `jev-ql` semantic/cognitive SQL over unstructured data via TypeSafe Jev (distinct from kylemclaren/jevql). | JavaScript · npm (`jev-ql`, MIT) |
| [jevsearch](jevsearch.md) | Add a ⌘K site-search palette to a shadcn/ui site: keyword hits on the first keystroke, then one TypeSafe Jev request re-ranks the top 20 by intent, with no embeddings. | TypeScript · shadcn registry block (React component, Fetch-API handler; MIT) |
| [JevSQL](jevsql.md) | Add TypeSafe Jev match/pick/rank/bool/choice helpers to SQLite SQL with batching, caches, and review queues. | TypeScript · library and CLI |
| [jgrep](jgrep.md) | Filters text, structured records, functions, and diff hunks against plain-English descriptions using Jev Noul judgments. | Python · library and CLI (`jev-grep`) |
| [jgrep (npm: jevgrep)](jgrep-jevgrep.md) | Gate a diff in CI on an English rule (`--diff`, grep exit codes), list the test files a diff can affect (`--tests`), or grep code and CSV rows by description with one TypeSafe Jev Noul per chunk. Distinct from the Python jgrep. | TypeScript · npm CLI (`jevgrep` 0.4.0, Node ≥ 18) |
| [jlink](jlink.md) | Links records under a plain-English match rule using Jev Noul pair judgments, with local candidate blocking and match resolution. | Python · library and CLI (`jlink`) |
| [jselect](jselect.md) | Selects source-linked evidence within a token budget using Jev Noul relevance judgments and local diversity-aware selection. | Python · library and CLI (`jev-select`) |
| [jsort](jsort.md) | Order lines/paragraphs/files along a plain-English dimension using pairwise TypeSafe Jev comparisons. | Python · CLI (`jsort` / jev-sort) |
| [laya-jev-GraphRAG](laya-jev-graphrag.md) | Agentic GraphRAG with swappable Laya/Jev System One decisions across Neo4j/Memgraph/AGE/Kùzu. | Python · GraphRAG framework (Apache-2.0) |
| [llama-index-jev](llama-index-jev.md) | Rerank retrieved passages or choose a query engine in LlamaIndex. | Python · integration packages |
| [Milvus Model](milvus-model.md) | Score candidate documents with Jev Noul and return sorted results with original indices. | Python · PyMilvus model adapter |
| [mysql-ailike](mysql-ailike.md) | Filter and join MySQL rows with natural-language conditions via TypeSafe Jev (`AILIKE`). | MySQL · native UDF/plugin (v0.2.0, GPL-2.0) |
| [neo4jev](neo4jev.md) | Explore graph paths with typed next-hop and goal judgments. | Python · Neo4j, notebooks and Streamlit |
| [Note Filer](obsidian-note-filer.md) | Classify Obsidian notes with TypeSafe Jev and move them into Thema or IAB taxonomy folders after confirmation. | TypeScript · Obsidian desktop plugin (0BSD) |
| [pg-jev](pg-jev.md) | Ask semantic questions from SQL over database rows. | PostgreSQL · PL/Python extension |
| [pg_typesafe](pg-typesafe.md) | Call Choice/Noul/Score from SQL via a C+libcurl extension with batched multi-text helpers (pre-alpha; distinct from pg-jev). | PostgreSQL · C extension |
| [sgrep](sgrep.md) | Semantic grep: chunk a repo and ask TypeSafe Jev which chunks match a plain-English query (mock offline). | Python · CLI (`sgrep`) |
| [sieve](sieve.md) | Local MCP: enumerate repo/search candidates and score with TypeSafe Jev (`jev_grep` / `jev_rank` / `jev_search`). | Python · MCP server (`sieve` 0.1.0, uv) |
| [Truffler](truffler.md) | Rails intent search with TypeSafe Jev index-time labels, query understanding, and optional streamed reranking. | Ruby · Rails gem (MIT) |
| [webctl](webctl.md) | Agent web-search CLI: multi-provider results scored/judged (and optionally chunk-scored) with TypeSafe Jev. | Go · CLI (`webctl`) |

## Try a smaller example

The repository also maintains its own [teaching examples](../../../examples/README.md), [Support Router](../../../projects/support-router/README.md), and [routing evaluation runner](../../../evaluations/README.md). These are useful when you want a small offline starting point before adopting a community project.

## Share or improve a tool

Follow [Add a community project](../../../CONTRIBUTING.md#add-a-community-project) and the [project-page template](../../PROJECT_TEMPLATE.md). Put the full guide in this folder, list it once in a category above, and keep its upstream and guide links in the root README. Corrections to setup instructions and limitations are welcome.

Upstream maintainers own their code and licenses. Check each page's reviewed version and [validation scope](../../../docs/validation.md#community-project-checks); a listing does not establish production quality or endorsement.
