# Paved Gate (fast Jev ingestion gate that blocks, answers or passes requests before a frontier model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python gate that sits in front of AI agents: it masks PII, asks Jev three typed questions about each request (intent, risk and sensitive data) in one round trip, and then blocks it, answers it with a deterministic handler or passes it to a frontier agent, writing an audit record with the raw scores and policy hash.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SoniaMehta14/paved-gate) |
| Maintainer | [SoniaMehta14](https://github.com/SoniaMehta14). Independently curated. |
| Format | Python library and FastAPI demo server (Apache-2.0) |
| Requirements | Python with uv; a TypeSafe key for live Jev calls (a contract-accurate mock runs without keys); optional Anthropic, OpenAI or Gemini keys for downstream agents. |
| License | [Apache-2.0](https://github.com/SoniaMehta14/paved-gate/blob/9c741fc0be6fa51e0ac7bcd9dfcb469eac0b9a21/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/paved_gate/evaluator/jev.py`](https://github.com/SoniaMehta14/paved-gate/blob/9c741fc0be6fa51e0ac7bcd9dfcb469eac0b9a21/src/paved_gate/evaluator/jev.py) at the pinned commit. |

## When to use

- Stop unsafe or unnecessary requests before they reach an expensive model.
- Answer simple requests with code and keep an audit trail of every decision.
- Mismatch: alpha; benchmark numbers are the author's own.

## How it works

`src/paved_gate/evaluator/jev.py` implements the FastEvaluator protocol against `https://api.typesafe.ai/v1`, sending Choice, Score and Noul questions in one request; policy-as-code YAML maps the answers to block, handle or pass. The author reports 144 live Jev requests across four benchmark runs on 2026-09-27; a Gemini Decisions evaluator is also included. Integration evidence: [`src/paved_gate/evaluator/jev.py`](https://github.com/SoniaMehta14/paved-gate/blob/9c741fc0be6fa51e0ac7bcd9dfcb469eac0b9a21/src/paved_gate/evaluator/jev.py).

## Get started

Install with uv, run the tests, and start the demo server with Jev in mock mode (no keys needed).

```sh
uv sync --all-extras
uv run python examples/server.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Policy example: [github.com/SoniaMehta14/paved-gate/blob/9c741fc0be6fa51e0ac7bcd9dfcb469eac0b9a21/policy/paved_gate.policy.yaml](https://github.com/SoniaMehta14/paved-gate/blob/9c741fc0be6fa51e0ac7bcd9dfcb469eac0b9a21/policy/paved_gate.policy.yaml)

## Limits and data handling

Requests are PII-masked before going to TypeSafe on your key; audit logs are written locally as JSONL.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 9c741fc0be6f](https://github.com/SoniaMehta14/paved-gate/tree/9c741fc0be6fa51e0ac7bcd9dfcb469eac0b9a21). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
