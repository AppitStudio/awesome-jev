# snake-ai (Snake learning lab)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Hands-on lab and nine-lesson course where neural networks learn Snake with a genetic algorithm or DQN, plus an untrained third player where Jev picks each move from a text description of what the snake senses.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/markmysler/snake-ai) |
| Maintainer | [markmysler](https://github.com/markmysler). Independently curated. |
| Format | Python lab with web dashboard (PyTorch, numpy); live read-only demo |
| Requirements | Python 3.10+ (or Docker); `TOKENROUTER_API_KEY` only for the Jev player. |
| License | [MIT](https://github.com/markmysler/snake-ai/blob/78688db1722b42956842e08e1a97d243c195b018/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev.py`](https://github.com/markmysler/snake-ai/blob/78688db1722b42956842e08e1a97d243c195b018/jev.py) at the pinned commit. |

## When to use

- Learn reinforcement learning and evolution by changing what a snake sees and how it is rewarded.
- Compare a prompted decision model against trained agents on the same fixed games.
- Mismatch: the Jev player goes through TokenRouter's decisions API, not TypeSafe directly.

## How it works

`jev.py` turns each board into a text description, batches many boards into one decisions request (default model `typesafe/jev-1.13`) and plays the chosen move; GA and DQN runs train locally. Integration evidence: [`jev.py`](https://github.com/markmysler/snake-ai/blob/78688db1722b42956842e08e1a97d243c195b018/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/markmysler/snake-ai.git && cd snake-ai
pip install torch --index-url https://download.pytorch.org/whl/cpu --extra-index-url https://pypi.org/simple
pip install -r requirements.txt
python run_all.py --dashboard-only
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live demo: [markmysler.github.io/snake-ai/](https://markmysler.github.io/snake-ai/)
- Video walkthrough: [youtu.be/1bu1y4cJJmA](https://youtu.be/1bu1y4cJJmA)

## Limits and data handling

The Jev player is optional and paid per move through TokenRouter. Training runs locally.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 78688db1722b](https://github.com/markmysler/snake-ai/tree/78688db1722b42956842e08e1a97d243c195b018). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
