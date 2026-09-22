# Jev Trip

[All projects](../README.md) · [Web apps](README.md#web-apps)

Explainable day-trip planner: an LLM drafts the itinerary; TypeSafe Jev screens candidates, compares transport, answers typed planning questions, and reviews; deterministic code owns routes, timing, validation, and repair bounds.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/liaoyuhua/jev-trip) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/liaoyuhua/jev-trip#readme) — local Next.js UI on `127.0.0.1:3100`; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-23**. Live mode needs `TYPESAFE_API_KEY`, `LLM_API_KEY` / `LLM_MODEL`, and `AMAP_KEY`. Replay demo needs no keys. Provider/map usage can incur charges. |
| Jev evidence | Inspected [`lib/providers/jev.ts`](https://github.com/liaoyuhua/jev-trip/blob/782a5f8b46d5bdf0b0048f33751551797ccc0de2/lib/providers/jev.ts): `POST https://api.typesafe.ai/v1/systemone` with Choice questions for screening, transport, queries, and review (`jev-1.13.0` default). Offline `npm test` **35 passed**; `tsc --noEmit` clean. Live Amap/LLM/Jev not run. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer, Amap, or TypeSafe. Listing is not an endorsement. Single-day mainland China scope; results are drafts, not guaranteed executable itineraries. |
| Maintainer | [liaoyuhua](https://github.com/liaoyuhua). |
| Format | Next.js 15 / React 19 local app (`jev-trip` **0.1.0**). |
| Platform and availability | Source build; `npm run dev -- --hostname 127.0.0.1 --port 3100`. Replay demo is fully offline. |
| Jev's role | Screens places, scores transport options, answers typed subject queries, and reviews schedule shape; controller code owns facts, IDs, timing math, and retry limits. LLM plans/repairs text itineraries. |
| Requirements | Node.js suitable for Next 15; live keys as above. |
| License | [MIT](https://github.com/liaoyuhua/jev-trip/blob/782a5f8b46d5bdf0b0048f33751551797ccc0de2/LICENSE). |

## When to use

Use it to study **Jev-gated trip planning** with a replayable offline demo before spending on maps/LLM/Jev. Prefer travel booking products when you need multi-day trips, live opening hours, or reservations (out of current scope).

## How it works

Places/routes feed an LLM planner. [`lib/providers/jev.ts`](https://github.com/liaoyuhua/jev-trip/blob/782a5f8b46d5bdf0b0048f33751551797ccc0de2/lib/providers/jev.ts) issues batched Choice questions; the controller validates and may request repair. Fixture mode scripts decisions without network.

## Get started

```sh
git clone https://github.com/liaoyuhua/jev-trip.git
cd jev-trip
git checkout 782a5f8b46d5bdf0b0048f33751551797ccc0de2
npm ci --ignore-scripts
npm test
npm run typecheck
# Live: cp .env.example .env.local; set keys; npm run dev -- --hostname 127.0.0.1 --port 3100
```

## Examples and demos

- Replay demo in the UI (no credentials).
- Offline on the review host: vitest **35 passed**; typecheck clean.

## Limits and data handling

Live mode sends preferences/place facts to TypeSafe and the configured LLM, and uses Amap for places/routes. Mainland China single-day only. No live spend on this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 782a5f8](https://github.com/liaoyuhua/jev-trip/tree/782a5f8b46d5bdf0b0048f33751551797ccc0de2) (`0.1.0`, MIT). AI-assisted review of README, LICENSE, `lib/providers/jev.ts`. **`npm test` / `typecheck` OK**; live not run.

Related: [Hearth](hearth.md), [Jev Radar](jev-radar.md).
