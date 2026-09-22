# Jev Column Race

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local (or hosted BYOK) race UI that labels 1,000 withheld-star app reviews in parallel columns: TypeSafe Jev typed questions versus a Gemini JSON lane, with free replay of recorded runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/goodrahstar/jev-column-race) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Hosted demo](https://jev-column-race.vercel.app) — BYOK live race or free replay; source also runs locally. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-22**. Live races need `TYPESAFE_API_KEY` and a Gemini/`LLM_API_KEY` (or visitor BYOK on the hosted deploy). Replay mode needs no keys. Provider usage for live races can incur charges. |
| Jev evidence | Inspected [`lib/racers.mjs`](https://github.com/goodrahstar/jev-column-race/blob/d9ee360ccd84462f4eab9493a7c2c617d0dab9df/lib/racers.mjs): `jevRacer` posts batches to `https://api.typesafe.ai/v1/systemone`. Recorded timing/cost comparisons in upstream `docs/performance.md` are upstream-reported for a dated run pair—not independently re-measured here. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Do not treat upstream race multipliers as guaranteed future performance. Source and offline verify scripts inspected; live TypeSafe/Gemini races not run on the review host. |
| Maintainer | [goodrahstar](https://github.com/goodrahstar). Independently curated. |
| Format | Zero-dependency Node server (`server.mjs`) + static `public/`; npm package name `jev-column-race` **1.0.0**. |
| Platform and availability | Node.js ≥ 20 locally at [http://127.0.0.1:8777](http://127.0.0.1:8777); hosted [jev-column-race.vercel.app](https://jev-column-race.vercel.app). |
| Jev's role | Answers typed Score/Choice/Noul questions over review batches (80 questions per 20-review request). Application code owns batching, validation, timers, cost accounting, and the Gemini comparison lane. |
| Requirements | Node ≥ 20; optional `.env` with `TYPESAFE_API_KEY` / `LLM_*` for live mode. |
| License | [MIT](https://github.com/goodrahstar/jev-column-race/blob/d9ee360ccd84462f4eab9493a7c2c617d0dab9df/LICENSE). |

## When to use

Use it when you want a **visible side-by-side labeling race** (Jev typed questions vs a generative JSON lane) with free replay. Prefer [jev-table](../tools/jev-table.md) for production CSV/JSONL labeling CLIs. Do not treat a single recorded run as a universal benchmark.

## How it works

[`server.mjs`](https://github.com/goodrahstar/jev-column-race/blob/d9ee360ccd84462f4eab9493a7c2c617d0dab9df/server.mjs) serves the UI and race API. Jev lane calls System One via `jevRacer`; Gemini lane uses an OpenAI-compatible chat endpoint. Reviews are 1,000 Android app reviews with stars withheld from both models. Replay re-emits recorded `runs/*.json` without keys.

## Get started

```sh
git clone https://github.com/goodrahstar/jev-column-race.git
cd jev-column-race
git checkout d9ee360ccd84462f4eab9493a7c2c617d0dab9df
# Optional: cp .env.example .env and add keys for live races
node server.mjs
# Open http://127.0.0.1:8777 — choose Replay for a free retake
```

Live races send review text to TypeSafe and Gemini and may incur charges. This listing did not start a live race.

## Examples and demos

- Offline on the review host: `node scripts/verify-data.mjs` → **DATA OK**; `node scripts/verify-replay.mjs` → **REPLAY OK**; `node scripts/verify-byok.mjs` → **BYOK OK**.
- Hosted demo: [jev-column-race.vercel.app](https://jev-column-race.vercel.app) (HTTP 200 checked).
- Upstream recorded run docs under `docs/performance.md` / `docs/design.md`.

## Limits and data handling

Review text leaves the host on live races. Upstream performance numbers are for a specific recorded pair; re-run before quoting. BYOK mode validates visitor keys against mocked providers in `verify-byok.mjs`.

## Review and maintenance

Reviewed on **2026-09-22** at [commit d9ee360](https://github.com/goodrahstar/jev-column-race/tree/d9ee360ccd84462f4eab9493a7c2c617d0dab9df): **1.0.0**, MIT. AI-assisted source review of README, `lib/racers.mjs`, `server.mjs`, LICENSE. Offline verify-data/replay/byok OK. No live TypeSafe or Gemini race on the review host.

Related: [jev-table](../tools/jev-table.md), [Jev Grand Prix](jev-grand-prix.md).
