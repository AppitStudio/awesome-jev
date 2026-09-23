# jevql

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

psql-style client that adds TypeSafe Jev `jev()`, `jev_prob`, `jev_choice`, and `jev_score` to queries against an unmodified PostgreSQL, with no extension or superuser access.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kylemclaren/jevql) |
| Maintainer | [kylemclaren](https://github.com/kylemclaren). Self-submission by the maintainer. |
| Format | Go CLI and REPL (`jevql`), MCP server (`jevql mcp`), shared HTTP node (`jevql serve`), and Go, TypeScript (`npm i jevql`), and Python (`pip install jevql`) SDKs. |
| Requirements | Any reachable PostgreSQL and `TYPESAFE_API_KEY` for live judgments. Homebrew (`kylemclaren/tap/jevql`) or release binaries for macOS/Linux arm64/amd64; source builds need Go 1.23+ and a C compiler (CGO, bundled libpg_query). |
| License | [MIT](https://github.com/kylemclaren/jevql/blob/274532af852e8edfb7715ec6dca1113e589cb191/LICENSE). |
| Disclosure | Submitted by the author with AI assistance (Claude Code). Listing is not an endorsement. |

## When to use

Use it when the rows already live in Postgres and you want to filter, rank, or group them by a plain-language condition without installing an extension, for example on a managed database where `CREATE EXTENSION` is unavailable. Agents can use the same surface through the MCP server. Prefer [pg-jev](pg-jev.md) or [pg_typesafe](pg-typesafe.md) when you want the functions inside the server so that any Postgres client can call them, [JevSQL](jevsql.md) for SQLite, and [duckdb-jev](duckdb-jev.md) for DuckDB.

## How it works

jevql parses each statement with libpg_query. Statements without `jev_*` calls go to Postgres unchanged. Otherwise it rewrites the query into plain SQL that collects candidate rows, sends those rows to TypeSafe in batches ([`internal/typesafe/client.go`](https://github.com/kylemclaren/jevql/blob/274532af852e8edfb7715ec6dca1113e589cb191/internal/typesafe/client.go)), caches repeated judgments, and applies the Jev filter, sort, or group in the client ([`internal/exec/exec.go`](https://github.com/kylemclaren/jevql/blob/274532af852e8edfb7715ec6dca1113e589cb191/internal/exec/exec.go)). ORDER BY and LIMIT are pushed to Postgres only when no Jev predicate or sort key depends on them. The SDKs and `jevql serve` share one JSON protocol ([`sdk/PROTOCOL.md`](https://github.com/kylemclaren/jevql/blob/274532af852e8edfb7715ec6dca1113e589cb191/sdk/PROTOCOL.md)).

## Get started

```sh
brew install kylemclaren/tap/jevql
export TYPESAFE_API_KEY=tsk_...
export DATABASE_URL=postgres://user:pass@localhost:5432/app

jevql --explain -c "SELECT name FROM people WHERE jev(people, 'could work from home')"  # plan and cost estimate, no API calls
jevql -c "SELECT name FROM people WHERE jev(people, 'could work from home') LIMIT 20"   # live: sends row contents to TypeSafe
```

`--explain` makes no TypeSafe requests. A live query sends the judged columns to TypeSafe and may incur charges. `-v` prints the rows judged, requests made, cache hits, tokens, and estimated cost.

## Examples and demos

- [Hosted playground](https://jevql.fly.dev/playground) with example queries over a sample dataset.
- README "Things to try" section with sample queries and the full SQL surface.
- `claude mcp add jevql -- jevql mcp` exposes `query`, `explain`, `judge`, `list_tables`, and `describe_table` tools. The MCP server is read-only unless started with `--allow-writes`.

## Limits and data handling

Every column of the judged alias, or the column list you give, is sent over HTTPS to TypeSafe. Use the column-list form or `--columns` to send less. `--max-rows` (default 2500) aborts the query before any TypeSafe call if more rows than that would be judged. The server never sees `jev()`, so the same SQL sent through psql or JDBC fails. The optional saved config `~/.config/jevql/env` stores the API key and database URL in plain text with mode `0600`. Cost figures are estimates.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 274532a](https://github.com/kylemclaren/jevql/tree/274532af852e8edfb7715ec6dca1113e589cb191) by the maintainer. `go test ./...` passes offline, using a mocked TypeSafe client and skipping the Postgres execution tests unless `PGTEST_URL` is set. Live queries against Postgres 17 and the TypeSafe API were run during development. This review makes no independent quality or accuracy claims.

Related: [pg-jev](pg-jev.md), [pg_typesafe](pg-typesafe.md), [JevSQL](jevsql.md), [duckdb-jev](duckdb-jev.md), [mysql-ailike](mysql-ailike.md).
