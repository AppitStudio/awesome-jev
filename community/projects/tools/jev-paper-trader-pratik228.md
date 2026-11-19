# jev-paper-trader by Pratik Mishra (paper market maker for Binance BTCUSDT that measures a Jev decision slot against plain code on recorded data)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Test bench for decision models in market making: code builds the market state from a recorded Binance BTCUSDT tape, a model (Jev or a stand-in) answers six narrow typed questions, code turns the answers into quotes and a risk engine can veto anything. The author's 18-day result is a negative one: every strategy lost money, mostly to fees, and an uninformed model did worse than no model. Paper only: nothing places a live order, and a test enforces that. Includes recording, replay, a read-only dashboard and reports.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Pratik228/jev-paper-trader) |
| Maintainer | [Pratik228](https://github.com/Pratik228). Independently curated. |
| Format | Python package with Make targets and Docker |
| Requirements | Python with the package installed; `TYPESAFE_API_KEY` for live Jev calls (a deterministic stand-in runs without one); Binance's public market data for recording. |
| License | [MIT](https://github.com/Pratik228/jev-paper-trader/blob/28d0ffbf0d29355c95d2f6a2b85b01ab9d42aa9f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_paper/decision/jev_client.py`](https://github.com/Pratik228/jev-paper-trader/blob/28d0ffbf0d29355c95d2f6a2b85b01ab9d42aa9f/src/jev_paper/decision/jev_client.py) at the pinned commit. |

## When to use

- Study whether a decision model adds anything to a market-making loop, with honest negative results to compare against.
- Mismatch: a trading bot; it never trades and reports losses.

## How it works

`src/jev_paper/decision/jev_client.py` makes the live TypeSafe calls (imported lazily) and provides the deterministic stand-in; `config.py` pins the Jev model and the six questions feed the quoting strategy. Integration evidence: [`src/jev_paper/decision/jev_client.py`](https://github.com/Pratik228/jev-paper-trader/blob/28d0ffbf0d29355c95d2f6a2b85b01ab9d42aa9f/src/jev_paper/decision/jev_client.py).

## Get started

Install in a virtualenv, run the synthetic sample tape, then record your own tape and replay it.

```sh
git clone https://github.com/Pratik228/jev-paper-trader && cd jev-paper-trader
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
make sample   # 40-minute synthetic tape
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Pratik228/jev-paper-trader/blob/28d0ffbf0d29355c95d2f6a2b85b01ab9d42aa9f/README.md](https://github.com/Pratik228/jev-paper-trader/blob/28d0ffbf0d29355c95d2f6a2b85b01ab9d42aa9f/README.md)

## Limits and data handling

Paper trading only and not financial advice. The 18-day tape is not redistributed (Binance terms); replays cost CPU time and disk. Results are the author's.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit 28d0ffbf0d29](https://github.com/Pratik228/jev-paper-trader/tree/28d0ffbf0d29355c95d2f6a2b85b01ab9d42aa9f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
