# Chon (open Gemma-4-31B LoRA decision model and server that speaks the System One wire format)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Serving code, Docker image and guide for Chon-1.1-31B, an Apache-2.0 LoRA adapter on Gemma-4-31B that answers typed choice, yes/no and score questions with a calibrated probability for every option in one forward pass. The HTTP server speaks TypeSafe's `/v1/systemone` format so JevBench's `typesafe` adapter and other System One clients work unchanged.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xoai/chon) |
| Maintainer | [xoai](https://github.com/xoai). Independently curated. |
| Format | Python package + Docker server (`chon[serve]`); model weights on Hugging Face |
| Requirements | One GPU with 80 GB+ for bf16 (maintainer timings on an RTX PRO 6000 Blackwell); Hugging Face access to `google/gemma-4-31B-it`. |
| License | [Apache-2.0](https://github.com/xoai/chon/blob/7e8c15ae3fde3e52e35d6b9ff83d0353b8adcdbd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/xoai/status/2116378297550741776)). |
| Jev evidence | [`chon/serve.py`](https://github.com/xoai/chon/blob/7e8c15ae3fde3e52e35d6b9ff83d0353b8adcdbd/chon/serve.py) at the pinned commit. |

## When to use

- Self-host a Jev-compatible typed-decision model for evaluation or private data.
- Mismatch: this is an alternative to hosted Jev, not a client for it; 31B needs a large GPU.

## How it works

`chon/serve.py` exposes `POST /v1/systemone` and `chon/answers.py` turns each label distribution into a System One answer object, so tools written for TypeSafe's API (including the JevBench harness) can point at it. A commit band (`--noul-commit 0.199,0.801`) matches JevBench's abstention rule. Integration evidence: [`chon/serve.py`](https://github.com/xoai/chon/blob/7e8c15ae3fde3e52e35d6b9ff83d0353b8adcdbd/chon/serve.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "chon[serve] @ git+https://github.com/xoai/chon"
python -m chon.serve --model ninhnv/chon-1.1-31b --port 8000 --noul-commit 0.199,0.801
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model card: [huggingface.co/ninhnv/chon-1.1-31b](https://huggingface.co/ninhnv/chon-1.1-31b)
- Release post on X: [x.com/xoai/status/2116378297550741776](https://x.com/xoai/status/2116378297550741776)

## Limits and data handling

Runs locally; no data leaves your GPU host. Decision Index and JevBench numbers in the README are the maintainer's own runs, not official board results. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 7e8c15ae3fde](https://github.com/xoai/chon/tree/7e8c15ae3fde3e52e35d6b9ff83d0353b8adcdbd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
