# Jeva

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research System One model (Jeva-4B) designed for typed choice/noul/score decisions, with weights, fine-tuning code and a project page comparing it with Jev-1.13.0.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/LiQiiiii/Jeva) |
| Maintainer | [LiQiiiii](https://github.com/LiQiiiii). Independently curated. |
| Format | Model + Python package + training code |
| Requirements | GPU for local inference; Hugging Face weights. |
| License | [Apache-2.0](https://github.com/LiQiiiii/Jeva/blob/f231c9ac31ba72f2ca4ca8aac662b279f3438fdb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`examples/local_inference.py`](https://github.com/LiQiiiii/Jeva/blob/f231c9ac31ba72f2ca4ca8aac662b279f3438fdb/examples/local_inference.py) at the pinned commit. |

## When to use

- Run a local open System One model as a Jev alternative for research.
- Mismatch: not TypeSafe Jev; benchmark comparisons are author-reported.

## How it works

`Jeva.from_pretrained` loads the model; typed Choice/Noul/Score questions are answered locally. Evaluation and fine-tuning docs are included. Integration evidence: [`examples/local_inference.py`](https://github.com/LiQiiiii/Jeva/blob/f231c9ac31ba72f2ca4ca8aac662b279f3438fdb/examples/local_inference.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m pip install -r requirements.txt
python examples/local_inference.py --model LIQIIIII/Jeva-4B
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model: [huggingface.co/LIQIIIII/Jeva-4B](https://huggingface.co/LIQIIIII/Jeva-4B)
- Project page: [liqiiiii.github.io/Jeva/](https://liqiiiii.github.io/Jeva/)

## Limits and data handling

Runs locally; no TypeSafe calls.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit f231c9ac31ba](https://github.com/LiQiiiii/Jeva/tree/f231c9ac31ba72f2ca4ca8aac662b279f3438fdb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
