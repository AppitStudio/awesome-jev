# OntologyJev (see which agent decisions change when a policy changes, with Jev as an optional semantic judge)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A Python SDK and local browser workbench that connects explicit object relationships, semantic judgments and business rules for agent decisions: change a policy (the demo compares a 7-day and a 14-day refund window across 20 cases), see which outcomes change, and save the decisions to preserve. Jev or a local Ollama model can supply the semantic observations.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Q-17/ontologyjev) |
| Maintainer | [Q-17](https://github.com/Q-17). Independently curated. |
| Format | Python SDK + local workbench |
| Requirements | Python 3.8+; no key needed for the fixture demo. A TypeSafe key (server-side) for live Jev observations, or a local Ollama model. |
| License | [MIT](https://github.com/Q-17/ontologyjev/blob/daaf89a0071b499236eaace588a15099f5472a2e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ontology_jev/providers.py`](https://github.com/Q-17/ontologyjev/blob/daaf89a0071b499236eaace588a15099f5472a2e/ontology_jev/providers.py) at the pinned commit. |

## When to use

- Check how a policy change would flip an agent's decisions before shipping it, with Jev reading the semantic part.
- Mismatch: an agent runtime; the demo proposes actions and never executes them.

## How it works

`ontology_jev/providers.py` posts to `/v1/systemone` with the key from `TYPESAFE_API_KEY`, kept server-side; the SDK does not assume a provider's scores are calibrated, and rule traces show how each observation fed the decision. Integration evidence: [`ontology_jev/providers.py`](https://github.com/Q-17/ontologyjev/blob/daaf89a0071b499236eaace588a15099f5472a2e/ontology_jev/providers.py).

## Get started

Start the workbench from a checkout; try Jev from the UI once a key is set.

```sh
git clone https://github.com/Q-17/ontologyjev
cd ontologyjev
python -m ontology_jev serve   # http://127.0.0.1:8765
# for live Jev observations: export TYPESAFE_API_KEY=... before serving
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Q-17/ontologyjev/blob/daaf89a0071b499236eaace588a15099f5472a2e/README.md](https://github.com/Q-17/ontologyjev/blob/daaf89a0071b499236eaace588a15099f5472a2e/README.md)
- Architecture: [github.com/Q-17/ontologyjev/blob/daaf89a0071b499236eaace588a15099f5472a2e/docs/architecture.md](https://github.com/Q-17/ontologyjev/blob/daaf89a0071b499236eaace588a15099f5472a2e/docs/architecture.md)

## Limits and data handling

The demo's probabilities are hand-authored fixtures and say nothing about Jev performance. Live mode sends the case text to TypeSafe.

## Review and maintenance

Reviewed **2026-11-21** (Europe/Sofia) at [commit daaf89a0071b](https://github.com/Q-17/ontologyjev/tree/daaf89a0071b499236eaace588a15099f5472a2e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
