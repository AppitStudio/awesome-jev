# anofox-decide

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

DuckDB extension: NL predicates and answer sets via TypeSafe Jev or local open System One–compatible models (remote opt-in).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DataZooDE/anofox-decide) |
| Maintainer | [DataZooDE](https://github.com/DataZooDE). Independently curated. |
| Format | C++/DuckDB · extension (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/DataZooDE/anofox-decide/blob/835d3f7b8b817e0992a6e20d786d2925e2c3fb14/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/DataZooDE/anofox-decide.git
cd anofox-decide
git checkout 835d3f7b8b817e0992a6e20d786d2925e2c3fb14
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 835d3f7b8b81](https://github.com/DataZooDE/anofox-decide/tree/835d3f7b8b817e0992a6e20d786d2925e2c3fb14). AI-assisted README and license inspection; install/live paths not executed.
