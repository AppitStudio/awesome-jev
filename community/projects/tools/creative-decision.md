# Creative Decision Making (cdm)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Paper and Python library that combine calibrated decision-model judgments (Jev and peers) with decision theory: calibrate, pool, gate unknowns to verify, and pick options plus bounded bets on new ideas, with a benchmark on 237 real Jev judgments.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chrisnkuno/creative-decision) |
| Maintainer | [chrisnkuno](https://github.com/chrisnkuno). Independently curated. |
| Format | Python library + paper |
| Requirements | Python with uv; `TYPESAFE_API_KEY` for live Jev (falls back to a mock judge). |
| License | [MIT](https://github.com/chrisnkuno/creative-decision/blob/abbc2b4b9be19e658c5b33d2549815bb9afd76ef/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/cdm/judges.py`](https://github.com/chrisnkuno/creative-decision/blob/abbc2b4b9be19e658c5b33d2549815bb9afd76ef/src/cdm/judges.py) at the pinned commit. |

## When to use

- Turn Jev probabilities into principled choices with calibration and risk bounds.
- Want to back novel options without betting on unverified ones.
- Mismatch: research code and maths; not a turnkey product.

## How it works

`src/cdm/judges.py` defines a `Judge` protocol for any System One JSON shape and a `JevJudge` that calls Jev. Judgments are temperature-calibrated per question type, pooled, gated (clear, verify, reject) and valued as exact lotteries before selection. `scripts/jev_benchmark.py` reproduces the Jev benchmark from cached answers. Integration evidence: [`src/cdm/judges.py`](https://github.com/chrisnkuno/creative-decision/blob/abbc2b4b9be19e658c5b33d2549815bb9afd76ef/src/cdm/judges.py).

## Get started

From the upstream README: `uv sync`, then run `demo.py` with or without a key.

```sh
uv sync
TYPESAFE_API_KEY=... uv run python demo.py
uv run python scripts/jev_benchmark.py analyze
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- paper.pdf (Unknown Is Not Risky)
- MATH.md

## Limits and data handling

Option text goes to TypeSafe in live mode. Benchmark results reflect the author's tasks and Jev 1.13.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit abbc2b4b9be1](https://github.com/chrisnkuno/creative-decision/tree/abbc2b4b9be19e658c5b33d2549815bb9afd76ef). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
