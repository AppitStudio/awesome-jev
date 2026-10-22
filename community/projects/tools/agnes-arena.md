# AGNES Arena (Pokémon battles with Jev-assisted decisions)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Pokémon Showdown battle arena where two persistent agent players evaluate legal moves through Jev, commit an action and play whole matches, with session management, a scheduler and a browser battle viewer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ZRDONG/AGNES-Arena) |
| Maintainer | [ZRDONG](https://github.com/ZRDONG). Independently curated. |
| Format | Node.js workspace (four packages) |
| Requirements | Node.js 24.10 to 24.x; an AGH player workspace; `TYPESAFE_API_KEY` for live Jev (an offline stub is included). |
| License | [MIT](https://github.com/ZRDONG/AGNES-Arena/blob/6f181aedafdeb0cc2019afe2579c9b97c23deda2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`packages/jev-client/index.mjs`](https://github.com/ZRDONG/AGNES-Arena/blob/6f181aedafdeb0cc2019afe2579c9b97c23deda2/packages/jev-client/index.mjs) at the pinned commit. |

## When to use

- Watch an agent keep context across a full turn-based match.
- Inspect how a Jev evaluation becomes a committed game action.
- Mismatch: needs the AGH agent setup described in RUNNING.md.

## How it works

`packages/jev-client/index.mjs` posts the battle state and legal candidates to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) as an `action` choice; the player picks the move and Showdown owns the rules. Integration evidence: [`packages/jev-client/index.mjs`](https://github.com/ZRDONG/AGNES-Arena/blob/6f181aedafdeb0cc2019afe2579c9b97c23deda2/packages/jev-client/index.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
npm run battle:build
# then follow RUNNING.md to start the players
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Running the players: [github.com/ZRDONG/AGNES-Arena/blob/main/RUNNING.md](https://github.com/ZRDONG/AGNES-Arena/blob/main/RUNNING.md)
- Match walkthrough video: [github.com/ZRDONG/AGNES-Arena/blob/main/demo/arena-match.mp4](https://github.com/ZRDONG/AGNES-Arena/blob/main/demo/arena-match.mp4)

## Limits and data handling

Battle states are sent to TypeSafe in live mode. Pokémon Showdown is a separate project with its own license.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 6f181aedafde](https://github.com/ZRDONG/AGNES-Arena/tree/6f181aedafdeb0cc2019afe2579c9b97c23deda2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
