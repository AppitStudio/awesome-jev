# Choice Four

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Four-in-a-row against Jev: the rules engine finds legal moves and tactical facts, and every Jev turn is a structured Choice over the remaining columns, with server-authoritative matches, Discord sign-in, leaderboards and a hash-linked move journal.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jevplays-games/jev-connect-four) |
| Maintainer | [jevplays-games](https://github.com/jevplays-games). Independently curated. |
| Format | Node.js game server + browser UI (also deployable as a Cloudflare Worker) |
| Requirements | Node.js 22.16+; `TYPESAFE_API_KEY` for Jev games; Discord app credentials for ranked play. |
| License | [MIT](https://github.com/jevplays-games/jev-connect-four/blob/b46f4ad28b0eade9f3c981c2e9f5c902ce8d6453/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/jev.js`](https://github.com/jevplays-games/jev-connect-four/blob/b46f4ad28b0eade9f3c981c2e9f5c902ce8d6453/server/jev.js) at the pinned commit. |

## When to use

- Play Connect Four against Jev and inspect how it weighs each column.
- Study a server-side pattern where code enforces the rules and Jev only chooses among legal candidates.
- Mismatch: local practice uses a heuristic, not Jev; live Jev, Discord and Cloudflare paths were not exercised by the authors when packaging.

## How it works

The server's Jev adapter posts the board context and candidate columns to `https://api.typesafe.ai/v1/systemone` with the key held server-side, validates the scores, ranks candidates, and records every move in a hash-linked event journal stored in SQLite or D1. Integration evidence: [`server/jev.js`](https://github.com/jevplays-games/jev-connect-four/blob/b46f4ad28b0eade9f3c981c2e9f5c902ce8d6453/server/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jevplays-games/jev-connect-four.git && cd jev-connect-four
npm start   # local practice at http://localhost:8787
cp .env.example .env   # set TYPESAFE_API_KEY for Jev games, then restart
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Analytics and tests: README sections Analytics and Tests and tools.

## Limits and data handling

Board states go to TypeSafe on the operator's key; the key never reaches the browser. Discord identity only for ranked play.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit b46f4ad28b0e](https://github.com/jevplays-games/jev-connect-four/tree/b46f4ad28b0eade9f3c981c2e9f5c902ce8d6453). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
