# JarvisCore

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Python multi-agent runtime (peer-to-peer mesh, durable state, integration atoms) with a `typesafe` extra that injects a shared Jev client as `self.decisions` and can route subagents, task complexity and RAG passages with Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Prescott-Data/jarviscore-framework) |
| Product homepage | [jarviscore.developers.prescottdata.io](https://jarviscore.developers.prescottdata.io/) |
| Maintainer | [Prescott-Data](https://github.com/Prescott-Data). Independently curated. |
| Format | Python framework/library with CLI (`jarviscore`) and examples |
| Requirements | Python and `pip install "jarviscore-framework[typesafe]"`; `TYPESAFE_API_KEY`. Distributed features need Redis; generative planning uses your LLM provider. |
| License | [Apache-2.0](https://github.com/Prescott-Data/jarviscore-framework/blob/678c2eb9275b91e89f73be1aa9f07df472e250f6/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Route tickets or tasks to the right agent with a typed choice instead of an LLM prompt.
- Classify a FAISS shortlist into accepted, conflicting and excluded passages before generation (`RAG_DECISION_PROVIDER=typesafe`).
- Mismatch: Jev complements the generative model for planning and execution; it does not replace it.

## How it works

With the extra installed and a key set, the Mesh creates one async decision client and injects it into agents as `self.decisions`; AutoAgents also get an `evaluate_decisions` thinking tool. Environment switches opt specific kernel decisions into Jev, while explicit planner, profile and execution-contract roles keep precedence ([README: TypeSafe Jev Decision Models](https://github.com/Prescott-Data/jarviscore-framework/blob/678c2eb9275b91e89f73be1aa9f07df472e250f6/README.md)).

## Get started

Install the extra, validate one round-trip, and run the decision demo (live Jev calls):

```sh
pip install "jarviscore-framework[typesafe]"
export TYPESAFE_API_KEY=...
jarviscore check --validate-typesafe
python examples/typesafe_jev_decisions.py   # from a clone of the repo
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- `examples/typesafe_jev_decisions.py` (Choice, Score and Noul with no Redis or LLM key) and the [Decision Models docs](https://jarviscore.developers.prescottdata.io/concepts/decision-models/).

## Limits and data handling

Decision calls send the given state to TypeSafe and incur charges. Routing switches are opt-in. The wider framework's production claims were not evaluated here.

## Review and maintenance

Reviewed **2026-10-05** (Europe/Sofia) at [commit 678c2eb9275b](https://github.com/Prescott-Data/jarviscore-framework/tree/678c2eb9275b91e89f73be1aa9f07df472e250f6). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
