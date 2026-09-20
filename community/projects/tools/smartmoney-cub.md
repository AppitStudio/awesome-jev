# SmartMoney-Cub

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first, read-only trading journal and review harness: optional TypeSafe Jev typed judgments over structured review fields, plus a frozen `finance-jev-v1` offline benchmark. No orders, no broker connection, no financial advice.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/myc0576/SmartMoney-Cub) |
| Maintainer | [myc0576](https://github.com/myc0576). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **smartmoney-cub-harness 1.0.0** (`smcub` CLI; optional GUI/npm surfaces upstream). |
| Requirements | Python ≥ 3.10; `pip install -e ".[dev]"` for the harness. Live Jev needs `TYPESAFE_API_KEY` (direct) or OpenRouter credentials for the optional OpenRouter→Jev backend. |
| License | [MIT](https://github.com/myc0576/SmartMoney-Cub/blob/d93cf493853dd79b337215909e6ac60bec22a799/LICENSE). |

## When to use

Use it to capture offline run envelopes, build evidence packs, replay reviews, and optionally ask Jev `noul` / `choice` / `score` questions while arithmetic and temporal gates stay in Python. Prefer [Jev Trader](jev-trader.md) only if you want an execution-oriented market experiment (that project can place orders when configured); SmartMoney-Cub is explicitly read-only.

## How it works

[`src/smartmoney_cub_harness/jev/direct.py`](https://github.com/myc0576/SmartMoney-Cub/blob/d93cf493853dd79b337215909e6ac60bec22a799/src/smartmoney_cub_harness/jev/direct.py) posts to `https://api.typesafe.ai` (default model `jev-latest`) for typed review judgments. An OpenRouter backend is also available. Deterministic code owns dates, arithmetic, and `available_at <= decision_time` checks. Upstream ships `finance-jev-v1` (240 frozen cases); published accuracy figures on that toy suite are empirical and do not imply production market performance.

## Get started

```sh
git clone https://github.com/myc0576/SmartMoney-Cub.git
cd SmartMoney-Cub
git checkout d93cf493853dd79b337215909e6ac60bec22a799
python -m pip install -e ".[dev]"
smcub doctor
smcub capture-run --mode after-close --preset toy --sandbox --decision-time "2026-06-01T15:31:00+08:00"
```

Toy capture/replay needs no TypeSafe key. Live Jev review is opt-in and billable. This listing did not call TypeSafe.

## Examples and demos

- Toy strategy example under [`examples/toy_strategy/`](https://github.com/myc0576/SmartMoney-Cub/tree/d93cf493853dd79b337215909e6ac60bec22a799/examples/toy_strategy).
- Benchmark pack under [`benchmarks/finance-jev-v1/`](https://github.com/myc0576/SmartMoney-Cub/tree/d93cf493853dd79b337215909e6ac60bec22a799/benchmarks/finance-jev-v1) and published run assets under `assets/benchmark/`.
- Safety contract docs under [`docs/safety.md`](https://github.com/myc0576/SmartMoney-Cub/blob/d93cf493853dd79b337215909e6ac60bec22a799/docs/safety.md).

## Limits and data handling

Core control plane is offline and read-only over markets/execution; journal writes stay local. Opt-in Jev review sends redacted structured fields to TypeSafe or OpenRouter. Upstream states no embedded trading agent and no automatic order placement. Do not treat benchmark scores as investment advice.

## Review and maintenance

Reviewed on **2026-09-20** at [commit d93cf49](https://github.com/myc0576/SmartMoney-Cub/tree/d93cf493853dd79b337215909e6ac60bec22a799): **1.0.0**, MIT. AI-assisted source review of README, `jev/direct.py`, and package metadata. Offline `smcub` toy path and live Jev were not executed on the review host.

Related: [Jev Trader](jev-trader.md), [JevScope](jevscope.md).
