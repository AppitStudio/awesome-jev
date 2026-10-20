# Harness² (recursive agent harnessing)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Python framework that improves an agent's harness (prompts, guardrails, memory, tools, skills, scripts) task by task while the model weights stay fixed, with OpenCode and Codex executors, three professional benchmarks, and optional Jev selection of the best final output when it runs k > 1 candidates.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SASUKE40/harness2) |
| Maintainer | [SASUKE40](https://github.com/SASUKE40). Independently curated. |
| Format | Python package and CLI (uv, Python 3.12) with benchmark runners and a web dashboard |
| Requirements | Linux, Python 3.12 and uv for the offline demo; Node.js 20+, Google Cloud CLI and Vertex AI models for benchmarks; `.[jev]` extra and a TypeSafe key for Jev selection. |
| License | [Apache-2.0](https://github.com/SASUKE40/harness2/blob/993c5337b889a6f8f3585fdb57043ca7bc9dade9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/edward40e/status/2112327768180703610)). |
| Jev evidence | [`harness2/core/jev.py`](https://github.com/SASUKE40/harness2/blob/993c5337b889a6f8f3585fdb57043ca7bc9dade9/harness2/core/jev.py) at the pinned commit. |

## When to use

- Try task-level harness refinement (propose, probe, compose) on JobBench, LAB or WorkBuddy-Bench without retraining a model.
- Let Jev pick between several finished candidate outputs instead of a generative judge.
- Mismatch: research framework; model-backed benchmark runs cost money and need cloud setup.

## How it works

Harness² runs a task, proposes edits to eight harness components, probes their effect on the same task, and composes a refined harness from the contrasts; lessons persist in an improvement harness for later tasks. With `HARNESS2_SELECTOR=jev`, `harness2/core/jev.py` uses the TypeSafe SDK to ask Jev which of the k final outputs to keep; the executor, editors and benchmark judges keep their own models. When outputs are equally good, Jev defers to the deterministic selector. Integration evidence: [`harness2/core/jev.py`](https://github.com/SASUKE40/harness2/blob/993c5337b889a6f8f3585fdb57043ca7bc9dade9/harness2/core/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv venv --python 3.12 .venv && source .venv/bin/activate
uv pip install -e '.[render,jev]'
harness2-demo --output runs/demo --k 2        # offline, no credentials
export TYPESAFE_API_KEY=... HARNESS2_SELECTOR=jev
harness2-demo --output runs/demo-jev --k 2    # only Jev makes paid calls
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author's X post (aircraft recognition 49% to 63% in three rounds with Jev): [x.com/edward40e/status/2112327768180703610](https://x.com/edward40e/status/2112327768180703610)
- docs/SETUP.md#jev-selection and docs/EXPERIMENTS.md

## Limits and data handling

Benchmark gains in the README are the authors' results with GLM-5 and Gemini 3.5 Flash; Jev is only the optional output selector and was not run here. Candidate outputs are sent to TypeSafe when Jev selection is on.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit 993c5337b889](https://github.com/SASUKE40/harness2/tree/993c5337b889a6f8f3585fdb57043ca7bc9dade9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
