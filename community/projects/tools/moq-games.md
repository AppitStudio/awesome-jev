# moq-games (tower-defense game with an optional TypeSafe Jev bot over MoQ)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Standalone TypeScript/three.js tower-defense game that plays fully locally; an optional Python bot can drive defenders through MoQ transport using TypeSafe Jev (`jev-latest` / `TYPESAFE_API_KEY`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yuki-uchida/moq-games) |
| Maintainer | [yuki-uchida](https://github.com/yuki-uchida). Independently curated. |
| Format | TypeScript browser game + optional Python Jev bot (MIT) |
| Requirements | A browser to play; optional Python + MoQ + TypeSafe key for the networked Jev bot. |
| License | [MIT](https://github.com/yuki-uchida/moq-games/blob/bdfaaac9f5817afd5f77194563292a2e43c46ecc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`examples/games/tower_diffence_with_jev/bot/.env.example`](https://github.com/yuki-uchida/moq-games/blob/bdfaaac9f5817afd5f77194563292a2e43c46ecc/examples/games/tower_diffence_with_jev/bot/.env.example) at the pinned commit. |

## When to use

- Play the browser tower-defense game offline.
- Optionally attach a Jev-driven MoQ bot.
- Mismatch: core gameplay does not require Jev; Jev is the optional bot path.

## How it works

The optional bot reads `JEV_MODEL=jev-latest` (or `TYPESAFE_API_KEY`) from `.env` and calls TypeSafe System One over MoQ transport for defender choices. Integration evidence: [`examples/games/tower_diffence_with_jev/bot/.env.example`](https://github.com/yuki-uchida/moq-games/blob/bdfaaac9f5817afd5f77194563292a2e43c46ecc/examples/games/tower_diffence_with_jev/bot/.env.example).

## Get started

Open the GitHub Pages demo, or clone and run locally; for the bot, copy the example env and set a TypeSafe key.

```sh
git clone https://github.com/yuki-uchida/moq-games.git && cd moq-games
# play locally per README
# optional bot:
cp examples/games/tower_diffence_with_jev/bot/.env.example examples/games/tower_diffence_with_jev/bot/.env
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/yuki-uchida/moq-games/blob/bdfaaac9f5817afd5f77194563292a2e43c46ecc/README.md](https://github.com/yuki-uchida/moq-games/blob/bdfaaac9f5817afd5f77194563292a2e43c46ecc/README.md)

## Limits and data handling

When the bot is enabled, game-state questions are sent to TypeSafe on your key. Local play needs no network AI.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit bdfaaac9f581](https://github.com/yuki-uchida/moq-games/tree/bdfaaac9f5817afd5f77194563292a2e43c46ecc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
