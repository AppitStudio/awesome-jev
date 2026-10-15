# jev-context-filter-harness

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Paper code and run records for screening LLM agents' tool output with Jev: a relevance filter keeps chunks that answer the agent's question and an injection filter withholds planted instructions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zacharytgray/jev-context-filter-harness) |
| Maintainer | [zacharytgray](https://github.com/zacharytgray). Independently curated. |
| Format | Python research harness (`uv`) with experiment data |
| Requirements | Python + `uv`; TypeSafe key and an LLM provider for live runs (tests use fakes). |
| License | [MIT](https://github.com/zacharytgray/jev-context-filter-harness/blob/d693c5fa2a89d4447fc91b5c0c1e6aa9ff1e122b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`s1harness/jev.py`](https://github.com/zacharytgray/jev-context-filter-harness/blob/d693c5fa2a89d4447fc91b5c0c1e6aa9ff1e122b/s1harness/jev.py) at the pinned commit. |

## When to use

- Reproduce tool-output screening results on ContextBench, LegalBench-RAG, DocFinQA and AgentDojo.
- Reuse the filter design in your own agent loop.
- Mismatch: paper under double-blind review; results are the authors' and were not reproduced here.

## How it works

Between the agent's tools and the agent, each chunk of tool output gets typed questions to Jev (`jev-latest` via `api.typesafe.ai/v1/systemone`): relevance to the agent's own question, and whether a line tries to assign an unrequested task. Integration evidence: [`s1harness/jev.py`](https://github.com/zacharytgray/jev-context-filter-harness/blob/d693c5fa2a89d4447fc91b5c0c1e6aa9ff1e122b/s1harness/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync
uv run pytest -q   # offline: fake LLM and fake Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results: `experiments/main/RESULTS.md`, `experiments/agentdojo/RESULTS.md`.

## Limits and data handling

Tool outputs go to TypeSafe and agent prompts to the LLM provider you configure, on your keys.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit d693c5fa2a89](https://github.com/zacharytgray/jev-context-filter-harness/tree/d693c5fa2a89d4447fc91b5c0c1e6aa9ff1e122b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
