# Jev Plays Snake (switty42) (terminal Snake played from outside through tmux, with Jev choosing every move in real time)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Terminal Snake game and a bot that only reads the screen through tmux and presses arrow keys: each frame becomes a text grid sent to Jev with the rules and the three legal moves, and answers that arrive after the snake has moved are dropped. Over a logged 100-game run the author reports an average score of 9.3 (best 27), a 125 ms median response and $1.10 total cost, against a path-finding player that passed 689.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/switty42/Jev_Plays_Snake) |
| Maintainer | [switty42](https://github.com/switty42). Independently curated. |
| Format | Python game and bot scripts, game logs and a PDF presentation (no license file) |
| Requirements | Python 3, tmux, and a TypeSafe key (`TYPESAFE_API_KEY` or a key file). |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`Source/snake_bot.py`](https://github.com/switty42/Jev_Plays_Snake/blob/0a3a3cca18d469a3dc042c28c2900022fa731bf1/Source/snake_bot.py) at the pinned commit. |

## When to use

- See how a decision model copes with a real-time game loop and late answers.
- Mismatch: a strong Snake player; the built-in path-finder far outscores Jev.

## How it works

`Source/snake_bot.py` posts each board to `api.typesafe.ai/v1/systemone`, waits at most 1 second per call, and stops on out-of-credit, rejected-key or repeated errors. Every move is logged as JSONL with the board, Jev's choice, confidence and probabilities, latency, tokens and cost. Integration evidence: [`Source/snake_bot.py`](https://github.com/switty42/Jev_Plays_Snake/blob/0a3a3cca18d469a3dc042c28c2900022fa731bf1/Source/snake_bot.py).

## Get started

Export your key and start the bot, which opens tmux with the game and live stats.

```sh
git clone https://github.com/switty42/Jev_Plays_Snake && cd Jev_Plays_Snake/Source
export TYPESAFE_API_KEY=...
./snake_bot.py --games 5
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/switty42/Jev_Plays_Snake/blob/0a3a3cca18d469a3dc042c28c2900022fa731bf1/ReadMe.md](https://github.com/switty42/Jev_Plays_Snake/blob/0a3a3cca18d469a3dc042c28c2900022fa731bf1/ReadMe.md)
- Presentation: [github.com/switty42/Jev_Plays_Snake/blob/0a3a3cca18d469a3dc042c28c2900022fa731bf1/Presentations/Jev_Plays_Snake_V1_111226.pdf](https://github.com/switty42/Jev_Plays_Snake/blob/0a3a3cca18d469a3dc042c28c2900022fa731bf1/Presentations/Jev_Plays_Snake_V1_111226.pdf)

## Limits and data handling

Board text goes to TypeSafe on your key. Logs are written locally; `Source/jev_key.txt` in the repo is a placeholder, so keep your real key out of it if you commit.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 0a3a3cca18d4](https://github.com/switty42/Jev_Plays_Snake/tree/0a3a3cca18d469a3dc042c28c2900022fa731bf1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
