# Apps powered by Jev

[All projects](../README.md) · [Tools and integrations](../tools/README.md) · [Share your app](../../../CONTRIBUTING.md#list-a-jev-powered-app)

Discover applications that use Jev to power a real user workflow. Each app has its own full page explaining what it does, how to access it, and where Jev fits. Hosted products and source-built apps are both welcome; other models may power additional features.

Read the [tag guide](../../APP_TAGS.md): **Open source** describes source licensing; **Commercial** marks a paid offering. Both can apply to the same app. Closed-source products are welcome with public Jev evidence and a clear source-review disclosure. Pricing unknowns stay visible.

## Web apps

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

### Notra

`Open source` · `Commercial` · `Paid`

Track how AI answers describe and position your brand. Jev judges brand sentiment and list position within a wider analytics application; other models handle scans, general judging, and drafting.

**Access:** the [hosted product](https://www.usenotra.com) requires an account and offers [paid plans](https://www.usenotra.com/pricing), checked 2026-09-19. Trial eligibility and checkout were not tested. Self-hosting requires database, authentication, and provider setup; the guide records database initialization caveats. This commercial listing is not an endorsement.

[Full Notra guide](notra.md) · [Source](https://github.com/usenotra/notra)

## macOS apps

### Jev Voice

`Open source` · `Free source build` · `BYOK`

Talk to your Mac with local whisper.cpp transcription. Jev selects a typed action and arguments in one fan-out; code executes via Accessibility/AppleScript.

**Access:** run the [MIT source](https://github.com/kevinbadi/jev-voice) on Apple Silicon–oriented macOS with Python 3.12+, the setup script, a TypeSafe key, and Microphone / Accessibility / Input Monitoring permissions. No app purchase fee; provider usage can incur charges. Live voice and desktop actions were not tested on the Linux review host.

[Full Jev Voice guide](jev-voice.md) · [Source](https://github.com/kevinbadi/jev-voice)

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

## Browser extensions

### Smart Paste

`Open source` · `Free source build` · `BYOK`

Paste a block of text into supported web form fields with undo. Jev chooses relevant passages, selects value boundaries, and verifies the proposed matches; JavaScript copies exact source text and checks that the page retains it.

**Access:** load the [MIT source as an unpacked Chrome extension](https://github.com/nomanjack/smart-paste#install), add a TypeSafe key, and enable matching. No app purchase is required for this source distribution; each paste can make up to three potentially billable provider requests. The extension is experimental, sends pasted text and limited form context to TypeSafe, and can replace the focused field. Source and mocked tests were checked; Chrome installation and live matching were not tested.

[Full Smart Paste guide](smart-paste.md) · [Source](https://github.com/nomanjack/smart-paste)

### Sponsor Skip

`Source unverified` · `Pricing unverified` · `BYOK`

Find sponsor reads on YouTube using Jev judgments over transcript lines or live speech text, then inspect or skip them.

**Access:** [load the Chrome extension from source](https://github.com/trungdq88/youtube-sponsor-detection#chrome-extension) with a TypeSafe key; audio modes also need Deepgram. Auto-skip defaults on. Provider fees apply; no license or app pricing terms were found. Source inspected only; live playback and accuracy untested.

[Full Sponsor Skip guide](sponsor-skip.md) · [Source](https://github.com/trungdq88/youtube-sponsor-detection)

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

## Before you get started

Each guide records supported platforms, setup, accounts and keys, data recipients, costs, limitations, and the version reviewed. Follow its launch or build path. Source availability does not imply a downloadable release or free inference, and an app listing does not certify production readiness.

For components to integrate into your own project, browse [tools and integrations](../tools/README.md). For a small offline introduction, try the repository's [teaching examples](../../../examples/README.md).

## List your app

Self-submissions are welcome, including open-source, closed-source, free, and paid apps. Provide a working product or source-build link, official pricing/access information, evidence of Jev use, and your affiliation. Apply the [source/pricing tags and disclosures](../../APP_TAGS.md). Closed-source listings must identify what could not be independently inspected; commercial listings must visibly identify paid access.

Follow [List a Jev-powered app](../../../CONTRIBUTING.md#list-a-jev-powered-app) and the [project-page template](../../PROJECT_TEMPLATE.md), or [open an app suggestion](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml). App pages live in this folder, one full page per app.
