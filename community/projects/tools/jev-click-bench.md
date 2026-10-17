# jev-click-bench

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark of Jev 1.14's `box` tool as a GUI click model on ScreenSpot-v2 and ScreenSpot-Pro with the official scoring: 84% on ordinary screens, 19% on 4K pro apps, and 43% to 60% on Pro after one or two zoomed second looks, with every request logged.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/arthurkatcher/jev-click-bench) |
| Maintainer | [arthurkatcher](https://github.com/arthurkatcher). Independently curated. |
| Format | Python benchmark harness with logged runs and analysis |
| Requirements | Python 3.10+, `requests` and `pillow`; the ScreenSpot datasets from Hugging Face; an OpenRouter key to re-run (about $0.19 per v2 pass). |
| License | [MIT](https://github.com/arthurkatcher/jev-click-bench/blob/8ddab44c8f8953d0d34b010577b4dd74ead3035e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/arthurkatcher/status/2111499108733038723)). |
| Jev evidence | [`jev.py`](https://github.com/arthurkatcher/jev-click-bench/blob/8ddab44c8f8953d0d34b010577b4dd74ead3035e/jev.py) at the pinned commit. |

## When to use

- Check how far Jev's box can go as the click step of a computer-use agent before you build on it.
- Reuse the zoom-and-look-again harness and its cost per 1,000 clicks.
- Mismatch: one model version and still screenshots; box always returns a box, so missing targets are not tested.

## How it works

`jev.py` sends each screenshot and instruction to `typesafe/jev-1.14` through OpenRouter and asks a Box question; `screenspot.py` scores the box centre with the benchmarks' official code. The zoom mode crops around the first answer at 2x (and post hoc 4x) and asks again, and every request and response is written to the run logs. Integration evidence: [`jev.py`](https://github.com/arthurkatcher/jev-click-bench/blob/8ddab44c8f8953d0d34b010577b4dd74ead3035e/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install requests pillow
cp .env.example .env   # add an OpenRouter key
python3 tests/test_offline.py                  # no API calls
python3 screenspot.py run --pass 1 --workers 4 # ScreenSpot-v2, raw
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author's write-up: [arthurkatcher.com/blog/teaching-jevs-box-to-click-3x-better](https://arthurkatcher.com/blog/teaching-jevs-box-to-click-3x-better)
- Author's X post: [x.com/arthurkatcher/status/2111499108733038723](https://x.com/arthurkatcher/status/2111499108733038723)

## Limits and data handling

Screenshots and instructions from the public benchmarks go to OpenRouter and TypeSafe on your key. The author notes Jev is not deterministic (the same request returns the same box about 30% of the time) and that other models' scores are as published, not re-run.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 8ddab44c8f89](https://github.com/arthurkatcher/jev-click-bench/tree/8ddab44c8f8953d0d34b010577b4dd74ead3035e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
