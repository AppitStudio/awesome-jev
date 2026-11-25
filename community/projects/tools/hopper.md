# Hopper by Hopit (single-pass decision models on Qwen3.5-4B and Gemma-4 12B with a server that speaks the /v1/systemone wire format)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Decision server for five published models, LoRA adapters on Qwen3.5-4B (Hopper, Hopper (G) 1.2 and 1.3) and on Gemma-4 12B (Hopper 12B and Hopper 12B (trained)): a document, policy and question go in and a calibrated probability for every option comes out in one forward pass, served over the JevBench `/v1/systemone` format. Scores on JevBench and the Jev Decision Index are listed per model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hopit-ai/hopper) |
| Maintainer | [Hopit](https://github.com/hopit-ai). Independently curated. |
| Format | Python package and server with Hugging Face adapters (Docker image available) |
| Requirements | Linux with a CUDA 12.8+ GPU and Python 3.12; adapters download from Hugging Face (`HopitAI/hopper`, `HopitAI/hopper-g`). |
| License | [Apache-2.0 (code; some adapters research-only)](https://github.com/hopit-ai/hopper/blob/b774218aa5193904509513a7ba95f12fa2607b61/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hopper_decisions/server.py`](https://github.com/hopit-ai/hopper/blob/b774218aa5193904509513a7ba95f12fa2607b61/hopper_decisions/server.py) at the pinned commit. |

## When to use

- Self-host a Jev-shaped decision model and compare it on JevBench or the Decision Index.
- Mismatch: commercial use of the Hopper and Hopper (G) 4B adapters; they are research and demo only.

## How it works

`hopper_decisions/server.py` serves `/v1/systemone`, so the JevBench harness's existing `typesafe` adapter runs unchanged; the answer is a softmax over option letters with a shipped per-type calibration map. These are Hopit's own models, not TypeSafe's Jev. Integration evidence: [`hopper_decisions/server.py`](https://github.com/hopit-ai/hopper/blob/b774218aa5193904509513a7ba95f12fa2607b61/hopper_decisions/server.py).

## Get started

Install the package and serve an adapter.

```sh
git clone https://github.com/hopit-ai/hopper
cd hopper
# install torch, transformers and peft as pinned in the README, then:
pip install --no-deps -e .
hopper-serve --adapter HopitAI/hopper --port 8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Model card: [huggingface.co/HopitAI/hopper](https://huggingface.co/HopitAI/hopper)
- JevBench board: [benchmarkheaven.com/jev-models](https://benchmarkheaven.com/jev-models)

## Limits and data handling

Not TypeSafe's Jev. The code is Apache-2.0, but the Hopper and Hopper (G) adapter weights are for research and demo use only (their training data included RACE, non-commercial); Hopper 12B (trained) is Apache-2.0. Benchmark figures are the boards' and the authors' own.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit b774218aa519](https://github.com/hopit-ai/hopper/tree/b774218aa5193904509513a7ba95f12fa2607b61). Inspected the README, NOTICE, model card and server code at the pinned commit; no model was run on the review host. Found via the Jev Decision Index board linked from the Nischay-1 model card. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
