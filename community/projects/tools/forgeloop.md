# ForgeLoop by Cassio Marques Campos (contracts, verification gates and evidence for AI coding work, with Jev for bounded semantic checks)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A CLI and protocol that governs AI-assisted engineering: you declare a task contract and the paths it may change, route the work, run checks through recorded command receipts, and only close the task when the validator accepts current evidence. Jev supplies bounded semantic checkpoints; ForgeLoop owns gates, evidence and completion. Optional paid ForgeLoop Cloud adds a team dashboard and PR checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cassiomc1/forgeloop) |
| Maintainer | [cassiomc1](https://github.com/cassiomc1). Independently curated. |
| Format | Node.js CLI (npm `@cassiomc1/forgeloop`) + protocol |
| Requirements | Node.js 24.19.0+ with `node:sqlite`; a `TYPESAFE_API_KEY` in the environment for semantic checkpoints (ForgeLoop never stores it). Free for noncommercial use; commercial use needs a $199/developer/year license (checked 2026-11-22 on forgeloop.monster). |
| License | [PolyForm Noncommercial 1.0.0 (reference runtime; commercial license $199/developer/year) + Apache-2.0 (protocol spec, schemas, conformance suite, verifier)](https://github.com/cassiomc1/forgeloop/blob/d0df7e7a9fbec726adfe742fdbdfaaf56a511258/LICENSING.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/unsec_33/status/2124264984066601146)). |
| Jev evidence | [`src/adapters/typesafe/client.js`](https://github.com/cassiomc1/forgeloop/blob/d0df7e7a9fbec726adfe742fdbdfaaf56a511258/src/adapters/typesafe/client.js) at the pinned commit. |

## When to use

- Put AI coding agents behind explicit task scopes, verification gates and an auditable evidence trail.
- Mismatch: commercial teams that cannot buy a license; the reference runtime is PolyForm Noncommercial (only the protocol, schemas and verifier are Apache-2.0).

## How it works

`src/adapters/typesafe/client.js` and `src/adapters/typesafe/engine.js` send bounded typed questions to TypeSafe's System One API at semantic checkpoints; the deterministic control plane decides routing, gates and completion from recorded evidence, so a model's confidence alone cannot close a task. Integration evidence: [`src/adapters/typesafe/client.js`](https://github.com/cassiomc1/forgeloop/blob/d0df7e7a9fbec726adfe742fdbdfaaf56a511258/src/adapters/typesafe/client.js).

## Get started

Install the CLI, set your TypeSafe key, initialise the repository and start a task contract.

```sh
npm install --global @cassiomc1/forgeloop
export TYPESAFE_API_KEY=...
forgeloop init
forgeloop doctor
forgeloop task-create --task hello --claim src
forgeloop contract-create --task hello --preset feature
forgeloop next --task hello
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/cassiomc1/forgeloop/blob/d0df7e7a9fbec726adfe742fdbdfaaf56a511258/README.md](https://github.com/cassiomc1/forgeloop/blob/d0df7e7a9fbec726adfe742fdbdfaaf56a511258/README.md)
- Licensing by path: [github.com/cassiomc1/forgeloop/blob/d0df7e7a9fbec726adfe742fdbdfaaf56a511258/LICENSING.md](https://github.com/cassiomc1/forgeloop/blob/d0df7e7a9fbec726adfe742fdbdfaaf56a511258/LICENSING.md)
- Product site and pricing: [forgeloop.monster/](https://forgeloop.monster/)
- Launch post on X: [x.com/unsec_33/status/2124264984066601146](https://x.com/unsec_33/status/2124264984066601146)

## Limits and data handling

Semantic checkpoint text (task context and claims) is sent to TypeSafe with your key. Evidence is self-reported by the CLI; ForgeLoop Cloud is a paid hosted service. The MCP companion has restricted distribution. Not OSI open source as a whole.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit d0df7e7a9fbe](https://github.com/cassiomc1/forgeloop/tree/d0df7e7a9fbec726adfe742fdbdfaaf56a511258). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
