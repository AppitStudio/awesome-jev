# Fotocopiatrice

[All projects](../README.md) · [Apps](README.md) · [Web apps](README.md#web-apps)

Italian parliamentary amendment explorer: downloads Camera open data, deduplicates identical texts in code, then uses TypeSafe Jev for typed judgments (topic, “tailor-made” score, pair equivalence). Static Next.js site plus reusable export dataset.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bnistor4/fotocopiatrice) |
| Tags | Open source · Free source build · BYOK |
| Product homepage | [fotocopiatrice.vercel.app](https://fotocopiatrice.vercel.app/) |
| Pricing and access | MIT source and static hosted site have no app purchase fee, checked **2026-09-21**. Hosted site reads committed JSON only (no server key). Local pipeline `analyze` / `pairs` need `TYPESAFE_API_KEY`. TypeSafe usage is separate. |
| Jev evidence | [`pipeline/questions.ts`](https://github.com/bnistor4/fotocopiatrice/blob/84b840c7e1253915b92bf1420706cd5c096b35cb/pipeline/questions.ts) builds noul/choice/score via `@typesafe-ai/sdk`; [`pipeline/analyze.ts`](https://github.com/bnistor4/fotocopiatrice/blob/84b840c7e1253915b92bf1420706cd5c096b35cb/pipeline/analyze.ts) and [`pipeline/pairs.ts`](https://github.com/bnistor4/fotocopiatrice/blob/84b840c7e1253915b92bf1420706cd5c096b35cb/pipeline/pairs.ts) call `TypeSafeClient`. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and TypeScript check inspected; live pipeline and political claims not re-run. |
| Maintainer | [bnistor4](https://github.com/bnistor4). Independently curated. |
| Format | Next.js **15** static app + TypeScript pipeline (`fotocopiatrice` 0.1.0). |
| Platform and availability | Hosted static site; local `npm run dev` / pipeline scripts. Italian UI and Camera dei Deputati data for A.C. 2112-bis (budget bill) in the reviewed tree. |
| Jev's role | Judges amendment attributes and candidate “photocopy” pairs with calibrated probabilities. Deterministic SHA-1 / Jaccard grouping is code-only. Jev does not invent amendment text. |
| Requirements | Node.js for site/pipeline; `TYPESAFE_API_KEY` only for regenerating model caches. |
| License | Code [MIT](https://github.com/bnistor4/fotocopiatrice/blob/84b840c7e1253915b92bf1420706cd5c096b35cb/LICENSE); derived data CC BY 4.0 (`LICENSE-DATI`). Camera source data remains under Camera terms. |

## When to use

Use it to explore identical/near-equivalent Italian amendments with inspectable Jev caches and reuse-ready exports. Prefer general classification demos when you do not need Camera open-data plumbing. Do not treat model pair scores as proof of copying or illegality—the README states those limits explicitly.

## How it works

The pipeline scrapes Camera XML, deduplicates republished texts, then asks Jev closed questions per amendment and per Jaccard-candidate pair. Aggregates land in `public/data/` (site) and `export/` (third-party reuse). The Vercel site serves JSON only—no API key on the server.

## Get started

```sh
git clone https://github.com/bnistor4/fotocopiatrice.git
cd fotocopiatrice
git checkout 84b840c7e1253915b92bf1420706cd5c096b35cb
npm ci
npm run dev   # http://localhost:3000 — uses committed JSON
# optional regenerate (TYPESAFE_API_KEY in .env.local):
# npm run pipeline:analyze && npm run pipeline:pairs && npm run pipeline:build
```

Or open [fotocopiatrice.vercel.app](https://fotocopiatrice.vercel.app/) (HTTP 200 on review host).

## Examples and demos

- Hosted site for legge di bilancio 2025 (A.C. 2112-bis).
- Review host: `npx tsc --noEmit` succeeded after `npm ci`. No live TypeSafe pipeline run.

## Limits and data handling

Model outputs are probabilities, not facts. Live pipeline sends amendment text/hashes to TypeSafe. Political interpretations remain the reader’s responsibility. Large `emendamenti.json` may need splitting before adding another act.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 84b840c](https://github.com/bnistor4/fotocopiatrice/tree/84b840c7e1253915b92bf1420706cd5c096b35cb): **0.1.0**, MIT. AI-assisted review of README, LICENSE, `pipeline/questions.ts`, analyze/pairs entrypoints; `tsc --noEmit` clean. Hosted homepage fetched (200). No live TypeSafe call.

Related: [Watermelon](watermelon.md), [RefGarden](refgarden.md), [Hx](hx.md).
