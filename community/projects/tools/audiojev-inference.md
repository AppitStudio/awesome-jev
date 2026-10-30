# AudioJev-Inference (Python library and System One-style HTTP server for the open AudioJev audio decision model)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Inference library and FastAPI service for AudioJev, an open audio decision model described in an arXiv paper: give it an audio clip and natural-language questions and it returns candidate probabilities, yes/no judgments or ordinal scores, several questions per request. The server exposes a `POST /v1/systemone` endpoint in the Jev request shape, and a standard-library client is included. Runs locally on an NVIDIA GPU.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SihanLv/AudioJev-Inference) |
| Maintainer | [SihanLv](https://github.com/SihanLv). Independently curated. |
| Format | Python library + HTTP server |
| Requirements | Python 3.10+ and an NVIDIA CUDA GPU with BF16 support; model weights download from Hugging Face (`shlv/AudioJev`) on first start. |
| License | [Apache-2.0 (code)](https://github.com/SihanLv/AudioJev-Inference/blob/8eeeab5e77d2c410fd6058e7bdf2b4125f11903e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`audiojev_inference/server.py`](https://github.com/SihanLv/AudioJev-Inference/blob/8eeeab5e77d2c410fd6058e7bdf2b4125f11903e/audiojev_inference/server.py) at the pinned commit. |

## When to use

- Ask typed questions about speech, music or sound clips locally, with the same request shape as Jev's text API.
- Mismatch: AudioJev is a separate open model, not TypeSafe's hosted Jev; needs a CUDA GPU.

## How it works

`server.py` serves `/v1/systemone`, decoding the audio and running AudioJev over each choice, noul or score question; `examples/http_client.py` posts a clip and prints each candidate's probability. Integration evidence: [`audiojev_inference/server.py`](https://github.com/SihanLv/AudioJev-Inference/blob/8eeeab5e77d2c410fd6058e7bdf2b4125f11903e/audiojev_inference/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m pip install '.[server]'
audiojev-serve --device cuda:0
curl http://127.0.0.1:8000/health
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo: [huggingface.co/spaces/hugging-apps/audiojev](https://huggingface.co/spaces/hugging-apps/audiojev)
- Paper: [arxiv.org/abs/2610.01293](https://arxiv.org/abs/2610.01293)

## Limits and data handling

Runs locally; audio does not leave the machine. Inference code is Apache-2.0; the `shlv/AudioJev` weights on Hugging Face carry their own (non-Apache) license, check it before use. Independent model; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 8eeeab5e77d2](https://github.com/SihanLv/AudioJev-Inference/tree/8eeeab5e77d2c410fd6058e7bdf2b4125f11903e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
