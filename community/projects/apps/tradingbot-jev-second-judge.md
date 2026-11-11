# Tradingbot (French Telegram trading assistant with Jev as a second judge)

[All projects](../README.md) · [Telegram bots](README.md#telegram-bots)

French-language Telegram bot for Bourse Direct with daily AI briefings, stop-loss/take-profit alerts and a buy gate where Jev gives a typed counter-opinion on each buy thesis and sorts news.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/myopencomm/Tradingbot) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/myopencomm/Tradingbot#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build (MIT); you host the bot and pay any model/TypeSafe usage and broker costs. Checked 2026-11-11. |
| Jev evidence | [`jev.py`](https://github.com/myopencomm/Tradingbot/blob/2818caf9a972b20b4789b43eb2f15ee2132e995f/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [myopencomm](https://github.com/myopencomm). Independently curated. |
| Format | Telegram bot (Python, MIT) |
| Platform and availability | Telegram (self-hosted bot; source build) |
| Jev's role | Jev gives a typed counter-opinion on each buy thesis and classifies news sentiment for alerts. |
| Requirements | Python, a Telegram bot token, Groq/Gemini keys, and `TYPESAFE_API_KEY` for the Jev judge. |
| License | [MIT](https://github.com/myopencomm/Tradingbot/blob/2818caf9a972b20b4789b43eb2f15ee2132e995f/LICENSE) |

## When to use

- Add a typed second opinion to an LLM trading workflow.
- Sort position news into bad-news alerts.
- Mismatch: built for Bourse Direct (France); not financial advice, and a connected autonomous mode exists.

## How it works

`jev.py` calls `/v1/systemone` for thesis vetoes, sentiment and news sorting; `thesis_gate.py` requires a thesis plus two evidence points and adds the Jev counter-opinion before a buy passes. Integration evidence: [`jev.py`](https://github.com/myopencomm/Tradingbot/blob/2818caf9a972b20b4789b43eb2f15ee2132e995f/jev.py).

## Get started

Copy the example env, add your Telegram and model keys and the TypeSafe key, then run `main.py`.

```sh
git clone https://github.com/myopencomm/Tradingbot.git && cd Tradingbot
pip install -r requirements.txt
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/myopencomm/Tradingbot/blob/2818caf9a972b20b4789b43eb2f15ee2132e995f/README.md](https://github.com/myopencomm/Tradingbot/blob/2818caf9a972b20b4789b43eb2f15ee2132e995f/README.md)

## Limits and data handling

Research text and news go to TypeSafe and the LLM providers on your keys; trading decisions are your responsibility.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 2818caf9a972](https://github.com/myopencomm/Tradingbot/tree/2818caf9a972b20b4789b43eb2f15ee2132e995f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
