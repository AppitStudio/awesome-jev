# JevChess by shihabalratul (Jev picks every chess move through multiple-choice questions while GPT Luna reads the board, no engine)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Experiment in whether a decision model can play chess: Jev picks every move by answering a short series of multiple-choice questions (attack or defend, what will the opponent reply, which finalist is best), GPT Luna reads the board, and a rules engine keeps every move legal. No Stockfish and no opening book. Includes a Chrome extension, a server, Lichess play and benchmark scripts, and a public replay page of a recorded win against Lichess AI level 2.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shihabalratul/Jev-chess) |
| Maintainer | [shihabalratul](https://github.com/shihabalratul). Independently curated. |
| Format | TypeScript monorepo (server, Chrome extension, scripts) |
| Requirements | Node.js 22.13+, pnpm 10 and Chrome, plus an OpenRouter key for Jev (`typesafe/jev-1.13`) and Luna; a Lichess token only for online play. |
| License | [MIT](https://github.com/shihabalratul/Jev-chess/blob/bd1ce7865b6ffd3bc590ca4a41dd2172807265b0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`apps/server/src/services/decisions.ts`](https://github.com/shihabalratul/Jev-chess/blob/bd1ce7865b6ffd3bc590ca4a41dd2172807265b0/apps/server/src/services/decisions.ts) at the pinned commit. |

## When to use

- See how far a decision model gets at chess when every move is a typed choice.
- Mismatch: a strong chess engine; it plays at a modest level by design.

## How it works

`apps/server/src/services/decisions.ts` runs the staged move-choice questions against `typesafe/jev-1.13` through OpenRouter's Decisions API and records each decision for the replay panel. Integration evidence: [`apps/server/src/services/decisions.ts`](https://github.com/shihabalratul/Jev-chess/blob/bd1ce7865b6ffd3bc590ca4a41dd2172807265b0/apps/server/src/services/decisions.ts).

## Get started

Watch the recorded game in the browser, or build the project and run it against Lichess with your keys.

```sh
# watch: https://shihabalratul.github.io/Jev-chess/
git clone https://github.com/shihabalratul/Jev-chess && cd Jev-chess
pnpm install && pnpm build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Replay page: [shihabalratul.github.io/Jev-chess/](https://shihabalratul.github.io/Jev-chess/)
- README: [github.com/shihabalratul/Jev-chess/blob/bd1ce7865b6ffd3bc590ca4a41dd2172807265b0/README.md](https://github.com/shihabalratul/Jev-chess/blob/bd1ce7865b6ffd3bc590ca4a41dd2172807265b0/README.md)

## Limits and data handling

Board descriptions go to OpenRouter on your key; each move takes several paid calls. Results in the README are the author's runs.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit bd1ce7865b6f](https://github.com/shihabalratul/Jev-chess/tree/bd1ce7865b6ffd3bc590ca4a41dd2172807265b0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
