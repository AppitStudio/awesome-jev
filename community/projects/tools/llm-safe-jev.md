# Jev as an LLM Safety Guardrail (USC study: Jev as input filter and selective output reviewer for a small LLM)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Reproducibility code and data for a USC paper testing Jev as a guardrail around a Qwen2.5-1.5B pipeline on 970 AdvBench and XSTest prompts: the LLM alone, a Jev input gate, and a selective setup that blocks clearly harmful requests, passes clearly safe ones and reviews the answers in between. Reports how many harmful prompts got answers and how many safe ones were refused, with threshold sweeps rebuilt from cached Jev scores.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ANRGUSC/llm-safe-jev) |
| Maintainer | [ANRGUSC](https://github.com/ANRGUSC). Independently curated. |
| Format | Python analysis code, notebook and cached results |
| Requirements | Python 3.10+; reproducing the tables needs no API key (a TypeSafe key only to rerun Jev calls). |
| License | [BSD-3-Clause](https://github.com/ANRGUSC/llm-safe-jev/blob/16e5f510b3a9cf77a57512d8f2e9383325683a74/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_repro/protocol.py`](https://github.com/ANRGUSC/llm-safe-jev/blob/16e5f510b3a9cf77a57512d8f2e9383325683a74/src/jev_repro/protocol.py) at the pinned commit. |

## When to use

- Pick thresholds for a Jev safety gate using published numbers instead of guesses.
- Mismatch: one small LLM and two benchmarks; the authors call the tuned thresholds exploratory.

## How it works

`src/jev_repro/protocol.py` records the exact request: one `noul` harmfulness question to `https://api.typesafe.ai/v1/systemone` with `jev-latest`, for the input gate and the output review. Integration evidence: [`src/jev_repro/protocol.py`](https://github.com/ANRGUSC/llm-safe-jev/blob/16e5f510b3a9cf77a57512d8f2e9383325683a74/src/jev_repro/protocol.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ANRGUSC/llm-safe-jev && cd llm-safe-jev
python -m venv .venv && source .venv/bin/activate
pip install -r requirements-analysis.txt
python scripts/reproduce.py   # rebuilds tables and figures from cached scores
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/ANRGUSC/llm-safe-jev#readme](https://github.com/ANRGUSC/llm-safe-jev#readme)

## Limits and data handling

Benchmark prompts include harmful requests. A delivered answer to a harmful prompt is counted as a non-refusal, not a verified harmful completion.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 16e5f510b3a9](https://github.com/ANRGUSC/llm-safe-jev/tree/16e5f510b3a9cf77a57512d8f2e9383325683a74). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
