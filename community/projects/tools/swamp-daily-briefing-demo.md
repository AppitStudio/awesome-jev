# swamp daily briefing demo (swamp workflow that grades an invented review queue with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-contained example for the swamp automation tool: a "daily briefing" workflow seeds an invented GitLab-style review queue and issue list, grades every item with Jev through the `@swamp/typesafe-ai` extension plus a fan-out triage method, and renders a terminal board with urgency, recommendation and vulnerability flags; all data is fiction.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/webframp/swamp-daily-briefing-demo) |
| Maintainer | [webframp](https://github.com/webframp). Independently curated. |
| Format | swamp workflow and TypeScript extension |
| Requirements | swamp; a TypeSafe API key stored in a swamp vault. |
| License | [Apache-2.0](https://github.com/webframp/swamp-daily-briefing-demo/blob/176d843a2c1178beb054d33e80fda28ed97083ba/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/models/typesafe/triage.ts`](https://github.com/webframp/swamp-daily-briefing-demo/blob/176d843a2c1178beb054d33e80fda28ed97083ba/extensions/models/typesafe/triage.ts) at the pinned commit. |

## When to use

- Learn how to call Jev from swamp workflows with a safe, invented dataset.
- Copy the fan-out triage pattern for your own queues.
- Mismatch: demo data only; it publishes nothing.

## How it works

`extensions/models/typesafe/triage.ts` extends `@swamp/typesafe-ai` with a `triage` method that makes one `POST /v1/systemone` call per item with batched questions and collects the typed answers for the board. Integration evidence: [`extensions/models/typesafe/triage.ts`](https://github.com/webframp/swamp-daily-briefing-demo/blob/176d843a2c1178beb054d33e80fda28ed97083ba/extensions/models/typesafe/triage.ts).

## Get started

From the upstream README (not run on the review host):

```sh
swamp extension pull @swamp/typesafe-ai
swamp vault put typesafe TYPESAFE_API_KEY
swamp workflow run daily-briefing-demo
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/webframp/swamp-daily-briefing-demo#readme](https://github.com/webframp/swamp-daily-briefing-demo#readme)
- swamp: [github.com/swamp-club/swamp](https://github.com/swamp-club/swamp)

## Limits and data handling

Invented items go to TypeSafe for grading; no other external service is contacted.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 176d843a2c11](https://github.com/webframp/swamp-daily-briefing-demo/tree/176d843a2c1178beb054d33e80fda28ed97083ba). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
