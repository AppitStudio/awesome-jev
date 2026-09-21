# Apps powered by Jev

[All projects](../README.md) · [Tools and integrations](../tools/README.md) · [Share your app](../../../CONTRIBUTING.md#list-a-jev-powered-app)

Discover applications that use Jev to power a real user workflow. Each app has its own full page explaining what it does, how to access it, and where Jev fits. Hosted products and source-built apps are both welcome; other models may power additional features.

Read the [tag guide](../../APP_TAGS.md): **Open source** describes source licensing; **Commercial** marks a paid offering. Both can apply to the same app. Closed-source products are welcome with public Jev evidence and a clear source-review disclosure. Pricing unknowns stay visible.

## Web apps

### Apparite (jev2ui)

`Open source` · `Free source build` · `BYOK`

Local design-mock lab where TypeSafe Jev chooses information architecture and component anatomy, Gemini writes copy, and code assembles A2UI-inspired mocks painted by a DESIGN.md.

**Access:** clone the [Apache-2.0 source](https://github.com/dglazkov/jev2ui) (Node.js) with `JEV_API_KEY` / TypeSafe credentials and a Gemini key for full mock generation. No app purchase fee; provider usage is separate. Offline `npm run typecheck` and `npm run build` passed on the review host; live mock generation was not run.

[Full Apparite (jev2ui) guide](jev2ui.md) · [Source](https://github.com/dglazkov/jev2ui)

### Call Coach

`Open source` · `Free source build` · `BYOK`

Local live sales-call coach: TypeSafe Jev judges next-best actions and buying stage from transcript turns; UI applies confidence gates (mic or sample call).

**Access:** clone the [MIT source](https://github.com/ZeroGold/call-coach-ai) (Node.js ≥ 18) with `TYPESAFE_API_KEY` and run `node server.mjs` → `http://localhost:3000`. No app purchase fee; TypeSafe usage is separate. Optional Electron overlay not required for the web demo. `node --check server.mjs` clean on the review host; live mic/TypeSafe not run.

[Full Call Coach guide](call-coach-ai.md) · [Source](https://github.com/ZeroGold/call-coach-ai)

### Clean Code Review

`Open source` · `Free source build` · `BYOK`

Hosted and source-built PR reviewer: TypeSafe Jev judges changed files against Clean Code questions; Luna writes evidence-first prose; MCP endpoint for agents.

**Access:** try [clean-code-review.vercel.app](https://clean-code-review.vercel.app) (operator budgets) or clone the [MIT source](https://github.com/frostney/clean-code-review) with Bun and provider keys. No app purchase fee; provider usage is separate. Offline `bun test`: 70 passed on the review host; live PR review not run.

[Full Clean Code Review guide](clean-code-review.md) · [Source](https://github.com/frostney/clean-code-review) · [Product homepage](https://clean-code-review.vercel.app)

### Crush Monitor

`Open source` · `Free source build` · `BYOK`

Local WeChat-style chat analyzer: TypeSafe Jev labels emotion and intent, scores affinity, and rates replies on localhost with your own key.

**Access:** clone the [MIT source](https://github.com/FerryCorleone/crush-monitor) (Node.js 22.12+) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `npm test`: 36 passed; live analysis not run on the review host.

[Full Crush Monitor guide](crush-monitor.md) · [Source](https://github.com/FerryCorleone/crush-monitor)

### Fotocopiatrice

`Open source` · `Free source build` · `BYOK`

Explore Italian Camera amendments: identical texts grouped in code, TypeSafe Jev judges attributes and near-duplicate pairs; static site plus reusable exports.

**Access:** open [fotocopiatrice.vercel.app](https://fotocopiatrice.vercel.app/) (committed JSON, no server key) or clone the [MIT source](https://github.com/bnistor4/fotocopiatrice) (Node.js) with `TYPESAFE_API_KEY` only to regenerate the pipeline. No app purchase fee; TypeSafe usage is separate. `tsc --noEmit` clean on the review host; live pipeline not run.

[Full Fotocopiatrice guide](fotocopiatrice.md) · [Source](https://github.com/bnistor4/fotocopiatrice) · [Product homepage](https://fotocopiatrice.vercel.app/)

### Hearth

`Open source` · `Free source build` · `BYOK`

Local multi-marketplace rental search (Craigslist, Facebook Marketplace, Redfin, Zillow): TypeSafe Jev chooses browser actions; the app only reads and shortlists—never messages sellers.

**Access:** clone the [MIT source](https://github.com/Nancy-Chauhan/hearth-jev-rental-search) (Python ≥ 3.12, `uv`, Chrome CDP) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `pytest`: 63 passed; live Chrome/marketplace runs not executed. Distinct from browser-use/jev-ultrafast despite a shared package folder name.

[Full Hearth guide](hearth.md) · [Source](https://github.com/Nancy-Chauhan/hearth-jev-rental-search)

### Hx

`Open source` · `Free source build` · `BYOK`

Clinical documentation aid: as a doctor types or dictates, Hx opens the checklist the note implies, ticks items against clauses copied from the text, and shows what is still undocumented—without generating clinical prose. TypeSafe Jev supplies typed judgments.

**Access:** public demo at [hx.semicoded.com](https://hx.semicoded.com) (rate/spend limited) or clone the [MIT source](https://github.com/doitrous/hx) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Postgres optional for accounts. Offline server unit tests partially passed without Postgres; live analyze not run on the review host.

[Full Hx guide](hx.md) · [Source](https://github.com/doitrous/hx) · [Product homepage](https://hx.semicoded.com)

### Jev Call Screener

`Open source` · `Free source build` · `BYOK`

Self-host a call-screening backend that classifies caller transcripts with TypeSafe Jev and forwards or rejects under a fail-open Go policy. Twilio adapter included; REST classify works without telephony.

**Access:** clone the [MIT source](https://github.com/SuchintK/jev-call-screener) (Go 1.27.1+) with `TYPESAFE_API_KEY`. No app purchase fee; Twilio/telephony minutes and TypeSafe usage are separate. Live Twilio and live Jev were not tested on the review host.

[Full Jev Call Screener guide](jev-call-screener.md) · [Source](https://github.com/SuchintK/jev-call-screener)

### Jev demos

`Open source` · `Free source build` · `BYOK`

Six local side-by-side TypeSafe Jev demos (router, triage, inbox, slop filter, title scorer, cost) with Claude/Kimi as interchangeable LLMs; simulated mode works without keys.

**Access:** clone the [MIT source](https://github.com/mayank953/Jev) (Node 22.6+) and `npm start` on localhost:3000. Optional `TYPESAFE_API_KEY` / Anthropic / Moonshot keys. No app purchase fee; provider usage is separate. Offline `npm run typecheck` passed; live UI/providers not run on the review host.

[Full Jev demos guide](jev-demos.md) · [Source](https://github.com/mayank953/Jev)

### Jev Grand Prix

`Open source` · `Free source build` · `BYOK`

Local F1 race where TypeSafe Jev picks racing line and pedals; code steers, brake-by-wires, and plans the next lap from corner history.

**Access:** clone the [MIT source](https://github.com/enoyola/jev-grand-prix) (`uv run server.py`) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `server.py` AST parse OK; live race not run on the review host.

[Full Jev Grand Prix guide](jev-grand-prix.md) · [Source](https://github.com/enoyola/jev-grand-prix)

### JevEye

`Open source` · `Free source build` · `BYOK`

Browser vision probes report calibrated facts (or abstain); TypeSafe Jev plans what to look for and judges the text fact sheet—never pixels.

**Access:** clone the [MIT source](https://github.com/Adityakhalkar/JevEye) (Node.js 20+) with `TYPESAFE_API_KEY` on the server, or deploy to Vercel with that env var. No app purchase fee; TypeSafe usage is separate. Offline `npm test`: 12 passed; live image judgment not run on the review host.

[Full JevEye guide](jeveye.md) · [Source](https://github.com/Adityakhalkar/JevEye)

### Jev Radar

`Open source` · `Free source build` · `BYOK`

Run local evidence-linked research from a prompt. Jev selects methods, questions, leads, and claim checks; Brave Search discovers sources; an optional text model proposes questions and drafts answers for Jev to verify.

**Access:** clone and run the [MIT source](https://github.com/Eliovp-BV/Jev-Radar) (Python 3.11+, Node 22.12+ or Node 20.19+ within 20) with `TYPESAFE_API_KEY` and usually `BRAVE_SEARCH_API_KEY`. No app purchase fee; search and provider usage can incur charges. Default estimated spend ceilings are $5 Jev / $20 text model per investigation. No login—bind to localhost on untrusted networks. Offline pytest on the review host: 600 passed, 2 failed, 22 skipped; live investigations not run.

[Full Jev Radar guide](jev-radar.md) · [Source](https://github.com/Eliovp-BV/Jev-Radar)

### Jev Search

`Open source` · `Pricing unverified` · `BYOK`

Search across selected sources and explore ranked links with editable filters. Jev selects queries, sources, and time windows, then judges result relevance; Search1API retrieves the links.

**Access:** use the [hosted application](https://jev.s1.dev) or self-host from source with Search1API and a configured Jev provider (TypeSafe by default; newer source also supports Vercel AI Gateway or Cloudflare Workers AI). Self-hosting can incur provider and hosting charges. The hosted homepage was checked; live search and hosted access limits were not tested.

[Try Jev Search](https://jev.s1.dev/) · [Full Jev Search guide](jev-search.md) · [Source](https://github.com/superagents-lab/jev-search)

### Jev Social

`Open source` · `Free source build` · `BYOK`

Run local Instagram, TikTok, and LinkedIn research from a goal. TypeSafe Jev (via OpenRouter) chooses each read-only socai CLI operation; Chrome evidence feeds the next decision and cited reports.

**Access:** with Node.js 20+, run `npx --yes github:socai-io/jev-social onboard`, then `npx --yes github:socai-io/jev-social`; cloning the [MIT source](https://github.com/socai-io/jev-social) remains an alternative. Onboarding validates the OpenRouter key, stores a key entered at its prompt, and can offer the official socai installer on macOS or Windows; Linux users install socai from source and set `SOCAI_BIN`. A usable Chrome login is required for the selected platform. No app purchase fee; provider and platform access are separate. Live social browsing was not tested on the review host.

[Live site](https://socai-io.github.io/jev-social/) · [Full Jev Social guide](jev-social.md) · [Source](https://github.com/socai-io/jev-social)

### JevSlop

`Open source` · `Free source build` · `BYOK`

Score note articles for AI-slop writing patterns with TypeSafe Jev (multi-axis Score plus overall Choice). Bring your own TypeSafe key on the hosted Pages app or a source build.

**Access:** open [jevslop.pages.dev](https://jevslop.pages.dev/) or build from the [MIT source](https://github.com/TKY-27/JevSlop). No app purchase fee; TypeSafe inference is separate. Live TypeSafe evaluation was not tested on the review host.

[Try JevSlop](https://jevslop.pages.dev/) · [Full JevSlop guide](jevslop.md) · [Source](https://github.com/TKY-27/JevSlop)

### Jevmail

`Open source` · `Free source build` · `BYOK`

Local read-only Gmail triage into Needs reply / Updates / Promos / Sales / Spam using TypeSafe Jev via the Vercel AI Gateway, with urgency and personal-mail scores plus retained corrections.

**Access:** clone and run the [MIT source](https://github.com/fazlerocks/jevmail) with pnpm, Google OAuth (Gmail API), `AI_GATEWAY_API_KEY`, and `AUTH_SECRET`. No app purchase fee; Gateway free-tier limits and Gmail quotas apply. Offline `pnpm test` skips without a Gateway key; live Gmail classification not run.

[Full Jevmail guide](jevmail.md) · [Source](https://github.com/fazlerocks/jevmail)

### JevZero

`Open source` · `Free source build` · `BYOK`

Local Gmail inbox helper: TypeSafe Jev classifies category/priority/signals; you review exact proposed labels, then apply with verified receipts and undo. Demo mode works without keys.

**Access:** clone and run the [MIT source](https://github.com/jayozer/jevzero) with `uv run jevzero` (Python ≥ 3.12, Node.js 22+). Needs your TypeSafe key and Google OAuth loopback client for live mail; TypeSafe/Google billed separately. Offline `uv run pytest`: 62 passed on this review; live Gmail/TypeSafe not run.

[Full JevZero guide](jevzero.md) · [Source](https://github.com/jayozer/jevzero)

### Notra

`Open source` · `Commercial` · `Paid`

Track how AI answers describe and position your brand. Jev judges brand sentiment and list position within a wider analytics application; other models handle scans, general judging, and drafting.

**Access:** the [hosted product](https://www.usenotra.com) requires an account and offers [paid plans](https://www.usenotra.com/pricing), checked 2026-09-19. Trial eligibility and checkout were not tested. Self-hosting requires database, authentication, and provider setup; the guide records database initialization caveats. This commercial listing is not an endorsement.

[Full Notra guide](notra.md) · [Source](https://github.com/usenotra/notra)

### QuantDinger

`Open source` · `Free source build` · `BYOK`

Self-host an AI trading research and execution stack. Optional TypeSafe Jev pre-trade Choice checks gate live *entry* orders with an auditable timeline; exits bypass AI. Hosted product also available.

**Access:** clone the [Apache-2.0 source](https://github.com/OpenByteInc/QuantDinger) and run via Docker Compose; configure `JEV_API_KEY` for the decision filter. No app purchase fee for self-host; hosted SaaS at [ai.quantdinger.com](https://ai.quantdinger.com) may bill separately (not verified here). Exchange and TypeSafe usage are separate. Live trading and live Jev calls were not run on the review host.

[Live app](https://ai.quantdinger.com) · [Website](https://www.quantdinger.com) · [Full QuantDinger guide](quantdinger.md) · [Source](https://github.com/OpenByteInc/QuantDinger)

### RefGarden

`Open source` · `Free source build` · `BYOK`

Explore a local 3D gallery of image and short-video references from a prompt. Jev chooses search phrases and highlights catalog items from titles/descriptions; Met, NASA, Cosmos, and Internet Archive supply media.

**Access:** clone and run the [MIT source](https://github.com/AlbionaHoti/refgarden#run-locally) (Node.js 22+) with a TypeSafe key for local Explore. No app purchase fee; provider usage can incur charges. Hosted preview is keyword-only (no Jev). Offline bun tests: 74 passed on the review host; live Explore not run.

[Full RefGarden guide](refgarden.md) · [Source](https://github.com/AlbionaHoti/refgarden)

### JEV Document Classification

`Open source` · `Free source build` · `BYOK`

File a local document folder into configured categories with TypeSafe Jev (Vercel AI Gateway): local extraction, typed category/confidentiality/injection/subject choices, audit preview and undo.

**Access:** clone the [MIT source](https://github.com/Charlyhno-eng/jev-document-classification) (Node.js + npm) with a Vercel AI Gateway key for classification. No app purchase fee; provider usage is separate. Live classification was not tested on the review host.

[Full JEV Document Classification guide](jev-document-classification.md) · [Source](https://github.com/Charlyhno-eng/jev-document-classification)

### Transcript Lens

`Open source` · `Free source build` · `BYOK`

Explore YouTube transcripts by meaning with a Turkish UI: TypeSafe Jev classifies caption blocks for kind, value, and signals without rewriting the text.

**Access:** clone the [MIT source](https://github.com/sensahin/transcript-lens) (Node.js 22+) with a Vercel AI Gateway or TypeSafe key for analysis. No app purchase fee; provider usage is separate. Keyless mode still opens/pastes/exports sample text. Live analysis was not tested on the review host.

[Full Transcript Lens guide](transcript-lens.md) · [Source](https://github.com/sensahin/transcript-lens)

### Watermelon

`Open source` · `Free source build` · `BYOK`

Status-update honesty auditor: TypeSafe Jev judges language while local code parses dates/slippage, then reports whether the health label matches the facts and whether escalation is warranted.

**Access:** public demo at [watermelon.shashwatchavan.com](https://watermelon.shashwatchavan.com) or clone the [MIT source](https://github.com/shashwatc12/watermelon) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `npm test`: 22 passed; live TypeSafe calls not run on the review host.

[Full Watermelon guide](watermelon.md) · [Source](https://github.com/shashwatc12/watermelon) · [Product homepage](https://watermelon.shashwatchavan.com)

## macOS apps

### Jaste

`Source unverified` · `Pricing unverified` · `BYOK`

Smart copy/paste beta with clipboard history and an optional Direct Jev mode that selects a saved text value for the focused field.

**Access:** [download the Mac beta](https://jaste.app/) for Apple silicon and macOS 14+. The inspected bundle offers a Direct Jev key setting; that mode requires a TypeSafe key and may incur inference charges. App pricing and hosted access limits are unverified. No public source or license was linked; review covered the homepage and release metadata/strings, without launching the app or testing live matching.

[Full Jaste guide](jaste.md) · [Product and access](https://jaste.app/)

### Jev Voice

`Open source` · `Free source build` · `BYOK`

Talk to your Mac with local whisper.cpp transcription. Jev selects a typed action and arguments in one fan-out; code executes via Accessibility/AppleScript.

**Access:** run the [MIT source](https://github.com/kevinbadi/jev-voice) on Apple Silicon–oriented macOS with Python 3.12+, the setup script, a TypeSafe key, and Microphone / Accessibility / Input Monitoring permissions. No app purchase fee; provider usage can incur charges. Live voice and desktop actions were not tested on the Linux review host.

[Full Jev Voice guide](jev-voice.md) · [Source](https://github.com/kevinbadi/jev-voice)

### Live Jev

`Open source` · `Free source build` · `BYOK`

Control Ableton Live from a ⌘⇧Space bar: TypeSafe Jev chooses typed mixer, transport, clip, note, and device actions from short English or Japanese phrases; a Remote Script applies them on localhost.

**Access:** build the [MIT source](https://github.com/okinaaudio/live-jev) on Apple Silicon macOS 14+ with Python 3.13, Xcode CLT, Ableton Live 12, and a TypeSafe key. Early **0.1x** source distribution (no packaged installer). No app purchase fee; provider usage can incur charges. Live Ableton control was not tested on the Linux review host.

[Full Live Jev guide](live-jev.md) · [Source](https://github.com/okinaaudio/live-jev)

### macbrow

`Open source` · `Free source build` · `BYOK`

Control macOS apps and perform Chrome tasks through an experimental voice assistant. Jev routes requests, selects tool arguments, and judges follow-ups; Gradium handles speech and a separate LLM supplies generated scripts and text.

**Access:** run the [MIT source](https://github.com/timpratim/macbrow#setup) on macOS with Python 3.12+, `uv`, TypeSafe and Gradium keys, and desktop permissions. The default LLM backend also needs LiveKit credentials; LM Studio is an alternative. No app purchase fee applies to the source build; provider usage can incur charges. Browser tasks require Chrome remote debugging. All 26 upstream tests passed with network access denied; live voice, desktop actions, and browser automation were not tested.

[Full macbrow guide](macbrow.md) · [Source](https://github.com/timpratim/macbrow)

### TipTour

`Open source` · `Free source build` · `BYOK`

Use a macOS menu bar companion to act on typed click requests. Jev chooses among locally detected controls and judges completion or missing targets. A separate Gemini mode handles voice and writing.

**Access:** macOS 14.2+, a source build with Xcode, a TypeSafe key, and desktop permissions. Gemini mode needs its own key. Source is MIT licensed; provider usage can incur charges. Eight isolated decision tests passed; the full app, packaged releases, and live desktop actions were not tested.

[Full TipTour guide](tiptour.md) · [Source](https://github.com/milind-soni/tiptour-macos)

## Android apps

### Jev Chat Assistant

`Open source` · `Free source build` · `BYOK`

Non-invasive Android overlay: Accessibility reads on-screen chat; TypeSafe Jev (OpenRouter Decisions) judges intent/danger/action and ranks drafted replies; fill-only paste (never auto-send). WeChat first.

**Access:** build the [MIT source](https://github.com/Finderchangchang/jev-chat-JARVIS) (JDK 17, Android SDK 35) with an OpenRouter API key plus Accessibility/overlay permissions. No app purchase fee; OpenRouter/Jev usage is separate. Source inspected; APK build and live calls not run on the Linux review host. Distinct from desktop WeChat-log analyzers and the separate Android UI-agent SDK listed under Developer tools.

[Full Jev Chat Assistant guide](jev-chat-jarvis.md) · [Source](https://github.com/Finderchangchang/jev-chat-JARVIS)

## Browser extensions

### Focus

`Open source` · `Free source build` · `BYOK`

Browser extension that uses TypeSafe Jev (via OpenRouter Decisions) to classify domains as productive or distracting and block distracting navigations, with local allow/block lists and cache.

**Access:** [load the GPL-3.0 source unpacked](https://github.com/bramtechs/Focus#install-chrome--edge--brave) (Chrome/Edge/Brave; Firefox temporary; Safari packaging script) with an OpenRouter API key. No app purchase fee; Decisions/Jev usage can incur charges. Source inspected; browser install and live calls not tested on the review host.

[Full Focus guide](focus.md) · [Source](https://github.com/bramtechs/Focus)

### HookMeter

`Open source` · `Free source build` · `BYOK`

Chrome extension (optional FastAPI / Cloudflare Worker) that scores social-post drafts as you type with TypeSafe Jev—curiosity, emotional arousal, hook pattern, and clickbait risk—then shows a short rewrite hint. Distinct from jevx and Vibe Check for X.

**Access:** [load the MIT source unpacked](https://github.com/ehui1226/hookmeter-jev) (`extension/`) with a TypeSafe or OpenRouter key; optional local server or Cloudflare Worker. No app purchase fee; inference can incur charges. Source inspected; Chrome install and live calls not tested on the review host; bundled engine unit tests were not green without live mocks.

[Full HookMeter guide](hookmeter.md) · [Source](https://github.com/ehui1226/hookmeter-jev)

### Jev for Chrome

`Open source` · `Free source build` · `BYOK`

Drive the Chrome tab you already have open with TypeSafe Jev. Community Manifest V3 port of browser-use/jev-ultrafast: Jev picks each click/keystroke/dropdown; a small text model fills TYPE_TEXT.

**Access:** build or load the [MIT source / releases](https://github.com/chy4pro/jev-for-chrome) as an unpacked Chromium extension with a TypeSafe (or OpenRouter/Cloudflare) key plus an OpenAI-compatible text helper. No app purchase fee; provider usage can incur charges. Offline vitest: 73 passed; Chrome install and live driving not tested on the review host.

[Full Jev for Chrome guide](jev-for-chrome.md) · [Source](https://github.com/chy4pro/jev-for-chrome)

### Jevfill

`Open source` · `Free source build` · `BYOK`

Chrome extension that autofills web forms from unstructured personal notes with TypeSafe Jev field-to-line matching. Distinct from Smart Paste (exact clipboard paste/verify).

**Access:** [build and load unpacked](https://github.com/imohitmayank/jevfill) (`npm run build` → `dist/`) with a TypeSafe API key in options. No app purchase fee; TypeSafe usage can incur charges. Offline vitest: 7 passed; Chrome install and live calls not tested on the review host.

[Full Jevfill guide](jevfill.md) · [Source](https://github.com/imohitmayank/jevfill)

### jevx

`Open source` · `Free source build` · `BYOK`

Find relevant X posts for your interests and optionally score unpublished drafts with TypeSafe Jev. Chrome/Firefox BYOK extension with no backend—local profile/key storage; consented text goes only to TypeSafe.

**Access:** [build and load unpacked](https://github.com/hawkyre/jevx#install) (Chrome MV3 / Firefox temporary) with a TypeSafe API key. No app purchase fee; TypeSafe usage can incur charges. Offline vitest: 87 passed; browser install and live calls not tested on the review host.

[Full jevx guide](jevx.md) · [Source](https://github.com/hawkyre/jevx)

### PageGrade

`Open source` · `Free source build` · `BYOK`

Grade readable page sections for clarity, writing, and on-page SEO with TypeSafe Jev Score rubrics via the Vercel AI Gateway; inspect an A–E page summary in Chrome's side panel.

**Access:** [build with Bun and load unpacked](https://github.com/kitze/pagegrade#install-locally) (`.output/chrome-mv3`) with a Vercel AI Gateway API key. No app purchase fee; Gateway/Jev usage can incur charges. Source inspected; Chrome install and live grading not tested on the review host.

[Full PageGrade guide](pagegrade.md) · [Source](https://github.com/kitze/pagegrade)

### Polymorph

`Open source` · `Free source build` · `BYOK`

Collapse posts that match English rules you wrote; TypeSafe Jev via OpenRouter Decisions is the judge. Matched posts become your images/GIFs or a compact card—Show original restores them.

**Access:** [build with pnpm and load unpacked](https://github.com/moomooskycow/polymorph#load) (`dist/`) with an OpenRouter API key. No app purchase fee; Decisions/Jev usage can incur charges. Not Chrome Web Store listed. Source inspected; Chrome install and live feed judging not tested on the review host.

[Full Polymorph guide](polymorph.md) · [Source](https://github.com/moomooskycow/polymorph)

### Smart Paste

`Open source` · `Free source build` · `BYOK`

Paste a block of text into supported web form fields with undo. Jev chooses relevant passages, selects value boundaries, and verifies the proposed matches; JavaScript copies exact source text and checks that the page retains it.

**Access:** load the [MIT source as an unpacked Chrome extension](https://github.com/nomanjack/smart-paste#install), add a TypeSafe key, and enable matching. No app purchase is required for this source distribution; each paste can make up to three potentially billable provider requests. The extension is experimental, sends pasted text and limited form context to TypeSafe, and can replace the focused field. Source and mocked tests were checked; Chrome installation and live matching were not tested.

[Full Smart Paste guide](smart-paste.md) · [Source](https://github.com/nomanjack/smart-paste)

### Slop Mop

`Open source` · `Free` · `BYOK`

Judge LinkedIn post writing with TypeSafe Jev (11–12 typed questions), then fold or highlight suspected slop with inspectable scores and local overrides. Not an AI detector. Distinct from JevSlop (note/article scoring).

**Access:** free hosted use via [slopmop.lol](https://slopmop.lol) (no signup; daily check limits on the maintainer's server, default 250/install/UTC day) or [self-host the MIT source](https://github.com/tomfrazier/slopmop) with your own TypeSafe/AI Gateway key. Desktop Chromium / LinkedIn only; load unpacked from a local build. No Chrome Web Store listing verified. Source and offline vitest inspected; Chrome install and live LinkedIn/Jev not tested on the review host.

[Full Slop Mop guide](slop-mop.md) · [Source](https://github.com/tomfrazier/slopmop)

### Sponsor Skip

`Source unverified` · `Pricing unverified` · `BYOK`

Find sponsor reads on YouTube using Jev judgments over transcript lines or live speech text, then inspect or skip them.

**Access:** [load the Chrome extension from source](https://github.com/trungdq88/youtube-sponsor-detection#chrome-extension) with a TypeSafe key; audio modes also need Deepgram. Auto-skip defaults on. Provider fees apply; no license or app pricing terms were found. Source inspected only; live playback and accuracy untested.

[Full Sponsor Skip guide](sponsor-skip.md) · [Source](https://github.com/trungdq88/youtube-sponsor-detection)

### Tab Bouncer

`Open source` · `Free source build` · `BYOK`

Rate open tabs for a task you type with TypeSafe Jev, then close the ones that do not belong. Distinct from Jev for Chrome (computer-use driver): bulk triage with keep noul + kind choice per tab, batches of up to 120.

**Access:** [load the MIT source as an unpacked Chromium extension](https://github.com/MANISH007700/tab-bouncer#install) and paste a TypeSafe key in options. No app purchase fee; inference usage can incur charges. Offline `node --test`: 7 passed; Chrome install and live TypeSafe calls not tested on the review host.

[Full Tab Bouncer guide](tab-bouncer.md) · [Source](https://github.com/MANISH007700/tab-bouncer)

### TypeSafe Fun AdBlocker

`Open source` · `Free source build` · `BYOK`

Ask Jev whether heuristically selected DOM elements are ads, then remove or highlight matches in an experimental Chrome extension.

**Access:** [load the MIT source as an unpacked Chrome extension](https://github.com/realZachi/typesafe-adblock#install) and paste a TypeSafe key. No app purchase fee; each batch can incur provider charges. Explicit fun demo, not a production ad blocker. Source inspected; Chrome installation and live browsing were not tested.

[Full TypeSafe Fun AdBlocker guide](typesafe-adblock.md) · [Source](https://github.com/realZachi/typesafe-adblock)

### Unclutter

`Open source` · `Free source build` · `BYOK`

Hide page clutter with Jev classifications and reusable local rules, with pause and per-element controls.

**Access:** build the [MIT source](https://github.com/kitze/unclutter#install-from-source) using Bun and Node.js 22.12+ for Chromium or Firefox 140+. Supply a TypeSafe or Vercel AI Gateway key; inference charges apply. Manual analysis is the default; optional automatic analysis sends snippets on page visits. Source was inspected; installation and live browsing were not tested.

[Full Unclutter guide](unclutter.md) · [Source](https://github.com/kitze/unclutter)

### Vibe Check for X

`Source unverified` · `Pricing unverified` · `BYOK`

Review draft X posts, replies, and quote posts with a scorecard inside the composer. Jev judges qualities such as clarity, humor, and regret risk; JavaScript combines the judgments into a verdict. Optional OpenAI vision calls describe media for Jev.

**Access:** load the source folder as an unpacked Chrome extension and supply a TypeSafe key; media descriptions need an OpenAI key. No license file or explicit app pricing terms were found. Provider calls can incur charges, auto-analysis is enabled by default, and keys use Chrome sync storage. Source and syntax were checked; Chrome installation and live scoring were not tested.

[Full Vibe Check guide](vibecheck.md) · [Source](https://github.com/RafalWilinski/vibecheck)

### Xtags

`Open source` · `Free source build` · `BYOK`

Label each X timeline post with intent and thresholded risk signals. Jev answers four typed questions per post; the extension renders tags in the timeline.

**Access:** load the [MIT `extension/` folder unpacked](https://github.com/manifoldor/xtags#安装) (or the Tampermonkey userscript) and paste a TypeSafe key. No app purchase fee; provider usage can incur charges. Independent of X Corp. Source inspected; Chrome install and live labeling not tested.

[Full Xtags guide](xtags.md) · [Source](https://github.com/manifoldor/xtags)

## Command-line apps

### Jev Mail Classifier

`Open source` · `Free source build` · `BYOK`

Classify IMAP mail with Jev yes/no category judgments, then tag, move, flag, or notify from a Textual TUI and cron-friendly CLI.

**Access:** clone and run the [MIT source](https://github.com/parth-kp/jev-mail-classifier) (Python 3.10+) with `./install.sh`, a Jev provider key (TypeSafe, OpenRouter, or Vercel AI Gateway), and IMAP credentials (often an app password). No app purchase fee; provider and mailbox-host usage can incur charges. Offline pytest: 61 passed on the review host; live mailbox classification not run.

[Full Jev Mail Classifier guide](jev-mail-classifier.md) · [Source](https://github.com/parth-kp/jev-mail-classifier)

### Jevmeter

`Open source` · `Free source build` · `BYOK`

Annotate videos with Jev judgments about sentence-level rhetoric, then render overlays and highlights.

**Access:** [build the MIT Python CLI](https://github.com/ChetasLua/jevmeter#-command-line-for-power-users) with a Whisper backend, FFmpeg support and TypeSafe key. Source has no purchase fee; inference charges apply. The review inspected source only. Scores are model judgments, not fact-checks; failed sentences can be omitted.

[Full Jevmeter guide](jevmeter.md) · [Source](https://github.com/ChetasLua/jevmeter)

## Discord bots

### Jev Moderation Bot

`Source unverified` · `Pricing unverified` · `BYOK`

Moderate Discord messages with Jev classifications, configurable escalation and member activity summaries.

**Access:** [self-host the Python bot](https://github.com/brainstormity/Jev-Moderation-Bot#setup) with Discord bot permissions and a TypeSafe key. Starting it enables automatic message deletion and escalating timeouts; no review-only mode was established. Inference/hosting costs apply. README declares MIT but a complete license was not found. Source reviewed; live moderation and accuracy untested.

[Full Jev Moderation Bot guide](jev-moderation-bot.md) · [Source](https://github.com/brainstormity/Jev-Moderation-Bot)

## Telegram bots

### Jev Anti-Spam Bot

`Open source` · `Free source build` · `BYOK`

Delete high-confidence Telegram group spam with TypeSafe Jev Noul signals and fail-open errors; optional Postgres stats without storing message text.

**Access:** [self-host with Bun or Docker](https://github.com/backmeupplz/jev_antispam_bot#setup) using a Telegram bot token (privacy mode disabled) and a TypeSafe key. Adding the bot as a group admin with delete permission enables automatic deletions. Inference/hosting costs apply. MIT source; live moderation accuracy untested in this catalog review.

[Full Jev Anti-Spam Bot guide](jev-antispam-bot.md) · [Source](https://github.com/backmeupplz/jev_antispam_bot)

## Before you get started

Each guide records supported platforms, setup, accounts and keys, data recipients, costs, limitations, and the version reviewed. Follow its launch or build path. Source availability does not imply a downloadable release or free inference, and an app listing does not certify production readiness.

For components to integrate into your own project, browse [tools and integrations](../tools/README.md). For a small offline introduction, try the repository's [teaching examples](../../../examples/README.md).

## List your app

Self-submissions are welcome, including open-source, closed-source, free, and paid apps. Provide a working product or source-build link, official pricing/access information, evidence of Jev use, and your affiliation. Apply the [source/pricing tags and disclosures](../../APP_TAGS.md). Closed-source listings must identify what could not be independently inspected; commercial listings must visibly identify paid access.

Follow [List a Jev-powered app](../../../CONTRIBUTING.md#list-a-jev-powered-app) and the [project-page template](../../PROJECT_TEMPLATE.md), or [open an app suggestion](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml). App pages live in this folder, one full page per app.
