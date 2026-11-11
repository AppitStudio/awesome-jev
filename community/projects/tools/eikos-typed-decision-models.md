# Eikos (open typed-decision models for finance, compared with Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Family of open typed-decision models (Eikos-4B and Eikos-27B) for finance, trading and trade finance that answer in one forward pass with a calibrated probability per option, served behind a TypeSafe-compatible `/v1/systemone` API and evaluated against Jev and Laya.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/caiovicentino/eikos) |
| Maintainer | [caiovicentino](https://github.com/caiovicentino). Independently curated. |
| Format | Open-weight models with serving, data, training and evaluation code (Python, MIT code) |
| Requirements | A GPU with vLLM 0.30+ (bf16, FP8 or INT4 builds) or an Apple Silicon Mac for the MLX builds. |
| License | [MIT](https://github.com/caiovicentino/eikos/blob/8902fbe9e06e10da50d3ed5d27bb52fcf8ddd900/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`eikos/serve.py`](https://github.com/caiovicentino/eikos/blob/8902fbe9e06e10da50d3ed5d27bb52fcf8ddd900/eikos/serve.py) at the pinned commit. |

## When to use

- Self-host a decision model for finance rules and policy checks.
- Compare calibration of an open decision model with Jev.
- Mismatch: finance-focused; headline numbers come from the maintainer's own harness; models MIT on fine-tuning deltas (Apache-2.0 bases), data CC BY 4.0.

## How it works

`eikos/serve.py` is a typed-decision server compatible with the TypeSafe API (`POST /v1/systemone` and `/v1/evaluate`); `evaluation/eval_jev_suite.py` runs the same suites through Jev for the comparison tables. Integration evidence: [`eikos/serve.py`](https://github.com/caiovicentino/eikos/blob/8902fbe9e06e10da50d3ed5d27bb52fcf8ddd900/eikos/serve.py).

## Get started

Install the library, then follow the README to serve a model with vLLM or MLX.

```sh
git clone https://github.com/caiovicentino/eikos.git && cd eikos
pip install -e ".[vllm]"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Models: [huggingface.co/caiovicentino1/Eikos-27B](https://huggingface.co/caiovicentino1/Eikos-27B)
- Live demo: [huggingface.co/spaces/caiovicentino1/eikos-4b-typed-decisions-demo](https://huggingface.co/spaces/caiovicentino1/eikos-4b-typed-decisions-demo)

## Limits and data handling

Self-hosted; data stays on your hardware unless you rerun the Jev comparison.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 8902fbe9e06e](https://github.com/caiovicentino/eikos/tree/8902fbe9e06e10da50d3ed5d27bb52fcf8ddd900). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
