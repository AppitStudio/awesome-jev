# Model vs Market

[All projects](../README.md) · [Web apps](README.md#web-apps)

Web app where three decision models — OpenAI Decisions, TypeSafe Jev and Cloudflare Clef — read recent news (never the odds), put a probability on Polymarket and Kalshi questions, and are compared with live market prices, with a replay of how each model changed its mind article by article.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yorkeccak/model-vs-market) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [model-vs-market.vercel.app](https://model-vs-market.vercel.app) (live demo). |
| Pricing and access | Live demo is free to browse; self-hosting needs your own Valyu, OpenAI, Cloudflare and TypeSafe (or Vercel AI Gateway) keys. Checked 2026-10-08. |
| Jev evidence | [`src/lib/models.ts`](https://github.com/yorkeccak/model-vs-market/blob/5fb863646e96a0d5b0c944c81626957e346bf684/src/lib/models.ts) and [`src/app/api/analyze/route.ts`](https://github.com/yorkeccak/model-vs-market/blob/5fb863646e96a0d5b0c944c81626957e346bf684/src/app/api/analyze/route.ts) call Jev (TypeSafe API directly when `TYPESAFE_API_KEY` is set, otherwise Vercel AI Gateway). Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [yorkeccak](https://github.com/yorkeccak). Independently curated. |
| Format | Next.js web app (Vercel) |
| Platform and availability | Any modern browser (hosted demo); self-host on Vercel or Node. |
| Jev's role | One of three models assigning a probability to each market question from retrieved news. |
| Requirements | Self-host: Node + pnpm; keys for Valyu search, OpenAI, Cloudflare Workers AI and Jev. |
| License | [MIT](https://github.com/yorkeccak/model-vs-market/blob/5fb863646e96a0d5b0c944c81626957e346bf684/LICENSE). |

## When to use

- Compare decision models on questions with an external scoreboard (market prices).
- See per-article belief updates rather than a single number.
- Mismatch: not trading advice; markets and models can both be wrong.

## How it works

The app searches news with Valyu, sends the same evidence to each model as a typed probability question, stores results and renders them beside live Polymarket/Kalshi prices.

## Get started

Self-host (README *Run it*):

```sh
git clone https://github.com/yorkeccak/model-vs-market.git && cd model-vs-market
pnpm install
cp .env.example .env.local   # add your keys
pnpm dev
```

Self-hosting bills each provider key you configure.

## Examples and demos

- Live: [model-vs-market.vercel.app](https://model-vs-market.vercel.app).

## Limits and data handling

News evidence and questions go to OpenAI, Cloudflare and TypeSafe. Not run on the review host; the live demo was not exercised beyond reachability.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 5fb863646e96](https://github.com/yorkeccak/model-vs-market/tree/5fb863646e96a0d5b0c944c81626957e346bf684). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
