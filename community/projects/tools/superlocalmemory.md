# SuperLocalMemory

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Local-first, governed memory for AI agents (SQLite, hybrid recall, time-aware facts) with an optional answer check that asks Laya on-device or Jev online whether the top recalled memories actually answer the question.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/qualixar/superlocalmemory) |
| Product homepage | [www.superlocalmemory.com](https://www.superlocalmemory.com) |
| Maintainer | [qualixar](https://github.com/qualixar). Independently curated. |
| Format | Self-hosted memory service with CLI, web dashboard and agent integrations |
| Requirements | Node 18+ and Python 3.12+ (npm route) or Python 3.12+ (pip/pipx). The online answer check needs your own TypeSafe or OpenRouter key plus an explicit consent tick; the on-device check needs Apple Silicon. |
| License | [AGPL-3.0](https://github.com/qualixar/superlocalmemory/blob/c3fcdda1901eae7e2fbbc502b1738891a5d75b9a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Give agents durable memory that admits when nothing on file answers the question instead of returning the nearest match as if it were the answer.
- Choose per install between a private on-device check (Laya) and a hosted Jev check.
- Mismatch: if no memory text may leave the machine, keep the answer check on *On this Mac* or *Off*.

## How it works

Recall ranks memories as usual; the answer check is a separate step over the top results. *Online with Jev* sends the question and the top 3 memories to TypeSafe or OpenRouter with your key, and the response marks whether the top result is likely an answer. An extra switch, *Also use Jev to reorder results*, sends the top 20 under its own notice, and Jev kind typing has its own consent. Only one checker runs at a time and the online option never turns itself on ([docs/answer-check.md](https://github.com/qualixar/superlocalmemory/blob/c3fcdda1901eae7e2fbbc502b1738891a5d75b9a/docs/answer-check.md)).

## Get started

Install, then enable the online answer check in the dashboard (live calls on recall once a key and consent are set):

```sh
npm install -g superlocalmemory   # or: pipx install superlocalmemory
slm recall "what did we decide about the billing retry?"
# Dashboard → Settings → Answer check → Online with Jev (add key, tick consent)
```

Live commands contact TypeSafe (or the configured provider) and may incur charges.

## Examples and demos

- [Answer check docs](https://github.com/qualixar/superlocalmemory/blob/c3fcdda1901eae7e2fbbc502b1738891a5d75b9a/docs/answer-check.md): the three choices, what each sends, dashboard history and the "I don't have that" rate.
- README data-egress table listing which feature sends which memory text.

## Limits and data handling

AGPL-3.0. With Jev enabled, recalled memory text goes to the chosen provider and is billed to your key. Upstream also promotes enterprise/governance features on its website; this listing covers the open-source package only and was not run on the review host. Surfaced via Show HN (item 49963368).

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit c3fcdda1901e](https://github.com/qualixar/superlocalmemory/tree/c3fcdda1901eae7e2fbbc502b1738891a5d75b9a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
