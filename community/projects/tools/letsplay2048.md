# letsplay2048 (decision models, including Jev, play 2048 live on OpenRouter)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Code and a daily-refreshed copy of every game on letsplay2048.lol, where models on OpenRouter's Decisions API, including Jev 1.13 and 1.14, play 2048 live at one move every three seconds; the player skips the model when only one move is possible.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mprpic/letsplay2048) |
| Maintainer | [mprpic](https://github.com/mprpic). Independently curated. |
| Format | Python player and game records |
| Requirements | Python 3; an OpenRouter key to play new games. |
| License | [MIT](https://github.com/mprpic/letsplay2048/blob/0d7860cf8095945c705a880ac64821999e807c63/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`v1/player.py`](https://github.com/mprpic/letsplay2048/blob/0d7860cf8095945c705a880ac64821999e807c63/v1/player.py) at the pinned commit. |

## When to use

- Compare decision models on a simple game with public records.
- Reuse the player loop as a minimal Decisions API example.
- Mismatch: game records are data, not a benchmark claim.

## How it works

`v1/player.py` sends the board, score and possible moves to `https://openrouter.ai/api/alpha/decisions` with models such as `typesafe/jev-1.13` and `typesafe/jev-1.14` and plays the chosen move. Integration evidence: [`v1/player.py`](https://github.com/mprpic/letsplay2048/blob/0d7860cf8095945c705a880ac64821999e807c63/v1/player.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/mprpic/letsplay2048 && cd letsplay2048
export OPENROUTER_API_KEY=...
# run the player in v1/player.py as described in the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [letsplay2048.lol](https://letsplay2048.lol)
- README: [github.com/mprpic/letsplay2048#readme](https://github.com/mprpic/letsplay2048#readme)

## Limits and data handling

Boards go to OpenRouter and on to the chosen model provider; Jev is reached through OpenRouter. Code is MIT; game records are CC0 (`LICENSE-DATA`).

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 0d7860cf8095](https://github.com/mprpic/letsplay2048/tree/0d7860cf8095945c705a880ac64821999e807c63). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
