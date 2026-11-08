# Swarms (multi-agent orchestration framework with a DecisionModel struct for TypeSafe Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Enterprise multi-agent framework whose `DecisionModel` struct wraps TypeSafe Jev for routing, referees, guards and ensemble judges, with runnable examples.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kyegomez/swarms) |
| Maintainer | [kyegomez](https://github.com/kyegomez). Independently curated. |
| Format | Python framework (Apache-2.0) |
| Requirements | Python, `pip install swarms`, and a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/kyegomez/swarms/blob/d46ee9ab3f5ccd44af4975e57e3ade88c1de73fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`swarms/structs/decision_model.py`](https://github.com/kyegomez/swarms/blob/d46ee9ab3f5ccd44af4975e57e3ade88c1de73fc/swarms/structs/decision_model.py) at the pinned commit. |

## When to use

- Route tasks between agents with a typed Jev decision.
- Add a Jev referee or guard to group chats.
- Mismatch: generation still runs on your LLM agents.

## How it works

`DecisionModel(model_name="jev-latest")` reads `TYPESAFE_API_KEY` and is used in `examples/decision_models/` as an agent router, debate referee, guarded group chat and screening funnel. Integration evidence: [`swarms/structs/decision_model.py`](https://github.com/kyegomez/swarms/blob/d46ee9ab3f5ccd44af4975e57e3ade88c1de73fc/swarms/structs/decision_model.py).

## Get started

Install Swarms and run one of the `examples/decision_models/` scripts with your key.

```sh
git clone https://github.com/kyegomez/swarms.git && cd swarms
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- examples/decision_models/: [github.com/kyegomez/swarms/tree/d46ee9ab3f5ccd44af4975e57e3ade88c1de73fc/examples/decision_models](https://github.com/kyegomez/swarms/tree/d46ee9ab3f5ccd44af4975e57e3ade88c1de73fc/examples/decision_models)

## Limits and data handling

Agent state and candidate options are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit d46ee9ab3f5c](https://github.com/kyegomez/swarms/tree/d46ee9ab3f5ccd44af4975e57e3ade88c1de73fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
