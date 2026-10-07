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
| [android-jev (FZ2000)](fz2000-android-jev.md) | Drive an Android phone over adb via MCP; TypeSafe Jev chooses each next action (distinct from jev-android/jevdevice). | Python · MCP server + skill (MIT) |
| [CloakBrowser-Agent](cloakbrowser-agent.md) | Stealth browser agent: TypeSafe Jev decides each step; CloakBrowser executes (MCP/CLI/Python). | Python · MCP/CLI/library (MIT) |
| [Cua jev-use](cua-jev-use.md) | Compose a bounded chooser with Driver and independent fixture verification. | Python / TypeScript · integration recipe |
| [CUA-JEV (ZJU-REAL)](cua-jev-zju.md) | Constrained computer-use loop: Jev selects typed action×channel candidates with guards and verifiers. | Python · framework (Apache-2.0) |
| [DepthJev](depthjev.md) | Embodied navigation with depth/text facts; TypeSafe Jev chooses EB-Navigation actions. | Python · EmbodiedBench agent (Apache-2.0) |
| [ego-decision-layer](ego-decision-layer.md) | Pluggable ego lite browser decision layer: one TypeSafe Jev System One call per step with fail-closed guards (measured benches). | JavaScript · skill/CLI (MIT) |
| [fast-browser](fast-browser.md) | Playwright browser automation for Codex/MCP with TypeSafe Jev (or Laya) decisions | Python · browser automation / MCP (MIT) |
| [firefox-jev-mcp](firefox-jev-mcp.md) | Claude plans; TypeSafe Jev picks Firefox element actions via MCP + WebExtension. | TypeScript · MCP + Firefox extension (MIT) |
| [Flick (flick-computer-use)](flick-computer-use.md) | MCP computer-use: Jev decides browser/macOS actions for whole goals. | TypeScript · MCP (MIT) |
| [Footwork](footwork.md) | Dual-process browser agent: TypeSafe Jev as System 1 in front of browser-use System 2, with a code-owned arbiter and evidence verification. | Python/Rust · package (`jevdual` 0.0.1) |
| [gpui-agent](gpui-agent.md) | Drive instrumented GPUI apps via accessibility: TypeSafe Jev chooses typed actions/targets (no screenshots to the model). | Rust/Python/TypeScript · experimental native toolkit |
| [InspireJev](inspire-jev.md) | Hand repetitive public-website steps (search, filter, collect, fill forms) to Jev-chosen actions while the host agent keeps the goal, authorization and verification. | Node.js · Playwright · release tarball (MIT) |
| [Jev Browser (openqa-cn)](openqa-jev-browser.md) | Indexed Playwright automation: TypeSafe Jev chooses control/op; replay, generate, explore, HTML reports (CodexQA skill). | TypeScript · CLI (`codexqa-jev-browser` 0.1.0, MIT) |
| [Jev Browser (tontoko)](jev-browser-tontoko.md) | Fill forms, extract records with evidence, and add semantic selection to Playwright tests. | TypeScript · SDK, CLI and MCP |
| [Jev Browser (Ying-Kai-Liao)](jev-browser-ying-kai-liao.md) | Run small browser goals with Jev action/target selection and direct inspection; page data and supplied values reach TypeSafe. | JavaScript · Playwright library, CLI and MCP |
| [Jev Browser Skill](jev-browser-skill.md) | Learn a minimal Jev-driven browser loop as a Claude Code/Codex skill (reference; see Ultrafast for fuller agents). | Agent skill + CDP scripts (`scripts/*.mjs`); explainer site |
| [Jev Ultrafast](jev-ultrafast.md) | Select browser operations and targets from the current page. | Python · browser agent and inspector |
| [jev-ui-test](jev-ui-test.md) | Natural-language UI tests: TypeSafe Jev scores candidate elements; pytest/Allure reports (fork of jev-ultrafast). | Python · pytest/Allure (MIT) |
| [Jev Voice Browser](jev-voice-browser.md) | Study partial speech, target disambiguation, and browser actions with an inspectable decision policy. | JavaScript · Playwright voice-control reference |
| [jev-android](jev-android.md) | Drive Android UI via accessibility with TypeSafe Jev or DeepSeek action choice (Kotlin SDK + sample). | Kotlin · Android SDK (`core`/`sdk`/`sample` 0.2.0) |
| [jev-browse (cooper667)](cooper667-jev-browse.md) | Claude Code plain-English Playwright QA checklist judged by TypeSafe Jev on Cloudflare Workers AI. | TypeScript · Claude Code plugin/skill (MIT) |
| [jev-browse (danielnc)](danielnc-jev-browse.md) | Fast Jev browser sub-tasks on browser-harness for coding agents. | Python · harness (MIT) |
| [jev-browser-bridge](jev-browser-bridge.md) | Plug any CDP browser (cloud/local/self-hosted, incl. no-render) into Jev browser automation. | Python · bridge (Apache-2.0) |
| [jev-browser-mcp (bothuany)](bothuany-jev-browser-mcp.md) | MCP browser: host intent → TypeSafe Jev clicks + cheap reader; DOM stays out of agent context. | JavaScript · MCP/Playwright (MIT) |
| [jev-browser-sidekick-mcp](jev-browser-sidekick-mcp.md) | Run plain-language browser steps via MCP; Jev picks the control; pairs with agentic-playwright-mcp for a shared Chrome session. | TypeScript · npm MCP (`jev-browser-sidekick-mcp` / `jev-bro`) |
| [jev-browser-skill (ChenYCL)](chenycl-jev-browser-skill.md) | Browser/computer-use CLI+MCP: TypeSafe Jev action choice (ego lite/Chrome/Safari); distinct from zurfyx/hqman. | Node.js ≥ 22 · CLI/MCP skill (MIT) |
| [jev-browser-skill (hqman)](hqman-jev-browser-skill.md) | Playwright Chromium skill/`jb` CLI: Jev chooses in-page actions (Gateway or TypeSafe); distinct from zurfyx teaching skill. | Node.js ≥ 22.18 · skill + CLI (`jb`, Apache-2.0) |
| [jev-browser-use (AuroraPixel)](aurorapixel-jev-browser-use.md) | Jev browser loops for Codex/Claude: warm Chrome daemon, CLI/MCP/extension, host handoffs. | Bun/TypeScript · CLI/MCP/extension (MIT) |
| [jev-chrome-mcp](jev-chrome-mcp.md) | MCP server wrapping jev-browser-use click loop in Google Chrome for Cursor/Codex. | JavaScript · MCP server (MIT) |
| [jev-computer-use-skill (Mrchen116)](mrchen116-jev-computer-use-skill.md) | Codex/agent skill: delegate repetitive computer-use judgments to TypeSafe Jev. | Python · agent skill (MIT) |
| [Jev-cu](jev-cu.md) | Study experimental Jev decisions over macOS Accessibility text in Codex; review the execution-policy limitations before use. | JavaScript · Codex skill and runtime |
| [jev-decide (abdullahaamuda)](abdullahaamuda-jev-decide.md) | Offload element picks, challenge detection, and routing from accessibility snapshots to TypeSafe Jev (~1s decisions). | Python · agent skill + stdlib CLI (`scripts/jev_ask.py`) |
| [jev-dom](jev-dom.md) | Drive any web page via DOM action space with TypeSafe Jev—no WebMCP required (Playwright peer). | TypeScript · research package (`jev-dom` 0.1.0, Apache-2.0) |
| [jev-flight-agent](jev-flight-agent.md) | Natural-language flight search in Chrome: TypeSafe Jev picks DOM actions; tiny LLM only types text. | Python · Playwright/CDP agent (MIT) |
| [jev-macos-loop](jev-macos-loop.md) | Automate native macOS GUI apps with local OmniParser/Vision perception and text-only Jev action choice. | TypeScript/Node · Apple silicon CLI |
| [jev-mcp (legostin)](legostin-jev-mcp.md) | Drive real Chrome via MCP: TypeSafe Jev picks elements/actions with calibrated confidence and HITL asks (distinct from jkudish judgment MCP). | TypeScript · MCP server (MIT) |
| [jev-phone](jev-phone.md) | Drive iOS/Android/cloud phones: TypeSafe Jev picks indexed UI actions; phone-use executes. | Bun/TypeScript · phone agent (MIT) |
| [jev-qa (moonshot-partners)](moonshot-partners-jev-qa.md) | Parallel browser QA: TypeSafe Jev-driven acceptance, adversarial, and smoke checks on web changes. | TypeScript · CLI (MIT) |
| [jev-ra](jev-ra.md) | Drive Chrome from Claude Code/Codex/MCP with TypeSafe Jev choosing each operation and target. | Python · MCP server, CLI and PyPI (`jev-ra` 0.1.1) |
| [jev-sim-use](jev-sim-use.md) | Jev-speed mobile UI navigation on sim-use (iOS/Android). | CLI · mobile (MIT) |
| [jev-ultrafast-skill (SherseaHe)](sherseahe-jev-ultrafast-skill.md) | Agent Skill package for bounded Jev Ultrafast Chrome automation (install via `npx skills add`); not the upstream runtime. | Python · Agent Skill + runner (MIT) |
| [jevbrief](jevbrief.md) | Filter Playwright elements with drop reasons; Jev Choice picks next click; local JSONL viewer. | Python · PyPI CLI (MIT) |
| [jevdevice](jevdevice.md) | MCP harness for Android (adb) or local shell: TypeSafe Jev (or local Laya) picks one runtime-discovered target per goal; code gates and executes. | Python · MCP server (`jevdevice` 0.1.0) |
| [jevnav](jevnav.md) | Automate browsers with Jev element choice, JSONL traces, risk gates, and offline CI replay. | Python · CLI/PyPI (`jevnav` 0.1.0, Apache-2.0) |
| [JevOnly](jevonly.md) | Drive a browser with pure Jev choices over code-built options—no planner or helper LLM. | Python · CLI, local viewer and Playwright |
| [JevPaper](jev-paper.md) | Mark arXiv abstract claims, delivering body sentences, and caveats with TypeSafe Jev (no summaries). | Chrome MV3 extension (GPL-3.0) |
| [jevpilot (bloudhood)](bloudhood-jevpilot.md) | MCP server: agent sends a goal; Jev drives Chrome step-by-step and returns a verified result or a question. | MCP · Chrome automation + TypeSafe Jev (MIT) |
| [macos-computer-use-kit](macos-computer-use-kit.md) | AX-first macOS computer use (MCP/CLI/pi/DSH) with optional TypeSafe Jev semantic guards before irreversible actions. | Python · PyPI MCP/CLI (MIT) |
| [Midscene JEV Runner](midscene-jev-runner.md) | Drive a caller-owned Playwright page with TypeSafe Jev via OpenRouter Decisions (`runJev` / Midscene `jevAct`). | TypeScript · npm (`@chlrc/midscene-jev-runner` 0.1.2, MIT) |
| [Mobile Jev](mobile-jev.md) | Navigate an Android device and verify a dark-theme task. | JavaScript / React · Mobilerun agent and studio |
| [Movo](movo.md) | Drive a Debian-family Linux desktop with AT-SPI candidates chosen by TypeSafe Jev (floating PySide6 agent). | Python · PySide6 + AT-SPI desktop agent (MIT) |
| [pi-Jev-browser](pi-jev-browser.md) | Let Jev choose each Playwright browser action over a structured DOM observation inside Pi. | TypeScript · Pi extension (npm) |
| [plain](plain.md) | Describe targets by role and visible text and assertions as claims; Jev picks elements and judges claims, with lock files and run modes to keep runs repeatable. | TypeScript · npm `@gabe4coding/plain` + Claude Code / Codex plugins (MIT) |
| [PlayJev (filed)](filedcom-playjev.md) | Add `page.act(...)`, `page.check(...)` style natural-language steps to Playwright tests and scripts, with Jev choosing from numbered page nodes. | TypeScript · npm `@filed/playjev` + Playwright (MIT, experimental) |
| [QAJev](qajev.md) | Run goal-driven exploratory tests with Jev choosing actions from the page text, separating product failures from harness problems, with HTML/MD/JSON reports and a live dashboard. | Python · CLI `qajev` + MCP (MIT) |
| [Sedum](sedum.md) | Mix plain-English steps with ordinary Playwright code; Jev returns probabilities for element resolution and claim checks while clicking, waiting, verdicts and exit codes stay deterministic. | TypeScript · npm `sedum-cli` + `@sedum-dev/provider-typesafe` (MIT) |
| [Surf CLI](surf-cli.md) | Drive Chrome from any agent; opt-in `semantic.find` / `semantic.act` let Jev pick the next allowed action and verify the goal (other commands never call TypeSafe). | TypeScript · npm CLI + Chrome extension + native host (MIT) |
| [Theme Tab Filter (jev-tab-filter)](jev-tab-filter.md) | Score Chrome tabs against a plain-English theme with TypeSafe Jev, then group/hide/window/close matches. | JavaScript · Chrome MV3 extension (MIT) |
| [tinycomputer](tinyhumansai-tinycomputer.md) | Drive desktop a11y and Chrome via a Rust TinyBus module; flows/tasks ask TypeSafe Jev many small questions (no screenshots). | Rust · TinyBus cdylib module (GPL-3.0) |
| [typesafe-computer-use](typesafe-computer-use.md) | Study OCR and Accessibility driven native macOS control. | Python · desktop CLI |
| [typesafe-computer-use-win](typesafe-computer-use-win.md) | Study OCR/UI Automation driven native Windows control with TypeSafe Jev decisions (`winclicker`). | Python · Windows desktop CLI |

## Customer feedback and marketing

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [call-eval](call-eval.md) | Score calls for satisfaction (1–5) and sentiment with an audit trail of transcript lines per number; runs offline or live against Jev. | Python · CLI package + static demo site (MIT) |
| [Jev Internal Links](jev-internal-links.md) | Claude Code skill: crawl sitemap paragraphs, TypeSafe Jev picks useful internal link targets, local rules + report. | Python · Claude Code skill (MIT) |
| [jev-linkedin-saved-classifier](jev-linkedin-saved-classifier.md) | LinkedIn saved-posts board classified into filters by TypeSafe Jev | Python · classifier board (MIT) |
| [Sales pipeline revival (Jev vs Gemini)](sales-pipeline-revival-jev.md) | Re-run Jev vs Gemini triage on 203 dead sales-deal threads with published metrics. | Python · benchmark harness + fixtures (MIT) |
| [Testimonial miner](testimonial-miner.md) | Find and review verbatim praise in email, grouped by product. | Python · CLI and local dashboard |
| [AnchorLint](anchorlint.md) | Audit internal links in built HTML: deterministic checks plus optional TypeSafe Jev promise/relevance judgments. | Python · CLI (`anchorlint`) |
| [Clay JEV People Ranker](clay-jev-people-ranker.md) | Qualify Clay people-search candidates with TypeSafe Jev Choice/Noul before enrichment (Agent Skill + Python script). | Python · Agent Skill + CLI script (`rank_clay_people.py`) |
| [jev-seo](jev-seo.md) | Local SEO/GEO CLI and MCP: DuckDuckGo SERP/audits plus optional TypeSafe Jev intent and visibility judgments. | Rust · CLI (`jev-seo`) and MCP |
| [jev-seo (AgriciDaniel)](agrici-jev-seo.md) | Live site SEO audit from one URL: crawl/rules/PageSpeed plus TypeSafe Jev judgments; PDF/XLSX/Markdown (distinct from Rust jev-seo). | Python · CLI (`jevseo` 0.1.1, MIT) + Claude skill |

