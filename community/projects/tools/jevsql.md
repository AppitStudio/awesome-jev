# JevSQL

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

SQLite-oriented SQL middleware and control plane that adds TypeSafe Jev judgments (match, pick, rank, bool, choice, and related helpers) with batching, caching, budgets, and review queues—distinct from PostgreSQL extensions such as pg-jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/EugeneBoondock/jevsql) |
| Maintainer | [EugeneBoondock](https://github.com/EugeneBoondock). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript npm package `jevsql` **0.1.0** — Node library and CLI (`jevsql`) with zero declared runtime dependencies beyond the package itself. |
| Requirements | Node.js (engines as published). Live judgments need a TypeSafe API key. Offline tests use local mock servers. Optional native-row and streaming-money paths are documented separately upstream. |
| License | [MIT](https://github.com/EugeneBoondock/jevsql/blob/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/LICENSE). |

## When to use

Use it when you want semantic predicates and decision tables over SQLite (or governed query templates) with inspectable refresh history, rather than embedding Jev only in application code. Prefer [pg-jev](pg-jev.md) or [pg_typesafe](pg-typesafe.md) when your workload is already inside PostgreSQL.

## How it works

The row-decision engine runs SQL, batches Jev requests, caches judgments, and can materialize decision tables with refresh that re-pays only for changed inputs. The control plane reviews database events and returns typed receipts without executing arbitrary SQL; it expects a pinned model version by default. Client evaluation lives in modules such as [`src/client.mjs`](https://github.com/EugeneBoondock/jevsql/blob/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/src/client.mjs) and [`src/decision-service.mjs`](https://github.com/EugeneBoondock/jevsql/blob/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/src/decision-service.mjs). Default row-engine model is the moving `jev-latest` alias unless pinned.

## Get started

```sh
git clone https://github.com/EugeneBoondock/jevsql.git
cd jevsql
git checkout 45f3862f679c064e371a800c2fcc0c5b8b90c6c6
npm install --ignore-scripts
npm test
node examples/contrast.mjs --offline
```

Live demos and evaluate paths call TypeSafe. This listing did not run live API examples or attach external databases beyond what the offline suite mocks.

## Examples and demos

- [`examples/`](https://github.com/EugeneBoondock/jevsql/tree/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/examples): contrast, workflows, control-plane, and showcase tours (use `--offline` where documented).
- [`test/`](https://github.com/EugeneBoondock/jevsql/tree/45f3862f679c064e371a800c2fcc0c5b8b90c6c6/test): engine, client, decision tables, control plane, and adapters with mock servers.
- Upstream README contrast tables and `jevsql-demo.mp4` are maintainer illustrations, not catalog-run accuracy claims.

## Limits and data handling

Row text and constructed states leave the machine on live Jev paths. Upstream is explicit that fixture comparisons demonstrate software behavior, not adjudicated model accuracy on production corpora. Destructive SQL guards and tenant policies are local software checks—review them for your threat model. PostgreSQL/MySQL adapter CI paths were not exercised on this host.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 45f3862](https://github.com/EugeneBoondock/jevsql/tree/45f3862f679c064e371a800c2fcc0c5b8b90c6c6): `jevsql` **0.1.0**, MIT. AI-assisted source review of client/engine/control-plane modules, README, and license. On Node.js 24.8.0, **`npm test`: 400 passed, 2 skipped**. No live TypeSafe calls or external database migrations were performed.

Related: [pg-jev](pg-jev.md), [pg_typesafe](pg-typesafe.md), [llama-index-jev](llama-index-jev.md).
