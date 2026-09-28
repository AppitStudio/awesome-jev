# sokudan

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Japanese System One decision model: typed answers and probabilities in one forward pass—no text generation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hiroki-abe-58/sokudan) |
| Maintainer | [hiroki-abe-58](https://github.com/hiroki-abe-58). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python research package + Hugging Face weights (~310M). |
| Requirements | Python; GPU recommended for training/eval; HF access for `GeneLab/sokudan-ja-310m`. |
| License | [Apache-2.0](https://github.com/hiroki-abe-58/sokudan/blob/24019601de86df085788039c364dbfb40c9abd0b/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Independent open model; not affiliated with TypeSafe AI. |

## When to use

Use when studying Japanese System One–style decisions without hosted Jev. Prefer TypeSafe Jev for production hosted API use.

## How it works

Encoder model takes Japanese state + typed questions and returns calibrated choice/score/bool answers without generating text. Independent of hosted TypeSafe Jev. Includes benches and a Laya position-bias reproduction. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/hiroki-abe-58/sokudan.git
cd sokudan
git checkout 24019601de86df085788039c364dbfb40c9abd0b
# follow upstream README_en.md / pyproject for install and benches
```

Pin revision `24019601de86df085788039c364dbfb40c9abd0b` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Independent model; not official Jev. Benchmark figures are upstream-reported. Training/live inference not run on the review host.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 2401960](https://github.com/hiroki-abe-58/sokudan/tree/24019601de86df085788039c364dbfb40c9abd0b). AI-assisted README and LICENSE inspection; install/live paths not executed.
