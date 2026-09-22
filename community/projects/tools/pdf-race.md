# PDF Race

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Timed document race: Docling → TypeSafe Jev vs Docling → Gemini vs Gemini reading the PDF, scored against arXiv metadata, with committed recorded runs for keyless replay (optional local Laya lane on Apple silicon).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/goodrahstar/pdf-race) |
| Maintainer | [goodrahstar](https://github.com/goodrahstar) (Rahul Kumar). Independently curated; this entry is not an upstream submission or endorsement. Same author as [Jev Column Race](../apps/jev-column-race.md); this repo is a separate PDF/document bench. |
| Format | Zero-dependency Node ≥ 20 local/Vercel app (`pdf-race` 1.0.0): `server.mjs`, committed `runs/`, optional Docling/Laya workers. |
| Requirements | Node **≥ 20** for replay. Live races need `TYPESAFE_API_KEY` and `GEMINI_API_KEY`. Docling lane needs a local `uv` venv with `docling` (~1.1 GB). Optional `laya-mlx` on darwin/arm64. |
| License | [MIT](https://github.com/goodrahstar/pdf-race/blob/2eae758f836d1a7c6c20b2709aa8dfff3d86b994/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline verify scripts for data/lanes-mock/run/quality/replay/CV/claims passed; `verify-browser` hung on the review host; `verify-laya-timing` failed a wall-clock assert (disclose, not used as quality evidence). No live TypeSafe/Gemini. Hosted demo: [pdf-race.vercel.app](https://pdf-race.vercel.app). |

## When to use

Use it when you want a **side-by-side cost/latency race** of TypeSafe Jev against Gemini on the same parsed (or raw PDF) documents with frozen ground truth. Prefer [DocJev](docjev.md) / [doc-router](doc-router.md) for production document classification/routing; prefer [Jev Column Race](../apps/jev-column-race.md) for review-labeling races.

## How it works

[`lib/lanes.mjs`](https://github.com/goodrahstar/pdf-race/blob/2eae758f836d1a7c6c20b2709aa8dfff3d86b994/lib/lanes.mjs) posts typed questions to `https://api.typesafe.ai/v1/systemone` for the Docling → Jev lane; Gemini lanes use the Gemini API. Rubric and scoring live in [`lib/rubric.mjs`](https://github.com/goodrahstar/pdf-race/blob/2eae758f836d1a7c6c20b2709aa8dfff3d86b994/lib/rubric.mjs). Replay mode streams committed `runs/*.json` without keys. Live races send document text (and PDF bytes for the Gemini-PDF lane) to providers.

## Get started

```sh
git clone https://github.com/goodrahstar/pdf-race.git
cd pdf-race
git checkout 2eae758f836d1a7c6c20b2709aa8dfff3d86b994
node scripts/verify-data.mjs
node scripts/verify-lanes-mock.mjs
node scripts/verify-run.mjs
node scripts/verify-replay.mjs
node server.mjs   # http://127.0.0.1:8778 — use Replay without keys
```

Live races: copy `.env.example` → `.env` with keys; optional Docling via `uv venv && uv pip install docling pypdfium2`.

## Examples and demos

- Offline on review host: DATA OK, LANES MOCK OK (mocked TypeSafe+Gemini hosts), RUN/QUALITY/REPLAY/CV/CLAIMS OK.
- Hosted UI: [pdf-race.vercel.app](https://pdf-race.vercel.app).
- Upstream README timing/cost tables are author-recorded; not remeasured live here.

## Limits and data handling

Parser time dominates wall clock when Docling runs. Segment-role “agreement” is not accuracy. Optional Laya is local open-weights and is not TypeSafe Jev. Live keys incur provider charges. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 2eae758](https://github.com/goodrahstar/pdf-race/tree/2eae758f836d1a7c6c20b2709aa8dfff3d86b994): **1.0.0**, MIT. AI-assisted review of README, LICENSE, `lib/lanes.mjs`, `lib/rubric.mjs`, `server.mjs`, and verify scripts. Offline verifies as above; browser verify not completed. No live TypeSafe/Gemini.

Related: [DocJev](docjev.md), [doc-router](doc-router.md), [Jev Column Race](../apps/jev-column-race.md), [tax-doc-classifier](tax-doc-classifier.md).
