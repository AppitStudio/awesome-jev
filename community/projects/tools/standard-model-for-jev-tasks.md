# standard_model_for_jev_tasks (jev-shim)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Dependency-free shim that serves an ordinary instruct LLM (vLLM or llama.cpp) behind TypeSafe's `POST /v1/systemone` interface, constraining every answer with a GBNF grammar and reading probabilities from logits, so Jev clients and JevBench can drive a self-hosted model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NeuralNotwerk/standard_model_for_jev_tasks) |
| Maintainer | [NeuralNotwerk](https://github.com/NeuralNotwerk). Independently curated. |
| Format | Python package providing the `jev-shim` HTTP server (install from source) |
| Requirements | Python; a vLLM (recommended, xgrammar structured outputs) or llama.cpp backend and a GPU suited to your model; no TypeSafe key needed. |
| License | [Apache-2.0](https://github.com/NeuralNotwerk/standard_model_for_jev_tasks/blob/f63fb177a1ca7e7508ff83d429f59d9438346842/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Develop against the `/v1/systemone` shape without hosted calls, or compare a local model with Jev on JevBench.
- Self-host Noul/Choice/Score answers with per-option probabilities from your own model.
- Mismatch: not Jev — an interface-compatible substitute; quality depends on the model you serve.

## How it works

[`src/jev_shim/server.py`](https://github.com/NeuralNotwerk/standard_model_for_jev_tasks/blob/f63fb177a1ca7e7508ff83d429f59d9438346842/src/jev_shim/server.py) builds a ChatML prompt with the state, question, options and the exact GBNF grammar, then (default `logprobs` mode) walks the grammar and reads option probabilities from the backend's logits without generating text. [`scripts/run_jevbench.sh`](https://github.com/NeuralNotwerk/standard_model_for_jev_tasks/blob/f63fb177a1ca7e7508ff83d429f59d9438346842/scripts/run_jevbench.sh) runs JevBench's stock `typesafe` adapter against the shim.

## Get started

Install, start a backend, then the shim:

```sh
git clone https://github.com/NeuralNotwerk/standard_model_for_jev_tasks.git && cd standard_model_for_jev_tasks
pip install -e .
vllm serve <model> --port 8000 --enable-prefix-caching \
  --structured-outputs-config '{"backend": "xgrammar", "disable_any_whitespace": true}'
jev-shim --help   # then point a Jev client at the shim's /v1/systemone
```

No TypeSafe usage; compute costs are your own hardware or hosting.

## Examples and demos

- JevBench results and caveats: [`docs/RESULTS.md`](https://github.com/NeuralNotwerk/standard_model_for_jev_tasks/blob/f63fb177a1ca7e7508ff83d429f59d9438346842/docs/RESULTS.md) (maintainer-measured; e.g. Qwen3.8-Flash-Next on 4× RTX 5090 vs the public Jev 1.13.0 board).
- README *Benchmark with JevBench* commands.

## Limits and data handling

Upstream states it is not affiliated with or endorsed by TypeSafe AI or JevBench; "Jev" describes interface compatibility only. Benchmark numbers are the maintainer's. Data stays on your backend. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit f63fb177a1ca](https://github.com/NeuralNotwerk/standard_model_for_jev_tasks/tree/f63fb177a1ca7e7508ff83d429f59d9438346842). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
