# Waldo Bench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Can a decision model find Waldo? 66 Where's Waldo scenes cut into tiles and nine image-input decision models asked to pick his tile: Jev 1.14 found 47 (71%) with the fastest typical search, 2.6 s, behind Liquid d1-ultra's 83%.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/musubipapi/waldo-bench) |
| Maintainer | [musubipapi](https://github.com/musubipapi). Independently curated. |
| Format | Python benchmark (uv) with results, leaderboard and per-tile-size curves |
| Requirements | Python with uv; an OpenRouter key; the IVSN Waldo images downloaded separately. |
| License | [MIT](https://github.com/musubipapi/waldo-bench/blob/fe9e396982730a2cb036723480b16b87c178515f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`waldobench/search_jev.py`](https://github.com/musubipapi/waldo-bench/blob/fe9e396982730a2cb036723480b16b87c178515f/waldobench/search_jev.py) at the pinned commit. |

## When to use

- Compare image-input decision models on a visual search task with cost and latency per scene.
- See how tile size changes accuracy (44% at 384 px to 67% at 128 px, averaged over five models).
- Mismatch: one pass per model on 66 scenes; a puzzle, not a production vision task.

## How it works

Each scene is cut into tiles and the model gets a picture of Waldo plus a Choice question over the tiles through OpenRouter's Decisions API; `search_jev.py` handles Jev. The harness records the pick, its probability, cost and time, and reports intervals and calibration. Integration evidence: [`waldobench/search_jev.py`](https://github.com/musubipapi/waldo-bench/blob/fe9e396982730a2cb036723480b16b87c178515f/waldobench/search_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env    # add your OpenRouter key
uv run python -m waldobench extract path/to/archive.tar.gz
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Full numbers: `results/waldo-bench-v1/` (results.json, leaderboard.csv, curve.csv).

## Limits and data handling

Scene images go to OpenRouter and each model provider on your key. The Waldo images come from a research dataset with its own terms.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit fe9e39698273](https://github.com/musubipapi/waldo-bench/tree/fe9e396982730a2cb036723480b16b87c178515f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
