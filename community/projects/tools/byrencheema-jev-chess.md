# jev-chess (byrencheema)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Experiment where Jev plays chess by choosing one move from all legal moves as a single Choice per turn, with no search or filtering: 350 games vs Stockfish and Maia, 50 vs random, 1,000 Lichess puzzles, Stockfish analysis and all results committed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/byrencheema/jev-chess) |
| Maintainer | [byrencheema](https://github.com/byrencheema). Independently curated. |
| Format | Bun/TypeScript CLI (`play`, `eval`, `puzzles`, `analyze`) + committed result files |
| Requirements | Bun, Stockfish and Lc0 (Maia weights), zstd and the Lichess puzzle database; `TYPESAFE_API_KEY`, `TYPESAFE_BASE_URL`, `TYPESAFE_MODEL` in `.env`. |
| License | **No LICENSE file** in the reviewed tree — publicly readable source with unspecified reuse terms; Source available, not Open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Study prompt and state-format effects on a hard sequential task where every option is legal.
- Reuse the budget-capped eval runner and Stockfish analysis for your own Jev agent.
- Mismatch: no LICENSE file, so reuse terms are unspecified; results are the maintainer's runs.

## How it works

[`src/jev.ts`](https://github.com/byrencheema/jev-chess/blob/1c2ecb4e783485a9773f5d341d30e71f0174f2af/src/jev.ts) sends the position (prompt variants in [`src/prompt.ts`](https://github.com/byrencheema/jev-chess/blob/1c2ecb4e783485a9773f5d341d30e71f0174f2af/src/prompt.ts)) with every legal move as Choice options and plays the pick; [`src/runner.ts`](https://github.com/byrencheema/jev-chess/blob/1c2ecb4e783485a9773f5d341d30e71f0174f2af/src/runner.ts) and [`src/puzzles.ts`](https://github.com/byrencheema/jev-chess/blob/1c2ecb4e783485a9773f5d341d30e71f0174f2af/src/puzzles.ts) run games and puzzles with concurrency and a dollar budget, and [`src/analysis.ts`](https://github.com/byrencheema/jev-chess/blob/1c2ecb4e783485a9773f5d341d30e71f0174f2af/src/analysis.ts) scores moves with Stockfish.

## Get started

Setup and commands from the README:

```sh
git clone https://github.com/byrencheema/jev-chess.git && cd jev-chess
brew install stockfish lc0 zstd && bun install
# add TYPESAFE_API_KEY, TYPESAFE_BASE_URL, TYPESAFE_MODEL to .env
bun run play --white jev --black stockfish:1320
bun run puzzles --set eval --agent jev --budget 0.10
```

Each move is a Jev request billed to your key; the README estimates about $0.001 per game and commands accept a `--budget` cap.

## Examples and demos

- README results (maintainer, held-out): 0 wins/14 draws/336 losses vs Stockfish and Maia, 23/26/1 vs random, puzzle rating 1085 on 1,000 puzzles, 0 illegal moves in 13,817 calls.
- Raw games, puzzles and analysis: [`results/`](https://github.com/byrencheema/jev-chess/tree/1c2ecb4e783485a9773f5d341d30e71f0174f2af/results).

## Limits and data handling

No LICENSE file. Results are upstream measurements with jev-1.13.0. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 1c2ecb4e7834](https://github.com/byrencheema/jev-chess/tree/1c2ecb4e783485a9773f5d341d30e71f0174f2af). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
