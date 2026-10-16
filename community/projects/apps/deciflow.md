# DeciFlow

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted log triage: groups log events into chunks and classifies each one as Normal, Warning, Error, Security or Other with urgency and a needs-a-ticket probability, using self-hosted Laya by default or TypeSafe Jev; batch scans, live follow and a dashboard with probabilities.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/call518/deciflow) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/call518/deciflow#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-17. |
| Jev evidence | [`config.py`](https://github.com/call518/deciflow/blob/2d010a76a5555e19d6d3fbe448da257a063fc20a/config.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [call518](https://github.com/call518). Independently curated. |
| Format | Docker Compose web app (dashboard on port 4000) |
| Platform and availability | Linux server (Docker Compose, self-hosted) |
| Jev's role | Optional engine: Jev (or Laya) classifies each log chunk by category, urgency and ticket need. |
| Requirements | Docker Compose on the host with your logs; for Jev, a TypeSafe API key and `DECISION_ENGINE=jev` in `.env`. |
| License | [MIT](https://github.com/call518/deciflow/blob/2d010a76a5555e19d6d3fbe448da257a063fc20a/LICENSE) |

## When to use

- Watch HTTP, system or app logs and review the chunks most likely to need action.
- Mismatch: Laya is the default engine; Jev is optional and paid. It does not create tickets itself.

## How it works

Each chunk is sent as the request's `state` with three questions in one call: a Choice for category, a Score for urgency (0 to 3) and a Noul for whether a work ticket is needed; with Jev selected it pins `jev-1.13.0`. There is no automatic paid fallback between engines. Integration evidence: [`config.py`](https://github.com/call518/deciflow/blob/2d010a76a5555e19d6d3fbe448da257a063fc20a/config.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/call518/DeciFlow.git && cd DeciFlow
test -f .env || cp .env.example .env   # set DECISION_ENGINE=jev and your TypeSafe key for Jev
docker compose up -d
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo video: [www.youtube.com/watch?v=wGMtxpeHHBs](https://www.youtube.com/watch?v=wGMtxpeHHBs)
- Korean README: `README.ko.md`.

## Limits and data handling

Log chunks go to TypeSafe on your key only when Jev is selected; with Laya everything stays on your host. Change the default `changeme` key before deployment.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 2d010a76a555](https://github.com/call518/deciflow/tree/2d010a76a5555e19d6d3fbe448da257a063fc20a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
