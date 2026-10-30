# CronSight (scheduled inspection agent platform with optional Jev anomaly triage and human review)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MiniClaw-based platform for scheduled health checks: a read-only runner checks error rate, latency, CPU, backlog, certificates and data freshness from a workspace JSON snapshot. An optional path sends anonymised metrics to Jev as a Choice of `anomaly`, `normal` or `uncertain`; low-confidence results go to a human review screen, and alerts leave through a separate outbox. README and docs in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jun516/cronsight) |
| Maintainer | [Jun516](https://github.com/Jun516). Independently curated. |
| Format | Self-hosted TypeScript platform (fork-based extension of MiniClaw) |
| Requirements | Node.js build of the service, web UI and agent runner; `TYPESAFE_API_KEY`, `JEV_MODEL` and an allowed source list to enable the Jev path. |
| License | [MIT](https://github.com/Jun516/cronsight/blob/046865a594440941885a761a65c3613678d87f64/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/cronsight-triage.ts`](https://github.com/Jun516/cronsight/blob/046865a594440941885a761a65c3613678d87f64/src/cronsight-triage.ts) at the pinned commit. |

## When to use

- Add a typed anomaly/normal/uncertain decision with review on top of fixed metric thresholds for scheduled checks.
- Mismatch: synthetic samples and offline tests only; thresholds are demo values, not calibrated on real incidents.

## How it works

Fixed metric rules run first; `cronsight-triage.ts` then sends anonymised metric names, values and thresholds through `jev-client.ts` and stores the class, confidence and evidence hash. A high-confidence `anomaly` still needs a deterministic breach before it alerts. Integration evidence: [`src/cronsight-triage.ts`](https://github.com/Jun516/cronsight/blob/046865a594440941885a761a65c3613678d87f64/src/cronsight-triage.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.jev.example .env  # set TYPESAFE_API_KEY and JEV_MODEL
# then enable 'Jev structured inspection' on a scheduled task (see docs/cronsight/jev-triage.md)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev triage setup and review flow (Chinese): [github.com/Jun516/cronsight/blob/046865a594440941885a761a65c3613678d87f64/docs/cronsight/jev-triage.md](https://github.com/Jun516/cronsight/blob/046865a594440941885a761a65c3613678d87f64/docs/cronsight/jev-triage.md)

## Limits and data handling

Anonymised metric values and thresholds are sent to TypeSafe when the Jev path is enabled; it is off by default per task. Builds on MiniClaw (MIT). Not production-validated by its author. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit 046865a59444](https://github.com/Jun516/cronsight/tree/046865a594440941885a761a65c3613678d87f64). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
