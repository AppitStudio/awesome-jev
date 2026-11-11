# JEMM (open-weight multimodal judgment model with a Jev-style endpoint)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open-weight Judgment Engine for MultiModal decisions that picks one candidate per question and returns a probability for every candidate, from text or text plus screenshots, served over a Jev-style `POST /v1/systemone` endpoint and compared with Jev 1.13.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ypcypc/JEMM) |
| Maintainer | [ypcypc](https://github.com/ypcypc). Independently curated. |
| Format | Model server (Python, Apache-2.0) |
| Requirements | One CUDA GPU with at least 64 GB and the `MaestroYan/JEMM` adapter from Hugging Face. |
| License | [Apache-2.0](https://github.com/ypcypc/JEMM/blob/6822fe0fd53c5e6670af6ba99fb2c857a661e532/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jemm/serve.py`](https://github.com/ypcypc/JEMM/blob/6822fe0fd53c5e6670af6ba99fb2c857a661e532/jemm/serve.py) at the pinned commit. |

## When to use

- Self-host screenshot-aware typed decisions behind a Jev-style API.
- Compare an open multimodal decision model with Jev.
- Mismatch: needs a 64 GB GPU; comparisons are the maintainer's.

## How it works

`jemm/serve.py` serves the model behind `/v1/systemone` with `choice` (2–32 options), `noul` and `score` questions and up to four images; the README says it is not affiliated with TypeSafe and treats low confidence as undecided. Integration evidence: [`jemm/serve.py`](https://github.com/ypcypc/JEMM/blob/6822fe0fd53c5e6670af6ba99fb2c857a661e532/jemm/serve.py).

## Get started

Install from GitHub and start the server with the adapter.

```sh
pip install git+https://github.com/ypcypc/JEMM
python -m jemm.serve --adapter MaestroYan/JEMM --port 8790
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model card: [huggingface.co/MaestroYan/JEMM](https://huggingface.co/MaestroYan/JEMM)

## Limits and data handling

Self-hosted; text and screenshots stay on your GPU.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 6822fe0fd53c](https://github.com/ypcypc/JEMM/tree/6822fe0fd53c5e6670af6ba99fb2c857a661e532). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
