# Tetris: You vs Jev (play Tetris against a Jev-assisted opponent)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Two-board Tetris in the browser where you play against a Jev-assisted planner on the same seeded 7-bag sequence, with garbage lines for clears, three difficulty levels and an offline planner that needs no key; a small local Python server forwards moves to TypeSafe with your key held only in page memory.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shuenrui/tetris-vs-jev) |
| Maintainer | [shuenrui](https://github.com/shuenrui). Independently curated. |
| Format | Browser game with a Python standard-library server |
| Requirements | Python 3.10+; a TypeSafe API key for the Jev opponent (offline planner without it). |
| License | [MIT](https://github.com/shuenrui/tetris-vs-jev/blob/eaabc7ac3bf726f9d1d1c6a925f4edf1748f3cf8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_api.py`](https://github.com/shuenrui/tetris-vs-jev/blob/eaabc7ac3bf726f9d1d1c6a925f4edf1748f3cf8/jev_api.py) at the pinned commit. |

## When to use

- Play against a decision model in real time.
- See a simple state-to-Choice loop for a game agent.
- Mismatch: distinct from the separately listed Tetris Arena and deadline-tetris; TypeSafe keys only.

## How it works

`jev_api.py` posts the board and candidate placements as a Choice to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); network failures retry once, then the labelled local fallback plays. Integration evidence: [`jev_api.py`](https://github.com/shuenrui/tetris-vs-jev/blob/eaabc7ac3bf726f9d1d1c6a925f4edf1748f3cf8/jev_api.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/shuenrui/tetris-vs-jev.git && cd tetris-vs-jev
python3 server.py   # open http://127.0.0.1:8765/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/shuenrui/tetris-vs-jev#readme](https://github.com/shuenrui/tetris-vs-jev#readme)

## Limits and data handling

Board descriptions go to TypeSafe with your key; the app writes no key files or request logs.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit eaabc7ac3bf7](https://github.com/shuenrui/tetris-vs-jev/tree/eaabc7ac3bf726f9d1d1c6a925f4edf1748f3cf8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
