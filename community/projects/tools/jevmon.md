# JevMon (Pokémon Showdown Random Battle bot that blends Jev move weights with Monte Carlo search)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Bot for Gen 9 Random Battle on Pokémon Showdown. Each turn it asks Jev to weigh the legal moves, runs a Monte Carlo tree search over possible opposing teams, blends the two, and lets code veto a few provably self-defeating moves. The README reports a peak of #7 on the public Random Battle ladder, with call counts and fallback rates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/YutaOkkotsu712/JevMon) |
| Maintainer | [YutaOkkotsu712](https://github.com/YutaOkkotsu712). Independently curated. |
| Format | TypeScript bot with a vendored Rust search engine |
| Requirements | Node.js, Rust (for the search engine build), a TypeSafe API key for `BATTLE_MODE=jev`. |
| License | [MIT](https://github.com/YutaOkkotsu712/JevMon/blob/bbf9f838092709ec0dd479ae3d811b5fae55d3f0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisions/JevDecisionProvider.ts`](https://github.com/YutaOkkotsu712/JevMon/blob/bbf9f838092709ec0dd479ae3d811b5fae55d3f0/src/decisions/JevDecisionProvider.ts) at the pinned commit. |

## When to use

- See Jev as a fast per-turn move prior combined with search in a real game.
- Mismatch: needs a Showdown account and your own key; ladder results are the author's report.

## How it works

`src/decisions/JevDecisionProvider.ts` sends the battle state and legal moves to Jev as a typed choice and returns per-move probabilities, which are blended with the search result; per-battle call limits and timeouts are configured in `src/config/env.ts`, and failed calls fall back to a legal move. Integration evidence: [`src/decisions/JevDecisionProvider.ts`](https://github.com/YutaOkkotsu712/JevMon/blob/bbf9f838092709ec0dd479ae3d811b5fae55d3f0/src/decisions/JevDecisionProvider.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp -n .env.example .env   # add TYPESAFE_API_KEY
npm test
npm run build:engine
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Ladder account named in the README: [pokemonshowdown.com/users/thenameisjev](https://pokemonshowdown.com/users/thenameisjev)

## Limits and data handling

Battle state is sent to TypeSafe on every Jev call. Automated play may be subject to Pokémon Showdown rules. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit bbf9f8380927](https://github.com/YutaOkkotsu712/JevMon/tree/bbf9f838092709ec0dd479ae3d811b5fae55d3f0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
