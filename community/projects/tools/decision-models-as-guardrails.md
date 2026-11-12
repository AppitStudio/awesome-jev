# decision-models-as-guardrails (open benchmark asking whether Jev and other decision models can replace a managed guardrail)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open benchmark by raxIT Labs that sends the same labelled rows to decision models (Jev 1.13 and 1.14, Kev, Open-Jev, Laya, Clef, Strands Decider), the Perplexity and OpenAI Decisions APIs and Bedrock Guardrails across six guardrail suites, and compares balanced accuracy and cost.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/raxITlabs/decision-models-as-guardrails) |
| Maintainer | [raxITlabs](https://github.com/raxITlabs). Independently curated. |
| Format | Python benchmark with a Hugging Face dataset and results site (Apache-2.0) |
| Requirements | Python with `uv`; free steps need no accounts, while reruns need a TypeSafe key (about USD 0.38 per Jev version per the README) and other provider accounts or GPUs. |
| License | [Apache-2.0](https://github.com/raxITlabs/decision-models-as-guardrails/blob/5a12b8efae18bdf080e8c8e76dc362e9ece97f35/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`benchmark/goldrails_bench/systemone.py`](https://github.com/raxITlabs/decision-models-as-guardrails/blob/5a12b8efae18bdf080e8c8e76dc362e9ece97f35/benchmark/goldrails_bench/systemone.py) at the pinned commit. |

## When to use

- Decide whether Jev could stand in for a managed guardrail on content, prompt-attack, topic, PII or grounding checks.
- Mismatch: a guardrail you can deploy; this is a benchmark, and its board includes an unpublished held-back slice.

## How it works

`benchmark/goldrails_bench/systemone.py` and the `noul` adapter send each row as a yes/no System One question to `https://api.typesafe.ai/v1/systemone`; 0.5 or more counts as yes with no per-model tuning, scored by balanced accuracy with bootstrap intervals. `REPRODUCE.md` lists each paid step and cost; part of the test split is held back and unpublished. Integration evidence: [`benchmark/goldrails_bench/systemone.py`](https://github.com/raxITlabs/decision-models-as-guardrails/blob/5a12b8efae18bdf080e8c8e76dc362e9ece97f35/benchmark/goldrails_bench/systemone.py).

## Get started

Clone, run the free steps in `REPRODUCE.md` first, and only then decide whether to spend on paid reruns.

```sh
git clone https://github.com/raxITlabs/decision-models-as-guardrails.git && cd decision-models-as-guardrails
uv sync
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/raxITlabs/decision-models-as-guardrails/blob/5a12b8efae18bdf080e8c8e76dc362e9ece97f35/README.md](https://github.com/raxITlabs/decision-models-as-guardrails/blob/5a12b8efae18bdf080e8c8e76dc362e9ece97f35/README.md)
- Results site: [dm-as-guardrails.raxitlabs.com](https://dm-as-guardrails.raxitlabs.com)
- Dataset: [huggingface.co/datasets/raxITLabs/decision-models-as-guardrails](https://huggingface.co/datasets/raxITLabs/decision-models-as-guardrails)

## Limits and data handling

Benchmark rows go to each provider you run; Jev reruns go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 5a12b8efae18](https://github.com/raxITlabs/decision-models-as-guardrails/tree/5a12b8efae18bdf080e8c8e76dc362e9ece97f35). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
