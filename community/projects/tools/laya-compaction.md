# laya-compaction

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Port of the listed fast-jev-compaction that swaps TypeSafe Jev for Laya, the open Jev-compatible decision model: a Claude Code plugin and npm library that replaces the compaction summary with per-item decisions — every tool call and result is scored, stale ones are dropped or truncated, and everything kept (including all user and assistant text) stays verbatim; Laya runs locally via a shared `laya-serve` or on your own server through `LAYA_URL`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bussolabs/laya-compaction) |
| Maintainer | [bussolabs](https://github.com/bussolabs). Independently curated. |
| Format | Claude Code plugin and npm library |
| Requirements | Node; uv (installs Python 3.12 for the local Laya server on first start) or a remote `laya-serve` at `LAYA_URL`. |
| License | [MIT](https://github.com/bussolabs/laya-compaction/blob/e8c1f7afefa36a3ad270c32e35b2a06a50ee30a2/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Compact long agent sessions without summaries that drop exact paths or errors.
- Keep compaction fully self-hosted with no TypeSafe key.
- Mismatch: Laya's default 4096-token window is far smaller than Jev's (README).

## How it works

[`src/compact.ts`](https://github.com/bussolabs/laya-compaction/blob/e8c1f7afefa36a3ad270c32e35b2a06a50ee30a2/src/compact.ts) builds keep/drop questions per tool item; [`src/client.ts`](https://github.com/bussolabs/laya-compaction/blob/e8c1f7afefa36a3ad270c32e35b2a06a50ee30a2/src/client.ts) calls `/v1/systemone` on Laya; [`hooks/laya.ts`](https://github.com/bussolabs/laya-compaction/blob/e8c1f7afefa36a3ad270c32e35b2a06a50ee30a2/hooks/laya.ts) wires it into Claude Code. Upstream credit: tamaratran/fast-jev-compaction.

## Get started

Install the library or the plugin (README):

```sh
npm install @bussolabs/laya-compaction
# or, as a Claude Code plugin:
claude plugin marketplace add bussolabs/laya-compaction
claude plugin install laya-compaction@laya-compaction
```

No API charges with local Laya; your own server's costs in remote mode.

## Examples and demos

- npm: [`@bussolabs/laya-compaction`](https://www.npmjs.com/package/@bussolabs/laya-compaction).
- Tuning data: [`tuning/README.md`](https://github.com/bussolabs/laya-compaction/blob/e8c1f7afefa36a3ad270c32e35b2a06a50ee30a2/tuning/README.md).

## Limits and data handling

Conversation items go to the Laya server you run. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit e8c1f7afefa3](https://github.com/bussolabs/laya-compaction/tree/e8c1f7afefa36a3ad270c32e35b2a06a50ee30a2). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
