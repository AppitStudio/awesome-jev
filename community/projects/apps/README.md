# Apps powered by Jev

[All projects](../README.md) · [Tools and integrations](../tools/README.md) · [Share your app](../../../CONTRIBUTING.md#list-a-jev-powered-app)

Discover applications that use Jev to power a real user workflow. Each app has its own full page explaining what it does, how to access it, and where Jev fits. Hosted products and source-built apps are both welcome; other models may power additional features.

Read the [tag guide](../../APP_TAGS.md): **Open source** describes source licensing; **Commercial** marks a paid offering. Both can apply to the same app. Closed-source products are welcome with public Jev evidence and a clear source-review disclosure. Pricing unknowns stay visible.

## Web apps

### 1 Million Emojis

`Open source` · `Free` · `BYOK`

Shared 1,000×1,000 emoji canvas where humans paint and TypeSafe Jev paints alongside them from local stroke context.

**Access:** try [chriswijnia.com/lab/emoji](https://chriswijnia.com/lab/emoji) (no account) or clone the [MIT source](https://github.com/cwdx/1-million-emojis). No app purchase fee; hosted Jev strokes use the site path; self-host needs a TypeSafe key. Source inspected; live paint not run on the review host.

[Try 1 Million Emojis](https://chriswijnia.com/lab/emoji) · [Full 1 Million Emojis guide](1-million-emojis.md) · [Source](https://github.com/cwdx/1-million-emojis)

### AI;DR

`Source available` · `Free`

Ranked daily AI-news site and digest whose importance scoring can use Jev through AnyRouter, with a chat-model rubric as backup.

**Jev's role:** Jev is one importance-scoring path for ranking stories; a chat-model rubric is the backup.

**Platform:** Web (hosted) · Chrome extension · Telegram · RSS

**Product:** [aidr.today](https://aidr.today)

**Pricing / access:** Hosted site free to read without an account (checked 2026-10-14). Self-hosting incurs your own Cloudflare and AnyRouter/TypeSafe costs. Source inspected; live app not run on the review host.

[Full AI;DR guide](aidr.md) · [Source](https://github.com/duyet/aidr)

### Aperture (ranked reading feed)

`Open source` · `Free`

Single-user, self-hosted intelligence feed that imports Readwise Reader documents and optional public sources (Reddit, GitHub Trending, YouTube, reports, CVEs), has Jev rate each item for quality, personal utility and actionability, and shows a ranked, explainable reading queue with summaries.

**Jev's role:** Jev rates each item on the ranking rubric; Aperture orders the queue from those ratings.

**Platform:** Self-hosted on a server or VPS; use in any browser.

**Product:** [github.com/richfairhurst/aperture](https://github.com/richfairhurst/aperture)

**Pricing / access:** Free MIT source; you pay for your own Jev and summary-model calls and hosting. Checked 2026-10-20. Source inspected; live app not run on the review host.

[Full Aperture (ranked reading feed) guide](aperture-reading-feed.md) · [Source](https://github.com/richfairhurst/aperture)

### Aplausômetro

`Open source` · `Free source build` · `BYOK`

Paste a post and watch a simulated audience react with TypeSafe Jev calibrated probabilities.

**Access:** Try [aplausometro.rafaelcamillo.com.br](https://aplausometro.rafaelcamillo.com.br). Clone the [MIT source](https://github.com/rf-camillo/jev-aplausometro) and follow upstream setup. No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live install/inference not tested on the review host.

[Try Aplausômetro](https://aplausometro.rafaelcamillo.com.br) · [Full Aplausômetro guide](jev-aplausometro.md) · [Source](https://github.com/rf-camillo/jev-aplausometro)

### Apparite (jev2ui)

`Open source` · `Free source build` · `BYOK`

Local design-mock lab where TypeSafe Jev chooses information architecture and component anatomy, Gemini writes copy, and code assembles A2UI-inspired mocks painted by a DESIGN.md.

**Access:** clone the [Apache-2.0 source](https://github.com/dglazkov/jev2ui) (Node.js) with `JEV_API_KEY` / TypeSafe credentials and a Gemini key for full mock generation. No app purchase fee; provider usage is separate. Offline `npm run typecheck` and `npm run build` passed on the review host; live mock generation was not run.

[Full Apparite (jev2ui) guide](jev2ui.md) · [Source](https://github.com/dglazkov/jev2ui)

### AskJev (openconstruct)

`Open source` · `Free` · `BYOK`

Tiny static web app for yes/no questions via TypeSafe Jev Noul through OpenRouter Decisions. Key stored in browser `localStorage`; no backend. Distinct from the [askjev MCP (pZacca)](https://github.com/pZacca/askjev) MCP server.

**Access:** open or host the MIT [`index.html`](https://github.com/openconstruct/askjev) and paste an OpenRouter key. No app purchase fee; Decisions/Jev usage can incur charges. Source inspected; live OpenRouter calls not run on the review host.

[Full AskJev (openconstruct) guide](openconstruct-askjev.md) · [Source](https://github.com/openconstruct/askjev)

### Beat Jev

`Open source` · `Free source build` · `BYOK`

Penalty shootout against TypeSafe Jev on Render Workflows with Python and TypeScript examples.

**Jev's role:** Jev decides shoot/save outcomes in the match workflow.

**Platform:** Web / Render Workflows

**Product:** [github.com/ojusave/beat-jev](https://github.com/ojusave/beat-jev)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Beat Jev guide](beat-jev.md) · [Source](https://github.com/ojusave/beat-jev)

### beebots

`Open source` · `Free source build` · `BYOK`

Three AI trading bees on OKX perpetual futures race on paper by default: TypeSafe Jev makes every trade decision; plain code owns the risk layer and orders. OpenAI is used only to design bee personas and portraits.

**Access:** Clone the [MIT source](https://github.com/imikerussell/beebots) and run via Docker Compose, or follow upstream deploy docs. Bring a TypeSafe Jev key (and OpenAI key for bee design). Paper trading is the default; live exchange use is operator-controlled and not recommended as advice. No app purchase fee; provider and infra costs are separate. Source inspected; live trading and live Jev not run on the review host.

[Full beebots guide](beebots.md) · [Source](https://github.com/imikerussell/beebots)

### BOOLS (Breakout played live by Jev in the browser)

`Open source` · `Free` · `BYOK`

Browser Breakout game where a System One decision model steers the paddle: while the ball falls the page sends its state and one Choice question over eight zones, and the paddle moves to the pick; on-screen stats show latency, accuracy by distance and per-zone probabilities.

**Jev's role:** Core: every paddle move comes from the model's answer; the game never predicts the ball itself. Default model `typesafe/jev-latest` through Requesty.

**Platform:** Web, at bools.iteratory.com; or run the single `public/index.html` locally.

**Product:** [bools.iteratory.com](https://bools.iteratory.com)

**Pricing / access:** Open source (MIT); free to play. Decisions are billed to your own Requesty or provider key (about 400 input tokens each, a few per second). Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full BOOLS (Breakout played live by Jev in the browser) guide](bools.md) · [Source](https://github.com/neovibrant/BOOLS)

### Bot Derby (Jev and OpenAI Decisions compete in a paper-trading experiment)

`Open source` · `Free`

Public paper-trading experiment: Ferdi (TypeSafe Jev) and Bodi (OpenAI Decisions) each get $50,000 of simulated cash, the same stock evidence and the same legal action menu for five large US stocks, and a public scoreboard tracks how their portfolios diverge.

**Jev's role:** Core: Jev is one of the two competing decision engines and picks an action from the legal menu each cycle.

**Platform:** Public web scoreboard; self-hosted engine from source.

**Product:** [botderby.dayinthecountry.co](https://botderby.dayinthecountry.co)

**Pricing / access:** Open source (MIT); the public scoreboard is free to view. Running your own needs your TypeSafe, OpenAI and Alpaca paper keys. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Bot Derby (Jev and OpenAI Decisions compete in a paper-trading experiment) guide](bot-derby.md) · [Source](https://github.com/Day-in-the-Country-LLC/bot-derby)

### Call Coach

`Open source` · `Free source build` · `BYOK`

Local live sales-call coach: TypeSafe Jev judges next-best actions and buying stage from transcript turns; UI applies confidence gates (mic or sample call).

**Access:** clone the [MIT source](https://github.com/ZeroGold/call-coach-ai) (Node.js ≥ 18) with `TYPESAFE_API_KEY` and run `node server.mjs` → `http://localhost:3000`. No app purchase fee; TypeSafe usage is separate. Optional Electron overlay not required for the web demo. `node --check server.mjs` clean on the review host; live mic/TypeSafe not run.

[Full Call Coach guide](call-coach-ai.md) · [Source](https://github.com/ZeroGold/call-coach-ai)

### ChatJev by JamesANZ (ask Jev to judge a document or web lookup in plain language)

`Open source` · `Free source build`

Web app where you upload a document or ask about the web: a fast LLM turns your question into Jev yes/no, choice or score judgments, can attach web excerpts as evidence, and then restates only Jev's numbers, with a verdict card showing each judgment.

**Jev's role:** Core: every verdict comes from Jev; the LLM only writes the questions and restates the numbers.

**Platform:** Web; hosted demo plus self-hosting from source.

**Product:** [chatjev.vercel.app](https://chatjev.vercel.app)

**Pricing / access:** Open source (MIT); free source build with your own keys. A hosted demo is at chatjev.vercel.app (reachable 2026-10-24; access terms not verified). Source inspected; live app not run on the review host.

[Full ChatJev by JamesANZ (ask Jev to judge a document or web lookup in plain language) guide](chatjev-jamesanz.md) · [Source](https://github.com/JamesANZ/ChatJev)

### ChatJevPT

`Open source` · `Free source build` · `BYOK`

Chat app that makes TypeSafe Jev 'generate' an answer one character at a time by asking the same choice question over and over (next character or END), shows each letter's top-five probabilities, lets Jev grade its own answer, and meters cost; several 'model levels' compare naive and fuller pipelines.

**Access:** clone the [MIT source](https://github.com/samkoosh/ChatJevPT) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full ChatJevPT guide](chatjevpt.md) · [Source](https://github.com/samkoosh/ChatJevPT)

### Cheese Toast

`Open source` · `Free`

Jim Bumgardner's teapot-in-space arcade game ported to JavaScript and canvas; TypeSafe Jev moderates new high-score names and can play the game as a bot.

**Jev's role:** Jev checks new score-table names for PG-13 compliance (moderator override available) and, as an optional bot policy, reads a symbolic game view and picks controls.

**Platform:** Web (play at ct.krazydad.com; self-host with Python score server)

**Product:** [ct.krazydad.com](https://ct.krazydad.com)

**Pricing / access:** Free to play online; self-hosting the score server with Jev moderation needs your own TypeSafe key.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Try Cheese Toast](https://ct.krazydad.com) · [Full Cheese Toast guide](cheese-toast.md) · [Source](https://github.com/jbum/cheesetoast)

### Chess with Jev

`Source available` · `Free source build` · `BYOK`

Browser chess where your opponent is TypeSafe Jev: every move is a short chain of choice questions (focus, piece, destination) whose options are the legal moves, so illegal moves cannot be expressed; you can read each answer chain and rewrite the questions in an in-app workflow editor.

**Access:** clone the [No LICENSE source](https://github.com/vlaier/chessWithJev) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Chess with Jev guide](chess-with-jev.md) · [Source](https://github.com/vlaier/chessWithJev)

### Clean Code Review

`Open source` · `Free source build` · `BYOK`

Hosted and source-built PR reviewer: TypeSafe Jev judges changed files against Clean Code questions; Luna writes evidence-first prose; MCP endpoint for agents.

**Access:** try [clean-code-review.vercel.app](https://clean-code-review.vercel.app) (operator budgets) or clone the [MIT source](https://github.com/frostney/clean-code-review) with Bun and provider keys. No app purchase fee; provider usage is separate. Offline `bun test`: 70 passed on the review host; live PR review not run.

[Full Clean Code Review guide](clean-code-review.md) · [Source](https://github.com/frostney/clean-code-review) · [Product homepage](https://clean-code-review.vercel.app)

### Clef homelab decision engine

`Open source` · `Free source build`

Self-hosted homelab dashboard where open Clef-flash (GGUF on a 6 GB laptop GPU) answers System One questions over llama.cpp's `/v1/systemone` endpoint — the same request shape as Jev — to triage Gmail, filter news, watch ~2,350 company job boards for internships and push matches to your phone through ntfy.

**Access:** clone the [MIT source](https://github.com/NikhileshThiru/clef) and self-host with llama.cpp and the open Clef-Flash GGUF. No fee and no TypeSafe key; local GPU required. Source inspected; not run on the review host.

[Full Clef homelab decision engine guide](clef-homelab.md) · [Source](https://github.com/NikhileshThiru/clef)

### CrawlHive

`Open source` · `Pricing unverified`

Swarm of user-owned crawlers that watch X accounts, Telegram channels and new Solana pairs for memecoin signals; TypeSafe Jev rates every crawler find before a safety scan and an optional Grok Bot review.

**Jev's role:** Jev scores each crawler find ("concrete memecoin signal worth a trader's attention?"); low-probability finds are skipped, the rest are scanned most-promising first, and Jev's look/watch/avoid take is final above 70% before Grok is called.

**Platform:** Web (Next.js) · Solana / Robinhood Chain wallets

**Product:** [crawlhive.xyz](https://crawlhive.xyz)

**Pricing / access:** Live app at crawlhive.xyz; pricing and the planned project-token mechanics are not documented as of 2026-10-13. MIT source can be self-hosted with your own OpenRouter/TypeSafe and Grok keys.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Try CrawlHive](https://crawlhive.xyz) · [Full CrawlHive guide](crawl-hive.md) · [Source](https://github.com/h100envy/crawl-hive)

### Crush Monitor

`Open source` · `Free source build` · `BYOK`

Local WeChat-style chat analyzer: TypeSafe Jev labels emotion and intent, scores affinity, and rates replies on localhost with your own key.

**Access:** clone the [MIT source](https://github.com/FerryCorleone/crush-monitor) (Node.js 22.12+) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `npm test`: 36 passed; live analysis not run on the review host.

[Full Crush Monitor guide](crush-monitor.md) · [Source](https://github.com/FerryCorleone/crush-monitor)

### Crush Monitor with Jev

`Open source` · `Free source build` · `BYOK`

MIT derivative of Crush Monitor: WeChat-style affinity analysis UI with TypeSafe Jev emotion/intent/affinity judgments, plus productized trial/account surfaces described upstream.

**Access:** clone the [MIT source](https://github.com/zhengge6/crush-monitor-with-jev) (Node.js 22.12+) and configure a TypeSafe (or compatible) key via `npm run setup`. No app purchase fee for the source build; provider/trial features billed per upstream docs. Source inspected; live analysis not run. Distinct from the original Crush Monitor listing (FerryCorleone).

[Full Crush Monitor with Jev guide](crush-monitor-with-jev.md) · [Source](https://github.com/zhengge6/crush-monitor-with-jev)

### CryptoCadence

`Open source` · `Free source build` · `BYOK`

Transparent AI-driven paper-trading and backtest platform for crypto with a calibrated TypeSafe Jev decision layer, hard risk vetoes, and an append-only journal. Simulation only.

**Jev's role:** Calibrated trade/decision judgments in `src/judgment/jev.py`.

**Platform:** Web dashboard / Python lab

**Product:** [GitHub README](https://github.com/KarelTestSpecial/crypto-trading-lab#readme)

**Pricing / access:** Free MIT source; TypeSafe key for live Jev (billed). No live exchange trading. Checked 2026-10-12.

**Access:** Run from source per README. Source inspected; app not run on the review host.

[Full CryptoCadence guide](crypto-cadence.md) · [Source](https://github.com/KarelTestSpecial/crypto-trading-lab)

### DeciFlow

`Open source` · `Free source build` · `BYOK`

Self-hosted log triage: groups log events into chunks and classifies each one as Normal, Warning, Error, Security or Other with urgency and a needs-a-ticket probability, using self-hosted Laya by default or TypeSafe Jev; batch scans, live follow and a dashboard with probabilities.

**Jev's role:** Optional engine: Jev (or Laya) classifies each log chunk by category, urgency and ticket need.

**Platform:** Linux server (Docker Compose, self-hosted)

**Product:** [github.com/call518/deciflow](https://github.com/call518/deciflow)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full DeciFlow guide](deciflow.md) · [Source](https://github.com/call518/deciflow)

### Decision Lab

`Open source` · `Free source build` · `BYOK`

Local visual System One playground for building decisions, comparing Jev, OpenJEV, and Laya, and exploring what-if evidence changes.

**Access:** Clone the [MIT source](https://github.com/Amine-LG/decision-lab); demos run without a key. Connect hosted Jev/OpenJEV or local Laya for live models. No app purchase fee; live providers may charge. Source inspected; live Jev not run.

[Full Decision Lab guide](decision-lab.md) · [Source](https://github.com/Amine-LG/decision-lab)

### Dice Chess bot (Jev)

`Open source` · `Free source build` · `BYOK`

Experimental Dice Chess webhook bot: TypeSafe Jev picks among legal turns without heuristic pre-ranking (AGPL-3.0).

- Full guide: [dicechess-bot-jev.md](dicechess-bot-jev.md)
- Source: [fortemate/dicechess-bot-jev](https://github.com/fortemate/dicechess-bot-jev)
- Access: free source build; BYOK TypeSafe/provider keys when live

### Did They Answer?

`Open source` · `Free`

Web app that scores how thoroughly the UK government engages with the petitions it answers: Jev rates each response against a published rubric, with a hand-labelled gold set split into tune and holdout to keep prompt changes honest.

**Jev's role:** Jev rates each government response against the rubric; the app stores and displays the scores.

**Platform:** Web (hosted site; self-hostable)

**Product:** [petitions.thegoated.dev/](https://petitions.thegoated.dev/)

**Pricing / access:** Free public site; MIT source if you self-host with your own OpenRouter key. Checked 2026-10-18. Source inspected; live app not run on the review host.

[Full Did They Answer? guide](did-they-answer.md) · [Source](https://github.com/TheGoatedDev/Did-They-Answer)

### Doom or Bloom

`Open source` · `Free` · `BYOK`

Free web interview that maps your AI worldview (doom↔bloom) using many TypeSafe Jev Choice/Score/Noul judgments; TypeScript owns routing and presentation.

**Access:** try [www.doom-or-bloom.com](https://www.doom-or-bloom.com) or clone the [MIT source](https://github.com/transitive-bullshit/doom-or-bloom). No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live session not run on the review host.

[Try Doom or Bloom](https://www.doom-or-bloom.com) · [Full Doom or Bloom guide](doom-or-bloom.md) · [Source](https://github.com/transitive-bullshit/doom-or-bloom)

### Dungeon of Jev

`Open source` · `Free source build` · `BYOK`

Turn-based browser dungeon crawler where Jev picks which champion to send, which form the shapeshifting boss opens with, and every enemy move, as single Choice questions.

**Jev's role:** Jev chooses champions, boss forms and every enemy move.

**Platform:** Web (author's hosted demo or self-hosted)

**Product:** [doj.blocbrain.xyz](https://doj.blocbrain.xyz)

**Pricing / access:** Free to play on the author's demo; free source build with your own TypeSafe key. Checked 2026-10-15. Source inspected; live app not run on the review host.

[Full Dungeon of Jev guide](dungeon-of-jev.md) · [Source](https://github.com/ericosg/doj)

### Elo Jev 4 Investment Ideas

`Open source` · `Free source build` · `BYOK`

Local tournament app that ranks investment ideas for further research: TypeSafe Jev judges pairwise matchups per weighted criterion and an Elo leaderboard emerges.

**Jev's role:** Jev compares two ideas at a time on each criterion prompt; the app turns outcomes into Elo ratings.

**Platform:** Web (local Node server)

**Product:** [github.com/DidierRLopes/elo-jev-4-investment-ideas#readme](https://github.com/DidierRLopes/elo-jev-4-investment-ideas#readme)

**Pricing / access:** Free MIT source; judging calls billed to your TypeSafe key.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Elo Jev 4 Investment Ideas guide](elo-jev-investment-ideas.md) · [Source](https://github.com/DidierRLopes/elo-jev-4-investment-ideas)

### enigma-jev

`Open source` · `Free` · `BYOK`

Software Enigma/Bombe pipeline: TypeSafe Jev ranks cribs and judges whether a trial decryption is German.

**Access:** try [enigma-jev.vercel.app](https://enigma-jev.vercel.app) (TypeSafe key to unlock the machine) or clone the [MIT source](https://github.com/agodoy21/enigma-jev) (Bun ≥ 1.3). No app purchase fee; TypeSafe usage is separate. Source inspected; live break not run on the review host.

[Try enigma-jev](https://enigma-jev.vercel.app) · [Full enigma-jev guide](enigma-jev.md) · [Source](https://github.com/agodoy21/enigma-jev)

### Eyedot · 点睛

`Open source` · `Freemium` · `Commercial` · `BYOK`

Turns your own study material (PDF, Word, text) into exams that grade themselves point by point: grading is decomposed into atomic checkable questions whose probabilities are combined in code, with TypeSafe Jev as the decision engine when `TYPESAFE_API_KEY` is set (general-LLM judge and a labelled lexical demo engine as fallbacks), plus cited follow-up answers and spaced-repetition review.

**Access:** use the [hosted site](https://exam.simon-zj.top) (free sign-up credits, then paid credits or your own key) or self-host the MIT [source](https://github.com/Simon-zj1/eyedot). Source inspected; hosted engine not verified.

[Full Eyedot · 点睛 guide](eyedot.md) · [Source](https://github.com/Simon-zj1/eyedot)

### Family Feud Live (multiplayer party game whose optional AI host uses Jev to judge answers)

`Open source` · `Free`

Jackbox-style multiplayer Family Feud fan game: the board runs on a TV, players join from phones by QR code, and an optional AI host writes surveys on any topic, speaks in character and judges fuzzy answers, with a local matcher first and Jev as the decision model for the guesses it cannot decide.

**Jev's role:** Optional answer judge: with the AI host on, guesses the local matcher cannot settle go to Jev, which picks the matching board answer or none.

**Platform:** Web (TV or laptop screen plus phones); self-deploy on Vercel.

**Product:** [family-feud-self.vercel.app](https://family-feud-self.vercel.app)

**Pricing / access:** Open source (MIT). The live demo is free to play; a self-deployed copy runs free with AI off. The AI host uses your own Vercel AI Gateway key and prepaid credits (BYOK for that mode); whether the public demo has the AI host on was not verified. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Family Feud Live (multiplayer party game whose optional AI host uses Jev to judge answers) guide](family-feud-live.md) · [Source](https://github.com/gocougs2020/family-feud)

### FilmHunch

`Open source` · `Free source build` · `BYOK`

Self-hostable movie finder: describe a film any way you like and TypeSafe Jev scores film cards and full profiles against your exact sentence.

**Jev's role:** Jev scores short cards for the 5,000 most-rated films plus ~300 retrieved candidates, then re-scores the top 40 on full profiles; code merges and streams results.

**Platform:** Web (self-hosted Node API + web app)

**Product:** [github.com/eduardoalba00/film-hunch#readme](https://github.com/eduardoalba00/film-hunch#readme)

**Pricing / access:** Free MIT source; upstream reports ~US$0.05 per search in TypeSafe/embedding costs on your keys (not verified here).

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full FilmHunch guide](film-hunch.md) · [Source](https://github.com/eduardoalba00/film-hunch)

### Find the Right API (Orthogonal × Jev)

`Closed source` · `Freemium` · `Commercial`

Hosted natural-language API discovery: product copy states Jev searches about 1,000 Orthogonal endpoints and returns priced matches with Orthogonal `curl` snippets.

**Jev's role:** vendor/product claim—ranks Orthogonal catalog endpoints for a described goal (implementation not inspected).

**Access:** public web UI at [findtherightapi.com](https://www.findtherightapi.com/) (search needed no signup during review). Executing matches uses Orthogonal pay-per-call ([pricing](https://docs.orthogonal.com/concepts/pricing); new accounts get $5 free credits). Closed source. Checked 2026-09-24. Launch: [X post](https://x.com/chrisspickett/status/2102855582969725198).

[Try Find the Right API](https://www.findtherightapi.com/) · [Full Find the Right API guide](find-the-right-api.md) · [Source](https://www.findtherightapi.com/)

### Finney (finance agent for hackathon directors, with Jev reviewing agent traces)

`Open source` · `Free source build` · `BYOK`

Event finance workspace for hackathon directors that keeps source evidence, budget commitments, decisions and reports together in Supabase with a Next.js front end; OpenCode and Hermes do scoped agent work, Jev asks four yes/no questions about each finished trace (unsupported completions, missing payer evidence, needless clarifications, stale links), and payments run only on Base Sepolia test funds with exact-action approvals.

**Jev's role:** Trace reviewer: completed agent traces get four Noul questions, and flagged ones queue a bounded diagnosis.

**Platform:** Web; hosted beta at finney-beta.vercel.app (sign-in required) or self-host.

**Product:** [finney-beta.vercel.app](https://finney-beta.vercel.app)

**Pricing / access:** Open source (MIT); free source build. Jev calls are billed to your Vercel AI Gateway key; Supabase and hosting are yours. Access terms for the hosted beta were not verified. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Finney (finance agent for hackathon directors, with Jev reviewing agent traces) guide](finney.md) · [Source](https://github.com/pauravhp/finney)

### Fly x Jev

`Open source` · `Free source build` · `BYOK`

Browser demo: MaleCNS fruit-fly connectome robot where TypeSafe Jev picks which descending neuron fires next.

**Access:** Clone the [MIT source](https://github.com/pasangimhana/fly-x-jev) and follow upstream setup. No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live install/inference not tested on the review host.

[Full Fly x Jev guide](fly-x-jev.md) · [Source](https://github.com/pasangimhana/fly-x-jev)

### Fotocopiatrice

`Open source` · `Free source build` · `BYOK`

Explore Italian Camera amendments: identical texts grouped in code, TypeSafe Jev judges attributes and near-duplicate pairs; static site plus reusable exports.

**Access:** open [fotocopiatrice.vercel.app](https://fotocopiatrice.vercel.app/) (committed JSON, no server key) or clone the [MIT source](https://github.com/bnistor4/fotocopiatrice) (Node.js) with `TYPESAFE_API_KEY` only to regenerate the pipeline. No app purchase fee; TypeSafe usage is separate. `tsc --noEmit` clean on the review host; live pipeline not run.

[Full Fotocopiatrice guide](fotocopiatrice.md) · [Source](https://github.com/bnistor4/fotocopiatrice) · [Product homepage](https://fotocopiatrice.vercel.app/)

### FrameFind

`Open source` · `Free`

Local Python web app that samples frames from an uploaded clip or public video URL, asks Jev image questions to find moments matching a plain-language description, and lets you play or export the matching snippets as MP4.

**Jev's role:** Core: Jev judges sampled video frames against your description and the matches become playable snippets.

**Platform:** Runs locally on macOS or Linux at `http://127.0.0.1:8765`; Windows through WSL2 only.

**Product:** [github.com/Lyadalachanchu/framefind](https://github.com/Lyadalachanchu/framefind)

**Pricing / access:** Free MIT source; you pay TypeSafe per image call, with a local spending guard (`JEV_BUDGET_USD`, default $15). Checked 2026-10-21. Source inspected; live app not run on the review host.

[Full FrameFind guide](framefind.md) · [Source](https://github.com/Lyadalachanchu/framefind)

### Goatside

`Open source` · `Free source build` · `BYOK`

Self-hosted personal finance tracker: type spending in plain words and the agent files it, with TypeSafe Jev choosing category and direction.

**Jev's role:** Code parses amount, date, split and account; Jev picks the category and money in/out, asking a one-tap question when unsure.

**Platform:** Web (self-hosted on Vercel + Turso)

**Product:** [github.com/joshxfi/goatside#readme](https://github.com/joshxfi/goatside#readme)

**Pricing / access:** Free MIT source; Vercel, Turso, AI Gateway and TypeSafe usage on your own accounts.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Goatside guide](goatside.md) · [Source](https://github.com/joshxfi/goatside)

### Hearth

`Open source` · `Free source build` · `BYOK`

Local multi-marketplace rental search (Craigslist, Facebook Marketplace, Redfin, Zillow): TypeSafe Jev chooses browser actions; the app only reads and shortlists—never messages sellers.

**Access:** clone the [MIT source](https://github.com/Nancy-Chauhan/hearth-jev-rental-search) (Python ≥ 3.12, `uv`, Chrome CDP) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `pytest`: 63 passed; live Chrome/marketplace runs not executed. Distinct from browser-use/jev-ultrafast despite a shared package folder name.

[Full Hearth guide](hearth.md) · [Source](https://github.com/Nancy-Chauhan/hearth-jev-rental-search)

### Heihua Translator

`Open source` · `Free source build` · `BYOK`

Workplace jargon (职场黑话) reader: guess first, then reveal TypeSafe Jev’s typed reading with confidence bands—including “I don’t understand.”

**Access:** run the [MIT Python stdlib server](https://github.com/casperkwok/heihua-translator) locally (`python3 server.py`) with a TypeSafe key in `.env`. No app purchase fee; TypeSafe usage separate.

[Full Heihua Translator guide](heihua-translator.md) · [Source](https://github.com/casperkwok/heihua-translator)

### Heliotrope (carbon-aware load scheduler with Jev load intake)

`Open source` · `Free source build`

Scheduler that shifts EV charging, water heating, laundry and pumps into low-carbon hours without missing deadlines, using OR-Tools; Jev turns plain-words load descriptions into typed load specs and ranks how essential each appliance is.

**Jev's role:** Classifies loads from plain words with confidence and judges appliance importance for prioritisation; numbers and schedules stay in code.

**Platform:** Self-hosted web app (Next.js front end, FastAPI backend).

**Product:** [github.com/StellarieX/Heliotrope](https://github.com/StellarieX/Heliotrope)

**Pricing / access:** Open source (MIT); free source build. Hosting and TypeSafe usage are yours. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Heliotrope (carbon-aware load scheduler with Jev load intake) guide](heliotrope.md) · [Source](https://github.com/StellarieX/Heliotrope)

### Hx

`Open source` · `Free source build` · `BYOK`

Clinical documentation aid: as a doctor types or dictates, Hx opens the checklist the note implies, ticks items against clauses copied from the text, and shows what is still undocumented—without generating clinical prose. TypeSafe Jev supplies typed judgments.

**Access:** public demo at [hx.semicoded.com](https://hx.semicoded.com) (rate/spend limited) or clone the [MIT source](https://github.com/doitrous/hx) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Postgres optional for accounts. Offline server unit tests partially passed without Postgres; live analyze not run on the review host.

[Full Hx guide](hx.md) · [Source](https://github.com/doitrous/hx) · [Product homepage](https://hx.semicoded.com)

### Hémicycle

`Open source` · `Free source build` · `BYOK`

French civic quiz comparing your answers on real National Assembly votes with each parliamentary group; the nightly pipeline uses an LLM to draft neutral cards and TypeSafe Jev to classify and check them.

**Jev's role:** Jev classifies each vote's category and scores neutrality (0–5) and favored side on drafted summaries; humans review before the static site regenerates.

**Platform:** Web (static site generated by a Python pipeline)

**Product:** [github.com/lduf/hemicycle#readme](https://github.com/lduf/hemicycle#readme)

**Pricing / access:** Free MIT source; pipeline LLM and TypeSafe usage on your keys.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Hémicycle guide](hemicycle.md) · [Source](https://github.com/lduf/hemicycle)

### Inbox Warden

`Open source` · `Free source build` · `BYOK`

Self-hosted agent that labels and cleans Gmail / Google Workspace inboxes with company-specific labels, using Jev as the first pass into existing labels and Claude for the rest.

**Jev's role:** Jev assigns each email to an existing label as the first pass; Claude handles the remainder.

**Platform:** Self-hosted (Docker)

**Product:** [github.com/IshanVats-6/inbox-warden](https://github.com/IshanVats-6/inbox-warden)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Inbox Warden guide](inbox-warden.md) · [Source](https://github.com/IshanVats-6/inbox-warden)

### IntentSQL

`Open source` · `Free source build` · `BYOK`

Local natural-language SQLite playground: inspectable semantic decisions, typed plans, deterministic SQL, and guarded writes via TypeSafe Jev / System One.

**Access:** Clone the [MIT source](https://github.com/Amine-LG/IntentSQL) and run the local uvicorn app; bring a TypeSafe (or compatible) key for live Jev. No app purchase fee; provider usage may incur charges. Source inspected; live Jev not run.

[Full IntentSQL guide](intentsql.md) · [Source](https://github.com/Amine-LG/IntentSQL)

### Jagent (jev-agent.com)

`Closed source` · `Freemium` · `Commercial`

Independent hosted Jev playground and gateway: no-key trial runs with a compare mode, browser tools, games where Jev picks every move, and a Jev API on its own key with System One, ruleset, Decisions-format and MCP endpoints.

**Jev's role:** requests pass through the site to TypeSafe's hosted Jev API, which answers the playground questions, picks game moves and serves the API.

**Platform:** web browser; REST API and hosted MCP server.

**Product:** [jev-agent.com](https://jev-agent.com)

**Pricing / access:** shared anonymous trial of three runs; free account with 5 credits a month (1 credit = 1,000 input tokens), paid credit packs, optional bring-your-own TypeSafe key at 0 credits. Closed source; public pages reviewed 2026-10-20, implementation not inspected. Self-submitted by the operator (not affiliated with TypeSafe).

[Try Jagent](https://jev-agent.com) · [Full Jagent guide](jagent-jev-agent.md) · [Source](https://jev-agent.com)

### Jeff

`Closed source` · `Free`

Hosted bookshelf search and sort: visitors ask by mood, theme, or plot; TypeSafe Jev ranks books, articles, and newsletters on the shelf. Any visitor can upload a Goodreads CSV and publish a shelf with a link and QR code.

**Access:** Open [read.atharvashah.com](https://read.atharvashah.com) in a modern browser (phone layout works at 360px). Free for visitors—no account and no API key. Closed source (private repository). Operator pays Jev, capped at about $1/day and $5/month; past the cap search falls back to keyword matching. Checked 2026-10-04. Implementation not inspected; live ranked search not instrumented on the review host.

[Full Jeff guide](jeff.md) · [Source](https://read.atharvashah.com)

### Jev 2048

`Open source` · `Free` · `BYOK`

Instrumented 2048 web lab: every move is a TypeSafe Jev Choice (no heuristic fallback); probability, confidence, latency, and cost are shown live.

**Access:** try the [hosted demo](https://jev-2048-ultra.vercel.app) (limited free trial) or clone the [MIT source](https://github.com/ARCJ137442/jev-2048) (Node.js ≥ 20, `./start.sh`) with optional BYOK TypeSafe/OpenRouter. No app purchase fee; TypeSafe/OpenRouter usage is separate. Source inspected; live play not run on the review host.

[Try Jev 2048](https://jev-2048-ultra.vercel.app) · [Full Jev 2048 guide](jev-2048.md) · [Source](https://github.com/ARCJ137442/jev-2048)

### Jev Arena

`Open source` · `Free source build` · `BYOK`

Dockerized web arena where TypeSafe Jev faces Claude Opus 5.5 live on trading, Tetris, lead racing, and review triage—with real OpenRouter calls and on-screen costs.

**Jev's role:** Decision player on the left side of each scene (typed System One calls via OpenRouter).

**Platform:** Web (Docker)

**Product:** [GitHub README](https://github.com/AlanECE/jev-arena#readme)

**Pricing / access:** Free MIT source build; needs your OpenRouter key (usage billed). Paper trading only. Checked 2026-10-12.

**Access:** `docker compose` per README. Source inspected; app not run on the review host.

[Full Jev Arena guide](jev-arena.md) · [Source](https://github.com/AlanECE/jev-arena)

### Jev as LLM

`Open source` · `Free` · `BYOK`

Experimental web chat where TypeSafe Jev picks the next word via Choice questions, with inspectable alternatives and replay.

**Access:** open [jev-as-llm.vercel.app](https://jev-as-llm.vercel.app) for recorded examples (no key) or paste an OpenRouter key for live BYOK; or [run the MIT source](https://github.com/damienen/jev-as-llm). No app fee; live Decisions can incur charges. Source inspected; live BYOK chat not tested on the review host.

[Full Jev as LLM guide](jev-as-llm.md) · [Source](https://github.com/damienen/jev-as-llm)

### Jev Asks Until Sure

`Open source` · `Free` · `BYOK`

Twenty-questions style web game: keeps asking until TypeSafe Jev’s calibrated confidence crosses a threshold—or gives up. Hosted demo available.

**Access:** try [jev.mintan.org](https://jev.mintan.org/) or clone the [MIT source](https://github.com/mintannn/jev-asks-until-sure) (Next.js) with `TYPESAFE_API_KEY` in `.env.local`. No app purchase fee; TypeSafe usage is separate. Hosted demo HTTP 200 on the review host; live diagnose not run; upstream eslint reported react-hooks issues at review time.

[Try Jev Asks Until Sure](https://jev.mintan.org/) · [Full Jev Asks Until Sure guide](jev-asks-until-sure.md) · [Source](https://github.com/mintannn/jev-asks-until-sure)

### Jev Call Screener

`Open source` · `Free source build` · `BYOK`

Self-host a call-screening backend that classifies caller transcripts with TypeSafe Jev and forwards or rejects under a fail-open Go policy. Twilio adapter included; REST classify works without telephony.

**Access:** clone the [MIT source](https://github.com/SuchintK/jev-call-screener) (Go 1.27.1+) with `TYPESAFE_API_KEY`. No app purchase fee; Twilio/telephony minutes and TypeSafe usage are separate. Live Twilio and live Jev were not tested on the review host.

[Full Jev Call Screener guide](jev-call-screener.md) · [Source](https://github.com/SuchintK/jev-call-screener)

### Jev Cards

`Open source` · `Free`

Visual quiz game where you race Jev, TypeSafe's vision decision model, on the same picture cards: tap the right thing, pick the answer, with Sprint, Versus, Streak and live multiplayer modes and server-checked leaderboards.

**Jev's role:** Jev answers each card live from its picture, as a `choice` with probabilities or a `box` for tap-the-place cards, and its answers and times become your opponent's score.

**Platform:** Web (hosted site; self-host with Node or the included Dockerfile).

**Product:** [jev-cards.apps.sabater.io](https://jev-cards.apps.sabater.io)

**Pricing / access:** Free to play on the hosted site (checked 2026-10-19). Self-hosting is free source; you pay for your own Jev calls and hosting. Source inspected; live app not run on the review host.

[Full Jev Cards guide](jev-cards.md) · [Source](https://github.com/Jose-Sabater/jevcards)

### Jev Chess

`Open source` · `Free` · `BYOK`

One-page web app where TypeSafe Jev plays chess against OpenRouter LLMs, Stockfish, or you—with live move probabilities, clocks, and saved games (hosted key-lending demo available).

**Access:** try [jevchess.xera.ac](https://jevchess.xera.ac) (site-lent keys capped, or BYOK) or clone the [MIT source](https://github.com/choxos/jevchess) (`npm start`, Node ≥ 20.3). No app purchase fee; live games need TypeSafe/OpenRouter keys. Offline `npm test` 12 passed; live games not run on the review host.

[Try Jev Chess](https://jevchess.xera.ac) · [Full Jev Chess guide](jevchess.md) · [Source](https://github.com/choxos/jevchess)

### JEV City

`Open source` · `Free source build` · `BYOK`

Illustrated isometric city simulation where every citizen decision (routine, shelter, help, restore power…) comes from TypeSafe Jev, with the full choice distribution shown on click.

**Jev's role:** Jev chooses each citizen's next action; the simulation executes it.

**Platform:** Web (local source build)

**Product:** [github.com/WilliamJones/JEV-City](https://github.com/WilliamJones/JEV-City)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full JEV City guide](jev-city.md) · [Source](https://github.com/WilliamJones/JEV-City)

### Jev Civilization

`Open source` · `Free source build` · `BYOK`

Browser strategy game: you reshape the environment; TypeSafe Jev chooses each tribe’s next action from legal moves (mock mode without a key).

**Access:** try [thunder-monocle.env-ca.veilstreamapp.com/](https://thunder-monocle.env-ca.veilstreamapp.com/) or clone the [MIT source](https://github.com/JonesSteven/jev_civilization). No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live session not run on the review host.

[Try Jev Civilization](https://thunder-monocle.env-ca.veilstreamapp.com/) · [Full Jev Civilization guide](jev-civilization.md) · [Source](https://github.com/JonesSteven/jev_civilization)

### Jev Column Race

`Open source` · `Free source build` · `BYOK`

Race UI that labels 1,000 withheld-star app reviews: TypeSafe Jev typed questions versus a Gemini JSON lane, with free replay of recorded runs.

**Access:** try the [hosted demo](https://jev-column-race.vercel.app) (BYOK live or free replay) or clone the [MIT source](https://github.com/goodrahstar/jev-column-race) (`node server.mjs`, Node ≥ 20). No app purchase fee; live races need TypeSafe and Gemini keys. Offline verify-data/replay/byok OK; live races not run on the review host.

[Try Jev Column Race](https://jev-column-race.vercel.app) · [Full Jev Column Race guide](jev-column-race.md) · [Source](https://github.com/goodrahstar/jev-column-race)

### Jev Decision Lab

`Open source` · `Free`

Browser workbench for designing typed Jev questions from sample situations, then copying them into the TypeSafe Jev Playground.

**Access:** open [nwadmark.github.io/jev-decision-lab](https://nwadmark.github.io/jev-decision-lab/) or clone the [MIT source](https://github.com/nwadmark/jev-decision-lab). No app purchase fee; Playground runs use your TypeSafe account. Source inspected; live Playground not run on the review host.

[Try Jev Decision Lab](https://nwadmark.github.io/jev-decision-lab/) · [Full Jev Decision Lab guide](jev-decision-lab.md) · [Source](https://github.com/nwadmark/jev-decision-lab)

### Jev demos

`Open source` · `Free source build` · `BYOK`

Six local side-by-side TypeSafe Jev demos (router, triage, inbox, slop filter, title scorer, cost) with Claude/Kimi as interchangeable LLMs; simulated mode works without keys.

**Access:** clone the [MIT source](https://github.com/mayank953/Jev) (Node 22.6+) and `npm start` on localhost:3000. Optional `TYPESAFE_API_KEY` / Anthropic / Moonshot keys. No app purchase fee; provider usage is separate. Offline `npm run typecheck` passed; live UI/providers not run on the review host.

[Full Jev demos guide](jev-demos.md) · [Source](https://github.com/mayank953/Jev)

### Jev demos (mani-aiml)

`Open source` · `Free source build` · `BYOK`

Self-contained Jev/System One demo folders (fetch-then-write, Laya-vs-Jev judge, prompt-injection gate) behind Agentic Enterprise videos.

**Access:** Clone the [MIT source](https://github.com/mani-aiml/jev-demos) and follow each folder README. No app purchase fee; TypeSafe/Laya usage is separate. Distinct from [mayank953/Jev](https://github.com/mayank953/Jev). Source inspected; live demos not run on the review host.

[Full Jev demos (mani-aiml) guide](mani-aiml-jev-demos.md) · [Source](https://github.com/mani-aiml/jev-demos)

### JEV Document Classification

`Open source` · `Free source build` · `BYOK`

File a local document folder into configured categories with TypeSafe Jev (Vercel AI Gateway): local extraction, typed category/confidentiality/injection/subject choices, audit preview and undo.

**Access:** clone the [MIT source](https://github.com/Charlyhno-eng/jev-document-classification) (Node.js + npm) with a Vercel AI Gateway key for classification. No app purchase fee; provider usage is separate. Live classification was not tested on the review host.

[Full JEV Document Classification guide](jev-document-classification.md) · [Source](https://github.com/Charlyhno-eng/jev-document-classification)

### Jev Fighter

`Open source` · `Free` · `BYOK`

Stick-figure fighting game where AI decision models such as Jev 1.13 and chat LLMs fight each other, doubling as a benchmark with deterministic replays, decision logs and an Elo leaderboard.

**Jev's role:** Jev (via Opper) picks each fighter move from the game state; every decision is logged for replay and stats.

**Platform:** Web (browser); self-host with Node.js

**Product:** [jev-fighter.apps.sabater.io](https://jev-fighter.apps.sabater.io)

**Pricing / access:** Hosted demo at jev-fighter.apps.sabater.io; model matches use your Opper key (author estimate $0.001–$0.02 per classifier match); baseline matches need no key. Checked 2026-10-13.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Try Jev Fighter](https://jev-fighter.apps.sabater.io) · [Full Jev Fighter guide](jev-fighter.md) · [Source](https://github.com/Jose-Sabater/jev-fighter)

### Jev Fraud Shield

`Open source` · `Free source build` · `BYOK`

Explainable card-fraud triage demo/library: per-factor TypeSafe Jev judgments with a self-hosted dashboard (honest about prior failed iterations).

**Access:** Clone the MIT source; run locally with `TYPESAFE_API_KEY`. Open `dashboard.html` for the sample run UI. No app purchase fee; TypeSafe usage separate. Source inspected; live fraud API paths not run on the review host.

[Full Jev Fraud Shield guide](jonny5isalive5-jev-fraud-shield.md) · [Source](https://github.com/jonny5isalive5/jev-fraud-shield)

### Jev FSD

`Open source` · `Free source build` · `BYOK`

Browser driving simulator on real OpenStreetMap streets where TypeSafe Jev makes every maneuver choice, with a decision inspector and benchmark.

**Access:** run the [MIT source](https://github.com/BrendanH18/jev_fsd) with `uv` + a WebGL desktop browser. Rules driver works offline; Jev autopilot needs `TYPESAFE_API_KEY`. Research/demo only — not a real vehicle controller.

[Full Jev FSD guide](jev-fsd.md) · [Source](https://github.com/BrendanH18/jev_fsd)

### Jev Grand Prix

`Open source` · `Free source build` · `BYOK`

Local F1 race where TypeSafe Jev picks racing line and pedals; code steers, brake-by-wires, and plans the next lap from corner history.

**Access:** clone the [MIT source](https://github.com/enoyola/jev-grand-prix) (`uv run server.py`) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `server.py` AST parse OK; live race not run on the review host.

[Full Jev Grand Prix guide](jev-grand-prix.md) · [Source](https://github.com/enoyola/jev-grand-prix)

### Jev Guess Who

`Open source` · `Free source build` · `BYOK`

Server-authoritative Guess Who (human vs TypeSafe Jev) with 24 original SVG portraits, local practice without credentials, and analytics hooks.

**Access:** Clone the [MIT source](https://github.com/jevplays-games/jev-guess-who) (`npm start`, Node ≥22.13). Local practice works without credentials; live Jev needs your configured accounts. No app purchase fee; provider usage may incur charges. Source inspected; live Jev not run.

[Full Jev Guess Who guide](jev-guess-who.md) · [Source](https://github.com/jevplays-games/jev-guess-who)

### Jev Inbox Queue

`Open source` · `Free source build` · `BYOK`

Local inbox action queue: TypeSafe Jev answers seven typed questions per email thread; plain Python policy decides To do / Check these / Filtered out.

**Access:** clone the [MIT source](https://github.com/tusharck/jev-inbox-queue) (Python 3.10+, uv) with `TYPESAFE_API_KEY`; optional Gmail IMAP app password. No app purchase fee; TypeSafe usage is separate. Source inspected; live demo/IMAP/Jev not run on the review host. Distinct from Jevmail.

[Full Jev Inbox Queue guide](jev-inbox-queue.md) · [Source](https://github.com/tusharck/jev-inbox-queue)

### Jev Kitchen

`Closed source` · `Free`

Name a dish or cocktail and watch ingredient stickers rise; maker states TypeSafe Jev judges membership.

**Jev's role:** judges which stickers belong (implementation not inspected).

**Access:** free public demo, no signup — [recipe](https://jev-kitchen.vercel.app/recipe) / [cocktail](https://jev-kitchen.vercel.app/cocktail). Closed source. Checked 2026-09-23.

[Try Jev Kitchen](https://jev-kitchen.vercel.app/recipe) · [Full Jev Kitchen guide](jev-kitchen.md) · [Source](https://jev-kitchen.vercel.app)

### Jev Lab (BrendanH18)

`Open source` · `Free source build` · `BYOK`

Local interactive workbench with small demos showing TypeSafe Jev System One capabilities (playground + Workbench).

**Access:** Clone the [MIT source](https://github.com/BrendanH18/jev-lab), `uv sync --locked`, and `uv run --locked server.py` on localhost:8321. No app purchase fee; TypeSafe usage is separate. Distinct from [jammaru/jev-lab](https://github.com/jammaru/jev-lab). Source inspected; live UI not run on the review host.

[Full Jev Lab (BrendanH18) guide](brendanh18-jev-lab.md) · [Source](https://github.com/BrendanH18/jev-lab)

### Jev plays chess

`Open source` · `Free` · `BYOK`

Public chess ladder where TypeSafe Jev picks each move as a Choice over legal moves annotated with local facts (no lookahead); Maia-3 is the opponent; Stockfish eval bar is display-only.

**Access:** Watch at [jev-plays-chess.view.fast](https://jev-plays-chess.view.fast/) or clone the [GPL-2.0 source](https://github.com/dmallory42/jev-plays-chess) (`npm start` with TYPESAFE_API_KEY). Hosted watch path is free for visitors; self-host needs a TypeSafe key. Source inspected; live TypeSafe games not run on the review host.

[Full Jev plays chess guide](jev-plays-chess.md) · [Source](https://github.com/dmallory42/jev-plays-chess)

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

### Jev Situation Puzzle

`Open source` · `Free` · `BYOK`

Lateral-thinking puzzle game where TypeSafe Jev answers yes / no / irrelevant and judges story reconstructs (English and Chinese).

**Jev's role:** Jev is the live host for yes/no/irrelevant answers and for checking reconstructed truths; no fixed script.

**Platform:** Web (hosted demo or self-host)

**Product:** [puzzle.xiaobaozi.cn](https://puzzle.xiaobaozi.cn/?lang=en)

**Pricing / access:** Free GPL-3.0 source and public demo; live Jev uses the operator's TypeSafe key.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Jev Situation Puzzle guide](situation-puzzle.md) · [Source](https://github.com/ZeroTang05/Situation-Puzzle)

### Jev Social

`Open source` · `Free source build` · `BYOK`

Run local Instagram, TikTok, and LinkedIn research from a goal. Jev, through OpenRouter or an explicit loopback System One-compatible provider, chooses each read-only socai CLI operation; Chrome evidence feeds the next decision and cited reports.

**Access:** with Node.js 20+, run `npx github:socai-io/jev-social#v0.1.10 onboard`, then `npx github:socai-io/jev-social#v0.1.10`; cloning the [MIT source](https://github.com/socai-io/jev-social) remains an alternative. The default onboarding path validates a user-provided OpenRouter key and can offer the official socai installer on macOS or Windows. An explicitly configured loopback `/v1/systemone` provider can make the typed decisions without an OpenRouter key; disable optional OpenRouter report synthesis for a fully local decision/report path. The v0.1.10 process boundary launches socai with telemetry off unless the exact value `SOCAI_TELEMETRY=1` opts in. Linux users install socai from source and set `SOCAI_BIN`. A usable Chrome login is required for the selected platform. No app purchase fee; provider and platform access are separate. Live social browsing was not tested on the review host.

[Live site](https://socai-io.github.io/jev-social/) · [Full Jev Social guide](jev-social.md) · [Source](https://github.com/socai-io/jev-social)

### Jev Songwriter

`Open source` · `Free` · `BYOK`

Composable song lab: code enumerates legal musical options; TypeSafe Jev picks mode, tempo, form, chords, and notes with replayable demos.

**Access:** try [jev-songwriter.chardonn.ai](https://jev-songwriter.chardonn.ai) (static replays) or clone the [MIT source](https://github.com/beingcognitive/jev-songwriter) (Node ≥ 22.15). Live compose needs `TYPESAFE_API_KEY`; mock works offline. No app purchase fee; TypeSafe usage is separate. Offline `npm test` **32 pass** on the review host; live compose not run.

[Try Jev Songwriter](https://jev-songwriter.chardonn.ai) · [Full Jev Songwriter guide](jev-songwriter.md) · [Source](https://github.com/beingcognitive/jev-songwriter)

### Jev Studio (CarlosGuedea)

`Source available` · `Free source build` · `BYOK`

Spanish-language visual editor (React Flow + FastAPI) for building and running AI workflows where a `Jev Decision` node is the decision engine next to LLM, Python, HTTP, Condition and Output nodes; real backend execution with graph validation, decision branches and step logs, webhook / interval / cron triggers and SQLite history. Distinct from the listed *Jev Studio* CLI/MCP kit.

**Access:** clone the [source](https://github.com/CarlosGuedea/JEV-Studio) (no LICENSE file — Source available) and self-host with Docker. No app fee; real Jev nodes need your own TypeSafe API key (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full Jev Studio (CarlosGuedea) guide](carlosguedea-jev-studio.md) · [Source](https://github.com/CarlosGuedea/JEV-Studio)

### Jev Talks (chat built one Jev choice at a time)

`Open source` · `Free`

Chat experiment where a decision model writes the reply: on every step Jev picks the next character (English and Turkish letters, digits, punctuation, SPACE or STOP) or the next word from 250 common words, with an optional recheck pass.

**Jev's role:** Jev chooses every character or word of the reply and when to stop.

**Platform:** Web, live at jev-talks.vercel.app.

**Product:** [jev-talks.vercel.app](https://jev-talks.vercel.app)

**Pricing / access:** Open source (MIT); see the live site for how keys are handled. Checked 2026-10-23. Source inspected; live app not run on the review host.

[Full Jev Talks (chat built one Jev choice at a time) guide](jev-talks.md) · [Source](https://github.com/bariskisir/JevTalks)

### Jev Town

`Open source` · `Free source build` · `BYOK`

Browser AI-town simulation where TypeSafe Jev makes each agent's structured next-action choices and an LLM handles dialogue and memory.

**Access:** build the [MIT source](https://github.com/NevaMind-AI/JevTown) (Node.js 22 LTS). Needs LLM + `JEV_API_KEY` for the Jev-driven demo; proxy caps runs at 2000 model calls. The playable Jev demo currently lives on `feat/jev-demo-solarium` until merge to main. No app purchase fee; provider usage separate.

[Full Jev Town guide](jevtown.md) · [Source](https://github.com/NevaMind-AI/JevTown)

### Jev Trip

`Open source` · `Free source build` · `BYOK`

Explainable day-trip planner: LLM drafts; TypeSafe Jev screens/compares/reviews; controller owns routes, timing, and validation (offline replay demo).

**Access:** run the [MIT Next.js source](https://github.com/liaoyuhua/jev-trip) locally. Replay needs no keys; live mode needs TypeSafe, LLM, and Amap keys. No app purchase fee; provider/map usage is separate. Offline vitest 35 passed + typecheck on review host; live planning not run.

[Full Jev Trip guide](jev-trip.md) · [Source](https://github.com/liaoyuhua/jev-trip)

### Jev Voice Chat (Japanese)

`Open source` · `Free source build` · `BYOK`

Japanese voice conversation in the browser where Jev handles turn-taking (end of utterance, backchannel vs interruption, restatement vs new content) and OpenAI models handle recognition, replies and speech.

**Jev's role:** Jev decides turn-taking: when to answer, wait, continue or stop.

**Platform:** Web UI served locally on Windows

**Product:** [github.com/snowconed/jev_gpt_voice_chat_jp](https://github.com/snowconed/jev_gpt_voice_chat_jp)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Jev Voice Chat (Japanese) guide](jev-voice-chat-jp.md) · [Source](https://github.com/snowconed/jev_gpt_voice_chat_jp)

### Jev X Sentiment Analysis (jev-v8)

`Open source` · `Free source build` · `BYOK`

Self-hosted crypto decision-support web terminal: it pulls 50–1,000 recent tweets about a coin plus market data, pre-processes them statistically, and asks Jev four typed questions (trade action, sentiment, squeeze risk, catalyst) to produce a decision card. It never trades automatically.

**Access:** build the [MIT source](https://github.com/aikeluargalee-tech/jev-v8) and run locally with your own TypeSafe and TwitterAPI.io keys (both usage-billed). No app fee. Not financial advice. Source inspected; app not run on the review host.

[Full Jev X Sentiment Analysis (jev-v8) guide](jev-x-sentiment.md) · [Source](https://github.com/aikeluargalee-tech/jev-v8)

### Jev 棋馆 (Jev board games)

`Open source` · `Free source build` · `BYOK`

Browser board-game hall (Gomoku, Go 9x9, Xiangqi, chess, checkers, Chinese checkers) where TypeSafe Jev chooses moves, with a deterministic safety layer and a Cloudflare Worker + D1 record book.

**Jev's role:** Jev chooses each move from candidates; code enforces legality and safety checks.

**Platform:** Web (self-hosted or the author's deployment; source build)

**Product:** [github.com/tripodxu/board-games](https://github.com/tripodxu/board-games)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Jev 棋馆 (Jev board games) guide](jev-board-games.md) · [Source](https://github.com/tripodxu/board-games)

### jev-demofast

`Open source` · `Free source build` · `BYOK`

One sentence in, a narrated product demo video out: TypeSafe Jev drives your real product in a browser, guided by an optional index built from your source code.

**Access:** try replays at [onecentdemo.com](https://onecentdemo.com) or clone the [MIT source](https://github.com/q3learners/jev-demofast) (Python 3.12+, uv, ffmpeg, Chrome) with Cloudflare Workers AI credentials. Optional Deepgram voice is paid separately. No app purchase fee for the source build; provider usage is separate. Live Cloudflare/Deepgram demo path not run on the review host.

[Full jev-demofast guide](jev-demofast.md) · [Source](https://github.com/q3learners/jev-demofast) · [Product homepage](https://onecentdemo.com)

### jev-ercot

`Open source` · `Free source build` · `BYOK`

Texas retail electric plan shopper over the Power to Choose corpus: TypeSafe Jev classifies Electricity Facts Label spans; Next.js ranks plans by projected 12-month cost.

**Access:** Clone the MIT source under `web/`, `npm install`, run the committed static dataset. Live `/classify` needs `TYPESAFE_API_KEY` on the server. No app purchase fee; TypeSafe usage separate. Early development. Source inspected; live classify not run on the review host.

[Full jev-ercot guide](jev-ercot.md) · [Source](https://github.com/cdubiel08/jev-ercot)

### jev-face (Imjungjuna)

`Open source` · `Free source build` · `BYOK`

Browser WebGL face that reacts while you type: TypeSafe Jev judges which emotion a recipient would feel and drives 52 ARKit blendshapes. Distinct from the Java `jevface` SDK listing.

**Jev's role:** Typed emotion/intensity decisions from the draft text.

**Platform:** Web (Three.js)

**Product:** [GitHub README](https://github.com/Imjungjuna/jev-face#readme)

**Pricing / access:** Free MIT source; needs TypeSafe key (usage billed). Checked 2026-10-12.

**Access:** Static/dev server per README. Source inspected; app not run on the review host.

[Full jev-face (Imjungjuna) guide](imjungjuna-jev-face.md) · [Source](https://github.com/Imjungjuna/jev-face)

### jev-gmail-filter

`Open source` · `Free source build` · `BYOK`

Self-hosted local web UI that filters Gmail with plain-English topics using [jevfilter](https://github.com/damiensmith1/jevfilter) and TypeSafe Jev—labels, tracked items, and quiet-item flags. Distinct from Jev for Gmail / Gmail Classifier extensions.

**Access:** clone the [MIT source](https://github.com/damiensmith1/jev-gmail-filter), `uv sync`, run `uv run jev-gmail-filter ui` with your own Google OAuth client and TypeSafe key. No app purchase fee; TypeSafe usage separate. Early development. Source inspected; live Gmail/Jev not run on the review host.

[Full jev-gmail-filter guide](jev-gmail-filter.md) · [Source](https://github.com/damiensmith1/jev-gmail-filter)

### jev-leads

`Open source` · `Free source build` · `BYOK`

Multi-channel inbound lead intake (web/WhatsApp/Telegram/webhooks) buffered in SQLite WAL, qualified by OpenRouter typesafe/jev-1.13 structured decisions, then synced to Airtable with hot-reloadable per-channel configs.

**Access:** Clone the [MIT source](https://github.com/SebassContreras/jev-leads) and follow upstream setup (Node 24 LTS / Hono). Bring OpenRouter and Airtable credentials. No app purchase fee; provider usage is separate. Source inspected; live intake/inference not run on the review host.

[Full jev-leads guide](jev-leads.md) · [Source](https://github.com/SebassContreras/jev-leads)

### jev-mail (vynnlee)

`Open source` · `Free source build` · `BYOK`

Config-driven Gmail zero-inbox triage powered by TypeSafe Jev System One judgments under local policy.

**Access:** [configure and run the MIT source](https://github.com/vynnlee/jev-mail) with Gmail OAuth + TypeSafe key (`jev-mail.example.yaml`). No app purchase fee; provider/Gmail usage separate. Source inspected; live Gmail/Jev not tested. Distinct from Jevmail / Jev for Gmail / Inbox Triage.

[Full jev-mail (vynnlee) guide](vynnlee-jev-mail.md) · [Source](https://github.com/vynnlee/jev-mail)

### jev-minecraft

`Open source` · `Free` · `BYOK`

Runnable demo (Chinese docs) in an open-source Minecraft-compatible world: each step sends the bot's position, inventory, nearby blocks, task progress and available options to TypeSafe Jev, Jev picks the next action, Mineflayer executes it and the real world is checked; tasks range from collecting logs and building a pillar to a 90-block camp, and you can join the same world from a browser player page.

**Access:** build the free [MIT source](https://github.com/BHD110/jev-minecraft) and enter your own TypeSafe key. Source inspected; app not run on the review host.

[Full jev-minecraft guide](jev-minecraft.md) · [Source](https://github.com/BHD110/jev-minecraft)

### Jev/ui (jev-genui)

`Source available` · `Free source build` · `BYOK`

**Jev's role:** answers parallel Choice questions that fill a page→section→tile grammar; code maps onto shadcn/ui (no JSX from Jev).

**Access:** clone the [public source](https://github.com/claudfuen/jev-genui) with Bun and `AI_GATEWAY_API_KEY`. No app purchase fee; Gateway/TypeSafe usage is separate. **No LICENSE** at reviewed commit—not open source. Source inspected; live compose not run.

[Full Jev/ui guide](jev-genui.md) · [Source](https://github.com/claudfuen/jev-genui)

### Jevassic Park

`Open source` · `Free`

A shared, live isometric theme park where about 100 individually simulated guests pick rides, snacks and spectacles through Jev while code handles movement, queues and rides; anyone can watch at the hosted site.

**Jev's role:** Jev picks each simulated guest's next activity from the legal options.

**Platform:** Web (hosted on Vercel); self-host with Node.js

**Product:** [jevassic-park.vercel.app/](https://jevassic-park.vercel.app/)

**Pricing / access:** Free to watch; MIT source. Self-hosting uses your own Vercel AI Gateway billing. Checked 2026-10-17. Source inspected; live app not run on the review host.

[Full Jevassic Park guide](jevassic-park.md) · [Source](https://github.com/orshemtov/jevassic-park)

### Jevatar

`Open source` · `Free source build` · `BYOK`

Local companion that replies only with facial expressions: TypeSafe Jev picks one of 16 moods; blobatar morphs the face (no text replies).

**Access:** clone the [MIT source](https://github.com/AppChainAI/Jevatar) (Bun + Vite) with `TYPESAFE_API_KEY` on the server. No app purchase fee; TypeSafe usage is separate. Offline `bun test` **1 pass** on the review host; live companion session not run.

[Full Jevatar guide](jevatar.md) · [Source](https://github.com/AppChainAI/Jevatar)

### jevbar

`Open source` · `Free source build` · `BYOK`

Plain-language query box that uses TypeSafe Jev to compose screens (forms, confirmations, rankings, dashboards) from declared parts.

**Access:** use the [MIT TypeScript source](https://github.com/marshallsfolly/jevbar). Without a TypeSafe key, exact wording still applies; live intent/screen choice needs a key. No app purchase fee; provider usage separate.

[Full jevbar guide](jevbar.md) · [Source](https://github.com/marshallsfolly/jevbar)

### JevChess

`Open source` · `Free source build` · `BYOK`

Mobile-friendly 3D browser chess where TypeSafe Jev chooses among legal moves instead of writing move text.

**Jev's role:** Jev picks the next legal move from a closed option list.

**Platform:** Web browser

**Product:** [github.com/Odinachi/jevchess](https://github.com/Odinachi/jevchess)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full JevChess guide](odinachi-jevchess.md) · [Source](https://github.com/Odinachi/jevchess)

### JevEye

`Open source` · `Free source build` · `BYOK`

Browser vision probes report calibrated facts (or abstain); TypeSafe Jev plans what to look for and judges the text fact sheet—never pixels.

**Access:** clone the [MIT source](https://github.com/Adityakhalkar/JevEye) (Node.js 20+) with `TYPESAFE_API_KEY` on the server, or deploy to Vercel with that env var. No app purchase fee; TypeSafe usage is separate. Offline `npm test`: 12 passed; live image judgment not run on the review host.

[Full JevEye guide](jeveye.md) · [Source](https://github.com/Adityakhalkar/JevEye)

### Jevflix

`Open source` · `Free source build` · `BYOK`

Hybrid movie recommender: FAISS + BM25 shortlist ~4,800 films, then TypeSafe Jev parses constraints and picks one title with a confidence gate.

**Access:** clone the [MIT source](https://github.com/ArielBubis/Jevflix) and run Streamlit (`app.py`) with `TYPESAFE_API_KEY` (optional Anthropic/template generator). No app purchase fee; TypeSafe usage is separate. Offline lightweight pytest: 12 passed / 26 skipped; live recommend not run on the review host.

[Full Jevflix guide](jevflix.md) · [Source](https://github.com/ArielBubis/Jevflix)

### Jevline

`Source available` · `Free` · `BYOK`

Incident-timeline proof of concept for security analysts: start from one confirmed-malicious process and Jev scores, process by process, which other activity belongs to the same incident, producing a reviewable timeline (web portal, local portal or CLI).

**Access:** open the [hosted portal](https://jev-incident-timeline.vercel.app/) or clone the [source](https://github.com/tsale/jevline) (no LICENSE file — source available, not Open source) and run `python3 web_app.py`. Your own telemetry needs your own TypeSafe key (usage billed by TypeSafe). Source inspected; live site not exercised on the review host.

[Full Jevline guide](jevline.md) · [Source](https://github.com/tsale/jevline)

### Jevmail

`Open source` · `Free source build` · `BYOK`

Local read-only Gmail triage into Needs reply / Updates / Promos / Sales / Spam using TypeSafe Jev via the Vercel AI Gateway, with urgency and personal-mail scores plus retained corrections.

**Access:** clone and run the [MIT source](https://github.com/fazlerocks/jevmail) with pnpm, Google OAuth (Gmail API), `AI_GATEWAY_API_KEY`, and `AUTH_SECRET`. No app purchase fee; Gateway free-tier limits and Gmail quotas apply. Offline `pnpm test` skips without a Gateway key; live Gmail classification not run.

[Full Jevmail guide](jevmail.md) · [Source](https://github.com/fazlerocks/jevmail)

### Jevmail (hwong103)

`Open source` · `Free source build` · `BYOK`

Self-hostable read-only Gmail triage where TypeSafe Jev sorts mail into trays you can correct (Cloudflare Worker + D1 + React PWA).

**Jev's role:** Jev classifies messages into triage trays.

**Platform:** Self-hosted web (Cloudflare Worker + React PWA)

**Product:** [github.com/hwong103/jevmail](https://github.com/hwong103/jevmail)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Jevmail (hwong103) guide](hwong103-jevmail.md) · [Source](https://github.com/hwong103/jevmail)

### jevmdb

`Open source` · `Free source build` · `BYOK`

Find similar movies with TypeSafe Jev over IMDb/TMDB/Wikidata metadata and where-to-watch links.

- Full guide: [jevmdb.md](jevmdb.md)
- Source: [ClaudioEden/jevmdb](https://github.com/ClaudioEden/jevmdb)
- Access: free source build; BYOK TypeSafe/provider keys when live

### JevPDF

`Open source` · `Free` · `BYOK`

Ask a PDF in your own words: pdf.js extracts lines in the browser, TypeSafe Jev answers one yes/no question per line, and matching lines highlight on the page ranked by probability.

**Access:** try the [hosted app](https://jevpdf.fly.dev) (no account; on 2026-09-23 it held no server key, so meaning search needs your own TypeSafe key, while exact-text search needs none) or self-host the [MIT source](https://github.com/kylemclaren/jevpdf) with Bun and `TYPESAFE_API_KEY`. No app fee; TypeSafe usage is billed to the key's owner. Offline `bun install && bun run build` passed on the review host; live searches not run.

[Try JevPDF](https://jevpdf.fly.dev) · [Full JevPDF guide](jevpdf.md) · [Source](https://github.com/kylemclaren/jevpdf)

### Jevry

`Open source` · `Free source build` · `BYOK`

Desktop browser agent for website tasks, research, and supported games: the page offers real controls; TypeSafe Jev chooses; a separate text/vision model plans and writes.

**Access:** clone the [MIT Electron source](https://github.com/michaelswissa/jevry) (Node.js 22.12+; `npm ci && npm run dev`). Needs TypeSafe plus a planning/vision provider. No app purchase fee; provider usage is separate. Live desktop runs not executed on the review host.

[Full Jevry guide](jevry.md) · [Source](https://github.com/michaelswissa/jevry)

### JevSlop

`Open source` · `Free source build` · `BYOK`

Score note articles for AI-slop writing patterns with TypeSafe Jev (multi-axis Score plus overall Choice). Bring your own TypeSafe key on the hosted Pages app or a source build.

**Access:** open [jevslop.pages.dev](https://jevslop.pages.dev/) or build from the [MIT source](https://github.com/TKY-27/JevSlop). No app purchase fee; TypeSafe inference is separate. Live TypeSafe evaluation was not tested on the review host.

[Try JevSlop](https://jevslop.pages.dev/) · [Full JevSlop guide](jevslop.md) · [Source](https://github.com/TKY-27/JevSlop)

### JevTRPG

`Open source` · `Free` · `BYOK`

Paste a résumé or backstory and get a 1920s TRPG investigator sheet judged by TypeSafe Jev (free live site; nothing stored).

**Access:** Hosted path free for visitors; optional source build with TypeSafe key. Checked 2026-10-04. Source inspected; live paths not run on the review host.

[Try JevTRPG](https://jevtrpg.chroniclecore.com) · [Full JevTRPG guide](jevtrpg.md) · [Source](https://github.com/Zaious/JevTRPG)

### JevZero

`Open source` · `Free source build` · `BYOK`

Local Gmail inbox helper: TypeSafe Jev classifies category/priority/signals; you review exact proposed labels, then apply with verified receipts and undo. Demo mode works without keys.

**Access:** clone and run the [MIT source](https://github.com/jayozer/jevzero) with `uv run jevzero` (Python ≥ 3.12, Node.js 22+). Needs your TypeSafe key and Google OAuth loopback client for live mail; TypeSafe/Google billed separately. Offline `uv run pytest`: 62 passed on this review; live Gmail/TypeSafe not run.

[Full JevZero guide](jevzero.md) · [Source](https://github.com/jayozer/jevzero)

### Jev会計 (jev-kaikei-free)

`Open source` · `Free source build` · `BYOK`

Local Japanese bookkeeping tool (playful "demon ledger" UI) that shows receipts to Jev, which picks the account, consumption-tax class and whether it is a private expense; confident results become journal entries and the rest drop into a human review queue, exportable as CSV.

**Access:** run the [MIT source](https://github.com/USHIKUNDESUYO/jev-kaikei-free) with Python 3.10+ (`python -m jev_kaikei --mock` needs no key). Live mode needs your own TypeSafe key (usage billed by TypeSafe). Source inspected; app not run on the review host.

[Full Jev会計 (jev-kaikei-free) guide](jev-kaikei.md) · [Source](https://github.com/USHIKUNDESUYO/jev-kaikei-free)

### jizhang (self-hosted subscription and renewal tracker with optional Jev categories)

`Open source` · `Free source build` · `BYOK`

Self-hosted command center for recurring expenses: subscriptions, renewals, reminders and the decisions around them; optional per-user Jev classification picks a category when a subscription is added.

**Jev's role:** Optional: off by default; when enabled, Jev suggests a category for each new subscription and only a confident suggestion is applied.

**Platform:** Self-hosted; Docker image on GHCR.

**Product:** [github.com/torr9522/jizhang](https://github.com/torr9522/jizhang)

**Pricing / access:** Open source (GPL-3.0-or-later); free to self-host. Jev calls use each user's own TypeSafe key. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full jizhang (self-hosted subscription and renewal tracker with optional Jev categories) guide](jizhang.md) · [Source](https://github.com/torr9522/jizhang)

### job-drill

`Open source` · `Free source build` · `BYOK`

Local workplace response drill: write timed replies to scenario prompts and get Jev scoring reports.

**Jev's role:** Jev scores each written reply against the scenario and shop rules.

**Platform:** Local web (source build)

**Product:** [github.com/ceokobec-hue/job-drill](https://github.com/ceokobec-hue/job-drill)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full job-drill guide](job-drill.md) · [Source](https://github.com/ceokobec-hue/job-drill)

### LifePot

`Open source` · `Free source build` · `BYOK`

Replayable artificial-life game where Jev proposes species roles, relationships and bounded rule changes from your three answers, and validated rules (not code) drive a deterministic ecosystem.

**Jev's role:** Jev proposes ecosystem rules; code validates and executes them.

**Platform:** Web (hosted at lifepot.modepot.io or self-hosted)

**Product:** [lifepot.modepot.io](https://lifepot.modepot.io)

**Pricing / access:** Free to play on the hosted site; free source build with your own TypeSafe key. Checked 2026-10-15. Source inspected; live app not run on the review host.

[Full LifePot guide](lifepot.md) · [Source](https://github.com/tugrulguner/lifepot)

### Liminal Drift

`Open source` · `Free source build` · `BYOK`

First-person Backrooms horror prototype with TypeSafe Jev realtime scene decisions.

**Jev's role:** Jev drives realtime scene/decision generation during exploration.

**Platform:** Web (client/server)

**Product:** [github.com/susyimes/liminal-drift](https://github.com/susyimes/liminal-drift)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Liminal Drift guide](liminal-drift.md) · [Source](https://github.com/susyimes/liminal-drift)

### Liuyao

`Source available` · `Free source build` · `BYOK`

Chinese-style I Ching (六爻) site with programmatic casting plus TypeSafe Jev semantic judgment (sixyao.app; non-commercial source).

**Access:** Clone the [source](https://github.com/masonweb3/liuyao) (non-commercial terms per upstream) with a TypeSafe API key for live judgment. No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live install/inference not tested on the review host.

[Full Liuyao guide](liuyao.md) · [Source](https://github.com/masonweb3/liuyao)

### Magic Jev Ball

`Open source` · `Free`

Magic 8 Ball in the browser that doesn't pick at random: hold it, shake it, let go, and Jev picks which of the 20 classic answers fits your question, with a probability for every answer shown under the ball.

**Jev's role:** Jev chooses the answer among the 20 classic options and returns their probabilities.

**Platform:** Web, live at magic-jev.mikecann.app.

**Product:** [magic-jev.mikecann.app](https://magic-jev.mikecann.app)

**Pricing / access:** Free to use on the live site; self-hosting needs a paid Convex plan for the AI Gateway. Checked 2026-10-22. Source inspected; live app not run on the review host.

[Full Magic Jev Ball guide](magic-jev-ball.md) · [Source](https://github.com/mikecann/magic-jev-ball)

### mail-watcher

`Open source` · `Free source build` · `BYOK`

Self-hosted Cloudflare Email Worker that redacts incoming mail, lets Jev pick a per-watch category, and forwards, drops, or notifies accordingly.

**Jev's role:** Jev picks the category for each redacted email; code executes the mapped action and fallbacks.

**Platform:** Self-hosted Cloudflare Worker (source build)

**Product:** [github.com/farhaduneci/mail-watcher](https://github.com/farhaduneci/mail-watcher)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full mail-watcher guide](mail-watcher.md) · [Source](https://github.com/farhaduneci/mail-watcher)

### Mailroom

`Open source` · `Free source build` · `BYOK`

Gmail sorter with readable rules plus TypeSafe Jev typed judgments, receipts, and undo.

**Access:** Clone the [MIT source](https://github.com/Kevin-Liu-01/mailroom) and follow upstream setup with a TypeSafe/provider key when live. No app purchase fee for the source build; provider usage is separate. Source inspected; live install/inference not tested on the review host.

[Full Mailroom guide](mailroom.md) · [Source](https://github.com/Kevin-Liu-01/mailroom)

### Masroufi

`Source available` · `Free source build` · `BYOK`

**Jev's role:** typed classification of redacted bank-statement notes (category / merchant / reducibility) with confidence; human review for unsure rows.

**Access:** clone the [public source](https://github.com/wafaa-alhayek/masroufi) (Python/FastAPI); mock classifier without keys, or `CLASSIFIER_BACKEND=jev` with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. **No LICENSE** at reviewed commit—not open source. Source inspected; live classify not run.

[Full Masroufi guide](masroufi.md) · [Source](https://github.com/wafaa-alhayek/masroufi)

### Metis Suite (self-hosted mail and calendar client with an optional Jev decision model)

`Open source` · `Free source build` · `BYOK`

Self-hosted mail, calendar and drive client with an AI agent and workflows for Gmail, Outlook, Zoho or any IMAP/SMTP and CalDAV server; an optional decision model (TypeSafe's Jev by default for the `systemone` driver) labels inbox mail, gates thread summaries and powers workflow Ask and Branch steps.

**Jev's role:** Optional: each decision-model feature (inbox labels, summary gate, workflow Ask and Branch) has its own switch, all off by default; the LLM still writes text.

**Platform:** Self-hosted web app; local SQLite or Turso database.

**Product:** [github.com/trymetis/metis](https://github.com/trymetis/metis)

**Pricing / access:** Open source (AGPL-3.0); free to self-host. Decision calls use your own TypeSafe key, OpenAI key or a local server. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full Metis Suite (self-hosted mail and calendar client with an optional Jev decision model) guide](metis-suite.md) · [Source](https://github.com/trymetis/metis)

### MinusPod (self-hosted podcast ad remover with native System One support)

`Open source` · `Free source build`

Self-hosted server that transcribes podcast episodes, detects and cuts ad segments, and learns sponsor patterns from your corrections; it has a native System One adapter so Jev can run ad detection and verification.

**Jev's role:** Optional: with TypeSafe selected as the System One provider, Jev handles ad detection, verification and ad categories.

**Platform:** Self-hosted via Docker (CPU multi-arch or NVIDIA GPU image).

**Product:** [github.com/ttlequals0/MinusPod](https://github.com/ttlequals0/MinusPod)

**Pricing / access:** Open source (MIT); free to self-host. Inference uses your own provider keys. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full MinusPod (self-hosted podcast ad remover with native System One support) guide](minuspod.md) · [Source](https://github.com/ttlequals0/MinusPod)

### Model vs Market

`Open source` · `Free` · `BYOK`

Web app where three decision models — OpenAI Decisions, TypeSafe Jev and Cloudflare Clef — read recent news (never the odds), put a probability on Polymarket and Kalshi questions, and are compared with live market prices, with a replay of how each model changed its mind article by article.

**Access:** browse the free [live demo](https://model-vs-market.vercel.app) or self-host the [MIT source](https://github.com/yorkeccak/model-vs-market) with your own provider keys. Source inspected; app not run on the review host.

[Full Model vs Market guide](model-vs-market.md) · [Source](https://github.com/yorkeccak/model-vs-market)

### Nature Lens

`Open source` · `Free source build` · `BYOK`

Upload a nature photo and Jev ranks which landscape categories are visible, picks the main subject and draws a box around any person (Jev 1.14 Box), all in one request.

**Jev's role:** Jev classifies each photo (visible categories, main subject, person + box).

**Platform:** Web (local source build or Docker)

**Product:** [github.com/JonesSteven/jevnatureimage](https://github.com/JonesSteven/jevnatureimage)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Nature Lens guide](nature-lens.md) · [Source](https://github.com/JonesSteven/jevnatureimage)

### Neon Chase

`Open source` · `Free source build` · `BYOK`

Neon-style endless runner where TypeSafe Jev can drive realtime gameplay decisions.

**Jev's role:** Jev supplies realtime gameplay decisions to the runner.

**Platform:** Web (client/server)

**Product:** [github.com/susyimes/neon-chase](https://github.com/susyimes/neon-chase)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Neon Chase guide](neon-chase.md) · [Source](https://github.com/susyimes/neon-chase)

### Notra

`Open source` · `Commercial` · `Paid`

Track how AI answers describe and position your brand. Jev judges brand sentiment and list position within a wider analytics application; other models handle scans, general judging, and drafting.

**Access:** the [hosted product](https://www.usenotra.com) requires an account and offers [paid plans](https://www.usenotra.com/pricing), checked 2026-09-19. Trial eligibility and checkout were not tested. Self-hosting requires database, authentication, and provider setup; the guide records database initialization caveats. This commercial listing is not an endorsement.

[Full Notra guide](notra.md) · [Source](https://github.com/usenotra/notra)

### open-annie

`Open source` · `Free source build` · `BYOK`

Voice-driven 3D character in the browser: GPT-Live-1 talks with you over WebRTC while TypeSafe Jev reads the live transcript and picks every face, gesture and dance (51 decisions at p50 118 ms and $0.0026 of Jev in the recorded session); lip-sync and rendering run in the browser behind a thin broker on fal serverless.

**Access:** clone the [Apache-2.0 source](https://github.com/rehan-remade/open-annie); serve the stage locally to view the preview or replay, or run the broker with your OpenAI and TypeSafe keys for live talk. Source inspected; not run on the review host.

[Full open-annie guide](open-annie.md) · [Source](https://github.com/rehan-remade/open-annie)

### Orbs

`Open source` · `Free source build` · `BYOK`

Self-hosted multi-bot chat: rooms hold people and bots, `@mentions` wake a bot, and with no mention TypeSafe Jev scores which bot should answer; a daemon on your machine runs each bot turn through your own Pi agent.

**Access:** clone the [MIT source](https://github.com/nikuscs/orbs) and run locally with Bun or deploy to your Cloudflare account. No app fee; bring your own model access through Pi and an optional TypeSafe key (usage billed by each provider). Source inspected; not run on the review host.

[Full Orbs guide](orbs.md) · [Source](https://github.com/nikuscs/orbs)

### Orphaned Films

`Open source` · `Free`

Free movie browser and player for public-domain films on archive.org (orphanedfilms.com) where Jev decided offline which TMDB film each upload really is and which films lead each collection shelf.

**Access:** use the free site at [orphanedfilms.com](https://www.orphanedfilms.com) (no account), or clone the [MIT source](https://github.com/amponce/archive-movie-browser). Visitors trigger no Jev calls; rebuilding the index uses your own OpenRouter key. Source inspected; the site is behind a Cloudflare bot check and was not loaded by the review host.

[Full Orphaned Films guide](orphaned-films.md) · [Source](https://github.com/amponce/archive-movie-browser)

### Paper Radar

`Open source` · `Free source build` · `BYOK`

Daily arXiv paper radar: TypeSafe Jev judges every new paper against plain-English interests; publish GitHub Pages + RSS (optional chat/email digests). Offline `paper-radar demo` needs no key.

**Access:** fork the [MIT source](https://github.com/Eliot5566/JEV-Paper-Radar) and enable Actions/Pages with `TYPESAFE_API_KEY` or OpenRouter, or `pip install` the CLI. No app purchase fee; provider usage is separate. Source inspected; live arXiv/Jev and author cost claims not verified on the review host. Distinct from Jev Radar (research workspace).

[Full Paper Radar guide](paper-radar.md) · [Source](https://github.com/Eliot5566/JEV-Paper-Radar)

### PaperRadar

`Open source` · `Free source build` · `BYOK`

Local web app to browse conference papers (ICML, ICLR, CVPR, NeurIPS and more), filter by research tags and export to Zotero; new tagging runs use TypeSafe Jev.

**Jev's role:** Jev applies your chosen research tags to scraped papers (with a cost estimate first); 25k saved tagging results ship with the app.

**Platform:** Web (local, `uv run research-tagger-web`)

**Product:** [github.com/eyad-al-shami/PaperRadar#readme](https://github.com/eyad-al-shami/PaperRadar#readme)

**Pricing / access:** Free MIT source; browsing bundled data needs no key; new tagging is billed to your TypeSafe key.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full PaperRadar guide](paperradar.md) · [Source](https://github.com/eyad-al-shami/PaperRadar)

### Pastewise

`Source unverified` · `Free` · `BYOK`

One paste box that recognizes JSON, JWTs, cron, stack traces, colors, and more, then morphs into the matching tool. TypeSafe Jev classifies ambiguous pastes; deterministic helpers format and decode.

**Access:** try [pastewise.vercel.app](https://pastewise.vercel.app) (HTTP 200 on review; limits unchecked) or clone the [public source](https://github.com/Nuu-maan/pastewise) with Bun; optional `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. **No LICENSE** at reviewed commit—not open source. Source inspected; live demo/Jev not run. Distinct from JevPaste and Shapeshift.

[Try Pastewise](https://pastewise.vercel.app) · [Full Pastewise guide](pastewise.md) · [Source](https://github.com/Nuu-maan/pastewise)

### patrol-jev

`Open source` · `Free source build` · `BYOK`

Upload patrol photos and get Korean patrol-log text (or HWPX). OpenAI reads the photo; TypeSafe Jev classifies the write-up into one of four branches; code owns bundling and formatting. Manual mode works without keys.

**Access:** Clone the [MIT source](https://github.com/patrol-jev/patrol-jev) and run `npm install && npm run dev`, or try the limited [patrol.ai.kr](https://patrol.ai.kr) demo. No app purchase fee; OpenAI and TypeSafe usage are separate (BYOK). Photos stay local in manual mode. Source inspected; live UI not run on the review host.

[Full patrol-jev guide](patrol-jev.md) · [Source](https://github.com/patrol-jev/patrol-jev)

### Penny (grocery receipt review for Grocy, with Jev suggesting storage and groups)

`Open source` · `Free source build`

Self-hosted receipt review for Grocy: upload a grocery receipt PDF, OpenAI extracts the lines, Jev suggests a storage location and product group for each product (low-confidence ones stay unassigned), and confirmed purchases are imported into Grocy stock.

**Jev's role:** Suggests storage locations and product groups; extraction uses OpenAI.

**Platform:** Self-hosted web app run from source.

**Product:** [github.com/YuryFilipovich/Penny](https://github.com/YuryFilipovich/Penny)

**Pricing / access:** Open source (Apache-2.0); free source build. Uses your own OpenAI and TypeSafe keys. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Penny (grocery receipt review for Grocy, with Jev suggesting storage and groups) guide](penny-grocy.md) · [Source](https://github.com/YuryFilipovich/Penny)

### Photo Ferret

`Open source` · `Free`

Self-hosted photo gallery where Jev's image questions rate every photo on dozens of scales (how much sky, water or snow, sky drama, wildness, close-up or vista, quality), so visitors filter a static Cloudflare site with sliders, chips, a colour picker and an experimental 3D map.

**Jev's role:** Jev looks at each photo and answers the tagging questions; the gallery filters on those stored answers.

**Platform:** Self-hosted: local Node.js tool; published gallery runs in any browser.

**Product:** [stevenjonesphotography.ca](https://stevenjonesphotography.ca)

**Pricing / access:** Free MIT source; you pay for your own Jev image calls and Cloudflare hosting (free plan fits about 10,000 photos, per the README). Checked 2026-10-20. Source inspected; live app not run on the review host.

[Full Photo Ferret guide](photo-ferret.md) · [Source](https://github.com/JonesSteven/photo-ferret)

### Plasis

`Open source` · `Free source build` · `BYOK`

One text box that turns what you type into the right UI card (event, reminder, issue, checklist, bill split and more): one TypeSafe Jev call answers 15 typed intent questions in parallel while a deterministic parser reads dates and amounts; a free offline keyword classifier is the default, with measured agreement against Jev.

**Access:** clone the [MIT source](https://github.com/shreyaspangal/plasis) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Plasis guide](plasis.md) · [Source](https://github.com/shreyaspangal/plasis)

### Preguntale a Jev

`Source unverified` · `Free` · `BYOK`

No-login Spanish yes/no chat: TypeSafe Jev Choice probabilities (Sí / No / No aplica) via Vercel AI Gateway or direct TypeSafe key. Hosted demo on Vercel.

**Access:** try [jev-chat-ten.vercel.app](https://jev-chat-ten.vercel.app) or run the [source](https://github.com/dariozfold6-wez2/JEV-CHAT) on Vercel/local. Gateway auth on Vercel; optional `TYPESAFE_API_KEY`. **No LICENSE at tip**—not Open source. Source inspected; live chat not exercised as a measured eval.

[Full Preguntale a Jev guide](preguntale-a-jev.md) · [Source](https://github.com/dariozfold6-wez2/JEV-CHAT) · [Try app](https://jev-chat-ten.vercel.app)

### QuantDinger

`Open source` · `Free source build` · `BYOK`

Self-host an AI trading research and execution stack. Optional TypeSafe Jev pre-trade Choice checks gate live *entry* orders with an auditable timeline; exits bypass AI. Hosted product also available.

**Access:** clone the [Apache-2.0 source](https://github.com/OpenByteInc/QuantDinger) and run via Docker Compose; configure `JEV_API_KEY` for the decision filter. No app purchase fee for self-host; hosted SaaS at [ai.quantdinger.com](https://ai.quantdinger.com) may bill separately (not verified here). Exchange and TypeSafe usage are separate. Live trading and live Jev calls were not run on the review host.

[Live app](https://ai.quantdinger.com) · [Website](https://www.quantdinger.com) · [Full QuantDinger guide](quantdinger.md) · [Source](https://github.com/OpenByteInc/QuantDinger)

### Railroad Route

`Open source` · `Free source build` · `BYOK`

Mine-cart track puzzle: lay and turn track pieces, then write the cart a one-sentence note; TypeSafe Jev-operated switches read the sentence and decide which way to send it, and each level forbids the obvious words, so you must describe the goal indirectly (English or Portuguese).

**Access:** clone the [MIT source](https://github.com/vinicius-francozo/railroad-route) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Railroad Route guide](railroad-route.md) · [Source](https://github.com/vinicius-francozo/railroad-route)

### RefGarden

`Open source` · `Free source build` · `BYOK`

Explore a local 3D gallery of image and short-video references from a prompt. Jev chooses search phrases and highlights catalog items from titles/descriptions; Met, NASA, Cosmos, and Internet Archive supply media.

**Access:** clone and run the [MIT source](https://github.com/AlbionaHoti/refgarden#run-locally) (Node.js 22+) with a TypeSafe key for local Explore. No app purchase fee; provider usage can incur charges. Hosted preview is keyword-only (no Jev). Offline bun tests: 74 passed on the review host; live Explore not run.

[Full RefGarden guide](refgarden.md) · [Source](https://github.com/AlbionaHoti/refgarden)

### Refix

`Closed source` · `Paid` · `Commercial`

Hosted growth teammate that investigates product, search, content, and ad signals against a goal, then proposes and runs growth work with a person approving each change.

**Access:** sign up and work a goal at [refix.ai](https://www.refix.ai); review [pricing](https://www.refix.ai/pricing/) (Free launch-week plan, Pro $150/month, Enterprise). An account is required, there is no bring-your-own-key path, and paid plans apply. Closed source — implementation not inspected. Checked 2026-09-23.

[Full Refix guide](refix.md) · [Source](https://www.refix.ai) · [Product homepage](https://www.refix.ai)

### Resurface

`Open source` · `Free source build` · `BYOK`

Resume screening: LLM writes questions; TypeSafe Jev System One classifies answers.

**Access:** Clone the [MIT source](https://github.com/dolevhayut/resurface) and follow upstream setup. No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live install/inference not tested on the review host.

[Full Resurface guide](resurface.md) · [Source](https://github.com/dolevhayut/resurface)

### River Oaks

`Source available` · `Free source build` · `BYOK`

Interactive NPCs of River Oaks, Houston, with TypeSafe Jev powering NPC decisions.

**Jev's role:** Jev powers NPC decision-making in the district simulation.

**Platform:** Web

**Product:** [github.com/bunsdev/river-oaks](https://github.com/bunsdev/river-oaks)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full River Oaks guide](river-oaks.md) · [Source](https://github.com/bunsdev/river-oaks)

### say-hi

`Open source` · `Free source build` · `BYOK`

Educational demo where TypeSafe Jev (jev-1.13.0) types every reply one key at a time by choosing among keyboard options, with cost/keystroke caps and a live request inspector.

**Access:** Clone the [AGPL-3.0 source](https://github.com/huemorgan2/say-hi), `npm install`, set `TYPESAFE_API_KEY`, `npm start` ([localhost:4317](http://localhost:4317)). No app purchase fee; TypeSafe usage billed separately. Source inspected; live chat not run on the review host.

[Full say-hi guide](say-hi.md) · [Source](https://github.com/huemorgan2/say-hi)

### ScamCheck

`Open source` · `Free source build` · `BYOK`

Paste a suspicious message and get a scam verdict and risk score: one TypeSafe Jev call answers about eleven typed questions, and code can only raise the risk.

**Access:** clone the [MIT source](https://github.com/AkashNaickar/scamcheck) and run locally with Node.js 20+. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full ScamCheck guide](scamcheck.md) · [Source](https://github.com/AkashNaickar/scamcheck)

### SeeFood (food recognizer with EmbeddingGemma and Jev)

`Source available` · `Free`

Web app inspired by the hot dog app from Silicon Valley that recognizes many dishes: EmbeddingGemma 2 retrieves candidate foods from mean-centered visual prototypes, and Jev image picks among them.

**Jev's role:** Jev looks at the photo and chooses the dish among the candidates retrieved by EmbeddingGemma.

**Platform:** Web, at seefood.verygoodproduct.company.

**Product:** [seefood.verygoodproduct.company/](https://seefood.verygoodproduct.company/)

**Pricing / access:** Free live demo; no license file in the repository, so the source is viewable but not open source. Checked 2026-10-22. Source inspected; live app not run on the review host.

[Full SeeFood (food recognizer with EmbeddingGemma and Jev) guide](seefood.md) · [Source](https://github.com/krjadhav/seefood)

### seo-jev-analyzer

`Open source` · `Free source build` · `BYOK`

Measures how closely each page matches the search intent you set, using TypeSafe Jev with a calibrated noise band.

**Jev's role:** Jev judges page-to-intent relevance; the app surfaces scores for SEO review.

**Platform:** Web (self-hosted Next.js)

**Product:** [github.com/matthelam/seo-jev-analyzer#readme](https://github.com/matthelam/seo-jev-analyzer#readme)

**Pricing / access:** Free MIT source; tagging/scoring billed to your TypeSafe key.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full seo-jev-analyzer guide](seo-jev-analyzer.md) · [Source](https://github.com/matthelam/seo-jev-analyzer)

### Shapes of Stories (story arcs of books and scripts scored with Jev)

`Open source` · `Free source build`

Charts the shape of a novel, screenplay or transcript: Jev scores every passage of about 800 words on ten qualities such as fortune and tension plus events, and the fortune curve is matched to named arcs like Rags to Riches or Man in a Hole.

**Jev's role:** Core: twenty typed questions per passage (ten 0-4 scales, nine yes/no events, one choice) produce the curves.

**Platform:** Self-hosted via Docker Compose.

**Product:** [github.com/Ferrum-Citadel/shapes-of-stories](https://github.com/Ferrum-Citadel/shapes-of-stories)

**Pricing / access:** Open source (MIT); free source build. The bundled gallery of fifty public-domain works needs no key; your own texts use your TypeSafe key. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Shapes of Stories (story arcs of books and scripts scored with Jev) guide](shapes-of-stories.md) · [Source](https://github.com/Ferrum-Citadel/shapes-of-stories)

### Shapeshift

`Open source` · `Free` · `BYOK`

One text box that morphs into the right UI (event, checklist, timer, split, …) as you type: TypeSafe Jev classifies intent; deterministic parsers fill values. Offline by default; optional live Jev.

**Access:** try [shapeshiftui.vercel.app](https://shapeshiftui.vercel.app) (appears free; limits unchecked) or clone the [MIT source](https://github.com/anishfn/shapeshift) with Bun; optional `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Source inspected; live demo/Jev not run on the review host.

[Try Shapeshift](https://shapeshiftui.vercel.app) · [Full Shapeshift guide](shapeshift.md) · [Source](https://github.com/anishfn/shapeshift)

### Should I Jev?

`Open source` · `Free` · `BYOK`

Describe a feature; get a verdict—plain code, TypeSafe Jev, LLM, Jev+LLM, classical ML, or not enough—via nineteen parallel Jev questions.

**Access:** try [shouldijev.vercel.app](https://shouldijev.vercel.app) or run the [MIT source](https://github.com/yakubmurcek/should-i-jev) with `TYPESAFE_API_KEY`. No app purchase fee; provider usage separate. Source inspected; live hosted verdicts not measured.

[Full Should I Jev? guide](should-i-jev.md) · [Source](https://github.com/yakubmurcek/should-i-jev) · [Try app](https://shouldijev.vercel.app)

### SiteClarity

`Open source` · `Free` · `BYOK`

Evidence-backed AI answer-readiness page audit: TypeSafe Jev meaning judgments plus deterministic structure/language checks; every finding includes a verbatim page quote.

**Access:** use the [hosted demo](https://siteclarity.sanjay-shankar.workers.dev) (appears free; limits unchecked) or self-host the [MIT source](https://github.com/sanjuacodez/siteclarity) with your own System One / Workers AI keys. Source inspected; live audit not run on the review host.

[Try SiteClarity](https://siteclarity.sanjay-shankar.workers.dev) · [Full SiteClarity guide](siteclarity.md) · [Source](https://github.com/sanjuacodez/siteclarity)

### Slator Localization Request Readiness Inbox

`Open source` · `Free` · `BYOK`

Local inbox dashboard for enterprise translation intake: it reads unread Gmail or Outlook messages (read-only OAuth), uses Jev to identify translation requests, analyses supported source attachments, infers target languages and deadlines, and shows brief completeness, capacity and clarification points beside each email.

**Access:** run the free [Apache-2.0 source](https://github.com/alexslator/Localization-Email-Analysis) with your own TypeSafe key and mail OAuth app. Source inspected; app not run on the review host.

[Full Slator Localization Request Readiness Inbox guide](slator-localization-inbox.md) · [Source](https://github.com/alexslator/Localization-Email-Analysis)

### SmartDoc Vision (self-hosted archive and drawing review platform with Jev classifiers)

`Open source` · `Free source build` · `BYOK`

Chinese-language self-hosted review platform for archives, drawings, scans and text: a Go and Gin backend with MySQL and Redis and a Vue 3 admin console run configurable, traceable review pipelines on general LLMs and on Jev Choice and Noul classifiers, with model failover, circuit breaking and token accounting.

**Jev's role:** Optional: Jev is one of two provider kinds; review configurations can use Jev Choice and Noul questions for classification, beside general LLMs.

**Platform:** Self-hosted with Docker Compose or a single Go binary that serves the admin console.

**Product:** [github.com/ImYoyoData/smart-doc-vision](https://github.com/ImYoyoData/smart-doc-vision)

**Pricing / access:** Open source (MIT); free source build. You host MySQL and Redis and supply provider keys. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full SmartDoc Vision (self-hosted archive and drawing review platform with Jev classifiers) guide](smartdoc-vision.md) · [Source](https://github.com/ImYoyoData/smart-doc-vision)

### Snake × Jev

`Source available` · `Free source build` · `BYOK`

Browser Snake played by TypeSafe Jev with a live panel of every call — the state sent, the one choice question asked and Jev's probabilities; code only describes what the snake sees and where the food is, shuffles option order each turn and never overrides Jev's move. Distinct from the listed *jev plays snake*.

**Access:** clone the [source](https://github.com/michaelmld/snake-jev) (no LICENSE file — Source available) and run locally. No app fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full Snake × Jev guide](snake-jev.md) · [Source](https://github.com/michaelmld/snake-jev)

### Stack4That

`Open source` · `Free source build` · `BYOK`

Describe what you are building in plain language; TypeSafe Jev assembles a coherent technology stack architecture.

**Jev's role:** Jev decides among stack options to produce an architecture you can review.

**Platform:** Web (self-hosted)

**Product:** [github.com/MoRohn/stack4that#readme](https://github.com/MoRohn/stack4that#readme)

**Pricing / access:** Free MIT source; decisions billed to your TypeSafe key.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Stack4That guide](stack4that.md) · [Source](https://github.com/MoRohn/stack4that)

### Surge Desk

`Source available` · `Free` · `BYOK`

Hackathon demo for 911 surges: each call transcript (multilingual, with location) gets six typed TypeSafe Jev questions in one request — same emergency as an open incident?, what the call adds, severity, life threat — so code can merge duplicates, keep new life-safety facts, split hidden emergencies and rank P1–P4, asking the supervisor when Jev is under 70% sure; nothing is dispatched without human approval.

**Access:** open the [live demo](https://rapid-response-command.vercel.app/911) or clone the [source](https://github.com/valensangui8/surge-desk) (no LICENSE file — Source available). Free demo; self-hosting with Jev needs your own TypeSafe key. Source inspected; not run on the review host.

[Full Surge Desk guide](surge-desk.md) · [Source](https://github.com/valensangui8/surge-desk)

### talktojev (Jev Prime)

`Open source` · `Free` · `BYOK`

Research/demo web chatbot with no LLM in the loop: TypeSafe Jev picks every word via OpenRouter Decisions (Choice), with confidence-driven lookahead. Free hosted communal budget or BYOK.

**Access:** open [talktojev.com](https://talktojev.com) (free communal limits) or run the [MIT source](https://github.com/xucian/talktojev) with an OpenRouter key. No app purchase fee; OpenRouter/Jev usage is separate. Source inspected; live hosted chat not measured on the review host. Community submission #533.

[Try talktojev](https://talktojev.com) · [Full talktojev guide](talktojev.md) · [Source](https://github.com/xucian/talktojev)

### Tavli

`Open source` · `Free source build` · `BYOK`

Play Tavli (Greek backgammon / Portes) against TypeSafe Jev via OpenRouter; includes a tutorial on building with typed decision models.

**Access:** Try [tavli.dimi.diy](https://tavli.dimi.diy) or clone the [MIT source](https://github.com/DimisCodes/tavli). Live games need OpenRouter/TypeSafe access. No app purchase fee; provider usage may incur charges. Source inspected; live play not run on the review host.

[Full Tavli guide](tavli.md) · [Source](https://github.com/DimisCodes/tavli)

### Tessmora (MMA-RAG)

`Source available` · `Free source build` · `BYOK`

Tessmora (Chinese docs): self-hosted omni-modal agentic retrieval platform for documents, images, audio and video, with opt-in TypeSafe Jev semantic judgment for a simple-question intent fast path, choice reranking and citation-support diagnostics.

**Access:** clone the [source](https://github.com/Champ-X/MMA-RAG) (no LICENSE file — source available, not Open source) and self-host with Docker Compose. No app fee; bring your own model keys and an optional TypeSafe key (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full Tessmora (MMA-RAG) guide](tessmora.md) · [Source](https://github.com/Champ-X/MMA-RAG)

### tg-crush

`Open source` · `Free source build` · `BYOK`

Local real-time Telegram coach: TypeSafe Jev judges partner messages and your drafts (quality + timing) before send on localhost.

**Access:** clone the [MIT source](https://github.com/BrickerP/tg-crush) (Node.js ≥ 22.12) with `TYPESAFE_API_KEY` and Telegram API id/hash. No app purchase fee; TypeSafe usage is separate. Offline `npm run check` clean; live smoke/Telegram not run on the review host.

[Full tg-crush guide](tg-crush.md) · [Source](https://github.com/BrickerP/tg-crush)

### THE SWARM

`Open source` · `Free source build` · `BYOK`

WebGL swarm of 1,000 light particles whose strategy (flee, attack, protect, split, regroup) is chosen live by TypeSafe Jev every 1.5 seconds or on events, while local rules move each particle.

**Jev's role:** Jev picks the swarm's strategy in real time.

**Platform:** Web (local source build)

**Product:** [github.com/machine1986/the-swarm](https://github.com/machine1986/the-swarm)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full THE SWARM guide](the-swarm.md) · [Source](https://github.com/machine1986/the-swarm)

### Toru (recording infrastructure for coding agents, with optional Jev browser navigation)

`Open source` · `Commercial` · `Freemium` · `BYOK`

MCP recorder that lets Claude Code, Cursor, Codex and other agents record product demos, changelog GIFs and bug repros in your signed-in Chrome or on your Mac, renders them with your brand and checks each take; optional server-side Jev navigation picks browser operations and targets for a goal.

**Jev's role:** Optional: with a TypeSafe key, Jev answers the operation and target questions for server-side navigation; manual MCP browser controls work without it, and Toru adds no model of its own otherwise.

**Platform:** Hosted at toru.tools (limited public beta) with Toru for Chrome and Toru for Mac; source on GitHub.

**Product:** [toru.tools](https://toru.tools)

**Pricing / access:** Hosted: Free (10 credits a month), Creator $19/month and Studio $49/month per [toru.tools/pricing](https://toru.tools/pricing); checkout after beta admission. Self-host under MIT. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full Toru (recording infrastructure for coding agents, with optional Jev browser navigation) guide](toru.md) · [Source](https://github.com/alifoo/toru)

### ToS Watch

`Open source` · `Free source build` · `BYOK`

Email alerts when a company's data practices change: Open Terms Archive history, TypeSafe Jev classification, static site, and Cloudflare Worker.

**Access:** public site [tos.watch](https://tos.watch); self-host the [Apache-2.0 source](https://github.com/watthem/tos-watch). Classification needs a TypeSafe key; Worker path needs Cloudflare credentials. No app purchase fee for the source; provider usage separate.

[Full ToS Watch guide](tos-watch.md) · [Source](https://github.com/watthem/tos-watch) · [Product homepage](https://tos.watch)

### Transcript Lens

`Open source` · `Free source build` · `BYOK`

Explore YouTube transcripts by meaning with a Turkish UI: TypeSafe Jev classifies caption blocks for kind, value, and signals without rewriting the text.

**Access:** clone the [MIT source](https://github.com/sensahin/transcript-lens) (Node.js 22+) with a Vercel AI Gateway or TypeSafe key for analysis. No app purchase fee; provider usage is separate. Keyless mode still opens/pastes/exports sample text. Live analysis was not tested on the review host.

[Full Transcript Lens guide](transcript-lens.md) · [Source](https://github.com/sensahin/transcript-lens)

### Treg ("OpenRouter for agent tools": pay-per-call tool catalog whose tool search is judged by Jev)

`Source available` · `Paid` · `Commercial`

Hosted tool registry from Superdesign: agents use one base URL and token to call thousands of priced endpoints (SEO, social, people and company enrichment, ads, scraping, media generation) without provider accounts, plus team keys and skills; tool search sends the query and candidates to Jev in one judge request, and Jev is also offered as a catalog endpoint.

**Jev's role:** Search judge: `/catalog/find` sends the job description and recalled tools to Jev, which keeps or drops each candidate; Jev is also resold as the `typesafe.jev` endpoint.

**Platform:** Web service at treg.to with a CLI and agent skills; self-hosting for your own organisation is permitted.

**Product:** [treg.to](https://treg.to)

**Pricing / access:** Pay per call, with prices shown per endpoint on [treg.to](https://treg.to) (from about one cent per the README); new verified accounts get $1.00 of free credit. Licence: Apache-2.0 with Additional Terms that forbid offering it as a hosted service to third parties without permission — source available, not OSI open source, despite the launch post's "fully open source" wording. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Treg ("OpenRouter for agent tools": pay-per-call tool catalog whose tool search is judged by Jev) guide](treg.md) · [Source](https://github.com/superdesigndev/treg)

### undertone

`Source available` · `Free source build` · `BYOK`

A text box that reads how your draft sounds before you send: TypeSafe Jev scores tone, flags, urgency, formality, and boss-safety.

**Access:** open [undertone-app.vercel.app](https://undertone-app.vercel.app) or build the [source](https://github.com/Nuu-maan/undertone) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage separate. **No LICENSE** at tip—not Open source. Source inspected; live typing not run.

[Full undertone guide](undertone.md) · [Source](https://github.com/Nuu-maan/undertone) · [Try app](https://undertone-app.vercel.app)

### UtilityPot

`Open source` · `Free`

Free web utilities for messy data, shared text, diagrams and planning: browser-local CSV/JSON conversion, date cleanup and meeting-time finder, plus three bounded Jev tools for custom entity extraction, text-to-Mermaid flowcharts and finding the exact paragraphs on a webpage that answer a question.

**Jev's role:** Jev answers bounded typed questions; code validates offsets and runs the operation.

**Platform:** Web (hosted; self-hostable)

**Product:** [utilitypot.modepot.io/](https://utilitypot.modepot.io/)

**Pricing / access:** Free hosted app, no signup (per the project README). Self-hosting needs your own TypeSafe key. Checked 2026-10-17. Source inspected; live app not run on the review host.

[Full UtilityPot guide](utilitypot.md) · [Source](https://github.com/tugrulguner/utilitypot)

### Varina

`Source available` · `Free source build` · `BYOK`

Chinese-language multi-seat AI design-exploration workbench (local web UI + CLI) where an optional TypeSafe Jev post-gate decides START or ASK — whether a finished answer merits deeper multi-seat exploration — before any extra model spend; Jev never writes answers.

**Access:** clone the [source](https://github.com/deillusion/Aha-Engine) (Business Source License 1.1 — source available, production use allowed under a revenue cap; read the terms) and run locally. Requires your own model keys; the optional Jev gate uses your own TypeSafe key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Varina guide](varina.md) · [Source](https://github.com/deillusion/Aha-Engine)

### VerdictKit

`Closed source` · `Freemium` · `Commercial`

Independent hosted Jev playground and field guide: build Choice, Score, or Noul questions over your text or JSON and inspect typed responses; demo outputs are clearly labelled.

**Access:** use [verdictkit.com](https://verdictkit.com). [Pricing](https://verdictkit.com/pricing): two free live runs per UTC day without signup, five with Google sign-in, plus paid Run Pack, Pro, and Batch plans (checked 2026-10-11). Closed source — implementation not inspected; self-submitted by the operator. Live runs not executed on the review host. Not an endorsement.

[Full VerdictKit guide](verdictkit.md) · [Product homepage](https://verdictkit.com)

### Vicaura

`Closed source` · `Pricing unverified`

Hosted product-to-markdown tool: turn a product URL or description into a markdown repo of features, ICP, messaging, and pricing strategy for coding agents. Vendor states the product is powered by Jev.

**Access:** use [vicaura.com](https://vicaura.com). No public pricing page found (checked 2026-09-22); [Terms](https://vicaura.com/terms-privacy) mention guest searches and possible Stripe-billed plans. Closed source — implementation not inspected; Jev evidence is the author's [X post](https://x.com/mmmikhaeel/status/2102105486501822826). Live generate not run. Not an endorsement.

[Full Vicaura guide](vicaura.md) · [Source](https://vicaura.com) · [Product homepage](https://vicaura.com)

### Vonage Video API x Jev support demo

`Open source` · `Free source build` · `BYOK`

Vonage Community demo where Jev reads a customer's chat messages for sentiment and frustration and escalates to a live Vonage video call with a human agent.

**Jev's role:** Jev scores frustration per message; code decides when to escalate to video.

**Platform:** Web (self-hosted Node.js demo)

**Product:** [github.com/Vonage-Community/demo-video-javascript-jev-starter](https://github.com/Vonage-Community/demo-video-javascript-jev-starter)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Vonage Video API x Jev support demo guide](vonage-video-jev-starter.md) · [Source](https://github.com/Vonage-Community/demo-video-javascript-jev-starter)

### Watermelon

`Open source` · `Free source build` · `BYOK`

Status-update honesty auditor: TypeSafe Jev judges language while local code parses dates/slippage, then reports whether the health label matches the facts and whether escalation is warranted.

**Access:** public demo at [watermelon.shashwatchavan.com](https://watermelon.shashwatchavan.com) or clone the [MIT source](https://github.com/shashwatc12/watermelon) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `npm test`: 22 passed; live TypeSafe calls not run on the review host.

[Full Watermelon guide](watermelon.md) · [Source](https://github.com/shashwatc12/watermelon) · [Product homepage](https://watermelon.shashwatchavan.com)

### Zearch

`Open source` · `Free source build` · `BYOK`

Perplexity-style open-source UI for TypeSafe Jev: search to evidence state to typed decisions.

**Jev's role:** Jev turns search evidence into typed research decisions.

**Platform:** Self-hosted web

**Product:** [github.com/zearchcomputer/zearch](https://github.com/zearchcomputer/zearch)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Zearch guide](zearch.md) · [Source](https://github.com/zearchcomputer/zearch)

### Zéro Ping (local inbox for lead developers ranked with Jev)

`Open source` · `Free source build`

Local inbox that replaces GitHub notification emails with a ranked list of reviews, replies, PRs and sprint items; Jev ranks lists and gives each PR KPI cards such as production risk, review effort and merge readiness.

**Jev's role:** Ranks inbox lists and scores PR and issue KPIs; urgency estimated by Jev feeds the priority score.

**Platform:** Runs locally on macOS (browser UI, optional Dock app).

**Product:** [alexandredc.github.io/zero-ping/](https://alexandredc.github.io/zero-ping/)

**Pricing / access:** Open source (MIT); free source build. Jev calls use your own TypeSafe key. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Zéro Ping (local inbox for lead developers ranked with Jev) guide](zero-ping.md) · [Source](https://github.com/Alexandredc/zero-ping)

## Desktop apps

### AI Plays Pokémon (kotlinds)

`Source available` · `Free source build` · `BYOK`

Kotlin desktop app that puts an AI in front of Pokémon HeartGold on a Nintendo DS emulator: the game RAM is described as JSON, and a Jev backend picks each action from a closed list with per-option probabilities, optionally with an LLM planner in hybrid mode.

**Access:** clone the [source](https://github.com/kotlinds/ai-plays-pokemon) (no LICENSE file — source available, not Open source) and run with Gradle, or use a release build. Bring your own ROM and TypeSafe key (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full AI Plays Pokémon (kotlinds) guide](ai-plays-pokemon.md) · [Source](https://github.com/kotlinds/ai-plays-pokemon)

### AlgorithVideo (open-source desktop video clipper with optional Jev clip review)

`Open source` · `Free` · `BYOK`

Open-source Electron desktop app that turns podcasts, interviews and streams into captioned short clips rendered on your own computer; an opt-in Jev review step, through OpenRouter's Decisions API, scores candidate moments from transcript excerpts.

**Jev's role:** Optional: Jev review is off by default in automatic clipping and always on in the Review & edit workflow; it answers typed questions about each candidate clip.

**Platform:** Windows x64, macOS (Apple silicon and Intel) and Linux x64 packages on GitHub Releases (v0.1.0 at review); unsigned, macOS not notarized.

**Product:** [github.com/algorithco/algorith-video](https://github.com/algorithco/algorith-video)

**Pricing / access:** Open source (MIT); free download. AI features use your own provider keys, stored in the OS secure storage. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full AlgorithVideo (open-source desktop video clipper with optional Jev clip review) guide](algorithvideo.md) · [Source](https://github.com/algorithco/algorith-video)

### Beam (Omarchy launcher with optional Jev intent search)

`Open source` · `Free`

One-box launcher plugin for Omarchy that launches apps, runs Omarchy menu actions, calculates and converts inline, and opens web searches and URLs; with an optional Jev key it also finds actions by meaning, so typing screen warmer finds Nightlight.

**Jev's role:** Optional: when typed text does not match an action by name, Jev picks the Omarchy action you most likely mean.

**Platform:** Linux desktop running Omarchy 4, installed with `omarchy plugin add`.

**Product:** [plugins.omarchy.org/plugin.html?id=dev.reuk.beam](https://plugins.omarchy.org/plugin.html?id=dev.reuk.beam)

**Pricing / access:** Open source (MIT); free to install from the Omarchy plugin directory or GitHub. Jev intent search uses your own TypeSafe key. Checked 2026-10-23. Source inspected; live app not run on the review host.

[Full Beam (Omarchy launcher with optional Jev intent search) guide](omarchy-beam.md) · [Source](https://github.com/RohitKaushal7/omarchy-beam)

### dotpals

`Open source` · `Free` · `BYOK`

Desktop pal and notch that shows what coding agents (Claude Code, Codex and others) actually did: test results read from the output, faked passes caught, and Claude Code sent back to fix what it broke. An opt-in double-check sends unclear test runs to TypeSafe Jev (through `@typesafe-ai/sdk`) or to a local Laya model.

**Access:** install with `npx dotpals@latest setup` ([MIT source](https://github.com/Rikinshah787/dotpals)). No fee; the optional Cloud check needs your own TypeSafe API key (usage billed by TypeSafe). Source inspected; app not run on the review host.

[Full dotpals guide](dotpals.md) · [Source](https://github.com/Rikinshah787/dotpals)

### extynt (After Effects plugin and MCP server: plain-language motion design with optional Jev checks)

`Open source` · `Free`

Native After Effects plugin for macOS and Windows: describe a motion-design change in plain language, a model proposes a typed plan, and extynt validates, previews, applies it in one undo group and verifies the result; Claude Code and Codex can drive the same project over MCP, and small closed questions can optionally be answered by Jev when it is confident.

**Jev's role:** Optional decision model for small closed questions (which effect was named, is the job finished); deterministic code answers by default.

**Platform:** macOS and Windows; After Effects 25 and 26; signed installers on GitHub Releases (0.1.0, early).

**Product:** [github.com/extynt-plugin/extynt/releases](https://github.com/extynt-plugin/extynt/releases)

**Pricing / access:** Open source (MIT); signed installers are a free download. Model and optional Jev usage is billed by your providers. Checked 2026-10-27. Source inspected; live app not run on the review host.

[Full extynt (After Effects plugin and MCP server: plain-language motion design with optional Jev checks) guide](extynt.md) · [Source](https://github.com/extynt-plugin/extynt)

### Facet

`Open source` · `Free source build` · `BYOK`

Photo culling and sorting app for photographers: an AI model checks every photo against built-in and your own labels (blurry, eyes closed, the couple kissing), faces are grouped locally, and you filter and sort into folders with undo. Jev or OpenAI vision can be chosen.

**Jev's role:** Jev scores each photo against your labels and can search for people by reference faces.

**Platform:** macOS and Windows (source launchers)

**Product:** [github.com/ceelnok/facet-photo](https://github.com/ceelnok/facet-photo)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Facet guide](facet-photo.md) · [Source](https://github.com/ceelnok/facet-photo)

### Goutoujunshi Jev Chat

`Open source` · `Free source build` · `BYOK`

WeChat companion (Mac source preview + Windows preview ZIP): OCR the chat, optional TypeSafe Jev strategy judgment, ranked reply drafts—you always send.

**Access:** download [GitHub Releases](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat/releases/latest) or build the [MIT source](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat). DeepSeek (or compatible) for drafts; optional TypeSafe Jev key. No app purchase fee; provider usage separate. Windows device validation still pending upstream. Source inspected; GUI/OCR/live not run on the Linux review host.

[Full Goutoujunshi Jev Chat guide](goutoujunshi-jev-chat.md) · [Source](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat)

### Jev Companion (read-only WeChat conversation companion with typed Jev judgments)

`Open source` · `Free source build` · `BYOK`

Native macOS and Windows companion that reads the text of the current WeChat window (or pasted text) and places Jev judgment cards under each message: communication needs, next actions and conversation tension, plus optional reply drafts from a local OpenAI-compatible model; it never sends messages.

**Jev's role:** Core: Jev Noul, Choice and Score questions produce the judgment cards; an optional separate model writes reply drafts.

**Platform:** macOS (app 0.3.1) and Windows preview (0.4.1); build from source.

**Product:** [github.com/jimmy1340/jev-companion](https://github.com/jimmy1340/jev-companion)

**Pricing / access:** Open source (MIT); free source build. Jev calls use your own TypeSafe key. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full Jev Companion (read-only WeChat conversation companion with typed Jev judgments) guide](jev-companion.md) · [Source](https://github.com/jimmy1340/jev-companion)

### Jev Linux (voice desktop controller)

`Open source` · `Free source build` · `BYOK`

Voice controller for Ubuntu: local Moonshine speech recognition, a Gemini planner that splits your command into steps, and Jev choosing the desktop action for each step (open apps and sites, click, type, scroll, create notes).

**Jev's role:** Jev picks the desktop action for each planned step from a bounded set of operations.

**Platform:** Ubuntu Linux (source build)

**Product:** [github.com/musagithub1/Browser_use](https://github.com/musagithub1/Browser_use)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Jev Linux (voice desktop controller) guide](jev-linux-voice.md) · [Source](https://github.com/musagithub1/Browser_use)

### Jev Sheets (OpenHarness)

`Open source` · `Free source build` · `BYOK`

OpenHarness desktop sheet pane: TypeSafe Jev answers typed `noul` / `choice` / `score` column headers for every row, with confidence, review gates, and Question Lab wording trials.

**Access:** [download OpenHarness](https://harness.autonomous.ai/desktop) for macOS or Linux (or build the [MIT source](https://github.com/autonomous-ai/openharness)), then open the bundled Jev Sheets harness from the Store. No app purchase fee observed on the download page (checked 2026-09-24); live answers need a TypeSafe, OpenRouter, or Cloudflare key (BYOK). Offline practice works without a key (word-matching only). Source and harness README inspected; desktop install and live Jev not run on the review host. Lists **Jev Sheets only**, not other OpenHarness DSHs.

[Full Jev Sheets guide](jev-sheets.md) · [Source](https://github.com/autonomous-ai/openharness) · [Product homepage](https://harness.autonomous.ai/desktop)

### JevClean

`Open source` · `Free source build` · `BYOK`

Local IMAP mail organizer: write natural-language rules (one action each), Jev judges every message against them, and you review and confirm delete, archive, move, spam or flag actions with undo.

**Jev's role:** Jev judges each email against your natural-language rules; code gates and executes confirmed actions.

**Platform:** Desktop (macOS Apple Silicon package; source build on macOS, Windows, Linux)

**Product:** [github.com/sufferfml/JevClean](https://github.com/sufferfml/JevClean)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full JevClean guide](jevclean.md) · [Source](https://github.com/sufferfml/JevClean)

### JevDash

`Open source` · `Free source build` · `BYOK`

100% clean-room 2D platformer for benchmarking TypeSafe Jev in real-time control at 60 FPS. Mock decision engine works without keys; live path can use Vercel AI Gateway.

**Access:** Clone the [MIT source](https://github.com/Sunwood-ai-labs/jevdash) and follow README (Pygame). Mock mode needs no key; live Jev/Gateway is BYOK. No app purchase fee. Docs: [jevdash site](https://sunwood-ai-labs.github.io/jevdash/). Source inspected; live gameplay not run on the Linux review host.

[Full JevDash guide](jevdash.md) · [Source](https://github.com/Sunwood-ai-labs/jevdash)

### JEVsnap

`Open source` · `Free source build` · `BYOK`

Screenshot hotkey that blacks out secrets and personal information (API keys, tokens, emails, phone numbers, names, internal hostnames, QR codes) before the image reaches your clipboard; on-device OCR and local rules first, with optional Jev text and Box checks.

**Jev's role:** Optional Jev text and Box checks find sensitive words and regions that local rules miss.

**Platform:** macOS, Linux and Windows (source builds)

**Product:** [github.com/brainstormity/jevsnap](https://github.com/brainstormity/jevsnap)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full JEVsnap guide](jevsnap.md) · [Source](https://github.com/brainstormity/jevsnap)

### Laser (Omarchy focus mode)

`Open source` · `Free` · `BYOK`

AI focus mode for Omarchy / Hyprland on Linux: you declare a task, and Laser judges each screen against it with TypeSafe Jev (about half a second per check), escalating from a red dot to a nudge, a red screen edge and a haze over the distracting window; screenshots are OCR'd on device and only text (per privacy level) is sent.

**Access:** install the free [MIT plugin](https://github.com/iYassr/omarchy-laser) and bring your own TypeSafe key. Source inspected; app not run on the review host.

[Full Laser (Omarchy focus mode) guide](omarchy-laser.md) · [Source](https://github.com/iYassr/omarchy-laser)

### Modex

`Open source` · `Free source build` · `BYOK`

Open Codex-App–style desktop coding agent (Electron+React) driving Claude Code/Codex CLIs; optional TypeSafe Jev Auto routing picks model/effort per turn.

**Access:** Build from the [MIT source](https://github.com/TypeSafeAI/modex). No app purchase fee. Optional TypeSafe key for Auto routing (OS keychain); Claude/Codex keep their own logins/costs. Source inspected; desktop/live paths not run on the Linux review host.

[Full Modex guide](modex.md) · [Source](https://github.com/TypeSafeAI/modex)

### Nudge for Omarchy

`Open source` · `Free source build` · `BYOK`

Omarchy (Hyprland) launcher plugin: describe what you need in plain words and Jev routes it to a reviewed safe desktop operation (night light, brightness, volume, folders, settings panels, reminders, shortcut lookup) or shows a preview and manual guidance for anything else.

**Jev's role:** Jev routes a plain-language request to a command group, a command and bounded arguments.

**Platform:** Linux (Omarchy / Hyprland)

**Product:** [github.com/cozidian/omarchy-jev](https://github.com/cozidian/omarchy-jev)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Nudge for Omarchy guide](nudge-omarchy.md) · [Source](https://github.com/cozidian/omarchy-jev)

### omarchy-mouse-sacrifice

`Open source` · `Free source build` · `BYOK`

Omarchy (Hyprland) plugin: move the pointer into the bottom-right corner and a card offers up to five keyboard shortcuts that fit what is on screen, ranked by TypeSafe Jev from a list built in code (focused app, workspace windows, bar widgets, recent use, your real Hyprland binds and press counts); no screenshots or typed text are sent.

**Access:** install from the [MIT source](https://github.com/ignotas/omarchy-mouse-sacrifice) with `omarchy plugin add`. No app fee; requires your own TypeSafe key (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full omarchy-mouse-sacrifice guide](omarchy-mouse-sacrifice.md) · [Source](https://github.com/ignotas/omarchy-mouse-sacrifice)

### Scene Finder

`Free` · `Source available` · `BYOK`

Desktop app for finding a moment in a movie you can only describe: it samples frames from your MKV or MP4, asks Jev which ones match, lets you play the hits, then trim and save an MP4 clip.

**Jev's role:** Jev judges which sampled frames match your scene description.

**Platform:** macOS (Apple silicon), Windows x64, Linux x64

**Product:** [github.com/EmmyMay/scene-finder/releases](https://github.com/EmmyMay/scene-finder/releases)

**Pricing / access:** Free beta downloads; you pay your own Jev/TypeSafe usage. No open-source license on the reviewed commit. Checked 2026-10-17. Source inspected; live app not run on the review host.

[Full Scene Finder guide](scene-finder.md) · [Source](https://github.com/EmmyMay/scene-finder)

### Stillwatch

`Open source` · `Free source build` · `BYOK`

Notification guardian that saves every notification locally and, in AI mode, uses TypeSafe Jev (via NanoGPT's Decisions API) to decide what needs you now with persistent modals.

**Jev's role:** Typed Jev choices classify each new notification's importance and severity; code handles cooldowns, history and cross-device sync.

**Platform:** Linux desktop (Python, GTK 4/libadwaita) · Android companion (early alpha)

**Product:** [github.com/difflabai/stillwatch#readme](https://github.com/difflabai/stillwatch#readme)

**Pricing / access:** Free MIT source; AI mode bills NanoGPT/TypeSafe usage to your key.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Stillwatch guide](stillwatch.md) · [Source](https://github.com/difflabai/stillwatch)

### Synax

`Open source` · `Free` · `BYOK`

Open-source local workspace for coding agents and codebase docs (agent chats, files, diffs, terminal) whose Electron app offers optional Jev-assisted Computer Use: with a TypeSafe key (or OpenRouter), Jev picks bounded semantic actions for the app-hosted Cua Driver instead of the default Direct Cua strategy.

**Access:** download a free desktop build from [GitHub Releases](https://github.com/coldmint9/Synax/releases/latest) or build the [Apache-2.0 source](https://github.com/coldmint9/Synax). Jev-assisted Computer Use is opt-in and uses your own TypeSafe or OpenRouter key. Source inspected; app not run on the review host.

[Full Synax guide](synax.md) · [Source](https://github.com/coldmint9/Synax)

### Text-To-VRMA

`Open source` · `Free` · `BYOK`

Text-to-motion app for VRM avatars: type a line such as "jump for joy" and it generates a `.vrma` animation with facial expressions, previews it on your VRM model, and exports VRMA, GIF or video. Since v1.1.9 an optional Jev pass analyses the text's emotion, gaze, energy and tempo and feeds those typed results into motion generation.

**Access:** free Windows portable zip on [Releases](https://github.com/Kirakun0328/text-to-vrma/releases/latest) or build the [MIT source](https://github.com/Kirakun0328/text-to-vrma) (`npm run dev`). Optional Jev analysis needs your own TypeSafe key (usage billed by TypeSafe); motion via local ARDY or your own LLM key. Source inspected; app not run on the review host.

[Full Text-To-VRMA guide](text-to-vrma.md) · [Source](https://github.com/Kirakun0328/text-to-vrma)

### Warren Duffer

`Open source` · `Free source build` · `BYOK`

Intraday Nifty-50 trading bot where TypeSafe Jev ranks names and code sizes/stops live broker orders (experimental; real-money risk).

**Access:** Free source build; BYOK TypeSafe/Vercel AI Gateway + broker API. Places real orders—no paper mode. Checked 2026-10-04. Source inspected; live paths not run on the review host.

[Full Warren Duffer guide](warrenduffer.md) · [Source](https://github.com/arimanyus/warrenduffer)

## macOS apps

### AI Model Picker

`Open source` · `Free`

Native macOS assistant: describe a task, review rule-ranked app/model/effort choices, and open or prepare the task in the client you already use; optional TypeSafe Jev classification.

**Jev's role:** Optional Jev classification of the task description feeds the ranking; offline rules work without it.

**Platform:** macOS (alpha, ad hoc signed, not notarized)

**Product:** [github.com/Gavinluo19/ai-model-picker/releases](https://github.com/Gavinluo19/ai-model-picker/releases)

**Pricing / access:** Free MIT download; optional TypeSafe key for Jev classification.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full AI Model Picker guide](ai-model-picker.md) · [Source](https://github.com/Gavinluo19/ai-model-picker)

### ASO Workbench (App Store Optimization on your Mac, with Jev keyword clues)

`Source available` · `Free`

Mac app for App Store Optimization that tracks keyword ranks per country, estimates popularity and difficulty with labelled sources, writes and publishes store listings in every language, and measures what each change did; Jev answers narrow keyword questions that feed its popularity estimate.

**Jev's role:** Optional: through OpenRouter, Jev answers probability questions about each keyword (is it a brand, is it relevant) that the app uses as clues for its popularity estimate.

**Platform:** macOS 15+; free unnotarized DMG from GitHub releases, or build from source with Xcode 26.

**Product:** [github.com/mustafakendiguzel/aso-workbench](https://github.com/mustafakendiguzel/aso-workbench)

**Pricing / access:** Free download (MIT with Commons Clause: free to use, including for your own apps, but not to sell). OpenRouter usage for Jev and the AI writer is pay per use on your key. Checked 2026-10-23. Source inspected; live app not run on the review host.

[Full ASO Workbench (App Store Optimization on your Mac, with Jev keyword clues) guide](aso-workbench.md) · [Source](https://github.com/mustafakendiguzel/aso-workbench)

### Baton (notch app)

`Open source` · `Free source build` · `BYOK`

macOS notch app that pings you when a ChatGPT, Codex, Claude or Cursor chat finishes or needs you; TypeSafe Jev decides finished vs needs-you.

**Jev's role:** Jev reads each chat's latest reply and decides whether it is finished or needs your answer; without a Jev key Baton only lists chats.

**Platform:** macOS (DMG, not notarized; Sparkle updates)

**Product:** [github.com/jeanlucandre-afk/baton/releases](https://github.com/jeanlucandre-afk/baton/releases)

**Pricing / access:** Free MIT app; Jev (and optional Gemini) calls use your own keys.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Baton (notch app) guide](baton-notch.md) · [Source](https://github.com/jeanlucandre-afk/baton)

### Call Coach by Darlison (live interview checklist on macOS, ticked by Jev)

`Open source` · `Free source build`

Live checklist for interviews and discovery calls: whisper.cpp transcribes both sides on your Mac, Jev ticks off each question once it is answered, tracks which listed question you just asked and flags answers worth a follow-up, and an MCP server lets your AI add follow-ups.

**Jev's role:** Core for automatic ticking: yes/no and choice questions on recent transcript lines. Without a key you tick by hand.

**Platform:** macOS on Apple silicon; local page at localhost:4800 after running the installer.

**Product:** [github.com/ByronDarlison/call-coach](https://github.com/ByronDarlison/call-coach)

**Pricing / access:** Open source (MIT); free source build. Jev calls use your own TypeSafe key. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Call Coach by Darlison (live interview checklist on macOS, ticked by Jev) guide](byrondarlison-call-coach.md) · [Source](https://github.com/ByronDarlison/call-coach)

### Capture (sgaabdu4)

`Open source` · `Free source build` · `BYOK`

Private Mac voice diary: local Parakeet transcription, TypeSafe Jev sorting into typed buckets, then Notion after you approve.

**Access:** build the [MIT source](https://github.com/sgaabdu4/capture) on macOS. Needs TypeSafe key for sorting and Notion OAuth. Audio stays on-device for transcription. No app purchase fee; provider usage separate.

[Full Capture guide](capture.md) · [Source](https://github.com/sgaabdu4/capture)

### ChatJump

`Open source` · `Free source build` · `BYOK`

Menu-bar launcher for your AI chats: press Control-Option-Space, type what you remember, and Jev ranks open Claude, ChatGPT, Codex and Chrome chat tabs by meaning, then opens the right one.

**Jev's role:** Jev ranks your open AI chats against a remembered description and flags weak matches.

**Platform:** macOS 14 or later (source build)

**Product:** [github.com/saydus/chatjump](https://github.com/saydus/chatjump)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full ChatJump guide](chatjump.md) · [Source](https://github.com/saydus/chatjump)

### Computer Use (lite) by ajokhai (Mac computer use for any AI, with an optional Jev mode)

`Source available` · `Free` · `BYOK`

Menu bar app and native MCP server that let an AI operate the whole Mac, not just a browser: Claude, ChatGPT, Gemini, OpenRouter or a local model plans the steps, and in its Jev modes TypeSafe Jev picks the next action and element from the app's accessibility tree.

**Jev's role:** Optional: in the Vision + Jev and Jev Only modes, Jev chooses the next action, the target element and the text to type from the accessibility tree; other modes do not use Jev.

**Platform:** macOS; DMG on GitHub Releases (v0.1.15 at review), signed with a local certificate rather than a verified Developer ID.

**Product:** [github.com/ajokhai/computer-use-lite](https://github.com/ajokhai/computer-use-lite)

**Pricing / access:** Free download; public source with no license file (no open-source license granted). Provider calls use your own keys; through MCP the AI app you already use does the thinking. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full Computer Use (lite) by ajokhai (Mac computer use for any AI, with an optional Jev mode) guide](computer-use-lite.md) · [Source](https://github.com/ajokhai/computer-use-lite)

### Covan (local-first personal agent desktop app with Jev reply decisions)

`Open source` · `Free source build` · `BYOK`

Local-first personal agent desktop app with memory, tools, workspaces and scheduled tasks, where several bots can chat with you or in groups; an optional Jev strategy decides whether each bot should reply in a group or follow up, with low-confidence answers falling back to the LLM strategy.

**Jev's role:** Optional: Jev answers the speak-or-stay-quiet and follow-up decisions; text is written by the bot's chosen model.

**Platform:** macOS mainly; run from source with `./start.command`.

**Product:** [github.com/Lichas/covan](https://github.com/Lichas/covan)

**Pricing / access:** Open source (Apache-2.0); free source build. Model and Jev calls use your own keys or CLIs. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full Covan (local-first personal agent desktop app with Jev reply decisions) guide](covan.md) · [Source](https://github.com/Lichas/covan)

### Hyperclip (macOS video clipper with Jev clip scoring)

`Open source` · `Free source build`

Native SwiftUI app that turns long videos into short captioned clips on your Mac: it downloads with yt-dlp, transcribes on device, finds clips with built-in scoring, a Jev-compatible decision model or an LLM, frames the speaker and burns in word-by-word captions.

**Jev's role:** Optional: after built-in scoring shortlists spans, Jev answers typed questions about each candidate clip (hook strength, whether it stands alone, payoff) to rank them.

**Platform:** macOS 26+ on Apple silicon; built from source by the install script.

**Product:** [github.com/alexisbcz/hyperclip](https://github.com/alexisbcz/hyperclip)

**Pricing / access:** Open source (MIT); free to build. Jev calls use your own TypeSafe key; self-hosted Jev-compatible servers and LLMs are alternatives; optional publishing uses Zernio. Checked 2026-10-23. Source inspected; live app not run on the review host.

[Full Hyperclip (macOS video clipper with Jev clip scoring) guide](hyperclip.md) · [Source](https://github.com/alexisbcz/hyperclip)

### Jaste

`Source unverified` · `Pricing unverified` · `BYOK`

Smart copy/paste beta with clipboard history and an optional Direct Jev mode that selects a saved text value for the focused field.

**Access:** [download the Mac beta](https://jaste.app/) for Apple silicon and macOS 14+. The inspected bundle offers a Direct Jev key setting; that mode requires a TypeSafe key and may incur inference charges. App pricing and hosted access limits are unverified. No public source or license was linked; review covered the homepage and release metadata/strings, without launching the app or testing live matching.

[Full Jaste guide](jaste.md) · [Product and access](https://jaste.app/)

### JEV (marcosdeaza)

`Open source` · `Free source build` · `BYOK`

macOS voice-control exploration: TypeSafe Jev decides intent and target while an Anthropic planner runs continuous sessions.

**Jev's role:** Jev classifies voice intents and targets for desktop actions.

**Platform:** macOS (source build)

**Product:** [github.com/marcosdeaza/JEV](https://github.com/marcosdeaza/JEV)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full JEV (marcosdeaza) guide](marcosdeaza-jev.md) · [Source](https://github.com/marcosdeaza/JEV)

### Jev Amazing (macOS WeChat sidebar for witty reply ideas, ranked by Jev)

`Open source` · `Free source build`

Native macOS side window for WeChat: one click reads the visible chat (text, images, stickers), a generative model drafts replies in five tones, and Jev ranks them; you edit and send yourself. A derivative of the Jev Chat assistant for macOS.

**Jev's role:** Ranks candidate replies by comparison; generation and vision use other models.

**Platform:** macOS on Apple Silicon, built from source with setup.command.

**Product:** [github.com/yxjsxy/jevchat-amazing-response-macos](https://github.com/yxjsxy/jevchat-amazing-response-macos)

**Pricing / access:** Open source (MIT); free source build. Model calls use your own OpenRouter/TypeSafe keys. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Jev Amazing (macOS WeChat sidebar for witty reply ideas, ranked by Jev) guide](jev-amazing-wechat.md) · [Source](https://github.com/yxjsxy/jevchat-amazing-response-macos)

### Jev Assistant by jbellsolutions (Mac voice assistant that works in Chrome, on your Mac and in cloud browsers)

`Open source` · `Free`

Voice assistant preview for Apple Silicon Macs: LiveKit with GPT-Live 1 handles conversation, GPT-6 Luna does reasoning and task execution, and Jev makes the fast judgments (routing, next actions and checks) for tasks in your Chrome, on your Mac, in a Browser Use cloud browser or on an optional Orgo computer, with approvals before sends and changes.

**Jev's role:** Fast judge: routes requests and makes yes/no and choice checks during tasks, alongside the reasoning model.

**Platform:** macOS 15+ on Apple Silicon; unsigned preview installer.

**Product:** [github.com/jbellsolutions/jev-assistant/releases/tag/v1.0.0-preview.1](https://github.com/jbellsolutions/jev-assistant/releases/tag/v1.0.0-preview.1)

**Pricing / access:** Open source (MIT); the preview installer is a free download. OpenAI, LiveKit, TypeSafe, Browser Use and optional Orgo/Composio usage is billed by those providers. Checked 2026-10-27. Source inspected; live app not run on the review host.

[Full Jev Assistant by jbellsolutions (Mac voice assistant that works in Chrome, on your Mac and in cloud browsers) guide](jev-assistant-jbellsolutions.md) · [Source](https://github.com/jbellsolutions/jev-assistant)

### Jev Voice

`Open source` · `Free source build` · `BYOK`

Talk to your Mac with local whisper.cpp transcription. Jev selects a typed action and arguments in one fan-out; code executes via Accessibility/AppleScript.

**Access:** run the [MIT source](https://github.com/kevinbadi/jev-voice) on Apple Silicon–oriented macOS with Python 3.12+, the setup script, a TypeSafe key, and Microphone / Accessibility / Input Monitoring permissions. No app purchase fee; provider usage can incur charges. Live voice and desktop actions were not tested on the Linux review host.

[Full Jev Voice guide](jev-voice.md) · [Source](https://github.com/kevinbadi/jev-voice)

### Jev Voice (CUA)

`Source available` · `Free source build` · `BYOK`

Native macOS floating bar for continuous voice and text. Jev selects the next live Accessibility action; Swift runs observe–act–verify with no LLM planner. Distinct from kevinbadi/jev-voice and Cua jev-use.

**Access:** build the [public source](https://github.com/ronadin2002/jev-cua) on Apple silicon macOS 14+ with Xcode CLT and an OpenRouter or TypeSafe key (Keychain). No app purchase fee; provider usage can incur charges. **No LICENSE file** in the reviewed tree (not Open source). Live voice/desktop control were not tested on the Linux review host.

[Full Jev Voice (CUA) guide](jev-cua.md) · [Source](https://github.com/ronadin2002/jev-cua)

### Jevcast

`Open source` · `Free source build` · `BYOK`

Native macOS launcher/window manager (Option–Space). Optional TypeSafe Jev matches loose natural-language requests to known actions; core search stays local.

**Access:** build the [MIT source](https://github.com/RyanErkal/jevcast) on macOS 14+ with Xcode 26+. Launcher works without Jev; optional NL matching needs a TypeSafe or OpenRouter key in Keychain. No app purchase fee; provider usage is separate. Source inspected; macOS build/live Jev not run on the Linux review host.

[Full Jevcast guide](jevcast.md) · [Source](https://github.com/RyanErkal/jevcast) · [Product homepage](https://jevcast.vercel.app)

### JevDK and jev-serve (Mac tools to design decision questions and serve a Jev-style API locally)

`Open source` · `Free`

Two free Mac tools: JevDK lets you design and test typed decision questions on a local MLX model and on hosted backends side by side (including TypeSafe Jev through OpenRouter), mark right answers and calibrate; jev-serve answers a hosted-Jev-style HTTP API on your Mac.

**Jev's role:** Optional hosted comparison backend: Jev (typesafe/jev-1.13 via OpenRouter) runs next to local models so you can compare answers before shipping questions.

**Platform:** macOS on Apple silicon; signed and notarized DMG from GitHub Releases (v0.2.2 at review).

**Product:** [github.com/ancientcomputing/jevdk](https://github.com/ancientcomputing/jevdk)

**Pricing / access:** Open source (Apache-2.0); free download. Hosted Jev calls go through your own OpenRouter key; local models are free to run. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full JevDK and jev-serve (Mac tools to design decision questions and serve a Jev-style API locally) guide](jevdk.md) · [Source](https://github.com/ancientcomputing/jevdk)

### JEVision (flowchart UI tests for any Mac app, with Jev checking screens and finding elements)

`Open source` · `Free source build` · `BYOK`

macOS app for visual UI testing of any Mac app, including ones you cannot instrument: a test is a JSON flowchart walked block by block with the real mouse and keyboard, and Jev can check what a screenshot shows with a confidence threshold and find elements described in words such as "the blue Save button".

**Jev's role:** Optional vision provider: Jev answers how sure it is that a screen matches an expectation and locates elements by description; Anthropic, OpenAI, Gemini, Ollama and LM Studio are alternatives.

**Platform:** macOS 26+ source build; the README describes signed DMG and Homebrew installs, but no GitHub release was published at review time.

**Product:** [github.com/dev-pikapik/JEVision](https://github.com/dev-pikapik/JEVision)

**Pricing / access:** Open source (MIT); free source build. Jev calls are billed to your TypeSafe account or Cloudflare AI Gateway credits. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full JEVision (flowchart UI tests for any Mac app, with Jev checking screens and finding elements) guide](jevision.md) · [Source](https://github.com/dev-pikapik/JEVision)

### JevPaste

`Open source` · `Free source build` · `BYOK`

macOS menu bar Smart Paste: TypeSafe Jev picks which exact value from a copied multi-field block fits the focused input.

**Access:** build the [MIT source](https://github.com/taiki510/JevPaste) on macOS 14+ with Swift/Xcode CLT, Accessibility permission, and a TypeSafe key in Keychain. No app purchase fee; provider usage can incur charges. Linux review cited upstream CI; live paste not run here. Distinct from closed-source Jaste.

[Full JevPaste guide](jevpaste.md) · [Source](https://github.com/taiki510/JevPaste)

### Keel

`Open source` · `Free source build` · `BYOK`

Local-first macOS coding workspace with sessions, composer, terminal, and ACP agents. Default selector is local Laya; hosted TypeSafe Jev is opt-in for fresh unpinned tasks.

**Access:** [build the MIT source](https://github.com/codejunkie99/keel) on macOS Apple Silicon (`docs/build.md`) with optional TypeSafe credential for Jev mode. No app purchase fee; Laya is local; coding providers and optional Jev are separate. Source inspected; macOS build/UI not run on the Linux review host.

[Full Keel guide](keel.md) · [Source](https://github.com/codejunkie99/keel)

### Live Jev

`Open source` · `Free source build` · `BYOK`

Control Ableton Live from a ⌘⇧Space bar: TypeSafe Jev chooses typed mixer, transport, clip, note, and device actions from short English or Japanese phrases; a Remote Script applies them on localhost.

**Access:** build the [MIT source](https://github.com/okinaaudio/live-jev) on Apple Silicon macOS 14+ with Python 3.13, Xcode CLT, Ableton Live 12, and a TypeSafe key. Early **0.1x** source distribution (no packaged installer). No app purchase fee; provider usage can incur charges. Live Ableton control was not tested on the Linux review host.

[Full Live Jev guide](live-jev.md) · [Source](https://github.com/okinaaudio/live-jev)

### Llasso (draw a box round anything on your Mac and ask about it or have it changed)

`Open source` · `Free` · `BYOK`

Mac app where you hold ⌘ and drag a box round anything on screen, then type or say what you want: Llasso guesses what the box holds, picks a model for the kind of work from OpenRouter's live lists, and every change waits for your tap; Jev on OpenRouter classifies the request when it can answer within 1.5 seconds.

**Jev's role:** Request router: Jev reads the typed request and names the kind of work (writing, coding, design and so on) so Llasso can pick a model; keyword rules decide when Jev is slow.

**Platform:** macOS 26+ on Apple silicon; install script fetches the GitHub release (v0.1.2 at review time).

**Product:** [github.com/jamiejefferson/llasso](https://github.com/jamiejefferson/llasso)

**Pricing / access:** Open source (MIT); free install. All model calls, including Jev, are billed to your OpenRouter key. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Llasso (draw a box round anything on your Mac and ask about it or have it changed) guide](llasso.md) · [Source](https://github.com/jamiejefferson/llasso)

### Mac Voice Control

`Open source` · `Free source build` · `BYOK`

Hands-free macOS control by voice: Deepgram or local Whisper speech-to-text, typed action routing by Jev (`typesafe/jev` through Command Code's provider API) or an LLM over a closed action set, and AppleScript/Accessibility execution; open apps, drive browser tabs and dictate code into IntelliJ or VS Code.

**Access:** clone the [MIT source](https://github.com/nagesh-bhosle/mac-voice-control) and run with uv on macOS. No app fee; Jev access goes through a Command Code key and STT through Deepgram or local Whisper (usage billed by each provider). Source inspected; not run on the review host.

[Full Mac Voice Control guide](mac-voice-control.md) · [Source](https://github.com/nagesh-bhosle/mac-voice-control)

### macbrow

`Open source` · `Free source build` · `BYOK`

Control macOS apps and perform Chrome tasks through an experimental voice assistant. Jev routes requests, selects tool arguments, and judges follow-ups; Gradium handles speech and a separate LLM supplies generated scripts and text.

**Access:** run the [MIT source](https://github.com/timpratim/macbrow#setup) on macOS with Python 3.12+, `uv`, TypeSafe and Gradium keys, and desktop permissions. The default LLM backend also needs LiveKit credentials; LM Studio is an alternative. No app purchase fee applies to the source build; provider usage can incur charges. Browser tasks require Chrome remote debugging. All 26 upstream tests passed with network access denied; live voice, desktop actions, and browser automation were not tested.

[Full macbrow guide](macbrow.md) · [Source](https://github.com/timpratim/macbrow)

### Meraline

`Open source` · `Free` · `BYOK`

Mac ⌥Space assistant for any app with a Decision mode: ask yes/no, choice or level questions about selected text and get Jev (direct or via OpenRouter) or local decision-model answers with how sure they are.

**Access:** download the free [MIT-licensed release](https://github.com/Meldiron/meraline/releases/latest) or `brew install --cask meldiron/tap/meraline`. Decision mode with Jev needs your own TypeSafe or OpenRouter key (usage billed separately). Source inspected; the app was not run on the Linux review host.

[Full Meraline guide](meraline.md) · [Source](https://github.com/Meldiron/meraline)

### Mish

`Open source` · `Free source build` · `BYOK`

Local-first AI design workspace: write a brief and a local agent CLI builds the design; in the agency fast lane, TypeSafe Jev routes the brief to a site family and verifies facts before publishing.

**Jev's role:** One Jev request places the brief on the Website Shape Atlas and picks a family package; Jev then checks each fact against the brief and strict mode blocks publishing on invented or missing facts.

**Platform:** macOS (Apple Silicon DMG, not notarized) or build from source

**Product:** [github.com/ZeroSum-Solutions/mish/releases/latest](https://github.com/ZeroSum-Solutions/mish/releases/latest)

**Pricing / access:** Free Apache-2.0 app; uses your agent CLI subscription (Claude Code/Codex) and your own TypeSafe key for routing/verification.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Mish guide](mish.md) · [Source](https://github.com/ZeroSum-Solutions/mish)

### Moji (macOS emoji picker with optional Jev ranking)

`Open source` · `Free source build`

Native macOS emoji picker: type `:` and a few letters in any app. Search runs locally; with a TypeSafe key, Jev reorders the suggestions to the emoji you most likely mean.

**Jev's role:** Optional: one choice question over about 200 local candidates reorders suggestions a moment after local results appear.

**Platform:** macOS 14+, built from source with `scripts/bundle.sh`.

**Product:** [github.com/beckyisj/moji](https://github.com/beckyisj/moji)

**Pricing / access:** Open source (MIT); free source build. Jev ranking uses your own TypeSafe key (the README estimates about $0.0001 per lookup). Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Moji (macOS emoji picker with optional Jev ranking) guide](moji-emoji-picker.md) · [Source](https://github.com/beckyisj/moji)

### PetPaw

`Source available` · `Free` · `BYOK`

Desktop pet companion for Apple Silicon Macs (SwiftUI, SceneKit, AVAudioEngine) with imported characters, voice and lip-sync: interaction reactions and poses are chosen by Cloud JEV (`typesafe-ai/jev`) or a Local Open-Jev mode that runs a 2B Open-Jev checkpoint ported to Swift/MLX on device, while Apple Foundation Models write moods and speech bubbles.

**Access:** download the free [DMG](https://github.com/sirily11/pet-companion/releases/latest/download/PetCompanion.dmg) or build the [source](https://github.com/sirily11/pet-companion) (no LICENSE file — Source available). Cloud JEV needs your own key; Local Open-Jev is free. Source inspected; not run on the review host.

[Full PetPaw guide](petpaw.md) · [Source](https://github.com/sirily11/pet-companion)

### Pointsman by RomainJeff (macOS link router that picks the right browser with Jev)

`Open source` · `Free source build` · `BYOK`

macOS menu bar app you set as the default browser: describe once how you use each real browser, and each clicked link goes to the right one, chosen by Jev from your descriptions, the app the link came from and the URL without its query string.

**Jev's role:** Core: Jev returns a probability for each browser plus none; below a 60% threshold, on error or after 1.5 s the link goes to your fallback browser.

**Platform:** macOS on Apple silicon; build from source (no signed release yet).

**Product:** [github.com/RomainJeff/pointsman](https://github.com/RomainJeff/pointsman)

**Pricing / access:** Open source (MIT); free source build. Jev calls go through your own OpenRouter key (the README estimates about $0.00002 per link). Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full Pointsman by RomainJeff (macOS link router that picks the right browser with Jev) guide](romainjeff-pointsman.md) · [Source](https://github.com/RomainJeff/pointsman)

### PR Review (sunwrobert)

`Open source` · `Free source build` · `BYOK`

Keyboard-first macOS app for reviewing and merging GitHub pull requests through your `gh` login, with optional Jev readiness scores, smart search and grouping of related PRs.

**Jev's role:** Optional: Jev adds readiness scoring, topic search and grouping on top of GitHub facts.

**Platform:** macOS (universal build)

**Product:** [github.com/sunwrobert/pr-review](https://github.com/sunwrobert/pr-review)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full PR Review (sunwrobert) guide](sunwrobert-pr-review.md) · [Source](https://github.com/sunwrobert/pr-review)

### pulp

`Open source` · `Free source build` · `BYOK`

Personal macOS pipeline that turns Safari iCloud tabs into clean EPUBs for an e-ink reader (OPDS catalog, KOReader sync, optional reMarkable push); optional `--smart` triage asks TypeSafe Jev whether each tab the denylist kept is worth reading.

**Access:** clone the [MIT source](https://github.com/danemarguglio/pulp) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full pulp guide](pulp.md) · [Source](https://github.com/danemarguglio/pulp)

### QuickAsk (macOS menu bar assistant for Codex and Claude, with Jev routing and follow-up checks)

`Source available` · `Free source build` · `BYOK`

Native macOS menu bar assistant: press Option–Space, ask a question and send it to Codex or Claude using your existing CLI logins; Jev (or optionally OpenAI Decisions) routes which context to attach and checks whether an answer needs a follow-up.

**Jev's role:** Context router and follow-up checker: Jev answers typed questions about which context to include and whether a reply needs a follow-up.

**Platform:** macOS 14+; build from source or use the `dist/QuickAsk.app` in the repository (no GitHub release at review time).

**Product:** [github.com/cxrobx/quickask](https://github.com/cxrobx/quickask)

**Pricing / access:** Source available under BSL 1.1: free for personal use and internal use by your organisation; selling it needs a commercial licence from CX Ventures LLC. Converts to Apache-2.0 on 2030-09-30. Jev calls billed to your TypeSafe key. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full QuickAsk (macOS menu bar assistant for Codex and Claude, with Jev routing and follow-up checks) guide](quickask.md) · [Source](https://github.com/cxrobx/quickask)

### RedOS

`Open source` · `Free source build` · `BYOK`

macOS menu-bar assistant for voice and text commands where a System One model using the Jev protocol routes request kinds and decides whether to speak or stay quiet.

**Jev's role:** Jev-protocol System One decisions route request kinds and speak/notify/silent choices; optional.

**Platform:** macOS (source build)

**Product:** [github.com/Carassale/redos](https://github.com/Carassale/redos)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full RedOS guide](redos.md) · [Source](https://github.com/Carassale/redos)

### Reflex (monotykamary)

`Open source` · `Free source build` · `BYOK`

Mac menu-bar app to see, answer and talk to every coding agent running in herdr; Jev (via jev-fabric) routes each request to the right session or folder and asks you to confirm when unsure.

**Jev's role:** Jev picks the destination session/folder for each request; code delivers it or asks you to confirm.

**Platform:** macOS 26+ (Apple Silicon), source build

**Product:** [github.com/monotykamary/reflex](https://github.com/monotykamary/reflex)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Reflex (monotykamary) guide](monotykamary-reflex.md) · [Source](https://github.com/monotykamary/reflex)

### Sippy (macOS water-break companion with optional Jev sip confirmation)

`Open source` · `Free source build` · `BYOK`

Small native macOS water reminder with a floating droplet buddy and menu-bar progress; Apple Vision face and hand tracking spots a possible sip on device, and with your own TypeSafe key Jev confirms the candidate frame before a drink is logged.

**Jev's role:** Optional: Jev answers one Noul question about a single candidate JPEG; 0.8 or higher confirms the sip, otherwise the local check decides.

**Platform:** macOS 13+, built from source (`scripts/build-app.sh`, ad-hoc signed); the README describes DMG/ZIP releases, but none were published at review time.

**Product:** [github.com/milanjain2208/sippy](https://github.com/milanjain2208/sippy)

**Pricing / access:** Open source (MIT); free source build with no account. The optional Jev check is billed to your own TypeSafe key, at most 3 photos per reminder. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Sippy (macOS water-break companion with optional Jev sip confirmation) guide](sippy.md) · [Source](https://github.com/milanjain2208/sippy)

### skil.li

`Open source` · `Free` · `BYOK`

Native macOS launcher and assistant (apps, files, clipboard, snippets, windows, Hyper Key) that can also act on requests; its Ask router uses a fast decision model such as TypeSafe Jev to route what you typed before a larger model runs.

**Jev's role:** Optional fast router: Jev decides how an Ask request should be handled before the main model is called.

**Platform:** macOS 26+ (signed, notarised download or Homebrew cask).

**Product:** [skil.li](https://skil.li)

**Pricing / access:** Free download (GPL-3.0); you bring your own AI keys and pay those providers. Checked 2026-10-19. Source inspected; live app not run on the review host.

[Full skil.li guide](skilli.md) · [Source](https://github.com/nomdelasociete/skilli)

### SplitSeek

`Open source` · `Free`

macOS desktop app that searches a folder of grey, flat LOG video footage by describing a moment in plain words: it samples a frame every 2 seconds, asks Jev a yes/no question about each frame, and ranks matching moments with timestamps, confidence and a preview from the best frame.

**Jev's role:** Jev answers one yes/no question per sampled frame; the app ranks and groups frames by the returned probability.

**Platform:** macOS on Apple Silicon (tested on macOS 15); build from source, no signed release.

**Product:** [github.com/okoryem/split-seek](https://github.com/okoryem/split-seek)

**Pricing / access:** Free MIT source build; you pay for your own Jev calls (image access required). Checked 2026-10-20. Source inspected; live app not run on the review host.

[Full SplitSeek guide](splitseek.md) · [Source](https://github.com/okoryem/split-seek)

### SpotAsk

`Open source` · `Free`

Native macOS menu-bar assistant: summon it with a hotkey to ask your own model (BYOK), act on selected text in any app, or route a question to web AI, desktop apps or local CLI agents, with an optional Jev decision that picks the destination and shows its confidence before sending.

**Jev's role:** Optional: Jev picks which destination (web AI, desktop app or CLI agent) a question should go to, with a confidence shown before sending.

**Platform:** macOS 15+ (Apple Silicon and Intel); DMG releases (v0.3.1 on 2026-10-19) and Homebrew cask.

**Product:** [shiquda.github.io/SpotAsk/](https://shiquda.github.io/SpotAsk/)

**Pricing / access:** Free AGPL-3.0 app; you pay your own model provider and Jev calls. Checked 2026-10-20. Source inspected; live app not run on the review host.

[Full SpotAsk guide](spotask.md) · [Source](https://github.com/shiquda/SpotAsk)

### Switchyard

`Open source` · `Free source build` · `BYOK`

macOS menu-bar app that opens every link in the right Dia/Chrome profile; TypeSafe Jev decides uncovered links and confident answers become local rules.

**Access:** Build the [MIT source](https://github.com/kevinebaugh/switchyard) on macOS with a TypeSafe API key. No app purchase fee; each Jev judgment can incur provider charges. Source inspected; macOS build/live routing not run on the Linux review host. Distinct from FrancoisChastel/jev-router's Switchyard-style naming.

[Full Switchyard guide](switchyard.md) · [Source](https://github.com/kevinebaugh/switchyard)

### Tab (Mac next-action autocomplete)

`Source available` · `Free source build` · `BYOK`

Hackathon proof of concept that predicts your next action on a Mac and shows it as a gray ghost (a highlighted button or gray text); press Tab to do it. Jev picks among code-proposed candidate actions, and x402 paywalls become testnet payments with an amount check.

**Jev's role:** Jev picks the next action from code-proposed candidates, with a calibrated confidence.

**Platform:** macOS (source build; work in progress)

**Product:** [github.com/alaramartin/paradigmhacks](https://github.com/alaramartin/paradigmhacks)

**Pricing / access:** Free source; no license file on the reviewed commit (all rights reserved by default). Testnet payments only. Checked 2026-10-16. Source inspected; live app not run on the review host.

[Full Tab (Mac next-action autocomplete) guide](tab-mac-next-action.md) · [Source](https://github.com/alaramartin/paradigmhacks)

### Tally (automatic time, income and evidence tracking for hourly contract work)

`Open source` · `Free source build`

Menu bar app for hourly contractors that records which app, window and tab you are in every few seconds, assigns time to projects by your rules, seals intervals into a hash-chained ledger and bills only explicit client sessions; optionally Jev assigns unmatched windows to projects (at 80% confidence or more) and to activity categories.

**Jev's role:** Optional classifier: windows no rule matches go to Jev once per window for a project or category; Jev never puts time on a client.

**Platform:** macOS; build from source (self-signed release builds).

**Product:** [github.com/0Calories/tally](https://github.com/0Calories/tally)

**Pricing / access:** Open source (MIT); free source build. Optional Jev calls are billed to your own TypeSafe key. Checked 2026-10-27. Source inspected; live app not run on the review host.

[Full Tally (automatic time, income and evidence tracking for hourly contract work) guide](tally-contract-time.md) · [Source](https://github.com/0Calories/tally)

### TipTour

`Open source` · `Free source build` · `BYOK`

Use a macOS menu bar companion to act on typed click requests. Jev chooses among locally detected controls and judges completion or missing targets. A separate Gemini mode handles voice and writing.

**Access:** macOS 14.2+, a source build with Xcode, a TypeSafe key, and desktop permissions. Gemini mode needs its own key. Source is MIT licensed; provider usage can incur charges. Eight isolated decision tests passed; the full app, packaged releases, and live desktop actions were not tested.

[Full TipTour guide](tiptour.md) · [Source](https://github.com/milind-soni/tiptour-macos)

### voice-browser

`Open source` · `Free source build` · `BYOK`

macOS command bar that drives Chromium, Dia, Arc or Chrome from plain English; TypeSafe Jev (or SubQ Snap) picks clicks and targets for fast single actions and goal chains.

**Jev's role:** Jev decides intent and UI targets for spoken or typed browser commands before Playwright/automation acts.

**Platform:** macOS (source build)

**Product:** [github.com/ken-code-wq/voice-browser#readme](https://github.com/ken-code-wq/voice-browser#readme)

**Pricing / access:** Free MIT source; TypeSafe or SubQ key for decisions.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full voice-browser guide](voice-browser.md) · [Source](https://github.com/ken-code-wq/voice-browser)

### YapSketch

`Open source` · `Free source build` · `BYOK`

macOS app for explaining bugs by talking and pointing: record your screen and voice, and Jev splits what you said into points, matches each to what you showed, and picks the clearest screenshot, then puts numbered text plus images on your clipboard for a coding agent.

**Jev's role:** Jev aligns transcript segments with on-screen gestures and picks the best frame for each point.

**Platform:** macOS 15+ (build from source with `./scripts/build-app.sh`).

**Product:** [github.com/farouqaldori/yapsketch](https://github.com/farouqaldori/yapsketch)

**Pricing / access:** Free source build; Jev calls are billed by TypeSafe, Opper, or OpenRouter. Speech-to-text runs locally by default. Source inspected; live app not run on the review host.

[Full YapSketch guide](yapsketch.md) · [Source](https://github.com/farouqaldori/yapsketch)

## Android apps

### Audience Moderator (Android counter for people and raised hands, with an optional Jev round insight)

`Open source` · `Free source build`

Android helper for event moderators: counts people and raised hands on-device (MediaPipe or YOLOv8n-pose), runs timed question rounds, picks a random audience member, and can optionally send round results, or one photo you confirm, to Jev for a short insight and a second count; camera pictures are never saved and there is no face recognition.

**Jev's role:** Optional insight: one Choice and one Noul question about a round, plus an experimental photo check.

**Platform:** Android arm64; debug APK built from source. The author notes the APK had not been run on a device at the time of writing.

**Product:** [github.com/irvan-putra/jev-moderator](https://github.com/irvan-putra/jev-moderator)

**Pricing / access:** Open source (AGPL-3.0); free source build. Optional Jev calls are billed to your own TypeSafe key. Checked 2026-10-27. Source inspected; live app not run on the review host.

[Full Audience Moderator (Android counter for people and raised hands, with an optional Jev round insight) guide](audience-moderator-jev.md) · [Source](https://github.com/irvan-putra/jev-moderator)

### axo-launcher

`Open source` · `Free source build` · `BYOK`

Minimalist Android launcher (Portuguese docs): text-only home, grayscale screen and delays for distracting apps; quick-capture phrases are classified offline, with TypeSafe Jev deciding the ambiguous ones.

**Jev's role:** When the offline keyword classifier is unsure what kind of item a phrase is, Jev (`typesafe/jev-1.13` via OpenRouter) chooses among the offered types; cached, capped at 300 calls/day.

**Platform:** Android 8+ (build from source; tuned for Xiaomi HyperOS)

**Product:** [github.com/axolutions/axo-launcher#readme](https://github.com/axolutions/axo-launcher#readme)

**Pricing / access:** Free MIT source; optional OpenRouter key for Jev (reported ~US$0.000018 per phrase).

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full axo-launcher guide](axo-launcher.md) · [Source](https://github.com/axolutions/axo-launcher)

### DSB (trust-first Android AI assistant with a Jev command gate)

`Open source` · `Free source build`

Open-source Android assistant built on DeepSeek Harness that operates apps on a background virtual display of your own phone, with execution gates, a task ledger and audit logs; an optional Jev gate classifies suspicious shell commands before they run.

**Jev's role:** Optional safety gate: Jev classifies the kind of each suspicious shell command and whether it would leak secrets, in shadow (log-only) mode by default.

**Platform:** Android 11+ via the project's installer; validated so far on the maintainer's device and an arm64 emulator.

**Product:** [github.com/tianye1999/dsb](https://github.com/tianye1999/dsb)

**Pricing / access:** Open source (Apache-2.0); free to install. DeepSeek and TypeSafe usage are billed to your keys. Checked 2026-10-23. Source inspected; live app not run on the review host.

[Full DSB (trust-first Android AI assistant with a Jev command gate) guide](dsb.md) · [Source](https://github.com/tianye1999/dsb)

### Jev Chat Assistant

`Open source` · `Free source build` · `BYOK`

Non-invasive Android overlay: Accessibility reads on-screen chat; TypeSafe Jev (OpenRouter Decisions) judges intent/danger/action and ranks drafted replies; fill-only paste (never auto-send). WeChat first.

**Access:** build the [MIT source](https://github.com/jev-chat/jev-chat-jarvis) (JDK 17, Android SDK 35) with an OpenRouter API key plus Accessibility/overlay permissions. No app purchase fee; OpenRouter/Jev usage is separate. Source inspected; APK build and live calls not run on the Linux review host. Distinct from desktop WeChat-log analyzers and the separate Android UI-agent SDK listed under Developer tools.

[Full Jev Chat Assistant guide](jev-chat-jarvis.md) · [Source](https://github.com/jev-chat/jev-chat-jarvis)

### JevBystander

`Open source` · `Free source build` · `BYOK`

Android Accessibility WeChat reader: TypeSafe Jev judges intent/emotion/urgency/stance and shows three Toasts only (~861 KB APK, zero third-party deps).

**Access:** install the [MIT Release APK](https://github.com/Nisaka520/JevBystander/releases/latest) or build the [source](https://github.com/Nisaka520/JevBystander) (JDK 17, Android SDK 35) with a TypeSafe key and Accessibility enabled. No app purchase fee; TypeSafe usage is separate. Source inspected; APK/device/live not run on the Linux review host. Sister of JevIntent; judgment-only vs reply-drafting Jev Chat Assistant.

[Full JevBystander guide](jev-bystander.md) · [Source](https://github.com/Nisaka520/JevBystander) · [Product page](https://nisaka520.github.io/JevBystander/)

### JevGuide

`Open source` · `Free source build` · `BYOK`

Android WeChat relationship-progress assistant: Accessibility or screenshot vision reads the chat; TypeSafe Jev scores intent/emotion/affinity; a chat model drafts three reply candidates on a sticky overlay (never auto-sends).

**Access:** install the [MIT Release APK](https://github.com/Nisaka520/JevGuide/releases/latest) or build the [source](https://github.com/Nisaka520/JevGuide) (JDK 17, Android SDK 35) with a TypeSafe key plus optional chat/vision keys. No app purchase fee; provider usage is separate. Source inspected; APK/device/live not run on the Linux review host. Sister of JevBystander/JevIntent; distinct from reply-drafting Jev Chat Assistant.

[Full JevGuide guide](jevguide-nisaka520.md) · [Source](https://github.com/Nisaka520/JevGuide) · [Product page](https://nisaka520.github.io/JevGuide/)

### JevIntent

`Open source` · `Free source build` · `BYOK`

FkWeChat/LSPosed WeChat plugin: long-press a message for TypeSafe Jev intent/emotion/urgency/stance overlays—no reply text, no send.

**Access:** copy the [MIT plugin files](https://github.com/Nisaka520/JevIntent) into FkWeChat with a TypeSafe API key. No app purchase fee; TypeSafe usage is separate. Source inspected; device/live calls not run on the Linux review host. Sister of JevBystander; distinct from reply-drafting Jev Chat Assistant.

[Full JevIntent guide](jev-intent.md) · [Source](https://github.com/Nisaka520/JevIntent)

### Mobile Agent (KYRIE66nb)

`Open source` · `Free` · `BYOK`

Open-source on-device Android AI agent (Chinese/English) that sees and taps the screen, with an optional dedicated decision backend — TypeSafe Jev or self-hosted Laya over `/v1/systemone` — for safety-gate verdicts and low-risk navigation choices; off by default, SHADOW/ENFORCE modes, explicit consent.

**Access:** install the free APK from [GitHub Releases](https://github.com/KYRIE66nb/mobile-agent/releases/latest) or build the [Apache-2.0 source](https://github.com/KYRIE66nb/mobile-agent). Requires your own model key; the optional Jev backend uses your own TypeSafe key (usage billed by TypeSafe). Early-stage; source inspected, app not run on the review host.

[Full Mobile Agent (KYRIE66nb) guide](mobile-agent.md) · [Source](https://github.com/KYRIE66nb/mobile-agent)

### Notiq

`Source available` · `Free source build` · `BYOK`

Native Android notification filter: natural-language rules plus TypeSafe Jev (or self-hosted FastJev) Choice keep/filter/uncertain.

**Access:** build the [source](https://github.com/chengyongru/notiq) (JDK/Android SDK) with Notification Access and a TypeSafe or FastJev endpoint/key. No app purchase fee; inference separate. **No LICENSE** at tip—not Open source. Source inspected; device/live not run on Linux review host.

[Full Notiq guide](notiq.md) · [Source](https://github.com/chengyongru/notiq)

### QuietFlow (Android notification attention manager with opt-in Jev classification)

`Open source` · `Free source build` · `BYOK`

Android proof of concept that listens to notifications and sorts them into five attention classes, from action required to hide; local safety rules protect OTP, security, finance, calls and system notifications, Jev classifies the rest when you opt in, and observation mode (never dismissing anything) is the default.

**Jev's role:** Optional but central: with a key and explicit permission, Jev picks one of the five classes for redacted notification text, with confidence; high-confidence results drive active-mode actions.

**Platform:** Android 10+, built from source or from the CI debug APK artifact; not on Google Play.

**Product:** [github.com/KoheiTakada/QuietFlow](https://github.com/KoheiTakada/QuietFlow)

**Pricing / access:** Open source (MIT); free source build. Jev calls are billed to your TypeSafe key. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full QuietFlow (Android notification attention manager with opt-in Jev classification) guide](quietflow.md) · [Source](https://github.com/KoheiTakada/QuietFlow)

### Simple Launcher

`Open source` · `Free source build` · `BYOK`

Minimal Android home app styled after Omarchy's waybar and walker: status bar, next event, notifications, recent apps, and a fuzzy app search where Jev picks the app by meaning when nothing matches by name.

**Jev's role:** Semantic fallback in search: when no prefix or word-start match exists, Jev chooses the app that fits the query (for example "music" finds the music app).

**Platform:** Android (build from source and sideload; tested on Pixel 4a, Android 13; no Play Store listing verified).

**Product:** [github.com/polidog/simple-launcher](https://github.com/polidog/simple-launcher)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Simple Launcher guide](simple-launcher.md) · [Source](https://github.com/polidog/simple-launcher)

## Windows apps

### Booksmith (Calibre ebooks to Plex audiobooks, with Jev-planned pauses)

`Source available` · `Free source build` · `BYOK`

Early Windows-first app that turns DRM-free Calibre ebooks into chaptered audiobooks narrated locally with Kokoro and imports them into Plex; optional Jev annotation proposes sentence pauses, reviews them in paragraph context and suggests pronunciations for ambiguous words.

**Jev's role:** Optional: when contextual pauses or pronunciation help are enabled, Jev picks pause boundaries and timing variants and suggests pronunciations; narration itself is local and Jev never rewrites the text.

**Platform:** Windows (service lock, scheduled task and Plex credential discovery are Windows-only); source release, not an installer.

**Product:** [github.com/neuralcataccel/booksmith](https://github.com/neuralcataccel/booksmith)

**Pricing / access:** Free source build; public source with no license file (no open-source license granted). Jev calls go to the decision endpoint you configure, with your own key and monthly spend limits in config. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full Booksmith (Calibre ebooks to Plex audiobooks, with Jev-planned pauses) guide](booksmith.md) · [Source](https://github.com/neuralcataccel/booksmith)

### Conclave (local multi-model council app with Jev routing and answer checks)

`Open source` · `Free source build` · `BYOK`

Local Windows app that sends one question to a council of up to 13 AI providers, has a chosen model synthesise their answers blind and an optional model from another company audit the result; optional Jev checks route questions, flag refusals or off-topic answers and test draft claims, in shadow (record-only) mode by default.

**Jev's role:** Optional: Jev routes questions, checks each council answer and the draft's claims; modes are Off, Shadow (record only, default) and Active.

**Platform:** Windows 10/11, runs locally on 127.0.0.1 in an Edge app window; keys are stored with Windows DPAPI.

**Product:** [github.com/btrischetta/conclave](https://github.com/btrischetta/conclave)

**Pricing / access:** Open source (Apache-2.0); free source build. Each provider, including TypeSafe, bills your own key; Conclave shows live per-call costs. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Conclave (local multi-model council app with Jev routing and answer checks) guide](conclave.md) · [Source](https://github.com/btrischetta/conclave)

### Emc² (desktop email client with Jev sorting)

`Open source` · `Free`

Desktop email client for Windows (macOS build from source) with a bundled mail service and encrypted SQLite storage; Jev sorts mail into Important and Other and gives each row a fixed label such as "Needs a reply".

**Jev's role:** Classifies each message and rates relevance in one call; sender rules and Teach corrections take priority.

**Platform:** Windows installer from GitHub Releases (unsigned); macOS build from source.

**Product:** [github.com/collection-of-things/aggregate-mail](https://github.com/collection-of-things/aggregate-mail)

**Pricing / access:** Open source (MIT); free download. Jev sorting uses your own provider key. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Emc² (desktop email client with Jev sorting) guide](emc2-mail.md) · [Source](https://github.com/collection-of-things/aggregate-mail)

### fine-file (Windows file explorer with optional Jev risk badges)

`Open source` · `Free` · `BYOK`

Korean-language Windows file explorer with folder sizes, instant search from an NTFS MFT scan and live updates, plus optional AI clean-up plans where Jev adds fast safe, caution or risky badges and a second risk check on each step.

**Jev's role:** Optional: Jev scores whether each item is safe to delete and whether a program recreates it; the explorer works fully without it.

**Platform:** Windows (installer on GitHub Releases); interface in Korean.

**Product:** [github.com/toxh13/fine-file/releases](https://github.com/toxh13/fine-file/releases)

**Pricing / access:** Free MIT/Apache-2.0 app; Jev calls are billed to your own key. Checked 2026-10-22. Source inspected; live app not run on the review host.

[Full fine-file (Windows file explorer with optional Jev risk badges) guide](fine-file.md) · [Source](https://github.com/toxh13/fine-file)

### FlowMesh

`Open source` · `Free`

Windows voice-workflow app built for the Wispr No Hands challenge: dictate into the command box, review an exact plan, then approve; Jev picks which registered routine (focus, meeting, research or none) fits, and a local runtime runs only allowlisted actions with receipts.

**Jev's role:** Jev answers one Choice question to route a spoken request among three registered routines or none; it never generates shell commands or unregistered device actions.

**Platform:** Windows (unsigned release zip; Windows may show a publisher warning).

**Product:** [github.com/HamzaShaikh-source/flowmesh/releases/latest](https://github.com/HamzaShaikh-source/flowmesh/releases/latest)

**Pricing / access:** Free download from GitHub Releases (v1.0.0, checked 2026-10-20); you pay for your own Jev calls. Source inspected; live app not run on the review host.

[Full FlowMesh guide](flowmesh-voice.md) · [Source](https://github.com/HamzaShaikh-source/flowmesh)

### INployed

`Open source` · `Free source build` · `BYOK`

Windows desktop app with a cloud pipeline that collects job postings, ranks them against your background, writes grounded one-page résumés, and fills and sends queued applications; Jev makes the yes-or-no calls in scoring and reads each application page when it is on.

**Jev's role:** Optional judge for scoring and for reading application pages before code fills them from your data.

**Platform:** Windows 11 (install from source per README).

**Product:** [github.com/yib7/INployed](https://github.com/yib7/INployed)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full INployed guide](inployed.md) · [Source](https://github.com/yib7/INployed)

### Jev Chat Windows

`Open source` · `Free source build` · `BYOK`

Windows WeChat (4.x) side panel: local offline OCR reads the chat window; TypeSafe Jev (OpenRouter Decisions) judges intent/emotion and ranks three fill-only reply candidates; send stays manual.

**Access:** download the [MIT Release zip](https://github.com/jev-chat/jev-chat-windows/releases) (`jev-chat-windows.exe`) or run the [source](https://github.com/jev-chat/jev-chat-windows) on Windows with an OpenRouter API key (optional DeepSeek). No app purchase fee; provider usage is separate. Source inspected on Linux; Windows GUI/OCR/live calls not run on the review host. Distinct from the Android Jev Chat Assistant listing.

[Full Jev Chat Windows guide](jev-chat-windows.md) · [Source](https://github.com/jev-chat/jev-chat-windows)

### jev-desktop

`Open source` · `Free source build` · `BYOK`

Windows desktop agent: UI Automation observes controls, TypeSafe Jev chooses the next action, and a small LLM types text when needed (`jevd`).

**Access:** Windows PowerShell install script or clone the MIT source; requires TypeSafe + OpenRouter keys. Experimental—moves the real mouse/keyboard. No app purchase fee; provider usage separate. Source inspected on Linux; Windows GUI/live paths not run on the review host.

[Full jev-desktop guide](ehtan-smaltai-jev-desktop.md) · [Source](https://github.com/ehtan-smaltai/jev-desktop)

### JevMail (Outlook)

`Open source` · `Free source build` · `BYOK`

Outlook add-in for Microsoft 365 work and school accounts, powered by TypeSafe Jev.

**Jev's role:** Jev powers mail decisions inside the Outlook add-in API surface.

**Platform:** Microsoft 365 Outlook (work/school)

**Product:** [github.com/koh-henry/jevmail](https://github.com/koh-henry/jevmail)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full JevMail (Outlook) guide](koh-henry-jevmail.md) · [Source](https://github.com/koh-henry/jevmail)

### KeyFlip (Windows tray app that picks the right Hebrew or English layout per text field)

`Open source` · `Free source build` · `BYOK`

Windows tray app for people who type in Hebrew and English: when you focus a text field it chooses the layout from what it learned for that field, the text already there, or Jev's reading of the app, site, page title and field label, and it fixes a word you typed on the wrong layout.

**Jev's role:** Layout classifier: Jev decides Hebrew or English from the field's context when local rules cannot, above a configurable threshold (default 0.70).

**Platform:** Windows 10/11; source build with `dotnet publish` (no published release at review time).

**Product:** [github.com/kivimedia/keyflip](https://github.com/kivimedia/keyflip)

**Pricing / access:** Open source (MIT); free source build. Jev calls (about $0.00002 each per the README) are billed to your TypeSafe account; the optional Haiku fixer to Anthropic. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full KeyFlip (Windows tray app that picks the right Hebrew or English layout per text field) guide](keyflip.md) · [Source](https://github.com/kivimedia/keyflip)

### Neutron Email Triage

`Open source` · `Free source build` · `BYOK`

Jev-first email classifier for Proton Mail through Proton Mail Bridge, with a Windows Electron GUI and a source CLI: dry-run by default, with optional moves to trash or archive above a confidence threshold.

**Jev's role:** Jev classifies each Proton Mail message so the app can keep, archive or trash it.

**Platform:** Windows x64 (preview installer, v0.1.0 pre-release); source CLI elsewhere is unofficial

**Product:** [github.com/Geneonosis/neutron-email-triage](https://github.com/Geneonosis/neutron-email-triage)

**Pricing / access:** Free preview installer and source build; you need a Proton plan with Bridge and pay your own TypeSafe usage. Checked 2026-10-17. Source inspected; live app not run on the review host.

[Full Neutron Email Triage guide](neutron-email-triage.md) · [Source](https://github.com/Geneonosis/neutron-email-triage)

### Qoresence

`Open source` · `Free` · `BYOK`

Local-first Windows 'gaming streaming observatory' for PS5 + capture card + DualSense (Madden 27 / College Football): HDMI video, controller HID and game situation become one causal event bus surfaced through overlays, clips and a pull-only AgentGlass/MCP; with opt-in TypeSafe Jev, typed score-plausibility and ticket checks keep the board dark instead of painting an unconfirmed score — Jev never mints score digits.

**Access:** clone the [MIT source](https://github.com/ConWan30/Qoresence) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Qoresence guide](qoresence.md) · [Source](https://github.com/ConWan30/Qoresence)

### RimWorld Autopilot

`Open source` · `Free`

Experimental autonomous colony manager for RimWorld 1.6 on Windows: Laya — the open, Jev-compatible System One decision model — runs locally, reads the map through a bundled RIMAPI mod, picks what matters next and issues real in-game orders (food, building, work, trade, caravans, raids), with a desktop app to watch its reasoning and change priorities.

**Access:** download the free Windows installer or build the [GPL-3.0 source](https://github.com/Georgy-hook/rimworld-autopilot). Local Laya model, no API key. Source inspected; app not run on the review host.

[Full RimWorld Autopilot guide](rimworld-autopilot.md) · [Source](https://github.com/Georgy-hook/rimworld-autopilot)

### SignalLens

`Open source` · `Free source build` · `BYOK`

Privacy-conscious local-first chat signal analyzer: on-device redaction, then TypeSafe Jev judges emotion, intent, and engagement for a closeness index. Windows portable exe or Streamlit source.

**Access:** download the [MIT Windows portable release](https://github.com/xinian5216/chat-signal-analyzer/releases) or run the [source](https://github.com/xinian5216/chat-signal-analyzer) with a TypeSafe API key. No app purchase fee; TypeSafe usage is separate. Source inspected on Linux; Windows GUI/live Jev not run. Distinct from Crush Monitor / tg-crush.

[Full SignalLens guide](signal-lens.md) · [Source](https://github.com/xinian5216/chat-signal-analyzer)

### SoluTerminal (Windows workspace for Claude Code and Codex, with Jev smart approvals)

`Open source` · `Free`

Windows workspace that runs Claude Code and Codex side by side in PowerShell and WSL panes, keeps them running when the window closes, lets one agent ask another for a second opinion, and stops agents approving their own requests; Jev classifies each task into a tier and answers cautious permission prompts as smart approvals.

**Jev's role:** Tier classification and smart approvals: one Choice for the task tier and one Noul risk question, gated on confidence.

**Platform:** Windows; installer from soluterminal.com (free during beta) or build from source.

**Product:** [soluterminal.com/](https://soluterminal.com/)

**Pricing / access:** Open source (Apache-2.0); the Windows app is free during beta per soluterminal.com (future pricing not published). With your own key, Jev calls are billed to your TypeSafe account. Checked 2026-10-27. Source inspected; live app not run on the review host.

[Full SoluTerminal (Windows workspace for Claude Code and Codex, with Jev smart approvals) guide](soluterminal.md) · [Source](https://github.com/soluterminal/soluterminal)

## Browser extensions

### AI, SI, or Whatever

`Open source` · `Free source build` · `BYOK`

Chrome extension that lets TypeSafe Jev choose AI / SI / alternating / custom webpage terminology per page.

**Jev's role:** Optional Jev path scores short candidate snippets and picks the terminology mode.

**Platform:** Chrome extension

**Product:** [github.com/SjJ1017/ai-si-or-whatever#readme](https://github.com/SjJ1017/ai-si-or-whatever#readme)

**Pricing / access:** Free MIT source; optional TypeSafe key for Jev mode.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full AI, SI, or Whatever guide](ai-si-or-whatever.md) · [Source](https://github.com/SjJ1017/ai-si-or-whatever)

### Attention Vaccine (Chrome extension that flags manipulation techniques with Jev)

`Open source` · `Free`

Chrome extension that tags posts and articles using manipulation techniques such as rage bait, easy-money pitches, impersonation notices, dehumanizing language and unsupported assertions, without judging viewpoints or fact-checking.

**Jev's role:** Core: Jev answers one yes/no question per technique; a tag appears only above your sensitivity threshold.

**Platform:** Desktop Chrome, installed with Load unpacked (not on the Chrome Web Store yet).

**Product:** [github.com/nevrs/attention-vaccine](https://github.com/nevrs/attention-vaccine)

**Pricing / access:** Open source (MIT); free to install from source. Detection uses your own TypeSafe key. Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Attention Vaccine (Chrome extension that flags manipulation techniques with Jev) guide](attention-vaccine.md) · [Source](https://github.com/nevrs/attention-vaccine)

### Auto-Oui

`Open source` · `Free` · `BYOK`

Chrome extension (French UI) that watches a tab you enable and answers "Oui" — or clicks the approve button — when an AI agent on supported sites stops to ask for permission; detection is local rules by default with no network calls, and an optional Jev mode with your TypeSafe key judges ambiguous wording against a probability threshold (0.90 default). The README warns to keep it off for payments, messages, deletions and production actions.

**Access:** load the free [MIT extension](https://github.com/jasondupontbizz/auto-oui) unpacked; Jev mode is optional BYOK. Source inspected; extension not run on the review host.

[Full Auto-Oui guide](auto-oui.md) · [Source](https://github.com/jasondupontbizz/auto-oui)

### betterx

`Source available` · `Free source build` · `BYOK`

Chrome/Brave extension that classifies posts and replies on x.com with TypeSafe Jev as you browse — seven questions per post in one ~150–250 ms request (tone, post type, argument quality, racist, contempt for a nationality or immigrants, antisemitic, sexually explicit) — and labels, dims, blurs or hides them by your rules.

**Access:** load the [source](https://github.com/kalowery/betterx) (no LICENSE file — Source available) as an unpacked extension. No fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full betterx guide](betterx.md) · [Source](https://github.com/kalowery/betterx)

### Bilibili noise filter for Firefox (JEV)

`Open source` · `Free source build` · `BYOK`

Firefox (and Chrome) port of littlewindy123/jev-bili-filter: toggles for spoilers, trolling, ads and partisan chants, plus your own one-sentence rules, filter Bilibili comments and danmaku with TypeSafe Jev; adds local keywords that work without a key, per-item Canvas danmaku filtering, a block log and usage tracking.

**Access:** clone the [MIT source](https://github.com/Ray4AI/jev-bili-filter) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Bilibili noise filter for Firefox (JEV) guide](ray4ai-jev-bili-filter.md) · [Source](https://github.com/Ray4AI/jev-bili-filter)

### B站降噪 · JEV (Bilibili noise filter)

`Open source` · `Free` · `BYOK`

Original Chrome/Edge extension (Chinese, with English README) that filters Bilibili comments and plain-text danmaku on the page with TypeSafe Jev: four toggles — spoilers, trolling, ads and fandom flame wars — plus one-sentence custom rules, no blocklists or prompts to maintain. Upstream of the listed Firefox port.

**Access:** clone the [MIT source](https://github.com/littlewindy123/jev-bili-filter) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full B站降噪 · JEV (Bilibili noise filter) guide](jev-bili-filter.md) · [Source](https://github.com/littlewindy123/jev-bili-filter)

### Danmaku spoiler filter (JEV)

`Open source` · `Free source build` · `BYOK`

Zero-dependency Chrome extension (plus CLI) that has TypeSafe Jev judge whether Bilibili danmaku comments are spoilers and filters the hits, batching comments per request with a local cache; built to add other danmaku sites later. Docs in Chinese and English.

**Access:** clone the [MIT source](https://github.com/meetchen/jev-danmaku-filter) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Danmaku spoiler filter (JEV) guide](jev-danmaku-filter.md) · [Source](https://github.com/meetchen/jev-danmaku-filter)

### Fallacy Lens

`Open source` · `Free source build` · `BYOK`

Chrome extension: select text, right-click and Jev (via OpenRouter, your own key) scores it for 69 logical fallacies, showing the highest-scoring ones first with explanations.

**Jev's role:** Jev scores the text for each fallacy.

**Platform:** Chrome (load unpacked from source)

**Product:** [github.com/cobmuddybug/fallacylens-extension](https://github.com/cobmuddybug/fallacylens-extension)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Fallacy Lens guide](fallacy-lens.md) · [Source](https://github.com/cobmuddybug/fallacylens-extension)

### Flash (YouTube Q&A)

`Source available` · `Free` · `BYOK`

Chrome extension: ask a YouTube video a question by voice or text and it jumps to the answer, or highlights where the topic comes up, using TypeSafe Jev to score transcript segments.

**Jev's role:** Jev scores transcript passages (with chapter context) against your question; a confident top passage triggers a jump, otherwise lime peaks mark matching regions on the progress bar.

**Platform:** Chrome (Chrome Web Store 0.1.0, or load unpacked from source) · YouTube videos with English captions

**Product:** [chromewebstore.google.com/detail/flash/mcfkndmlbcdlmjgkdkjkaolcodjjopbp](https://chromewebstore.google.com/detail/flash/mcfkndmlbcdlmjgkdkjkaolcodjjopbp)

**Pricing / access:** Free on the Chrome Web Store (checked 2026-10-13); needs your own TypeSafe key (billed per search); optional OpenAI key for the Accurate voice mode.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Try Flash (YouTube Q&A)](https://chromewebstore.google.com/detail/flash/mcfkndmlbcdlmjgkdkjkaolcodjjopbp) · [Full Flash (YouTube Q&A) guide](flash-youtube.md) · [Source](https://github.com/surbhit20/jev-on-yt)

### Focus

`Open source` · `Free source build` · `BYOK`

Browser extension that uses TypeSafe Jev (via OpenRouter Decisions) to classify domains as productive or distracting and block distracting navigations, with local allow/block lists and cache.

**Access:** [load the GPL-3.0 source unpacked](https://github.com/bramtechs/Focus#install-chrome--edge--brave) (Chrome/Edge/Brave; Firefox temporary; Safari packaging script) with an OpenRouter API key. No app purchase fee; Decisions/Jev usage can incur charges. Source inspected; browser install and live calls not tested on the review host.

[Full Focus guide](focus.md) · [Source](https://github.com/bramtechs/Focus)

### Gmail notifications with Jev (Safari)

`Open source` · `Free source build` · `BYOK`

Free, open-source Safari extension for Gmail on Mac: write in plain language which emails deserve your attention, and Jev decides which new messages trigger a floating alert. Interface and docs are in Spanish.

**Jev's role:** Jev judges each new email against your plain-language alert criterion.

**Platform:** macOS Safari (source build)

**Product:** [github.com/jaumesaa/gmail-jev-notifications](https://github.com/jaumesaa/gmail-jev-notifications)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Gmail notifications with Jev (Safari) guide](gmail-jev-notifications-safari.md) · [Source](https://github.com/jaumesaa/gmail-jev-notifications)

### HookMeter

`Open source` · `Free source build` · `BYOK`

Chrome extension (optional FastAPI / Cloudflare Worker) that scores social-post drafts as you type with TypeSafe Jev—curiosity, emotional arousal, hook pattern, and clickbait risk—then shows a short rewrite hint. Distinct from jevx and Vibe Check for X.

**Access:** [load the MIT source unpacked](https://github.com/ehui1226/hookmeter-jev) (`extension/`) with a TypeSafe or OpenRouter key; optional local server or Cloudflare Worker. No app purchase fee; inference can incur charges. Source inspected; Chrome install and live calls not tested on the review host; bundled engine unit tests were not green without live mocks.

[Full HookMeter guide](hookmeter.md) · [Source](https://github.com/ehui1226/hookmeter-jev)

### Jev Check (browser extension)

`Open source` · `Free` · `BYOK`

Chrome and Firefox side-panel extension that asks the page you are reading your own question sets (yes/no, choice, score, multi-pick) and shows probability-ranked answers from Jev, optionally judged against your uploaded resume or checklist.

**Jev's role:** Answers each question in a set about the page's Markdown with typed probabilities; the panel ranks answers and highlights the winner.

**Platform:** Chrome (Chrome Web Store) and Firefox (Firefox Add-ons), Manifest V3.

**Product:** [chromewebstore.google.com/detail/acobeddijnaokjkpkmcdfoepbmibpicc](https://chromewebstore.google.com/detail/acobeddijnaokjkpkmcdfoepbmibpicc)

**Pricing / access:** Free extension on the Chrome Web Store and Firefox Add-ons; you pay your chosen provider for Jev calls. Checked 2026-10-19. Source inspected; live app not run on the review host.

[Full Jev Check (browser extension) guide](jev-check-extension.md) · [Source](https://github.com/amir9480/JevCheck)

### Jev Content Filter (hide classified ads that don't match your plain-language criteria)

`Open source` · `Free source build`

Browser extension for classified-ad and auction sites: you write what you want in plain Czech or English (price range, model year, condition), it asks Jev one yes/no question per ad in batches of ten, and collapses or dims the ads that don't match; works on Bazos.cz/.sk/.pl/.at today, with a modular design for other sites.

**Jev's role:** Per-ad yes/no filter: each ad's text goes to Jev as a Noul question against your criteria.

**Platform:** Chromium-based browsers; build from source and load unpacked. Work in progress.

**Product:** [github.com/Aladincz/Jev-Content-Filter](https://github.com/Aladincz/Jev-Content-Filter)

**Pricing / access:** Open source (MIT); free source build. Jev calls are billed to your own TypeSafe key. Checked 2026-10-27. Source inspected; live app not run on the review host.

[Full Jev Content Filter (hide classified ads that don't match your plain-language criteria) guide](jev-content-filter.md) · [Source](https://github.com/Aladincz/Jev-Content-Filter)

### Jev Content Guard

`Open source` · `Free source build` · `BYOK`

Chrome Manifest V3 extension that scans page text for fraud, advertising, AI slop, spam, clickbait, infobusiness, and toxicity with TypeSafe Jev (`jev-latest`), then shows badges or blur overlays from two-tier thresholds.

**Access:** install from the [Chrome Web Store](https://chromewebstore.google.com/detail/jev-content-guard/icdfmbedfjfodocdhpnecdjgofakeemn) or [load the MIT source unpacked](https://github.com/serejkaaa512/jev-content-guard-ext) (Developer mode) and paste a TypeSafe API key in the popup (`chrome.storage.local`). No app purchase fee; each analyzed block can incur provider charges. Source inspected; Chrome install and live page analysis not tested on the review host. Distinct from TypeSafe Fun AdBlocker (heuristic DOM ads) and Unclutter (clutter rules).

[Full Jev Content Guard guide](jev-content-guard.md) · [Source](https://github.com/serejkaaa512/jev-content-guard-ext)

### Jev Fit Scorer

`Open source` · `Free source build` · `BYOK`

Chromium extension (plus a dependency-free Node CLI) that scores the job posting you have open against your saved resume with one TypeSafe Jev request — fit 0–4 shown out of 10 with confidence, the single strongest factor, and optionally how likely the employer sponsors US visas — with cached results and per-call time and cost.

**Access:** load the [MIT source](https://github.com/akhil-neelam-ai/jev-fit-scorer) as an unpacked Chromium extension, or run the CLI. No fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full Jev Fit Scorer guide](jev-fit-scorer.md) · [Source](https://github.com/akhil-neelam-ai/jev-fit-scorer)

### Jev Focus (MateusRogien)

`Open source` · `Free source build` · `BYOK`

Chrome extension: keep YouTube for focus music/learning while TypeSafe Jev hides the rest (distinct from Focus / jev-focus-guard).

**Access:** Clone the [MIT source](https://github.com/MateusRogien/jev-focus) and follow upstream setup. No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live install/inference not tested on the review host.

[Full Jev Focus (MateusRogien) guide](mateusrogien-jev-focus.md) · [Source](https://github.com/MateusRogien/jev-focus)

### Jev Focus Guard

`Open source` · `Free source build` · `BYOK`

Local Chrome MV3 extension that asks TypeSafe Jev whether heuristically selected page elements are ads or distractions, then hides matches. Candidate state is metadata-only (no page body text). Distinct from Focus (domain block) and TypeSafe Fun AdBlocker.

**Access:** [load the MIT source unpacked](https://github.com/tx-smitht/jev-focus-guard) (Developer mode) with a TypeSafe API key. No app purchase fee; each judgment can incur provider charges. Source inspected; Chrome install and live browsing not tested on the review host.

[Full Jev Focus Guard guide](jev-focus-guard.md) · [Source](https://github.com/tx-smitht/jev-focus-guard)

### Jev for Chrome

`Open source` · `Free source build` · `BYOK`

Drive the Chrome tab you already have open with TypeSafe Jev. Community Manifest V3 port of browser-use/jev-ultrafast: Jev picks each click/keystroke/dropdown; a small text model fills TYPE_TEXT.

**Access:** build or load the [MIT source / releases](https://github.com/chy4pro/jev-for-chrome) as an unpacked Chromium extension with a TypeSafe (or OpenRouter/Cloudflare) key plus an OpenAI-compatible text helper. No app purchase fee; provider usage can incur charges. Offline vitest: 73 passed; Chrome install and live driving not tested on the review host.

[Full Jev for Chrome guide](jev-for-chrome.md) · [Source](https://github.com/chy4pro/jev-for-chrome)

### Jev for Gmail

`Open source` · `Free source build` · `BYOK`

Chrome extension: TypeSafe Jev priority-score badges on Gmail Primary (7-day window) with local redaction and patient-mail locks—does not change labels or read state.

**Access:** [load the MIT source unpacked](https://github.com/JeonKH81/jev-for-gmail) (Developer mode) with a TypeSafe API key in options. No app purchase fee; TypeSafe usage can incur charges. Source inspected; Chrome install and live Gmail/Jev not tested on the review host. Distinct from Jev Inbox (reorder) and Inbox Triage (label writes).

[Full Jev for Gmail guide](jev-for-gmail.md) · [Source](https://github.com/JeonKH81/jev-for-gmail)

### Jev Form Fill

`Open source` · `Free source build` · `BYOK`

Chrome extension that matches clipboard/source text to form fields with TypeSafe Jev, lets you review proposals, fill selected fields in page order, read back values, and undo—you submit the form yourself.

**Access:** Load unpacked from the [MIT source](https://github.com/takasek/jev-form-fill) (Chrome 116+). Bring a TypeSafe API key in the popup. No app purchase fee; TypeSafe usage billed separately. Source inspected; live form fills not run on the review host.

[Full Jev Form Fill guide](jev-form-fill.md) · [Source](https://github.com/takasek/jev-form-fill)

### Jev Inbox

`Open source` · `Free source build` · `BYOK`

Chrome extension that reorders Gmail’s list: unread first, critical on top, with your label chips—TypeSafe Jev (or Vercel AI Gateway) over row metadata only. Distinct from Jev Inbox Queue.

**Access:** [build and load unpacked](https://github.com/iamomiid/jev-inbox#install-from-source) (`npm run build` → `dist/`) with a TypeSafe or Vercel AI Gateway key. No app purchase fee; inference can incur charges. Source inspected; Chrome install and live Gmail/Jev not tested on the review host.

[Full Jev Inbox guide](jev-inbox.md) · [Source](https://github.com/iamomiid/jev-inbox)

### Jev Investment Forecast (jev-investment-forecast)

`Open source` · `Free source build` · `BYOK`

Chrome extension that inspects any displayed web page and uses TypeSafe Jev to forecast investment potential across 27 category judgments (50% positive-value threshold, 25% risk threshold) plus 2 choice questions (investment amount and duration).

**Access:** clone or load the MIT source (or the Chrome Web Store listing linked from the root README) with a TypeSafe Jev API key. No app purchase fee; API usage costs are separate. Source inspected; live calls not run on the review host.

[Full Jev Investment Forecast guide](jev-investment-forecast.md) · [Source](https://github.com/serejkaaa512/jev-investment-forecast)

### Jev Mail (Gmail extension)

`Open source` · `Free source build` · `BYOK`

Open-source Chrome/Brave extension that classifies Gmail with TypeSafe Jev — category, priority, important, needs-reply and junk as separate narrow questions — then applies `Jev/...` labels and previews safe, Trash-only cleanup with Undo; runs in the browser with your TypeSafe or OpenRouter key.

**Access:** load the [MIT source](https://github.com/KirtanUgreja/jev-mail) as an unpacked extension. No fee; bring your own TypeSafe or OpenRouter key (usage billed by the provider). Source inspected; not run on the review host.

[Full Jev Mail (Gmail extension) guide](kirtanugreja-jev-mail.md) · [Source](https://github.com/KirtanUgreja/jev-mail)

### Jev Review (Gmail)

`Open source` · `Free source build` · `BYOK`

Chrome extension that grades Gmail compose/reply text with TypeSafe Jev on configurable criteria and tracks which questions from the other person's email remain unanswered.

**Access:** Load unpacked from the [MIT source](https://github.com/petrzpav/jev-review) in chrome://extensions; paste a TypeSafe key in options. No app purchase fee; TypeSafe usage billed separately. Source inspected; live Gmail grading not run on the review host.

[Full Jev Review (Gmail) guide](petrzpav-jev-review.md) · [Source](https://github.com/petrzpav/jev-review)

### Jev Slop Detector

`Source available` · `Free source build` · `BYOK`

Unofficial Chrome extension (with a local Node relay holding your key) that labels posts on your X feed with a TypeSafe Jev classification probability such as `● Slop | 83%`; it never hides or edits posts. The repo also holds SylphAI's class material for teaching Jev and the demo-recording scripts.

**Access:** clone the [source](https://github.com/SylphAI-Inc/jev-slop-detector) (no LICENSE file — source available), start the relay and load the extension unpacked. No app fee; requires your own TypeSafe key (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full Jev Slop Detector guide](jev-slop-detector.md) · [Source](https://github.com/SylphAI-Inc/jev-slop-detector)

### Jev Slop Guard

`Open source` · `Free source build` · `BYOK`

Chrome extension that scores and stamps AI slop on X and LinkedIn feeds with TypeSafe Jev as you scroll.

**Access:** [build/load the MIT source unpacked](https://github.com/davertor/jev-slop-guard) (Chrome MV3) with a TypeSafe API key. No app purchase fee; inference can incur charges. Source inspected; Chrome install and live feed scoring not tested on the review host. Distinct from LinkedIn Slop Filter and JevSlop.

[Full Jev Slop Guard guide](jev-slop-guard.md) · [Source](https://github.com/davertor/jev-slop-guard)

### Jev ToS Checker (Chrome extension that flags terms-of-service clauses that may work against you)

`Open source` · `Free` · `BYOK`

Chrome extension that, on request, splits the terms of service or privacy policy on the current page into clauses, has Jev check each against five risk types, and lists the flagged clauses with their original text, scrolling to each on the page; works on any site and in any language; English and Japanese UI.

**Jev's role:** Clause judge: each clause is asked five typed risk questions, and the flagged ones are shown.

**Platform:** Chrome (installed from a downloaded release folder; not on the Chrome Web Store at review time).

**Product:** [shohei81.github.io/jev-tos-checker/](https://shohei81.github.io/jev-tos-checker/)

**Pricing / access:** Open source (MIT); free from GitHub Releases (v0.3.1). Jev calls are billed to your TypeSafe key, or handled by a server you are given. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Jev ToS Checker (Chrome extension that flags terms-of-service clauses that may work against you) guide](jev-tos-checker.md) · [Source](https://github.com/shohei81/jev-tos-checker)

### Jev Tweet Radar

`Open source` · `Free source build` · `BYOK`

Chrome MV3 (optional iOS Safari Web Extension) that scores each visible X post with one TypeSafe Jev System One call—worth engaging, buzz, spam, AI-ish, and related tags—shown in the avatar column. Distinct from Jev Slop Guard and jev-x-filter.

**Access:** [load the MIT source unpacked](https://github.com/DDnim/jev-tweet-radar) with a TypeSafe API key in options; optional Xcode Safari project for iOS. No app purchase fee; each judgment can incur provider charges. Source inspected; Chrome/Safari install and live X scoring not tested on the review host.

[Full Jev Tweet Radar guide](jev-tweet-radar.md) · [Source](https://github.com/DDnim/jev-tweet-radar)

### Jev X Blocker (Chrome extension that hides high-confidence porn and spam on X with your own Jev key)

`Open source` · `Free` · `BYOK`

Local-first Chrome extension that uses your own TypeSafe key to cover high-confidence pornographic, sexually suggestive and porn-funnel posts and replies on X with restorable placeholders, across timelines, search, profiles and threads; a refactor and extension of bugkiwi's elons-job; Chinese documentation.

**Jev's role:** Content judge: the username and post or reply text go to Jev, and items above the confidence threshold are hidden behind a placeholder.

**Platform:** Chrome and Edge (unpacked from the v1.0.0 release zip); not on the Chrome Web Store at review time.

**Product:** [github.com/bit-cook/Jev-X-Blocker](https://github.com/bit-cook/Jev-X-Blocker)

**Pricing / access:** Open source (MIT); free download from GitHub Releases. Jev calls are billed to your TypeSafe account. Without a key nothing is hidden. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Jev X Blocker (Chrome extension that hides high-confidence porn and spam on X with your own Jev key) guide](jev-x-blocker.md) · [Source](https://github.com/bit-cook/Jev-X-Blocker)

### Jev × WebMCP

`Open source` · `Free source build` · `BYOK`

Chrome side panel that uses TypeSafe Jev to select and populate WebMCP tool calls from keystrokes on the current page; converts page tool schemas into Jev questions and shows confidence/latency, with per-site permissions and confirmation for non-readOnly/consequential tools.

**Access:** [load the Apache-2.0 source unpacked](https://github.com/sdras/jev-webmcp-extension#set-it-up) on Chrome 149+ with WebMCP (origin trial or `chrome://flags/#enable-webmcp-testing`) and a TypeSafe API key in extension settings (`chrome.storage.local`). No app purchase fee; TypeSafe usage can incur charges. Not verified on the Chrome Web Store. Offline `npm test`: 16 passed on the review host; Chrome install and live TypeSafe/WebMCP not tested.

[Full Jev × WebMCP guide](jev-webmcp-extension.md) · [Source](https://github.com/sdras/jev-webmcp-extension)

### jev-email-classifier

`Open source` · `Free source build` · `BYOK`

Chrome MV3 extension that classifies Gmail rows with TypeSafe Jev (Choice/Score/Noul); metadata-only, BYOK.

**Access:** Clone the [MIT source](https://github.com/AkashNaickar/jev-email-classifier) and follow upstream setup with a TypeSafe/provider key when live. No app purchase fee for the source build; provider usage is separate. Source inspected; live install/inference not tested on the review host.

[Full jev-email-classifier guide](jev-email-classifier.md) · [Source](https://github.com/AkashNaickar/jev-email-classifier)

### jev-x-filter

`Open source` · `Free source build` · `BYOK`

Chrome MV3 extension: TypeSafe Jev filters X timeline spam (six classes) with high-confidence mute/block and default dry-run.

**Access:** load the [MIT source](https://github.com/harodggg/jev-x-filter) unpacked in Chrome with a TypeSafe key. No app purchase fee; provider usage separate. Source inspected; live X filtering not tested.

[Full jev-x-filter guide](jev-x-filter.md) · [Source](https://github.com/harodggg/jev-x-filter)

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

### L Ragebait

`Open source` · `Free`

Chrome extension that conservatively hides high-confidence ragebait, hostile threads and sensationalised tragedy commentary on X and YouTube, using three Jev noul scores per item in one request against a threshold you set (default 0.85).

**Jev's role:** Jev scores each visible item on three yes/no questions; the extension hides items above your threshold.

**Platform:** Chrome or Chromium desktop; build from source and load unpacked.

**Product:** [github.com/davidherring123/l-ragebait](https://github.com/davidherring123/l-ragebait)

**Pricing / access:** Free MIT source; you pay for your own Jev calls. Checked 2026-10-20. Source inspected; live app not run on the review host.

[Full L Ragebait guide](l-ragebait.md) · [Source](https://github.com/davidherring123/l-ragebait)

### LinkedIn Slop Filter

`Open source` · `Free source build` · `BYOK`

Chrome extension + local Node proxy: TypeSafe Jev stamps LinkedIn posts Bait/Corp/Brag/Slop (distinct from Slop Mop writing scores).

**Access:** clone the [MIT source](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter) (Node ≥ 20 for `server/`), put a TypeSafe key in `.env`, run the localhost proxy, load `extension/` unpacked. No Chrome Web Store listing (key stays local). Source inspected; Chrome/live Jev not run on the review host.

[Full LinkedIn Slop Filter guide](jev-linkedin-slop-filter.md) · [Source](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter)

### LinkScout

`Open source` · `Free source build` · `BYOK`

Browser extension plus your own Cloudflare Worker that scores Google, Bing and DuckDuckGo results before you click: pages are fetched as Markdown and TypeSafe Jev judges relevance, depth, SEO spam and category and picks a key passage.

**Access:** deploy the [MIT source](https://github.com/ianTPE/linkscout) Worker with Wrangler and load the extension unpacked. No fee; your Cloudflare, TypeSafe and optional Jina usage is billed by those providers. Source inspected; not run on the review host.

[Full LinkScout guide](linkscout.md) · [Source](https://github.com/ianTPE/linkscout)

### Noa

`Open source` · `Pricing unverified` · `BYOK`

Chrome extension for browser automation in your own logged-in Chrome: Claude Code plans each task and TypeSafe Jev picks what to click and type step by step.

**Jev's role:** Jev carries out single steps (which element to click, what to type) so runs don't wait on a full Claude turn per click; Claude plans and handles the rest.

**Platform:** Chrome extension + local helper

**Product:** [www.noa.bot](https://www.noa.bot)

**Pricing / access:** Free MIT source with your own Claude plan/key and Jev key; voice and Noa-hosted Jev need a Noa account plan ([pricing](https://www.noa.bot/pricing), not verified here).

**Access:** Source inspected at a pinned commit; not run on the review host.

[Try Noa](https://www.noa.bot) · [Full Noa guide](noa.md) · [Source](https://github.com/m0dE/noa)

### PageGrade

`Open source` · `Free source build` · `BYOK`

Grade readable page sections for clarity, writing, and on-page SEO with TypeSafe Jev Score rubrics via the Vercel AI Gateway; inspect an A–E page summary in Chrome's side panel.

**Access:** [build with Bun and load unpacked](https://github.com/kitze/pagegrade#install-locally) (`.output/chrome-mv3`) with a Vercel AI Gateway API key. No app purchase fee; Gateway/Jev usage can incur charges. Source inspected; Chrome install and live grading not tested on the review host.

[Full PageGrade guide](pagegrade.md) · [Source](https://github.com/kitze/pagegrade)

### Please.exe

`Open source` · `Free`

Private tone coach for Claude and ChatGPT prompts: a local tone meter with suggested edits, plus an optional, explicitly confirmed TypeSafe Jev second opinion.

**Jev's role:** Optional: after you confirm, Jev gives a second opinion on a draft's tone in a separate extension tab; local rules do the default rating.

**Platform:** Chrome extension (beta release zip) · web playground

**Product:** [hyper186.github.io/please-exe/](https://hyper186.github.io/please-exe/)

**Pricing / access:** Free; local mode needs no key. Jev second opinions use your own TypeSafe key (see docs/JEV-SETUP.md).

**Access:** Source inspected at a pinned commit; not run on the review host.

[Try Please.exe](https://hyper186.github.io/please-exe/) · [Full Please.exe guide](please-exe.md) · [Source](https://github.com/hyper186/please-exe)

### Polymorph

`Open source` · `Free source build` · `BYOK`

Collapse posts that match English rules you wrote; TypeSafe Jev via OpenRouter Decisions is the judge. Matched posts become your images/GIFs or a compact card—Show original restores them.

**Access:** [build with pnpm and load unpacked](https://github.com/moomooskycow/polymorph#load) (`dist/`) with an OpenRouter API key. No app purchase fee; Decisions/Jev usage can incur charges. Not Chrome Web Store listed. Source inspected; Chrome install and live feed judging not tested on the review host.

[Full Polymorph guide](polymorph.md) · [Source](https://github.com/moomooskycow/polymorph)

### Qiaomu Banbot (乔木净评)

`Free` · `Source available` · `BYOK`

Chrome extension preview that uses TypeSafe Jev (or Magpie / OpenRouter / Vercel gateways) to fold suspected AI, low-signal, and promo replies on X, with optional natural-language rules and hot-post probability estimates.

**Jev's role:** Jev scores each reply (and optional hot-post questions) over the System One or Decisions wire format; the extension folds or marks based on thresholds you set.

**Platform:** Chrome / Chromium (preview release; not yet on the Chrome Web Store).

**Product:** [github.com/joeseesun/qiaomu-ban-bot](https://github.com/joeseesun/qiaomu-ban-bot)

**Pricing / access:** Free source / preview build; you supply your own provider key and pay that provider. Source inspected; live app not run on the review host.

[Full Qiaomu Banbot (乔木净评) guide](qiaomu-ban-bot.md) · [Source](https://github.com/joeseesun/qiaomu-ban-bot)

### Quiet X

`Open source` · `Free source build` · `BYOK`

Open-source Chrome extension that silently hides X ads and posts by account country, language or topic; optional language/topic rules are judged by TypeSafe Jev on the rendered post text through a small local proxy that holds your key.

**Access:** build from the [MIT source](https://github.com/arzumanabbasov/quiet-x) or download the v1.2.2 release and load it unpacked. AI filters need your own TypeSafe key in the local proxy (usage billed by TypeSafe). Source inspected; not run on the review host.

[Full Quiet X guide](quiet-x.md) · [Source](https://github.com/arzumanabbasov/quiet-x)

### Reddit Pain

`Open source` · `Free` · `BYOK`

Chrome extension that labels Reddit posts and comments as you scroll and boxes the ones asking for a product or describing a pain (with intensity 0–3), using TypeSafe Jev with your own key.

**Jev's role:** Jev labels each post/comment that scrolls into view (product request, pain, intensity); the extension draws boxes and caches labels.

**Platform:** Chrome (unpacked extension from release zip)

**Product:** [github.com/Tribespencer/reddit-pain#readme](https://github.com/Tribespencer/reddit-pain#readme)

**Pricing / access:** Free MIT extension; every labelled item is one TypeSafe API call billed to your key. Checked 2026-10-13.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Reddit Pain guide](reddit-pain.md) · [Source](https://github.com/Tribespencer/reddit-pain)

### Regret Check

`Open source` · `Free source build` · `BYOK`

Chrome extension + local FastAPI server that pauses commit-like clicks when TypeSafe Jev (OpenRouter) scores high regret risk.

**Access:** run the [MIT source](https://github.com/danilocecilia/sleep-on-it) server (`uvicorn` :8001) with an OpenRouter key as `TYPESAFE_API_KEY`, then Load unpacked `extension/`. No app purchase fee; provider usage is separate. Keep keys on the server only. Source inspected; Chrome/live scoring not run on the review host.

[Full Regret Check guide](regret-check.md) · [Source](https://github.com/danilocecilia/sleep-on-it)

### ScrollPatrol

`Open source` · `Free source build` · `BYOK`

Chrome extension that mutes feed posts by meaning: TypeSafe Jev scores each post against your mute rules on LinkedIn, Reddit, Hacker News, and selected short-video surfaces.

**Access:** build and [load the MIT source unpacked](https://github.com/ennsharma/scrollpatrol) (`npm run build`, Chromium) with a TypeSafe API key. No app purchase fee; TypeSafe usage can incur charges. Offline vitest 40 passed after build; Chrome install and live calls not run on the review host.

[Full ScrollPatrol guide](scrollpatrol.md) · [Source](https://github.com/ennsharma/scrollpatrol)

### SearchJev

`Open source` · `Free` · `BYOK`

Firefox extension (Japanese UI) that asks Jev six questions about each Google result, then shows 0 to 100 scores and reorders the page to push mass-produced SEO and affiliate articles down and first-hand sources up; one click restores Google's order.

**Jev's role:** Jev answers six typed questions per search result; the extension weights the answers into a score and reorders the page.

**Platform:** Firefox desktop and Android

**Product:** [addons.mozilla.org/ja/firefox/addon/searchjev/](https://addons.mozilla.org/ja/firefox/addon/searchjev/)

**Pricing / access:** Free add-on (MIT); you pay your own TypeSafe usage. Checked 2026-10-18. Source inspected; live app not run on the review host.

[Full SearchJev guide](searchjev.md) · [Source](https://github.com/mita-pixels/searchjev)

### Signal & Noise

`Source unverified` · `Free source build` · `BYOK`

Chrome extension that hides X timeline posts you don't want: tap noise bubbles (rage bait, crypto shilling, engagement bait, spoilers…) or write your own in plain words, and TypeSafe Jev judges each tweet with one `choice` question (keep vs each mute) before it scrolls into view; hidden posts fold into a bar that says why, and your Good hide / Shouldn't have hidden feedback is kept locally.

**Access:** load the [source](https://github.com/icpmacdo/signal-and-noise) as an unpacked Chrome extension. No fee; requires your own TypeSafe API key (usage billed by TypeSafe) or another configured route. No LICENSE file. Source inspected; extension not run on the review host.

[Full Signal & Noise guide](signal-and-noise.md) · [Source](https://github.com/icpmacdo/signal-and-noise)

### Signal Feed (X and YouTube bait filter with Jev)

`Open source` · `Free source build`

Chromium extension that folds ragebait, empty hype and engagement bait on the X timeline and YouTube before you scroll to them, each with the reason, highlights posts on topics you choose, and shows what the Jev calls cost.

**Jev's role:** Jev answers one yes-or-no question per post (hide under your list?) plus one for highlights, in batches ahead of your scroll.

**Platform:** Chromium browsers, loaded unpacked from source or a release zip; Chrome Web Store listing announced as coming soon.

**Product:** [github.com/harish-anumula/signal-feed](https://github.com/harish-anumula/signal-feed)

**Pricing / access:** Open source (MIT); free to load. Jev usage is billed to your OpenRouter key; the author measured about $0.02 per 1,000 posts on 2026-10-23. Checked 2026-10-23. Source inspected; live app not run on the review host.

[Full Signal Feed (X and YouTube bait filter with Jev) guide](signal-feed.md) · [Source](https://github.com/harish-anumula/signal-feed)

### Skipto

`Open source` · `Free source build` · `BYOK`

Chrome extension that answers a question about a YouTube video by asking TypeSafe Jev a Choice over ~30-second transcript windows plus a yes/no “is it covered at all?” check, then highlights the progress bar and jumps to the best moment.

**Access:** load the [MIT source](https://github.com/jinukuntlaakhilakumargoud-web/skipto) as an unpacked extension. No fee; bring your own key (usage billed by the provider). Source inspected; not run on the review host.

[Full Skipto guide](skipto.md) · [Source](https://github.com/jinukuntlaakhilakumargoud-web/skipto)

### Slop Mop

`Open source` · `Free` · `BYOK`

Judge LinkedIn post writing with TypeSafe Jev (11–12 typed questions), then fold or highlight suspected slop with inspectable scores and local overrides. Not an AI detector. Distinct from JevSlop (note/article scoring).

**Access:** free hosted use via [slopmop.lol](https://slopmop.lol) (no signup; daily check limits on the maintainer's server, default 250/install/UTC day) or [self-host the MIT source](https://github.com/tomfrazier/slopmop) with your own TypeSafe/AI Gateway key. Desktop Chromium / LinkedIn only; load unpacked from a local build. No Chrome Web Store listing verified. Source and offline vitest inspected; Chrome install and live LinkedIn/Jev not tested on the review host.

[Full Slop Mop guide](slop-mop.md) · [Source](https://github.com/tomfrazier/slopmop)

### Smart Dark (adaptive dark mode with optional Jev screenshot checks)

`Open source` · `Free source build`

Chrome extension that darkens websites by using a site's own dark theme when it has one and otherwise rewriting its colours while keeping layout, hover states and brand colours; optional Jev screenshot checks decide whether a page should stay dark or return to its original look.

**Jev's role:** Optional: Jev looks at a screenshot of the darkened page and decides whether to keep the dark theme or restore the original.

**Platform:** Chrome desktop, loaded unpacked from a release zip or source build; not on the Chrome Web Store.

**Product:** [github.com/ThrownLemon/smart-dark](https://github.com/ThrownLemon/smart-dark)

**Pricing / access:** Open source (MIT); free to load from a release or source. Jev checks use your own TypeSafe key and are capped at 30 image checks per UTC day. Checked 2026-10-23. Source inspected; live app not run on the review host.

[Full Smart Dark (adaptive dark mode with optional Jev screenshot checks) guide](smart-dark.md) · [Source](https://github.com/ThrownLemon/smart-dark)

### Smart Find

`Open source` · `Free source build` · `BYOK`

Chrome extension that works like Ctrl+F for questions: ask a page a question and TypeSafe Jev scores page passages so the answers are highlighted.

**Jev's role:** Jev scores each passage (with its section heading) against your question, 8 passages per request; code highlights matches and marks the scrollbar.

**Platform:** Chrome (load unpacked)

**Product:** [github.com/eduardoalba00/smart-find#readme](https://github.com/eduardoalba00/smart-find#readme)

**Pricing / access:** Free MIT extension; each search is billed to your TypeSafe key (upstream reports US$0.0005–0.007).

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Smart Find guide](smart-find.md) · [Source](https://github.com/eduardoalba00/smart-find)

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

### Tab Bouncer

`Open source` · `Free source build` · `BYOK`

Rate open tabs for a task you type with TypeSafe Jev, then close the ones that do not belong. Distinct from Jev for Chrome (computer-use driver): bulk triage with keep noul + kind choice per tab, batches of up to 120.

**Access:** [load the MIT source as an unpacked Chromium extension](https://github.com/MANISH007700/tab-bouncer#install) and paste a TypeSafe key in options. No app purchase fee; inference usage can incur charges. Offline `node --test`: 7 passed; Chrome install and live TypeSafe calls not tested on the review host.

[Full Tab Bouncer guide](tab-bouncer.md) · [Source](https://github.com/MANISH007700/tab-bouncer)

### Tab Land

`Open source` · `Free source build` · `BYOK`

Chrome extension that finds any tab fast, groups tabs by the job you are doing, and closes stale ones; with a Jev key, Jev double-checks each group, removes tabs that do not fit, and names groups.

**Jev's role:** Optional judge that asks typed questions like whether tabs serve one goal and what kind of work a tab is.

**Platform:** Chrome (load unpacked from source; no Chrome Web Store listing verified).

**Product:** [github.com/robin-anil/tab-land](https://github.com/robin-anil/tab-land)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Tab Land guide](tab-land.md) · [Source](https://github.com/robin-anil/tab-land)

### TabTidy

`Open source` · `Free source build` · `BYOK`

Chrome MV3 extension that filters tabs locally (active, pinned, audible, downloading stay), then sends one Jev request with a KEEP / CLOSE / UNCERTAIN choice question per remaining tab; it closes only what you confirm (one-click undo through Chrome sessions) and turns your corrections into domain rules that override Jev next time.

**Access:** load the [MIT source](https://github.com/123456342g-lang/tabtidy) as an unpacked Chrome extension. No fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; extension not run on the review host.

[Full TabTidy guide](tabtidy.md) · [Source](https://github.com/123456342g-lang/tabtidy)

### Tabwerk

`Open source` · `Free`

German-language Chrome extension for people with many tabs: quick search, groups, sorting, duplicates, page watchers and full history, where exact work is done in code and optional Jev calls answer the semantic questions (find a tab by description, suggest groups, rank priority, judge watcher conditions).

**Jev's role:** Optional: Jev handles the semantic features (find, group, prioritise, duplicate content, watchers); everything else works without it.

**Platform:** Chrome Web Store; interface in German.

**Product:** [chromewebstore.google.com/detail/tabwerk/jimalfhplojokembebogjlplobgoobdg](https://chromewebstore.google.com/detail/tabwerk/jimalfhplojokembebogjlplobgoobdg)

**Pricing / access:** Free MIT extension; Jev calls are billed to your own OpenRouter or TypeSafe key. Checked 2026-10-21. Source inspected; live app not run on the review host.

[Full Tabwerk guide](tabwerk.md) · [Source](https://github.com/DigitalIQ/tabwerk)

### Text-Only YouTube (userscript with Jev genre tags)

`Open source` · `Free`

Violentmonkey userscript that turns YouTube into a plain list of titles without thumbnails, avatars or Shorts; one click sends the visible titles to Jev to tag each video with a genre icon you can filter by.

**Jev's role:** Optional: one choice question per video assigns a genre from the list in `GENRES`; a ring marks low-confidence answers.

**Platform:** Desktop browsers with Violentmonkey.

**Product:** [github.com/JohnVonDrashek/youtube-text-only](https://github.com/JohnVonDrashek/youtube-text-only)

**Pricing / access:** Open source (MIT); free userscript. Genre tagging uses your own TypeSafe key (the README estimates about a twentieth of a cent per 30 videos). Checked 2026-10-24. Source inspected; live app not run on the review host.

[Full Text-Only YouTube (userscript with Jev genre tags) guide](text-only-youtube.md) · [Source](https://github.com/JohnVonDrashek/youtube-text-only)

### ToS Decipher (terms-of-service and privacy-policy reviewer whose claims are checked by Jev)

`Open source` · `Free source build` · `BYOK`

English and Spanish web app, Chrome/Edge MV3 extension and Python API that summarise terms of service and privacy policies, highlight important clauses next to their source text and find policy links on a page; Jev classifies links and verifies each finding against the source passages.

**Jev's role:** Core: with `TYPESAFE_API_KEY` set, Jev classifies policy links and verifies the generated claims in one bundled request; policy analysis itself uses an OpenRouter model.

**Platform:** Chrome/Edge extension loaded unpacked, talking to a local API at `localhost:8000`; not packaged for general distribution.

**Product:** [github.com/javierBrenesAI/ToS-Defender](https://github.com/javierBrenesAI/ToS-Defender)

**Pricing / access:** Open source (MIT); free source build. You supply OpenRouter and TypeSafe keys. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full ToS Decipher (terms-of-service and privacy-policy reviewer whose claims are checked by Jev) guide](tos-decipher.md) · [Source](https://github.com/javierBrenesAI/ToS-Defender)

### Tube Focus Mode

`Open source` · `Free source build` · `BYOK`

Chrome extension that filters YouTube down to your channels, playlists and chosen topics: Jev scores each other video against your focus topics, and off-topic videos are blurred or blocked.

**Jev's role:** Jev decides whether each non-allowlisted video matches your focus topics.

**Platform:** Chrome and Chromium browsers (unpacked source build)

**Product:** [github.com/OriolSegarra/tube-focus-mode](https://github.com/OriolSegarra/tube-focus-mode)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Tube Focus Mode guide](tube-focus-mode.md) · [Source](https://github.com/OriolSegarra/tube-focus-mode)

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

### Vertika Command

`Closed source` · `Free` · `BYOK`

Chrome extension that runs your browser from spoken or typed English commands, with free in-browser Laya or TypeSafe Jev online with your own key.

**Jev's role:** Optional fast cloud model that turns a command plus page context into the browser action to run.

**Platform:** Chrome extension (Chrome Web Store 0.7.0) · English only

**Product:** [command.vertika.io](https://command.vertika.io/)

**Pricing / access:** Free; Jev option needs your own TypeSafe or OpenRouter key (about $0.0002 per command per the site). Closed source. Checked 2026-10-19.

**Access:** No public source; product site and Chrome Web Store listing reviewed; not run on the review host.

[Try Vertika Command](https://chromewebstore.google.com/detail/vertika-command-run-your/lhjeopjappljkcdgjhiafhobjafmmhmh) · [Full Vertika Command guide](vertika-command.md) · [Product site](https://command.vertika.io/)

### Vibe Check for X

`Source unverified` · `Pricing unverified` · `BYOK`

Review draft X posts, replies, and quote posts with a scorecard inside the composer. Jev judges qualities such as clarity, humor, and regret risk; JavaScript combines the judgments into a verdict. Optional OpenAI vision calls describe media for Jev.

**Access:** load the source folder as an unpacked Chrome extension and supply a TypeSafe key; media descriptions need an OpenAI key. No license file or explicit app pricing terms were found. Provider calls can incur charges, auto-analysis is enabled by default, and keys use Chrome sync storage. Source and syntax were checked; Chrome installation and live scoring were not tested.

[Full Vibe Check guide](vibecheck.md) · [Source](https://github.com/RafalWilinski/vibecheck)

### Xift

`Open source` · `Free source build` · `BYOK`

Firefox add-on that collapses noise on your X timeline: TypeSafe Jev (via OpenRouter) scores each post for engagement bait, rage bait, low substance, and self-promotion, and posts over your thresholds fold to a one-line reason.

**Jev's role:** Jev answers four probability questions per post (text plus first photo); your thresholds, adjusted by Keep and Hide feedback, decide what collapses.

**Platform:** Firefox 140+ (run with web-ext or self-sign; no addons.mozilla.org listing verified).

**Product:** [github.com/asaidaoui-netria/xift](https://github.com/asaidaoui-netria/xift)

**Pricing / access:** Free source build; you pay OpenRouter per post judged (README estimates about 3 cents per 1,000 posts) with a default $1/month spending limit. Source inspected; live app not run on the review host.

[Full Xift guide](xift.md) · [Source](https://github.com/asaidaoui-netria/xift)

### XPostFilterPlus (Chrome extension that hides X posts by keyword or by Jev classification)

`Open source` · `Free source build`

Unofficial Chrome extension that hides X posts using keyword rules with case, accent and symbol normalisation, plus optional semantic exclusion conditions judged by Jev, OpenAI Decisions or Cloudflare Clef with your own key; settings open over the X page and a chip counts hidden posts; Japanese and English documentation.

**Jev's role:** Optional semantic filter: each post is checked against your exclusion conditions, one of three selectable providers.

**Platform:** Chrome (load unpacked from the dist folder); not in the Chrome Web Store at review time.

**Product:** [github.com/doraTeX/XPostFilterPlus](https://github.com/doraTeX/XPostFilterPlus)

**Pricing / access:** Open source (MIT); free source build. AI classification is billed by the provider you choose. Checked 2026-10-27. Source inspected; live app not run on the review host.

[Full XPostFilterPlus (Chrome extension that hides X posts by keyword or by Jev classification) guide](xpostfilterplus.md) · [Source](https://github.com/doraTeX/XPostFilterPlus)

### Xtags

`Open source` · `Free source build` · `BYOK`

Label each X timeline post with intent and thresholded risk signals. Jev answers four typed questions per post; the extension renders tags in the timeline.

**Access:** load the [MIT `extension/` folder unpacked](https://github.com/manifoldor/xtags#安装) (or the Tampermonkey userscript) and paste a TypeSafe key. No app purchase fee; provider usage can incur charges. Independent of X Corp. Source inspected; Chrome install and live labeling not tested.

[Full Xtags guide](xtags.md) · [Source](https://github.com/manifoldor/xtags)

### YouTube Sponsor Skip (Jev)

`Open source` · `Free` · `BYOK`

Chrome and Safari extension that detects in-video spoken sponsorships on Russian-language YouTube using TypeSafe Jev over subtitles and auto-skips them (pause, timecodes, daily spend cap).

**Jev's role:** Classifies subtitle windows as sponsor vs content (via OpenRouter `typesafe/jev-1.13`).

**Platform:** Chrome, Safari (macOS) · Manifest V3

**Product:** [GitHub README](https://github.com/AnatoliyLikarchuk/youtube-sponsor-skip#readme)

**Pricing / access:** Free MIT source build; needs your OpenRouter/TypeSafe-compatible key (usage billed by provider). Checked 2026-10-12.

**Access:** Load unpacked from source per README. Source inspected; extension not run on the review host.

[Full YouTube Sponsor Skip (Jev) guide](youtube-sponsor-skip.md) · [Source](https://github.com/AnatoliyLikarchuk/youtube-sponsor-skip)

## Command-line apps

### Albatross

`Open source` · `Free source build` · `BYOK`

Terminal-first coding harness (bring your own model, key or MCP server) with an experimental Jev Mode that puts TypeSafe's decision model before the main LLM.

**Jev's role:** Optional pre-LLM decision layer for supported questions.

**Platform:** macOS / Linux terminal (Homebrew or source)

**Product:** [github.com/morganlinton/Albatross](https://github.com/morganlinton/Albatross)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Albatross guide](albatross.md) · [Source](https://github.com/morganlinton/Albatross)

### Anki Review-Finder

`Open source` · `Free source build` · `BYOK`

Alpha CLI that audits Anki flashcards through AnkiConnect with TypeSafe Jev, flagging structural defects such as answer leaks, missing context, scope problems and binary questions, then writes priority and defect tags back to Anki (never card text) and produces an HTML report.

**Access:** clone the [MIT source](https://github.com/elias170105/anki-review-finder) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Anki Review-Finder guide](anki-review-finder.md) · [Source](https://github.com/elias170105/anki-review-finder)

### arJev

`Open source` · `Free source build` · `BYOK`

Daily arXiv digest engine: lexical front-line plus TypeSafe Jev confidence-gated rerank against an Obsidian vault.

**Access:** Clone the [Apache-2.0 source](https://github.com/harmoniqs/arjev) and follow upstream setup with a TypeSafe/provider key when live. No app purchase fee for the source build; provider usage is separate. Source inspected; live install/inference not tested on the review host.

[Full arJev guide](arjev.md) · [Source](https://github.com/harmoniqs/arjev)

### Better Email Filter (local Gmail triage with Jev that learns from your corrections)

`Source available` · `Free source build` · `BYOK`

Local command-line Gmail triage: Jev sorts messages into Spam, Ignore or Important, sends uncertain ones to Review, and the labels you correct in Gmail become examples for future classifications.

**Jev's role:** Core: Jev classifies each message and its confidence decides whether a label or Review is used.

**Platform:** macOS and Linux command line, run from source; Windows not supported.

**Product:** [github.com/miguelgarcia/better-email-filter](https://github.com/miguelgarcia/better-email-filter)

**Pricing / access:** Free source build; public source with no license file (no open-source license granted). Jev calls use your own TypeSafe key and are billed by TypeSafe. Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full Better Email Filter (local Gmail triage with Jev that learns from your corrections) guide](better-email-filter.md) · [Source](https://github.com/miguelgarcia/better-email-filter)

### buildornot (BUILD, MAYBE or DON'T BUILD verdicts on side-project ideas, judged by Jev)

`Open source` · `Free source build` · `BYOK`

Command-line tool that judges a side-project idea: it searches GitHub and Hacker News for prior art, has Jev rate pain, reach, feasibility and deal-breakers and how likely each match does the same job, and prints BUILD, MAYBE or DON'T BUILD with the reasons.

**Jev's role:** Core: Jev answers every judgment (levels out of five, deal-breakers, prior-art matches) and code turns them into a score and verdict.

**Platform:** Any OS with Python 3.10+; install with uvx or pipx from GitHub.

**Product:** [github.com/blakestone-x/buildornot](https://github.com/blakestone-x/buildornot)

**Pricing / access:** Open source (MIT); free. Jev calls use your own TypeSafe key (the README says a run is well under a cent). Checked 2026-10-25. Source inspected; live app not run on the review host.

[Full buildornot (BUILD, MAYBE or DON'T BUILD verdicts on side-project ideas, judged by Jev) guide](buildornot.md) · [Source](https://github.com/blakestone-x/buildornot)

### Clasificador de noticias regionales con Jev

`Open source` · `Free source build` · `BYOK`

Spanish-language Windows workflow that turns a monthly multi-portal news Excel into a reviewed list of Arequipa economic news, using Jev to classify headlines before scraping.

**Jev's role:** Jev classifies each Arequipa headline/summary as economic news before scraping.

**Platform:** Windows (Python source build)

**Product:** [github.com/EdgarTapara/clasificador-noticias-jev](https://github.com/EdgarTapara/clasificador-noticias-jev)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Clasificador de noticias regionales con Jev guide](clasificador-noticias-jev.md) · [Source](https://github.com/EdgarTapara/clasificador-noticias-jev)

### Gmail Classifier

`Open source` · `Free source build` · `BYOK`

Local Gmail triage CLI (uv): TypeSafe Jev classifies threads (category/priority), with phishing/unsubscribe helpers, confirm-then-apply labels, undo, and an optional Chrome sidebar panel.

**Access:** clone the [MIT source](https://github.com/leomfu/gmail-classifier) (`uv sync`) with Google OAuth desktop credentials and `TYPESAFE_API_KEY`. No app purchase fee; Google/TypeSafe billed separately. Source inspected; live Gmail/Jev not run. Distinct from Inbox Triage / JevZero.

[Full Gmail Classifier guide](gmail-classifier.md) · [Source](https://github.com/leomfu/gmail-classifier)

### Inbox Triage

`Open source` · `Free source build` · `BYOK`

Private-by-default Gmail labeler: local policy asks TypeSafe Jev (or OpenAI/Anthropic/rules) focused yes/no questions over trimmed excerpts, then adds triage labels only.

**Access:** clone the [MIT source](https://github.com/shimoverse/inbox-triage) (Python 3.11+, uv) with your Google OAuth desktop client; `TYPESAFE_API_KEY` for `--provider jev`. No app purchase fee; Google/TypeSafe billed separately. Source inspected; live Gmail/Jev not run.

[Full Inbox Triage guide](inbox-triage.md) · [Source](https://github.com/shimoverse/inbox-triage)

### inbox-jev

`Open source` · `Free source build` · `BYOK`

Self-hosted Gmail triage: every few minutes it asks Jev which category each new email belongs to, then labels, archives, unsubscribes from verified marketing and cold outreach, moves scams to Spam and leaves uncertain mail in the inbox for review.

**Jev's role:** Jev classifies each new email with a calibrated confidence; code applies per-category thresholds and actions.

**Platform:** Linux/macOS server or desktop (self-hosted Python service)

**Product:** [inboxjev.dev](https://inboxjev.dev)

**Pricing / access:** Free and MIT-licensed; self-hosted, you pay your own TypeSafe usage. Checked 2026-10-17. Source inspected; live app not run on the review host.

[Full inbox-jev guide](inbox-jev.md) · [Source](https://github.com/hellolitebox/litebox-inbox-jev)

### Jev Mail Classifier

`Open source` · `Free source build` · `BYOK`

Classify IMAP mail with Jev yes/no category judgments, then tag, move, flag, or notify from a Textual TUI and cron-friendly CLI.

**Access:** clone and run the [MIT source](https://github.com/parth-kp/jev-mail-classifier) (Python 3.10+) with `./install.sh`, a Jev provider key (TypeSafe, OpenRouter, or Vercel AI Gateway), and IMAP credentials (often an app password). No app purchase fee; provider and mailbox-host usage can incur charges. Offline pytest: 61 passed on the review host; live mailbox classification not run.

[Full Jev Mail Classifier guide](jev-mail-classifier.md) · [Source](https://github.com/parth-kp/jev-mail-classifier)

### Jev Mail Triage

`Open source` · `Free source build` · `BYOK`

Dry-run-first Proton Mail Bridge triage that uses TypeSafe Jev to flag spam and phishing before touching your mailbox.

**Jev's role:** Jev classifies messages for spam/phishing triage.

**Platform:** CLI with Proton Mail Bridge

**Product:** [github.com/soderlind/jev-mail-triage](https://github.com/soderlind/jev-mail-triage)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Jev Mail Triage guide](soderlind-jev-mail-triage.md) · [Source](https://github.com/soderlind/jev-mail-triage)

### Jev Personal Radar

`Source unverified` · `Free source build` · `BYOK`

Privacy-first daily info radar (Go): ranks GitHub Trending / Hacker News / inbox links with TypeSafe Jev into private GitHub Issues; MiniMax explains selected public items. Secrets stay in a private runner repo.

**Access:** clone the [public source](https://github.com/zhazhahuiyuxiaoxiao/jev-personal-radar) (Go 1.25+) and pin it from a private Actions repo with `TYPESAFE_API_KEY` + `MINIMAX_API_KEY`. No app purchase fee; providers billed separately. **No LICENSE file at tip**—not tagged Open source. Source inspected; live Jev/MiniMax/Actions not run.

[Full Jev Personal Radar guide](jev-personal-radar.md) · [Source](https://github.com/zhazhahuiyuxiaoxiao/jev-personal-radar)

### Jev Quiz Pilot

`Open source` · `Free source build` · `BYOK`

Python CLI that lets TypeSafe Jev navigate web quizzes in Chrome and logs every pick for measurement.

**Access:** clone the [MIT source](https://github.com/juanfabrega/jev-quiz-pilot) with TypeSafe credentials and Chrome. No app purchase fee; provider usage separate. Source inspected; live quiz runs not executed on the review host.

[Full Jev Quiz Pilot guide](juanfabrega-jev-quiz-pilot.md) · [Source](https://github.com/juanfabrega/jev-quiz-pilot)

### Jev Soundboard

`Open source` · `Free source build` · `BYOK`

Live AI soundboard that listens to a call (FaceTime, Zoom, Meet, Discord or a stream), transcribes it and lets TypeSafe Jev decide whether to react and which clip to play within about a second; 15 built-in synthesized sounds, local control panel and an optional Discord bot.

**Access:** clone the [MIT source](https://github.com/Kiggsworthy/jev-soundboard) and run with uv. No app fee; bring TypeSafe and OpenAI keys (usage billed by each provider). Source inspected; not run on the review host.

[Full Jev Soundboard guide](jev-soundboard.md) · [Source](https://github.com/Kiggsworthy/jev-soundboard)

### jev-crypto-scout

`Open source` · `Free source build` · `BYOK`

Crypto screening pipeline: quant signals from CoinGecko stay in code; TypeSafe Jev System One judges news for sentiment/catalyst/confirmed labels. Explicitly not a trading bot.

**Access:** Clone the [MIT source](https://github.com/yasdelayu/jev-crypto-scout) and follow README/USAGE with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe and market-data usage are separate. Source inspected; live scout runs not executed on the review host.

[Full jev-crypto-scout guide](jev-crypto-scout.md) · [Source](https://github.com/yasdelayu/jev-crypto-scout)

### jevelry

`Open source` · `Free source build` · `BYOK`

Terminal app to make and track everyday decisions with TypeSafe Jev, storing reusable “jevels” locally.

**Access:** Install from the [MIT npm/source](https://github.com/backant-io/jevelry) (Node ≥22) with a TypeSafe API key. No app purchase fee; TypeSafe usage may incur charges. Source inspected; live Jev not run.

[Full jevelry guide](jevelry.md) · [Source](https://github.com/backant-io/jevelry)

### Jevmeter

`Open source` · `Free source build` · `BYOK`

Annotate videos with Jev judgments about sentence-level rhetoric, then render overlays and highlights.

**Access:** [build the MIT Python CLI](https://github.com/ChetasLua/jevmeter#-command-line-for-power-users) with a Whisper backend, FFmpeg support and TypeSafe key. Source has no purchase fee; inference charges apply. The review inspected source only. Scores are model judgments, not fact-checks; failed sentences can be omitted.

[Full Jevmeter guide](jevmeter.md) · [Source](https://github.com/ChetasLua/jevmeter)

### keyed james bible

`Open source` · `Free source build` · `BYOK`

Turns a question into a span of King James Version verses by keying it through TypeSafe Jev choice requests (book and extent → chapter → verse) and clipping the passage verbatim from a local KJV corpus; nothing is generated, and the author documents measured Jev quirks.

**Access:** clone the [MIT source](https://github.com/mccartykim/keyed_james_bible) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full keyed james bible guide](keyed-james-bible.md) · [Source](https://github.com/mccartykim/keyed_james_bible)

### kureksistant

`Source available` · `Free source build` · `BYOK`

Arch Linux (Hyprland) personal AI assistant that uses TypeSafe Jev for sub-second decisions.

**Jev's role:** Jev makes fast personal-assistant judgments in the local loop.

**Platform:** Linux/Arch (source build)

**Product:** [github.com/nodaysidle/kureksistant](https://github.com/nodaysidle/kureksistant)

**Pricing / access:** Free source build where licensed; uses your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full kureksistant guide](kureksistant.md) · [Source](https://github.com/nodaysidle/kureksistant)

### Mardi Gras

`Open source` · `Free source build` · `BYOK`

Terminal UI for Beads agent issues that can use Jev as an optional fast judge for duplicate checks, focus order, formula choice and Codex approval risk advice.

**Jev's role:** Jev judges duplicates, ordering and risk; code and the user decide.

**Platform:** macOS / Linux terminal (Homebrew or source)

**Product:** [github.com/quietpublish/mardi-gras](https://github.com/quietpublish/mardi-gras)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full Mardi Gras guide](mardi-gras.md) · [Source](https://github.com/quietpublish/mardi-gras)

### meeting-ledger

`Open source` · `Free source build` · `BYOK`

Terminal app that keeps meetings on the record: Claude extracts decisions, action items, promises and open questions with cited transcript lines, a System One model (TypeSafe Jev or local Kev) checks proposed status changes across meetings, and anything the two disagree on waits for your review; stale promises are flagged.

**Access:** clone the [MIT source](https://github.com/owen-alderson/meeting-ledger) and run locally. No app purchase fee; requires your own TypeSafe API key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full meeting-ledger guide](meeting-ledger.md) · [Source](https://github.com/owen-alderson/meeting-ledger)

### Nectra

`Open source` · `Free source build` · `BYOK`

One chat in front of Claude Code, Codex, Gemini CLI and Ollama: each message is classified and routed to the model that should answer it, then that provider's real terminal opens.

**Jev's role:** Jev classifies each prompt's task type and needed capability; Nectra's scorer picks the model and runtime and explains why.

**Platform:** Command line (Rust)

**Product:** [github.com/MBarc/nectra#readme](https://github.com/MBarc/nectra#readme)

**Pricing / access:** Free MIT source; you use your existing provider subscriptions/keys plus a TypeSafe key.

**Access:** Source inspected at a pinned commit; not run on the review host.

[Full Nectra guide](nectra.md) · [Source](https://github.com/MBarc/nectra)

### Omarchy Mail

`Open source` · `Free source build` · `BYOK`

Terminal Gmail client for Omarchy; TypeSafe Jev files inbox into labels.

**Access:** Clone the [MIT source](https://github.com/petrzpav/omarchy-mail) and follow upstream setup. No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live install/inference not tested on the review host.

[Full Omarchy Mail guide](omarchy-mail.md) · [Source](https://github.com/petrzpav/omarchy-mail)

### pitwall

`Open source` · `Free` · `BYOK`

Native terminal multiplexer for coding agents (live status, persistent sessions, tabs/panes) that can connect TypeSafe Jev (`pitwall jev login`) to answer quick questions about your agents: is this permission request safe, how urgent is this pane, has a hook-less agent finished, does this turn need review.

**Access:** install the free [MIT binaries](https://github.com/quanticstudios/pitwall) with the upstream script (checksums verified). Jev decisions are opt-in and use your own TypeSafe key (usage billed by TypeSafe). Alpha software; source inspected, not run on the review host.

[Full pitwall guide](pitwall.md) · [Source](https://github.com/quanticstudios/pitwall)

### Tidyward (private file housekeeper for macOS where Jev answers what each file is)

`Open source` · `Free source build` · `BYOK`

Early macOS command-line housekeeper: it identifies files locally first, masks real names before anything leaves the machine, asks Jev only semantic yes/no questions such as "is this an invoice?", and your plain-text rules turn the answers into a keep, archive or Trash plan you confirm; every move can be undone.

**Jev's role:** Core for semantic matching: Jev returns calibrated yes/no probabilities for each rule's description; exact conditions run locally and the model never chooses an action.

**Platform:** macOS command line (`cargo install`); no scheduler or GUI yet, Windows planned.

**Product:** [github.com/chatpoc-ai/tidyward](https://github.com/chatpoc-ai/tidyward)

**Pricing / access:** Open source (Apache-2.0); free source build. Jev calls are billed to your TypeSafe or Vercel AI Gateway account. Checked 2026-10-26. Source inspected; live app not run on the review host.

[Full Tidyward (private file housekeeper for macOS where Jev answers what each file is) guide](tidyward.md) · [Source](https://github.com/chatpoc-ai/tidyward)

## Discord bots

### jeff (Discord bot)

`Open source` · `Free source build` · `BYOK`

Discord bot built with botbox where every feature is a typed Jev question: settle debates, rank lists, tag forum posts with the forum's own tags, answer FAQ repeats, and track unanswered help questions.

**Jev's role:** Every command is one Jev request with a few typed questions; code owns the thresholds.

**Platform:** Self-hosted Discord bot.

**Product:** [github.com/saembit/jeff-bot](https://github.com/saembit/jeff-bot)

**Pricing / access:** Free source build; bring your own TypeSafe/provider key when live. Source inspected; live app not run on the review host.

[Full jeff (Discord bot) guide](jeff-discord-bot.md) · [Source](https://github.com/saembit/jeff-bot)

### Jev Moderation Bot

`Source unverified` · `Pricing unverified` · `BYOK`

Moderate Discord messages with Jev classifications, configurable escalation and member activity summaries.

**Access:** [self-host the Python bot](https://github.com/brainstormity/Jev-Moderation-Bot#setup) with Discord bot permissions and a TypeSafe key. Starting it enables automatic message deletion and escalating timeouts; no review-only mode was established. Inference/hosting costs apply. README declares MIT but a complete license was not found. Source reviewed; live moderation and accuracy untested.

[Full Jev Moderation Bot guide](jev-moderation-bot.md) · [Source](https://github.com/brainstormity/Jev-Moderation-Bot)

### Jev-Mod (undeemed)

`Open source` · `Free source build` · `BYOK`

Discord moderation bot powered by TypeSafe Jev rules: hosted dashboard or self-host on Cloudflare/Docker with your own API key.

**Access:** use the [hosted dashboard](https://app.jevmod.us) (Discord sign-in + your TypeSafe key) or self-host the [MIT source](https://github.com/undeemed/jev-mod) via Docker/Cloudflare. No bot-token setup needed for the hosted path. TypeSafe usage separate. Distinct from brainstormity/Jev-Moderation-Bot and Soter.

[Full Jev-Mod (undeemed) guide](undeemed-jev-mod.md) · [Source](https://github.com/undeemed/jev-mod) · [Product page](https://jevmod.us)

### Soter

`Open source` · `Free source build` · `BYOK`

Automated Discord moderation: TypeSafe Jev (OpenRouter Decisions) scores hate speech and spam; code deletes clear hits, flags borderline cases, and can timeout repeat violators.

**Access:** self-host the [MIT Bun source](https://github.com/frolleks/soter) with `DISCORD_TOKEN` + `OPENROUTER_API_KEY`, or try the early hosted invite (not 24/7). No app purchase fee; OpenRouter/Jev usage separate. Source inspected; live moderation accuracy not measured.

[Full Soter guide](soter.md) · [Source](https://github.com/frolleks/soter) · [Product page](https://soter.frolleks.site)

## Telegram bots

### Jev Anti-Spam Bot

`Open source` · `Free source build` · `BYOK`

Delete high-confidence Telegram group spam with TypeSafe Jev Noul signals and fail-open errors; optional Postgres stats without storing message text.

**Access:** [self-host with Bun or Docker](https://github.com/backmeupplz/jev_antispam_bot#setup) using a Telegram bot token (privacy mode disabled) and a TypeSafe key. Adding the bot as a group admin with delete permission enables automatic deletions. Inference/hosting costs apply. MIT source; live moderation accuracy untested in this catalog review.

[Full Jev Anti-Spam Bot guide](jev-antispam-bot.md) · [Source](https://github.com/backmeupplz/jev_antispam_bot)

### TG-Spam

`Open source` · `Free source build` · `BYOK`

Self-hosted Telegram anti-spam bot and Go library (maintained since 2023); its optional Jev provider asks one typed spam question (plus an optional gibberish question) and thresholds the returned probability.

**Access:** build from the [MIT source](https://github.com/umputun/tg-spam), install with Homebrew, or run the Docker image, then add the bot to your group. Jev is optional (`--jev.token`), uses your own TypeSafe key, and is billed separately. Source documentation inspected; live moderation not run in this catalog review.

[Full TG-Spam guide](tg-spam.md) · [Source](https://github.com/umputun/tg-spam)

## Before you get started

Each guide records supported platforms, setup, accounts and keys, data recipients, costs, limitations, and the version reviewed. Follow its launch or build path. Source availability does not imply a downloadable release or free inference, and an app listing does not certify production readiness.

For components to integrate into your own project, browse [tools and integrations](../tools/README.md). For a small offline introduction, try the repository's [teaching examples](../../../examples/README.md).

## List your app

Self-submissions are welcome, including open-source, closed-source, free, and paid apps. Provide a working product or source-build link, official pricing/access information, evidence of Jev use, and your affiliation. Apply the [source/pricing tags and disclosures](../../APP_TAGS.md). Closed-source listings must identify what could not be independently inspected; commercial listings must visibly identify paid access.

Follow [List a Jev-powered app](../../../CONTRIBUTING.md#list-a-jev-powered-app) and the [project-page template](../../PROJECT_TEMPLATE.md), or [open an app suggestion](https://github.com/AppitStudio/awesome-jev/issues/new?template=resource.yml). App pages live in this folder, one full page per app.
