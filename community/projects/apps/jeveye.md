# JevEye

[All projects](../README.md) · [Web apps](README.md#web-apps)

Browser vision probes report calibrated facts (or abstain); TypeSafe Jev never sees pixels—it plans what to look for and judges the text fact sheet.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Adityakhalkar/JevEye) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/Adityakhalkar/JevEye#readme) — Next.js app; deployable to Vercel with `TYPESAFE_API_KEY`. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-21**. Live judgments need a TypeSafe key. Vision models run in the visitor's browser; provider usage is billed separately. |
| Jev evidence | Inspected [`src/lib/jev.ts`](https://github.com/Adityakhalkar/JevEye/blob/86357ab550077682a8073c4eb76e9a3ac998e595/src/lib/jev.ts) (`@typesafe-ai/sdk` `TypeSafeClient`) and API routes under `src/app/api/plan` / `judge`. Live image judgment was not run. |
| Disclosure | Free source access does not include TypeSafe usage. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [Adityakhalkar](https://github.com/Adityakhalkar). |
| Format | Next.js TypeScript app (`JevEye`). |
| Platform and availability | Source build / Vercel deploy; experimental demo quality. |
| Jev's role | Reads the user question into a bounded reading (only/every/presence/count/rating/…), chooses probes and label sets, then judges the vision fact sheet as text. The CNN/open-vocab layer never judges; Jev never sees pixels. |
| Requirements | Node.js 20+; `TYPESAFE_API_KEY` on the server (`.env.local`). |
| License | [MIT](https://github.com/Adityakhalkar/JevEye/blob/86357ab550077682a8073c4eb76e9a3ac998e595/LICENSE). |

## When to use

Use it to study a strict see-then-judge split for photos: local probes produce probabilities, Jev concludes in text with inspectable confidence. Prefer a single VLM when you want one opaque multimodal pass instead of a readable fact sheet.

## How it works

Plan/judge API routes call Jev via `@typesafe-ai/sdk`. Browser-side vision probes emit calibrated labels/coverage/scores; the server forwards only text state. Calibration helpers are covered by offline unit tests.

## Get started

```sh
git clone https://github.com/Adityakhalkar/JevEye.git
cd JevEye
git checkout 86357ab550077682a8073c4eb76e9a3ac998e595
npm ci
npm test
# Live UI (charges TypeSafe):
# echo 'TYPESAFE_API_KEY=…' > .env.local && npm run dev
```

## Examples and demos

- README walkthrough with a flower-field fixture explanation and reading table.
- Fixtures under [`fixtures/`](https://github.com/Adityakhalkar/JevEye/tree/86357ab550077682a8073c4eb76e9a3ac998e595/fixtures).

## Limits and data handling

Questions and fact sheets go to TypeSafe on live plan/judge calls; images stay in the browser for probing. Experimental UX and label sets may change. Do not treat demo confidence numbers as catalog-remeasured accuracy.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 86357ab](https://github.com/Adityakhalkar/JevEye/tree/86357ab550077682a8073c4eb76e9a3ac998e595): MIT. AI-assisted source review of `src/lib/jev.ts`, plan/judge routes, README, and LICENSE. On Node.js 22.23.2, **`npm test`**: **12 pass / 0 fail**. No live TypeSafe or browser vision runs on the review host.

Related: [Apparite (jev2ui)](jev2ui.md), [Transcript Lens](transcript-lens.md).
