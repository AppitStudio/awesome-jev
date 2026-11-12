# jevmark (small open decision model inspired by Jev, with calibration research)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent re-implementation of the Jev idea on Qwen3-0.6B and 1.7B base models with LoRA: one forward pass returns a probability for each option in the request, with reports on calibration and on when reinforcement learning for calibrated decisions helps. Not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yuan-phd/jevmark) |
| Maintainer | [yuan-phd](https://github.com/yuan-phd). Independently curated. |
| Format | Python package, training pipeline and LoRA adapters on Hugging Face (Apache-2.0) |
| Requirements | Python 3.11 and uv; a GPU for training (tests run on CPU); adapters download from `yuanphd/jevmark`. |
| License | [Apache-2.0](https://github.com/yuan-phd/jevmark/blob/287bbb1f23440c5f6afd35167167997b07303073/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevmark/systemone.py`](https://github.com/yuan-phd/jevmark/blob/287bbb1f23440c5f6afd35167167997b07303073/jevmark/systemone.py) at the pinned commit. |

## When to use

- Run a small local decision model with System One-style requests.
- Study calibration of decision heads in and out of domain.
- Mismatch: research code; overconfident on unfamiliar domains per its own results; does not call Jev.

## How it works

`jevmark/systemone.py` exposes `systemone()` and `systemone_batch()` that take a message plus questions with options and return per-option probabilities from the loaded adapter, mirroring the System One request shape; results in `docs/RESULTS_v1.md` and later reports cite committed metrics files. Integration evidence: [`jevmark/systemone.py`](https://github.com/yuan-phd/jevmark/blob/287bbb1f23440c5f6afd35167167997b07303073/jevmark/systemone.py).

## Get started

Install the dev environment and load a Hub adapter with `JEVMARK_CHECKPOINT`.

```sh
git clone https://github.com/yuan-phd/jevmark && cd jevmark && make setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Adapters: [huggingface.co/yuanphd/jevmark](https://huggingface.co/yuanphd/jevmark)
- Results v1: [github.com/yuan-phd/jevmark/blob/287bbb1f23440c5f6afd35167167997b07303073/docs/RESULTS_v1.md](https://github.com/yuan-phd/jevmark/blob/287bbb1f23440c5f6afd35167167997b07303073/docs/RESULTS_v1.md)

## Limits and data handling

Runs locally; no requests leave your machine.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 287bbb1f2344](https://github.com/yuan-phd/jevmark/tree/287bbb1f23440c5f6afd35167167997b07303073). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
