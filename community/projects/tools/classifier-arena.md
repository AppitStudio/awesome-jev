# Classifier Arena

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Three small browser games (a real-time fighter, a spam and smishing lane game, and a reverse-dictionary clue game) where Jev and OpenAI Decisions play head to head on one shared classifier core, with every match logged and replayable.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Malleable-ai/classifier-arena) |
| Maintainer | [Malleable-ai](https://github.com/Malleable-ai). Independently curated. |
| Format | TypeScript browser games and match runner (Node 24, pnpm) |
| Requirements | Node 24, pnpm 10; TypeSafe and OpenAI keys for live matches. |
| License | [MIT](https://github.com/Malleable-ai/classifier-arena/blob/081b28dd14fac05dde184f68d7450f79bccba14f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/core/classifier/formats/systemone.ts`](https://github.com/Malleable-ai/classifier-arena/blob/081b28dd14fac05dde184f68d7450f79bccba14f/src/core/classifier/formats/systemone.ts) at the pinned commit. |

## When to use

- Compare two decision APIs under identical state, prompt, options and timing.
- Replay recorded matches from their logs.
- Mismatch: a game benchmark; win rates do not transfer directly to business classification tasks.

## How it works

A game-agnostic classifier core sends the same state and option list to each provider, using the System One request format for Jev (`jev-latest`) and the OpenAI Decisions format for `gpt-6-luna`; real-time games never wait for answers, so speed matters. Integration evidence: [`src/core/classifier/formats/systemone.ts`](https://github.com/Malleable-ai/classifier-arena/blob/081b28dd14fac05dde184f68d7450f79bccba14f/src/core/classifier/formats/systemone.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install
pnpm dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results table with Wilson intervals in the README.
- Game rules under `docs/architecture/`.

## Limits and data handling

Game state goes to TypeSafe and OpenAI on your keys during live matches; runs without keys use built-in baselines.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 081b28dd14fa](https://github.com/Malleable-ai/classifier-arena/tree/081b28dd14fac05dde184f68d7450f79bccba14f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
