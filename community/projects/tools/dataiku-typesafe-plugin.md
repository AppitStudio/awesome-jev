# Dataiku TypeSafe AI plugin

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Dataiku's DSS plugin that brings TypeSafe Jev into the LLM Mesh: a `Jev Question Set` block for Structured Visual Agents, a yes/no Jev guardrail, a Jev reranker and a Jev chat-completion model usable in prompt and Classify text recipes, with usage, cost and traces recorded by the Mesh.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dataiku/dss-plugin-typesafe-ai) |
| Maintainer | [Dataiku](https://github.com/dataiku) (Dataiku SAS). Independently curated; no affiliation. |
| Format | Dataiku DSS plugin (`plugin.json` 1.0.0 at review) |
| Requirements | Dataiku DSS with LLM Mesh; a TypeSafe API key preset; a Custom LLM connection `typesafe` with `jev` (Chat completion) and `jev-reranker` (Reranking) models. Only dependency: `requests` from the built-in environment. |
| License | [Apache-2.0](https://github.com/dataiku/dss-plugin-typesafe-ai/blob/b33b22c097ad7719ea2a35e263e66564b7b098b5/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Ask several typed questions about one input in a Structured Visual Agent and store each answer in agent state.
- Block or audit LLM calls with a Jev yes/no guardrail on the prompt or response, or rerank retrieved documents by answer probability.
- Mismatch: requires a Dataiku DSS instance; data leaves DSS for the TypeSafe API.

## How it works

[`python-lib/typesafe_jev/client.py`](https://github.com/dataiku/dss-plugin-typesafe-ai/blob/b33b22c097ad7719ea2a35e263e66564b7b098b5/python-lib/typesafe_jev/client.py) calls TypeSafe with retries (4 attempts on connection errors, 429 and 5xx, honoring `retry-after`; no timeout retries); [`mesh.py`](https://github.com/dataiku/dss-plugin-typesafe-ai/blob/b33b22c097ad7719ea2a35e263e66564b7b098b5/python-lib/typesafe_jev/mesh.py) and [`blocks.py`](https://github.com/dataiku/dss-plugin-typesafe-ai/blob/b33b22c097ad7719ea2a35e263e66564b7b098b5/python-lib/typesafe_jev/blocks.py) expose the LLM Mesh models and agent block; the guardrail lives in [`python-guardrails/jev-guardrail`](https://github.com/dataiku/dss-plugin-typesafe-ai/tree/b33b22c097ad7719ea2a35e263e66564b7b098b5/python-guardrails/jev-guardrail). Jev version defaults to `jev-latest`; the README recommends pinning (e.g. `jev-1.13.0`) after tuning thresholds.

## Get started

Install from Git in DSS and wire the connection:

```sh
# DSS: Plugins > Add Plugin > From Git repository > https://github.com/dataiku/dss-plugin-typesafe-ai
#   (or: make plugin  → upload dist/dss-plugin-typesafe-ai-<version>.zip)
# Plugins > TypeSafe AI > Settings: add a TypeSafe API key preset
# Administration > Connections: Custom LLM 'typesafe' with models 'jev' and 'jev-reranker'
```

Jev calls are billed by TypeSafe; set *Cost per million input tokens* so LLM Mesh reports cost.

## Examples and demos

- README *Usage* sections: Structured Visual Agent `Jev Question Set`, guardrail, reranker, prompt recipes and Classify text recipe.
- [CHANGELOG](https://github.com/dataiku/dss-plugin-typesafe-ai/blob/b33b22c097ad7719ea2a35e263e66564b7b098b5/CHANGELOG.md) for release history.

## Limits and data handling

Inputs and questions are sent to the TypeSafe API outside your DSS instance; evaluate thresholds on your own data (upstream data-handling note). Not installed on the review host (no DSS instance).

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit b33b22c097ad](https://github.com/dataiku/dss-plugin-typesafe-ai/tree/b33b22c097ad7719ea2a35e263e66564b7b098b5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
