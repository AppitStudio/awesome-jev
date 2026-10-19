# Jev Cards

[All projects](../README.md) · [Web apps](README.md#web-apps)

Visual quiz game where you race Jev, TypeSafe's vision decision model, on the same picture cards: tap the right thing, pick the answer, with Sprint, Versus, Streak and live multiplayer modes and server-checked leaderboards.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jose-Sabater/jevcards) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://jev-cards.apps.sabater.io) |
| Pricing and access | Free to play on the hosted site (checked 2026-10-19). Self-hosting is free source; you pay for your own Jev calls and hosting. |
| Jev evidence | [`server/jev.ts`](https://github.com/Jose-Sabater/jevcards/blob/1c185ce583bf9969fe80f8b985e35cf70991ae7a/server/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Jose-Sabater](https://github.com/Jose-Sabater). Independently curated. |
| Format | Web app (TypeScript, Node server, Vite) |
| Platform and availability | Web (hosted site; self-host with Node or the included Dockerfile). |
| Jev's role | Jev answers each card live from its picture, as a `choice` with probabilities or a `box` for tap-the-place cards, and its answers and times become your opponent's score. |
| Requirements | Play in a browser; self-hosting needs Node.js and `TYPESAFE_API_KEY`. |
| License | [AGPL-3.0 (code); CC BY 4.0 (cards)](https://github.com/Jose-Sabater/jevcards/blob/1c185ce583bf9969fe80f8b985e35cf70991ae7a/LICENSE) |

## When to use

- Want a fun, visible demo of how fast and accurate a vision decision model is.
- Play live matches with friends against Jev.
- Mismatch: game, not a benchmark; card set is fixed by the author.

## How it works

Each card is an SVG picture plus one typed question. `server/jev.ts` asks Jev with the picture, routing through the Opper gateway when configured or straight to TypeSafe. Options go to Jev under neutral names in random order, the server marks answers and signs Jev's results, and `/how` shows the exact request. Integration evidence: [`server/jev.ts`](https://github.com/Jose-Sabater/jevcards/blob/1c185ce583bf9969fe80f8b985e35cf70991ae7a/server/jev.ts).

## Get started

From the upstream README: play at the hosted site, or render the deck and run the dev server locally.

```sh
npm install
npm run deck
npm run dev   # http://localhost:5173
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [jev-cards.apps.sabater.io](https://jev-cards.apps.sabater.io)
- `npm run bench` (asks Jev every card)

## Limits and data handling

Card pictures and questions go to TypeSafe (or Opper) when Jev plays. AGPL applies if you host a modified version.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 1c185ce583bf](https://github.com/Jose-Sabater/jevcards/tree/1c185ce583bf9969fe80f8b985e35cf70991ae7a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
