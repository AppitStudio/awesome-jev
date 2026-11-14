# Jev × ANT SIMULATOR (auto-player for the ANT SIMULATOR stock-market game where Jev sets target positions from the game's local market feed)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Experimental bot for the Steam game ANT SIMULATOR: stock market game. It reads quotes and account state from the game's local HTTP/WebSocket interface, asks Jev (or a built-in momentum rule) for target positions, turns the difference into in-game orders with position and order limits, logs every decision and can show a viewer window with a "JEV OPS" overlay. README is in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yangyuan-zhen/antsim-jev) |
| Maintainer | [yangyuan-zhen](https://github.com/yangyuan-zhen). Independently curated. |
| Format | Bun scripts for a local game API (JavaScript) |
| Requirements | Windows, the ANT SIMULATOR game, Bun, and a TypeSafe or OpenRouter key (or none for the momentum rule). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.mjs`](https://github.com/yangyuan-zhen/antsim-jev/blob/5933d75332f8d28ff251d8f079dbe1a352f6ee8d/jev.mjs) at the pinned commit. |

## When to use

- Watch Jev make repeated typed allocation decisions in a game market.
- Mismatch: real trading; it only places orders in the game and is not investment advice.

## How it works

`jev.mjs` supports TypeSafe (`api.typesafe.ai/v1/systemone`, `jev-latest`, `TYPESAFE_API_KEY`) and OpenRouter (`/api/alpha/decisions`, `typesafe/jev-1.13`); `bot.mjs` uses Jev when a key is present and the momentum rule otherwise. Integration evidence: [`jev.mjs`](https://github.com/yangyuan-zhen/antsim-jev/blob/5933d75332f8d28ff251d8f079dbe1a352f6ee8d/jev.mjs).

## Get started

Copy the env template, add a key, and start in dry-run mode first.

```sh
git clone https://github.com/yangyuan-zhen/antsim-jev && cd antsim-jev
cp .env.example .env    # TYPESAFE_API_KEY=... or OPENROUTER_API_KEY=...
ANTSIM_DRY=1 bun bot.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/yangyuan-zhen/antsim-jev/blob/5933d75332f8d28ff251d8f079dbe1a352f6ee8d/README.md](https://github.com/yangyuan-zhen/antsim-jev/blob/5933d75332f8d28ff251d8f079dbe1a352f6ee8d/README.md)

## Limits and data handling

In-game market and account state is sent to TypeSafe or OpenRouter on your key. Game simulation only; no real brokerage accounts. No license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 5933d75332f8](https://github.com/yangyuan-zhen/antsim-jev/tree/5933d75332f8d28ff251d8f079dbe1a352f6ee8d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
