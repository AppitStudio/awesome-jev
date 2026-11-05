# pi-rector (Pi coding-agent extension that routes each request to the cheapest usable subscription, with a free Jev classifier rating message difficulty)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Extension for the Pi coding agent that registers `auto/*` virtual models and routes every request to the cheapest model your subscription plans can serve, using quota blocks, off-peak time windows and balanced accounts. At medium thinking level the free Jev classifier (`opencode/jev-1.13-free`) rates the last user message as trivial, standard or complex to pick the workload tier; a missing or failed rating counts as standard.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tonyputi/pi-rector) |
| Maintainer | [tonyputi](https://github.com/tonyputi). Independently curated. |
| Format | Pi extension (single TypeScript file `auto-router.ts`, MIT) |
| Requirements | The Pi coding agent, the subscription providers you want to route between, and the Jev classifier model registered in Pi's model registry (`opencode/jev-1.13-free`). |
| License | [MIT](https://github.com/tonyputi/pi-rector/blob/1eec6353bf08c3efe9e2f6a934b28581d7ef7b9a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`auto-router.ts`](https://github.com/tonyputi/pi-rector/blob/1eec6353bf08c3efe9e2f6a934b28581d7ef7b9a/auto-router.ts) at the pinned commit. |

## When to use

- Spend cheap or off-peak coding-agent subscriptions first and fail over when a plan runs out of quota.
- Let a small decision model pick between trivial, standard and complex workloads instead of a fixed thinking level.
- Mismatch: Jev is only the difficulty classifier for the medium level; the routing, quota and balancing logic is ordinary code, and the repository was created on 2026-11-05.

## How it works

`rateDifficulty` in `auto-router.ts` sends the last user message (first 16,000 characters) as state with one `choice` question (trivial, standard or complex) to the Jev classifier model through Pi's `modelRegistry.classify`, and falls back to standard when the classifier is missing or fails. Integration evidence: [`auto-router.ts`](https://github.com/tonyputi/pi-rector/blob/1eec6353bf08c3efe9e2f6a934b28581d7ef7b9a/auto-router.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# copy auto-router.ts into ~/.pi/agent/extensions/ (or point Pi's `extensions` setting at the repo)
# then select auto/smart in /model and set thinking level to medium
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (virtual models, routing steps, configuration): [github.com/tonyputi/pi-rector/blob/1eec6353bf08c3efe9e2f6a934b28581d7ef7b9a/README.md](https://github.com/tonyputi/pi-rector/blob/1eec6353bf08c3efe9e2f6a934b28581d7ef7b9a/README.md)

## Limits and data handling

At the medium level the last user message is sent to the classifier model through Pi's provider for that model. Routing depends on your own plans and settings, and the extension is days old with no stars or release.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 1eec6353bf08](https://github.com/tonyputi/pi-rector/tree/1eec6353bf08c3efe9e2f6a934b28581d7ef7b9a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
