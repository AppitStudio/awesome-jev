# Apparite (jev2ui)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local design-mock lab: TypeSafe Jev chooses information architecture and component anatomy; Gemini writes copy; code assembles A2UI-inspired mocks painted by a DESIGN.md.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dglazkov/jev2ui) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/dglazkov/jev2ui#readme) — local Vite app (Apparite); no separate commercial product page. |
| Pricing and access | Apache-2.0 source has no app purchase fee, checked **2026-09-20**. Live mocks need a TypeSafe/Jev key and a Gemini key (see `.env.example`). Provider usage is billed separately. |
| Jev evidence | Inspected [`src/server/models.ts`](https://github.com/dglazkov/jev2ui/blob/d55836912ff022db5671e5cf0b75011d35607bb5/src/server/models.ts): `@typesafe-ai/sdk` `TypeSafeClient` with default model `jev-latest`, plus design-mix / IA probe paths that issue typed System One questions. Live mock generation was not run. |
| Disclosure | Free source access does not include TypeSafe or Gemini usage. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [dglazkov](https://github.com/dglazkov). |
| Format | TypeScript Vite + Node server (`jev2ui` / Apparite **1.0.0**). |
| Platform and availability | Source build; `npm run dev` serves the UI (default Vite localhost). Experimental research/demo quality—not a hosted SaaS. |
| Jev's role | Chooses archetypes, blocks, anatomy, and instance controls as calibrated Choice/Score/Noul answers; Gemini supplies prose; application code owns tree assembly, validity, and chrome. Optional `gev` endpoint speaks the same wire format for experiments. |
| Requirements | Node.js matching the lockfile; `JEV_API_KEY` (or upstream-documented TypeSafe key) and Gemini credentials for full mock generation. IA probes can run Jev-only without Gemini. |
| License | [Apache-2.0](https://github.com/dglazkov/jev2ui/blob/d55836912ff022db5671e5cf0b75011d35607bb5/LICENSE). |

## When to use

Use it to study “Jev decides structure, text model writes words, code assembles UI” with inspectable per-turn probabilities. Prefer production design tools or component libraries when you need shipped product UI—not an experimental mock loop. Do not treat probe timing or sample-sweep writeups as catalog-measured quality scores.

## How it works

A prompt drives nested Jev questions that fill a mock tree (archetype → blocks → anatomy → instance controls). Gemini streams copy into slots; DESIGN.md themes the result. Compare mode and IA probes (`probe:ia`, `observe:journeys`) exercise decision endpoints without always rendering full mocks.

## Get started

```sh
git clone https://github.com/dglazkov/jev2ui.git
cd jev2ui
git checkout d55836912ff022db5671e5cf0b75011d35607bb5
npm ci --ignore-scripts
cp .env.example .env   # add keys for live mocks
npm run typecheck
npm run build
npm run dev            # http://localhost:5173 — live keys required for full generation
```

## Examples and demos

- Upstream README walkthrough and closed-IA / sample-sweep docs under [`docs/`](https://github.com/dglazkov/jev2ui/tree/d55836912ff022db5671e5cf0b75011d35607bb5/docs).
- `compare.html` dual-run UI for Jobs / Sections / Baseline modes.
- No `npm test` script at this revision; typecheck and production build were used as offline checks.

## Limits and data handling

Prompts and design state go to TypeSafe Jev and Gemini when live. Experimental UX and catalogs may change. IA sample results in docs are author-reported. Failures and uncertain answers should be read from the decision list—do not assume a pretty mock is correct.

## Review and maintenance

Reviewed on **2026-09-20** at [commit d558369](https://github.com/dglazkov/jev2ui/tree/d55836912ff022db5671e5cf0b75011d35607bb5): **1.0.0**, Apache-2.0. AI-assisted source review of `models.ts`, design-mix paths, README, and LICENSE. On Node.js 22.23.2: **`npm run typecheck`** and **`npm run build`** passed. No live Jev or Gemini calls.

Related: [JevSlop](jevslop.md), [RefGarden](refgarden.md).
