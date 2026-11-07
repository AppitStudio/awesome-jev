# JEV-block-out (TypeSafe Jev plays the Block Out! puzzle game)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

AI player for the mobile puzzle game Block Out! driven by TypeSafe Jev via `@typesafe-ai/sdk`, with a live watchable simulation of it solving levels.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mrinal-rangers/JEV-block-out) |
| Maintainer | [mrinal-rangers](https://github.com/mrinal-rangers). Independently curated. |
| Format | TypeScript monorepo (no SPDX license file on the reviewed commit) |
| Requirements | Node.js and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/bridge/src/jev.ts`](https://github.com/mrinal-rangers/JEV-block-out/blob/31048cda6c57f6b89b53c65c6f6da995bd06a92d/packages/bridge/src/jev.ts) at the pinned commit. |

## When to use

- Watch Jev pick moves in a color-sort puzzle.
- Reuse the bridge pattern for other turn-based games.
- Mismatch: hobby game agent; no OSI license on the reviewed commit.

## How it works

`packages/bridge/src/jev.ts` uses `TypeSafeClient` with `choice`/`noul`/`score` questions to choose moves. Integration evidence: [`packages/bridge/src/jev.ts`](https://github.com/mrinal-rangers/JEV-block-out/blob/31048cda6c57f6b89b53c65c6f6da995bd06a92d/packages/bridge/src/jev.ts).

## Get started

Clone, copy `.env.example`, set TYPESAFE_API_KEY, and run the simulation per README.

```sh
git clone https://github.com/mrinal-rangers/JEV-block-out.git && cd JEV-block-out
export TYPESAFE_API_KEY=...
npm install && npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mrinal-rangers/JEV-block-out/blob/31048cda6c57f6b89b53c65c6f6da995bd06a92d/README.md](https://github.com/mrinal-rangers/JEV-block-out/blob/31048cda6c57f6b89b53c65c6f6da995bd06a92d/README.md)

## Limits and data handling

Board states are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 31048cda6c57](https://github.com/mrinal-rangers/JEV-block-out/tree/31048cda6c57f6b89b53c65c6f6da995bd06a92d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
