# JEV AgentNetwork

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Event-driven multi-agent network where TypeSafe Jev observes live network state and assigns pending work to idle general-purpose agents each time one finishes (reference `AgentRouter`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Kelly-Leeee/AgentNetwork-jev) |
| Maintainer | [Kelly-Leeee](https://github.com/Kelly-Leeee). Independently curated. |
| Format | Python package (`agentrouter`) + frontend |
| Requirements | Python (uv); TypeSafe key; agent CLIs per `settings.example.json`. |
| License | [Apache-2.0](https://github.com/Kelly-Leeee/AgentNetwork-jev/blob/6bc53d5a25c1ed0d404d486088e8a1e2e64cb1d5/LICENSE) |
| Jev evidence | [`agentrouter`](https://github.com/Kelly-Leeee/AgentNetwork-jev/tree/6bc53d5a25c1ed0d404d486088e8a1e2e64cb1d5/agentrouter) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Experiment with routing inside the execution loop rather than one up-front plan.
- Mismatch: research/demo topology, not a hardened orchestrator.

## How it works

Completion events trigger a Jev Choice over pending tasks and idle agents using recent results; roles are optional prompt hints. (Summarized from the upstream [README](https://github.com/Kelly-Leeee/AgentNetwork-jev/blob/6bc53d5a25c1ed0d404d486088e8a1e2e64cb1d5/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `uv sync` then `./start.sh` per the README.

## Limits and data handling

Task state and recent results go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 6bc53d5a25c1](https://github.com/Kelly-Leeee/AgentNetwork-jev/tree/6bc53d5a25c1ed0d404d486088e8a1e2e64cb1d5). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
