# Games by productowner.ro (browser Tetris, chess and a Monopoly-style game where Jev makes the players' moves)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Browser games built with Claude to show Jev as a gameplay engine: Jev decides the moves in tetris, chess and "mitropoly". A Cloudflare-style Worker passes calls to Jev under a daily cap and logs games to D1; it also runs on the open-source workerd runtime via Docker Compose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/productowner-ro/games) |
| Maintainer | [Gabi Udrescu / productowner.ro](https://github.com/productowner-ro). Independently curated. |
| Format | JavaScript browser games with a Worker backend (Docker Compose for local runs) |
| Requirements | Docker and a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [AGPL-3.0](https://github.com/productowner-ro/games/blob/b13fef76ce5b428aa670d0403099e24979025bd2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`worker/src/index.js`](https://github.com/productowner-ro/games/blob/b13fef76ce5b428aa670d0403099e24979025bd2/worker/src/index.js) at the pinned commit. |

## When to use

- See Jev drive game moves, or reuse the capped Worker pattern for a public Jev demo.
- Mismatch: if you want a hosted game to play now; the public site was not live on 2026-11-25.

## How it works

`worker/src/index.js` forwards each game's decision request to `https://api.typesafe.ai/v1/systemone` after reserving calls against a daily cap (default 5,000). Integration evidence: [`worker/src/index.js`](https://github.com/productowner-ro/games/blob/b13fef76ce5b428aa670d0403099e24979025bd2/worker/src/index.js).

## Get started

Start the dev stack with your key; the planned public site games.productowner.ro did not serve the games when checked.

```sh
git clone https://github.com/productowner-ro/games.git && cd games
export TYPESAFE_API_KEY=...
docker compose up dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Plan to put the games online: [github.com/productowner-ro/games/issues/1](https://github.com/productowner-ro/games/issues/1)

## Limits and data handling

AGPL-3.0: running a modified copy as a site requires publishing its source. Each move is a paid Jev call on your key, bounded by the daily cap.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit b13fef76ce5b](https://github.com/productowner-ro/games/tree/b13fef76ce5b428aa670d0403099e24979025bd2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
