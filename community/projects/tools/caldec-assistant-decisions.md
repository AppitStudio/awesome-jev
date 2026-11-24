# CalDec (Assistant Decisions) by Kristijan Grozdanovski (open dataset and small encoder checkpoints for typed decisions in real-time assistants, with Jev as a reference)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Dataset, training recipes and checkpoints (fine-tunes of Laya and GLiNER2.5-Decide, plus CalDec Ultra with 8,192-token context) for closed assistant questions such as end of turn, prompt injection, tool selection and memory-worthiness. Jev 1.13 is the zero-shot hosted reference: on the 1,647-case test, CalDec GLiNER scored 0.843 accuracy vs Jev's 0.836, a gap the author reports as not significant.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kgrozdanovski/caldec) |
| Maintainer | [Kristijan Grozdanovski](https://github.com/kgrozdanovski). Independently curated. |
| Format | Python dataset, training recipes, checkpoints and evaluation harness |
| Requirements | Python; an OpenRouter key only to re-run the Jev reference. |
| License | [Apache-2.0](https://github.com/kgrozdanovski/caldec/blob/0f39a35484c15bf297da857ecadd811936476a00/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev_decisions.py`](https://github.com/kgrozdanovski/caldec/blob/0f39a35484c15bf297da857ecadd811936476a00/scripts/jev_decisions.py) at the pinned commit. |

## When to use

- Run assistant-side typed decisions locally and compare against Jev on the same cases.
- Mismatch: if you need a TypeSafe client; Jev is only the reference here.

## How it works

`scripts/jev_decisions.py` calls Jev (and the open Kev 4B) through OpenRouter's decisions endpoint for evaluation only; their outputs were never used as training labels. Integration evidence: [`scripts/jev_decisions.py`](https://github.com/kgrozdanovski/caldec/blob/0f39a35484c15bf297da857ecadd811936476a00/scripts/jev_decisions.py).

## Get started

Read the dataset and results docs, then use the released checkpoints or re-run the benchmark.

```sh
git clone https://github.com/kgrozdanovski/caldec.git && cd caldec
python3 -m pip install -r requirements.txt
# then load a checkpoint, e.g. laya.load("checkpoints/v1-laya/final").system_one(state, questions)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev reference: [github.com/kgrozdanovski/caldec/blob/0f39a35484c15bf297da857ecadd811936476a00/JEV.md](https://github.com/kgrozdanovski/caldec/blob/0f39a35484c15bf297da857ecadd811936476a00/JEV.md)
- Results: [github.com/kgrozdanovski/caldec/blob/0f39a35484c15bf297da857ecadd811936476a00/RESULTS.md](https://github.com/kgrozdanovski/caldec/blob/0f39a35484c15bf297da857ecadd811936476a00/RESULTS.md)

## Limits and data handling

Accuracy is agreement with synthetic target labels, not independent correctness (the author's caveat). Jev was reached through OpenRouter, not TypeSafe directly.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 0f39a35484c1](https://github.com/kgrozdanovski/caldec/tree/0f39a35484c15bf297da857ecadd811936476a00). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
