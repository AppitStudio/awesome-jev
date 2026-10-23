# Jong (Pong against Jev)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Pong in the browser against an AI paddle steered by Jev's typed decisions, fetched live during a best-of-3 match, with Jev's response time shown in the HUD.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alexandreroman/jong) |
| Maintainer | [alexandreroman](https://github.com/alexandreroman). Independently curated. |
| Format | Browser game (canvas) with a small Node.js proxy |
| Requirements | Node.js 24.2+, make; a TypeSafe API key entered in the game (kept in memory only). |
| License | [Apache-2.0](https://github.com/alexandreroman/jong/blob/7303b1276895760ca554efe81b4bab090b47b041/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/api.js`](https://github.com/alexandreroman/jong/blob/7303b1276895760ca554efe81b4bab090b47b041/src/api.js) at the pinned commit. |

## When to use

- Feel Jev's latency and decisions in a real-time loop.
- Use as a tiny, dependency-free reference for calling Jev from the browser through a proxy.
- Mismatch: a toy; the opponent's play depends on network latency.

## How it works

`src/api.js` asks `jev-latest` to pick the court zone where the ball will meet the AI paddle, and `server.mjs` forwards those calls to `https://api.typesafe.ai/v1/systemone`. Integration evidence: [`src/api.js`](https://github.com/alexandreroman/jong/blob/7303b1276895760ca554efe81b4bab090b47b041/src/api.js).

## Get started

From the upstream README (not run on the review host):

```sh
make dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Gameplay video and Docker targets in the README: [github.com/alexandreroman/jong#readme](https://github.com/alexandreroman/jong#readme)

## Limits and data handling

Game state is sent to TypeSafe on every decision; the key is never stored, per the README.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 7303b1276895](https://github.com/alexandreroman/jong/tree/7303b1276895760ca554efe81b4bab090b47b041). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
