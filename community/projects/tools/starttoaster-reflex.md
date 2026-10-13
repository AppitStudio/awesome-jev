# reflex (Alertmanager router)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Alertmanager webhook receiver that asks TypeSafe Jev one Choice question per alert group to send it to an urgent or informational Discord channel, falling back to label routing (distinct from [Reflex System One](reflex-system-one.md)).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Starttoaster/reflex) |
| Maintainer | [Starttoaster](https://github.com/Starttoaster). Independently curated. |
| Format | Go service |
| Requirements | Go or container; Alertmanager; Discord webhooks; TypeSafe key. |
| License | [MIT](https://github.com/Starttoaster/reflex/blob/317e067bdec31feeeb92113416a6fb22f4ecb200/LICENSE) |
| Jev evidence | [`internal/jev/client.go`](https://github.com/Starttoaster/reflex/blob/317e067bdec31feeeb92113416a6fb22f4ecb200/internal/jev/client.go) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Reduce pager noise by letting a decision model separate act-now alerts from informational ones.
- Mismatch: lab project; do not make it your only path for critical alerts.

## How it works

Each firing group is summarized (labels, annotations, duration, hosts); Jev chooses `page now` or `informational` plus a logged urgency score; slow, missing or unsure answers fall back to severity labels. (Summarized from the upstream [README](https://github.com/Starttoaster/reflex/blob/317e067bdec31feeeb92113416a6fb22f4ecb200/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): configure the Discord webhooks and key, run the binary, and point an Alertmanager receiver at it.

## Limits and data handling

Alert labels and annotations go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 317e067bdec3](https://github.com/Starttoaster/reflex/tree/317e067bdec31feeeb92113416a6fb22f4ecb200). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
