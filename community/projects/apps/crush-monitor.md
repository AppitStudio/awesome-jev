# Crush Monitor

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local WeChat-style conversation analyzer: TypeSafe Jev labels emotion and intent per message, scores affinity signals, and rates your replies—run on localhost with your own API key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FerryCorleone/crush-monitor) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/FerryCorleone/crush-monitor#readme) — local web UI; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-21**. Requires `TYPESAFE_API_KEY`. TypeSafe usage can incur charges. |
| Jev evidence | Inspected [server/analysis.ts](https://github.com/FerryCorleone/crush-monitor/blob/be1b33b2bc48a69bf7f88921e722e0c14cc1d3d0/server/analysis.ts): `@typesafe-ai/sdk` posts typed emotion/intent/affinity judgments (`jev-1.13.0`). Offline `npm test` mocks providers. Live chat analysis was not run. |
| Disclosure | Free source access does not include inference. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. Not affiliated with WeChat/Tencent or TypeSafe. |
| Maintainer | [FerryCorleone](https://github.com/FerryCorleone). |
| Format | TypeScript local web app (`crush-monitor` 1.1.0): Vite/React UI + Express API. |
| Platform and availability | Source build on Node.js **22.12+**. Bind to `127.0.0.1` by default. Paste WeChat-exported chat text; does not read the WeChat database. |
| Jev's role | Per-message emotion (12-class) and intent (35-class) Choice/probability judgments, affinity scoring, and reply-quality tiers; application code batches long chats and stores results in the browser. |
| Requirements | Node.js 22.12+, `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/FerryCorleone/crush-monitor/blob/be1b33b2bc48a69bf7f88921e722e0c14cc1d3d0/LICENSE). |

## When to use

Use it for personal, local analysis of pasted WeChat-style chat logs when you want structured emotion/intent labels instead of free-form chat summaries. Prefer ordinary note-taking or non-AI reflection when you do not want chat text sent to TypeSafe. Treat scores as optional reference, not relationship advice.

## How it works

Paste multi-select WeChat exports (or `我：` / `对方：` lines). The Express server builds typed System One questions and calls TypeSafe via `@typesafe-ai/sdk`. The UI shows tags under bubbles, affinity on top, and reply tiers. Incremental paste reuses prior analyses and rechecks recent partner messages. Chat and results stay in browser storage on the machine that runs the UI.

## Get started

```sh
git clone https://github.com/FerryCorleone/crush-monitor.git
cd crush-monitor
git checkout be1b33b2bc48a69bf7f88921e722e0c14cc1d3d0
npm ci
npm run setup
# edit .env with TYPESAFE_API_KEY
npm run build
npm start
```

Open **[http://127.0.0.1:3178/](http://127.0.0.1:3178/)**. Live analysis sends message text to TypeSafe and may incur charges. Do not commit `.env` or private chats.

Offline tests (no key required):

```sh
npm test
```

## Examples and demos

- README documents WeChat paste formats, affinity dimensions, and batching limits.
- [tests/](https://github.com/FerryCorleone/crush-monitor/tree/be1b33b2bc48a69bf7f88921e722e0c14cc1d3d0/tests): capacity, core, and incremental coverage without live model calls.
- `npm run check:live` exercises a real key (not run here).

## Limits and data handling

Analyzed message text goes to TypeSafe under your key. Affinity and reply grades are heuristics over model outputs, not measured relationship outcomes. History lives in browser storage for that origin; clearing site data deletes it. Not affiliated with WeChat or Tencent.

## Review and maintenance

Reviewed on **2026-09-21** at [commit be1b33b](https://github.com/FerryCorleone/crush-monitor/tree/be1b33b2bc48a69bf7f88921e722e0c14cc1d3d0): package **1.1.0**, MIT. AI-assisted source review of README, LICENSE, `server/analysis.ts`, and package scripts. On Node 22 with `npm ci`, **`npm test`: 36 passed**. No live TypeSafe calls.

Related: [Jevmail](jevmail.md) and [Jev Mail Classifier](jev-mail-classifier.md) also classify personal messages with Jev for inbox triage rather than chat affinity.
