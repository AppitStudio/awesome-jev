# Banking customer service agent by Ashwin Sayenju (multi-agent bank support where Jev gates every request before it acts)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A typed multi-agent customer service system on tau2-bench's `banking_knowledge` domain: an LLM splits a message into typed requests, Jev scores whether each was read correctly and is in scope, code checks identity and missing details, and each request is run, clarified, planned for a yes, or handed to a person. The README documents what Jev sees, what it is trusted with, and a small evaluation.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asayenju/banking_customer_service_agent) |
| Maintainer | [asayenju](https://github.com/asayenju). Independently curated. |
| Format | Python (FastAPI) backend + demo web page |
| Requirements | Python 3.12 with uv, the tau2-bench submodule, an OpenAI key and a TypeSafe key (`JEV_KEY`) for the live demo; the tests run offline with no keys. |
| License | no license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/The56hjkl/status/2124002595068850609)). |
| Jev evidence | [`backend/src/orchestrator/jev.py`](https://github.com/asayenju/banking_customer_service_agent/blob/e19a6c5d5db705a7abade13c4c279764b164f604/backend/src/orchestrator/jev.py) at the pinned commit. |

## When to use

- Study a worked example of putting Jev as the act/ask/escalate gate in a customer service agent, with the trust boundary spelled out.
- Mismatch: a production banking assistant; this is a portfolio project on a benchmark domain.

## How it works

`backend/src/orchestrator/jev.py` is the per-intent scorer: two yes/no questions per request (is the kind right, is it something bank customer service handles), sent with the redacted message, the decomposer's reading, the assistant's capabilities and recent context, never slot values. Confidence is the weakest of Jev's two scores and a code check on missing details; the model is pinned to `jev-1.13.0`, and injection-flagged messages are not sent at all. Integration evidence: [`backend/src/orchestrator/jev.py`](https://github.com/asayenju/banking_customer_service_agent/blob/e19a6c5d5db705a7abade13c4c279764b164f604/backend/src/orchestrator/jev.py).

## Get started

Clone with submodules, run the offline tests, then start the demo with your keys in `.env`.

```sh
git clone --recurse-submodules https://github.com/asayenju/banking_customer_service_agent.git
cd banking_customer_service_agent/backend
uv sync && uv run pytest   # offline
PYTHONPATH=src:../tau2-bench/src uv run uvicorn main:app --port 8765
# open http://localhost:8765/demo (needs OPENAI_KEY and JEV_KEY in the repo-root .env)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Where Jev is included (README): [github.com/asayenju/banking_customer_service_agent/blob/e19a6c5d5db705a7abade13c4c279764b164f604/README.md](https://github.com/asayenju/banking_customer_service_agent/blob/e19a6c5d5db705a7abade13c4c279764b164f604/README.md)
- Launch post on X: [x.com/The56hjkl/status/2124002595068850609](https://x.com/The56hjkl/status/2124002595068850609)

## Limits and data handling

The redacted customer message and conversation context go to TypeSafe (and to OpenAI for decomposition and replies). The README's evaluation is a small sample (30/40 cases) and was not reproduced here. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit e19a6c5d5db7](https://github.com/asayenju/banking_customer_service_agent/tree/e19a6c5d5db705a7abade13c4c279764b164f604). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
