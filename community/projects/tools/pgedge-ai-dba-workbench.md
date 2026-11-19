# pgEdge AI DBA Workbench (self-hosted PostgreSQL monitoring whose alerter can ask Jev whether an anomaly is a real issue)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source, agentless PostgreSQL monitoring from pgEdge (collector, server, alerter, web client, MCP tools and the Ellie assistant). Its alerter runs three-tier anomaly detection, and tier 3 can use an optional decision provider: with `decision_provider: typesafe` it asks Jev (`jev-latest` by default) one yes/no question per anomaly candidate, whether it is a real issue that needs attention, and suppresses the alert when the probability of no passes a configurable threshold.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pgEdge/ai-dba-workbench) |
| Maintainer | [pgEdge](https://github.com/pgEdge). Independently curated. |
| Format | Go services + React web client |
| Requirements | PostgreSQL to monitor and a PostgreSQL datastore for the workbench; Go and Node to build from source, or the published binaries/Docker images. For the Jev tier: a TypeSafe API key file and `decision_provider: typesafe` in the alerter config. Embedding and reasoning providers (Ollama by default) are configured separately. |
| License | [PostgreSQL License](https://github.com/pgEdge/ai-dba-workbench/blob/c10c66480f51fecfce562fd2673c9f623eb8b978/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Maintained by pgEdge, Inc.; the Jev decision tier is optional. Discovered via X ([post](https://x.com/pgEdgeInc/status/2123523153095692794)). |
| Jev evidence | [`alerter/src/internal/llm/decision.go`](https://github.com/pgEdge/ai-dba-workbench/blob/c10c66480f51fecfce562fd2673c9f623eb8b978/alerter/src/internal/llm/decision.go) at the pinned commit. |

## When to use

- Self-host PostgreSQL monitoring that suppresses noisy anomaly alerts with a cheap yes/no decision before paging anyone.
- Mismatch: a hosted SaaS monitor or a small single-script example; this is a full multi-service product, and the Jev tier is optional and off by default.

## How it works

Tier 1 flags metric outliers by z-score, tier 2 compares candidates with past anomalies by embedding similarity, and tier 3 classifies what remains with a reasoning model and, when configured, a decision model. `alerter/src/internal/llm/decision.go` defines the `DecisionProvider` that sends the tier 3 context (metric, value, z-score, baseline, similar past anomalies, past acknowledgments and cluster peer alerts) to TypeSafe as a single `real` question and applies `anomaly.tier3.decision_suppress_threshold`; refusals and out-of-range probabilities are errors, never verdicts. The OpenAI Decisions API is the other supported provider. Integration evidence: [`alerter/src/internal/llm/decision.go`](https://github.com/pgEdge/ai-dba-workbench/blob/c10c66480f51fecfce562fd2673c9f623eb8b978/alerter/src/internal/llm/decision.go).

## Get started

Install the workbench from binaries, Docker or source (see the upstream docs), then enable the decision tier in the alerter configuration.

```sh
git clone https://github.com/pgEdge/ai-dba-workbench
cd ai-dba-workbench
# follow docs/getting-started/ (binaries, Docker or build from source)
# alerter config (see examples/ai-dba-alerter.yaml):
#   llm:
#     decision_provider: typesafe
#     typesafe:
#       api_key_file: /etc/ai-workbench/typesafe-api-key.txt
#       decision_model: jev-latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision model docs: [github.com/pgEdge/ai-dba-workbench/blob/c10c66480f51fecfce562fd2673c9f623eb8b978/docs/configuration/alerter/llm_providers.md](https://github.com/pgEdge/ai-dba-workbench/blob/c10c66480f51fecfce562fd2673c9f623eb8b978/docs/configuration/alerter/llm_providers.md)
- Example alerter config: [github.com/pgEdge/ai-dba-workbench/blob/c10c66480f51fecfce562fd2673c9f623eb8b978/examples/ai-dba-alerter.yaml](https://github.com/pgEdge/ai-dba-workbench/blob/c10c66480f51fecfce562fd2673c9f623eb8b978/examples/ai-dba-alerter.yaml)
- Product docs: [docs.pgedge.com/ai-dba-workbench](https://docs.pgedge.com/ai-dba-workbench)
- Release announcement on X: [x.com/pgEdgeInc/status/2123523153095692794](https://x.com/pgEdgeInc/status/2123523153095692794)

## Limits and data handling

When the decision tier is on, the tier 3 context (metric names and values, database and connection identifiers, past acknowledgment notes and usernames) is sent to TypeSafe; pgEdge's docs advise reviewing the provider's data-handling terms first. Version 2.0.0-beta1 is a beta. pgEdge's X post reports its own comparison (about 200 ms and $0.04 per 1,000 decisions against Claude Haiku 4.5); those figures were not reproduced here.

## Review and maintenance

Reviewed **2026-11-20** (Europe/Sofia) at [commit c10c66480f51](https://github.com/pgEdge/ai-dba-workbench/tree/c10c66480f51fecfce562fd2673c9f623eb8b978). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
