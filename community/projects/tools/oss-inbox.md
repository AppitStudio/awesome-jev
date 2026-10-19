# OSS Inbox

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-hosted GitHub App and dashboard for maintainers: Jev answers typed questions about each issue, PR and CI report to label, route, prioritize and screen them, acting only above thresholds measured on your own repo history and never closing anything.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DibbayajyotiRoy/oss-inbox) |
| Maintainer | [DibbayajyotiRoy](https://github.com/DibbayajyotiRoy). Independently curated. |
| Format | Self-hosted GitHub App + dashboard (Python backend, Docker Compose) |
| Requirements | Docker with Compose v2; a TypeSafe API key; a GitHub account or org that can own an App. |
| License | [Apache-2.0](https://github.com/DibbayajyotiRoy/oss-inbox/blob/8767b9f7968685e7d07a893075aafb28821a64fb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/dibbayajyoti/status/2112109652674752865)). |
| Jev evidence | [`backend/app/decision/jev.py`](https://github.com/DibbayajyotiRoy/oss-inbox/blob/8767b9f7968685e7d07a893075aafb28821a64fb/backend/app/decision/jev.py) at the pinned commit. |

## When to use

- Triage a busy repo's issues and PRs with labels, routing and needs-info checks.
- Screen low-quality or AI-generated reports before they reach maintainers.
- Mismatch: needs self-hosting and a GitHub App; starts in shadow mode until you enable auto.

## How it works

A webhook builds a short state text from the item and your repo facts, then `backend/app/decision/jev.py` makes one `/v1/systemone` call with all enabled questions. Each answer's probability is its confidence. In auto mode an action runs only above your threshold on questions measured against your closed issues and merged PRs; everything else goes to a review queue. Integration evidence: [`backend/app/decision/jev.py`](https://github.com/DibbayajyotiRoy/oss-inbox/blob/8767b9f7968685e7d07a893075aafb28821a64fb/backend/app/decision/jev.py).

## Get started

From the upstream README: try the sample-data demo with Docker Compose, or self-host on your repos with a TypeSafe key and the in-app GitHub App setup.

```sh
git clone https://github.com/DibbayajyotiRoy/oss-inbox.git && cd oss-inbox
cp .env.example .env && echo "DEMO_MODE=true" >> .env
docker compose up -d --build
docker compose exec api python -m app.cli demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [oss.dibbayajyoti.com/login](https://oss.dibbayajyoti.com/login)
- docs/self-hosting.md

## Limits and data handling

Issue, PR and CI text goes to TypeSafe. It never closes, deletes, locks or transfers; comments are off by default. Independent project, not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 8767b9f79686](https://github.com/DibbayajyotiRoy/oss-inbox/tree/8767b9f7968685e7d07a893075aafb28821a64fb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
