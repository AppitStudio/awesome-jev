# jev-brain (one GPU serving chat and Jev-compatible decisions from one open model)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Self-hosted gateway in front of a single vLLM process that serves OpenAI-style chat and Jev-compatible `/v1/systemone` decisions at the same time from one loaded model, with nine profiles across Gemma 4 and Qwen models in several quantizations (some with image decisions) and published Decision Index and latency results; independent of hosted Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wcole3/jev-brain) |
| Maintainer | [wcole3](https://github.com/wcole3). Independently curated. |
| Format | Python gateway with vLLM profiles |
| Requirements | A large NVIDIA GPU, vLLM and uv; open model weights per profile. |
| License | [MIT](https://github.com/wcole3/jev-brain/blob/900d621428e682c4e021c3b104db5a6449f852a7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`gateway/decide.py`](https://github.com/wcole3/jev-brain/blob/900d621428e682c4e021c3b104db5a6449f852a7/gateway/decide.py) at the pinned commit. |

## When to use

- Run Jev-style typed decisions and chat on your own GPU from one model.
- Mismatch: not TypeSafe's Jev; scores and latency are the author's measurements.

## How it works

`gateway/decide.py` implements the `/v1/systemone` request flow against the loaded open model; the gateway proxies chat to vLLM alongside it. Integration evidence: [`gateway/decide.py`](https://github.com/wcole3/jev-brain/blob/900d621428e682c4e021c3b104db5a6449f852a7/gateway/decide.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/wcole3/jev-brain && cd jev-brain
uv sync
make up PROFILE=gemma-4-31b-fp8
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with scores: [github.com/wcole3/jev-brain#readme](https://github.com/wcole3/jev-brain#readme)

## Limits and data handling

Runs on your hardware; nothing goes to TypeSafe. Model licences follow each base model.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 900d621428e6](https://github.com/wcole3/jev-brain/tree/900d621428e682c4e021c3b104db5a6449f852a7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
