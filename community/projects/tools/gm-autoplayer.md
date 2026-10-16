# gm-autoplayer

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Agent that plays browser games such as slither.io from screenshots through the Playwright MCP server; pick an LLM brain, a Jev brain that answers quick typed questions about each frame (danger, nearest food) for game rules to turn into moves, or a hybrid with an LLM strategist.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sugeesh/gm-autoplayer) |
| Maintainer | [sugeesh](https://github.com/sugeesh). Independently curated. |
| Format | Python project (uv) driving Playwright MCP |
| Requirements | Python 3.12/3.13 via uv, Node.js for Playwright MCP, `TYPESAFE_API_KEY` (and `OPENAI_API_KEY` for the LLM or hybrid brain). |
| License | [MIT](https://github.com/sugeesh/gm-autoplayer/blob/69fee7da45b7caf521d79ec65a1ae539b848ff14/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`game_agent/brains/jev.py`](https://github.com/sugeesh/gm-autoplayer/blob/69fee7da45b7caf521d79ec65a1ae539b848ff14/game_agent/brains/jev.py) at the pinned commit. |

## When to use

- Compare an LLM agent with a fast Jev reflex loop on the same live game.
- Mismatch: a game-playing experiment; every move comes from the model, with no hidden in-page bot.

## How it works

The Jev brain sends each screenshot with typed Choice, Score, Noul and Box questions through the TypeSafe Python SDK; deterministic game rules turn the answers into mouse or key actions, while the hybrid mode lets an LLM set a plan every few seconds. Integration evidence: [`game_agent/brains/jev.py`](https://github.com/sugeesh/gm-autoplayer/blob/69fee7da45b7caf521d79ec65a1ae539b848ff14/game_agent/brains/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/sugeesh/gm-autoplayer.git && cd gm-autoplayer
uv sync
cp .env.example .env   # set TYPESAFE_API_KEY (and OPENAI_API_KEY for llm/hybrid)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Brain modes and setup steps in the README.

## Limits and data handling

Screenshots go to TypeSafe (and OpenAI for LLM modes) on your key.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 69fee7da45b7](https://github.com/sugeesh/gm-autoplayer/tree/69fee7da45b7caf521d79ec65a1ae539b848ff14). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
