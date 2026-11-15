# Decision models in games (harness pitting Jev, Drex and Clef against Claude, GPT and bots in poker, Catan, backgammon and Pokémon)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Every seat gets the same game-state text and list of legal actions; decision models pick an action with probabilities, reasoning LLMs pick with a one-line reason. Covers heads-up no-limit hold'em (seats swapped every deal to cancel card luck), Catan via Catanatron, backgammon and Pokémon random battles via a local Showdown server, with per-decision logs, spend caps and replays. The README calls it a quick look, not a benchmark, and flags small samples.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Alyasska/decision-models-in-games) |
| Maintainer | [Alyasska](https://github.com/Alyasska). Independently curated. |
| Format | Python scripts and logs (GPL-3.0) |
| Requirements | Python 3, an `OPENROUTER_API_KEY` (Jev, Drex, Clef and GPT); Claude seats use your local Claude Code CLI; Pokémon needs a local Showdown server. |
| License | [GPL-3.0](https://github.com/Alyasska/decision-models-in-games/blob/2336449cdc110ada60b137e7a1831f055c85000f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`catan/drex_player.py`](https://github.com/Alyasska/decision-models-in-games/blob/2336449cdc110ada60b137e7a1831f055c85000f/catan/drex_player.py) at the pinned commit. |

## When to use

- Compare how Jev and reasoning LLMs choose among legal moves in classic games.
- Mismatch: strength rankings; samples are small by design.

## How it works

`catan/drex_player.py` posts decision requests to OpenRouter's `https://openrouter.ai/api/alpha/decisions`; `catan/play.py` maps the `jev` seat to `typesafe/jev-1.14` (and `jev-1.13`). Integration evidence: [`catan/drex_player.py`](https://github.com/Alyasska/decision-models-in-games/blob/2336449cdc110ada60b137e7a1831f055c85000f/catan/drex_player.py).

## Get started

Install requirements, then run a match with a spend cap.

```sh
git clone https://github.com/Alyasska/decision-models-in-games && cd decision-models-in-games
python -m venv .venv && . .venv/bin/activate && pip install -r requirements.txt
export OPENROUTER_API_KEY=...
cd games && python poker.py --a gpt-terra --b jev --deals 25 --shuffle --max-usd 0.25
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/Alyasska/decision-models-in-games/blob/2336449cdc110ada60b137e7a1831f055c85000f/README.md](https://github.com/Alyasska/decision-models-in-games/blob/2336449cdc110ada60b137e7a1831f055c85000f/README.md)

## Limits and data handling

Game states go to OpenRouter (and Anthropic via your Claude Code login) on your keys. Results are the maintainer's small runs.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 2336449cdc11](https://github.com/Alyasska/decision-models-in-games/tree/2336449cdc110ada60b137e7a1831f055c85000f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
