# Jev Mario by imink (Super Mario Bros played by Jev decisions, with a full-campaign replay site)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Super Mario Bros in a real NES emulator where structured game state goes to a Jev Choice that picks the controller input; a browser replay site plays back all 32 stages and 6,275 recorded decisions with their answers, without calling a model; bring your own legally obtained ROM.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/imink/local-jev-mario) |
| Maintainer | [imink](https://github.com/imink). Independently curated. |
| Format | Node.js app with browser replay site |
| Requirements | Node.js 24+, pnpm 9.3+ and a lawfully obtained SMB1 `.nes` file; a TypeSafe API key for live play. |
| License | [MIT](https://github.com/imink/local-jev-mario/blob/0daa2a0d0dcda88de2b250963b9ff3691a00a319/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/imink1029/status/2114727103895904423)). |
| Jev evidence | [`game.mjs`](https://github.com/imink/local-jev-mario/blob/0daa2a0d0dcda88de2b250963b9ff3691a00a319/game.mjs) at the pinned commit. |

## When to use

- Watch or step through a complete decision-model playthrough.
- Use the state-to-Choice loop as a template for game agents.
- Mismatch: no ROM is included; distinct from the separately listed typesafe-mario.

## How it works

`game.mjs` turns emulator state into a Choice over controller actions and only accepts `https://api.typesafe.ai` for official Jev; `local-jev.mjs` provides a local `/v1/systemone` stand-in for isolated replay tests. Integration evidence: [`game.mjs`](https://github.com/imink/local-jev-mario/blob/0daa2a0d0dcda88de2b250963b9ff3691a00a319/game.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install --frozen-lockfile
# see the README for live play with TYPESAFE_API_KEY and for the replay build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live replay: [jev-mario.zoink.site](https://jev-mario.zoink.site)
- README: [github.com/imink/local-jev-mario#readme](https://github.com/imink/local-jev-mario#readme)

## Limits and data handling

Live play sends game state to TypeSafe; the replay site calls no model. The MIT LICENSE names Bytedance, Inc. as copyright holder. Discovered on X from the creator's post.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 0daa2a0d0dcd](https://github.com/imink/local-jev-mario/tree/0daa2a0d0dcda88de2b250963b9ff3691a00a319). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
