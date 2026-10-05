# CLM (Contrastive Language Models)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent open System One model (CLM-8B: Qwen3-8B embeddings plus a small contrastive state/action head) served behind a TypeSafe-compatible `POST /v1/systemone`, so Jev-style requests replay unchanged; not affiliated with TypeSafe.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Contrastive-LM/CLM) |
| Maintainer | [Contrastive-LM](https://github.com/Contrastive-LM). Independently curated. |
| Format | Model + inference server + Python client, benchmarks and fine-tuning guide |
| Requirements | A GPU host for `vllm serve Qwen/Qwen3-8B` (pooling runner) plus `clm-serve` (downloads a 75 MB reference head). No TypeSafe key needed; the Jev comparison example needs one. |
| License | [Apache-2.0](https://github.com/Contrastive-LM/CLM/blob/d5f9ef0fd9bde185df0ceaad4f4ecc6cfe8c34f6/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run Jev-shaped decisions on your own hardware when data cannot leave it or latency matters (many candidate actions, reused actions).
- Use a fine-tuned verifier to pick among sampled agent solutions.
- Mismatch: CLM is not Jev; parity and speed figures are maintainer-reported, so validate on your own labelled examples before swapping providers.

## How it works

CLM embeds the state and each candidate action/option with Qwen3-8B and scores them with a 20M-parameter contrastive head, so option texts are embedded once and cached. `clm-serve` exposes `POST /v1/systemone`, `GET /v1/models` and a playground; `CLMClient.system_one(state, questions)` accepts TypeSafe wire-format questions. The README reports CLM-8B on par with Jev on computer-use, gaming and tool-calling tasks at up to 9× lower latency, and fine-tuned verifier results on DeepSWE and Terminal-Bench 2.1 (all maintainer measurements; [README](https://github.com/Contrastive-LM/CLM/blob/d5f9ef0fd9bde185df0ceaad4f4ecc6cfe8c34f6/README.md)).

## Get started

Install, start the embedding server and the CLM API, then ask a typed question (local inference, no TypeSafe charge):

```sh
pip install contrastive-lm
vllm serve Qwen/Qwen3-8B --served-model-name qwen3-8b --runner pooling --max-model-len 2048 --port 8090 &
clm-serve   # CLM API on :8700
# python: from clm import CLMClient, Noul
#         CLMClient().system_one(state="...", questions={"urgent": Noul(instructions="Is this urgent?")})
```

Self-hosted inference has no TypeSafe charge; GPU/hosting costs are yours. Only the optional Jev comparison runs contact TypeSafe.

## Examples and demos

- `examples/t_rex/`: the Chrome dinosaur game in real time with `run.py --model clm|jev`, including recorded Jev results.
- README *Results* (zero-shot and agentic-verifier charts) and `docs/FINETUNING.md`.

## Limits and data handling

States are truncated at 2048 tokens by default (raise both server limits for longer ones). Benchmark claims, including that Jev underperforms as a long-horizon verifier, are the maintainer's and were not reproduced. Not affiliated with or endorsed by TypeSafe.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit d5f9ef0fd9bd](https://github.com/Contrastive-LM/CLM/tree/d5f9ef0fd9bde185df0ceaad4f4ecc6cfe8c34f6). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
