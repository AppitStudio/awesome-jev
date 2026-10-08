# Herdr-Jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Plugin for the Herdr terminal workspace and AI-Harness that uses TypeSafe Jev System One (~260–340 ms) for multi-model triage — architectural complexity, research need and reasoning effort — then routes turns to Codex, Claude, Kiro and other peers with calibrated latency deadlines, Triad plan/implement/review orchestration, quota awareness and resumable runs. Separate from the listed alexzfe jev-herdr.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/flaviomartil/herdr-jev) |
| Maintainer | [flaviomartil](https://github.com/flaviomartil). Independently curated. |
| Format | CLI (`herdr-jev plan / route / run-status / run-resume`) + Herdr plugin + agent skills via `./scripts/install.sh` |
| Requirements | Herdr, AI-Harness profiles, the agent CLIs you route to, and `TYPESAFE_API_KEY`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Spread work across several coding-agent subscriptions by task complexity.
- Run implement-then-independent-review loops with a verification command.
- Mismatch: assumes the Herdr + AI-Harness stack; dense, fast-moving docs.

## How it works

Jev triage plus [`src/triage/calibrator.ts`](https://github.com/flaviomartil/herdr-jev/blob/c3ebc7d72370fb4033a08bfe2d8ea831bfa3b76b/src/triage/calibrator.ts) measure round-trips to `api.typesafe.ai` and set deadlines; `plan` exposes advisory and canonical execution stages and `route` launches workers in Herdr panes. Architecture: [`docs/herdr-jev/architecture.html`](https://github.com/flaviomartil/herdr-jev/blob/c3ebc7d72370fb4033a08bfe2d8ea831bfa3b76b/docs/herdr-jev/architecture.html).

## Get started

Install from a checkout (README):

```sh
git clone https://github.com/flaviomartil/herdr-jev.git && cd herdr-jev
./scripts/install.sh
herdr-jev plan "Implement the change" --client codex --triad --json
```

Jev triage billed to your TypeSafe key, plus the routed agents' usage.

## Examples and demos

- [Companion features](https://github.com/flaviomartil/herdr-jev/blob/c3ebc7d72370fb4033a08bfe2d8ea831bfa3b76b/docs/companions.md).

## Limits and data handling

Task text goes to TypeSafe for triage. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit c3ebc7d72370](https://github.com/flaviomartil/herdr-jev/tree/c3ebc7d72370fb4033a08bfe2d8ea831bfa3b76b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
