# MM-SystemOneBias (benchmark of how stable multimodal System One models, including Jev, stay under option order, labels and injected judgments)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code for the paper "MM-SystemOneBias: Evaluating Bias in Multimodal Jev-Style System One Decision Models": a controlled benchmark of 5,323 image-based Choice, Yes/No and Scoring instances with interventions such as reordered options, changed labels, appended correct or wrong external judgments, conflicting image descriptions, irrelevant information and changed rating scales. It reports flip rates, error introduction and correction, and probability shifts for 5 general backbones and 8 decision models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ALIENS32/MM-SystemOneBias) |
| Maintainer | [ALIENS32](https://github.com/ALIENS32). Independently curated. |
| Format | Python benchmark + dataset on Hugging Face |
| Requirements | Python 3.12+ with uv; GPUs for the local open models; `TYPESAFE_API_KEY` and a `TYPESAFE_BASE_URL` that serves `/typesafe/v1/systemone` to evaluate hosted Jev. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`configs/models/typesafe_jev.yaml`](https://github.com/ALIENS32/MM-SystemOneBias/blob/59a405b13367ac93318bbc913fef470dd1743960/configs/models/typesafe_jev.yaml) at the pinned commit. |

## When to use

- Check how sensitive a decision model is to answer order, label format or a confident wrong hint before you rely on it.
- Mismatch: a quick test; full runs over all models need GPUs and many API calls.

## How it works

`configs/models/typesafe_jev.yaml` evaluates hosted Jev (`jev-1.14.0`) with image input by posting to `/typesafe/v1/systemone` under the base URL you set in `TYPESAFE_BASE_URL` (a gateway-style path; the docs use a placeholder host); other configs cover open decision models such as Jev-Omni, Clef, d3 and JEV-27B-VL, served locally. The pinned dataset is downloaded from Hugging Face. Integration evidence: [`configs/models/typesafe_jev.yaml`](https://github.com/ALIENS32/MM-SystemOneBias/blob/59a405b13367ac93318bbc913fef470dd1743960/configs/models/typesafe_jev.yaml).

## Get started

Set up the environment, download the pinned test split, then run inference for one model config and summarize the metrics.

```sh
git clone https://github.com/ALIENS32/MM-SystemOneBias && cd MM-SystemOneBias
uv sync --extra dev
bash scripts/download_dataset.sh --repo-id ALIENS232/MM-SystemOneBias
export TYPESAFE_API_KEY=... TYPESAFE_BASE_URL=...
bash scripts/infer.sh --config configs/models/typesafe_jev.yaml \
--dataset-path ~/.cache/mm-systemonebias/dataset --output-dir ~/.cache/mm-systemonebias/runs/typesafe_jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2611.26557](https://arxiv.org/abs/2611.26557)
- Dataset: [huggingface.co/datasets/ALIENS232/MM-SystemOneBias](https://huggingface.co/datasets/ALIENS232/MM-SystemOneBias)
- Inference guide: [github.com/ALIENS32/MM-SystemOneBias/blob/59a405b13367ac93318bbc913fef470dd1743960/docs/inference.md](https://github.com/ALIENS32/MM-SystemOneBias/blob/59a405b13367ac93318bbc913fef470dd1743960/docs/inference.md)

## Limits and data handling

Results are the authors' own (paper on arXiv, 2611.26557); for example they report Jev-Omni at 25.18% flip rate on option order. Images and questions are sent to TypeSafe when evaluating hosted Jev. Dataset and model licenses are separate; the code repository has no license file, so reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 59a405b13367](https://github.com/ALIENS32/MM-SystemOneBias/tree/59a405b13367ac93318bbc913fef470dd1743960). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