## Developer tools

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Abide](abide.md) | Enforce project instruction rules on agent edits/turns with TypeSafe Jev per-rule probabilities (Claude Code/Codex/OpenCode/Pi). | TypeScript · agent hooks/CLI (`@coldtea/abide`, MIT) |
| [adecider](adecider.md) | CLI/MCP/HTTP/pi surfaces for multi-question System One judgments (local Laya default; optional Jev). | TypeScript · CLI + MCP + HTTP + pi (MIT) |
| [Agent Router](agent-router.md) | Quota-aware Herdr launcher: local eligibility then TypeSafe System One (Jev) picks agent/model/effort. | TypeScript · CLI (`@agent-router/router` 0.1.0) |
| [Agent Stack](agent-stack.md) | Local multi-agent team stack (OpenRig + Claude/Codex) with TypeSafe Jev typed merge/assignment decisions. | JavaScript · local stack (license unspecified at tip) |
| [agent-chaperone](agent-chaperone.md) | Calibrated MCP + hooks firewall: TypeSafe Jev screens tool calls/results with policy thresholds and a shadow log. | TypeScript · npm CLI (`agent-chaperone` 0.3.1, Apache-2.0) |
| [agent-evals](agent-evals.md) | Deterministic agent eval harness: rule scorers plus optional calibrated TypeSafe Jev judge as a CI gate. | TypeScript · npm CLI (`agent-evals` 0.1.0) |
| [agent-fastpath](agent-fastpath.md) | MCP decision layer: rules then TypeSafe Jev for ship/risk/triage/browser gates (files stay out of agent context). | TypeScript · npm CLI (`agent-fastpath` 0.2.0) |
| [AgentRun](agentrun.md) | Write agent workflows where Jev gates answers (for example, confidence ≥ 0.8 before replying), ranks candidates, or screens evidence; includes a Pi extension. | TypeScript · npm `@parcha/agentrun-dsl` + `@parcha/agentrun-jev` + `@parcha/agentrun-pi` (beta, Apache-2.0) |
| [agy-jevgate](agy-jevgate.md) | Fail-closed Antigravity PreToolUse hook: fast-pass + static guard + TypeSafe Jev risk score. | Python · agy plugin |
| [AlphaOptimizer](alphaoptimizer.md) | Compact large Codex/tool outputs locally and optionally rank chunks with TypeSafe Jev. | Node.js · TypeScript package (`alphaoptimizer` 0.1.0) |
| [ask-jev-skill](ask-jev-skill.md) | Call TypeSafe Jev as a Hermes typed tiebreaker (Choice/Score/Noul) when multiple paths remain. | Python · Hermes skill + stdlib CLI |
| [askjev](askjev.md) | Ask TypeSafe Jev via MCP (local or hosted) for calibrated Noul/Choice/Score over agent-held context. | TypeScript · MCP server (`askjev` 0.2.0) |
| [Astra-Ares](astra-ares.md) | Adapt GPT-6 Astra reasoning effort mid-Codex-task with TypeSafe Jev Choice (patched Codex CLI preview). | Node.js ≥ 22 · CLI (`astra-ares` / `ares` 0.2.1) |
| [atoma](atoma.md) | Submit a goal (report, data study, software) and watch agents produce and verify it, with Jev making bounded routing/approval decisions recorded on the timeline. | TypeScript · Node platform + web console (AGPL-3.0) |
| [auth-audit-jev](auth-audit-jev.md) | Shadow-mode Jev audit of allowlisted OAuth/IAM events with advisory alerts only (no enforce). | Python · EventPlugin + docs (MIT) |
| [AutoJev](autojev.md) | Route agent requests through a local AutoJev gateway; optional OpenRouter Jev model selection with local fallback. | Tauri/React/Rust · desktop gateway (AGPL-3.0-only) |
| [Auto Mode for Paseo](auto-mode-for-paseo.md) | Paseo plugin: TypeSafe Jev (or local Laya) picks Codex model/effort/mode/speed per turn. | TypeScript · Paseo plugin 0.2.0 |
| [autoloop](autoloop.md) | Automate issue-board triage and implementation; turn on `[jev] mode = "shadow"` to log Jev's typed view of each triage/auto-merge decision without changing behaviour. | Python · CLI (`uv tool install`) (Apache-2.0) |
| [AutoRouter (claude-autorouter)](claude-autorouter.md) | Use cheaper Claude models for simple coding turns in one session, with Jev as an optional hosted evaluator. | Node.js 22+ · npm `claude-autorouter` (Apache-2.0) |
| [beam-cli](beam-cli.md) | Local AgentBeam hooks/policy for coding agents; optional TypeSafe Jev Noul/Score action judging (off by default). | TypeScript · npm CLI (`@agent-beam/beam` 0.2.16, AGPL-3.0) |
| [bekko-system-one](bekko-system-one.md) | Small System One decision models (17M–400M) for Yes/No, Choice, and Score (independent open weights). | Python · local models (MIT) |
| [bitrate-advisor](bitrate-advisor.md) | Choose live-stream encoder bitrate/resolution/next-step with TypeSafe Jev via OpenRouter inside deterministic guardrails. | TypeScript · Deno/Node library (`@affirmi/bitrate-advisor` 0.2.7) |
| [Blackrose](blackrose.md) | Run typed TypeSafe System One checks and return allow/review/block with scores in app code. | Python + JS packages (MIT) · TypeSafe Jev |
| [BoundedCode](boundedcode.md) | Local OpenCode coding on 8 GB GPUs with a required TypeSafe Jev decision plane and Go verification gates. | Go · OpenCode supervisor (Apache-2.0) |
| [BrighTO Router](brighto-router.md) | Self-host a Rust LLM gateway with OpenAI/Anthropic-compatible routes plus System One/Jev/DJEV/Laya decision routing, load balancing, and budgets. | Rust · Docker gateway (`thusinh1969/brighto_airouter`, Apache-2.0) |
| [btx-skill-jev-judge](btx-skill-jev-judge.md) | Claude Code plugin: hand repeated judgments to TypeSafe Jev from a tested script. | Claude Code plugin (MIT) |
| [cai](cai.md) | Ask Jev yes/no, choice, score or multi-question judgments from the shell on piped text alongside cai's chat, image, OCR and other commands. | Rust · CLI (build from Git for Jev; ISC) |
| [Cairn Jev Lab](cairn-jev-lab.md) | Test memory-admission policies with TypeSafe Jev judgments and inspectable save/skip/defer recommendations. | Node.js ≥ 22 · lab/CLI/playground (`cairn-jev-lab` 0.1.0) |
| [Candidate Experience Feedback Benchmark](candidate-experience-benchmark.md) | Compare TypeSafe Jev vs LLMs on 60 synthetic candidate-experience reviews (four typed tasks). | HTML · evidence packs + explorer (MIT) |
| [Canny](canny.md) | Stop Claude Code/Codex “done” claims without ledger evidence; TypeSafe Jev advises, only facts block. | TypeScript · CLI (`canny-warden` 0.1.0), zero runtime deps |
| [CanvasTTY Assistant](canvastty-plugin-assistant.md) | Review agent commands and triage launches in CanvasTTY with System One (Jev/Laya/Eikos) decisions. | CanvasTTY plugin · System One (MIT) |
| [Captain Code](captaincode.md) | Route coding tasks to the cheapest capable agent; optional Jev triage/gating (`captain jev`, `captain jev shadow`). | Go · CLI (`captain`) (MIT) |
| [catherd](47vigen-catherd.md) | Autopilot coding-agent herds where TypeSafe Jev picks which model writes while Claude plans/verifies. | TypeScript · orchestrator (MIT) |
| [changelog-bot](changelog-bot.md) | Generate changelog entries from releases; add `--why --why-engine jev` (or `why-engine: jev` in the Action) so WHY notes come only from evidence Jev accepts. | TypeScript/Node · npm CLI (`@nyaomaru/changelog-bot`) + GitHub Action (MIT) |
| [chatwoot-workers](chatwoot-workers.md) | Chatwoot Cloudflare Workers: Discord relay + TypeSafe Jev ticket triage router. | TypeScript · Cloudflare Workers (MIT) |
| [chinese-workflow-decision-bench](chinese-workflow-decision-bench.md) | Benchmark Feishu-style Chinese message triage with frozen Choice/four-Noul tracks and published Jev vs Laya results. | Python · bench harness + adapters |
| [classifier.dev](classifier-dev.md) | Classify text with `curl https://classifier.dev/<labels>/<text>` or the `classify` CLI; Jev returns the label and confidence (`src/jev.ts`). | TypeScript · Cloudflare Worker + npm CLI (`classifier-dev`) (MIT) |
| [claude-referee](claude-referee.md) | Gate risky Claude Code tool actions with TypeSafe Jev referee judgments. | TypeScript · Claude Code plugin (MIT) |
| [claude-risk-router](claude-risk-router.md) | Route Claude Code tasks across Opus/Sonnet/Haiku using TypeSafe Jev risk judgments. | Python · Claude Code add-on (MIT) |
| [Claude x Jev](claude-x-jev.md) | Claude Code skill: Jev classify/route/gate via OpenRouter; Claude deep-reads only unsure items. | Python/npm · Claude Code skill (`claude-x-jev`, MIT) |
| [claude-code-jev](claude-code-jev.md) | Claude Code PreToolUse gate: TypeSafe Jev via OpenRouter Decisions classifies allow/block/ask with fixture benchmarks. | Python · CLI/hook (`jev-auto-mode` 0.1.0) |
| [claude-jev (darwintechlab)](darwintechlab-claude-jev.md) | Claude Code plugin/MCP: live TypeSafe Jev Choice/Noul/Score with auto/escalate confidence labels. | TypeScript · Claude plugin/MCP (MIT) |
| [claude-jev-funnel](claude-jev-funnel.md) | Bulk TypeSafe Jev funnel for Claude Code: resolve confident YES/NO in code; escalate only the uncertain band. | Python · Claude plugin + CLI (Apache-2.0) |
| [claude-router (alexei-led)](alexei-led-claude-router.md) | Local Anthropic gateway: Jev routes micro/low/medium/high tiers for Claude Code. | TypeScript · npm gateway plugin (MIT) |
| [clear-head](clear-head.md) | Claude Code Stop hook: TypeSafe Jev checks answer claims against what was read this session. | Python · Stop hook + install scripts |
| [cmd-mod-jev-nudge](cmd-mod-jev-nudge.md) | Command Code stop-hook mod: TypeSafe Jev judges whether unfinished work warrants a continue nudge. | TypeScript · Command Code mod (`cmd-mod-jev-nudge` 0.1.0) |
| [Code Quality (smixs)](code-quality.md) | Run deterministic checks (complexity, CRAP, coverage, secrets, weakened tests, hook bypasses) on each change; with `[review] jev = true` Jev flags textual tests, untested error paths and other hunk-level smells as notes. | TypeScript/Bun · agent plugin + git hooks (MIT) |
| [Codex Jev Preflight](codex-jev-preflight.md) | Fail-open Codex UserPromptSubmit hook: TypeSafe Jev advisory task_type/complexity/risk/execution_mode. | Python · stdlib hook + installer |
| [Codex Jev Router (suenot)](codex-jev-router-suenot.md) | Choose Codex subagent model and reasoning effort with Jev Choice/Noul decisions and local confidence gates. | Node.js · CLI + installer |
| [Codex-Jev](philippelhaus-codex-jev.md) | VS Code Codex plugin that shortens noisy tool results with Jev-gated evidence selection before Codex reads them. | Python · VS Code Codex plugin (MIT) |
| [codex-jev-router](codex-jev-router.md) | Route OpenAI Codex CLI turns through TypeSafe Jev model/effort selection via a local Responses proxy (fail-open). | Node.js · CLI (`codex-jev` 0.1.0) |
| [codex-triage](codex-triage.md) | Local Codex task triage dashboard with human-reviewed archiving and optional TypeSafe Jev analysis. | TypeScript · local app (MIT) |
| [Codify (cg)](codify.md) | Plan-to-proof agent workflow CLI; `cg jev` and `cg memory classify` use Jev Noul/Choice/Score answers (advisory, never changes exit codes). | C/Go static binary · CLI + MCP tools (MIT) |
| [Coding Router Jev](coding-router-jev.md) | Route Codex, Claude Code or Pi turns to cheaper or stronger models per request, with explicit overrides and routing notices. | TypeScript · Bun (release binaries need no Bun) |
| [ComfyUI-ScriptFlow](comfyui-scriptflow.md) | ComfyUI script node: ask TypeSafe Jev yes/no/choice/score and branch workflows (GGUF fallback). | Python · ComfyUI custom node (GPL-3.0) |
| [compact-adviser](compact-adviser.md) | Ask TypeSafe Jev whether a coding session is at a safe `/compact` boundary; hint or optional auto-compact on Pi/Claude Code. | Node.js ≥ 22 · npm plugins (`compact-adviser` 0.1.6) |
| [Copilot Studio × Jev](copilot-studio-jev.md) | Gate Azure AI Search passages with four Jev Noul questions per hit so Copilot Studio answers with citations or abstains; optional Power Platform connector. | TypeScript MCP + Power Platform connector (MIT) |
| [daf-jev](daf-jev.md) | Build typed Jev questions, gates, batch evaluation, and optional MCP tools in Python. | Python · library/CLI (`daf-jev` 0.3.0) |
| [Damocles](damocles.md) | Use the coding agent with persistent memory; add a TypeSafe key so Jev decides whether a new fact supersedes an old one and grades memories for recall. | TypeScript · VS Code extension + Electron desktop app (MIT) |
| [Data Agent MNIST (ClickHouse)](data-agent-mnist.md) | Generate and grade text-to-SQL agent tasks on your warehouse; with `--extra jev`, rank tables by how likely each is needed and label failed cells by sub-mode and preventing rule. | Python · uv project and scripts (Apache-2.0) |
| [dbt_jev](dbt-jev.md) | Classify SQL values with TypeSafe Jev (or OpenRouter→Jev) from dbt macros on DuckDB/ClickHouse. | Python · dbt package + DuckDB/ClickHouse runtime |
| [DecideKit](decidekit.md) | Define typed decision policies and evaluate them with Jev via OpenRouter or TypeSafe, with offline fixtures and fallbacks. | TypeScript/Python · library/CLI (`decidekit` 0.1.0) |
| [Decision Tagger (Obsidian)](obsidian-decision-tagger.md) | Tag Obsidian notes with TypeSafe Jev System One rules; single-note and vault/folder batch with multi-key concurrency. | JavaScript · Obsidian plugin (MIT) |
| [decision-first](decision-first.md) | Spot bounded judgments, try TypeSafe Jev first, and log adopt/decline cases for reuse. | Python · agent skill + stdlib scripts |
| [Deeds](deeds.md) | Report capabilities shipped per week/author for a repo (`deeds analyze . --since 30d`), with terminal, HTML, or JSON output. | TypeScript · Bun CLI + Claude Code plugin (MIT) |
| [DeepSeek Harness for VS Code](dsh-vsc-integration.md) | Turn on Jev (or wire-compatible Laya) inside DSH sessions to catch loops, fold noisy tool output, and check completion claims. | TypeScript · VS Code extension (MIT) |
| [deepseek-harness-jev (luobosibing2)](luobosibing2-deepseek-harness-jev.md) | DSH plugin: TypeSafe Jev for skill/file ranking, supervision, corrections, and workspace approval (off by default; ≠ wjw66 pre-compaction). | TypeScript · DSH/Cordis plugin (MIT) |
| [demo-expanso-jev](demo-expanso-jev.md) | Run Expanso Edge pipelines that bypass routine lines and ask TypeSafe Jev only on the rest (boards + mock server). | Demo suite · Expanso YAML, Python boards, `just` recipes |
| [deslop](deslop.md) | Score page bodies with TypeSafe Jev probabilities for ad/slop/seo/derivative (caller sets thresholds). | Python · agent skill + stdlib CLI |
| [Discern](discern.md) | Build Effect Decision/DecisionModel patterns, policies, and procedures; optional TypeSafe Jev provider. | TypeScript · npm (`@doeixd/discern` 0.4.0) |
| [discoprint](discoprint.md) | Classify an artist discography for theme/mood/lyrical complexity with TypeSafe Jev and render an Ink terminal dashboard. | TypeScript · npm CLI (`discoprint` 0.1.0) |
| [Distill](distill.md) | Route coding-agent model/effort and utility/retention choices with TypeSafe Jev (or OpenRouter decisions) inside a local TUI harness. | Rust · coding agent CLI/TUI (Distill 2.0) |
| [doc-router](doc-router.md) | Select which PDF pages need OCR using optional Jev judgments, then merge local extraction and provider results. | Rust · library and CLI, Python bindings |
| [DocJev](docjev.md) | Classify or split PDF/DOCX/PPTX packets with LiteParse text and TypeSafe Jev category/boundary judgments. | Python · CLI/library (`docjev`, Apache-2.0) |
| [dsh-auto-review-jev (sperictao)](sperictao-dsh-auto-review-jev.md) | DeepSeek Harness Auto-permission: TypeSafe Jev reviews each tool call (≠ xlennart). | TypeScript · DSH plugin (MIT) |
| [dsh-jev](dsh-jev.md) | Register `jev_ask` on DeepSeek Harness so agents can send typed noul/choice/score questions to TypeSafe Jev (install from GitHub pin). | TypeScript · DSH plugin (`dsh-jev` 0.1.0) |
| [dsh-jev-context-gate](dsh-jev-context-gate.md) | DeepSeek Harness preflight + evidence-aware review/skill gates via TypeSafe Jev. | JavaScript · DSH plugin (MIT) |
| [dsh-jev-decide](dsh-jev-decide.md) | Register DSH agent tool `jev_decide` for TypeSafe Jev noul/choice/score over text state (distinct from dsh-jev / verify / prune). | TypeScript · npm plugin (`dsh-jev-decide` 0.1.1) |
| [dsh-jev-gate](dsh-jev-gate.md) | Catch work that only looks finished (unreported, no evidence, skeleton, unauthorized downgrade) in DSH agent teams, with Jev as an optional external adjudicator. | TypeScript · DSH plugin (MIT) |
| [dsh-jev-interceptor](dsh-jev-interceptor.md) | DeepSeek Harness: Jev risk classification on tool calls plus optional semantic session-reference retention. | TypeScript · DSH plugin (MIT) |
| [dsh-jev-kit](dsh-jev-kit.md) | DeepSeek Harness plugin: ~23 named TypeSafe Jev advisory judgments (privacy scan, scope, memory/batch triage) without hooks. | TypeScript · DSH plugin (`@dsh-external/dsh-jev-kit` 0.13.0) |
| [dsh-jev-loop](dsh-jev-loop.md) | TypeSafe Jev judgments at DeepSeek Harness agent-loop gates (no UI dependency). | TypeScript · DSH plugin (MIT) |
| [dsh-jev-plugin (jackie-cqz)](jackie-cqz-dsh-jev-plugin.md) | DeepSeek Harness plugin: TypeSafe Jev noul/choice/score tools, guardrails, and Web UI result cards (distinct from other dsh-jev*). | TypeScript · DSH plugin npm package (MIT) |
| [dsh-jev-plugin (luobosibing2)](luobosibing2-dsh-jev-plugin.md) | DeepSeek Harness: TypeSafe Jev for skill/file ranking, supervision, corrections, and workspace approvals (distinct from other dsh-jev*). | JavaScript · DSH Cordis plugin (MIT) |
| [dsh-jev-prune](dsh-jev-prune.md) | Replace DSH size-only pruning and model summaries with TypeSafe Jev keep/drop judgments plus deterministic receipts. | JavaScript · DSH plugin (`dsh-jev-prune` 0.1.0) |
| [dsh-jev-thinking](dsh-jev-thinking.md) | Ask Jev how deep a DSH prompt needs to think; write the chosen level into reasoningEffort using only route-offered options. | TypeScript · DSH/npm plugin (`dsh-jev-thinking`, MIT) |
| [dsh-jev-verify](dsh-jev-verify.md) | Call TypeSafe Jev choice/score/noul from DSH and run a live labeled verification benchmark (honest, no mock mode). | JavaScript · DSH plugin (`dsh-jev-verify` 0.1.0) |
| [dsh-plugin-jev-compaction](dsh-plugin-jev-compaction.md) | Compact DSH context by Jev relevance scores instead of age; pin constraints/tracebacks; fall open to stock on endpoint failure. | TypeScript · DSH plugin / npm (MIT) |
| [DuoMind](duomind.md) | OpenAI-compatible local LLM proxy: small local model generates; TypeSafe Jev makes System One decisions along the way. | Python · llama.cpp local server + TypeSafe Jev (MIT) |
| [Edward](edward.md) | Wrap an agent run (`edward wrap -- pi "task"`) so loops, budget bleed, dangerous commands and stalls trigger resumable PAUSE or CANCEL/BLOCK, with Jev (or a local 4B scorer) judging continue/pause/escalate. | Python 3.11+ · PyPI `edward-guard` CLI (MIT) |
| [effortless](effortless.md) | Let easy prompts run at low effort and hard ones at high without touching the Effort control, using Jev as a fast judge when you have a key. | TypeScript · Claude Code plugin (MIT) |
| [Engraphis](engraphis.md) | Durable coding-agent memory across sessions; optional advisory Jev decisions (`ENGRAPHIS_DECISION_BACKEND`, pinned `jev-1.13.0`). | Python · pip package + MCP server + WebUI (Apache-2.0) |
| [enowx](enowx.md) | Hand small typed judgments in an agent team to Jev (`jev-latest`), Cloudflare Clef (the default provider), a compatible endpoint, or a configured LLM, each with its own switch and threshold. | Rust · CLI binary (macOS/Linux/Windows releases) (Apache-2.0) |
| [Eutrya](eutrya.md) | Run a CLI agent loop where TypeSafe Jev picks attention modes and scores candidates; text model proposes; offline demo included (alpha). | Node.js · CLI (`eutrya` 0.4.9) |
| [evidence-referee](evidence-referee.md) | Evidence-over-eloquence Claude Code plugin: Jev done-gates and judgment receipts (≠ claude-referee). | Claude Code plugin (MIT) |
| [ExcelPilot](excelpilot.md) | Drive live Excel workbooks with Qwen planning and TypeSafe Jev intent/tool gates (cascade to OpenRouter/offline). | Python · Office.js add-in + FastMCP agent (`excelpilot` 1.0.0) |
| [fastcampus-jev](fastcampus-jev.md) | Learn TypeSafe Jev in Korean via notebooks and a Teddy Market customer-support LangGraph demo (tool choice, guardrails, risk gates, RAG). | Python 3.12 + LangGraph + React (MIT) |
| [fast-jev-compaction](fast-jev-compaction.md) | Select which old tool calls and results remain in agent context. | TypeScript · library and Claude Code plugin |
| [fast-jev-opencode](fast-jev-opencode.md) | Prune stale OpenCode V2 tool calls/results on the outgoing request with TypeSafe Jev (fail-open; does not rewrite history). | TypeScript · OpenCode plugin (`fast-jev-opencode` 0.1.0) |
| [fast-jev-compaction-opencode](fast-jev-compaction-opencode.md) | opencode session compaction with probabilistic keep/drop (local LM Studio judge by default). | TypeScript · opencode plugin (MIT) |
| [fast-jev-opencode (roshan-shaik-ml)](roshan-shaik-ml-fast-jev-opencode.md) | Prune stale OpenCode tool calls/results with TypeSafe Jev on the outgoing request only (v1+v2 adapters). | JavaScript · OpenCode plugin (MIT) |
| [FAVA Trails](fava-trails.md) | Gate which agent conclusions become shared memory with a calibrated Jev check and an inspectable review record. | Python · PyPI `fava-trails` · MCP server (Apache-2.0) |
| [fndds-matcher-jev](fndds-matcher-jev.md) | Match food descriptions to USDA FNDDS codes via hybrid retrieval plus TypeSafe Jev. | Python · matcher (MIT) |
| [Foreman](foreman.md) | Experiment with Jev supervision of Codex workers and inspect steering, retry, and verification decisions. | Python · CLI and supervision runtime |
| [Formanator](formanator.md) | Submit Forma benefit claims from CLI/MCP; optional TypeSafe Jev picks benefit/category (receipt LLM separate). | Rust · CLI/MCP (`formanator` 5.4.0) |
| [fr (Arindam200)](arindam200-fr.md) | Ask a codebase question and get relevant files via live parallel TypeSafe Jev relevance. | CLI · code relevance (MIT) |
| [fusion-jev](fusion-jev.md) | Local coding evidence plus optional guarded TypeSafe Jev choices for MCP hosts. | TypeScript · MCP (MIT) |
| [Gatekeeper](gatekeeper.md) | Route Claude Code prompts to the right skill/agent with YAML rules plus TypeSafe Jev Choice verdicts. | Python · Claude Code hooks (MIT) |
| [ghtriage](ghtriage.md) | Classify GitHub issues with TypeSafe Jev typed labels/confidence and code-owned write guards (`ghtriage`). | Python · CLI (`ghtriage` / `jev-issue-classifier` 0.1.0) |
| [git-jev-stage](git-jev-stage.md) | Classify Git hunks against a plain-language staging intent with TypeSafe Jev, then stage confirmed blocks. | TypeScript · CLI (`git-jev-stage` 0.1.1) + skill |
| [Graphlin](graphlin.md) | Live architecture/activity diagrams for Claude Code or Codex; optional TypeSafe Jev classification of graph evidence. | Node.js · CLI/viewer (`npx graphlin`), plugins |
| [grev](grev.md) | Grep, label, rank, sort, and guard text by meaning in pipelines (for example a semantic pre-commit secret guard with `isv`). | Go · CLI suite with man pages and shell completions (Apache-2.0) |
| [Grok Bot Jev](grok-bot-jev.md) | Gate Grok Bot research/browser/retry/subagent work with TypeSafe Jev actions (shadow or active skill mode). | Python · router, skill template and dry-run CLI |
| [guardrails-md](guardrails-md.md) | Block destructive, secret-leaking or rule-breaking agent commands in about 100 ms, with the reason returned to the agent. | TypeScript · npm `@bergetai/opencode-guardrails-md` (MIT) |
| [guesswork](guesswork.md) | zsh history autosuggestions ranked by TypeSafe Jev instead of prefix match | TypeScript/zsh · shell plugin (MIT) |
| [hak-jev-plugin](hak-jev-plugin.md) | Hedera Agent Kit policy: TypeSafe Jev gates swaps before sign; decisions notarized to HCS. | TypeScript · npm (`hak-jev-plugin`, MIT) |
| [grok-jev-guard](grok-jev-guard.md) | Prefight Grok Bot tool sequences: local hard rules + TypeSafe Jev ambiguity judgments (shadow-first). | Python · CLI + skill (`grok-jev-guard` 0.1.0, MIT) |
| [harness-router](protocol-lattice-harness-router.md) | Route agent-harness tool selection with TypeSafe Jev over MCP, plus MCTS for multi-step decisions. | Python · MCP (MIT) |
| [HearMemory](hearmemory.md) | Share project memory across coding agents; TypeSafe Jev judges claims against tests/diffs/commits. | Python · MCP/hooks (MIT) |
| [HekaJev](hekajev.md) | Ask reproducible Git-history analytics questions; TypeSafe Jev classifies commits with saved evidence/cost. | Python · CLI (`hekajev`, MIT) |
| [here-we-go-jev](creativoma-here-we-go-jev.md) | One-page UI and scripts to run System One questions against OpenRouter/TypeSafe Jev, an LLM baseline, or a mock `/v1/systemone`. | TypeScript · Bun (`bun run dev`) |
| [Hermes Jev Skills](hermes-jev-skills.md) | Add Jev model routing, memory filter, compaction, skill pick, triage, and computer/browser choices to Hermes, Claude Code, and Codex. | Python · skills, `jev` CLI and Hermes plugin |
| [hermes-adaptive-model-router](hermes-adaptive-model-router.md) | Collect calibrated fast-vs-capable route decisions for human turns in Hermes Agent before ever enabling automatic switching. | Python · Hermes Agent plugin (MIT) |
| [hermes-jev (ourines)](ourines-hermes-jev.md) | Add an explicit Jev decision sidekick (tools + skill) to Hermes Agent across TypeSafe, Cloudflare, and OpenRouter backends. | Python · Hermes plugin (MIT, prerelease) |
| [hermes-jev-curator](hermes-jev-curator.md) | Typed Jev skill-relationship judgments and safe archive/guard plans for Hermes Agent’s background skill curator. | Python · Hermes plugin (experimental 0.1.0) |
| [hermes-jev-helper](hermes-jev-helper.md) | Hermes `pre_llm_call` plugin: TypeSafe Jev (OpenRouter Decisions) classifies intent route before the agent improvises. | Python · Hermes plugin (MIT) |
| [hermes-jev-lesson-gate](hermes-jev-lesson-gate.md) | Hermes background review gate: TypeSafe Jev decides when memory/skill review should run. | Python · Hermes plugin (MIT) |
| [himalaya-jev-mail-classify](himalaya-jev-mail-classify.md) | CLI `mail-classify`: himalaya Gmail threads → TypeSafe Jev labels/colours via OpenRouter (dry-run default). | Python · CLI (`mail-classify` 0.1.0, MIT) |
| [HiRoute](hiroute.md) | Local-first agent routing engine with TypeSafe Jev decision extensions for branch selection | Rust · routing engine (Apache-2.0) |
| [hookgate](hookgate.md) | Gate Claude Code/Codex shell and Stop hooks with TypeSafe Jev (audit mode, fail-open). | Node.js ≥ 18 · CLI/plugin (`hookgate` 0.0.2) |
| [hyalo](hyalo.md) | Manage and query a Markdown knowledgebase from the CLI; during tidy, ask Jev for type/folder suggestions on chosen notes instead of letting the agent guess. | Rust · CLI (Homebrew, apt, dnf, AUR, Scoop, winget, Cargo, npm) + agent plugin/skills (MIT) |
| [Intent-Router](intent-router.md) | Compile vague agent requests into typed IntentSpec contracts (probe, ask, or halt) before Jev/Laya routing. | Agent Skill (`intent-router` 0.3.0, MIT) |
| [invalidate](invalidate.md) | Check every stored agent memory against new evidence with TypeSafe Jev; mark superseded facts without rewriting text. | Python · library, CLI and memory adapters |
| [is-malicious](is-malicious.md) | Scan a codebase for deceptive or data-stealing behavior with TypeSafe Jev file/line findings. | TypeScript · npm CLI (`is-malicious` 0.1.0) |
| [J++](jpp.md) | Experimental language/Rust runtime composing Jev questions with exact methods; offline fixtures and Towow demos. | Rust · `jpp-cli` + Python reference |
| [japanese-jev-lint](japanese-jev-lint.md) | Lint Japanese prose with TypeSafe Jev Noul flags (typo/twist/length/repeat) plus regex です/ます checks; no rewrites. | Go · CLI (`jjl`) |
| [JCR](jcr.md) | Resolve deterministic commands from a nested capability tree with TypeSafe Jev (MCP + Claude/Codex harnesses). | TypeScript · resolver, MCP and harnesses (`jcr` 1.0.0) |
| [Jeffort](jeffort.md) | Set Claude Code effort per turn from TypeSafe Jev scores (depth/scope/stakes/ambiguity); leave /effort alone on low confidence. | Claude Code plugin (MIT) |
| [JEV Book Tags](jev-book-tags.md) | Tag Calibre books with TypeSafe Jev (single-book and batch classification). | Python · Calibre plugin (GPL-3.0-or-later) |
| [JEV Codex Pilot](jev-codex-pilot.md) | Local Codex Kanban workspace with Jev-model routing, contextual compaction, and ticket lifecycle control. | TypeScript · desktop/workspace (MIT) |
| [Jev Foundry Judge](jev-foundry-judge.md) | Score Azure AI Foundry agent traces with TypeSafe Jev evaluators (intent/adherence/tools/groundedness) and optional model router. | Python · Azure AI Foundry evaluators + demo (MIT) |
| [Jev Skills (n23eos)](n23eos-jev-skills.md) | Install skills such as `jev-skill-picker`, `jev-test-prioritizer`, `jev-bug-triage` and `jev-plan-selector`; automatic routing stays off unless you enable it. | Python 3.10+ · uv tool CLI (`jev-skills`) + agent skills (MIT) |
| [jev-answers](jev-answers.md) | Ask TypeSafe Jev about files via MCP/CLI and keep each request's raw answer in a session folder. | TypeScript · MCP + CLI (MIT) |
| [jev-cc-codex-router](jev-cc-codex-router.md) | Route each Codex turn via TypeSafe Jev tier choice, rewrite the model, and retry flaky upstream errors. | TypeScript · Codex proxy (MIT) |
| [jev-compaction-plus](jev-compaction-plus.md) | Claude Code compaction with TypeSafe Jev keep/drop plus a drawer file for dropped tool outputs (fork of fast-jev-compaction). | TypeScript · Claude Code plugin (MIT) |
| [Jev Cookbook (Datawhale)](jev-cookbook.md) | Learn TypeSafe Jev / System One in Chinese via notebooks, recipes, and docs translation (CC BY-NC-SA 4.0; non-commercial). | Jupyter + docs site (CC BY-NC-SA 4.0) |
| [jev-cops](jev-cops.md) | Police coding-agent tool calls in context with graduated allow/annotate/rewrite/hold/deny/kill verdicts; optional Jev semantic judge. | TypeScript/Bun · npm (`jev-cops`, Apache-2.0) |
| [jev-decision-kit (kdcadmin)](kdcadmin-jev-decision-kit.md) | Local skill/plugin cabinet: an on-device Jev head selects which skills to preface before the chat model speaks (≠ DecisionKit .NET). | Python · local web + host hooks (MIT) |
| [jev-dotnet](jev-dotnet.md) | Unofficial typed C# client for the Jev System One API (Choice/Score/Noul). | C# · .NET client (MIT) |
| [Jev for Claude Code (brookcs3)](brookcs3-jev-system-one-for-claude.md) | Use TypeSafe Jev as a Claude Code tool for typed judgments and corpus→eval loops (unofficial). | Claude Code plugin (MIT) |
| [jev-gateway-bench](jev-gateway-bench.md) | Compare coding-agent cost/quality with jev-gateway Jev routing on vs off on chess-engine tasks. | JavaScript · bench harness (MIT) |
| [jev-gateway (TexasOct)](texasoct-jev-gateway.md) | Route OpenAI-compatible chat across providers with strategies and optional typed Choice decision providers (AGPL). | Python 3.12+ · gateway + dashboard (AGPL-3.0) |
| [jev-herdr](jev-herdr.md) | Spawn Claude Code agents in Herdr with TypeSafe Jev choosing model and effort per agent. | TypeScript · Herdr integration (MIT) |
| [jev-judge](jev-judge.md) | Run cheap, structured output checks in CI with thresholds, using Jev as the judge. | Python · CLI `jev-judge` (MIT) |
| [jev-llm-guard](jev-llm-guard.md) | Guard LLM inputs/outputs against OWASP LLM risks with TypeSafe Jev judgments (Turkish demo). | TypeScript · web demo (MIT) |
| [jev-map](jev-map.md) | Find related tests for a function (`related-tests`, MCP `serve`); `--jev` adds Jev-scored links with a call budget. | Python · CLI + MCP server (MIT) |
| [jev-mcp-router (ini8labs)](ini8labs-jev-mcp-router.md) | Let Jev select MCP servers/tools per request instead of loading every tool schema into the LLM context. | Python · uv MCP gateway (MIT) |
| [jev-navigator](jev-navigator.md) | Let coding agents find code through closed Jev judgments over candidates the index built, with raw probabilities and partial results, while code owns goals and stopping. | Python 3.11+ · `jvn` CLI · optional `typesafe` extra |
| [jev-qa-demos](jev-qa-demos.md) | Learn TypeSafe Jev for QA/SDET with commented TypeScript demos (Vercel AI Gateway + local Ollama). | TypeScript · demo scripts (source available; no LICENSE file) |
| [jev-query](jev-query.md) | Answer analytics questions over Postgres with SQL that is valid by construction, read-only and parameterized, using Jev only to choose among legal plan moves. | TypeScript · Node ≥ 20 · `pg` or PGlite |
| [jev-router-mcp](jev-router-mcp.md) | Route agent questions to tools with a Jev-compatible `/v1/systemone` MCP server (Laya-friendly). | Node.js · npm MCP (`@humayunkabir/jev-router-mcp`, MIT) |
| [jev-secret-guard](jev-secret-guard.md) | Stop Claude Code from writing/committing secrets: local regex blocks plus masked TypeSafe Jev judgments. | JavaScript · Claude Code hook (MIT) |
| [jev-tokensaver](jev-tokensaver.md) | Cut coding-agent context spent on reading by letting Jev pick the lines and files that matter, with the full output kept on disk. | Python (uv) · CLI + MCP server + Claude skill |
| [jevkit (bragamat)](bragamat-jevkit.md) | Let agents locate the relevant lines, verify claims and make calibrated judgment calls with Jev, logging every decision locally; optionally steer tool choice through a passthrough-on-doubt gateway. | Go · CLI `jev` + Agent Skill / Claude Code plugin (MIT) |
| [Jevlint (codegirl-007)](codegirl-007-jevlint.md) | Codify code-taste rules in plain language; Tree-sitter extracts units and Jev returns pass/fail per rule (`jevlint check`). | Go · CLI + rule-pack plugins (MIT) |
| [jevmem (illescasDaniel)](illescasdaniel-jev-mem.md) | Store/recall agent notes with Jev admission/typing/relevance; MCP + Claude Code hooks + CLI over SQLite (fails open). | Python 3.12+ · MCP/hooks/CLI (`jevmem`, MIT, beta) |
| [Jev Mode](tiffygk-jev-mode.md) | Claude Code skills/study course for building with TypeSafe Jev (PolyForm Noncommercial; commercial use restricted). | Claude Code skills (PolyForm Noncommercial 1.0.0) |
| [Jev Observer](jev-observer.md) | Proxy and inspect TypeSafe Jev decisions locally with history, question versions, latency, and cost estimates. | Rust · local proxy + dashboard (MIT) |
| [jevroute](jevroute.md) | Reference: TypeSafe Jev skill hints for Claude Code; project stopped after baseline met stop rule (negative pilot findings published). | Rust · docs + eval data (MIT; no binary shipped) |
| [Jev Router for Windows](jev-router-windows.md) | Windows GUI setup/control panel for TypeSafe Jev routing (Codex automatic; Claude Code plugin-assisted). | Windows 10/11 · portable alpha (MIT) |
| [jev-router (hectorj2f)](hectorj2f-jev-router.md) | Score Claude Code subagent tasks with five atomic Jev questions; upgrade ungated / downgrade earned; findings included. | Python · Claude Code router (Apache-2.0) |
| [jev (taifoon-io)](taifoon-io-jev.md) | Grade an AI agent job with TypeSafe Jev: fact checks in code, four closed questions, receipt with probabilities,… | TypeScript · npm `@taifoon/jev` (MIT) |
| [Jev Atlas](jev-atlas.md) | Map a repo’s semantic decisions, reject weak Jev fits with published gates, then validate/implement survivors from `.jev-atlas/` state. | Agent skill + Claude/Codex plugin (`jev-atlas` 0.2.0) |
| [Jev Bug Hunter](jev-bug-hunter.md) | Run a bounded TypeSafe Jev first-pass bug hunt over a source file (optional spec/context). | Python/CLI · bug-hunt tool (MIT) |
| [Jev by Example](jev-by-example.md) | Ten runnable lessons on agent decisions between steps (memory, completion, handoffs, …); Jev judges, code owns policy; offline fixtures by default. | JavaScript · zero-dep CLI (`jev-by-example` 0.1.0, MIT) |
| [Jev Checkpoint](jev-checkpoint.md) | Ask TypeSafe Jev for an advisory, confidence-gated next-step route over a fixed Choice set (MCP; never executes). | TypeScript · local MCP server (`jev-checkpoint` 0.1.0) |
| [Jev Classifier for Obsidian](obsidian-jev-classifier.md) | Fill Obsidian note properties from a guide note by asking TypeSafe Jev for allowed values. | Obsidian plugin (MIT) · TypeSafe Jev |
| [Jev Code Reviewer (egma-ai)](egma-ai-jev-code-reviewer.md) | Local Jev priority + OpenAI NL review overlay for GitHub PRs. | Node · CLI/extension (MIT) |
| [Jev Decision Gateway (kartikanand73)](kartikanand73-jev-decision-gateway.md) | Governed withdrawal PoC: Jev scores, code signs policy, executor accepts signed decisions only; bench vs LLM/rules (≠ kuldeepsinh19). | Python · PoC + bench harness (MIT) |
| [JEV Flaky Detective](jev-flaky-detective.md) | Jev classifies CI test failures without masking or auto-rerun. | TypeScript · Action (MIT) |
| [Jev Flow](jev-flow.md) | Standalone studio for typed Jev workflows (Studio, Compendium, Battle Arena, labs). | Node.js · app (MIT) |
| [Jev Gatehouse (Kinde)](jev-gatehouse.md) | Kinde who/what plus Jev typed gate before each MCP tool call (allow/step-up/stop). | TypeScript · Convex starter (MIT) |
| [Jev GitHub Action](jev-action.md) | Install pinned Jev CLI in Actions; run typed judgments on event/JSON; expose answers (no issue mutation). | GitHub Action (Apache-2.0) |
| [Jev Logs](jevlogs.md) | Prioritize logs for deeper analysis alongside your archive. | TypeScript · library, CLI and OpenTelemetry integration |
| [JEV Mail Filtering](jev-mail-filtering.md) | Read-only local mail client that asks TypeSafe Jev to triage each message into actionable buckets. | Node.js · IMAP + TypeSafe Jev (MIT) |
| [Jev Model Router](jev-model-router.md) | Route Claude Code subagent models and main-conversation reasoning effort using Jev assessments; requires early-access function hooks. | TypeScript · Claude Code mod |
| [Jev Model Routing Lab](jev-model-routing.md) | Demo typed, confidence-aware Claude/Kimi routing where Jev chooses tier and code applies policy. | TypeScript · demo lab (MIT) |
| [JEV Reasoning Navigator](jev-reasoning-navigator.md) | Supervise agents: TypeSafe Jev semantic judgment ≠ PolicyEngine ≠ capability receipts ≠ sandboxed execution. | Python · middleware runtime (license unspecified) |
| [Jev Review](jev-review.md) | Add experimental quality judgments to a coding agent's review loop. | Node.js · MCP server |
| [Jev Review (Dev Agrawal)](jev-review-devagrawal.md) | Screen JavaScript/TypeScript diffs or codebases and inspect staged review findings. | TypeScript · CLI and local dashboard |
| [Jev Review Action](jev-review-action.md) | Review catalog submissions or PR diffs with TypeSafe Jev only; one template PR comment (GitHub Action). | Node.js · GitHub Action (`jev-review-action` 0.2.0) |
| [Jev review gate](jev-review-gate.md) | CI check that reads a diff, applies local rules, and asks TypeSafe Jev before later jobs run. | GitHub Action · TypeSafe Jev (MIT) |
| [Jev Runway](jev-runway.md) | Local Codex proxy: TypeSafe Jev keeps needed tool output and trims the rest between turns. | TypeScript · npm CLI (`jev-runway`, MIT) |
| [Jev Score](jev-score.md) | Score document revisions against criteria with TypeSafe Jev (OpenRouter Decisions) and keep revision history. | Node.js · CLI + local web UI (`jev-score` 1.0.0) |
| [JEV Sees](jev-sees.md) | Give TypeSafe Jev eyes: one call, many object judgments from camera/video frames | Python · vision + Jev toolkit (MIT) |
| [Jev Sift](jev-sift.md) | Screen candidate content before reading it into agent context; requires a TypeSafe key, with upstream licensing unspecified. | Node.js · MCP server and agent plugin |
| [Jev Starter](yanflizi56-jev-starter.md) | Visually configure Noul/Choice/Score questions, test against TypeSafe Jev, and export ready-to-use code or example JSON. | Vue · browser console (MIT) |
| [Jev the Janitor](jev-the-janitor.md) | Ask TypeSafe Jev to vote on markdown vault notes; code adds frontmatter or quarantines secrets (dry-run default; offline mode). | Python · CLI (`jev-janitor` 0.1.1) |
| [Jev Trader](jev-trader.md) | Study Jev market-direction choices, simulated fills, and on-chain order execution through a Bun trading experiment. | TypeScript / Bun · trading reference and dashboard |
| [Jev WCAG Auditor](jev-wcag-auditor.md) | Audit public URLs with axe-core plus optional TypeSafe Jev judgement-call adjudication and uncertainty band. | Next.js · web app (`jev-wcag-auditor` 0.1.0, MIT) |
| [jev-agent-browser](jev-agent-browser.md) | Confidence-gated next browser action for `agent-browser` via TypeSafe Jev (or Gateway/Cloudflare/custom). | TypeScript · npm (`@mhingston5/jev-agent-browser` 0.3.1) |
| [jev-agent-failure-benchmark](jev-agent-failure-benchmark.md) | Score TypeSafe Jev on Who&When Pro text traces for responsible agent, step, and error type; compare to paper LLMs. | Python · CLI (`jevbench`, Apache-2.0) |
| [jev-agent-kit](jev-agent-kit.md) | Zero-dependency CLI + MCP tools (check/choose/score/judge/route/triage/guard/grep/rank/compact) on TypeSafe Jev — distinct from the Rust jevkit CLI. | Node.js ≥ 18 · npm (`@walidboulanouar/jevkit` 0.2.0) |
| [jev-agent-kit (nanoDBA)](nanodba-jev-agent-kit.md) | Evidence-layer hooks for Claude Code/Codex/Hermes: TypeSafe Jev scores risky tool calls (shadow by default; ≠ walidboulanouar/jev-agent-kit). | Python · agent hooks kit (MIT) |
| [jev-agent-skill (RosarioDiBartolo)](rosariodibartolo-jev-agent-skill.md) | Connect Jev/Kev System One models to Codex and AI agents for tool routing, classification, and bounded decisions. | Python · agent skill (MIT) |
| [Jev-AI-Skill](jev-ai-skill.md) | Claude Code/Codex/Hermes skill + MCP: TypeSafe Jev gates for agent decisions | Python · agent skill + MCP (MIT) |
| [jev-ai-use-cases (atliq)](atliq-jev-ai-use-cases.md) | LangChain notebook: TypeSafe Jev triage/routing/guards/tool-select/finance checks. | Jupyter · langchain-typesafe (MIT) |
| [jev-align](jev-align.md) | Build calibrated classifiers/AI Functions from human feedback with TypeSafe Jev + GEPA (`jeva`). | Python · CLI (`jev-align` / `jeva`) |
| [jev-auto-approve](basmaabouzied0-jev-auto-approve.md) | Claude Code hook: TypeSafe Jev auto-approves read-only shell commands in milliseconds; everything else still prompts… | Python · Claude Code hook (MIT) |
| [jev-backend-qa](jev-backend-qa.md) | Audit backend surfaces then PAL/Jev risk adjudication to BLOCK/WARN/PASS (CLI + Action). | Python · CLI/Action + Node bridge (MIT) |
| [jev-blindspot](jev-blindspot.md) | Claude Code / Codex side panel: Jev gate then optional blind-spot analysis without editing the session. | TypeScript · npm CLI/hooks (MIT) |
| [jev-calibrate](jev-calibrate.md) | Calibrate Jev questions against labelled examples; per-question gate/ranker/unusable verdicts. | TypeScript · npm CLI (`jev-calibrate` 0.1.11) |
| [jev-certify](jev-certify.md) | Turn Jev probabilities into conformal routing certificates and PPI audits (offline math + OpenRouter Decisions client). | Python · CLI/library (`jev-certify` 0.1.0) |
| [jev-ci-pathfinder](jev-ci-pathfinder.md) | Select allowlisted CI jobs after a change with TypeSafe Jev; deterministic allowlist + dependency closure. | TypeScript · GitHub Action (MIT) |
| [jev-ci-selector](jev-ci-selector.md) | Select which described CI jobs apply to a PR diff with TypeSafe Jev (shadow or enforce). | Node.js · GitHub Action (`jev-ci-selector` 0.1.0) |
| [jev-ci-triage](criguex-jev-ci-triage.md) | Label each failing test with a triage class using deterministic rules plus Jev for leftovers; emit a report without changing build status. | TypeScript · CI report tool (Playwright/JUnit) |
| [jev-claude-code (Axiumine)](axiumine-jev-claude-code.md) | Research catalog + reference MCP: TypeSafe Jev yes/no triage for Claude Code via OpenRouter (≠ DarioFontanel/weiping). | HTML/Node · research + MCP (GPL-3.0) |
| [jev-claude-code (DarioFontanel)](dariofontanel-jev-claude-code.md) | Paste-in Claude Code prompts for TypeSafe Jev model routing, context compaction, and 14-question diff review. | Markdown prompts (MIT) |
| [jev-claude-code (weiping)](weiping-jev-claude-code.md) | Claude Code plugin: Jev permission gate, output ladder, context load, and subagent router (shadow default; distinct from DarioFontanel). | Python · Claude Code plugin marketplace (MIT) |
| [jev-claude-router (Flam1ngFir3ball)](jev-claude-router.md) | Claude Code plugin: Jev picks tier/effort with cost-aware switches and optional Jev compaction. | TypeScript · Claude Code plugin (MIT) |
| [jev-claw](jev-claw.md) | OpenClaw `jev_route` tool: TypeSafe Jev classifies task type/complexity/risk; code applies routing policy. | OpenClaw plugin (MIT) |
| [jev-cloud-cost-guardian](jev-cloud-cost-guardian.md) | FinOps CI gate: Jev scores proposed cloud spend vs budget; policy never hides cost lines. | TypeScript · GitHub Action (MIT) |
| [jev-cmdline-classifier](jev-cmdline-classifier.md) | Classify shell commands with TypeSafe Jev Choice (`allow`/`prompt`/`forbidden`) plus fail-closed local rules for agent skills. | Python/JS skill + CLI (`jev-command-classifier` 0.1.0) |
| [jev-codex-router](jev-codex-router.md) | Route each Codex turn's model and thinking depth with Jev via a Codex Router generic provider. | Python · local server and Codex Router integration |
| [jev-codex-token-saver](jev-codex-token-saver.md) | Gather local workspace/log evidence and let TypeSafe Jev select exact excerpts for Codex (MCP plugin; local fallback). | Node.js · Codex plugin + MCP (`jev-codex-token-saver` 0.3.2) |
| [jev-community-ops](firasb9-jev-community-ops.md) | Triage developer-community messages with TypeSafe Jev typed questions, confidence gates, and a weekly digest. | Python · ops toolkit (MIT) |
| [jev-compact](jev-compact.md) | Score Codex tool calls with TypeSafe Jev before compaction and re-inject critical outputs the summary dropped. | TypeScript · Codex plugin (`jev-compact` 0.1.0) |
| [jev-compaction (Waxmell114514)](waxmell114514-jev-compaction.md) | Score-only context compaction so memory cannot hold facts absent from the transcript (offline demo). | Python · library/demo (MIT) |
| [jev-controller](ac-kurniawan-jev-controller.md) | After each tool result, ask Jev which next step to append as a one-line directive; fail-open if the key/timeout fails. | TypeScript · OMP (`oh-my-pi`) post-tool hook |
| [jev-debtgate](jev-debtgate.md) | Gate agents/CI on technical-debt risk with TypeSafe Jev over local git/file metrics. | Node.js · CLI/MCP/Action (`jev-debtgate` 0.3.0) |
| [jev-decisions (wonghanz)](wonghanz-jev-decisions.md) | Model backend decisions (log triage, incidents, PR triage, deploy risk) with typed Jev questions plus a control-group eval harness. | JavaScript · decision library + harness (MIT) |
| [jev-effort](jev-effort.md) | Claude Code: TypeSafe Jev picks per-step reasoning effort + lease (OpenRouter/TypeSafe/Vercel). | Node.js · hooks/setup (MIT) |
| [jev-effort-router](jev-effort-router.md) | Hermes on Ollama:Cloud: TypeSafe Jev picks model **and** reasoning effort per turn and rewrites `llm_request`. | Python · Hermes plugin (`hermes-plugin-jev-effort-router` 0.2.1, MIT) |
| [jev-enforce](jev-enforce.md) | Claude Code plugin: TypeSafe Jev checks replies and edits against CLAUDE.md/AGENTS.md and blocks broken rules in the same turn. | TypeScript · Claude Code plugin / npm (`jev-enforce`) |
| [jev-evolve](jev-evolve.md) | Evolve agent policies with typed Jev decisions and measure how much improvement is selection luck. | Python · library (`jev-evolve` on PyPI) |
| [jev-eyes](jev-eyes.md) | Turn images into inspectable OCR/layout `state` for TypeSafe Jev locally (`see`/`ask`, CLI, optional MCP). | Python · library/CLI/MCP (`jev-eyes` 0.1.0) |
| [jev-filter (ByteBell)](bytebell-jev-filter.md) | Claude Code plugin: TypeSafe Jev keeps relevant files after grep so the coding LLM reads a shortlist. | Python · Claude Code plugin / MCP (MIT) |
| [jev-for-all](jev-for-all.md) | Shared System One decision contract: Jev picks skill/tool subset/browser moves for OpenCode/Claude Code/Hermes. | TypeScript · OpenCode plugin + adapters (MIT) |
| [jev-fuse](jev-fuse.md) | Governed System One proxy: policy actions, AST guards, singleflight, and WAL audit for TypeSafe Jev/local Laya. | Python · proxy/PyPI (`jev-fuse`, Apache-2.0) |
| [jev-gate (MongLong0214)](monglong0214-jev-gate.md) | Claude Code plugin: Jev-backed Gate/Router/Evidence plus non-Jev Compact/Output (≠ Neoo-Blue jev-gate). | TypeScript · Claude Code plugin (no LICENSE file) |
| [jev-gate (Neoo-Blue)](neoo-blue-jev-gate.md) | Gate Claude Code plans and stop summaries with TypeSafe Jev clause checks; block edits until the plan passes. | Python · Claude Code plugin (MIT) |
| [jev-gates](jev-gates.md) | Compose three-valued TRUE/FALSE/UNKNOWN circuits from TypeSafe Jev judgments plus exact rules (auditable traces). | TypeScript · library/CLI (`jev-gates` 0.1.0) |
| [jev-gateway](jev-gateway.md) | Let Jev choose each tool call for Codex, Claude Code, OpenCode, or Gemini through a local LLM gateway. | TypeScript · npm launchers and dashboard |
| [jev-git-graph](jev-git-graph.md) | Evidence-backed TypeSafe Jev relationship graph for Git branch/worktree/PR consolidation (read-only default). | Python · CLI (Apache-2.0) |
| [jev-guard](jev-guard.md) | Risk-score coding-agent tool calls with TypeSafe Jev (deny/ask/allow), flag injection in results, and scan skills across many agents. | Node.js · npm CLI/hooks (`jev-guard` 0.3.1) |
| [jev-guard (CMaintz)](cmaintz-jev-guard.md) | Framework-agnostic allow/block/hold tool-call guard with TypeSafe Jev + LangChain/Vercel adapters (distinct from leepokai jev-guard). | TypeScript · library (`jev-guard` 0.1.0, MIT) |
| [jev-guard (klauswg)](klauswg-jev-guard.md) | Exchange deposit/withdrawal risk triage: TypeSafe Jev answers; Java hard rules and gates decide (distinct from coding-agent jev-guard). | Java · Spring Boot demo (MIT) |
| [jev-guard (muratcakmak)](muratcakmak-jev-guard.md) | Claude Code hooks: regex + TypeSafe Jev rules deny bad edits/deploys; fail-open if scorer down (distinct from leepokai/CMaintz). | TypeScript · Claude Code plugin (MIT) |
| [jev-guard (rudra72r)](rudra72r-jev-guard.md) | Guard LLM app inputs/outputs with TypeSafe Jev or offline/local backends and severity-weighted policies. | Python · PyPI (`jev-guard`, MIT) |
| [jev-guard (yelkhanyergali-sys)](yelkhanyergali-sys-jev-guard.md) | Prune in-flight terminal noise and guard risky diffs in PI Mono with Jev judgments while preserving prompt-cache prefixes. | JavaScript · PI Mono extension (Node ≥ 18) |
| [jev-guardbench](dfranco-projects-jev-guardbench.md) | Benchmark whether System One (Jev/Kev) can replace LLM-as-judge in agent guardrail callbacks. | Python · uv package (license unspecified) |
| [jev-guardrails (deepansh-saxena)](deepansh-saxena-jev-guardrails.md) | Compare LLM-as-judge vs TypeSafe Jev on identical 25 guardrail rules for a mock support agent (cost/latency/calibration). | Python · LangChain/LangGraph eval (license unspecified) |
| [jev-harness](jev-harness.md) | Map TypeSafe Jev answers to actions with confidence gates, shadow mode, recipes, and an eval CLI. | TypeScript · npm library/CLI (`jev-harness` 0.1.0) |
| [jev-harness (TypeSafeAI)](typesafeai-jev-harness.md) | Research proposal-review contract: LLM proposes, Jev answers four narrow questions, code emits host evidence (distinct from AntonioCoppe/jev-harness). | TypeScript · source-only (`jev-harness` 0.0.0, MIT) |
| [jev-healthcare-lab](jev-healthcare-lab.md) | Open Jev vs DeepSeek comparison on 96 healthcare tasks / 12 scenarios (quality/latency/cost). | Python · research lab (MIT) |
| [jev-hooks](jev-hooks.md) | Review Claude Code commits with typed System One questions (self-hosted rizzo-flow or TypeSafe Jev) via PreToolUse hooks. | TypeScript · Claude Code plugins (MIT, 0.1.0-dev preview) |
| [jev-humanizer](snjrusmn-jev-humanizer.md) | Anti-slop skill: TypeSafe Jev flags AI-sounding paragraphs so the writing model rewrites only those spans… | Python · agent skill (MIT) |
| [jev-in-codex](jev-in-codex.md) | Rank Codex capabilities, search hits, and output excerpts with TypeSafe Jev via local MCP. | TypeScript · MCP server + Codex plugin (0.1.0) |
| [jev-issue-radar](jev-issue-radar.md) | Find duplicate/related GitHub issues with TypeSafe Jev evidence choices in a local read-only dashboard. | Node.js · loopback server + static UI (0.1.1) |
| [jev-judge-mcp (PyModel)](pymodel-jev-judge-mcp.md) | MCP typed judgment tools (verify/screen/find/classify/rerank/decide/…); policy owns auto/review/escalate. | Python · MCP (`jev-mcp-python`, MIT) |
| [jev-layer](jev-layer.md) | Route harness capability choices with receipts/replay; host keeps execution (demo/OpenRouter/TypeSafe). | TypeScript · CLI, MCP and harness installers (`jev-layer` 0.1.0) |
| [jev-lint](jev-lint.md) | Ast-grep selects subjects; TypeSafe Jev Noul scores one-sentence semantic rules (distinct from huntedman/JevLint). | TypeScript · npm CLI (`jev-lint` 0.4.1) |
| [jev-lint (ckorhonen)](ckorhonen-jev-lint.md) | Fuzzy agent linter: hook checks agent edits against team rule packs in ~0.3s (jevlint.dev; distinct from mizchi/huntedman linters). | TypeScript/Bun · agent hooks + rule packs (MIT) |
| [jev-linter-action](jev-linter-action.md) | Gate CI on yes/no TypeSafe Jev review questions over selected repo files (thresholds in `.jev-lint.json`). | Node.js · GitHub Action (`jev-linter-action` 1.0.0) |
| [jev-loop (King4s)](king4s-jev-loop.md) | Build loop where TypeSafe Jev decides and Claude Code/Hermes executes (MCP + skill; ≠ lvzhaobo/jev-loop). | Python · MCP/skill (MIT) |
| [jev-mcp (pyck-ai)](pyck-ai-jev-mcp.md) | Expose batched Jev Noul/Choice/Score framings as MCP tools for OpenCode and other MCP clients, reusing OpenRouter login when present. | Go · MCP server for OpenCode/MCP clients |
| [Jev-Mem](jev-mem.md) | Control agentic memory admission/linking/retrieval with TypeSafe Jev over a multi-view graph. | Python · library/CLI (`jev-mem` 0.1.0) |
| [jev-oas-sentinel](jev-oas-sentinel.md) | Compare OpenAPI specs with structural diffs plus TypeSafe Jev semantic contract questions. | Python · CLI (`jev-oas-sentinel`) |
| [jev-ood-calibration](jev-ood-calibration.md) | Independent calibration study of TypeSafe Jev with published raw dumps: public benches plus 900 OOD synthetic support tickets. | Node/Python · research scripts + committed results |
| [jev-opus](jev-opus.md) | Re-pick Claude Opus 5.5 effort each step with TypeSafe Jev without breaking the prompt cache. | Node.js · CLI + Claude Code plugin (`jev-opus` 0.3.0, MIT) |
| [jev-packs](jev-packs.md) | Evidence-gated registry of Jev question packs with golden cases and an offline multi-backend scoreboard. | Pack data + Python scripts (CC0-1.0) |
| [jev-permission-gate (madisonrickert)](madisonrickert-jev-permission-gate.md) | Claude Code auto-mode tool-call gate: TypeSafe Jev allow/deny/defer ahead of the built-in classifier. | Claude Code mod/plugin (MIT) |
| [jev-pi (weiping)](weiping-jev-pi.md) | pi extension: Jev permission gate, output ladder, conditional context, agent router, and jev_ask tool (shadow default). | TypeScript · pi package (`jev-pi`, MIT) |
| [jev-pi-token-reduction](jev-pi-token-reduction.md) | Trim Pi tool outputs with TypeSafe Jev visibility levels before the model sees them; expand on demand. | Python · Pi extension (MIT) |
| [jev-pii-checker](jev-pii-checker.md) | Scan text/files for PII with TypeSafe Jev presence/sensitivity judgments plus regex and segmentation layers. | TypeScript/Bun · CLI (`@coo-quack/jev-pii-checker` 0.3.1) |
| [jev-pilot (Akramovic1)](akramovic1-jev-pilot.md) | Claude Code plugin: TypeSafe Jev routes effort, subagent model, strategy advice, and one skill per prompt. | TypeScript · Claude Code plugin (`jev-pilot` 0.4.4, MIT) |
| [jev-pilot (wangzhezbz)](wangzhezbz-jev-pilot.md) | Codex plugin: TypeSafe Jev for effort routing, context filtering, and workflow help (macOS/Windows/Linux; distinct from Akramovic1/jev-pilot). | JavaScript · Codex plugin + platform launchers (MIT) |
| [jev-playground](frederico-kluser-jev-playground.md) | Try TypeSafe Jev via OpenRouter with typed questions, calibration view, cost metrics, and exportable requests. | TypeScript · Vercel playground (MIT) |
| [jev-playwright (arthurfiorette)](arthurfiorette-jev-playwright.md) | Jev-powered Playwright test selection from changed files. | TypeScript · Playwright (MIT) |
| [jev-pr-judge](jev-pr-judge.md) | Typed PR verdicts with one parallel TypeSafe Jev call, TypeScript policy, Next.js UI, and GitHub Action sticky comments. | TypeScript · Next.js app and Action |
| [jev-pr-profiler](jev-pr-profiler.md) | GitHub Action: TypeSafe Jev PR risk profile + review-depth outputs (never merges alone). | TypeScript · GitHub Action (MIT) |
| [jev-pr-quality](jev-pr-quality.md) | Add TypeSafe Jev-assisted PR review comments/checks and a RawTree multi-repo quality dashboard. | GitHub Action + dashboard (Apache-2.0) |
| [jev-pref](jev-pref.md) | Turn AGENTS.md preferences into a TypeSafe Jev semantic linter for coding-agent diffs (setup/review/tune + Action). | TypeScript · npm (`jev-pref` 0.4.1) |
| [jev-preflight](jev-preflight.md) | Score eight risk axes on a Claude Code turn diff with one TypeSafe Jev request; optional assist reinspection. | Go · Claude Code plugin (v0.1.0) |
| [jev-project-context](jev-project-context.md) | Keep evidence-first experiment memory for coding agents; optional TypeSafe Jev triage on doctor/context loads. | Agent skill + stdlib Python scripts |
| [jev-proxy](jev-proxy.md) | Sit in front of TypeSafe /v1/systemone to record, cache, and replay Jev calls locally. | Rust · SQLite + HTMX UI (MIT) |
| [jev-pruner](jev-pruner.md) | Prune eligible Bash stdout with Jev before Claude Code or an opt-in Codex wrapper returns it to the model. | TypeScript · library, Claude Code plugin and Codex wrapper |
| [jev-realtime-observability](jev-realtime-observability.md) | Real-time agent observability with a Jev-protocol judge (open default model path) | TypeScript · observability + judge (Apache-2.0) |
| [jev-reflex (xnuonux)](jev-reflex-xnuonux.md) | Portable Jev decision sidecar: MCP/CLI/pi recipes with durable budgets and source-bound context plans. | Python · MCP/CLI (`jev-reflex`, MIT) |
| [jev-req-gate](jev-req-gate.md) | Gate AI-written requirements with TypeSafe Jev (PASS/REVIEW/BLOCK); CLI, skill, CI Action, offline demo. | Python · CLI/API/skill + GH Action (MIT) |
| [jev-research-pipeline](jev-research-pipeline.md) | Schedule daily research harvests where TypeSafe Jev screens sources per standing question and an LLM writes vault notes. | Python · pipeline + Obsidian notes (MIT) |
| [jev-risk-check-provider](caiovicentino-jev-risk-check-provider.md) | x402 risk-check provider: TypeSafe Jev typed decisions plus ES256-signed attestations facilitators can verify for… | TypeScript · x402 provider (MIT) |
| [jev-router](jev-router.md) | Route Claude Code and Codex turns through Jev model selection and inspect stored routing exchanges. | JavaScript · CLI launchers and HTTP proxies |
| [jev-router (Ex8-ca)](ex8-ca-jev-router.md) | Hermes Jev skill router + session-start pre-route. | Python · plugin (MIT) |
| [jev-router (FrancoisChastel)](francoischastel-jev-router.md) | Relay that picks fast/mid/frontier model+effort per turn via tool signals and TypeSafe Jev; fails open; honest cost logs. | TypeScript · npm (`@french-castle/jev-router`, MIT) |
| [jev-router (jjjjjjjjjjjjjjjjacob)](jjjjjjjjjjjjjjjjacob-jev-router.md) | Let TypeSafe Jev pick Claude Code effort and subagent models on demand via /jev. | TypeScript · Claude Code plugin (MIT) |
| [jev-rules](jev-rules.md) | Select project rules and codebase-map documents for Claude Code prompts and file changes. | JavaScript · Claude Code plugin |
| [jev-safety-gateway](jev-safety-gateway.md) | Nginx-front reverse proxy: TypeSafe Jev judges each user input before LLM backends (AGPL-3.0) | Go · reverse-proxy gateway (AGPL-3.0) |
| [jev-sap-commerce](emenowicz-jev-sap-commerce.md) | SAP Commerce extension: TypeSafe Jev review moderation + category suggestions (dry runs, audits). | Java · Commerce extension (Apache-2.0) |
| [jev-seatbelts](jev-seatbelts.md) | Seven Claude Code hooks catching expensive agent mistakes; TypeSafe Jev on judgment tiers. | Python · Claude hooks (MIT) |
| [jev-sec-audit](dhanushnehru-jev-sec-audit.md) | Lightning-fast AI supply-chain security auditor: TypeSafe Jev scores typosquatting and malicious package scripts in… | JavaScript · CLI / GitHub Action (Apache-2.0) |
| [jev-sec-bench](jev-sec-bench.md) | Run or browse blind TypeSafe Jev prompt-injection and vulnerable-code benchmarks (jev-go + results TUI). | Go · CLI/TUI |
| [jev-security-prioritization](jev-security-prioritization.md) | Jev vs severity baselines for SCA/SAST triage. | Python · research (MIT) |
| [jev-security-sentinel](jev-security-sentinel.md) | Security CI gate over SAST/SCA/IaC/secrets/container findings via TypeSafe Jev; findings stay visible. | TypeScript · GitHub Action (MIT) |
| [jev-seo-skills](jackson7705-jev-seo-skills.md) | Run five tested SEO workflows where TypeSafe Jev judges intent, internal links, cannibalization, briefs, and AI mentions. | Python · skills pack (MIT) |
| [jev-shadow-adapter](ianlintner-jev-shadow-adapter.md) | Observe TypeSafe Jev routing decisions in shadow mode without enforcing them, with docs site. | Python · shadow adapter + MkDocs (MIT) |
| [jev-shell-history](jev-shell-history.md) | Recall zsh history commands with optional acceptance of Jev-ranked inline suggestions; selected history is sent to TypeSafe. | TypeScript / zsh · shell plugin and CLI |
| [jev-shield](jev-shield.md) | Semantic MCP firewall: screen tool calls/results/descriptions with TypeSafe Jev via Vercel AI Gateway. | Node.js · CLI, MCP wrap, opt-in hooks (`jev-shield` 0.1.0) |
| [jev-skill (marcodicesare-dev)](marcodicesare-dev-jev-skill.md) | Community Jev skill for Claude Code/Codex: guide, Python CLI, five tested recipes, and measured findings from ~19k… | Python · skill + CLI (MIT) |
| [jev-skill-gate](jev-skill-gate.md) | Score Claude Code skills with TypeSafe Jev and write `skillOverrides` so only relevant skills reach context. | Node.js · CLI (`jev-skill-gate` 0.2.0) |
| [jev-skill-router-bench](jev-skill-router-bench.md) | Independent reproducible scorecard of a Jev skill router on an 84-skill Hermes roster (81 labelled turns). | Python · bench artifacts + scripts |
| [jev-skill-scout](jev-skill-scout.md) | Audit Claude Code skill misses with TypeSafe Jev; optional live mod suggests a skill without changing the roster. | Node.js ≥ 20 · npm CLI/mod (`jev-skill-scout` 0.1.0) |
| [jev-skills](jev-skills.md) | Claude Code/Codex plugin: TypeSafe Jev picks which skills enter context each turn (0 always-on skill-list tokens). | TypeScript · Claude Code/Codex plugin (MIT) |
| [jev-subtitle-translator](jev-subtitle-translator.md) | Translate SRT with structured LLM batches and TypeSafe Jev QC on every source–translation pair. | Python · web UI/CLI (GPL-3.0) |
| [jev-suite](jev-suite.md) | Four Java decision-quality apps on one Jev kernel: structured questions; code keeps thresholds/vetoes. | Java · Maven suite (`jev-suite` 0.1.0, MIT) |
| [jev-supervisor](jev-supervisor.md) | DeepSeek Harness macOS Jev execution-supervisor plugin (own TypeSafe key + budgets). | DeepSeek Harness plugin (MIT) |
| [jev-support-agents](jev-support-agents.md) | FastAPI support orchestrator: LLM specialists write text; TypeSafe Jev routes and evaluates with retry/escalation. | Python · FastAPI + Ollama reference (MIT) |
| [jev-support-desk](jev-support-desk.md) | Developer-support queue tooling on TypeSafe Jev: confidence-gated triage and request doctor. | TypeScript · support desk (MIT) |
| [jev-swap](jev-swap.md) | Find LLM→Jev decision swaps; shadow-test on traffic. | Node · CLI (MIT) |
| [jev-switchboard](jev-switchboard.md) | Gate cross-agent messages with TypeSafe Jev: interrupt vs drop plus selected evidence injection. | Node.js ≥ 20 · CLI/hooks (`jev-switchboard` 0.1.0) |
| [jev-table](jev-table.md) | Add TypeSafe Jev AI columns to CSV/JSONL with confidence, review queue, resume, and dry-run cost preview. | Python · CLI (`jev-table` 0.1.1, Apache-2.0) |
| [jev-test-filter](jev-test-filter.md) | Score repository tests against a git diff with TypeSafe Jev and emit runner-native filter arguments. | TypeScript · npm CLI (`jev-test-filter` 0.1.0; Node ≥ 24) |
| [jev-test-impact](jev-test-impact.md) | Select Vitest/Jest tests impacted by a Git diff using static deps plus optional TypeSafe Jev scoring. | TypeScript · npm CLI + GitHub Action (MIT) |
| [jev-test-triage](jev-test-triage.md) | Rank mutation-testing survivors with TypeSafe Jev; emit summary/SARIF/agent prompts for Claude Code or Codex. | Python · CLI (`jtt`) + pre-commit/GitHub Action (MIT) |
| [jev-ticket-triage](beese54-jev-ticket-triage.md) | Reproduce TypeSafe Jev vs LLM support-ticket triage on banking77 and customer-support datasets (WIP). | Python · eval harness (MIT) |
| [jev-toolkit](jev-toolkit.md) | Serve TypeSafe Jev asks/verify/review over MCP plus CLI triage, audit, skill routing, and local impact metrics. | TypeScript · CLI/MCP (`jev`, Effect; Node ≥ 26) |
| [jev-tools (CMaintz)](cmaintz-jev-tools.md) | TypeScript TypeSafe Jev tools including an agent tool-call guardrail | TypeScript · library/tools (MIT) |
| [jev-tools (Rcidshacker)](rcidshacker-jev-tools.md) | Claude Code plugin: OpenJev/Codiv cheap typed agent judgments (≠ CMaintz/jev-tools). | Claude Code plugin (MIT) |
| [jev-tree](jev-tree.md) | Recursive TypeSafe Jev Choice over a JSON taxonomy when a flat list exceeds the 255-option cap. | TypeScript · npm (`jev-tree` 0.1.0) |
| [jev-triage](jev-triage.md) | GitHub Action: label issues with TypeSafe/Cloudflare Jev typed answers; low confidence escalates to needs-human. | TypeScript · Action (`cmaintz/jev-triage@v0`, MIT) |
| [jev-triage (ZephyrDeng)](zephyrdeng-jev-triage.md) | Triage GitHub/GitLab backlogs with TypeSafe Jev into an HTML report (duplicates, types, dependency order). | TypeScript · gh/glab CLI (MIT) |
| [jev-use (shitianfang)](jev-use.md) | Route the no-text steps of a Claude Code, Codex or pi loop to Jev, with an opt-in PreToolUse gate and typed handbacks to the LLM. | TypeScript · MCP server, CLI and agent plugin |
| [jev-verify (stillmarcus24)](stillmarcus-jev-verify.md) | Audit published Jev answers against the Yurin confidence identity; flag fixture violations. | JavaScript · CLI (MIT) |
| [jev-web-skills](jackson7705-jev-web-skills.md) | Run five tested website-building workflows where TypeSafe Jev judges page maps, migration, silo/doorway QA, and routing. | Python · skills pack (MIT) |
| [Jev_validation_agent](jev-validation-agent.md) | Python Jev Guard validating agent outputs via TypeSafe Jev with reports and a local demo UI. | Python · package + demo (MIT) |
| [jeval](jeval.md) | Measure classifier confidence calibration and set cost-optimal human hand-off thresholds (Jev-motivated, provider-neutral). | Python · CLI (`jeval` 0.1.0, Apache-2.0) |
| [jevals](jevals.md) | Author and run TypeSafe Jev Noul/Choice/Score evaluations locally; compare saved results in a browser workbench. | TypeScript · local server/UI (`jevals` 0.1.1) |
| [JEVals (duberblock)](duberblock-jevals.md) | Evaluate SystemOneRequest payloads vs JEV baseline and OpenAI-compatible judges; inspect fidelity/divergence in a web UI. | TypeScript · apps/packages playground (MIT) |
| [Jevals.com](jevals-com.md) | Hosted independent Jev vs LLM boards (accuracy/calibration/cost/latency); open data, private harness (distinct from local jevals). | Hosted boards + [jevals-data](https://github.com/Jevals/jevals-data) (CC BY 4.0) |
| [Jevaluate](jevaluate.md) | Confidence-gated web walkthroughs with TypeSafe Jev; optional DeepSeek vision; eval/judge scripts and skill. | Node/Python · Playwright scripts (MIT) |
| [JevAny](jevany.md) | Open infrastructure for training, evaluating, and deploying System 1 decision models (independent of hosted TypeSafe Jev). | Python · System 1 infra (Apache-2.0) |
| [jevbus](jevbus.md) | Route/subscribe/deliver streaming events with TypeSafe Jev (or any Judge) and policy thresholds. | Rust · crate (`jevbus` 0.1.0) |
| [jevc](jevc.md) | Compile agent rules/JSON Schema into TypeSafe Jev programs (typed questions + code reducers) with offline fixture checks. | TypeScript · npm CLI (`jevc` 0.1.0, Apache-2.0) |
| [jevcache](jevcache.md) | Reuse chat completions when TypeSafe Jev (via OpenRouter) admits paraphrased prompts as same-intent. | TypeScript · OpenAI-compatible proxy CLI (`@kushalicious/jevcache` 0.1.5) |
| [jevci (sumant1122)](sumant1122-jevci.md) | Sub-second CI/diff/commit/doc quality gate powered by TypeSafe Jev System One (score+noul). | CLI · CI gate (MIT) |
| [jevcompat](jevcompat.md) | Spec + conformance suite for Jev-compatible `/v1/systemone` servers (proxy, mock, Action). | Python · suite + GitHub Action (MIT) |
| [JevCore Agent](carter1111-jevcore.md) | Coding harness: TypeSafe Jev classifies task/risk/mode; hard-policy Guard; MCP + `npx jevcoreagent`. | JavaScript · npm CLI/MCP (Apache-2.0) |
| [jevcut](jevcut.md) | Turn long talk videos into ranked short clips: code lists cut edges; TypeSafe Jev judges standalone worth. | Python · CLI (`jevcut`, MIT) |
| [jevdev](jevdev.md) | Rust coding-agent harness centered on TypeSafe Jev System One (HTTP or local transport). | Rust · crate/CLI (Apache-2.0) |
| [JevDo](jevdo.md) | Jev-first DeepSeek Harness loop: reuse validated Actions before calling a frontier model. | TypeScript · DSH agent loop (MIT) |
| [jeveloper](jeveloper.md) | Claude Code System-1 reflex layer: TypeSafe Jev route/gate/verify/done plus optional driver mode. | Claude Code plugin (`jeveloper` 0.2.0, MIT) |
| [JeVerifier](jeverifier.md) | Jev reading lists + doc/code checks under Claude sessions. | Python · harness (MIT) |
| [jevernetes](jevernetes.md) | Tail and triage Kubernetes logs with optional TypeSafe Jev analysis, local review rules, and coding-agent prompts. | Python · CLI/dashboard (`jevernetes`, Apache-2.0) |
| [jevex-cli](jevex-cli.md) | Jev-powered per-turn Codex model router with a terminal UI. | TypeScript · CLI (MIT) |
| [jevface](jevface.md) | Typed judgments for Java: declare questions as an interface and let Jev answer them. | Java · interface client (Apache-2.0) |
| [JevFlow](parth1811-jevflow.md) | Claude Code plugin that keeps agents honest: plans as phases with checks; when Claude tries to stop, JevFlow asks… | Python · Claude Code plugin (MIT) |
| [jevgate (craxrev)](craxrev-jevgate.md) | Claude Code Bash/Write gate from Jev risk facts with allow/ask/deny rules. | TypeScript · Claude Code plugin (MIT) |
| [JevGate (RichieLoco)](richieloco-jevgate.md) | Pure-MQL5 MetaTrader 5 module that vetoes EA trades using TypeSafe Jev calibrated judgments (≠ Claude Code jevgate). | MQL5 · MT5 include (MIT) |
| [JevGuard](jevguard.md) | Enforce CLAUDE.md/AGENTS.md-derived rules on Claude Code/Codex via TypeSafe Jev PreToolUse/Stop hooks (distinct from jev-guard risk firewall). | TypeScript · Claude/Codex plugin (`jevguard` 0.1.0) |
| [JevGuard (blacksinisterx)](blacksinisterx-jev-guard.md) | Hard-rule prefilter then Jev allow/review/block between agent and tools (mock-first). | TypeScript/Python · FastAPI + Vite demo (no LICENSE) |
| [jevkit](jevkit.md) | Ask TypeSafe Jev from a Rust CLI and lint question sets offline before spending on inference. | Rust · CLI (`jevkit` 0.3.0, rustc ≥ 1.88) |
| [jevlang (RoyWiggins)](roywiggins-jevlang.md) | Rewrite Python if/while/match so TypeSafe Jev decides each condition (English or Python); distinct from TimMikeladze/JevLang. | Python · codec preprocessor (license file not found) |
| [JevLang (TimMikeladze)](timmikeladze-jevlang.md) | Declare routes/gates/actions once; Jev answers only needed questions; signed journal replay. | TypeScript/Python · library `jevlang` (MIT) |
| [JevLangGraph (blacksinisterx)](blacksinisterx-jev-langgraph.md) | LangGraph loop where Jev—not an LLM—chooses the next branch action (mock-first). | TypeScript/Python · FastAPI + Vite demo (no LICENSE) |
| [jevlens](jevlens.md) | Run labeled Choice/Noul/Score evals, store full distributions, calibrate thresholds, and optionally dashboard or CI-gate. | Python · CLI (`jevlens` 0.1.0) + optional Streamlit/Action |
| [JevLint](jevlint.md) | Lint source against plain-English conventions with file-level TypeSafe Jev Noul judgments (magic-strings, descriptive-names). | TypeScript · npm CLI (`@jevlint/cli`) |
| [jevlint (Ice-Hazymoon)](ice-hazymoon-jevlint.md) | Write plain-English semantic lint rules; TypeSafe Jev returns calibrated yes/no probabilities (distinct from huntedman/JevLint). | TypeScript · npm (`@hazymoon/jevlint`, MIT) |
| [jevmate](jevmate.md) | Coding-agent triage/test-selection/risk review via TypeSafe Jev (CLI, Claude Code plugin, MCP). | Python · CLI + plugin + MCP (MIT) |
| [jevmem](jevmem.md) | Git-tracked JEVMEM.md memory for Claude Code/Cursor/Codex; TypeSafe Jev decides what to save and recall, and checks tool calls against saved rules. | Node.js · Claude Code plugin + CLI/hooks + MCP (`jevmem` 0.6.4, MIT) |
| [jevmetrics](jevmetrics.md) | Assess unfamiliar OTel metrics for retention with TypeSafe Jev, then apply deterministic keep/reduce policy. | Go · OpenTelemetry Collector processor (0.1.0-dev alpha) |
| [jevmod](jevmod.md) | Moderation CLI/SDK/API/MCP and optional chat bots with per-category TypeSafe Jev probabilities and owned thresholds. | Python · `jevmod` 0.2.1 (MIT) |
| [jevmory](jevmory.md) | Build quote-backed agent memory with TypeSafe Jev grading and audit MEMORY.md with receipts. | Python · CLI (`jevmory`) + Claude/Codex hooks |
| [jevq](who-jevq.md) | Read JSONL on stdin, ask Jev a yes/no claim about each value, pass through those above threshold (optional `--score` / `--pass`). | Python · CLI (`jevq` via uv/pipx) |
| [JevRepoTriage](jevrepo-triage.md) | Self-hosted GitHub issue/PR triage with TypeSafe Jev classifications and operator-approved actions. | TypeScript · web UI + workers (MIT) |
| [Jevris](jevris.md) | Local control plane that uses TypeSafe Jev to decide, verify, and route AI-assisted development work. | Node.js · npm `@webventures/jevris` (MIT) |
| [JevRoute (suncirkles)](suncirkles-jev-router.md) | Route coding tasks to a model id via decision-only JevRoute, with a separate eval harness and recorded evidence. | Python · router library + eval harness (MIT) |
| [JevRouter](jevrouter.md) | Route among models/subagents/skills/MCP/CLIs with TypeSafe Jev Choice plus permissions, risk, confirmation, and receipts. | TypeScript · SDK/CLI/MCP (`jevrouter` 0.1.0) |
| [JevScope](jevscope.md) | Edit Jev projects visually, batch JSONL regression cases, and compare definitions locally. | TypeScript · Studio + local API (pnpm) |
| [jevseek](jevseek.md) | Let DeepSeek propose tokens and TypeSafe Jev (OpenRouter System One) choose the next one. | Python ≥ 3.11 · CLI (`jevseek` 0.1.0) |
| [jevsh](jevsh.md) | Ask TypeSafe Jev the risk of a shell command (LOW–CRITICAL) before confirming execution. | Bash · single-script CLI (MIT) |
| [JevShield](jevshield.md) | Wrap Python/LangChain tool calls with a TypeSafe Jev dual-factor risk gate and keyless local heuristic fallback. | Python · library/PyPI (`jevshield`, Apache-2.0) |
| [jevskillz](jevskillz.md) | Calibrated multi-phrasing Jev checks (claims/tests/AC/triage) as Claude Code skills + CLI. | JavaScript · CLI + skills (MIT) |
| [JevTape](jevtape.md) | Record and replay TypeSafe Jev HTTP decisions from JSON cassettes with contract fingerprint misses. | Java 21 · Maven CLI (`jevtape` 0.5.0) |
| [jevtok](jevtok.md) | Count Jev tokens and estimate billed request input_tokens offline before calling TypeSafe. | Python · library/CLI (`jevtok` 0.1.0) |
| [JevTree (Chuf-H)](chuf-h-jev-tree.md) | Probability tree/graph runtime: compose TypeSafe Jev action probs into path mass and Pareto picks (distinct from taxonomy jev-tree). | Python · CLI/library (`jev-tree` 0.1.0, Apache-2.0) |
| [jevtriage](jevtriage.md) | Triage PRs with TypeSafe Jev Choice (`ready` / `needs_review` / `risky`) plus confidence-gated exit codes and optional labels. | Python · PyPI/Action (`jevtriage` 0.1.0) |
| [jevtrim](jevtrim.md) | LoCoMo compaction benchmark: Jev judge vs retrieval. | Python · research (MIT) |
| [jevwright](jevwright.md) | Write Chromium business-flow tests as user steps; TypeSafe Jev finds controls once, then replay without the model. | TypeScript · Playwright (`@hazymoon/jevwright`, MIT) |
| [jevx (muthuishere)](muthuishere-jevx.md) | Agent skill + CLI for typed yes/no/choice/rating gut checks via System One (hosted or self-hosted); ≠ hawkyre/jevx extension. | Go CLI + npm (`@muthuishere/jevx`) · agent skill (MIT) |
| [JevX (vij-sameerb5)](vij-sameerb5-jevx.md) | Scan a codebase for judgment-shaped rules and replace strong fits with TypeSafe Jev decisions (dry-run/undo). | TypeScript · npm (`@vij-sameerb5/jevx`, MIT) |
| [jevyoumean](jevyoumean.md) | Wrap any CLI so unknown subcommands get TypeSafe Jev intent-based "Did you mean?" suggestions from help text. | Go · CLI (`jym`) |
| [JIS · PARALLELIZE](jis-parallelize.md) | Self-organising swarm: rules first; Jev for verify/adopt/dispute; LLM escalation on low confidence. | TypeScript · swarm harness (Apache-2.0) |
| [JIT-JEV Context OS](jit-context.md) | Epistemic context runtime + TypeSafe Jev System 1 gate for tool-using coding agents | Python · context OS / gate (MIT) |
| [jmc-jev-mcp](jmc-jev-mcp.md) | MCP server that judges JDK Flight Recorder recordings with TypeSafe Jev typed questions. | Java · MCP server (MIT) |
| [JMP](jmp.md) | Local coding workspace: TypeSafe Jev picks the next tool action; DeepSeek/Codex/Bonsai supply arguments; OpenHands/MCP execute. | Python · desktop (pywebview) + CLI (MIT) |
| [Juardrails](juardrails.md) | Manage TypeSafe Jev guardrail policies (YAML/UI), batch questions, apply rules via REST/CLI with audit. | Go · server + CLI (license unspecified at review) |
| [Kassad](kassad.md) | Gate .NET LLM prompts/completions/tools/citations with TypeSafe Jev Allow/Flag/Review/Block verdicts. | C# · .NET library (Apache-2.0) |
| [KiroGraph](kirograph.md) | Index a codebase for symbol lookups and context; set `memoryRelationMode`, `wikiContradictionMode` or `securityAuthDetectionMode` to `'jev'` for typed judgments (or `'strands'` for a local decision server). | TypeScript/Node · CLI + MCP server (`kirograph`, MIT) |
| [laya-packet-analyser](laya-packet-analyser.md) | Triage laptop packet alerts with detectors + local Laya System One judgments and a live dashboard. | Python · stdlib analyser + dashboard (MIT) |
| [laya-skill](laya-skill.md) | Claude Code skill/plugin for local Laya or hosted TypeSafe Jev typed decisions (plus fine-tune helpers). | Claude Code skill/plugin (Apache-2.0) |
| [Leash](leash.md) | Judge each coding-agent turn against un-lintable rules with TypeSafe Jev and a one-way debt ratchet. | TypeScript · CLI/npm (`leash`, MIT) |
| [lintent](lintent.md) | Plain-language lint rules judged by TypeSafe Jev, scoped with tree-sitter. | Rust · CLI linter (MIT) |
| [llmbridge](llmbridge.md) | OpenAI-compatible LLM gateway with L1 rules / L2 TypeSafe Jev / L3 fallback routing. | Python/FastAPI + Vue · gateway (Apache-2.0) |
| [mayi](mayi.md) | Tool-call gate for Claude Code/Cursor/Codex: TypeSafe Jev scores each call; dialog on unsafe (fail-deny on errors). | Rust · CLI (`mayi` 0.1.0) |
| [metajev](metajev.md) | Store typed Jev/System One distributions keyed by state+question+model; apply/change accept/review policies without re-calling the model. | Python · library + SQLite store (MIT) |
| [Metis](metis.md) | Triage new GitHub issues with TypeSafe Jev labels and missing-detail comments via a reusable Action/CLI. | Python · GitHub Action + `metis-triage` 0.1.0 |
| [Misogi](misogi.md) | Sidecar that asks TypeSafe Jev whether a coding agent's "done" claim is actually done (Claude Code/Codex/Kimi). | TypeScript · agent sidecar (MIT) |
| [MM3](mm3.md) | Have an agent ask Jev focused code questions ("does this handler check the caller?") in one call, with verdicts and outcomes tracked over time. | TypeScript · npm `@mvpscale/mm3` · Claude Code plugin (Apache-2.0) |
| [mnemon-memory-agent](mnemon-memory-agent.md) | Agent long-term memory judged with TypeSafe Jev System One over raw records | TypeScript · memory agent (MIT) |
| [mobai-ci](mobai-ci.md) | Run MobAI `.mob` / Maestro mobile UI flows in CI; `.mobflow` steps are judged/acted by TypeSafe Jev. | CLI · GitHub Action |
| [model-router-python](model-router-python.md) | Filter models by limits/budget, then ask TypeSafe Jev which remaining model should handle the prompt. | Python · PyPI library (MIT) |
| [Moongate](moongate.md) | Evaluate PR diffs against JSON semantic rules with TypeSafe Jev and emit CI annotations. | MoonBit / GitHub Action (`brickfrog/moongate`) |
| [mu](mu.md) | Run a pi-based coding agent where Jev (or a local Laya judge, a classifier, or an LLM) makes routine calls; compare judges in shadow mode via `mu ledger` before activating a decision point. | TypeScript · npm `mu-agent` CLI + desktop app (pre-release 0.1.x, MIT) |
| [Navigator (qf-studio)](qf-studio-navigator.md) | Install Navigator in Claude Code, then say `enable judge` with a TypeSafe key so Jev decides loop-trigger, complexity and ambiguity tiers for each prompt. | Python + TypeScript hooks · Claude Code plugin (MIT) |
| [oh-my-jev (apetcu)](apetcu-oh-my-jev.md) | oh-my-pi plugin: TypeSafe Jev tool-call gate (default), optional model router, and latency telemetry (≠ MassiveLabsNet/oh-my-jev). | TypeScript · oh-my-pi plugin (MIT) |
| [olla-jev](olla-jev.md) | Ollama-style local server for HF System One models behind Jev /v1/systemone. | Python · CLI/server (Apache-2.0) |
| [omo-jev-plugin](omo-jev-plugin.md) | OmO/senpi plugin: TypeSafe Jev advises skill/tool fit, loop and completion signals (shadow/advise/act; does not replace permissions). | TypeScript · OmO/senpi npm plugin (`omo-jev-plugin`) |
| [omp-jev-compaction](omp-jev-compaction.md) | Reduce omp tool context with sticky TypeSafe/OpenRouter Jev scores while keeping retained text verbatim. | TypeScript · omp plugin (`omp-jev-compaction` 0.1.0) |
| [onesie](frodi-karlsson-onesie.md) | Unix-pipeable System One CLI for TypeSafe Jev (also OpenRouter/Berget): pipe text, ask a typed question, script the… | Go · CLI (MIT) |
| [open-source-finder](open-source-finder.md) | Rank GitHub open issues for good-first-issue fit with TypeSafe Jev (size/clarity/knowledge/claimed). | Python · CLI/tooling (MIT) |
| [opencode-toolrouter](opencode-toolrouter.md) | Shrink opencode MCP tool schemas per request using TypeSafe Jev tool selection. | TypeScript · opencode plugin (MIT) |
| [Open Jev Bridge](open-jev-bridge.md) | Zero-dep Node MCP + Claude/Codex hooks bridging hosted Jev or local Kev/Laya System One (compaction + completion gates). | Node.js · CLI/MCP (`open-jev-bridge` 0.3.0, MIT) |
| [openclaw-jev (Hyper-AI-Lab)](hyper-ai-lab-openclaw-jev.md) | OpenClaw control plane: intake routing with TypeSafe Jev (≠ yousan openclaw-jev-* plugins) | Python · OpenClaw control plane (MIT) |
| [openclaw-jev-leakguard](openclaw-jev-leakguard.md) | Block OpenClaw posts that leak clients/credentials to the wrong channel; judged by Jev or local Kev. | TypeScript · OpenClaw plugin (MIT) |
| [openclaw-jev-trigger](openclaw-jev-trigger.md) | Plain-language OpenClaw automation triggers judged by TypeSafe Jev (`decisionModel`) each tick. | TypeScript · OpenClaw plugin + CLI (MIT) |
| [openclaw-typesafe-ai](openclaw-typesafe-ai.md) | Add an optional OpenClaw `typesafe_decide` tool for explicit TypeSafe Jev judgments without lifecycle hooks. | TypeScript · OpenClaw plugin (`openclaw-typesafe-ai` 0.1.3) |
| [OpenCode Security Guard](opencode-security-guard.md) | Linux OpenCode shell guard: local read-only check + Jev Noul ≥0.90 auto-allow. | TypeScript · OpenCode plugin (MIT) |
| [opencode-jev-compaction](radqnico-opencode-jev-compaction.md) | On OpenCode compaction, ask Jev which tool calls/outputs are still needed; drop or truncate the rest while keeping user/assistant text verbatim. | TypeScript · OpenCode plugin |
| [opencode-jev-guard](opencode-jev-guard.md) | OpenCode 2 plugin: TypeSafe Jev triages every local/FarHand shell command before run. | TypeScript · OpenCode plugin (`opencode-jev-guard` 0.1.0, MIT) |
| [opencode-jev-plugin (fsodanogm2dev)](fsodanogm2dev-opencode-jev-plugin.md) | Hook OpenCode/OmO to TypeSafe Jev via a local broker for safety, routing, and token-saving transforms. | JavaScript · OpenCode plugin + broker (MIT) |
| [opencode-jev-router](opencode-jev-router.md) | OpenCode Responses proxy: TypeSafe Jev selects reasoning effort for Astra/Luna/Sol with cache lineage. | Node.js 24 · npm CLI (`@robertn702/opencode-jev-router` 0.1.0, MIT) |
| [opencode-smart-reasoning](opencode-smart-reasoning.md) | Route OpenCode per-request reasoning effort with TypeSafe Jev via Zen SystemOne (fail-open). | TypeScript · OpenCode plugin (`opencode-smart-reasoning` 0.2.0) |
| [openjev-mcp (markylaredo)](markylaredo-openjev-mcp.md) | Expose OpenJEV System One judgments over MCP with shared context and multi-question batches. | TypeScript · MCP stdio server (`openjev-mcp`) |
| [openwebui-jev-style-decisions](openwebui-jev-style-decisions.md) | Open WebUI plugin for JEV-style typed decisions via local Ollama (unofficial). | Open WebUI plugin (MIT) |
| [orca-jev-advisor](orca-jev-advisor.md) | Orca Lab plugin: local rules + TypeSafe Jev gate agent commands (ask before force-push/merge/apply). | TypeScript · Orca/Electron plugin (license unspecified) |
| [Pad](pad.md) | Track work for you and your coding agents on local SQLite; optionally let Jev flag `needs_human` / blocked items and route free text to playbooks (`pad playbook match`). | Go · single binary with embedded web UI + MCP/agent skill (Apache-2.0) |
| [paperclip-jev](paperclip-jev.md) | Run Paperclip with automatic task routing by TypeSafe Jev (fork of paperclipai/paperclip). | TypeScript · Paperclip fork + Jev router (MIT) |
| [patdown](patdown.md) | Lint a tree against fuzzy markdown rules with a swappable judge; default backend is TypeSafe Jev. | TypeScript · npm CLI (`patdown`) and Effect packages |
| [PDF Race](pdf-race.md) | Race Docling→TypeSafe Jev vs Gemini on the same PDFs with committed keyless replays. | Node.js ≥ 20 · local/Vercel bench (`pdf-race` 1.0.0) |
| [PerfectRecall](perfectrecall.md) | Hermes/Python agent memory: TypeSafe/OpenRouter Jev evidence questions over local SQLite (Mnemosyne-compatible; no embeddings). | Python · Hermes provider + library |
| [Pi Adaptive Effort Router (XDeviation)](xdeviation-pi-jev-router.md) | Change Pi thinking level only with TypeSafe Jev (not the model); distinct from philippdubach pi-jev-router. | TypeScript · Pi extension (`pi-jev-router` 0.2.0, MIT) |
| [pi-advisor](pi-advisor.md) | Configurable Advisor/Executor Pi flow with optional TypeSafe Jev consultation filter and turn gate. | TypeScript · Pi plugin (`pi-advisor-flow`, MIT) |
| [pi-extensions (narumiruna)](narumiruna-pi-extensions.md) | Install Pi extensions including TypeSafe Jev decision, compaction, and FTS5+Jev search packages (`@narumitw/*`). | TypeScript · Pi monorepo (MIT) |
| [pi-follow-through](pi-follow-through.md) | Nudge Pi after agent_settled only when TypeSafe Jev cites unfinished work above a probability threshold. | TypeScript · Pi extension (`pi-follow-through`) |
| [pi-heed](pi-heed.md) | Enforce evolving conversational constraints on Pi tool calls; TypeSafe Jev classifies policy changes, code owns the ledger. | TypeScript · Pi extension (`pi-heed`) |
| [pi-jev](pi-jev.md) | Add a Jev pre-tool gate, output judge, and jev_ask tool to the Pi coding agent (shadow mode default, fail-open). | TypeScript · Pi extension (npm) |
| [pi-jev (kurowashi)](kurowashi-pi-jev.md) | Add TypeSafe Jev semantic checks for Pi file edits and new-file placement (content-guard + placement plugins). | TypeScript · Pi extensions monorepo (MIT) |
| [pi-jev-context](pi-jev-context.md) | Trim long pi tool outputs before they enter context (comparison first; TypeSafe Jev only when needed) with lossless recall. | TypeScript · Pi extension (`pi-jev-context`) |
| [pi-jev-effort](pi-jev-effort.md) | Set Pi thinking level per prompt from a TypeSafe Jev difficulty score, capped by remaining quota. | TypeScript · Pi extension (`pi-jev-effort` 0.1.0) |
| [pi-jev-permit](pi-jev-permit.md) | Gate Pi bash/write/edit calls with TypeSafe Jev allow judgments after local hard-deny and read-only fast paths. | TypeScript · Pi extension (`pi-jev-permit` 0.2.0) |
| [pi-jev-router](pi-jev-router.md) | Route pi tasks across OpenRouter models with TypeSafe Jev classification and local Pareto/role policy (shadow default). | TypeScript · Pi extension (`pi-jev-router` 0.1.0) |
| [pi-jev-sentinel](pi-jev-sentinel.md) | Check Pi/Claude/Codex tool calls, outputs, and replies with Jev intent/risk and injection screens (fail-closed without a key). | TypeScript · Pi extension and host hooks |
| [pi-shift-router](pi-shift-router.md) | Route Pi turns between cheap and strong model tiers; optional TypeSafe Jev probability judge. | TypeScript · Pi npm extension (MIT) |
| [pi-subagent-jev](pi-subagent-jev.md) | pi package: gate subagent dispatches via a Jev System One endpoint; expose jev_ask/jev_models (needs pi-subagents). | TypeScript · pi package (MIT) |
| [pi-thinking-router-jev](pi-thinking-router-jev.md) | Pi extension: TypeSafe Jev (or local rules) picks thinking level low/medium/high/xhigh from task feedback. | TypeScript · Pi extension (license unspecified) |
| [pi-typesafe-approve](pi-typesafe-approve.md) | Pi extension: System One/Jev triage auto-approves routine Bash; escalates the rest to a human. | TypeScript · Pi extension (MIT) |
| [pi-typesafe-bash-guard](pi-typesafe-bash-guard.md) | Classify Pi bash tool calls and user `!` shells with TypeSafe Jev before execution. | TypeScript · Pi extension (npm `@gowthamgts/pi-typesafe-bash-guard` 0.1.0) |
| [pi-verdict](pi-verdict.md) | Minimal Pi allow/ask/deny permission gate with optional TypeSafe Jev classifier adapter. | TypeScript · Pi extension (`pi-verdict`, MIT) |
| [pi-warden](pi-warden.md) | Add configurable action holds, project-rule feedback and context checks to Pi using local policy and Jev judgments. | TypeScript · Pi extension |
| [plain-language-gate](plain-language-gate.md) | Jev plain-language readability gate (six checks → pass/review/rewrite) for agent writing. | Python · skill/CLI (MIT) |
| [playwright-jev](criguex-playwright-jev.md) | Assert UI meaning with Jev Noul/Choice/Score helpers that fail closed on ambiguity, missing keys, or timeouts. | TypeScript · `@playwright/test` ≥ 1.45 · Node ≥ 20 |
| [playwright-jev (AdriaanVE)](adriaanve-playwright-jev.md) | Use TypeSafe Jev in Playwright for failure triage, retries, healer gating, snapshot pruning, locator healing, and test ordering. | TypeScript · Playwright helpers (MIT) |
| [Poltergeist](poltergeist.md) | Scan code for secrets as usual; add `-classify` so each finding gets a `real_secret_probability` and a `likely_real` / `uncertain` / `likely_dummy` label from Jev. | Go · CLI and library (Apache-2.0) |
| [prompt2jev](prompt2jev.md) | Convert natural language, an LLM prompt, or prompt-running code into a TypeSafe Jev decision package. | Python · agent skill + stdlib CLI |
| [pytest-jev](pytest-jev.md) | Semantic pytest assertions (holds/lacks/choice/score) judged by TypeSafe Jev via typesafe-sdk. | Python · pytest plugin (`pytest-jev` 0.1.0) |
| [Qualixar Jev Decision Layer](qualixar-jev-decision-layer.md) | Route bounded task/tool/skill/review choices through TypeSafe Jev (optional Laya) via one MCP server shared across five hosts. | Python · MCP plugin (`qualixar-jev-decision-layer` 1.0.7, MIT) |
| [Quicksilver](quicksilver.md) | Hand bulk judgment/shortlist calls from Claude Code to TypeSafe Jev (parallel typed verdicts). | JavaScript · Claude Code skill/plugin (MIT) |
| [rea-jev](rea-jev.md) | Add fast typed checks to reverse-engineering sessions: route, scope/risk gate, evidence scoring and a done-check around REA tools. | JavaScript · Claude Code plugin + CLI (MIT) |
| [Reflex (kaustav1996)](kaustav1996-reflex.md) | Pi coding agent with TypeSafe Jev action gates, model-tier/skill routing, completion checks, and outside-result screening (code owns thresholds). | TypeScript · CLI (`reflex` / `reflex-agent` 0.1.0, MIT) |
| [Reflex (ursuciprian)](ursuciprian-reflex.md) | Pre-execution risk gate + prompt-injection guard for coding agents; optional TypeSafe Jev/Laya (≠ kaustav1996 Reflex). | JavaScript · agent hooks (`@ursuciprian/reflex`, MIT) |
| [Repo Graph](repo-graph.md) | Map and search a large repository locally, and opt in to Jev reranking of the top candidates when local ranking is not enough. | Python · `repo-graph-agent` (uv tool install from Git tag) |
| [Responsible AI Harness](responsible-ai-harness.md) | Assess AI systems with hard rules plus optional TypeSafe Jev judge; checksummed evidence bundles and offline report UI. | TypeScript · assessment harness + static UI (`responsible-ai-harness` 0.1.0) |
| [riff](riff.md) | Lint prose with ruff-style rule codes; deterministic static rules plus optional TypeSafe Jev judgment rules. | Python · CLI (`riff` / `riff-lint` 0.1.0) |
| [rippy](rippy.md) | Gate agent shell commands with allow/ask/deny rules; with `rippy-jev`, uncertain asks (unknown command, unresolvable variable) may be auto-approved when Jev is confident and the effect class is allowed. | Rust · CLI hook (`rippy-cli`, crates.io/Homebrew; `rippy-jev` feature build) (MIT) |
| [RLCD Gateway](rlcd-gateway.md) | Self-hosted Go gateway: LLM routing with context pruning plus Jev/open-rlcd System One audit/calibration dashboard. | Go · binary/npm/PyPI (`rlcd-gateway`, Apache-2.0) |
| [s1-tui](s1-tui.md) | Terminal UI for System One typed decisions over laya + TypeSafe Jev backends. | TUI (MIT) |
| [Scope (code context selector)](tjeastmond-scope.md) | Hand a coding agent or developer a compact, evidence-backed set of code chunks for a task instead of whole files. | TypeScript · Bun tooling · Node 24+ CLI |
| [semantic-assert](semantic-assert.md) | Assert plain-English claims about UI/text state with TypeSafe Jev (Playwright helpers; thresholds in code). | TypeScript · npm packages + Playwright adapter |
| [SemDecide](semdecide.md) | Run TypeSafe Jev predicates, routes, scores, and JSONL filters as Unix CLI exit codes for pipelines and CI. | Python · CLI (`semdecide` 0.2.1) |
| [sensored](sensored.md) | Cut false positives in PII redaction by letting Jev confirm ambiguous detections (currently `person_name_lite`) in the async API; fails open when the provider is unavailable. | TypeScript · npm `sensored` (optional `@typesafe-ai/sdk`) |
| [similarity-ts-jev](similarity-ts-jev.md) | Run similarity-ts + fallow on TypeScript, keep only the pairs TypeSafe Jev judges worth merging (with copy/derive/extract shape), and calibrate the cutoff. | TypeScript · npm CLI/library (`@kongyo2/similarity-ts-jev` 0.2.0, MIT) |
| [Skill Dash](skill-dash.md) | Judge Claude Code/Codex skills with TypeSafe Jev (usefulness/redundancy/clarity/action) in a local dashboard. | Python · stdlib loopback server + SQLite |
| [Skillbox](skillbox.md) | Share versioned agent skills and use optional Jev scores to recommend authorized skills for a task. | TypeScript / Bun / PostgreSQL · skill library, MCP and CLI |
| [SkillRanker](skillranker.md) | Rank which agent skills fit the next step from live session context using Jev wide/re-rank stages. | Rust · CLI (`sr`), hooks and TUI |
| [skill-scanner](skill-scanner.md) | Scan Agent Skills offline before install and gate Claude Code/Codex/OpenCode/Pi/`npx skills`; optional Jev judge. | TypeScript · npm (`@french-castle/skill-scanner`, MIT) |
| [Skylos](skylos.md) | Scan PRs for dead code, security issues, and AI-code mistakes; optionally have TypeSafe Jev review static dead-code findings. | Python · CLI (`pip install skylos`) (Apache-2.0) |
| [SlidePilot](slidepilot.md) | Advance Slidev decks from presenter voice when TypeSafe Jev and TypeScript policy agree the slide is complete. | TypeScript · Slidev addon + Cloudflare Worker (0.1.0) |
| [slophound](slophound.md) | Lint Markdown or stdin for LLM-prose patterns with bite/bark/sniff tiers and CI-friendly exit codes; Jev removes false positives for rules that ask it to. | Python · CLI + Python interface + agent skill (MIT) |
| [SmartMoney-Cub](smartmoney-cub.md) | Capture offline trading-journal evidence packs and optionally ask TypeSafe Jev typed review questions (read-only; no orders). | Python · `smcub` CLI and harness |
| [Snapif](snapif.md) | Gate coding-agent tool calls (e.g. Claude Code PreToolUse hooks) with a calibrated verdict while the host keeps the final decision. | Rust · crate `snapif` on crates.io (MIT) |
| [Sniff Test](snifftest.md) | Lint Markdown/prose with local countable rules plus optional confirmed TypeSafe Jev judgment rules. | TypeScript/Bun · CLI (`snifftest` 0.1.0) |
| [specpi-jev-guard](specpi-jev-guard.md) | Gate risky Pi agent shell/file commands with local rules then TypeSafe Jev danger scores. | TypeScript · Pi npm extension (MIT) |
| [Spotlight (Buried Signals)](spotlight.md) | Run source-backed investigations with agent skills; opt in per install and per investigation so Jev checks each finding against its quoted evidence before publication. | Python · agent skills + scripts (MIT) |
| [Stanley Code](stanley-code.md) | Review code changes, triage failures, and extend Jev workflows; optional Pi delegation can edit the repository. | TypeScript · source-built CLI and workflow runtime |
| [stil-lint](stil-lint.md) | Let agents that message people check and revise drafts before sending; local layers run without any network call. | Python · CLI + MCP server (MIT) |
| [stingray](stingray.md) | Stop half-done Claude Code/Codex turns with TypeSafe Jev judgments (empty action, broken promise, watch with nothing running). | Shell · Stop hook (MIT) |
| [stop-rules](stop-rules.md) | Coding-agent stop hook: TypeSafe Jev yes/no per changed piece against written team rules (multi-agent + optional team server). | TypeScript · CLI (`stop-rules` 0.1.0) |
| [stuntd](stuntd.md) | Local Jev-compatible proxy: serve/learn typed System One decisions on a Laya head (or zero-shot), optional OpenAI/Jev upstream. | Python ≥ 3.10 · PyPI (`stuntd` 0.1.0, Apache-2.0) |
| [Sudus](sudus.md) | Track requirements and verdicts in the repo; at Consequential choices, let Jev score the agent's draft (evidence, reach, contract, surface, ambiguity) as its gut check. | Node.js · agent plugin (command, five skills, hooks) (MIT) |
| [super-jev](super-jev.md) | Run evidence → typed Jev judgments → permitted actions → verified outcomes with local JSONL traces. | TypeScript · harness (Node ≥ 24) |
| [Supercov](supercov.md) | Code quality and test coverage for coding agents: Jev scores each source file so the agent knows what to fix first. | Rust · CLI via npm, Homebrew, Go or crates.io |
| [System One Harness](systemone-harness.md) | Drive finite-action environments with TypeSafe Jev (OpenRouter/TypeSafe): one typed decision per step, confidence gates, full traces. | Python · CLI `s1` (`systemone-harness` 0.4.0) |
| [System One Playground](system-one-playground.md) | Write SysOneScript, use a Go System One client, semlint, and Studio/VS Code—offline first, optional live Jev. | Go · CLI/extension (`sysone`/`sos`) + `typesafe` module |
| [system-one-reviewer](system-one-reviewer.md) | Review local git ranges with deterministic clustering + TypeSafe Jev/System One typed judgments and an eval harness. | Python · local CLI reviewer (MIT) |
| [systemone-poc](systemone-poc.md) | Pre-route Pi/OpenCode/DSH coding agents with Jev/Laya before the main agent run (POC + reports). | Plugins/MCP · Pi/OpenCode/DSH (MIT) |
| [Taste Lint](taste-lint.md) | Catch AI-sloppy UI motion/copy/typography before ship; optional TypeSafe Jev under-review judgments via Gateway or direct. | Node.js ≥ 24.11 · npm CLI (`taste-lint` 0.3.0) |
| [tax-doc-classifier](tax-doc-classifier.md) | Classify tax PDF page text into IRS form ids and page kinds with TypeSafe Jev Choice over shipped criteria. | TypeScript · library (`tax-doc-classifier`) |
| [tdd-gate](tdd-gate.md) | Dual-agent TDD gates: TypeSafe Jev coverage/blame/gaming/weakening/drift judgments; optional isolated orchestrator. | TypeScript · CLI (`tdd-gate` 0.1.0, MIT) |
| [Temporal Agent Harness](temporal-agent-harness.md) | Approve or escalate agent tool calls with one typed Jev judgment (`auto_mode_evaluator=agent.jev_evaluator()`), failing closed on low confidence. | Python · `temporal-agent-harness` package (MIT) |
| [Ten Levels of Jev](ten-levels-of-jev.md) | Walk ten incremental Jev levels from a smart if-statement to a pi agent that reaches for Jev itself (offline mocks + live lab). | TypeScript · Vue lab + pi agent levels (MIT) |
| [The Jev-enator](the-jev-enator.md) | Claude Code hooks: TypeSafe Jev danger gate, failure notice, and log-only completion check. | Python · stdlib hooks + install scripts |
| [thinkdial](thinkdial.md) | Set Claude Code reasoning effort per turn with TypeSafe Jev (main loop, subagents, Codex; fail-open). | TypeScript · Claude Code mod (MIT) |
| [Tidepool](tidepool.md) | Turn recurring agent procedures into typed Haskell programs that call Jev only where a decision depends on meaning. | Rust · Haskell · Nix/Buck (PolyForm Shield 1.0.0) |
| [tiergear](tiergear.md) | Spend less on easy Claude Code prompts and more on hard ones by letting Jev choose the tier, changing effort mid-session and the model only on the first turn by default. | Claude Code plugin · Node 20+ CLI (npm `tiergear`) |
| [tink-route](tink-route.md) | Gate Agent Skills with TypeSafe Jev (specialist Noul + Choice), then optionally install via Tink. | Python · CLI (`tink-route` 0.3.1) |
| [todo-jev](todo-jev.md) | Classify requests into a 3-tier path (local rule / Jev skill / foundation model) with skill profiles and preflight. | Python · Typer CLI (`todo-jev` 0.1.0) |
| [tokengate](jev-model-tokengate.md) | Buffer streamed LLM tokens and gate each window with TypeSafe Jev before the client sees them. | Node.js · OpenAI-compatible proxy (`tokengate` 0.1.0) |
| [toolgate](toolgate.md) | Gate Claude Code and MCP tool calls with static rules plus TypeSafe Jev risk judgments and a local audit log. | TypeScript · CLI, Claude Code hook and MCP proxy |
| [triagedy](triagedy.md) | Triage JSONL security alerts with TypeSafe Jev typed questions; route outcomes in ordinary Rust code. | Rust · CLI (`triagedy` 0.1.0) |
| [Tripwire](tripwire.md) | Abort bad streaming completions mid-flight using TypeSafe Jev (or an offline heuristic) inside an OpenAI-compatible proxy. | Python · package (`tripwire` 0.1.0) |
| [trirouter](trirouter.md) | Install hooks, an MCP server and a `trirouter` command so every prompt is routed to the right agent/model/effort, with parallel agents, queue protection and shared skills. | Python · installer + hooks + MCP server (MIT) |
| [Typed Evals](typed-evals.md) | Evaluate RAG/agent outputs and guard tools with TypeSafe Jev judges and optional calibration. | Python · library/CLI (`typed_evals`) |
| [typesafe-agent-gates](typesafe-agent-gates.md) | Gate unattended LangChain/Deep Agents shell commands and triage with TypeSafe Jev middleware. | Python · LangChain middleware |
| [TypeWright](typewright.md) | Compile Decision Contracts into checksummed typed Jev JSON programs (DSPy/GEPA search; runtime without DSPy). | Python 3.11+ · compiler + runtime (MIT, alpha) |
| [unsafe-c-finder](unsafe-c-finder.md) | Classify C/C++ snippets and staged hunks with TypeSafe Jev via OpenRouter (unsafe probability, then CWE when over threshold). | Python · CLI (`unsafe-c-finder`, MPL-2.0) |
| [use-jev](use-jev.md) | Skill that lets Claude Code/Codex ask TypeSafe Jev typed questions and keep writing in the agent. | Agent skill · OpenRouter typesafe/jev-1.13 (MIT) |
| [VexJoy Agent](vexjoy-agent.md) | Route plain-English requests to specialist agents/skills; optional `/d` uses TypeSafe Jev classification and intent gates. | Python · agent toolkit (Claude Code / Codex hooks) |
| [voicevox-jev-proxy](voicevox-jev-proxy.md) | Fix VOICEVOX readings (and optional intonation) with TypeSafe Jev via CLI or a VOICEVOX-compatible proxy. | Python · CLI + VOICEVOX-compatible proxy (MIT) |
| [wellposed](wellposed.md) | Lint TypeSafe Jev requests for broken paths, missing Choice escape hatches, and other structural smells before calling the API. | TypeScript · npm CLI (`wellposed` 0.4.0, zero deps) |
| [winnow](winnow.md) | Hide confident-irrelevant Claude Code tool-result blocks with TypeSafe Jev (or adapter) judgments; recall stubs on demand. | Python · Claude Code hooks + sidecar CLI (`winnow` 0.5.0) |
| [Yoshi](yoshi.md) | Local Claude Code/Codex context-pruning proxy: TypeSafe Jev via AI Gateway judges omit/keep spans (experimental POC). | Bun/TypeScript · loopback proxy (`yoshi` 0.1.0) |
| [your-cto-jev](your-cto-jev.md) | CTO-style agent guard: Jev blocks leaked secrets and destructive commands. | Agent hook / guard (MIT) |
| [Zevals](zevals.md) | Assert behaviours on full agent transcripts with Jev as a fast, low-variance judge, and call an LLM only to explain failures. | TypeScript · npm `@zevals/core` (MIT) |

## Games and simulation

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Honeytongue](honeytongue.md) | NPC persuasion engine: TypeSafe Jev judges whether player dialogue convinced a character. | JavaScript · library (MIT) |
| [jev plays snake](jev-plays-snake.md) | See a closed-menu, deadline-bound control loop where code supplies exact facts and Jev only chooses among legal moves. | TypeScript · Vite/React UI · Hono proxy · `@typesafe-ai/sdk` |
| [Jev Vampire Survivors](jev-vampire-survivors.md) | BepInEx + Python brain: TypeSafe Jev plays real Steam Vampire Survivors with a live ops dashboard. | BepInEx plugin + Python (MIT) · TypeSafe Jev |
| [Jev NetHack](jev-nethack.md) | TypeSafe Jev plays NetHack 5.0: code lists legal moves, Jev picks one; live dashboard. | Python + NetHack50 + web dashboard (MIT) |
| [jev-drone](jev-drone.md) | Study typed maneuver judgments alongside deterministic simulated flight control and inspect a separate tunnel experiment. | Python / MuJoCo · simulation and replay |
| [jev-libero](jev-libero.md) | Study fine-grained LIBERO robot actions with TypeSafe Jev layered choices and local physics previews. | Python · CLI and MuJoCo/LIBERO extras |
| [jev-plays](jev-plays.md) | Watch TypeSafe Jev play Craftax (macro/raw actions) with optional LLM planner-as-facts and a local web UI. | Python · Craftax harness + viewer |
| [jev-robotics-eval](jev-robotics-eval.md) | Evaluate JEV-compatible robot control on MetaWorld/RoboTwin (text/vision, privilege levels). | Python · eval harness (MIT) |
| [JevBird](jevbird.md) | Watch Jev play Flappy Bird from a typed Choice over precomputed paths, with live request/response console output; manual mode without a key. | Python 3.10+ · pygame + `typesafe-sdk` (MIT) |
| [Ministry of Truth](ministry-of-truth.md) | Play (or study) a game whose only actions are your words, judged by one batched Jev call per briefing with an automatic offline fallback. | Vanilla JS · zero-dependency Node server |
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
| [Laya for Home Assistant](home-assistant-laya.md) | Run a fully local Assist conversation agent on open-weight Laya with speculative intent/entity scoring (independent of hosted Jev). | Python · Home Assistant integration (Apache-2.0) |

