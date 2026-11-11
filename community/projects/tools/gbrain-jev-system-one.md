# GBrain (agent memory brain with Jev System One decision slots)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Agent memory and knowledge brain for OpenClaw and Hermes that can hand typed decisions in search, think, dream triage and the fact sweep to TypeSafe Jev, and can use Jev as an optional search reranker.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/garrytan/gbrain) |
| Maintainer | [garrytan](https://github.com/garrytan). Independently curated. |
| Format | CLI and MCP server (TypeScript/Bun, MIT) |
| Requirements | Bun, the model/embedding keys GBrain asks for, and `TYPESAFE_API_KEY` (or `JEV_TYPESAFE_API_KEY`) for the Jev slots. |
| License | [MIT](https://github.com/garrytan/gbrain/blob/747dc24cc17608968aa34cf425129773ced4547b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/core/ai/decide/providers/typesafe.ts`](https://github.com/garrytan/gbrain/blob/747dc24cc17608968aa34cf425129773ced4547b/src/core/ai/decide/providers/typesafe.ts) at the pinned commit. |

## When to use

- Add typed Jev decisions to an agent memory system.
- Compare Jev against other providers per decision slot (the companion gbrain-evals study is already listed).
- Mismatch: a key turns two slots on by default and sends transcript windows and fact text, including private facts, to TypeSafe.

## How it works

`src/core/ai/decide/providers/typesafe.ts` sends System One requests for the `decide` slots; `docs/ai-providers/typesafe.md` says a key turns on dream triage and contradiction proposals by default (other slots stay off), and `search.reranker.model typesafe:jev-1.13.0` opts into Jev reranking. Integration evidence: [`src/core/ai/decide/providers/typesafe.ts`](https://github.com/garrytan/gbrain/blob/747dc24cc17608968aa34cf425129773ced4547b/src/core/ai/decide/providers/typesafe.ts).

## Get started

Install GBrain, put a TypeSafe key in `~/.gbrain/.env`, then check `gbrain decide status`; read the System One guide before enabling more slots.

```sh
bun install -g github:garrytan/gbrain#stable
gbrain decide status
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- TypeSafe provider doc: [github.com/garrytan/gbrain/blob/747dc24cc17608968aa34cf425129773ced4547b/docs/ai-providers/typesafe.md](https://github.com/garrytan/gbrain/blob/747dc24cc17608968aa34cf425129773ced4547b/docs/ai-providers/typesafe.md)
- System One guide: [github.com/garrytan/gbrain/blob/747dc24cc17608968aa34cf425129773ced4547b/docs/guides/system-one.md](https://github.com/garrytan/gbrain/blob/747dc24cc17608968aa34cf425129773ced4547b/docs/guides/system-one.md)

## Limits and data handling

With a key, dream triage sends conversation transcript windows and the conflict slot sends fact text to TypeSafe; opt out with `gbrain decide disable --all`.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 747dc24cc176](https://github.com/garrytan/gbrain/tree/747dc24cc17608968aa34cf425129773ced4547b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
