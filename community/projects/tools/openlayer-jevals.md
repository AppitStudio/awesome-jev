# jevals (Openlayer)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Evals and guardrails for agent traces (tool choice, grounding, relevancy, completeness, indirect injection, PHI) sent to Jev-style decision models as one request instead of an LLM judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/openlayer-ai/jevals) |
| Maintainer | [openlayer-ai](https://github.com/openlayer-ai). Independently curated. |
| Format | Python library (PyPI `jevals`) |
| Requirements | Python; a TypeSafe, Vercel AI Gateway or OpenRouter key (or a local decision model). |
| License | [MIT](https://github.com/openlayer-ai/jevals/blob/47095b2509e9ff046bb03f88e2c113b3ad99a3da/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/_vMyth/status/2110581433601507836)). |
| Jev evidence | [`src/jevals/backends/typesafe.py`](https://github.com/openlayer-ai/jevals/blob/47095b2509e9ff046bb03f88e2c113b3ad99a3da/src/jevals/backends/typesafe.py) at the pinned commit. |

## When to use

- Score every production trace, or gate inside the agent loop, when an LLM judge is too slow or costly.
- Swap between Jev (TypeSafe or Vercel), OpenRouter decision models and local Kev/Laya with one API.
- Mismatch: distinct from the already-listed dayhaysoos/jevals workbench; cost and latency figures are the author's.

## How it works

`evaluate()` turns a chat trace and tool schemas into typed questions for each requested metric and sends them in one decision-model request; results come back as answers with probabilities and scores. Backends cover TypeSafe, Vercel AI Gateway, OpenRouter and local models. Integration evidence: [`src/jevals/backends/typesafe.py`](https://github.com/openlayer-ai/jevals/blob/47095b2509e9ff046bb03f88e2c113b3ad99a3da/src/jevals/backends/typesafe.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install jevals
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Quickstart trace: `examples/quickstart.py`.
- Support-agent gating example: `examples/support_agent_gates.py`.

## Limits and data handling

Trace contents (messages, tool calls and results) go to the backend you configure and are billed to that key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 47095b2509e9](https://github.com/openlayer-ai/jevals/tree/47095b2509e9ff046bb03f88e2c113b3ad99a3da). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
