# Jev Trader by Errr0rr404 (local trading desk where Jev votes and code owns sizing and exits, simulate by default)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local CLI and web desk that uses Robinhood's Agentic MCP for quotes and orders, asks Jev to vote on entries, and leaves sizing, stops and scale-outs to code. Simulates a $100 paper book by default; live orders need an explicit armed mode.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Errr0rr404/jev-trader) |
| Maintainer | [Errr0rr404](https://github.com/Errr0rr404). Independently curated. |
| Format | Node.js / TypeScript CLI + local web desk |
| Requirements | Node.js; a TypeSafe key; a Robinhood account for live data and orders. |
| License | [MIT](https://github.com/Errr0rr404/jev-trader/blob/cf91be0b7439694b97b7185170ec72e590aa2329/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/Errr0rr404/jev-trader/blob/cf91be0b7439694b97b7185170ec72e590aa2329/src/jev.ts) at the pinned commit. |

## When to use

- Experiment with a Jev vote inside code-owned trading rails.
- Mismatch: not financial advice; live trading is opt-in and risky.

## How it works

`src/jev.ts` builds a market packet per trading mode (configured in `config/jev.yaml`) and asks Jev to vote; guardrails in `src/guardrails.ts` and exits in `src/exits.ts` stay in code. Integration evidence: [`src/jev.ts`](https://github.com/Errr0rr404/jev-trader/blob/cf91be0b7439694b97b7185170ec72e590aa2329/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.example .env   # TYPESAFE_AI_API_KEY
npx tsx src/cli.ts watch AAPL --trading-mode swing --once --force
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/Errr0rr404/jev-trader#readme](https://github.com/Errr0rr404/jev-trader#readme)

## Limits and data handling

Not financial advice. Market data packets go to TypeSafe. Live orders can lose money. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit cf91be0b7439](https://github.com/Errr0rr404/jev-trader/tree/cf91be0b7439694b97b7185170ec72e590aa2329). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
