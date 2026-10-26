# decision-agent-lab (measured tool routing and command gating with Jev and other decision models)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Korean-language lab that measures the "LLM generates, decision model judges, code executes" pattern: Jev, OpenAI Decisions, Upstage Solar Decide and local Ollama models are called through one interface on a 40-request tool-routing task and a 1,007-command allow/ask/deny gate, with every call's model version, latency, tokens and cost logged.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Daewooki/decision-agent-lab) |
| Maintainer | [Daewooki](https://github.com/Daewooki). Independently curated. |
| Format | Python research code (uv) with committed summaries |
| Requirements | Python with uv; a TypeSafe API key (optional OpenRouter, OpenAI, Upstage or Ollama backends); unit tests run offline. |
| License | [MIT](https://github.com/Daewooki/decision-agent-lab/blob/bfacde52e58f2ee092f19584a8f5ea2643d9744e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/dalab/backends/systemone.py`](https://github.com/Daewooki/decision-agent-lab/blob/bfacde52e58f2ee092f19584a8f5ea2643d9744e/src/dalab/backends/systemone.py) at the pinned commit. |

## When to use

- Compare Jev with other decision models and LLM structured output for tool routing on your own requests.
- Prototype a layered command gate where code rules run before any model question.
- Mismatch: single-location measurements; numbers are the author's.

## How it works

`src/dalab/backends/systemone.py` implements System One backends for TypeSafe (`https://api.typesafe.ai/v1/systemone`, `jev-1.13.0` and `jev-1.14.0`), OpenRouter, Upstage and Ollama, plus an optional jevstation.com relay; each response is recorded with model version and cost. Integration evidence: [`src/dalab/backends/systemone.py`](https://github.com/Daewooki/decision-agent-lab/blob/bfacde52e58f2ee092f19584a8f5ea2643d9744e/src/dalab/backends/systemone.py).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # add TYPESAFE_API_KEY
uv sync --all-extras
uv run pytest                      # offline unit tests
uv run python scripts/smoke.py     # one call per configured backend
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Daewooki/decision-agent-lab#readme](https://github.com/Daewooki/decision-agent-lab#readme)

## Limits and data handling

Benchmark requests and commands go to each configured provider. The optional jevstation.com relay is a third-party service, not TypeSafe; leave its key empty to call TypeSafe directly. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit bfacde52e58f](https://github.com/Daewooki/decision-agent-lab/tree/bfacde52e58f2ee092f19584a8f5ea2643d9744e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
