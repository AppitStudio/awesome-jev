# jizhang (self-hosted subscription and renewal tracker with optional Jev categories)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted command center for recurring expenses: subscriptions, renewals, reminders and the decisions around them; optional per-user Jev classification picks a category when a subscription is added.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/torr9522/jizhang) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/torr9522/jizhang#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (GPL-3.0-or-later); free to self-host. Jev calls use each user's own TypeSafe key. Checked 2026-10-25. |
| Jev evidence | [`internal/service/jev/client.go`](https://github.com/torr9522/jizhang/blob/a3d465ae8d94906c93bc17ff32151755cc25d6e3/internal/service/jev/client.go) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [torr9522](https://github.com/torr9522). Independently curated. |
| Format | Self-hosted web app (Go, Docker image) |
| Platform and availability | Self-hosted; Docker image on GHCR. |
| Jev's role | Optional: off by default; when enabled, Jev suggests a category for each new subscription and only a confident suggestion is applied. |
| Requirements | Docker (or Docker Compose); each user's own TypeSafe key for the optional classification. |
| License | [GPL-3.0-or-later](https://github.com/torr9522/jizhang/blob/a3d465ae8d94906c93bc17ff32151755cc25d6e3/LICENSE) |

## When to use

- Track what renews next on your own server.
- Skip manual categorising with a cheap Jev suggestion.
- Mismatch: classification is the only Jev feature.

## How it works

`internal/service/jev/client.go` posts the subscription name, website domain and your category names to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); notes, amounts and URL paths are excluded. Integration evidence: [`internal/service/jev/client.go`](https://github.com/torr9522/jizhang/blob/a3d465ae8d94906c93bc17ff32151755cc25d6e3/internal/service/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
docker run -d --name subdux -p 8080:8080 --env-file ./jizhang.env -e DATA_PATH=/data -v "$(pwd)/data:/data" ghcr.io/torr9522/jizhang:jizhang-v0.33.0-1
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/torr9522/jizhang#readme](https://github.com/torr9522/jizhang#readme)

## Limits and data handling

Only the subscription name, domain and category names go to TypeSafe; keys are encrypted on the server and excluded from exports.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit a3d465ae8d94](https://github.com/torr9522/jizhang/tree/a3d465ae8d94906c93bc17ff32151755cc25d6e3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
