# Drone Autonomy: AI vs Rules

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Local benchmark that flies a simulated Crazyflie drone through adversarial events and measures collision rate against decision latency for Jev, other decision models, chat LLMs, rule-based pilots and a perfect oracle.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/subho004/drone-autonomy-ai-vs-rules) |
| Maintainer | [subho004](https://github.com/subho004). Independently curated. |
| Format | Python simulator + dashboard |
| Requirements | Python; provider keys for live models (Jev via a decisions endpoint); a hard USD cap is enforced in code. |
| License | [MIT](https://github.com/subho004/drone-autonomy-ai-vs-rules/blob/01bd056d108f36998f78a7dd05a36996becdb07e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/providers/decisions_endpoint.py`](https://github.com/subho004/drone-autonomy-ai-vs-rules/blob/01bd056d108f36998f78a7dd05a36996becdb07e/app/providers/decisions_endpoint.py) at the pinned commit. |

## When to use

- See how decision latency turns into collisions for a moving robot.
- Compare Jev with chat LLMs and rule baselines on certified scenarios.
- Mismatch: simulation only; not flight software.

## How it works

A decision layer picks one of 11 discrete actions while a PID controller flies. Latency is injected as ticks so faster-than-real-time runs stay honest, and scenarios are certified avoidable by a zero-latency oracle. `app/providers/decisions_endpoint.py` defaults to `typesafe/jev-1.13`. Integration evidence: [`app/providers/decisions_endpoint.py`](https://github.com/subho004/drone-autonomy-ai-vs-rules/blob/01bd056d108f36998f78a7dd05a36996becdb07e/app/providers/decisions_endpoint.py).

## Get started

From the upstream README quick start: install, run the simulator and dashboard, and add keys for live models.

```sh
git clone https://github.com/subho004/drone-autonomy-ai-vs-rules && cd drone-autonomy-ai-vs-rules
# see README quick start
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/FINDINGS.md
- docs/LIVE-RESULTS.md

## Limits and data handling

Scenario state goes to each live provider. Results depend on the simulated latency model.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 01bd056d108f](https://github.com/subho004/drone-autonomy-ai-vs-rules/tree/01bd056d108f36998f78a7dd05a36996becdb07e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
