# pi-router by JangMan-J (session-level model router for Pi, with Jev as a fallback decider)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi virtual model (`router/auto`) that picks a model per session along three axes (depth, width, urgency) from a paired review by decision models on OpenRouter, detects when a conversation pivots using local telemetry and embeddings, and keeps a SQLite store of routing records for calibration and retrieval. Jev (`typesafe/jev-1.14`) is the first automatic fallback decider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JangMan-J/pi-router) |
| Maintainer | [JangMan-J](https://github.com/JangMan-J). Independently curated. |
| Format | Pi package (TypeScript, npm `@jangmanj/pi-router`) |
| Requirements | Pi, an OpenRouter key, and optionally a local embedding server for pivot detection. |
| License | [MIT](https://github.com/JangMan-J/pi-router/blob/2e1ca1aa7a242042ada3b17196234693a4ef7fd9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`pipeline/config.json`](https://github.com/JangMan-J/pi-router/blob/2e1ca1aa7a242042ada3b17196234693a4ef7fd9/pipeline/config.json) at the pinned commit. |

## When to use

- Let Pi choose a model tier per session instead of per message.
- Mismatch: Jev is a fallback, not the primary decider; an advanced setup.

## How it works

`pipeline/config.json` enables the `openrouter-jev` decider (`typesafe/jev-1.14` via OpenRouter) as fallback #1 behind two other decision models. Integration evidence: [`pipeline/config.json`](https://github.com/JangMan-J/pi-router/blob/2e1ca1aa7a242042ada3b17196234693a4ef7fd9/pipeline/config.json).

## Get started

From the upstream README (not run on the review host):

```sh
pi install npm:@jangmanj/pi-router
# then select router/auto as the model in Pi
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/JangMan-J/pi-router#readme](https://github.com/JangMan-J/pi-router#readme)
- Pipeline guide: [github.com/JangMan-J/pi-router/blob/main/pipeline_guide.md](https://github.com/JangMan-J/pi-router/blob/main/pipeline_guide.md)

## Limits and data handling

Session summaries sent for routing go to OpenRouter and the decision-model providers.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 2e1ca1aa7a24](https://github.com/JangMan-J/pi-router/tree/2e1ca1aa7a242042ada3b17196234693a4ef7fd9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
