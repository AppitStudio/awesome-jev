# jev-guardrails (deepansh-saxena)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Research/eval repo that runs the same mock carrier support agent and 25 behavioural guardrail rules behind two backends—chat-model JSON judge vs TypeSafe Jev typed questions—so latency, cost, and coverage can be compared.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/deepansh-saxena/jev-guardrails) |
| Maintainer | [deepansh-saxena](https://github.com/deepansh-saxena). Independently curated. |
| Format | Python eval/demo (LangChain/LangGraph) with offline tests. |
| Requirements | Python 3.11+; provider keys for live arms. |
| License | No LICENSE file at the reviewed tip—reuse terms unspecified. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream accuracy/cost tables not independently reproduced. Confirm redistribution rights before shipping derived work. |

## When to use

Use to **study** Jev vs LLM-as-judge guardrails on a fixed rule set. Prefer production firewalls ([agent-chaperone](agent-chaperone.md), [jev-guard](jev-guard.md)) when you need a shippable product rather than an A/B harness.

## How it works

One interface swaps `llm` vs `jev` backends. Soft rules live in prompts for the LLM arm and as typed questions for Jev. Offline tests and labelled cases live under `tests/` and `evals/`.

## Get started

```sh
git clone https://github.com/deepansh-saxena/jev-guardrails.git
cd jev-guardrails
git checkout 6514f76535feebb0e093d3dd01dcd22ac12c3a48
pip install -r requirements.txt
# offline tests per README; live compare needs provider keys
```

## Examples and demos

- `tests/test_offline.py` (upstream badge claims 63 passing—not re-run here).
- `GUARDRAILS.md` / `SCENARIOS.md`.

## Limits and data handling

No project LICENSE at tip. Live evals spend provider budget. Do not treat upstream tables as Awesome Jev measured results.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 6514f76](https://github.com/deepansh-saxena/jev-guardrails/tree/6514f76535feebb0e093d3dd01dcd22ac12c3a48). AI-assisted README and source inspection; live provider calls not run on the review host.

Related: [jev-guardbench (dfranco-projects)](dfranco-projects-jev-guardbench.md), [Juardrails](juardrails.md), [agent-chaperone](agent-chaperone.md).
