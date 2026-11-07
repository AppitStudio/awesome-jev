# jev-paper-trader (paper-trade Polymarket/Kalshi with TypeSafe Jev as judge)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Paper-trading harness on real Polymarket and Kalshi markets with a fake $100k bankroll: Claude can research, and TypeSafe Jev judges decisions; no real money or orders.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MojoAI-King/jev-paper-trader) |
| Maintainer | [MojoAI-King](https://github.com/MojoAI-King). Independently curated. |
| Format | Python paper-trading harness (no SPDX license file on the reviewed commit) |
| Requirements | Python and a TypeSafe API key; market data access per README. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`papertrade/jev_client.py`](https://github.com/MojoAI-King/jev-paper-trader/blob/4ea7943ec37201555f67671bd874bc36799a5521/papertrade/jev_client.py) at the pinned commit. |

## When to use

- Simulate prediction-market trading with Jev judgments.
- Keep research and judgment separated (Claude vs Jev).
- Mismatch: no OSI license on the reviewed commit; paper trading only.

## How it works

`papertrade/jev_client.py` POSTs to `https://api.typesafe.ai/v1/systemone` with `jev-latest` using `TYPESAFE_API_KEY` / `TYPESAFE_AI_API_KEY`. Integration evidence: [`papertrade/jev_client.py`](https://github.com/MojoAI-King/jev-paper-trader/blob/4ea7943ec37201555f67671bd874bc36799a5521/papertrade/jev_client.py).

## Get started

Clone, put TYPESAFE_API_KEY in `.env`, and run the papertrade scripts per README.

```sh
git clone https://github.com/MojoAI-King/jev-paper-trader.git && cd jev-paper-trader
export TYPESAFE_API_KEY=...
# follow README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/MojoAI-King/jev-paper-trader/blob/4ea7943ec37201555f67671bd874bc36799a5521/README.md](https://github.com/MojoAI-King/jev-paper-trader/blob/4ea7943ec37201555f67671bd874bc36799a5521/README.md)

## Limits and data handling

No open-source license file on the reviewed commit—do not treat as OSI OSS. Market/question text goes to TypeSafe on your key. No real orders.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 4ea7943ec372](https://github.com/MojoAI-King/jev-paper-trader/tree/4ea7943ec37201555f67671bd874bc36799a5521). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
