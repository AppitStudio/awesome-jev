# JevMap (typed Jev decisions for spatial web-map workflows)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MapLibre web-map demo where Jev picks spatial tools, layers and allowed parameter candidates from bounded choices built from a semantic summary of the map, Turf.js runs the buffer, intersect, nearest, filter, select and export operations deterministically, and every model-assisted step is kept as a replayable receipt; an optional local Julia 1 model is supported.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danmaps/jevmap) |
| Maintainer | [danmaps](https://github.com/danmaps). Independently curated. |
| Format | TypeScript web app (Vite, MapLibre GL JS) |
| Requirements | Node.js and npm; your own server-side `/api/jev` proxy holding a TypeSafe key (not included in the repository). |
| License | [MIT](https://github.com/danmaps/jevmap/blob/d7a948afa1a285374b1d3fce7a244c9f796e59fb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisions/index.ts`](https://github.com/danmaps/jevmap/blob/d7a948afa1a285374b1d3fce7a244c9f796e59fb/src/decisions/index.ts) at the pinned commit. |

## When to use

- Prototype natural-language GIS tasks without letting a model touch geometry.
- Review and approve lower-confidence spatial calls from a receipt before they run.
- Mismatch: you must add the server-side Jev proxy; the browser never holds the key.

## How it works

`src/decisions/index.ts` builds System One request payloads with Choice questions (default `jev-latest`) and sends them to the same-origin `/api/jev` route; policy and runtime guards check each choice before Turf.js executes it. Integration evidence: [`src/decisions/index.ts`](https://github.com/danmaps/jevmap/blob/d7a948afa1a285374b1d3fce7a244c9f796e59fb/src/decisions/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run dev
# provide a server-side /api/jev proxy to TypeSafe; VITE_TYPESAFE_MODEL=jev-latest selects the model
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/danmaps/jevmap#readme](https://github.com/danmaps/jevmap#readme)
- Inspiration: [github.com/danmaps/webmap_ai](https://github.com/danmaps/webmap_ai)

## Limits and data handling

Compact map summaries and the task go to TypeSafe through your proxy; geometry stays in the browser. Estimated costs use published Jev pricing.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit d7a948afa1a2](https://github.com/danmaps/jevmap/tree/d7a948afa1a285374b1d3fce7a244c9f796e59fb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
