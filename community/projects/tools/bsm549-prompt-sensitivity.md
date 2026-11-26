# BSM 549 prompt sensitivity study by Cihat Şengün (how much meaning-preserving prompt changes move Jev, Laya and Gemini decisions in Turkish and English)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

University course project (SUBÜ, autumn 2026, in Turkish) measuring how often meaning-preserving prompt rewrites change typed decisions from Jev 1.14, Laya and Gemini 3.1 Flash-Lite on XNLI and SIB-200 in Turkish and English. Ships the code, prompts, all 60,480 model calls, statistics and figures; the analysis reruns without an API key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chtsngn/bsm549-prompt-duyarliligi) |
| Maintainer | [Cihat Şengün](https://github.com/chtsngn). Independently curated. |
| Format | Python research code with full call logs and results |
| Requirements | Python 3 and the pinned requirements to reproduce the analysis; TypeSafe and Gemini keys only to rerun the model calls. |
| License | [MIT](https://github.com/chtsngn/bsm549-prompt-duyarliligi/blob/0779759715be7e3dd68f686cb93a0ff1e3ea8e13/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bsm549/models.py`](https://github.com/chtsngn/bsm549-prompt-duyarliligi/blob/0779759715be7e3dd68f686cb93a0ff1e3ea8e13/bsm549/models.py) at the pinned commit. |

## When to use

- Anyone choosing prompts for a decision model, or comparing decision models with a general LLM on non-English text.
- Mismatch: a general benchmark; it covers two classification datasets and three models.

## How it works

`bsm549/models.py` sends each case to `https://api.typesafe.ai/v1/systemone` as `jev-1.14.0` with typed choice questions, and the same prompts and variants go to Laya and Gemini; `stats.py` separates prompt-change flips from a repeat-call noise floor and reports calibration (ECE). Integration evidence: [`bsm549/models.py`](https://github.com/chtsngn/bsm549-prompt-duyarliligi/blob/0779759715be7e3dd68f686cb93a0ff1e3ea8e13/bsm549/models.py).

## Get started

Restore the saved call database and rerun the analysis; no model is called.

```sh
git clone https://github.com/chtsngn/bsm549-prompt-duyarliligi && cd bsm549-prompt-duyarliligi
pip install -r requirements.txt
python -m bsm549.export --restore
python -m bsm549.analyze && python -m bsm549.stats && python -m bsm549.figures
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results and figures: [github.com/chtsngn/bsm549-prompt-duyarliligi/tree/main/results](https://github.com/chtsngn/bsm549-prompt-duyarliligi/tree/main/results)

## Limits and data handling

Findings are the student author's own: no significant accuracy difference between Jev and Gemini; 1.7–4.6% of decisions flip under prompt changes for both; Jev's repeat-call noise is 0.7–2.2%; Laya flips up to 24.5%. XNLI is CC BY-NC 4.0 and SIB-200 CC BY-SA 4.0. Text is in Turkish.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 0779759715be](https://github.com/chtsngn/bsm549-prompt-duyarliligi/tree/0779759715be7e3dd68f686cb93a0ff1e3ea8e13). Inspected the README, LICENSE, `bsm549/models.py` and the results folder at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
