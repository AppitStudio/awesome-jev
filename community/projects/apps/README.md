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

### Airtale

`Open source` · `Free source build` · `BYOK`

Inbound lead ingestion and AI qualification pipeline using TypeSafe Jev System One.

**Access:** Clone the [MIT source](https://github.com/SebassContreras/airtale) and follow upstream setup. No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live install/inference not tested on the review host.

[Full Airtale guide](airtale.md) · [Source](https://github.com/SebassContreras/airtale)

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

### beebots

`Open source` · `Free source build` · `BYOK`

Three AI trading bees on OKX perpetual futures race on paper by default: TypeSafe Jev makes every trade decision; plain code owns the risk layer and orders. OpenAI is used only to design bee personas and portraits.

**Access:** Clone the [MIT source](https://github.com/imikerussell/beebots) and run via Docker Compose, or follow upstream deploy docs. Bring a TypeSafe Jev key (and OpenAI key for bee design). Paper trading is the default; live exchange use is operator-controlled and not recommended as advice. No app purchase fee; provider and infra costs are separate. Source inspected; live trading and live Jev not run on the review host.

[Full beebots guide](beebots.md) · [Source](https://github.com/imikerussell/beebots)

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

### Crush Monitor with Jev

`Open source` · `Free source build` · `BYOK`

MIT derivative of Crush Monitor: WeChat-style affinity analysis UI with TypeSafe Jev emotion/intent/affinity judgments, plus productized trial/account surfaces described upstream.

**Access:** clone the [MIT source](https://github.com/zhengge6/crush-monitor-with-jev) (Node.js 22.12+) and configure a TypeSafe (or compatible) key via `npm run setup`. No app purchase fee for the source build; provider/trial features billed per upstream docs. Source inspected; live analysis not run. Distinct from the original Crush Monitor listing (FerryCorleone).

[Full Crush Monitor with Jev guide](crush-monitor-with-jev.md) · [Source](https://github.com/zhengge6/crush-monitor-with-jev)

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

### Doom or Bloom

`Open source` · `Free` · `BYOK`

Free web interview that maps your AI worldview (doom↔bloom) using many TypeSafe Jev Choice/Score/Noul judgments; TypeScript owns routing and presentation.

**Access:** try [www.doom-or-bloom.com](https://www.doom-or-bloom.com) or clone the [MIT source](https://github.com/transitive-bullshit/doom-or-bloom). No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live session not run on the review host.

[Try Doom or Bloom](https://www.doom-or-bloom.com) · [Full Doom or Bloom guide](doom-or-bloom.md) · [Source](https://github.com/transitive-bullshit/doom-or-bloom)

### enigma-jev

`Open source` · `Free` · `BYOK`

Software Enigma/Bombe pipeline: TypeSafe Jev ranks cribs and judges whether a trial decryption is German.

**Access:** try [enigma-jev.vercel.app](https://enigma-jev.vercel.app) (TypeSafe key to unlock the machine) or clone the [MIT source](https://github.com/agodoy21/enigma-jev) (Bun ≥ 1.3). No app purchase fee; TypeSafe usage is separate. Source inspected; live break not run on the review host.

[Try enigma-jev](https://enigma-jev.vercel.app) · [Full enigma-jev guide](enigma-jev.md) · [Source](https://github.com/agodoy21/enigma-jev)

### Find the Right API (Orthogonal × Jev)

`Closed source` · `Freemium` · `Commercial`

Hosted natural-language API discovery: product copy states Jev searches about 1,000 Orthogonal endpoints and returns priced matches with Orthogonal `curl` snippets.

**Jev's role:** vendor/product claim—ranks Orthogonal catalog endpoints for a described goal (implementation not inspected).

**Access:** public web UI at [findtherightapi.com](https://www.findtherightapi.com/) (search needed no signup during review). Executing matches uses Orthogonal pay-per-call ([pricing](https://docs.orthogonal.com/concepts/pricing); new accounts get $5 free credits). Closed source. Checked 2026-09-24. Launch: [X post](https://x.com/chrisspickett/status/2102855582969725198).

[Try Find the Right API](https://www.findtherightapi.com/) · [Full Find the Right API guide](find-the-right-api.md) · [Source](https://www.findtherightapi.com/)

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

### Hx

`Open source` · `Free source build` · `BYOK`

Clinical documentation aid: as a doctor types or dictates, Hx opens the checklist the note implies, ticks items against clauses copied from the text, and shows what is still undocumented—without generating clinical prose. TypeSafe Jev supplies typed judgments.

**Access:** public demo at [hx.semicoded.com](https://hx.semicoded.com) (rate/spend limited) or clone the [MIT source](https://github.com/doitrous/hx) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Postgres optional for accounts. Offline server unit tests partially passed without Postgres; live analyze not run on the review host.

[Full Hx guide](hx.md) · [Source](https://github.com/doitrous/hx) · [Product homepage](https://hx.semicoded.com)

### IntentSQL

`Open source` · `Free source build` · `BYOK`

Local natural-language SQLite playground: inspectable semantic decisions, typed plans, deterministic SQL, and guarded writes via TypeSafe Jev / System One.

**Access:** Clone the [MIT source](https://github.com/Amine-LG/IntentSQL) and run the local uvicorn app; bring a TypeSafe (or compatible) key for live Jev. No app purchase fee; provider usage may incur charges. Source inspected; live Jev not run.

[Full IntentSQL guide](intentsql.md) · [Source](https://github.com/Amine-LG/IntentSQL)

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

### Jev Chess

`Open source` · `Free` · `BYOK`

One-page web app where TypeSafe Jev plays chess against OpenRouter LLMs, Stockfish, or you—with live move probabilities, clocks, and saved games (hosted key-lending demo available).

**Access:** try [jevchess.xera.ac](https://jevchess.xera.ac) (site-lent keys capped, or BYOK) or clone the [MIT source](https://github.com/choxos/jevchess) (`npm start`, Node ≥ 20.3). No app purchase fee; live games need TypeSafe/OpenRouter keys. Offline `npm test` 12 passed; live games not run on the review host.

[Try Jev Chess](https://jevchess.xera.ac) · [Full Jev Chess guide](jevchess.md) · [Source](https://github.com/choxos/jevchess)

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

### jev-leads

`Open source` · `Free source build` · `BYOK`

Multi-channel inbound lead intake (web/WhatsApp/Telegram/webhooks) buffered in SQLite WAL, qualified by OpenRouter typesafe/jev-1.13 structured decisions, then synced to Airtable with hot-reloadable per-channel configs.

**Access:** Clone the [MIT source](https://github.com/SebassContreras/jev-leads) and follow upstream setup (Node 24 LTS / Hono). Bring OpenRouter and Airtable credentials. No app purchase fee; provider usage is separate. Source inspected; live intake/inference not run on the review host.

[Full jev-leads guide](jev-leads.md) · [Source](https://github.com/SebassContreras/jev-leads)

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

### jev-gmail-filter

`Open source` · `Free source build` · `BYOK`

Self-hosted local web UI that filters Gmail with plain-English topics using [jevfilter](https://github.com/damiensmith1/jevfilter) and TypeSafe Jev—labels, tracked items, and quiet-item flags. Distinct from Jev for Gmail / Gmail Classifier extensions.

**Access:** clone the [MIT source](https://github.com/damiensmith1/jev-gmail-filter), `uv sync`, run `uv run jev-gmail-filter ui` with your own Google OAuth client and TypeSafe key. No app purchase fee; TypeSafe usage separate. Early development. Source inspected; live Gmail/Jev not run on the review host.

[Full jev-gmail-filter guide](jev-gmail-filter.md) · [Source](https://github.com/damiensmith1/jev-gmail-filter)

### jev-mail (vynnlee)

`Open source` · `Free source build` · `BYOK`

Config-driven Gmail zero-inbox triage powered by TypeSafe Jev System One judgments under local policy.

**Access:** [configure and run the MIT source](https://github.com/vynnlee/jev-mail) with Gmail OAuth + TypeSafe key (`jev-mail.example.yaml`). No app purchase fee; provider/Gmail usage separate. Source inspected; live Gmail/Jev not tested. Distinct from Jevmail / Jev for Gmail / Inbox Triage.

[Full jev-mail (vynnlee) guide](vynnlee-jev-mail.md) · [Source](https://github.com/vynnlee/jev-mail)

### Jev/ui (jev-genui)

`Source available` · `Free source build` · `BYOK`

**Jev's role:** answers parallel Choice questions that fill a page→section→tile grammar; code maps onto shadcn/ui (no JSX from Jev).

**Access:** clone the [public source](https://github.com/claudfuen/jev-genui) with Bun and `AI_GATEWAY_API_KEY`. No app purchase fee; Gateway/TypeSafe usage is separate. **No LICENSE** at reviewed commit—not open source. Source inspected; live compose not run.

[Full Jev/ui guide](jev-genui.md) · [Source](https://github.com/claudfuen/jev-genui)

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

### Jevmail

`Open source` · `Free source build` · `BYOK`

Local read-only Gmail triage into Needs reply / Updates / Promos / Sales / Spam using TypeSafe Jev via the Vercel AI Gateway, with urgency and personal-mail scores plus retained corrections.

**Access:** clone and run the [MIT source](https://github.com/fazlerocks/jevmail) with pnpm, Google OAuth (Gmail API), `AI_GATEWAY_API_KEY`, and `AUTH_SECRET`. No app purchase fee; Gateway free-tier limits and Gmail quotas apply. Offline `pnpm test` skips without a Gateway key; live Gmail classification not run.

[Full Jevmail guide](jevmail.md) · [Source](https://github.com/fazlerocks/jevmail)

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

### Liuyao

`Source available` · `Free source build` · `BYOK`

Chinese-style I Ching (六爻) site with programmatic casting plus TypeSafe Jev semantic judgment (sixyao.app; non-commercial source).

**Access:** Clone the [source](https://github.com/masonweb3/liuyao) (non-commercial terms per upstream) with a TypeSafe API key for live judgment. No app purchase fee for the described path; TypeSafe usage is separate. Source inspected; live install/inference not tested on the review host.

[Full Liuyao guide](liuyao.md) · [Source](https://github.com/masonweb3/liuyao)

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

### Notra

`Open source` · `Commercial` · `Paid`

Track how AI answers describe and position your brand. Jev judges brand sentiment and list position within a wider analytics application; other models handle scans, general judging, and drafting.

**Access:** the [hosted product](https://www.usenotra.com) requires an account and offers [paid plans](https://www.usenotra.com/pricing), checked 2026-09-19. Trial eligibility and checkout were not tested. Self-hosting requires database, authentication, and provider setup; the guide records database initialization caveats. This commercial listing is not an endorsement.

[Full Notra guide](notra.md) · [Source](https://github.com/usenotra/notra)

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

### tg-crush

`Open source` · `Free source build` · `BYOK`

Local real-time Telegram coach: TypeSafe Jev judges partner messages and your drafts (quality + timing) before send on localhost.

**Access:** clone the [MIT source](https://github.com/BrickerP/tg-crush) (Node.js ≥ 22.12) with `TYPESAFE_API_KEY` and Telegram API id/hash. No app purchase fee; TypeSafe usage is separate. Offline `npm run check` clean; live smoke/Telegram not run on the review host.

[Full tg-crush guide](tg-crush.md) · [Source](https://github.com/BrickerP/tg-crush)

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

### undertone

`Source available` · `Free source build` · `BYOK`

A text box that reads how your draft sounds before you send: TypeSafe Jev scores tone, flags, urgency, formality, and boss-safety.

**Access:** open [undertone-app.vercel.app](https://undertone-app.vercel.app) or build the [source](https://github.com/Nuu-maan/undertone) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage separate. **No LICENSE** at tip—not Open source. Source inspected; live typing not run.

[Full undertone guide](undertone.md) · [Source](https://github.com/Nuu-maan/undertone) · [Try app](https://undertone-app.vercel.app)

### Varina

`Source available` · `Free source build` · `BYOK`

Chinese-language multi-seat AI design-exploration workbench (local web UI + CLI) where an optional TypeSafe Jev post-gate decides START or ASK — whether a finished answer merits deeper multi-seat exploration — before any extra model spend; Jev never writes answers.

**Access:** clone the [source](https://github.com/deillusion/Aha-Engine) (Business Source License 1.1 — source available, production use allowed under a revenue cap; read the terms) and run locally. Requires your own model keys; the optional Jev gate uses your own TypeSafe key (usage billed by TypeSafe). Source inspected; live app not run on the review host.

[Full Varina guide](varina.md) · [Source](https://github.com/deillusion/Aha-Engine)

### Vicaura

`Closed source` · `Pricing unverified`

Hosted product-to-markdown tool: turn a product URL or description into a markdown repo of features, ICP, messaging, and pricing strategy for coding agents. Vendor states the product is powered by Jev.

**Access:** use [vicaura.com](https://vicaura.com). No public pricing page found (checked 2026-09-22); [Terms](https://vicaura.com/terms-privacy) mention guest searches and possible Stripe-billed plans. Closed source — implementation not inspected; Jev evidence is the author's [X post](https://x.com/mmmikhaeel/status/2102105486501822826). Live generate not run. Not an endorsement.

[Full Vicaura guide](vicaura.md) · [Source](https://vicaura.com) · [Product homepage](https://vicaura.com)

### Watermelon

`Open source` · `Free source build` · `BYOK`

Status-update honesty auditor: TypeSafe Jev judges language while local code parses dates/slippage, then reports whether the health label matches the facts and whether escalation is warranted.

**Access:** public demo at [watermelon.shashwatchavan.com](https://watermelon.shashwatchavan.com) or clone the [MIT source](https://github.com/shashwatc12/watermelon) with `TYPESAFE_API_KEY`. No app purchase fee; TypeSafe usage is separate. Offline `npm test`: 22 passed; live TypeSafe calls not run on the review host.

[Full Watermelon guide](watermelon.md) · [Source](https://github.com/shashwatc12/watermelon) · [Product homepage](https://watermelon.shashwatchavan.com)

## Desktop apps

### Goutoujunshi Jev Chat

`Open source` · `Free source build` · `BYOK`

WeChat companion (Mac source preview + Windows preview ZIP): OCR the chat, optional TypeSafe Jev strategy judgment, ranked reply drafts—you always send.

**Access:** download [GitHub Releases](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat/releases/latest) or build the [MIT source](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat). DeepSeek (or compatible) for drafts; optional TypeSafe Jev key. No app purchase fee; provider usage separate. Windows device validation still pending upstream. Source inspected; GUI/OCR/live not run on the Linux review host.

[Full Goutoujunshi Jev Chat guide](goutoujunshi-jev-chat.md) · [Source](https://github.com/shengjidaguai-china/goutoujunshi-jev-chat)

### Jev Sheets (OpenHarness)

`Open source` · `Free source build` · `BYOK`

OpenHarness desktop sheet pane: TypeSafe Jev answers typed `noul` / `choice` / `score` column headers for every row, with confidence, review gates, and Question Lab wording trials.

**Access:** [download OpenHarness](https://harness.autonomous.ai/desktop) for macOS or Linux (or build the [MIT source](https://github.com/autonomous-ai/openharness)), then open the bundled Jev Sheets harness from the Store. No app purchase fee observed on the download page (checked 2026-09-24); live answers need a TypeSafe, OpenRouter, or Cloudflare key (BYOK). Offline practice works without a key (word-matching only). Source and harness README inspected; desktop install and live Jev not run on the review host. Lists **Jev Sheets only**, not other OpenHarness DSHs.

[Full Jev Sheets guide](jev-sheets.md) · [Source](https://github.com/autonomous-ai/openharness) · [Product homepage](https://harness.autonomous.ai/desktop)

### JevDash

`Open source` · `Free source build` · `BYOK`

100% clean-room 2D platformer for benchmarking TypeSafe Jev in real-time control at 60 FPS. Mock decision engine works without keys; live path can use Vercel AI Gateway.

**Access:** Clone the [MIT source](https://github.com/Sunwood-ai-labs/jevdash) and follow README (Pygame). Mock mode needs no key; live Jev/Gateway is BYOK. No app purchase fee. Docs: [jevdash site](https://sunwood-ai-labs.github.io/jevdash/). Source inspected; live gameplay not run on the Linux review host.

[Full JevDash guide](jevdash.md) · [Source](https://github.com/Sunwood-ai-labs/jevdash)

### Modex

`Open source` · `Free source build` · `BYOK`

Open Codex-App–style desktop coding agent (Electron+React) driving Claude Code/Codex CLIs; optional TypeSafe Jev Auto routing picks model/effort per turn.

**Access:** Build from the [MIT source](https://github.com/TypeSafeAI/modex). No app purchase fee. Optional TypeSafe key for Auto routing (OS keychain); Claude/Codex keep their own logins/costs. Source inspected; desktop/live paths not run on the Linux review host.

[Full Modex guide](modex.md) · [Source](https://github.com/TypeSafeAI/modex)

### Synax

`Open source` · `Free` · `BYOK`

Open-source local workspace for coding agents and codebase docs (agent chats, files, diffs, terminal) whose Electron app offers optional Jev-assisted Computer Use: with a TypeSafe key (or OpenRouter), Jev picks bounded semantic actions for the app-hosted Cua Driver instead of the default Direct Cua strategy.

**Access:** download a free desktop build from [GitHub Releases](https://github.com/coldmint9/Synax/releases/latest) or build the [Apache-2.0 source](https://github.com/coldmint9/Synax). Jev-assisted Computer Use is opt-in and uses your own TypeSafe or OpenRouter key. Source inspected; app not run on the review host.

[Full Synax guide](synax.md) · [Source](https://github.com/coldmint9/Synax)

### Warren Duffer

`Open source` · `Free source build` · `BYOK`

Intraday Nifty-50 trading bot where TypeSafe Jev ranks names and code sizes/stops live broker orders (experimental; real-money risk).

**Access:** Free source build; BYOK TypeSafe/Vercel AI Gateway + broker API. Places real orders—no paper mode. Checked 2026-10-04. Source inspected; live paths not run on the review host.

[Full Warren Duffer guide](warrenduffer.md) · [Source](https://github.com/arimanyus/warrenduffer)

## macOS apps

### Capture (sgaabdu4)

`Open source` · `Free source build` · `BYOK`

Private Mac voice diary: local Parakeet transcription, TypeSafe Jev sorting into typed buckets, then Notion after you approve.

**Access:** build the [MIT source](https://github.com/sgaabdu4/capture) on macOS. Needs TypeSafe key for sorting and Notion OAuth. Audio stays on-device for transcription. No app purchase fee; provider usage separate.

[Full Capture guide](capture.md) · [Source](https://github.com/sgaabdu4/capture)

### Jaste

`Source unverified` · `Pricing unverified` · `BYOK`

Smart copy/paste beta with clipboard history and an optional Direct Jev mode that selects a saved text value for the focused field.

**Access:** [download the Mac beta](https://jaste.app/) for Apple silicon and macOS 14+. The inspected bundle offers a Direct Jev key setting; that mode requires a TypeSafe key and may incur inference charges. App pricing and hosted access limits are unverified. No public source or license was linked; review covered the homepage and release metadata/strings, without launching the app or testing live matching.

[Full Jaste guide](jaste.md) · [Product and access](https://jaste.app/)

### Jevcast

`Open source` · `Free source build` · `BYOK`

Native macOS launcher/window manager (Option–Space). Optional TypeSafe Jev matches loose natural-language requests to known actions; core search stays local.

**Access:** build the [MIT source](https://github.com/RyanErkal/jevcast) on macOS 14+ with Xcode 26+. Launcher works without Jev; optional NL matching needs a TypeSafe or OpenRouter key in Keychain. No app purchase fee; provider usage is separate. Source inspected; macOS build/live Jev not run on the Linux review host.

[Full Jevcast guide](jevcast.md) · [Source](https://github.com/RyanErkal/jevcast) · [Product homepage](https://jevcast.vercel.app)

### JevPaste

`Open source` · `Free source build` · `BYOK`

macOS menu bar Smart Paste: TypeSafe Jev picks which exact value from a copied multi-field block fits the focused input.

**Access:** build the [MIT source](https://github.com/taiki510/JevPaste) on macOS 14+ with Swift/Xcode CLT, Accessibility permission, and a TypeSafe key in Keychain. No app purchase fee; provider usage can incur charges. Linux review cited upstream CI; live paste not run here. Distinct from closed-source Jaste.

[Full JevPaste guide](jevpaste.md) · [Source](https://github.com/taiki510/JevPaste)

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

### Switchyard

`Open source` · `Free source build` · `BYOK`

macOS menu-bar app that opens every link in the right Dia/Chrome profile; TypeSafe Jev decides uncovered links and confident answers become local rules.

**Access:** Build the [MIT source](https://github.com/kevinebaugh/switchyard) on macOS with a TypeSafe API key. No app purchase fee; each Jev judgment can incur provider charges. Source inspected; macOS build/live routing not run on the Linux review host. Distinct from FrancoisChastel/jev-router's Switchyard-style naming.

[Full Switchyard guide](switchyard.md) · [Source](https://github.com/kevinebaugh/switchyard)

### TipTour

`Open source` · `Free source build` · `BYOK`

Use a macOS menu bar companion to act on typed click requests. Jev chooses among locally detected controls and judges completion or missing targets. A separate Gemini mode handles voice and writing.

**Access:** macOS 14.2+, a source build with Xcode, a TypeSafe key, and desktop permissions. Gemini mode needs its own key. Source is MIT licensed; provider usage can incur charges. Eight isolated decision tests passed; the full app, packaged releases, and live desktop actions were not tested.

[Full TipTour guide](tiptour.md) · [Source](https://github.com/milind-soni/tiptour-macos)

## Android apps

### JevBystander

`Open source` · `Free source build` · `BYOK`

Android Accessibility WeChat reader: TypeSafe Jev judges intent/emotion/urgency/stance and shows three Toasts only (~861 KB APK, zero third-party deps).

**Access:** install the [MIT Release APK](https://github.com/Nisaka520/JevBystander/releases/latest) or build the [source](https://github.com/Nisaka520/JevBystander) (JDK 17, Android SDK 35) with a TypeSafe key and Accessibility enabled. No app purchase fee; TypeSafe usage is separate. Source inspected; APK/device/live not run on the Linux review host. Sister of JevIntent; judgment-only vs reply-drafting Jev Chat Assistant.

[Full JevBystander guide](jev-bystander.md) · [Source](https://github.com/Nisaka520/JevBystander) · [Product page](https://nisaka520.github.io/JevBystander/)

### Jev Chat Assistant

`Open source` · `Free source build` · `BYOK`

Non-invasive Android overlay: Accessibility reads on-screen chat; TypeSafe Jev (OpenRouter Decisions) judges intent/danger/action and ranks drafted replies; fill-only paste (never auto-send). WeChat first.

**Access:** build the [MIT source](https://github.com/jev-chat/jev-chat-jarvis) (JDK 17, Android SDK 35) with an OpenRouter API key plus Accessibility/overlay permissions. No app purchase fee; OpenRouter/Jev usage is separate. Source inspected; APK build and live calls not run on the Linux review host. Distinct from desktop WeChat-log analyzers and the separate Android UI-agent SDK listed under Developer tools.

[Full Jev Chat Assistant guide](jev-chat-jarvis.md) · [Source](https://github.com/jev-chat/jev-chat-jarvis)

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

## Windows apps

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

### SignalLens

`Open source` · `Free source build` · `BYOK`

Privacy-conscious local-first chat signal analyzer: on-device redaction, then TypeSafe Jev judges emotion, intent, and engagement for a closeness index. Windows portable exe or Streamlit source.

**Access:** download the [MIT Windows portable release](https://github.com/xinian5216/chat-signal-analyzer/releases) or run the [source](https://github.com/xinian5216/chat-signal-analyzer) with a TypeSafe API key. No app purchase fee; TypeSafe usage is separate. Source inspected on Linux; Windows GUI/live Jev not run. Distinct from Crush Monitor / tg-crush.

[Full SignalLens guide](signal-lens.md) · [Source](https://github.com/xinian5216/chat-signal-analyzer)

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

### Jev Content Guard

`Open source` · `Free source build` · `BYOK`

Chrome Manifest V3 extension that scans page text for fraud, advertising, AI slop, spam, clickbait, infobusiness, and toxicity with TypeSafe Jev (`jev-latest`), then shows badges or blur overlays from two-tier thresholds.

**Access:** install from the [Chrome Web Store](https://chromewebstore.google.com/detail/jev-content-guard/icdfmbedfjfodocdhpnecdjgofakeemn) or [load the MIT source unpacked](https://github.com/serejkaaa512/jev-content-guard-ext) (Developer mode) and paste a TypeSafe API key in the popup (`chrome.storage.local`). No app purchase fee; each analyzed block can incur provider charges. Source inspected; Chrome install and live page analysis not tested on the review host. Distinct from TypeSafe Fun AdBlocker (heuristic DOM ads) and Unclutter (clutter rules).

[Full Jev Content Guard guide](jev-content-guard.md) · [Source](https://github.com/serejkaaa512/jev-content-guard-ext)

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

### Jev Form Fill

`Open source` · `Free source build` · `BYOK`

Chrome extension that matches clipboard/source text to form fields with TypeSafe Jev, lets you review proposals, fill selected fields in page order, read back values, and undo—you submit the form yourself.

**Access:** Load unpacked from the [MIT source](https://github.com/takasek/jev-form-fill) (Chrome 116+). Bring a TypeSafe API key in the popup. No app purchase fee; TypeSafe usage billed separately. Source inspected; live form fills not run on the review host.

[Full Jev Form Fill guide](jev-form-fill.md) · [Source](https://github.com/takasek/jev-form-fill)

### Jev Investment Forecast (jev-investment-forecast)

`Open source` · `Free source build` · `BYOK`

Chrome extension that inspects any displayed web page and uses TypeSafe Jev to forecast investment potential across 27 category judgments (50% positive-value threshold, 25% risk threshold) plus 2 choice questions (investment amount and duration).

**Access:** clone or load the MIT source (or the Chrome Web Store listing linked from the root README) with a TypeSafe Jev API key. No app purchase fee; API usage costs are separate. Source inspected; live calls not run on the review host.

[Full Jev Investment Forecast guide](jev-investment-forecast.md) · [Source](https://github.com/serejkaaa512/jev-investment-forecast)

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

### Jev Inbox

`Open source` · `Free source build` · `BYOK`

Chrome extension that reorders Gmail’s list: unread first, critical on top, with your label chips—TypeSafe Jev (or Vercel AI Gateway) over row metadata only. Distinct from Jev Inbox Queue.

**Access:** [build and load unpacked](https://github.com/iamomiid/jev-inbox#install-from-source) (`npm run build` → `dist/`) with a TypeSafe or Vercel AI Gateway key. No app purchase fee; inference can incur charges. Source inspected; Chrome install and live Gmail/Jev not tested on the review host.

[Full Jev Inbox guide](jev-inbox.md) · [Source](https://github.com/iamomiid/jev-inbox)

### Jev Review (Gmail)

`Open source` · `Free source build` · `BYOK`

Chrome extension that grades Gmail compose/reply text with TypeSafe Jev on configurable criteria and tracks which questions from the other person's email remain unanswered.

**Access:** Load unpacked from the [MIT source](https://github.com/petrzpav/jev-review) in chrome://extensions; paste a TypeSafe key in options. No app purchase fee; TypeSafe usage billed separately. Source inspected; live Gmail grading not run on the review host.

[Full Jev Review (Gmail) guide](petrzpav-jev-review.md) · [Source](https://github.com/petrzpav/jev-review)

### Jev Slop Guard

`Open source` · `Free source build` · `BYOK`

Chrome extension that scores and stamps AI slop on X and LinkedIn feeds with TypeSafe Jev as you scroll.

**Access:** [build/load the MIT source unpacked](https://github.com/davertor/jev-slop-guard) (Chrome MV3) with a TypeSafe API key. No app purchase fee; inference can incur charges. Source inspected; Chrome install and live feed scoring not tested on the review host. Distinct from LinkedIn Slop Filter and JevSlop.

[Full Jev Slop Guard guide](jev-slop-guard.md) · [Source](https://github.com/davertor/jev-slop-guard)

### Jev Tweet Radar

`Open source` · `Free source build` · `BYOK`

Chrome MV3 (optional iOS Safari Web Extension) that scores each visible X post with one TypeSafe Jev System One call—worth engaging, buzz, spam, AI-ish, and related tags—shown in the avatar column. Distinct from Jev Slop Guard and jev-x-filter.

**Access:** [load the MIT source unpacked](https://github.com/DDnim/jev-tweet-radar) with a TypeSafe API key in options; optional Xcode Safari project for iOS. No app purchase fee; each judgment can incur provider charges. Source inspected; Chrome/Safari install and live X scoring not tested on the review host.

[Full Jev Tweet Radar guide](jev-tweet-radar.md) · [Source](https://github.com/DDnim/jev-tweet-radar)

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

### LinkedIn Slop Filter

`Open source` · `Free source build` · `BYOK`

Chrome extension + local Node proxy: TypeSafe Jev stamps LinkedIn posts Bait/Corp/Brag/Slop (distinct from Slop Mop writing scores).

**Access:** clone the [MIT source](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter) (Node ≥ 20 for `server/`), put a TypeSafe key in `.env`, run the localhost proxy, load `extension/` unpacked. No Chrome Web Store listing (key stays local). Source inspected; Chrome/live Jev not run on the review host.

[Full LinkedIn Slop Filter guide](jev-linkedin-slop-filter.md) · [Source](https://github.com/Arpit-Khandelwal/jev-linkedin-slop-filter)

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

### Slop Mop

`Open source` · `Free` · `BYOK`

Judge LinkedIn post writing with TypeSafe Jev (11–12 typed questions), then fold or highlight suspected slop with inspectable scores and local overrides. Not an AI detector. Distinct from JevSlop (note/article scoring).

**Access:** free hosted use via [slopmop.lol](https://slopmop.lol) (no signup; daily check limits on the maintainer's server, default 250/install/UTC day) or [self-host the MIT source](https://github.com/tomfrazier/slopmop) with your own TypeSafe/AI Gateway key. Desktop Chromium / LinkedIn only; load unpacked from a local build. No Chrome Web Store listing verified. Source and offline vitest inspected; Chrome install and live LinkedIn/Jev not tested on the review host.

[Full Slop Mop guide](slop-mop.md) · [Source](https://github.com/tomfrazier/slopmop)

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

### arJev

`Open source` · `Free source build` · `BYOK`

Daily arXiv digest engine: lexical front-line plus TypeSafe Jev confidence-gated rerank against an Obsidian vault.

**Access:** Clone the [Apache-2.0 source](https://github.com/harmoniqs/arjev) and follow upstream setup with a TypeSafe/provider key when live. No app purchase fee for the source build; provider usage is separate. Source inspected; live install/inference not tested on the review host.

[Full arJev guide](arjev.md) · [Source](https://github.com/harmoniqs/arjev)

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

### Jev Mail Classifier

`Open source` · `Free source build` · `BYOK`

Classify IMAP mail with Jev yes/no category judgments, then tag, move, flag, or notify from a Textual TUI and cron-friendly CLI.

**Access:** clone and run the [MIT source](https://github.com/parth-kp/jev-mail-classifier) (Python 3.10+) with `./install.sh`, a Jev provider key (TypeSafe, OpenRouter, or Vercel AI Gateway), and IMAP credentials (often an app password). No app purchase fee; provider and mailbox-host usage can incur charges. Offline pytest: 61 passed on the review host; live mailbox classification not run.

[Full Jev Mail Classifier guide](jev-mail-classifier.md) · [Source](https://github.com/parth-kp/jev-mail-classifier)

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

### Jevmeter

`Open source` · `Free source build` · `BYOK`

Annotate videos with Jev judgments about sentence-level rhetoric, then render overlays and highlights.

**Access:** [build the MIT Python CLI](https://github.com/ChetasLua/jevmeter#-command-line-for-power-users) with a Whisper backend, FFmpeg support and TypeSafe key. Source has no purchase fee; inference charges apply. The review inspected source only. Scores are model judgments, not fact-checks; failed sentences can be omitted.

[Full Jevmeter guide](jevmeter.md) · [Source](https://github.com/ChetasLua/jevmeter)

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

## Discord bots

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
