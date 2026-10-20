# jev-poke (Jev plays Pokémon Showdown)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Node.js bot (README in Chinese) that plays Pokémon Showdown VGC doubles: at each team preview, turn and forced switch it sends structured questions about the full battle state to Jev through OpenRouter's Decisions API, with local fallbacks and an optional advisor model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fangzipei/let-jev-play-pokemon) |
| Maintainer | [fangzipei](https://github.com/fangzipei). Independently curated. |
| Format | Node.js bot (TypeScript) for the Pokémon Showdown WebSocket protocol |
| Requirements | Node.js 20+ and an OpenRouter key (`OPENROUTER_API_KEY`); `JEV_MOCK=1` runs local heuristics without a key. |
| License | [MIT](https://github.com/fangzipei/let-jev-play-pokemon/blob/9dd680aac460fe37e2907432664f1534cf994e1a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/fangzipei/let-jev-play-pokemon/blob/9dd680aac460fe37e2907432664f1534cf994e1a/src/jev/client.ts) at the pinned commit. |

## When to use

- Watch a decision model play a real-time competitive game against people.
- Study how to pack game state and legal actions into one batch of choice and noul questions.
- Mismatch: plays on the public server and tells opponents it is an AI; follow Showdown's rules for bots.

## How it works

The bot reads the battle over WebSocket, adds context (objective state, tactical notes, opponent priors from daily usage snapshots) and `src/jev/client.ts` posts the questions to `https://openrouter.ai/api/alpha/decisions` with model `~typesafe/jev-latest`. Timeouts, missing answers or illegal moves fall back to local heuristics; a separate chat model answers opponents' messages. Integration evidence: [`src/jev/client.ts`](https://github.com/fangzipei/let-jev-play-pokemon/blob/9dd680aac460fe37e2907432664f1534cf994e1a/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.example .env   # OPENROUTER_API_KEY=
# JEV_MOCK=1 for a keyless smoke test; see README for play commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README configuration table (context levels 1 to 3, advisor, decision budget)
- tests/jev-client.test.ts

## Limits and data handling

Battle state goes to OpenRouter and TypeSafe; opponent chat goes to a separate chat model. Not affiliated with Pokémon Showdown.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 9dd680aac460](https://github.com/fangzipei/let-jev-play-pokemon/tree/9dd680aac460fe37e2907432664f1534cf994e1a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
