# MiniCPM-OCR (open OCR models from OpenBMB, with a 2B Jev-style decision model that scores OCR correctness)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open-source document parsing from OpenBMB: a 1.3B OCR model for text, tables and formulas, plus MiniCPM-OCR Jev, a 2B decision model trained from Qwen3.5-2B that returns a 0-1 quality score for an OCR result against the original region image. It can pick the best of several OCR models' outputs per region and flag doubtful tables and formulas for human review before they enter a RAG index. OpenBMB reports 93.6 AUROC on its JevOCRBench. Weights and code under Apache-2.0.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/OpenBMB/MiniCPM-OCR) |
| Maintainer | [OpenBMB](https://github.com/OpenBMB). Independently curated. |
| Format | Model weights on Hugging Face, SDK, Docker and llama.cpp/Ollama guides |
| Requirements | A GPU for fast parsing; Ollama or llama.cpp for the GGUF decision model. No TypeSafe key. |
| License | [Apache-2.0](https://github.com/OpenBMB/MiniCPM-OCR/blob/62d5e649c32be2271f2c8c66ec8307f3d7373903/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/enmao_li/status/2115370301995581712)). |
| Jev evidence | [`docs/minicpm_ocr_jev_en.md`](https://github.com/OpenBMB/MiniCPM-OCR/blob/62d5e649c32be2271f2c8c66ec8307f3d7373903/docs/minicpm_ocr_jev_en.md) at the pinned commit. |

## When to use

- Quality-check OCR output before indexing documents.
- Mismatch: an OpenBMB model named after Jev, not TypeSafe's Jev; benchmark figures are OpenBMB's.

## How it works

`docs/minicpm_ocr_jev_en.md` documents the classification-head model and its scoring; the llama.cpp and Ollama guides convert it to a GGUF with the `systemone` chat template so it serves typed decisions locally. Integration evidence: [`docs/minicpm_ocr_jev_en.md`](https://github.com/OpenBMB/MiniCPM-OCR/blob/62d5e649c32be2271f2c8c66ec8307f3d7373903/docs/minicpm_ocr_jev_en.md).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/OpenBMB/MiniCPM-OCR && cd MiniCPM-OCR
# follow docs/minicpm_ocr_jev_en.md (SDK, Docker) or docs/ollama_deploy_jev_en.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Weights: [huggingface.co/openbmb/MiniCPM-OCR-1.0-Jev](https://huggingface.co/openbmb/MiniCPM-OCR-1.0-Jev)
- Benchmark: [huggingface.co/datasets/openbmb/JevOCRBench](https://huggingface.co/datasets/openbmb/JevOCRBench)

## Limits and data handling

Runs on your own hardware; OpenBMB's optional hosted API has its own terms.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 62d5e649c32b](https://github.com/OpenBMB/MiniCPM-OCR/tree/62d5e649c32be2271f2c8c66ec8307f3d7373903). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
