# Jev Fighter

[All projects](../README.md) · [Web apps](README.md#web-apps)

Stick-figure fighting game where AI decision models such as Jev 1.13 and chat LLMs fight each other, doubling as a benchmark with deterministic replays, decision logs and an Elo leaderboard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jose-Sabater/jev-fighter) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [jev-fighter.apps.sabater.io](https://jev-fighter.apps.sabater.io) |
| Pricing and access | Hosted demo at jev-fighter.apps.sabater.io; model matches use your Opper key (author estimate $0.001–$0.02 per classifier match); baseline matches need no key. Checked 2026-10-13. |
| Jev evidence | [`adapters/decisions.ts`](https://github.com/Jose-Sabater/jev-fighter/blob/a42042d3de9e1c315db0fd230cfc7740cd8a1a5a/adapters/decisions.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |
| Maintainer | [Jose-Sabater](https://github.com/Jose-Sabater). Independently curated. |
| Format | Web game (TypeScript, Vite) |
| Platform and availability | Web (browser); self-host with Node.js |
| Jev's role | Jev (via Opper) picks each fighter move from the game state; every decision is logged for replay and stats. |
| Requirements | Browser; Opper API key for model matches; Node.js to self-host. |
| License | [MIT](https://github.com/Jose-Sabater/jev-fighter/blob/a42042d3de9e1c315db0fd230cfc7740cd8a1a5a/LICENSE) |

## When to use

- Watch or benchmark how decision models behave in a fast, repeatable game.
- Mismatch: Jev is reached through Opper, not the TypeSafe API directly.

## How it works

A deterministic engine asks each model a typed move question per tick; replays and Elo come from the logged decisions. (Summarized from the upstream [README](https://github.com/Jose-Sabater/jev-fighter/blob/a42042d3de9e1c315db0fd230cfc7740cd8a1a5a/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): play at the hosted site or `npm install` and `npm run dev` after setting `OPPER_API_KEY`.

## Limits and data handling

Game state goes to Opper and its model providers. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit a42042d3de9e](https://github.com/Jose-Sabater/jev-fighter/tree/a42042d3de9e1c315db0fd230cfc7740cd8a1a5a). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
