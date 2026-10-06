# FAVA Trails

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Git-native, versioned memory for AI agents via MCP (Machine Wisdom AI): drafts are isolated, and since 0.8 the default Trust Gate asks TypeSafe Jev through OpenRouter one typed Noul question with an explicit threshold before a memory is promoted to shared truth.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MachineWisdomAI/fava-trails) |
| Product homepage | [fava-trails.org](https://fava-trails.org) |
| Maintainer | [MachineWisdomAI](https://github.com/MachineWisdomAI). Independently curated. |
| Format | MCP server + CLI (PyPI `fava-trails`, 0.8.0 at review) |
| Requirements | Python; Jujutsu (JJ) ≥ 0.28 (`fava-trails install-jj`); `OPENROUTER_API_KEY` for the default `decisions` Trust Gate. |
| License | [Apache-2.0](https://github.com/MachineWisdomAI/fava-trails/blob/5153b7625cf2a9f62b9ae68a5f061a7da5940ba0/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Share reviewed decisions across agent sessions and environments with history in your own Git repo.
- Add a cheap approval step before agents' memories are inherited by other agents.
- Mismatch: the gate is process control with limited context, not fact verification (upstream statement).

## How it works

Agents save drafts and call `propose_truth`; under the default `decisions` policy [`trust_gate.py`](https://github.com/MachineWisdomAI/fava-trails/blob/5153b7625cf2a9f62b9ae68a5f061a7da5940ba0/src/fava_trails/trust_gate.py) sends the candidate and memory policy to OpenRouter Decisions (`~typesafe/jev-latest`) as one Noul question; FAVA applies the threshold, records model and probability, and promotes or rejects. `llm-oneshot` and human approval remain alternatives.

## Get started

Install from PyPI and set up JJ (live Trust Gate calls go to OpenRouter):

```sh
pip install fava-trails
fava-trails install-jj
export OPENROUTER_API_KEY=...
fava-trails doctor     # shows the effective destination/model
```

Each promotion under `decisions` is one OpenRouter request billed to your key.

## Examples and demos

- [Two-agent case study](https://fava-trails.org/case-study/) (upstream).
- v0.8.0 release notes with calibration details.

## Limits and data handling

Under `decisions`, the prompt, candidate content and selected metadata leave the process before a verdict (upstream). A convincing false claim can still be approved. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit 5153b7625cf2](https://github.com/MachineWisdomAI/fava-trails/tree/5153b7625cf2a9f62b9ae68a5f061a7da5940ba0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
