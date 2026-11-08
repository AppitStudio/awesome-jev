# deckuse (local-first PPTX structural editing engine with TypeSafe Jev element finding)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first CLI/engine for agents to edit PowerPoint files structurally; `deckuse find` uses TypeSafe Jev to locate elements from a natural-language description.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/deckflow/deckuse) |
| Maintainer | [deckflow](https://github.com/deckflow). Independently curated. |
| Format | TypeScript CLI + library (AGPL-3.0) |
| Requirements | Node, deckuse, and `TYPESAFE_API_KEY` for `find`. |
| License | [AGPL-3.0](https://github.com/deckflow/deckuse/blob/5e173df64fb3e9d0bc3ca6c214280482ee870844/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/find/client.ts`](https://github.com/deckflow/deckuse/blob/5e173df64fb3e9d0bc3ca6c214280482ee870844/src/find/client.ts) at the pinned commit. |

## When to use

- Let agents target slide elements by description.
- Edit PPTX structurally without a GUI.
- Mismatch: only `find` uses Jev.

## How it works

`src/find/client.ts` uses `@typesafe-ai/sdk` with default `jev-latest` to pick matching shapes; it sends element names plus visible text to `api.typesafe.ai`. Other commands stay local. Integration evidence: [`src/find/client.ts`](https://github.com/deckflow/deckuse/blob/5e173df64fb3e9d0bc3ca6c214280482ee870844/src/find/client.ts).

## Get started

Install deckuse per README and run `deckuse find "the revenue card" --json` with your key.

```sh
git clone https://github.com/deckflow/deckuse.git && cd deckuse
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Agent cookbook: [github.com/deckflow/deckuse/blob/5e173df64fb3e9d0bc3ca6c214280482ee870844/docs/agent-cookbook.md](https://github.com/deckflow/deckuse/blob/5e173df64fb3e9d0bc3ca6c214280482ee870844/docs/agent-cookbook.md)

## Limits and data handling

Shape names and visible slide text are sent to TypeSafe for `find`.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 5e173df64fb3](https://github.com/deckflow/deckuse/tree/5e173df64fb3e9d0bc3ca6c214280482ee870844). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
