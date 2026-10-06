# EuLLM

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Sovereign, local-first LLM engine (AGPL-3.0, Ollama/OpenAI-compatible APIs) whose v0.7.20 adds a `/v1/systemone` decisions endpoint that reads option probabilities straight from local models — e.g. its Jev-Style 2B — with an audit trail; no hosted Jev involved.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eullm/eullm) |
| Product homepage | [www.eullm.eu](https://www.eullm.eu) |
| Maintainer | [eullm](https://github.com/eullm). Independently curated. |
| Format | Engine binary with Ollama- and OpenAI-compatible APIs, chat UI and `/v1/systemone` |
| Requirements | Linux, macOS or Windows; optional NVIDIA GPU. No TypeSafe account — decisions come from local GGUF models. |
| License | [AGPL-3.0](https://github.com/eullm/eullm/blob/34e23986986d162254d49494c49fb93aa4ce0d72/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run Jev-style typed decisions entirely on your own hardware (no cloud, no external API) for latency, cost or data-sovereignty reasons.
- Prototype against the System One wire shape locally before (or instead of) using hosted Jev.
- Mismatch: this is not TypeSafe's Jev; answer quality depends on the local model you serve, so validate it on your own tasks.

## How it works

EuLLM's `/v1/systemone` takes a state and typed questions and, instead of generating text, reads the probability of every option from the served model in one pass, then records each decision to the engine's audit trail. The README's demo has the maintainers' Jev-Style 2B deciding every Snake move in about 8 ms on an RTX 5070 Ti, and 64 questions about a one-page document in 0.66 s (maintainer-reported). Examples cover Snake and email triage.

## Get started

Install the engine with the upstream script (it checks release checksums), then follow the engine guide for `/v1/systemone`:

```sh
curl -fsSL https://raw.githubusercontent.com/eullm/eullm/main/installer/install.sh | sh
eullm run hf.co/Qwen/Qwen3-8B-GGUF:Q4_K_M
# decisions: POST http://localhost:11434/v1/systemone (see docs/engine-guide.md)
```

Runs locally; no TypeSafe charges. Hardware and power costs are yours.

## Examples and demos

- [Snake and email triage examples](https://github.com/eullm/eullm/tree/34e23986986d162254d49494c49fb93aa4ce0d72/examples) using `/v1/systemone`.
- `bench/decision_bench.py` and `bench/decision_calibration.py` for throughput and calibration measurements (maintainer-reported numbers in `docs/benchmarks.md`; not reproduced).

## Limits and data handling

Independent project, not affiliated with TypeSafe; local models are not hosted Jev and calibration varies by model. Forge (pruning/distillation) is still in development. AGPL-3.0 obligations apply to network deployments. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 34e23986986d](https://github.com/eullm/eullm/tree/34e23986986d162254d49494c49fb93aa4ce0d72). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