## Independent model research

These projects study related typed-decision patterns using other models. They are independent research implementations, not official Jev releases or validated substitutes; their guides separate code, model and dataset licensing, and reported benchmarks from catalog checks.

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [AnyJev (Nokia Applied Research)](nokia-anyjev.md) | Turn an open LLM into Jev-style typed decisions with probabilities (L0–L2); independent of official Jev. | Python · PyPI (`anyjev` 0.1.0, Apache-2.0) |
| [assay](assay.md) | Run local typed Choice/Score/Noul-style decisions with calibrated confidence (assay; independent of hosted Jev). | Python · stdlib local decision engine (MIT) |
| [basal](basal.md) | Self-host Jev-style typed decisions (probability per allowed answer) on your GPU or Mac, and compare against hosted Jev on the maintainer's Werdykt benchmark. | Python · `basal-serve` engine (vLLM/SGLang/MLX/llama.cpp backends) (Apache-2.0) |
| [Bongard](bongard.md) | Run Bongard open System One judgments (parallel typed questions → probabilities); independent of hosted Jev. | Python · HF weights + inference (Apache-2.0) |
| [Brier](brier.md) | Run a local MLX Jev-format choice/score/noul decision model (PT-BR training focus) on Apple Silicon. | Python · MLX LoRA decision model (Apache-2.0) |
| [calfram-bench](calfram-bench.md) | Calibration audit of TypeSafe Jev on 25 public benchmarks with CalFram (code + paper). | Python · research harness (MIT) |
| [Can you fool Jev?](can-you-fool-jev.md) | See where Jev and local decision models break on trick choice, yes/no and score questions, and rerun the same requests against your own endpoint. | Python · dataset + scripts (MIT) |
| [Canopy-Jev](canopy-jev.md) | Run Canopy-Jev tree-based typed decisions with shared context and isolated branches (independent of hosted Jev). | Python · Qwen tree decision research (MIT) |
| [Chinese-Jev](gulucaptain-chinese-jev.md) | Build/fine-tune Chinese typed-decision models with the Chinese-Jev pipeline and CJ-Bench (weights release pending; independent of hosted Jev). | Python · research pipeline (Apache-2.0) |
| [cleffa](cleffa.md) | Run Cloudflare Clef/Clef-Flash locally on Apple Silicon Metal and serve POST /v1/systemone typed decisions (BF16; text-only v1). | C11 + Metal 4 · clef/clef-server (MIT) |
| [CLM (Contrastive Language Models)](contrastive-lm.md) | Self-host typed decisions (noul/choice/score) with CLM-8B, rank free-form candidates directly, compare against Jev on the bundled T-Rex example, or fine-tune the head on your own trajectories. | Python · `contrastive-lm` package (`clm-serve`, `CLMClient`), vLLM embedding server (Apache-2.0) |
| [codegraph-jev](codegraph-jev.md) | Benchmarks BM25/embeddings/call-graph + Jev judge against a coding agent on code-reading tasks. | Python research harness · TypeSafe Jev (MIT) |
| [Conjevture](conjevture.md) | Combine Boolean rules with declared probability models; convert Jev Noul/Choice answers while keeping provenance (offline example; optional live game). | TypeScript · npm library (MIT) |
| [Cygnet recipe](cygnet-recipe.md) | Serve a self-hosted `/v1/systemone`-compatible decision endpoint from stock Gemma weights and reproduce the maintainer's JevBench public-set run. | Python · vLLM 0.30.0 + shim (`shim/decision_server.py`) (MIT) |
| [Decis](chaitin-decis.md) | Self-host a Jev-compatible `/v1/systemone` API with open Laya/kev engines in Docker (independent of hosted Jev). | Python · Docker inference server (Apache-2.0) |
| [Decision Index (apolinario)](apolinario-decision-index.md) | Reproduce the Decision Index typed-decision benchmark suite locally or as one Hugging Face Job (not affiliated with TypeSafe). | Python · Decision Index kit + HF Jobs (MIT) |
| [Deqio](deqio.md) | Self-host typed noul/choice/shared decisions behind one local API with swappable engines (Kev/Laya/Open-Jev, etc.). | Python · local decision server + UI (MIT) |
| [dopp](dopp.md) | Proxy Jev-shaped decisions, capture traffic, train a small owned model, and serve hosted/offline/in-browser. | Python/TypeScript · capture + train/serve (MIT) |
| [DriveJev](drivejev.md) | Run/study DriveJev-4B open System I driving decisions (behaviour probabilities) with the JevPilot closed-loop harness. | Python · HF weights + simulator harness (MIT) |
| [EuLLM](eullm.md) | Serve Jev-shaped typed decisions locally (up to 64 questions per request) next to ordinary chat endpoints, from an ARM board to data-centre GPUs, with every decision written to an audit trail. | Rust (llama.cpp-based) · single binary engine (AGPL-3.0) |
| [goinfer](goinfer.md) | Run Jev-shaped decisions locally from Go, scoring options with a GGUF model or a JEV-layout decision head, with published measurements of how that compares to a trained head. | Go · library + `goinfer-serve` / `goinfer-chat` binaries (MIT) |
| [gutsy](gutsy.md) | Run gutsy-0.8b local calibrated yes/no/choice/score decisions via Jev-compatible APIs on CPU (independent of hosted Jev). | Python · llama.cpp + HF GGUF (Apache-2.0) |
| [imajev](imajev.md) | Open multimodal typed-decision models that answer constrained options with probabilities and can't-tell. | Open weights · local serve (Apache-2.0); not TypeSafe-hosted Jev |
| [J3v](j3v.md) | Edge-compiled System One decisions (J3v∶Jev :: k3s∶k8s) with Rust compiler and firmware demos. | Rust · compiler/runtime (MIT) |
| [Jeeves (PostHog)](posthog-jeeves.md) | Run a 9B Jev-like reasoning decision model (noul/choice/score) via a Jev-compatible API; independent of hosted TypeSafe Jev. | Python · open weights + serving (MIT) |
| [Jeff (firelex)](firelex-jeff.md) | Run Jev-format choice/noul/score decisions locally with a small base model plus task adapters, e.g. in front of a larger local LLM. | Python · `jeff-serve` (uv) · Hugging Face weights / GGUF |
| [jev-guardrail-benchmark](jev-guardrail-benchmark.md) | Reproduce WSO2 AI Gateway TypeSafe Jev guardrail accuracy/latency/cost vs Azure Content Safety and an LLM judge. | Python · WSO2 AI Gateway benchmark (Apache-2.0) |
| [jev-imdb-benchmark](jev-imdb-benchmark.md) | Reproduce Jev IMDB review benchmarks (sentiment/spoilers/quality) with published metrics. | Python · IMDB benchmark harness (MIT) |
| [Jev-Lite](jev-lite.md) | Serve local System One–style Choice/Score/Noul decisions via FastAPI (Qwen backbone; independent of hosted Jev). | Python · FastAPI + PyTorch (Apache-2.0) |
| [jev-zh-tw-eval](jev-zh-tw-eval.md) | Reproduce zh-TW System One evals (Plumb-4B/Ollama) with adversarial and calibration probes (independent of hosted Jev). | Python · Ollama `/v1/systemone` eval toolkit (MIT; docs separate) |
| [JevAlt](jevalt.md) | Run open Jev-API–compatible Choice/Score/Noul models locally (EN/TR/DE) on CPU; not TypeSafe-hosted. | Python · HF open models (Apache-2.0) |
| [jev-browsecomp](jev-browsecomp.md) | Measure Jev document screening vs RLM/LLM arms on BrowseComp-Plus with id→span citation checks. | Python · research harness (Apache-2.0) |
| [jev-calibration](jev-calibration.md) | Plot and reproduce Jev calibration (reliability/ECE) on 240 labelled tool-call cases. | Python research scripts (Apache-2.0) |
| [jev-fanout-bench](jev-fanout-bench.md) | Measure Jev multi-question fan-out billing linearity and savings vs separate calls. | Python · benchmark + raw results (MIT) |
| [jev-frontier-bench](jev-frontier-bench.md) | Reproduce Jev vs frontier LLM typed-decision accuracy/calibration/cost on shared 200-item set. | Python · benchmark suite (MIT) |
| [Jev-LCT](jev-lct.md) | Looped Calibration Transformer System One engine with Jev-shaped Choice/Noul/Score serving; independent of hosted Jev. | Python · research engine + HF weights (Apache-2.0) |
| [Jevometry](jevometry.md) | Analyze System One / Jevlike decision probability models with information geometry (Fisher sensitivity); does not orchestrate agents. | Python · research toolkit (MIT) |
| [Jev-Omni](jev-omni.md) | Run an open multimodal System One–style classifier (text/image/audio/video → option probabilities) on Gemma 4 12B IT; independent of official Jev. | Python / PyTorch · HF weights (CUDA, ~50 GB FP32) |
| [jev-omni.js](jev-omni-js.md) | Run independent Jev-Omni multimodal decisions in-browser on WebGPU (text+images; WIP video/audio). | JavaScript · onnxruntime-web (Apache-2.0) |
| [jev-router (peptidehackers)](peptidehackers-jev-router.md) | Train/serve schema-typed probability heads with Wilson-certified act-or-escalate routing (numpy-only; independent of hosted Jev). | Python · numpy library + infer/approve/monitor (MIT) |
| [Jev-Style](jev-style.md) | Local System One–compatible decision models + skills/guard/MCP tooling; independent of hosted Jev. | Python · local server + skills/MCP (Apache-2.0) |
| [jev-switch](arcj137442-jev-switch.md) | Expose `/v1/systemone` locally and route/failover across configured upstream adapters (Vercel, Laya) via an editable DAG; dashboard + Tauri shell. | Rust (axum) · React UI · Tauri · Docker |
| [jevbench (dhruvmehra)](dhruvmehra-jevbench.md) | Reproduce TypeSafe Jev vs LLM/BERT/Laya/NLI text-classification accuracy, calibration, latency, throughput, and cost… | Python · benchmark suite (MIT) |
| [JevBench (metamorphic)](jevbench.md) | Run metamorphic coherence tests (50 probability/choice laws) on typed decision models; no gold labels required. | Python · PyPI (`jevbench`, Apache-2.0) |
| [JevEmbed](jevembed.md) | Turn embedding models into Choice/Score/Noul decisions via a Jev-shaped Python API/CLI/HTTP server. | Python · framework + HF configs (Apache-2.0) |
| [Jevlet](jevlet.md) | From-scratch System One–style decision model research + Windows command palette; independent of hosted Jev. | Python · research model + desktop app (MIT) |
| [Jevlike](jevlike.md) | Train a small option-attention scorer with synthetic data and optional frozen encoders; independent of official Jev. | Python / PyTorch · research starter |
| [jevos](jevos.md) | Serve yes/no (Noul) decisions from a CPU-only, offline 1B GGUF model behind a Jev-compatible `/v1/systemone` API. | Python/FastAPI · llama.cpp GGUF weights (MIT) |
| [JevOss](jevoss.md) | Probe suite for Jev-API decision models: accuracy, calibration, adversarial recipes. | Python · eval harness (Apache-2.0) |
| [jev-web](jev-web.md) | Run open-jev/Laya/Strands/Bekko/Decision 2.0 typed decisions in-browser after weight cache (no hosted TypeSafe required). | TypeScript · npm `jev-web` + Transformers.js (MIT) |
| [kevala](kevala.md) | Run Laya/Kev/Bruv/SemIf-style typed decisions in-browser via Rust→WASM + WebGPU (no server; independent of official Jev). | JavaScript/WASM · npm/CDN (`kevala`, Apache-2.0) |
| [L2S1](l2s1.md) | Turn local GGUF model scores into typed binary/choice/ordinal decisions with abstention policy (not TypeSafe-hosted). | Rust · CLI/runtime + SDKs (MIT) |
| [laya-candle](laya-candle.md) | Run local Laya typed Choice/Score/Noul in pure Rust via Candle (no Python; not TypeSafe-hosted). | Rust · Candle crate (Apache-2.0) |
| [laya-guardrails](laya-guardrails.md) | Fast input/tool/output guardrails using self-hosted laya-pt-es-typed System One (not hosted Jev). | Python · FastAPI + HF model (Apache-2.0) |
| [layajev](layajev.md) | Serve a local `/v1/systemone` subset on verified Laya (in-process Go/ONNX); not TypeSafe-hosted. | Go · npm (`@metalagman/layajev`, MIT) |
| [laya-vs-jev](zaferayan-laya-vs-jev.md) | Head-to-head local Laya (MLX) / Ollaya vs TypeSafe Jev on ~900 cases across 3 tasks and 6 languages. | HTML / harness · multilingual bench (MIT) |
| [lev (Abhinavexists)](lev.md) | Run an open Qwen3.5-4B LoRA System One model over `/v1/systemone` (independent of hosted Jev). | Python · model + harness (Apache-2.0) |
| [Lichen](lichen.md) | Run a local `/v1/systemone` drop-in for typed choice/noul/score (incl. images) on open weights; independent of hosted Jev. | Python · local decision engine (MIT) |
| [Malkuth](malkuth.md) | Multilingual open decision models (Choice/Noul/Score) via Kev. | Weights · research (Apache-2.0) |
| [mcp-agent-openjev](christofmilius-mcp-agent-openjev.md) | Local OpenJev Choice/Noul/Score decision service for agents via MCP + CLI (LM Studio logprobs; not TypeSafe-hosted). | Python · MCP/CLI (MIT) |
| [NanoJev](nanojev.md) | Study independent Qwen-based typed decision heads, local serving, and game controllers with recorded comparisons. | Python / PyTorch · model research and replay |
| [Noma](noma.md) | Self-host fast single-pass decisions (classify, route, check) with an explicit abstain signal for handing off to a reasoning model. | Python · PyPI `blackdrome-noma` (MPL-2.0 weights and code) |
| [OneJev](onejev.md) | Run a multimodal System One decision model (text/image/video → calibrated option probabilities); independent of hosted Jev; distinct from Jev-Omni/PlayJev. | Python / PyTorch · HF weights + System One–shaped API (Apache-2.0) |
| [Open Alternative to Jev](open-alternative-jev.md) | Compare packed and separate typed decisions from open models and fit calibration on labeled data; not a Jev reproduction. | Python · Transformers/vLLM research library |
| [OpenDecider](opendecider.md) | Open System One choice/score/yes-no models with optional Jev-compatible `/v1/systemone` serve; independent of hosted Jev. | Python · HF weights + serve (Apache-2.0) |
| [OpenJev (alanhuangyoo)](alanhuangyoo-openjev.md) | Serve Jev-shaped typed decisions from open weights on your own GPU or laptop, including browser-step questions (which operation, which element). | Python · `wev-ai` (PyPI) · Hugging Face models (Apache-2.0) |
| [OpenJev-Cactus](siliconlabai-openjev-cactus.md) | Serve OpenAI-compatible chat + `/v1/systemone` typed decisions on CPU via cactus-needle (not TypeSafe-hosted). | Python · FastAPI edge server (MIT) |
| [OpenJev (ejhshen)](ejhshen-openjev.md) | Study OpenJev-4B open-vocabulary probabilistic decisions from Qwen3.5-4B; independent of hosted Jev; distinct from lookski/openjev. | Python · HF OpenJev-4B + training (MIT) |
| [openjev-rs](codesoda-openjev-rs.md) | Local typed decisions from pinned GGUF logits via Rust openjev-core/openjev-llama (not TypeSafe-hosted). | Rust · crates (MIT) |
| [openjev-server (abhishekgahlot2)](abhishekgahlot2-openjev-server.md) | Serve OpenJev-style choice/noul/score decisions from open models via vLLM or MLX (not TypeSafe-hosted). | Python · vLLM/MLX server (Apache-2.0) |
| [Open Medical Jev](open-medical-jev.md) | Run Jev-class medical yes/no judgments from frozen open models with dual-reader fusion, auto-release gates, and conformal sets; compare vs hosted Jev. | Python · GGUF readers + routing recipes (MIT) |
| [open-jev](open-jev.md) | Experiment with independent Kev and DeBERTa typed decisions locally in a browser; does not use official Jev weights. | TypeScript · npm library, Transformers.js / ONNX |
| [OpenJev](openjev.md) | Local Jev-compatible typed decisions via masked-logit softmax (not TypeSafe-hosted) | Python · local decision engine (MIT) |
| [openjev-sglang](openjev-sglang.md) | Inspect a Jev-shaped HTTP decision API using Qwen and SGLang; independent model behavior and unspecified code licensing. | Python / FastAPI / SGLang · inference research |
| [openjevx](muthuishere-openjevx.md) | Serve an open-weight Jev-compatible `/v1/systemone` endpoint locally for jevx (CPU/GPU; Apache-2.0 LICENSE in repo). | Go · local System One server + HF weights (Apache-2.0) |
| [PlayJev](playjev.md) | Study a 0.8B model that picks a game's next move from the frame alone, one forward pass, probability per listed move; independent of official Jev. | Python / PyTorch · model research and browser demo |
| [polyjev](polyjev.md) | Turn any LLM into typed calibrated Noul/Choice/Score/Span decisions; optional Jev-compatible `/v1/systemone` server. | Python · PyPI (`polyjev`) + serve (Apache-2.0) |
| [Privatemode Decisions benchmark](privatemode-decisions-benchmark.md) | Reproduce a vendor's System One comparison with identical states, options and instructions per arm, with cost forecasting and budget caps. | Python · benchmark suite (MIT) |
| [Reflex-1](matu79go-reflex-1.md) | Run/study Reflex-1, a 4B open decision model for fast typed classification with latent reasoning (independent of hosted Jev). | Python · open weights + examples (Apache-2.0) |
| [ReJev](rejev.md) | Reproduce a lightweight Jev-style Choice decision post-training loop on MiniCPM5-2B with sealed holdout metrics. | Python · LoRA post-training research (MIT) |
| [RSI-Jev](rsi-jev.md) | Train and serve Jev-style typed-decision checkpoints via a self-improving agent loop; independent of hosted Jev. | Python · research training + `/v1/systemone` serve (MIT code) |
| [ruling](ruling.md) | Serve typed, calibrated decisions from a local model on a Jev-compatible endpoint and compare it with Jev on public judgment sets. | Python · uv CLI/server (MIT) |
| [RYOTIDE](ryotide.md) | Local LLM one-forward-pass typed decisions (MLX/PyTorch) measured on JevBench; independent of official Jev. | Python · research (MIT) |
| [SelfJev](jwuthri-selfjev.md) | Run an open Jev-shaped decisions model (typed answers with probabilities) locally on one GPU; independent of hosted Jev. | Python · Qwen3.5-4B LoRA (Apache-2.0) |
| [SemIf](semif.md) | Explore typed option scoring and shared-state reuse with local open models; independent of official Jev. | Python / PyTorch / MLX · research and browser lab |
| [sokudan](hiroki-abe-58-sokudan.md) | Run a Japanese System One decision model (typed answers + probabilities, no generation) with bench_ja/bench_en and a Laya position-bias repro. | Python · HF weights (`GeneLab/sokudan-ja-310m`, Apache-2.0) |
| [StartLux-Decision](startlux-decision.md) | Self-host Jev-compatible decision models (GGUF/llama.cpp or vLLM) and reproduce the maintainer's Decision Index and game-harness comparisons against Jev 1.13. | Python · inference/eval code (Apache-2.0); weights on Hugging Face (CC BY-NC 4.0) |
| [Strands Decider](strands-decider.md) | Run Strands Decider open System One–style typed decisions for agent workflows (independent of hosted Jev). | Python · open decision model (Apache-2.0) |
| [Sureband](sureband.md) | Conformal coverage wrappers for System One outputs (Jev/Laya/…) from labeled calibration sets. | Python · library (`sureband`, Apache-2.0) |
| [System-1 decision benchmark](system1-decision-benchmark.md) | Compare Jev with other one-pass decision models and classic zero-shot baselines on one shared protocol, or reuse its HTTP runner for a typed-decision service. | Python · research repo (MIT) |
| [system-one-parsers](system-one-parsers.md) | Study how far closed System One questions get on dependency parsing, with offline checks and replayable recordings. | TypeScript (Bun) · research harness (MIT) |
| [system-one-security](system-one-security.md) | Rerun security experiments on TypeSafe Jev and Cloudflare Clef (truncation, injection, fact poisoning, tripwires). | TypeScript · experiment harness (MIT) |
| [TensorSharp](tensorsharp.md) | Run Jev-shaped typed decisions locally from C#/.NET (CUDA, Metal, or pure-C# CPU) with one structured read of DiffusionGemma, alongside ordinary chat endpoints on the same server. | C# / .NET · `TensorSharp.Server.Host` (BSD-3-Clause) |
| [TetraJev](tetrajev.md) | Run a zero-training local decision layer: four readings from two frozen readers, fit-free fusion, agreement routing, and published coverage–accuracy across eight decision suites plus a RAG reranking pass. | Python · runners + llama.cpp GGUF readers (MIT) |
| [tev1 (Together)](tev1.md) | Fine-tune/study tev1-4B Jev-inspired choice decisions (Together open weights + recipe; independent of hosted Jev). | Python · HF/Together weights + recipe (MIT) |
| [TinyJev](tinyjev.md) | Run an offline ~0.6B System One–compatible Choice/Noul/Score model (MLX/PyTorch); independent of hosted Jev. | Python · package + HF weights (MIT) |
| [typed-lm](typed-lm.md) | Serve Jev-style Choice/Noul/Score from dense LLMs in Rust (single forward pass; independent of hosted Jev). | Rust · Candle serve + training (Apache-2.0) |
| [Valen](valen.md) | Train/serve a multimodal System One–style decision model (text/image/video → probabilities); independent of hosted Jev. | Python · training/inference + HF weights (Apache-2.0) |
| [vev](vev.md) | Run open multimodal System One–style decisions (text+images) locally via `/v1/systemone`; not TypeSafe-hosted. | Python · HF open weights (Apache-2.0) |
| [vLLM Jev](vllm-jev.md) | Serve Jev-compatible decision models through vLLM. | Python · server (Apache-2.0) |
| [vLLM Jev (mode-io)](mode-io-vllm-jev.md) | Serve Jev-style Choice/Noul/Score checkpoints through vLLM (distinct from Egbertjing/vllm-jev). | Python · server (Apache-2.0) |
| [v1-decisions-vllm](v1-decisions-vllm.md) | Modular vLLM `/v1/decisions` typed API with `/v1/systemone` projection; pluggable backends. | Python · vLLM overlay (Apache-2.0); not hosted Jev |
| [vidjev](vidjev.md) | Typed decisions on video: CARLA drone follow + UCF-Crime anomaly detection with open VLMs. | Python · research + demos (MIT); not hosted Jev |
| [Wald-Q4B](wald-4b.md) | Self-host Wald-Q4B open-weight 4B decisions via Jev-compatible `/v1/systemone` (independent of hosted Jev). | Python · HF weights + serve scripts (Apache-2.0) |
| [WaterSheep](watersheep.md) | Run an Apache-2.0 decision model locally behind a Jev-compatible `/v1/systemone`: noul/choice/score plus multi-label answers with a probability per option (independent of hosted Jev). | Python · local server + HF weights + browser demo (Apache-2.0) |
| [WorkflowEvals](workflowevals.md) | Reproduce TypeSafe workflow evals (invoice/support/traces/security) against Jev and other providers. | Python · uv harness (Apache-2.0) · official TypeSafe |
| [XavierJev](xavierjev.md) | Local Jev-shaped yes/no/choice/rubric decisions from one-token logprobs with measured gates and a Claude Code permission hook (no hosted Jev calls). | TypeScript · local judge + Claude Code hook (MIT) |
| [zh-decision-bench](codyqin-zh-decision-bench.md) | Chinese-language calibration benchmark for Jev-class System One decision models (dataset CC BY 4.0; code… | Python · HF dataset + eval (Apache-2.0 code; dataset CC BY 4.0) |

## SDKs and integrations

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [adk-go-typesafe](adk-go-typesafe.md) | Call System One from Go and Google ADK-Go with OpenAPI-generated types (Choice/Score/Noul). | Go · module + ADK tool (`adk-go-typesafe`) |
| [Advocaat](advocaat.md) | Batch typed Jev choice, score, and yes/no questions about structured data from TypeScript. | TypeScript · client library and agent skill |
| [anofox-decide](anofox-decide.md) | Evaluate NL predicates/choices in DuckDB SQL via TypeSafe Jev or local open decision models (remote opt-in). | C++ · DuckDB extension (MIT) |
| [ask-jev (Aether-254)](aether-254-ask-jev.md) | MCP + Codex/Claude plugin for TypeSafe Jev evaluate/batch/ping (Choice/Score/Noul). | TypeScript · MCP/plugin (MIT) |
| [askif](askif.md) | Write readable if/switch/score control flow over Jev probabilities, with thresholds, unsure bands and offline tests. | TypeScript · npm `askif` + `@askif/jev` (MIT) |
| [Backdrop AI Provider TypeSafe AI](backdrop-ai-provider-typesafeai.md) | Backdrop CMS AI module provider for TypeSafe System One decisions and moderation checks. | PHP · Backdrop module (GPL-2.0) |
| [Camunda Jev AI Decision Connector](camunda-jev-ai-decision-connector.md) | Call TypeSafe Jev noul/choice/score from Camunda 8 BPMN for typed AI decisions over lists. | Java · Camunda 8 connector (Apache-2.0) |
| [Cite](cite.md) | Declare concerns with `detect` questions and yes/no descriptions, then `Cite.judge/3` a source of passages (log lines, caption chunks, conversation turns) to get the matching passages. | Elixir · Hex package `cite` (Req + Spark) (MIT) |
| [cog-typesafe](cog-typesafe.md) | Bind TypeSafe Jev as a versioned `system-one/decisions` provider Cog for decision Cogs. | Python · pixi Cog provider (Apache-2.0) |
| [datafusion-jev](datafusion-jev.md) | DataFusion SQL `prompt_jev` UDF for typed TypeSafe Jev answers over row text (bring HTTP client). | Rust · DataFusion 55 crate (MIT OR Apache-2.0) |
| [Dataiku TypeSafe AI plugin](dataiku-typesafe-plugin.md) | Use Jev typed decisions inside Dataiku agents, guardrails, RAG reranking and recipes with LLM Mesh governance. | Python · Dataiku DSS plugin (Apache-2.0) |
| [decide (vsekhar)](vsekhar-decide.md) | Ask TypeSafe Jev yes/no, choice, and scored decisions from the command line, scripts, and agent skills. | Go · brew CLI (Apache-2.0) |
| [Decision Model Rust SDK](decision-model-sdk-rust.md) | Call `/v1/systemone` from Rust with compile-time question sets and typed answers; no default vendor URL, so keys go only where you point them. | Rust · crates `decision-model-sdk`, `-macros`, `decision-model-adapter` (Apache-2.0) |
| [DecisionKit](decisionkit.md) | Model Jev decisions in .NET domain terms and keep the Jev protocol in a separate provider package (Choice/Score/Noul). | C# · NuGet packages (DecisionKit.* 0.1.0, MIT) |
| [ex_typesafe_ai](iamtalha-arshad-ex-typesafe-ai.md) | Call TypeSafe AI Jev from Elixir with typed structs and noul/choice/score helpers (unofficial). | Elixir · library (MIT) |
| [feelings](feelings.md) | Add typed `.feels()` / `.how()` / `.matches<T>()` methods on any BAML value using TypeSafe Jev (license unspecified). | BAML · library (`baml_src/vibes.baml`) |
| [Gavel](gavel.md) | Call TypeSafe Jev Choice/Score/Noul from Salesforce Flow/Apex/Agentforce with policy + ledger. | Salesforce · Apex/Flow packages (Apache-2.0) |
| [genai (maruel)](maruel-genai.md) | Use one Go API for chat, tools, streaming and typed decisions; switch the decision provider between hosted Jev and local or Cloudflare models without changing your question code. | Go · library (Apache-2.0) |
| [go-jev](go-jev.md) | Call TypeSafe Jev from Go (Ask/Evaluate) and UNIX pipelines via jev-cli; explicit API key option. | Go · module + CLI (`github.com/mattn/go-jev`, MIT) |
| [GoEventBus](goeventbus.md) | Route ambiguous events with rules → cache → Jev fallback, then dispatch inside the bus (local ring buffer, Redis Streams, or RabbitMQ). | Go · library (`go get github.com/Protocol-Lattice/GoEventBus`) (MIT) |
| [Gut](gut.md) | Pick an atom/value for a subject and question in Elixir (for example route a ticket to `:billing`) using Jev as the evaluator. | Elixir · Hex package `gut` + `req_llm` (Apache-2.0) |
| [hono-jev-router](hono-jev-router.md) | Route Hono HTTP requests by plain-English meaning with TypeSafe Jev Noul judgments (experimental). | TypeScript · Hono router (`hono-jev-router`) |
| [hunch](hunch.md) | Call TypeSafe Jev classify/score/check/pick/rank/where over scalars, lists, and pandas columns (`hunch-jev`). | Python · PyPI library (`hunch-jev` 0.6.0) |
| [JarvisCore](jarviscore.md) | Give every agent bounded Choice/Score/Noul judgments via `self.decisions.evaluate(...)`, and opt in to Jev-backed subagent selection (`KERNEL_ROUTER_PROVIDER=typesafe`) or RAG passage classification. | Python · PyPI `jarviscore-framework[typesafe]` (Apache-2.0) |
| [jear](jear.md) | Route NEAR AI Cloud / IronClaw choices by budget, quality, and sensitivity using TypeSafe Jev structured decisions. | Rust · CLI/library (`jear` 0.1.0) |
| [jeff (Viperwow)](viperwow-jeff.md) | Put one typed-decision API in your stack and switch between hosted Jev and local Jev-compatible models by provider/model name. | Rust · single binary (release archives; `cargo`) |
| [Jev for Excel](jev-excel.md) | Classify, score or fact-check a column of text with a fill-down formula instead of code. | JavaScript Office add-in + VBA module (MIT) |
| [Jev Moderation](jev-moderation.md) | Moderate user text with portable JSON policies where every rule is a separate Jev yes/no question, and test policy changes against labelled cases before shipping. | TypeScript + Python · shared policy schemas (MIT) |
| [jevai](jevai.md) | Call TypeSafe System One from Rust with typed noul/choice/score questions in parallel (unofficial). | Rust · async client crate (MIT) |
| [jev-cli (shetautnetjer)](shetautnetjer-jev-cli.md) | Clean-room `jev` CLI for Decision Contracts, local search, and benchmarks against TypeSafe System One. | Python · CLI (MIT) |
| [jev (drpaneas)](drpaneas-jev.md) | Call TypeSafe Jev System One from Go with a small client package. | Go · module (`github.com/drpaneas/jev`, MIT) |
| [jev (okooo5km)](okooo5km-jev.md) | Stdlib Python CLI + Agent Skill for TypeSafe Jev yes/pick/score via TypeSafe API or OpenRouter (distinct from typesafe-cli / typesafeai-cli). | Python · CLI 0.3.2 + skill |
| [jev-dotnet (CMaintz)](cmaintz-jev-dotnet.md) | Unofficial zero-dep .NET Jev client (Choice/Score/Noul); distinct from ukashanoor/jev-dotnet. | C# · .NET client (MIT) |
| [jev-php (f-lombardo)](f-lombardo-jev-php.md) | Call TypeSafe Jev System One APIs from PHP applications. | PHP · library (LGPL-2.1) |
| [jev (polidog)](polidog-jev.md) | Pipe state on stdin and run jev noul/choice/score against TypeSafe, Cloudflare Workers AI, or Vercel AI Gateway. | Rust · CLI (`cargo install --git`) |
| [jev (stefafafan)](stefafafan-jev.md) | Unix/Go CLI for typed TypeSafe Jev questions across TypeSafe, Cloudflare, and Vercel providers. | Go · CLI (`go install`, MIT) |
| [JEV ADK](jev-adk.md) | Build System One agent pipelines with TypeSafe Jev primitives: bash guardrails, dual-brain routing, PR triage blueprints. | Python · ADK / examples (MIT) |
| [Jev Classification for n8n](jev-classification-n8n.md) | Route workflow items with typed Jev decisions, configurable review handling, and multi-item batching. | TypeScript · self-hosted n8n community node |
| [Jev for Splunk](jev-for-splunk.md) | Ask TypeSafe Jev typed questions about Splunk events (the `jev` search command) and cache answers in the KV store. | Python · Splunk app (`jev_for_splunk`, Apache-2.0 file) |
| [Jev MCP (Freepik)](freepik-jev-mcp.md) | Go MCP server for typed decide/classify/verify/rerank via OpenRouter or TypeSafe (binary/container). | Go · MCP binary (`jev-mcp` v0.3.0) |
| [Jev MCP Server (keysersoft)](keysersoft-jev-mcp-server.md) | Install a remote/self-hosted AnythingMCP Jev connector (yes/no, classify, score + probabilities) for Claude/ChatGPT MCP hosts. | JavaScript · AnythingMCP connector (AGPL-3.0) |
| [Jev Studio](jev-studio.md) | Experiment with TypeSafe Jev via a `jev` CLI (verify/screen/classify/…) and an MCP server with cookbook tools. | Python · CLI + MCP (`jev-studio` 0.1.0 Alpha) |
| [Jev Symfony Bundle](jev-symfony-bundle.md) | Wire TypeSafe Jev into Symfony via typed client, validator attributes, Messenger, Workflow guards, and profiler. | PHP · Symfony bundle (Apache-2.0) |
| [jev-agent-tools](jkudish-jev-agent-tools.md) | Share a fail-closed multi-provider Jev transport used by jev-browser and jev-mcp. | JavaScript · library (MIT) |
| [jev-broker](alekseiul-jev-broker.md) | Local HTTP MCP broker for Hermes agents: validate questions, call TypeSafe Jev via OpenRouter, return structured… | Go · HTTP MCP tool (MIT) |
| [jev-cli (shaharia-lab)](shaharia-lab-jev-cli.md) | Rust `jev` CLI + MCP: typed TypeSafe Jev questions with shell exit codes and JSON (distinct from tumf). | Rust · crates.io CLI/MCP (Apache-2.0 OR MIT) |
| [jev-cli (tumf)](tumf-jev-cli.md) | Ask TypeSafe Jev noul/choice/score from a PyPI CLI plus bundled stdio MCP (`jev` / `jev-mcp`). | Python · PyPI CLI/MCP (`jev-cli` 0.6.2) |
| [jev-code-mode](jev-code-mode.md) | Expose typed Jev judgments as two MCP tools (`search` and `execute`) for agent cheap-checks before heavier work. | TypeScript · MCP server (MIT) |
| [jev-feels](jev-feels.md) | Use TypeSafe Jev as Ruby `feels?` / `decide` / `score` and Rails validations (distinct from BAML feelings). | Ruby · gem (`jev-feels` 1.1.0) |
| [jev-foundation-models](jev-foundation-models.md) | Use TypeSafe Jev as an Apple Foundation Models `LanguageModel` for `@Generable` Bool/enum/score fields. | Swift 6 · SwiftPM (`JevFoundationModels` 0.1.0, Apache-2.0) |
| [jev-java](jev-java.md) | Call TypeSafe Jev (or OpenRouter/Vercel adapters) from Java 17+ with typed Choice/Noul/Score and optional Spring. | Java · Maven (`jev-typesafe` 0.1.1) |
| [jev-mcp](jev-mcp.md) | Give agents ten purpose-built TypeSafe Jev judgment MCP tools (verify, screen, find, classify, review, gate, …). | TypeScript · npm MCP server (`@jkudish/jev-mcp`) |
| [jev-mcp (Afloat16)](afloat16-jev-mcp.md) | Unofficial conservative MCP server for TypeSafe AI Jev (stdio) so agents can ask typed System One questions. | Node.js · MCP server (MIT) |
| [jev-mcp-server](jev-mcp-server.md) | MCP for official TypeSafe Jev choice/score/noul plus compare/verify/batch classify and client installer. | Python · PyPI MCP (`jev-mcp-server` 0.2.3) |
| [jev-prompt-sentry](jev-prompt-sentry.md) | Reverse-proxy Anthropic Messages through one batched TypeSafe Jev jailbreak/injection/exfil screen (PolyForm Noncommercial). | Python · FastAPI proxy |
| [jev-recipes](jev-recipes.md) | 66 TypeScript recipes for TypeSafe Jev decisions (rerank/verify/clarify/route/…) via `@typesafe-ai/sdk`. | TypeScript · npm (`jev-recipes` 0.2.0) |
| [jev-sdk-java](jev-sdk-java.md) | Call System One from Java 21 with sealed Question/Answer records (TypeSafe-only; source-build until Central lists 0.1.0). | Java 21 · Maven (`com.luigivismara:jev-sdk-java`) |
| [jev.zig](jakeknowlton-jev-zig.md) | Call TypeSafe System One from Zig with compile-time typed noul/choice/score questions. | Zig 0.16 · library via build.zig.zon (MIT) |
| [jev2mcp](jev2mcp.md) | Local companion + Chrome extension: TypeSafe Jev selects ChatGPT MCP/plugin/tool mentions from your catalog. | Node.js · local server + extension (`jev2mcp` 0.2.1) |
| [jev4j](jev4j.md) | Call TypeSafe/OpenRouter Jev from Java (noul/choice/score, multi-question, Spring starter). | Java · Maven (`jev4j-core` 0.1.0, MIT) |
| [jev4k](jev4k.md) | Declare TypeSafe Jev Noul/Choice/Score questions in a Kotlin DSL and read typed answers. | Kotlin · Maven (`com.pambrose:jev4k` 0.1.0) |
| [JevApi](jevapi.md) | .NET 10 TypeSafe.Client + MCP server for typed noul/choice/score evaluate/batch. | C# · .NET library + MCP (MIT) |
| [JevClient.jl](jevclient-jl.md) | Call System One from Julia with Noul/Choice/Score sets and endpoint policy locks to api.typesafe.ai. | Julia · package (`JevClient` 0.1.0) |
| [jevframe](jevframe.md) | Classify/score pandas and Polars rows with TypeSafe Jev via a `.jev` accessor and full probability columns. | Python · PyPI (`jevframe` 0.1.0; pandas/polars extras) |
| [jevgo](jevgo.md) | Call TypeSafe System One from Go with typed Noul/Choice/Score (unofficial stdlib client). | Go · module (`github.com/devbackend/jevgo`) |
| [Jevlin](copyleftdev-jevlin.md) | Call TypeSafe Jev from Zig with typed Choice/Score/Noul helpers, owned buffers, and offline checks. | Zig 0.16 · library (`jevlin`, MIT) |
| [jevmcp (eaisdevelopment)](eaisdevelopment-jevmcp.md) | One Agent Plugins install: TypeSafe Jev MCP tools for spec-drift, CI triage, and code-audit screening. | Python · Agent Plugins + MCP (Apache-2.0) |
| [jevonian](jevonian.md) | Local OpenAI/Anthropic/Responses proxy: one Jev call picks the model and the thinking level after code has filtered candidates; pinned models skip Jev. | Node.js ≥ 22 · CLI and local server (`jevonian` 0.0.1, AGPL-3.0-only) |
| [jevper](jevper.md) | Jev-shaped System One noul/choice/score over any OpenAI-compatible client (no hosted TypeSafe API). | Python · PyPI (`jevper` 0.1.2, Apache-2.0) |
| [Jevs](jevs.md) | Call TypeSafe Jev classify/score/check/batch from Bun MCP / Codex plugin via the official JS SDK. | TypeScript · Bun MCP / Codex plugin (`jevs` 0.1.0) |
| [JevT++](jevtpp.md) | C++20 typed decision library with optional local Laya (ONNX/ggml) or remote System One backends. | C++20 · library (MIT) |
| [jevtok-ts](jevtok-ts.md) | Offline Jev token counting and request accounting for Node.js/TypeScript (companion to Python jevtok). | TypeScript · library (MIT) |
| [judge_rails](judge-rails.md) | Declare `judge_attribute :urgency, Judge.noul(...)` on a model and query judged records with scopes; three judgments cost one API call per record. | Ruby · gem `judge_rails` (Rails generators; plain-Ruby client) (MIT) |
| [judgment (Rust)](judgment.md) | Write Jev decisions in Rust with typed options and thresholds, and unit-test them offline against answers the real model could give. | Rust · crates.io `judgment` (MIT) |
| [Kestra TypeSafe plugin](kestra-plugin-typesafe.md) | Run TypeSafe System One typed evaluations inside Kestra flows (branch on structured answers). Not Scala Typesafe. | Java · Kestra plugin (Apache-2.0) |
| [Klassify](klassify.md) | Kotlin Multiplatform DSL/SDK and Native CLI/MCP for TypeSafe System One classification (distinct from jev4k). | Kotlin · KMP SDK + Native CLI (`klassify` v0.1.1, Apache-2.0) |
| [kotlin-jev](kotlin-jev.md) | Kotlin SDK + CLI for TypeSafe Jev (port of mattn/go-jev patterns). | Kotlin/JVM · library + `jev-cli` (MIT) |
| [langgraph-jev](langgraph-jev.md) | Call TypeSafe Jev typed decisions from LangGraph/LangChain graphs (distinct from JevLangGraph). | Python · LangGraph/LangChain (MIT) |
| [Laravel AI](laravel-ai.md) | Add typed classification through Laravel’s TypeSafe provider. | PHP · Laravel package |
| [laya-php](laya-php.md) | Classify/route text in PHP with local Laya typed decisions (Choice/Score/Noul); Laravel-ready; independent of hosted Jev. | PHP · Composer (`marcreichel/laya-php`, Apache-2.0) |
| [llm-typesafe](llm-typesafe.md) | Call TypeSafe Jev noul/choice/score from the LLM CLI (`typesafe/jev-latest` / `jev`). | Python · LLM plugin (`llm-typesafe` 0.1a0) |
| [MakerAi](makerai.md) | Call Jev from Delphi with typed Choice/Score/Noul questions, or drop in adapters such as `TAiJevRouterTool`, `TAiJevGuardrailClassifier`, `TAiJevPromptGuard`, `TAiJevRAGReranker` and `TAiJevBatchLabeler`. | Delphi (Object Pascal) · component packages, Delphi 10.4–13.1 (MIT) |
| [Mechanical Jev](mechanical-jev.md) | Ask System One Noul/Choice/Score from Rust (`mjev`) against local Intel Phi Jev or compatible endpoints. | Rust · library/CLI (Apache-2.0) |
| [Micdrop](micdrop.md) | Build real-time TypeScript voice agents; optional `@micdrop/typesafe` classifies each user turn with TypeSafe Jev (choice/score/noul) before the LLM answers. | TypeScript · voice SDK + `@micdrop/typesafe` 1.0.1 (MIT) |
| [Moreno.Jev](morenoland-moreno-jev.md) | Cross-platform MCP server and agent skill for TypeSafe Jev structured code review and debugging (review_code /… | Python · MCP server + skill (MIT) |
| [Mule 4 TypeSafe Connector](mule4-typesafe-connector.md) | Drive Mule 4 flows with TypeSafe Jev typed noul/choice/score decisions (connector ops + DataSense). | Java · Mule 4 connector (Apache-2.0) |
| [n8n-nodes-jev](n8n-nodes-jev.md) | Classify, route, and score n8n workflow items with TypeSafe Jev questions. | TypeScript · n8n community node `n8n-nodes-jev` (MIT) |
| [n8n-nodes-system-one](n8n-nodes-system-one.md) | Add one decision node to an n8n workflow, pick a credential (which picks the provider), and route items on `is_urgent_yes`, `team`, confidences and probabilities. | TypeScript · npm `@diegohh0411/n8n-nodes-system-one` (MIT) |
| [n8n-nodes-typesafe](n8n-nodes-typesafe.md) | Ask TypeSafe Jev noul/choice/score questions about workflow text or JSON inside n8n. | TypeScript · n8n community node |
| [n8n-nodes-typesafe-ai](n8n-nodes-typesafe-ai.md) | Official TypeSafe n8n nodes: Evaluate answers or Route items with System One (Jev) noul/choice/score questions. | TypeScript · n8n community node `@typesafe-ai/n8n-nodes-typesafe-ai` (MIT) |
| [naturalcodz](naturalcodz.md) | Natural-logic npm helpers (classify/guard/route/score) on TypeSafe Jev with confidence thresholds. | TypeScript · npm (`naturalcodz`, MIT) |
| [NeuroLink](neurolink.md) | Call generate/stream across many providers and use TypeSafe Jev `decide` for typed boolean/choice/score judgments. | TypeScript · SDK/CLI (`@juspay/neurolink`) |
| [nf-jev](nf-jev.md) | Call TypeSafe Jev noul/choice/score from Nextflow pipelines and gate on returned probabilities. | Groovy · Nextflow plugin (`nf-jev` 0.1.0, Apache-2.0) |
| [nifi-jev](nifi-jev.md) | Apache NiFi `RouteWithJev` processor: TypeSafe Jev semantic yes/no routing with yes/no/review/failure relations. | Java · NiFi NAR (MIT) |
| [Octolib](octolib.md) | Call Jev from Rust with `EvaluationRequest` + `Question::noul/choice/score` and branch on calibrated probabilities, alongside every other provider in the same crate. | Rust · crate `octolib` on crates.io (Apache-2.0) |
| [Photoshop MCP](photoshop-mcp.md) | Control Photoshop from Cursor, Claude or the bundled chat UI; with a TypeSafe key, Jev routes each prompt to Instant (known safe command), Plan, Look & iterate, or Ask first. | TypeScript · npm `@alisaitteke/photoshop-mcp` (MCP server + browser chat UI) (MIT) |
| [pi-jev-extension (rioliu)](rioliu-pi-jev-extension.md) | Pi extension: `jev_decide` asks TypeSafe Jev choice/score/noul; falls back to the session model if Jev is unavailable. | TypeScript · Pi extension (Bun, MIT) |
| [Prompt Rejector](prompt-rejector.md) | Screen prompts, skills, and MCP tool descriptions via HTTPS/MCP with TypeSafe Jev plus deterministic checks. | TypeScript · npm (`prompt-rejector` 1.2.0, ISC) |
| [protoc-gen-jev](protoc-gen-jev.md) | Define decisions once in Protobuf (`bool` → noul with threshold, `enum` → choice, `int32` levels → score) and generate typed Jev service clients with confidence and probability metadata. | Go · protoc plugin + runtime packages; BSR module `buf.build/bufbuild-experimental/protoc-gen-jev` (MIT) |
| [ruby_decision_model](ruby-decision-model.md) | Ask Noul, Choice, and Score questions from Ruby via Typesafe or OpenRouter. | Ruby · gem (stdlib HTTP) |
| [ruby_llm-typesafe](ruby-llm-typesafe.md) | Call TypeSafe Jev Choice/Noul/Score from RubyLLM 2 apps via a `:typesafe` provider. | Ruby · gem (`ruby_llm-typesafe`, MIT) |
| [s1 (s1-rs)](s1-rs.md) | Derive Choice/Score/Noul question sets in Rust; optional `typesafe-rs` backend (distinct from typesafe-api). | Rust · workspace crates (`s1` 0.1.0, MSRV 1.85) |
| [scala-jev-sdk](scala-jev-sdk.md) | Call System One from Scala 3.3 LTS with typed Question/answer lookup over an sttp 4 backend (Maven Central). | Scala 3 · Maven (`io.github.ticofab:scala-jev-sdk_3` 0.1.0, Apache-2.0) |
| [semgate](semgate.md) | Filter and route Go HTTP requests with TypeSafe Jev noul/choice/score middlewares. | Go · net/http middleware |
| [Skill Router (LangChain)](langchain-skill-router.md) | Load only the relevant skills per user turn from large catalogs (rank, then verify) with tunable load/offer/skip thresholds and per-decision traces. | Python · PyPI `langchain-skill-router[jev]` (MIT) |
| [Spring AI TypeSafe](spring-ai-typesafe.md) | Call System One from Java/Spring AI (client, JevJudge, guardrail/RAG/tool-search advisors). | Java · Maven (`org.springaicommunity`, 0.1.0) |
| [standard_model_for_jev_tasks (jev-shim)](standard-model-for-jev-tasks.md) | Point existing Jev clients at a model you serve yourself, for offline development, comparison or self-hosting. | Python (stdlib) · `jev-shim` server (Apache-2.0) |
| [strapi-plugin-jev-review](strapi-plugin-jev-review.md) | Gate Strapi 5 publish with TypeSafe Jev approve/escalate/revise decisions (optional Document Service guard). | JavaScript · Strapi 5 plugin (MIT) |
| [swift-jev](swift-jev.md) | Call TypeSafe Jev Choice/Noul/Score from SwiftPM apps or a JSON CLI (`jev`); no free-form generation. Distinct from TypeSafe (Swift). | Swift 6.2 · SwiftPM library (`Jev`) + CLI |
| [sys1 (alvarobartt)](alvarobartt-sys1.md) | Serve open decision models (e.g. Laya) behind a System One–compatible `/v1/systemone` API in Rust. Distinct from hraness/sys1. | Rust · CLI/server (Apache-2.0) |
| [System One Connector](system-one-connector.md) | MCP `evaluate` tool: typed Jev/Laya/System One judgments with probabilities for supported coding agents. | Go · static binary + MCP setup (MIT) |
| [system-one (asynq-io)](asynq-io-system-one.md) | Vendor-neutral Python SDK for typed System One yes/no/choice/score (hosted or local ONNX). | Python · PyPI (`system-one`, Apache-2.0) |
| [systemone (justintout)](systemone-justintout.md) | Unofficial Go System One/Jev client with compile-time typed questions (distinct from TypeSafe Go). | Go · module (`github.com/justintout/systemone`, MIT) |
| [taurus-jev-sdk-go](taurus-jev-sdk-go.md) | Hard-failing stdlib Go System One client (unofficial). | Go · library (MIT) |
| [TypeSafe Jev custom connector](jev-custom-connector.md) | Call TypeSafe Jev from Power Automate/Copilot Studio with typed dynamic-content answers. | Power Platform · managed custom connector (MIT) |
| [typesafe-go (zhirschtritt)](zhirschtritt-typesafe-go.md) | Call TypeSafe System One from Go with an idiomatic unofficial SDK (≠ stacklok/typesafe-go). | Go · module (`github.com/zhirschtritt/typesafe-go`, MIT) |
| [TypeSafe (Swift)](typesafe-swift.md) | Call System One Noul/Choice/Score from SwiftPM apps and servers. | Swift · SwiftPM library (`TypeSafe`) |
| [TypeSafe AI for Agent Zero](a0-typesafe-ai.md) | Ask TypeSafe Jev Choice/Noul/Score from Agent Zero chat with probability cards; bundles the official agent skill. | Python · Agent Zero plugin (`typesafe_ai` 1.0.0) |
| [TypeSafe C++ SDK](typesafe-sdk-cpp.md) | Call TypeSafe System One (Choice/Score/Noul) from C++20 with a builder-configured client. | C++20 · library (MIT) |
| [TypeSafe Go](typesafe-go.md) | Call System One from Go with explicit auth options and no implicit env reads (Stacklok; unofficial). | Go · module (`github.com/stacklok/typesafe-go`) |
| [TypeSafe MCP](typesafe-mcp.md) | Give agents a general-purpose Jev evaluation tool with raw provider responses. | Go · MCP server and pi extension |
| [typesafe-api (Rust)](typesafe-api-rs.md) | Call System One from Rust with typed questions/answers (`typesafe-api` 0.1.0, MSRV 1.88). | Rust · crates.io client |
| [TypeSafe-as-a-Judge](typesafe-as-a-judge.md) | Give Codex/Claude Code bounded TypeSafe Jev route/rank/extract/verify/judge MCP tools (unofficial). | Node.js · MCP plugin + skills (`0.1.0`) |
| [typesafe-cli](typesafe-cli.md) | Ask Jev noul/choice/score questions from the shell (`jev`); answers are numbers, not prose. | TypeScript · npm CLI / Nix |
| [typesafe-client (haileyok)](haileyok-typesafe-client.md) | Call TypeSafe System One (Noul/Choice/Score) from Go (stdlib) or Rust (async reqwest) with typed errors and retry policy matching the official SDKs. | Go 1.22+ · Rust 1.88+ (`typesafe-system-one` crate) |
| [typesafe-sdk-csharp (tylerwarner33)](tylerwarner33-typesafe-sdk-csharp.md) | Unofficial C# TypeSafe API client (≠ listed TypeSafe.AI NuGet / CMaintz jev-dotnet). | C# · .NET client (MIT) |
| [typesafe-sdk-go (jmelahman)](typesafe-sdk-go-jmelahman.md) | Stdlib-only Go client for TypeSafe System One (Noul/Choice/Score helpers). | Go · module (`github.com/jmelahman/typesafe-sdk-go`, MIT) |
| [typesafe-sdk-rust (zchee)](zchee-typesafe-sdk-rust.md) | Async Rust client for TypeSafe System One with derive(QuestionSet) macros (unofficial port of the Python SDK). | Rust · crates.io `typesafe-sdk-rust` (Apache-2.0) |
| [TypeSafe.AI (.NET SDK)](typesafe-sdk-csharp.md) | Call System One from .NET with DI, resilience, and OTel (NuGet TypeSafe.AI; distinct from TypeSafeAI.Net). | C# · NuGet client (`TypeSafe.AI` v1.0.0) |
| [typesafeai-cli](typesafeai-cli.md) | Run TypeSafe Jev ask/decide/screen/verify flows from a Python `typesafe` CLI for humans or agents. | Python · CLI (`typesafe`) |
| [TypeSafeAI.Net](typesafeai-net.md) | Add typed Jev judgments to .NET applications and Microsoft.Extensions.AI pipelines. | C# · client library |
| [TypeSafeSharp (.NET)](typesafesharp.md) | Call Jev from C#/.NET services, including .NET Framework 4.7.2+, with DI and tracing. | C# · NuGet `TypeSafeSharp` (MIT) |
| [typia (`@typia/jev`)](typia-jev.md) | Keep Jev question schemas and answer validation in one TypeScript type instead of hand-written JSON. | TypeScript · npm `typia` + `@typia/jev` (MIT) |
| [wagtail-jev](wagtail-jev.md) | Wagtail CMS editor buttons: TypeSafe Jev suggests page tags and rates fields on custom scales. | Python · Wagtail/Django package (MIT) |
| [Wingman](wingman.md) | Route System One requests through one gateway: a `typesafe` provider preserves Jev probabilities, confidence, model, and usage. | Go · server + YAML config (MIT) |
| [yoagent](yoagent.md) | Build Rust agents and add Jev typed decisions: advisory skill/tool hints, a fail-closed destructive-call gate, and a prompt-injection input guard. | Rust · crate `yoagent` (feature `decision`) (MIT) |
| [zenai](zenai.md) | Call TypeSafe Jev from Zig with typed `Questions` and answers (`zenai.typesafe.Client`). | Zig · library (Apache-2.0) |
| [ZeroAlloc.Jev](zeroalloc-jev.md) | Call TypeSafe Jev System One from .NET with a source-generated, Native AOT–friendly unofficial client. | .NET · library (MIT) |

## Search and retrieval

| Project | What you can do | Stack / format |
| --- | --- | --- |
| [Agent Seek](agent-seek.md) | Cheap web recall for agents: You.com discover + TypeSafe Jev cascade ranking (REST/MCP/UI). Does not write answers. | Python 3.12+ · FastAPI/MCP (`agentseek.dev` demo) |
| [arxiv-relevance-watch](arxiv-relevance-watch.md) | Get a deterministic, explainable nightly shortlist of arXiv papers for a narrow topic you define in three JSON files. | JavaScript (Node) · CLI (MIT) |
| [blink](blink.md) | Search a local codebase with TypeSafe Jev via ensemble directory walkers that Choice-pick the next file or folder. | Bun · CLI (`./blink`); license unspecified |
| [Brave Jev MCP](brave-jev-mcp.md) | Keep agent context for passages that help answer the query; other Brave tools pass through unfiltered. | TypeScript · MCP server, npm `@romantcig/brave-jev-mcp` (MIT) |
| [dailypaper-skills](dailypaper-skills.md) | Install seven skills into Claude Code, Codex, Cursor, Copilot, Gemini CLI, OpenCode or OpenClaw; Jev scores each candidate paper's title/abstract for relevance, the host agent reviews and writes notes. | Python 3.10+ · agent skills + installer (Apache-2.0) |
| [Deep Recall](deep-recall.md) | Index Markdown notes into one SQLite file, then let `backend = "jev"` rerank hybrid-search windows by P(states the answer), widen when unsure, and optionally classify question kinds. | Python · Claude Code plugin, MCP server and `deeprecall` CLI (MIT) |
| [duckdb-jev](duckdb-jev.md) | Run TypeSafe Jev Noul/Choice/Score predicates natively inside DuckDB SQL (C++ extension; no Python UDF). | C++ · DuckDB extension (Apache-2.0) |
| [FastGate](fastgate-jev.md) | Gate a multilingual EN/UZ/RU RAG helpdesk with TypeSafe Jev decisions before the LLM writes; includes an independent benchmark. | Python · RAG helpdesk + benchmark (MIT) |
| [gbrain-evals](gbrain-evals.md) | Reproduce gbrain retrieval/memory benchmarks and read (or replay) a Jev slot study: wins on dream triage and contradiction proposals, regressions on reranking, evidence trimming and abstention. | TypeScript/Bun · benchmark harness, datasets and reports (MIT) |
| [genigrep](genigrep.md) | Retrieve answering source for a codebase question; TypeSafe Jev ranks/filters candidates. | TypeScript · search tool (Apache-2.0) |
| [graphify-jev](54lynnn-graphify-jev.md) | Build a local AST knowledge graph and use Jev System One judgments for semantic navigation/refactor guidance without a vector store. | Python 3.10+ · Tree-sitter + Jev |
| [jegrep](jegrep.md) | Find code by natural-language intent using TypeSafe Jev (or OpenRouter→Jev) without embeddings. | Rust · CLI (`jegrep`) and release binaries |
| [Jev Deep Research](jevdeepresearch.md) | Parallel evidence finding: GPT drives research steps; TypeSafe Jev judges document regions concurrently and returns excerpts. | TypeScript/Python research harness (Apache-2.0) |
| [Jev Graph Search](jev-graph-search.md) | Ask an agent-memory question over Markdown notes and get source passages ranked by Jev; also audits links and suggests where a new note belongs. | JavaScript · npm `jev-graph-search` + agent skill (MIT) |
| [JEV Research MCP](jev-research-mcp.md) | Select web research evidence with TypeSafe Jev at search-result and content-block layers (MCP `research`). | TypeScript · MCP server (Apache-2.0) |
| [Jev Second Brain](jev-second-brain.md) | Index a Markdown/Obsidian vault and optionally judge note relationships with TypeSafe Jev (Gateway). | Python · CLI (`secondbrain`) |
| [jev-corrective-rag](jev-corrective-rag.md) | Corrective RAG with TypeSafe Jev typed gates for triage, chunk grading, and answer verification (LLM only generates). | Python · Streamlit app, CLI and bench |
| [jev-doc-search](jev-doc-search.md) | Find answering pages in long PDFs with TypeSafe Jev `Choice` over a PageIndex tree (no vector DB). | Python · PageIndex + typesafe_sdk (Apache-2.0) |
| [jev-rag](jev-rag.md) | Index local files with SQLite BM25, rerank evidence with TypeSafe Jev, optionally stream grounded answers. | Python · local RAG CLI/UI (MIT) |
| [jev-rag-gate](jev-rag-gate.md) | Gate RAG retrieval candidates with TypeSafe Jev for relevance, premise contradiction, and prompt-injection risk. | Python · library/CLI (MIT) |
| [jev-rerank-bench](jev-rerank-bench.md) | Reproduce TypeSafe Jev vs Cohere/zerank reranker experiments on shared BM25 candidate sets. | Python · benchmark suite (MIT) |
| [jev-reranker](jev-reranker.md) | Rerank, filter, or compress JSON search candidates with TypeSafe Jev via a stdin/stdout Rust CLI. | Rust · npm CLI (`jev-reranker` 0.1.1) |
| [jev-reranker (hotchpotch)](hotchpotch-jev-reranker.md) | Score/filter RAG candidates with TypeSafe Jev in Python (listwise/pointwise/pairwise; PyPI). Distinct from the Rust CLI. | Python · library (`jev-reranker` 0.1.2) |
| [jev-search (AnthonyDavidAdams)](anthonydavidadams-jev-search.md) | Decision-only agentic search: fetch/parse locally; score/rank candidates with Jev or local Laya. | Python · library/CLI + skill (MIT) |
| [jev-tool-search](jev-tool-search.md) | Compare BM25, embeddings, rerankers, and TypeSafe Jev for picking among hundreds of MCP tools; includes an experimental Jev search engine. | Python · benchmark + experimental search (MIT) |
| [jev4pg](jev4pg.md) | Query PostgreSQL records with natural language and Jev-backed semantic filters, extraction, and reusable named features (`SEMANTIC_FEATURE`). | Python · app/HTTP API + PostgreSQL (Apache-2.0); native Rust preview |
| [jevfilter](damiensmith1-jevfilter.md) | Filter/classify text with plain-English rules via TypeSafe Jev (`choose`/`check`/`rate`); PyPI. | Python · PyPI (`jevfilter`, MIT) |
| [jevgrep (dzhng)](dzhng-jevgrep.md) | Ask a repository question; Jev judges folder/file/declaration relevance and returns files plus verbatim excerpts for coding agents (`jg`). Distinct from kyu1204/jgrep. | TypeScript · npm CLI (`@dzhng/jevgrep`, Node 22+) |
| [jevql](jevql.md) | Add `jev()` / `jev_prob` / `jev_choice` / `jev_score` to queries against vanilla PostgreSQL without an extension, from a psql-style CLI, MCP server, or SDKs. | Go · CLI, MCP server and Go/TypeScript/Python SDKs (MIT) |
| [jevql (hemanth)](hemanth-jevql.md) | npm `jev-ql` semantic/cognitive SQL over unstructured data via TypeSafe Jev (distinct from kylemclaren/jevql). | JavaScript · npm (`jev-ql`, MIT) |
| [jevsearch](jevsearch.md) | Add a ⌘K site-search palette to a shadcn/ui site: keyword hits on the first keystroke, then one TypeSafe Jev request re-ranks the top 20 by intent, with no embeddings. | TypeScript · shadcn registry block (React component, Fetch-API handler; MIT) |
| [JevSQL](jevsql.md) | Add TypeSafe Jev match/pick/rank/bool/choice helpers to SQLite SQL with batching, caches, and review queues. | TypeScript · library and CLI |
| [JevTrace](jevtrace.md) | MCP retrieval filter: TypeSafe Jev keeps only relevant snippets to cut agent tokens | TypeScript · MCP server (MIT) |
| [jevzf](jevzf.md) | Rank piped text by meaning with TypeSafe Jev — plain filter or stock fzf Ctrl-R reload. | Node.js · CLI (`jevzf`, Apache-2.0) |
| [jgrep](jgrep.md) | Filters text, structured records, functions, and diff hunks against plain-English descriptions using Jev Noul judgments. | Python · library and CLI (`jev-grep`) |
| [jgrep (npm: jevgrep)](jgrep-jevgrep.md) | Gate a diff in CI on an English rule (`--diff`, grep exit codes), list the test files a diff can affect (`--tests`), or grep code and CSV rows by description with one TypeSafe Jev Noul per chunk. Distinct from the Python jgrep. | TypeScript · npm CLI (`jevgrep` 0.4.0, Node ≥ 18) |
| [jlink](jlink.md) | Links records under a plain-English match rule using Jev Noul pair judgments, with local candidate blocking and match resolution. | Python · library and CLI (`jlink`) |
| [jselect](jselect.md) | Selects source-linked evidence within a token budget using Jev Noul relevance judgments and local diversity-aware selection. | Python · library and CLI (`jev-select`) |
| [jsort](jsort.md) | Order lines/paragraphs/files along a plain-English dimension using pairwise TypeSafe Jev comparisons. | Python · CLI (`jsort` / jev-sort) |
| [laya-jev-GraphRAG](laya-jev-graphrag.md) | Agentic GraphRAG with swappable Laya/Jev System One decisions across Neo4j/Memgraph/AGE/Kùzu. | Python · GraphRAG framework (Apache-2.0) |
| [ldraw-nova](ldraw-nova.md) | Guide an agent to build LDraw LEGO models; its part/example search re-ranks candidates with Jev (falls back to full-text search without a key). | Python · Dockerized web app + agent tools (AGPL-3.0) |
| [llama-index-jev](llama-index-jev.md) | Rerank retrieved passages or choose a query engine in LlamaIndex. | Python · integration packages |
| [Milvus Model](milvus-model.md) | Score candidate documents with Jev Noul and return sorted results with original indices. | Python · PyMilvus model adapter |
| [mysql-ailike](mysql-ailike.md) | Filter and join MySQL rows with natural-language conditions via TypeSafe Jev (`AILIKE`). | MySQL · native UDF/plugin (v0.2.0, GPL-2.0) |
| [neo4jev](neo4jev.md) | Explore graph paths with typed next-hop and goal judgments. | Python · Neo4j, notebooks and Streamlit |
| [Note Filer](obsidian-note-filer.md) | Classify Obsidian notes with TypeSafe Jev and move them into Thema or IAB taxonomy folders after confirmation. | TypeScript · Obsidian desktop plugin (0BSD) |
| [pg-jev](pg-jev.md) | Ask semantic questions from SQL over database rows. | PostgreSQL · PL/Python extension |
| [pg_typesafe](pg-typesafe.md) | Call Choice/Noul/Score from SQL via a C+libcurl extension with batched multi-text helpers (pre-alpha; distinct from pg-jev). | PostgreSQL · C extension |
| [ReadyCode Reader](readycode-reader.md) | Local PDF/DOCX/XLSX evidence for agents: TypeSafe Jev checks passages before cited answers (MCP + browser) | Node.js · MCP (`@readycode/reader`) + browser demo (Apache-2.0) |
| [sgrep](sgrep.md) | Semantic grep: chunk a repo and ask TypeSafe Jev which chunks match a plain-English query (mock offline). | Python · CLI (`sgrep`) |
| [Semble + Jev (semble-jev)](semble-jev.md) | Semble retrieves local snippets; TypeSafe Jev scores relevance; CLI returns original source (`sj`). | Python · CLI via uv (Apache-2.0) |
| [sieve](sieve.md) | Local MCP: enumerate repo/search candidates and score with TypeSafe Jev (`jev_grep` / `jev_rank` / `jev_search`). | Python · MCP server (`sieve` 0.1.0, uv) |
| [sift-light](sift-light.md) | Replace an agent's grep/glob with paged, evidence-carrying search; set `semanticJudge.enabled: true` with `provider: "jev"` so Jev classifies hybrid-search candidates. | Node.js 22.19+ · npm package (Pi/OMP plugin, MCP server) (AGPL-3.0) |
| [SlopSearX](slopsearx.md) | Serve agent-friendly search (HTML/JSON/YAML, MCP) and let Jev add the specialist engines that can contribute distinctive evidence and reorder a bounded shortlist. | Python · server + MCP (`slopsearx-mcp`), Docker/k8s (MIT) |
| [SuperLocalMemory](superlocalmemory.md) | Store and recall agent memories locally (CLI, dashboard, Claude Code/Codex hooks); opt in to *Online with Jev* so TypeSafe or OpenRouter judges the top 3 results and SLM can say "I don't have that". | Python 3.12+ (npm or pip install) · CLI, daemon, dashboard, MCP/plugin (AGPL-3.0) |
| [sys1grep (jev-semgrep)](jev-semgrep.md) | Filter lines by whether a plain-language proposition holds, with AND/OR/NOT meanings via TypeSafe Jev (not Semgrep Inc). Renamed from jev-semgrep / `@uehaj/semgrep`. | Node.js · CLI (`@uehaj/sys1grep`) |
| [Truffler](truffler.md) | Rails intent search with TypeSafe Jev index-time labels, query understanding, and optional streamed reranking. | Ruby · Rails gem (MIT) |
| [web-scout-ai](web-scout-ai.md) | Read real sources (HTML, JS sites, documents) rather than snippets, with Jev choosing which follow-up links to open and classifying content; GPT fallback available. | Python · PyPI `web-scout-ai` (MIT) |
| [webctl](webctl.md) | Agent web-search CLI: multi-provider results scored/judged (and optionally chunk-scored) with TypeSafe Jev. | Go · CLI (`webctl`) |
| [XERJ](xerj.md) | Index code, docs, logs and PDFs for agents; add `"rerank": {}` to a `_search` so Jev scores the top hits, or use the local `/v1/systemone`-compatible `_decide` endpoint (answered by XERJ, not Jev). | Rust · single binary (HTTP + MCP), Elasticsearch-compatible API (Apache-2.0) |
| [Zerikai Memory](zerikai-memory.md) | Local code-memory MCP with TypeSafe Jev semantic judgment over retrieved snippets | Python · MCP server (MIT) |

## Try a smaller example

The repository also maintains its own [teaching examples](../../../examples/README.md), [Support Router](../../../projects/support-router/README.md), and [routing evaluation runner](../../../evaluations/README.md). These are useful when you want a small offline starting point before adopting a community project.

## Share or improve a tool

Follow [Add a community project](../../../CONTRIBUTING.md#add-a-community-project) and the [project-page template](../../PROJECT_TEMPLATE.md). Put the full guide in this folder, list it once in a category above, and keep its upstream and guide links in the root README. Corrections to setup instructions and limitations are welcome.

Upstream maintainers own their code and licenses. Check each page's reviewed version and [validation scope](../../../docs/validation.md#community-project-checks); a listing does not establish production quality or endorsement.
