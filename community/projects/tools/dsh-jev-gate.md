# dsh-jev-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

DeepSeek Harness (DSH) plugin for AgentTeams (Chinese docs) that checks each round's promised deliverables against a frozen baseline and evidence ledger before the team advances, with an optional `native-jev` decider (TypeSafe Jev) as an advisory or enforcing second opinion.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hemppp/dsh-jev-gate) |
| Maintainer | [hemppp](https://github.com/hemppp). Independently curated. |
| Format | DSH (DeepSeek Harness) desktop plugin |
| Requirements | DSH with AgentTeams; for the Jev decider, a TypeSafe API key and base URL configured in plugin settings. |
| License | [MIT](https://github.com/hemppp/dsh-jev-gate/blob/dc4a5c9629385741930b754a05ead38b93065355/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Add a delivery audit to multi-agent DSH teams so self-reports alone cannot close a round.
- Try a dry-run → advisory → enforce rollout with a calibrated second opinion.
- Mismatch: docs are Chinese and specific to DSH AgentTeams; the default decider is local and deterministic.

## How it works

The default `baseline` decider only replays the ledger. Setting `deciderKind` to `native-jev` (base `https://api.typesafe.ai`, model `jev-1.13.0`) sends the evidence for each gap to Jev; `decider.authority` controls whether its verdict is advisory or binding. Code: [`host/decider.ts`](https://github.com/hemppp/dsh-jev-gate/blob/dc4a5c9629385741930b754a05ead38b93065355/host/decider.ts), [`host/gate.ts`](https://github.com/hemppp/dsh-jev-gate/blob/dc4a5c9629385741930b754a05ead38b93065355/host/gate.ts).

## Get started

Install into DSH (disabled by default), then enable dry-run first:

```sh
dsh plugin --profile desktop add --save-exact <path-to-plugin>@0.2.0
# restart the web UI; Settings → Plugins → dsh-jev-gate → Configure
# mode: dry-run → advisory → enforce; deciderKind: native-jev
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- README tables of the four gap types and the L-levels of intervention.
- Configuration sample with `native-jev` decider fields.

## Limits and data handling

Ledger evidence is sent to TypeSafe only when the Jev decider is enabled. Enforcement quality was not evaluated. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit dc4a5c962938](https://github.com/hemppp/dsh-jev-gate/tree/dc4a5c9629385741930b754a05ead38b93065355). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
