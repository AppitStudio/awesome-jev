# decision-cli (Jev-like decision API from local models on Apple Silicon via MLX)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Go CLI (Chinese docs) that deploys small local LLMs on Apple Silicon with MLX and reads candidate-token logits from a single prefill step to return Jev-style class probabilities for batches, text and multimodal input. It can serve an HTTP endpoint compatible with TypeSafe's `/v1/systemone`, and ships a JevBench public-231 comparison against TypeSafe Jev 1.13.0.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cafe3310/decision-cli) |
| Maintainer | [cafe3310](https://github.com/cafe3310). Independently curated. |
| Format | Go CLI + local HTTP server (MLX backend) |
| Requirements | macOS on Apple Silicon; Go to build; local MLX models. |
| License | [Apache-2.0](https://github.com/cafe3310/decision-cli/blob/4adc47e44206492acdd8db0378497e0f3e1c7f14/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/server/server.go`](https://github.com/cafe3310/decision-cli/blob/4adc47e44206492acdd8db0378497e0f3e1c7f14/internal/server/server.go) at the pinned commit. |

## When to use

- Run cheap on-device classification with a System One-shaped API for prototyping.
- Mismatch: an alternative to hosted Jev; accuracy depends on the small local model.

## How it works

`internal/server/server.go` registers `POST /v1/systemone` (multi-question decisions) and computes probabilities from first-step logits; `bench/run_full_eval.py` records TypeSafe Jev 1.13.0 alongside local models on JevBench. Integration evidence: [`internal/server/server.go`](https://github.com/cafe3310/decision-cli/blob/4adc47e44206492acdd8db0378497e0f3e1c7f14/internal/server/server.go).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/cafe3310/decision-cli.git && cd decision-cli
go build -o bin/decision-cli ./cmd/decision-cli
./bin/decision-cli serve --host 127.0.0.1 --port 8080
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmark report: [github.com/cafe3310/decision-cli/tree/main/bench](https://github.com/cafe3310/decision-cli/tree/main/bench)

## Limits and data handling

Runs locally. Benchmark numbers are self-reported. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 4adc47e44206](https://github.com/cafe3310/decision-cli/tree/4adc47e44206492acdd8db0378497e0f3e1c7f14). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
