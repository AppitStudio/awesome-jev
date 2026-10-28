# hndelegate (Hacker News curator that sends stories matching your Jev decision trees to Telegram)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Go service that polls new Hacker News stories every two minutes, fetches their content, evaluates each against one or more customisable decision trees stored in SQLite with Jev answering each node, and sends stories that match a tree to a Telegram chat or channel.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uint4096/hndelegate) |
| Maintainer | [uint4096](https://github.com/uint4096). Independently curated. |
| Format | Go service (release binaries) |
| Requirements | Go to build (or a release binary), a Telegram bot token and a TypeSafe API key. |
| License | [GPL-3.0](https://github.com/uint4096/hndelegate/blob/b0da7d2f1a8e51ca8406b53039ade1a417db107f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`internal/model/jev/client.go`](https://github.com/uint4096/hndelegate/blob/b0da7d2f1a8e51ca8406b53039ade1a417db107f/internal/model/jev/client.go) at the pinned commit. |

## When to use

- Get a personal HN feed filtered by several criteria, not keywords.
- Mismatch: every new story costs Jev calls.

## How it works

`internal/model/jev/client.go` posts story content to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) for each decision-tree node. Integration evidence: [`internal/model/jev/client.go`](https://github.com/uint4096/hndelegate/blob/b0da7d2f1a8e51ca8406b53039ade1a417db107f/internal/model/jev/client.go).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/uint4096/hndelegate && cd hndelegate
go build -o hndelegate
JEV_API_KEY=... ./hndelegate   # see README for the Telegram variables
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Decision trees: [github.com/uint4096/hndelegate/blob/main/docs/decisions.md](https://github.com/uint4096/hndelegate/blob/main/docs/decisions.md)
- Releases: [github.com/uint4096/hndelegate/releases/latest](https://github.com/uint4096/hndelegate/releases/latest)

## Limits and data handling

Public HN story content goes to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit b0da7d2f1a8e](https://github.com/uint4096/hndelegate/tree/b0da7d2f1a8e51ca8406b53039ade1a417db107f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
