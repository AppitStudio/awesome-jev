# Jev Ants (a thousand Jev-steered ants that form the word or picture you give them)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Browser simulation where every ant is its own Jev agent: it sees its nine neighbouring cells, how many ants each still wants and its neighbours' headings, and Jev answers which way to move and whether to settle, so about a thousand decisions turn a random scatter into a typed word or uploaded image; an image overseer and spend and time caps are built in.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/scalefreegan/jev-ants) |
| Maintainer | [scalefreegan](https://github.com/scalefreegan). Independently curated. |
| Format | React web app on a Vite dev server with a key-holding middleware |
| Requirements | Node.js and npm; a TypeSafe API key in `JEV_API_KEY` (the browser never sees it). |
| License | [MIT](https://github.com/scalefreegan/jev-ants/blob/24476e9c86e1aae23c3930eaa6984a0d8afb11fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`web/server/jev.ts`](https://github.com/scalefreegan/jev-ants/blob/24476e9c86e1aae23c3930eaa6984a0d8afb11fc/web/server/jev.ts) at the pinned commit. |

## When to use

- See many small typed decisions add up to emergent behaviour.
- Learn request packing and live spend caps from a compact example.
- Mismatch: a toy; the README cites about six to seven cents per formation.

## How it works

`web/server/jev.ts` is Vite middleware that forwards packed ant requests to `api.typesafe.ai` (`jev-latest`) and stops at the spend cap (default $0.50) or time cap (default 3 minutes) using real `usage.input_tokens` from each reply. Integration evidence: [`web/server/jev.ts`](https://github.com/scalefreegan/jev-ants/blob/24476e9c86e1aae23c3930eaa6984a0d8afb11fc/web/server/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
export JEV_API_KEY=...
cd web && npm install && npm run dev
open http://localhost:38500
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README and demo GIF: [github.com/scalefreegan/jev-ants#readme](https://github.com/scalefreegan/jev-ants#readme)

## Limits and data handling

Ant neighbourhoods and the target image go to TypeSafe. Cost figures are the author's.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 24476e9c86e1](https://github.com/scalefreegan/jev-ants/tree/24476e9c86e1aae23c3930eaa6984a0d8afb11fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
