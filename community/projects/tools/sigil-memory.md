# Sigil (local-first shared memory for coding agents with an optional TypeSafe Jev reranker)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first memory shared across Claude Code, Codex, Cursor and MCP clients, stored in your Postgres; an optional Jev mode reranks recalled facts before they reach the prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Anmol-Srv/sigil) |
| Maintainer | [Anmol-Srv](https://github.com/Anmol-Srv). Independently curated. |
| Format | Node daemon + MCP server (MIT) |
| Requirements | Node, Postgres, an embedding/LLM provider, and a TypeSafe key for the Jev reranker. |
| License | [MIT](https://github.com/Anmol-Srv/sigil/blob/56a07df7bcbb851f9dcc5fe1581b359a1b893b49/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/lib/jev.js`](https://github.com/Anmol-Srv/sigil/blob/56a07df7bcbb851f9dcc5fe1581b359a1b893b49/src/lib/jev.js) at the pinned commit. |

## When to use

- Keep only relevant memories in agent context.
- Share one memory store across coding agents.
- Mismatch: Jev reranking is opt-in.

## How it works

`src/lib/jev.js` calls `https://api.typesafe.ai/v1/systemone` with pinned `jev-1.13.0` to accept or drop candidate facts; `eval/jev-rerank` and `demo/jev-before-after-dataset.json` hold the evaluation. Integration evidence: [`src/lib/jev.js`](https://github.com/Anmol-Srv/sigil/blob/56a07df7bcbb851f9dcc5fe1581b359a1b893b49/src/lib/jev.js).

## Get started

Install with the README installer or from a checkout, then enable Jev and paste the key in the Sigil dashboard.

```sh
git clone https://github.com/Anmol-Srv/sigil.git && cd sigil
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Anmol-Srv/sigil/blob/56a07df7bcbb851f9dcc5fe1581b359a1b893b49/README.md](https://github.com/Anmol-Srv/sigil/blob/56a07df7bcbb851f9dcc5fe1581b359a1b893b49/README.md)

## Limits and data handling

Queries and candidate facts go to TypeSafe when Jev is enabled; memory stays in your Postgres.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 56a07df7bcbb](https://github.com/Anmol-Srv/sigil/tree/56a07df7bcbb851f9dcc5fe1581b359a1b893b49). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
