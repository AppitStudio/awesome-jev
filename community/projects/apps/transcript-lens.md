# Transcript Lens

[All projects](../README.md) · [Web apps](README.md#web-apps)

Next.js app (Türkçe UI) that explores YouTube transcripts by meaning: TypeSafe Jev classifies blocks for kind, value, and signals without rewriting the text.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sensahin/transcript-lens) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/sensahin/transcript-lens#readme) — source-built Next.js app; no separate hosted product required. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-20**. Analysis needs your Vercel AI Gateway key (`JEV_PROVIDER=gateway`) or TypeSafe key (`JEV_PROVIDER=typesafe`). Provider usage can incur charges. Keyless mode still opens/pastes/exports sample text without analysis. |
| Jev evidence | Inspected [`src/lib/jev.ts`](https://github.com/sensahin/transcript-lens/blob/9183ef9ff0f9a18834bb139d01e508c22d422257/src/lib/jev.ts) and [`src/lib/analyze.ts`](https://github.com/sensahin/transcript-lens/blob/9183ef9ff0f9a18834bb139d01e508c22d422257/src/lib/analyze.ts): Gateway `experimental_evaluate` with model `typesafe-ai/jev`, or direct `POST https://api.typesafe.ai/v1/systemone`; per-block Choice/Noul suite (kind, value, surprising, funny, …). Live analysis not run. |
| Disclosure | Free source access does not include Gateway/TypeSafe usage. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [sensahin](https://github.com/sensahin). |
| Format | Next.js application (`transcript-lens` 0.1.0) with API routes for analyze/lens. |
| Platform and availability | Source build with Node.js 22+; `npm run dev` on localhost, or deploy your own Vercel fork. Experimental personal tool—upstream warns open deployments share your provider bill. |
| Jev's role | Classifies transcript blocks and powers semantic search views; application code owns captions, heatmaps, sectioning, and exports. Claims are not fact-checked. |
| Requirements | Node.js 22+, npm; optional `AI_GATEWAY_API_KEY` or `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/sensahin/transcript-lens/blob/9183ef9ff0f9a18834bb139d01e508c22d422257/LICENSE). |

## When to use

Use it to skim long YouTube captions for substance, sponsors, and topical passages with a Turkish-first UI. Prefer [Sponsor Skip](sponsor-skip.md) when you only need sponsor-read boundaries for playback skip, or [Jevmeter](jevmeter.md) for video caption gauges from sentence judgments.

## How it works

Transcript text is split into blocks. [`analyze.ts`](https://github.com/sensahin/transcript-lens/blob/9183ef9ff0f9a18834bb139d01e508c22d422257/src/lib/analyze.ts) issues one multi-question Jev call per block (kind Choice, value Choice, several Noul signals) through Gateway or direct TypeSafe. Code aggregates answers into heatmaps, section titles from native phrases, and search hits that show original wording rather than summaries.

## Get started

```sh
git clone https://github.com/sensahin/transcript-lens.git
cd transcript-lens
git checkout 9183ef9ff0f9a18834bb139d01e508c22d422257
npm ci
cp .env.example .env.local
npm run dev
```

Open <http://localhost:3000>, try the built-in Turkish sample transcript. Analysis without a key shows an explanatory message. Live analysis sends transcript blocks to your chosen provider and can incur charges. This listing did not run `npm test` or live Jev.

## Examples and demos

- In-app Turkish sample transcript (project-authored; not taken from another video).
- Offline `tests/core.test.ts` — not executed on the review host.

## Limits and data handling

Transcript text leaves the host for Gateway or TypeSafe when analysis runs. Keys must not use `NEXT_PUBLIC_` prefixes. Public Vercel deploys without auth can spend the deployer's quota—upstream documents this risk. UI language is Turkish; analysis criteria in code are English.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 9183ef9](https://github.com/sensahin/transcript-lens/tree/9183ef9ff0f9a18834bb139d01e508c22d422257): **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `src/lib/jev.ts`, `src/lib/analyze.ts`, and package metadata. No live TypeSafe/Gateway analysis.

Related: [Sponsor Skip](sponsor-skip.md), [Jevmeter](jevmeter.md).
