# dbt-decisions (dbt package for System One / Jev-class decisions inside SQL)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

dbt Labs package that brings System One / Jev-class decisions into SQL models: DuckDB can load the community `jev` extension, macros such as `load_jev` point live runs at TypeSafe via `TYPESAFE_API_KEY`, and examples show call-fit analytics scored with Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dbt-labs/dbt-decisions) |
| Maintainer | [dbt-labs](https://github.com/dbt-labs). Independently curated. |
| Format | dbt package with DuckDB/BigQuery helpers (Apache-2.0) |
| Requirements | dbt, a supported warehouse (DuckDB examples use the community `jev` extension), and `TYPESAFE_API_KEY` for live calls (or `DECISIONS_API_URL` for mock/offline). |
| License | [Apache-2.0](https://github.com/dbt-labs/dbt-decisions/blob/94f1c98068364d1fdabfacaea02147b3cc00a47d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`examples/jev_analytics/3_call_fit/macros/jev.sql`](https://github.com/dbt-labs/dbt-decisions/blob/94f1c98068364d1fdabfacaea02147b3cc00a47d/examples/jev_analytics/3_call_fit/macros/jev.sql) at the pinned commit. |

## When to use

- Score rows inside dbt models with typed System One questions.
- Keep secrets out of SQL by reading TYPESAFE_API_KEY from the environment.
- Mismatch: warehouse support and the DuckDB extension must be installed; mock mode needs DECISIONS_API_URL.

## How it works

The `load_jev` macro installs/loads the DuckDB `jev` extension and, unless a mock URL is set, leaves the extension to read `TYPESAFE_API_KEY` from the environment for live TypeSafe calls. Integration evidence: [`examples/jev_analytics/3_call_fit/macros/jev.sql`](https://github.com/dbt-labs/dbt-decisions/blob/94f1c98068364d1fdabfacaea02147b3cc00a47d/examples/jev_analytics/3_call_fit/macros/jev.sql).

## Get started

From the upstream README (not run on the review host):

```sh
# from the call_fit example (not run on the review host)
export TYPESAFE_API_KEY=...
cd examples/jev_analytics/3_call_fit && dbt run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Jev macro: [github.com/dbt-labs/dbt-decisions/blob/94f1c98068364d1fdabfacaea02147b3cc00a47d/examples/jev_analytics/3_call_fit/macros/jev.sql](https://github.com/dbt-labs/dbt-decisions/blob/94f1c98068364d1fdabfacaea02147b3cc00a47d/examples/jev_analytics/3_call_fit/macros/jev.sql)
- README: [github.com/dbt-labs/dbt-decisions/blob/94f1c98068364d1fdabfacaea02147b3cc00a47d/README.md](https://github.com/dbt-labs/dbt-decisions/blob/94f1c98068364d1fdabfacaea02147b3cc00a47d/README.md)

## Limits and data handling

Row text and questions leave the warehouse toward TypeSafe on your key. Mock mode never hits TypeSafe.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 94f1c9806836](https://github.com/dbt-labs/dbt-decisions/tree/94f1c98068364d1fdabfacaea02147b3cc00a47d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
