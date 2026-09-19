# pg_typesafe

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Call TypeSafe Jev Choice, Noul, and Score from PostgreSQL through a C extension with libcurl, including batched multi-text helpers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/giuliosmall/pg_typesafe) |
| Maintainer | [giuliosmall](https://github.com/giuliosmall) (Giulio Piccolo). Independently curated; this entry is not an upstream submission or endorsement. Upstream states it is unaffiliated with TypeSafe AI and the PostgreSQL Global Development Group. |
| Format | PostgreSQL extension (`CREATE EXTENSION typesafe`) implemented in C with libcurl; SQL wrappers and a mock-response GUC for offline tests. |
| Requirements | Upstream targets PostgreSQL 16–17 and libcurl 7.61+. Building needs PGXS/`pg_config` and write access to `pkglibdir` (often `sudo make install`). Live use needs server HTTPS access and `TYPESAFE_API_KEY` on the Postgres process (or `typesafe.api_key_file`). Pre-alpha **0.0.1**. |
| License | [MIT](https://github.com/giuliosmall/pg_typesafe/blob/4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a/LICENSE). |

## When to use

Use it when you want categorical Jev judgments inside SQL and prefer a native C extension with explicit `EXECUTE` grants and batched `*_many` helpers over PL/Python. Prefer [pg-jev](pg-jev.md) when you already run that PL/Python extension or need its `jev_*` SQL surface and documented regression container.

**Distinct from catalogued [pg-jev](pg-jev.md):** different author and stack (C + libcurl vs PL/Python), different function names (`typesafe_*` vs `jev_*`), and a batch-oriented `detect_many` / `classify_many` path. Do not install both casually into the same cluster without reviewing GUC and privilege differences.

## How it works

The [C implementation](https://github.com/giuliosmall/pg_typesafe/blob/4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a/typesafe.c) posts to `https://api.typesafe.ai/v1/systemone` with default model `jev-latest`. Scalar helpers issue one HTTP call per invocation; `typesafe_detect_many` / `typesafe_classify_many` chunk arrays with `typesafe.batch_size` (default 32) and overlapping concurrency. `typesafe.mock_response` injects JSON for network-free SQL tests. Default privileges revoke `EXECUTE` from `PUBLIC`.

## Get started

```sh
git clone https://github.com/giuliosmall/pg_typesafe.git
cd pg_typesafe
git checkout 4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a
make
make install   # often needs sudo / write access to pkglibdir
```

```sql
CREATE EXTENSION typesafe;
-- Live: set TYPESAFE_API_KEY on the server process, then:
-- SELECT typesafe_noul('Help! payouts failing.', 'Does this convey urgency?');
```

Offline mock path (no TypeSafe network) is illustrated in [test/ci_mock.sql](https://github.com/giuliosmall/pg_typesafe/blob/4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a/test/ci_mock.sql). This listing did not build against PostgreSQL headers or run the extension (no `pg_config` / Postgres in the review environment).

## Examples and demos

- [examples/311.sql](https://github.com/giuliosmall/pg_typesafe/blob/4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a/examples/311.sql): NYC 311 resolution classification demo (live Jev; not run here).
- [expected/typesafe.out](https://github.com/giuliosmall/pg_typesafe/blob/4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a/expected/typesafe.out) and [test/ci.sh](https://github.com/giuliosmall/pg_typesafe/blob/4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a/test/ci.sh): upstream CI/regression assets.
- Upstream README timing claims for `detect_many` vs per-row calls are maintainer measurements, not reproduced here.

## Limits and data handling

SQL text and questions go to TypeSafe (or the configured HTTPS endpoint) when not mocked. Keys must stay out of shared SQL; session `SET typesafe.api_key` can appear in logs. Pre-alpha surface may change. Retries honor 429/529; responses are capped. Batching reduces round trips but still submits every distinct text you pass. Upstream speed claims were not reproduced.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 4b5bfc1](https://github.com/giuliosmall/pg_typesafe/tree/4b5bfc1df11b18c3f07bb10804eeb47e4508ec6a): extension **0.0.1**, MIT. AI-assisted source review of `typesafe.c`, SQL control files, mock CI SQL, README, and license. PostgreSQL build/install and live inference were **not** executed (`pg_config` unavailable). Compared against catalogued [pg-jev](pg-jev.md) for de-duplication.

Related: [pg-jev](pg-jev.md).
