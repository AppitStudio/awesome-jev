# AI Chess Benchmark: Jev vs Fable (side-by-side web benchmark where Jev picks chess moves from the legal-move list against identical Stockfish opponents)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Next.js benchmark that plays Jev (a System One model) and Anthropic's Fable side by side against identical Stockfish opponents. Jev gets the game state and one `choice` question whose options are every legal move; the app plays its pick and records confidence and top-3 probabilities, then reports results, centipawn loss, accuracy, speed, cost, illegal-move retries and calibration, with CSV and PGN export.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NJashwanth/chess_ai) |
| Maintainer | [NJashwanth](https://github.com/NJashwanth). Independently curated. |
| Format | Next.js web app (MIT; bundled Stockfish 19 WASM stays under GPL-3.0) |
| Requirements | Node.js and npm, a `TYPESAFE_API_KEY` (or `OPENROUTER_API_KEY` with `JEV_PROVIDER=openrouter`) for the Jev board, and an `ANTHROPIC_API_KEY` for the Fable board; if one key is missing the other board still runs. |
| License | [MIT](https://github.com/NJashwanth/chess_ai/blob/2731a50e24ad2efc72d362ed004232588492cf92/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/jev.ts`](https://github.com/NJashwanth/chess_ai/blob/2731a50e24ad2efc72d362ed004232588492cf92/src/lib/jev.ts) at the pinned commit. |

## When to use

- Compare a System One decision model with a text-generating model on the same game states, cost, speed and calibration.
- Study how often a typed choice question returns an illegal or low-confidence move.
- Mismatch: TypeSafe's token pricing is not published, so the cost columns use placeholder rates you must set yourself.

## How it works

`src/lib/jev.ts` posts `{base}/v1/systemone` with the model pinned to `jev-1.13.0` on TypeSafe or `typesafe/jev-1.13` on OpenRouter, retrying 429, 503 and 529 gateway errors inside a 30 second budget; both boards receive the identical state payload built in `src/lib/state.ts`. Integration evidence: [`src/lib/jev.ts`](https://github.com/NJashwanth/chess_ai/blob/2731a50e24ad2efc72d362ed004232588492cf92/src/lib/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.example .env.local   # add TYPESAFE_API_KEY and ANTHROPIC_API_KEY
npm run dev                  # http://localhost:3000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (setup, metrics, upstream-error handling): [github.com/NJashwanth/chess_ai/blob/2731a50e24ad2efc72d362ed004232588492cf92/README.md](https://github.com/NJashwanth/chess_ai/blob/2731a50e24ad2efc72d362ed004232588492cf92/README.md)

## Limits and data handling

Game states are sent to TypeSafe (or OpenRouter) and to Anthropic on your keys, and games cost real tokens. Small game counts give noisy comparisons. The repository was created on 2026-11-05, so it is brand new and unproven.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 2731a50e24ad](https://github.com/NJashwanth/chess_ai/tree/2731a50e24ad2efc72d362ed004232588492cf92). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
