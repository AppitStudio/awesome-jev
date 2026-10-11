# StockSignal

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Terminal dashboard that pulls market data with yfinance and recent news with the Olostep SDK, then asks TypeSafe Jev choice and score questions to show BUY / HOLD / SELL probabilities and market impact for a five-trading-day horizon.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kingabzpro/StocksSignal) |
| Maintainer | [kingabzpro](https://github.com/kingabzpro). Independently curated. |
| Format | Python terminal app |
| Requirements | Python 3.11-3.13, `uv`; Olostep and TypeSafe API keys (demo mode needs none). |
| License | [Apache-2.0](https://github.com/kingabzpro/StocksSignal/blob/bfbcf6efe1acbb01a5d56e529a9480d87718543e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Explore how Jev choice and score questions summarize market data and news.
- Mismatch: Demo/educational signals, not investment advice; needs two paid-capable API keys.

## How it works

Market data and news for each ticker form the state; Jev answers a choice (BUY/HOLD/SELL) and score questions shown in the dashboard. (Summarized from the upstream [README](https://github.com/kingabzpro/StocksSignal/blob/bfbcf6efe1acbb01a5d56e529a9480d87718543e/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Run `uv sync`, add keys to `.env`, then `uv run app` (or `uv run app --demo` without keys).

## Limits and data handling

Ticker data and news text are sent to the TypeSafe API. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-11** (Europe/Sofia) at [commit bfbcf6efe1ac](https://github.com/kingabzpro/StocksSignal/tree/bfbcf6efe1acbb01a5d56e529a9480d87718543e). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
