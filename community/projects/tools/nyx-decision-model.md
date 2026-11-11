# nyx (compact 4B decision model with a TypeSafe-compatible gateway)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Compact 4B decision model, production gateway and typed SDKs for Choice, Score and Noul; the 3.29 GB GGUF runs locally through llama.cpp, the gateway implements the TypeSafe System One wire contract, and the README benchmarks it against Jev 1.13.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/devanshbatham/nyx) |
| Maintainer | [devanshbatham](https://github.com/devanshbatham). Independently curated. |
| Format | Open-weight model, gateway and SDKs (Python/TypeScript, Apache-2.0) |
| Requirements | 8 GB free RAM, Python 3.11+, a C++ toolchain and CMake; optional Metal, CUDA or ROCm. |
| License | [Apache-2.0](https://github.com/devanshbatham/nyx/blob/f54400f5b3c766be695420b788dfd5bc0b75d780/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/nyx/hosted_api.py`](https://github.com/devanshbatham/nyx/blob/f54400f5b3c766be695420b788dfd5bc0b75d780/src/nyx/hosted_api.py) at the pinned commit. |

## When to use

- Run a local decision model behind the same API as Jev.
- Benchmark a small open model against Jev on classification.
- Mismatch: lower pooled accuracy than Jev in the maintainer's own table; benchmarks are the maintainer's.

## How it works

`src/nyx/hosted_api.py` serves `POST /v1/systemone`; the README says existing TypeSafe clients only change their base URL and key, and `benchmarks/` reproduces the nyx vs Jev table. Integration evidence: [`src/nyx/hosted_api.py`](https://github.com/devanshbatham/nyx/blob/f54400f5b3c766be695420b788dfd5bc0b75d780/src/nyx/hosted_api.py).

## Get started

Clone, install the server extra, download the model from Hugging Face, then start the gateway.

```sh
git clone https://github.com/devanshbatham/nyx.git && cd nyx
pip install '.[server]' && hf download devanshbatham/nyx --local-dir ./nyx-model
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmarks: [github.com/devanshbatham/nyx/tree/f54400f5b3c766be695420b788dfd5bc0b75d780/benchmarks](https://github.com/devanshbatham/nyx/tree/f54400f5b3c766be695420b788dfd5bc0b75d780/benchmarks)
- Model: [huggingface.co/devanshbatham/nyx](https://huggingface.co/devanshbatham/nyx)

## Limits and data handling

Runs on your hardware; nothing goes to TypeSafe unless you rerun the Jev comparison.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit f54400f5b3c7](https://github.com/devanshbatham/nyx/tree/f54400f5b3c766be695420b788dfd5bc0b75d780). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
