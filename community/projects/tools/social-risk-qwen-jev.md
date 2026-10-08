# Social Risk · Qwen3-VL + Jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Concluded research project (Chinese, with English README) on multimodal risk moderation for Chinese social posts (LT-EDI Chinese misogyny memes): Qwen3-VL with a language-side LoRA extracts structured evidence JSON, TypeSafe Jev makes the policy decision, and a frozen 170-item test leaderboard compares 13 methods — where a TF-IDF + logistic-regression baseline ranked first — with pure-Jev vs multimodal+Jev ablations and CPU regression tests.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev) |
| Maintainer | [TianJinWeiBoss520](https://github.com/TianJinWeiBoss520). Independently curated. |
| Format | Python research repository with offline demo, experiments and docs |
| Requirements | Python 3.12+; GPU and dataset access for full reproduction; `TYPESAFE_API_KEY` for Jev runs. Offline demo needs no key. |
| License | [MIT](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev/blob/16b09d609c4515164ee157abe57f2642c96b6f12/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Study how a hosted decision model behaves as the policy layer over VLM evidence.
- Reuse the honest, frozen-test evaluation setup and negative results.
- Mismatch: research artefact, not a moderation service; risk bands are operational, not calibrated probabilities.

## How it works

Experiment scripts such as [`run_ltedi_jev_text_vs_multimodal172.py`](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev/blob/16b09d609c4515164ee157abe57f2642c96b6f12/experiments/v1/src/run_ltedi_jev_text_vs_multimodal172.py) send evidence JSON (Qwen fields removed) to Jev; results and methodology are in [`docs/PURE_JEV_TEST_SUPPLEMENT.md`](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev/blob/16b09d609c4515164ee157abe57f2642c96b6f12/docs/PURE_JEV_TEST_SUPPLEMENT.md) and the README leaderboard.

## Get started

Run the three-minute offline demo (README):

```sh
git clone https://github.com/TianJinWeiBoss520/social-risk-qwen-jev.git && cd social-risk-qwen-jev
python -m venv .venv && source .venv/bin/activate
# follow README 三分钟离线体验 / README.en.md
```

Jev experiment runs bill TypeSafe; the offline demo is free.

## Examples and demos

- [English README](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev/blob/16b09d609c4515164ee157abe57f2642c96b6f12/README.en.md).
- README frozen-test leaderboard (author-reported).

## Limits and data handling

Code, configs and summary results are public; dataset images/text are not. Results are the author's. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 16b09d609c45](https://github.com/TianJinWeiBoss520/social-risk-qwen-jev/tree/16b09d609c4515164ee157abe57f2642c96b6f12). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
