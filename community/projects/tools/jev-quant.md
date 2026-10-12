# jev-quant

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Early-stage C++ paper-trading system that asks Jev (via OpenRouter Decisions, model `typesafe/jev-1.13`) for trading decisions, with SimNow/CTP simulated futures, Binance and a local simex venue adapter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/itsadrianxv/jev-quant) |
| Maintainer | [itsadrianxv](https://github.com/itsadrianxv). Independently curated. |
| Format | C++20 application (CMake/Ninja) |
| Requirements | C++20 compiler, CMake 3.24+, Ninja, libcurl, nlohmann-json; an OpenRouter API key. |
| License | [MIT](https://github.com/itsadrianxv/jev-quant/blob/c3809a2feabbc803c07e924ffff0d97862e08465/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Study how a low-latency decision model can sit inside a C++ trading loop.
- Paper-trade SHFE futures via SimNow or a local simex venue.
- Mismatch: Maintainer: "very, very early … expect bugs". Paper trading only; not financial advice.

## How it works

A Jev HTTP client posts market state to OpenRouter's decisions endpoint; contract tests use a mock Jev server. Jev integration: [`src/trading/strategy/jev_http_client.h`](https://github.com/itsadrianxv/jev-quant/blob/c3809a2feabbc803c07e924ffff0d97862e08465/src/trading/strategy/jev_http_client.h). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
cmake -S . -B build -G Ninja -DCMAKE_BUILD_TYPE=Release -DJEV_ENABLE_SIMEX=OFF
cmake --build build --parallel
cp .env.example .env   # set your OpenRouter key
./build/jev_trading
```

## Limits and data handling

Market state goes to OpenRouter/TypeSafe; OpenRouter usage is billed. Not built or run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit c3809a2feabb](https://github.com/itsadrianxv/jev-quant/tree/c3809a2feabbc803c07e924ffff0d97862e08465). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
