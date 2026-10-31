# TradingAgents (multi-agent LLM trading research framework with optional Jev screening of social posts)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Multi-agent financial trading research framework (analyst, researcher, trader and risk-manager agents). Since v0.5.1 the Sentiment Analyst can screen StockTwits and Reddit posts with Jev before reading them, dropping posts that are not about the company and counting stances only when Jev is not genuinely uncertain.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TauricResearch/TradingAgents) |
| Maintainer | [TauricResearch](https://github.com/TauricResearch). Independently curated. |
| Format | Python package / CLI (also Docker) |
| Requirements | Python 3.13; an LLM provider key; `TYPESAFE_API_KEY` to turn on Jev post screening (optional). |
| License | [Apache-2.0](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tradingagents/agents/post_screen.py`](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tradingagents/agents/post_screen.py) at the pinned commit. |

## When to use

- Filter noisy social sentiment before it reaches an LLM analyst.
- Mismatch: Jev is an optional pre-filter; the trading analysis is LLM-driven research, not financial advice.

## How it works

`tradingagents/agents/post_screen.py` sends each post to TypeSafe (`jev-latest` by default, configurable via `TYPESAFE_DEFAULT_MODEL` / `TYPESAFE_BASE_URL`, including OpenRouter) with relevance and stance questions; uncertain stances are discarded in code. Integration evidence: [`tradingagents/agents/post_screen.py`](https://github.com/TauricResearch/TradingAgents/blob/c4544913a14ed3df5f1ed7b9e8483270ce20682a/tradingagents/agents/post_screen.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/TauricResearch/TradingAgents.git && cd TradingAgents
pip install .
export TYPESAFE_API_KEY=...   # optional Jev social-post screening
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Changelog entry for Jev screening (v0.5.1): [github.com/TauricResearch/TradingAgents/blob/main/CHANGELOG.md](https://github.com/TauricResearch/TradingAgents/blob/main/CHANGELOG.md)

## Limits and data handling

Social posts and ticker context are sent to TypeSafe when the key is set. Research framework; the README disclaims financial advice. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit c4544913a14e](https://github.com/TauricResearch/TradingAgents/tree/c4544913a14ed3df5f1ed7b9e8483270ce20682a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
