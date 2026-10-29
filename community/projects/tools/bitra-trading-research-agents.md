# TRA / bitra (trading research agents where models give opinions and fixed rules price, size and gate every trade, with a Jev provider)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Trading research agents (`bitra` on PyPI, runs as `tra`): language models read the market and give an opinion; the system itself, with no model involved, fetches data, computes every figure, applies your limits, sizes the trade and either records it or sends one order with the stop attached. Every decision and refusal is kept on disk with its reason, and an arena replays policies over a recorded archive. Jev is one of the supported decision providers. Early release.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/BijectiveLabs/bitra) |
| Maintainer | [BijectiveLabs](https://github.com/BijectiveLabs). Independently curated. |
| Format | Python package (PyPI `bitra`) |
| Requirements | Python 3.11+ (uv recommended) and a model provider key (TypeSafe for Jev); a venue account for orders. |
| License | [MIT](https://github.com/BijectiveLabs/bitra/blob/3d49f8db2e039f7450b401554f93e255dd9bf574/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/trading_research_agents/llm/providers/typesafe.py`](https://github.com/BijectiveLabs/bitra/blob/3d49f8db2e039f7450b401554f93e255dd9bf574/src/trading_research_agents/llm/providers/typesafe.py) at the pinned commit. |

## When to use

- Study agent-assisted trading with hard rule gates and full decision records.
- Mismatch: early release; real orders are risky and only the practice-environment path is described as working.

## How it works

`src/trading_research_agents/llm/providers/typesafe.py` posts `{model, state, questions}` to `https://api.typesafe.ai/v1/systemone` and refuses moving aliases such as `jev-latest`, so the Jev version is pinned. Integration evidence: [`src/trading_research_agents/llm/providers/typesafe.py`](https://github.com/BijectiveLabs/bitra/blob/3d49f8db2e039f7450b401554f93e255dd9bf574/src/trading_research_agents/llm/providers/typesafe.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install 'bitra[ccxt,openai,anthropic,google,data]'
tra --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/BijectiveLabs/bitra#readme](https://github.com/BijectiveLabs/bitra#readme)

## Limits and data handling

Market data and prompts go to the chosen model provider. Not financial advice; check every order path on a practice environment first.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 3d49f8db2e03](https://github.com/BijectiveLabs/bitra/tree/3d49f8db2e039f7450b401554f93e255dd9bf574). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
