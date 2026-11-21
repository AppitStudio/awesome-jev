# chat-reading-bandit by Giovanna Fernandes (does a store-offer bandit earn more when Jev reads the shopper's chat?)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

A reproducible simulation study: a logistic Thompson-sampling bandit picks no offer, 10% off or free shipping for synthetic shoppers, with and without three readings Jev (`jev-1.14.0`) takes from LLM-written chats. The repo reports profit uplift over 30 paired replications, compares Claude Haiku/Opus and embeddings as readers, and includes every chat, reading and run.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gioamorim80/chat-reading-bandit) |
| Maintainer | [gioamorim80](https://github.com/gioamorim80). Independently curated. |
| Format | Python research repo (scripts + data) |
| Requirements | Python 3.11+ with uv or pip. Regenerating the results needs no key; re-reading chats needs TypeSafe (and Anthropic for the comparison readers). |
| License | [MIT](https://github.com/gioamorim80/chat-reading-bandit/blob/11d1fb8a8d0d2c296e19df30969ffadd34f2596c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/03_read_chats_with_jev.py`](https://github.com/gioamorim80/chat-reading-bandit/blob/11d1fb8a8d0d2c296e19df30969ffadd34f2596c/scripts/03_read_chats_with_jev.py) at the pinned commit. |

## When to use

- Look at a careful, reproducible example of using Jev readings as features for a contextual bandit.
- Mismatch: evidence about real shoppers; the shoppers are synthetic, and the gain depends on how often chats reveal the shopper's reason.

## How it works

`scripts/03_read_chats_with_jev.py` sends each chat to Jev with typed questions (is price the obstacle, shipping, and so on) and stores the probabilities in `data/`; later scripts feed them to the bandit and `scripts/15_make_results.py` recomputes every number and figure from the included runs. Integration evidence: [`scripts/03_read_chats_with_jev.py`](https://github.com/gioamorim80/chat-reading-bandit/blob/11d1fb8a8d0d2c296e19df30969ffadd34f2596c/scripts/03_read_chats_with_jev.py).

## Get started

Clone, run the tests, and regenerate the results from the included runs.

```sh
git clone https://github.com/gioamorim80/chat-reading-bandit
cd chat-reading-bandit
uv sync --extra test
uv run pytest
uv run python scripts/15_make_results.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: [github.com/gioamorim80/chat-reading-bandit/blob/11d1fb8a8d0d2c296e19df30969ffadd34f2596c/results/numbers.md](https://github.com/gioamorim80/chat-reading-bandit/blob/11d1fb8a8d0d2c296e19df30969ffadd34f2596c/results/numbers.md)
- README: [github.com/gioamorim80/chat-reading-bandit/blob/11d1fb8a8d0d2c296e19df30969ffadd34f2596c/README.md](https://github.com/gioamorim80/chat-reading-bandit/blob/11d1fb8a8d0d2c296e19df30969ffadd34f2596c/README.md)

## Limits and data handling

Results come from simulated shoppers and LLM-written chats; the author's figures were not re-run here.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit 11d1fb8a8d0d](https://github.com/gioamorim80/chat-reading-bandit/tree/11d1fb8a8d0d2c296e19df30969ffadd34f2596c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
