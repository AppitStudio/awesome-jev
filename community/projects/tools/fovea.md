# Fovea-4B (open image decision model served over the System One API)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Fovea-4B is a 4B decision model for images: given a photo, document, receipt, chart or screenshot plus a JSON state and a typed question, it returns a probability for every allowed answer in one forward pass. It is served over TypeSafe's System One API shape, so existing System One clients can call it unchanged; the README compares it with Imajev-4B, H2O-Lightning-4B and Jev-Vision on ImageJevBench.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Sivasuthan9/fovea) |
| Maintainer | [Sivasuthan9](https://github.com/Sivasuthan9). Independently curated. |
| Format | Python SDK (`fovea-sdk`) + local server; Apache-2.0 weights on Hugging Face |
| Requirements | A CUDA GPU for local serving (`fovea-sdk[local]`); the client alone needs no extra packages. |
| License | [Apache-2.0](https://github.com/Sivasuthan9/fovea/blob/80f09c602d3f511b0144496ea351cc709d4d4afb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`fovea_sdk/server.py`](https://github.com/Sivasuthan9/fovea/blob/80f09c602d3f511b0144496ea351cc709d4d4afb/fovea_sdk/server.py) at the pinned commit. |

## When to use

- Self-host image yes/no, choice and score decisions with a System One-compatible endpoint.
- Mismatch: an alternative to hosted Jev-Vision, not a Jev client; benchmark figures are the maintainer's.

## How it works

`fovea_sdk/server.py` serves `/v1/systemone` for `fovea-4b` and `fovea_sdk/client.py` posts the same request shape, so swapping between Fovea and other System One hosts is a URL change. Integration evidence: [`fovea_sdk/server.py`](https://github.com/Sivasuthan9/fovea/blob/80f09c602d3f511b0144496ea351cc709d4d4afb/fovea_sdk/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "fovea-sdk[local]"
fovea-sdk serve   # prints the /v1/systemone URL when ready
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Weights: [huggingface.co/Sivasuthan/fovea-4b](https://huggingface.co/Sivasuthan/fovea-4b)

## Limits and data handling

Runs locally; images stay on your host. ImageJevBench comparisons are self-reported. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 80f09c602d3f](https://github.com/Sivasuthan9/fovea/tree/80f09c602d3f511b0144496ea351cc709d4d4afb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
