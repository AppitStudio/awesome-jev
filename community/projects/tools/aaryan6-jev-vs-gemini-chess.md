# Jev vs Gemini Decision chess (TypeSafe's Jev plays chess against Google's Gemini Decision 1, one closed-set decision per move)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Next.js app where TypeSafe's Jev plays chess against Google's Gemini Decision 1: each turn code lists every legal move with computed facts, and each model answers a Choice over the moves plus a 7-level Score of who is better, shown with their top three candidate moves.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Aaryan6/jev-vs-gemini-chess) |
| Maintainer | [Aaryan6](https://github.com/Aaryan6). Independently curated. |
| Format | Next.js web app (TypeScript; no license file) |
| Requirements | Node.js with pnpm, `TYPESAFE_API_KEY` and `GEMINI_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. No license file on the reviewed commit, so reuse rights are not granted. Discovered via X ([post](https://x.com/aaryanpatel_06/status/2120930261735199015)). |
| Jev evidence | [`src/lib/players.ts`](https://github.com/Aaryan6/jev-vs-gemini-chess/blob/df96187d1b001c66c24d8efd34747501a4283850/src/lib/players.ts) at the pinned commit. |

## When to use

- Watch two decision models compare on the same closed-set chess decisions.
- Mismatch: strong chess play or an engine benchmark; this is a side-by-side demo.

## How it works

`src/lib/players.ts` holds both integrations: Jev through the official `@typesafe-ai/sdk` `systemOne` call (model `jev-1.14.0` by default) and Gemini through Google's Decisions API; `src/app/api/move/route.ts` checks the history and returns the pick. A toggle turns off the code-computed move facts. Integration evidence: [`src/lib/players.ts`](https://github.com/Aaryan6/jev-vs-gemini-chess/blob/df96187d1b001c66c24d8efd34747501a4283850/src/lib/players.ts).

## Get started

Add both keys to `.env.local`, install and start the dev server; the author also hosts a demo at jev-vs-gemini-chess.vercel.app (not reviewed).

```sh
pnpm install
pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Aaryan6/jev-vs-gemini-chess/blob/df96187d1b001c66c24d8efd34747501a4283850/README.md](https://github.com/Aaryan6/jev-vs-gemini-chess/blob/df96187d1b001c66c24d8efd34747501a4283850/README.md)
- Author's hosted demo (not reviewed): [jev-vs-gemini-chess.vercel.app](https://jev-vs-gemini-chess.vercel.app)

## Limits and data handling

Board states go to TypeSafe and Google on your keys when run locally.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit df96187d1b00](https://github.com/Aaryan6/jev-vs-gemini-chess/tree/df96187d1b001c66c24d8efd34747501a4283850). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
