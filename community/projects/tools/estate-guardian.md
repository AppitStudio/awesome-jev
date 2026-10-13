# estate-guardian

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Python watchdog that keeps a fleet of AI coding agents working overnight (credit, CI runners, disk, services), routes jobs to an available lab, and uses TypeSafe Jev as a tier-2 classifier for free text rules miss.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/m-check1B/estate-guardian) |
| Maintainer | [m-check1B](https://github.com/m-check1B). Independently curated. |
| Format | Python script (cron-style) |
| Requirements | Python; your agent/CI setup; TypeSafe key. |
| License | [MIT](https://github.com/m-check1B/estate-guardian/blob/e9298665852c62aa5011e3b373a4f9efd4282f6b/LICENSE) |
| Jev evidence | [`classify.py`](https://github.com/m-check1B/estate-guardian/blob/e9298665852c62aa5011e3b373a4f9efd4282f6b/classify.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Catch stalled agents, dead runners and full disks at 3 a.m. and reroute work.
- Mismatch: opinionated around the author's orchestration chain.

## How it works

Every 5 minutes deterministic checks run; unmatched free text goes to Jev for a typed choice over the failure taxonomy with a minimum confidence, then a ticket is opened. (Summarized from the upstream [README](https://github.com/m-check1B/estate-guardian/blob/e9298665852c62aa5011e3b373a4f9efd4282f6b/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): configure the presets and run the script on a schedule per the README.

## Limits and data handling

Failure text goes to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit e9298665852c](https://github.com/m-check1B/estate-guardian/tree/e9298665852c62aa5011e3b373a4f9efd4282f6b). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
