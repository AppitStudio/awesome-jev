# jev-guardrail-benchmark

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark of TypeSafe Jev content-safety guardrails in WSO2 AI Gateway vs Azure Content Safety and an LLM judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/randilt/jev-guardrail-benchmark) |
| Maintainer | [randilt](https://github.com/randilt). Independently curated. |
| Format | Guardrail benchmark suite + AgentDojo agent run (Apache-2.0) |
| Requirements | See upstream README; TypeSafe/OpenRouter/provider keys when using hosted Jev paths. |
| License | [Apache-2.0](https://github.com/randilt/jev-guardrail-benchmark/blob/2d24a5f331e1d19fa22a24959eaffa0c51cc5eaf/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when benchmark of TypeSafe Jev content-safety guardrails in WSO2 AI Gateway vs Azure Content Safety and an LLM judge. Prefer related catalog tools when another listing better matches your stack.

## How it works

Harness sends the same labelled prompts through Jev/Azure/LLM-judge policies and records accuracy, latency, and cost.

## Get started

```sh
git clone https://github.com/randilt/jev-guardrail-benchmark.git
cd jev-guardrail-benchmark
git checkout 2d24a5f331e1d19fa22a24959eaffa0c51cc5eaf
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit 2d24a5f331e1](https://github.com/randilt/jev-guardrail-benchmark/tree/2d24a5f331e1d19fa22a24959eaffa0c51cc5eaf). AI-assisted README and license inspection; install/live paths not executed.
