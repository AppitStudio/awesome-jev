# StartLux-Decision

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent open typed decision models (0.8B to 35B-A3B, text and images) served on the TypeSafe `/v1/systemone` request format, with inference code, evaluation scripts, and game logs; not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/StartLuxLabs/StartLux-Decision) |
| Maintainer | [StartLuxLabs](https://github.com/StartLuxLabs). Independently curated. |
| Format | Model family + inference server code + evaluation harnesses |
| Requirements | A GPU (or CPU for small GGUF quantizations) with llama.cpp or the provided server; Hugging Face access to download weights. No TypeSafe key needed for self-hosted inference. |
| License | [Apache-2.0 (code); weights CC BY-NC 4.0](https://github.com/StartLuxLabs/StartLux-Decision/blob/0e7a2e81b9c92756e26d8edd843a44d50e362669/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run Jev-style typed decisions locally or on your own GPU while keeping clients written for `/v1/systemone` unchanged.
- Compare an open decision model against hosted Jev in the same game or benchmark harness.
- Mismatch: commercial use of the weights needs a separate license from StartLux Labs.

## How it works

The models answer Noul/Choice/Score questions with option probabilities in one forward pass and accept TypeSafe-format `/v1/systemone` requests, so existing Jev clients can point at a self-hosted base URL. The README reports Decision Index 0.2.1 scores and game results (chess vs Jev 1.13, Super Mario Bros.) measured by the maintainer; some benchmark train splits are in its training data, as disclosed upstream.

## Get started

Download a small GGUF and serve it with llama.cpp (per the README quick start):

```sh
hf download startlux-models/StartLux-Decision-4B-Q8_0-GGUF --local-dir StartLux-Decision-4B-Q8_0-GGUF
cd StartLux-Decision-4B-Q8_0-GGUF && pip install -r requirements.txt
llama-server -m StartLux-Decision-4B-Q8_0.gguf -ngl 99 -c 16384 --parallel 4 --port 8081
```

Self-hosted inference has no TypeSafe charge; GPU/hosting costs are yours.

## Examples and demos

- [Hugging Face collection](https://huggingface.co/collections/startlux-models/startlux-decision-6abba92b301b573fa154d493) and README demos (computer-use store task, chess vs Jev 1.13). All scores are maintainer-reported, not reproduced here.

## Limits and data handling

Weights are CC BY-NC 4.0 (non-commercial; commercial use needs a separate license). Benchmark figures are self-reported and partly use public train splits. Independent of TypeSafe; not official Jev.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 0e7a2e81b9c9](https://github.com/StartLuxLabs/StartLux-Decision/tree/0e7a2e81b9c92756e26d8edd843a44d50e362669). Inspected the README (license, quick start, benchmark disclosures) and the repository LICENSE; weights were not downloaded and no inference was run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
