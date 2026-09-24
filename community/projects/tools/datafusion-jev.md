# datafusion-jev

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Apache DataFusion SQL UDF crate: `prompt_jev` sends row text to TypeSafe System One and returns typed Noul/Choice/Score answers (you supply the HTTP client).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hotdata-dev/datafusion-jev) |
| Maintainer | [hotdata-dev](https://github.com/hotdata-dev). Independently curated. |
| Format | Rust crate for DataFusion 55 (`prompt_jev` SQL function). |
| Requirements | Rust; DataFusion 55; implement `JevClient` HTTP POST to `https://api.typesafe.ai/v1/systemone` with your API key. |
| License | **MIT OR Apache-2.0** per [`Cargo.toml`](https://github.com/hotdata-dev/datafusion-jev/blob/7164f5d168f653f1efaf414f9fb689b8ac09748d/Cargo.toml) (no standalone LICENSE file in tree). |
| Disclosure | AI-assisted catalog review; no affiliation. No live SQL/Jev execution on the review host. |

## When to use

Use it to **classify or score text columns inside DataFusion SQL** with calibrated Jev answers. Prefer application-level SDKs when you are not on DataFusion.

## How it works

You implement `JevClient::request`, register it once, and run SQL through `datafusion_jev::sql` so `prompt_jev(text, 'question', options…)` batches rows to System One. Retries map `Unavailable` vs fatal errors per README.

## Get started

```sh
git clone https://github.com/hotdata-dev/datafusion-jev.git
cd datafusion-jev
git checkout 7164f5d168f653f1efaf414f9fb689b8ac09748d
# add as crate dependency; implement JevClient; register + datafusion_jev::sql(...)
```

## Examples and demos

- README SQL examples (complaint Choice, refund Noul, …).
- Client trait sketch in README.

## Limits and data handling

Row text leaves your process on each Jev call—keep keys server-side. Plain `ctx.sql` will not parse `prompt_jev` options; use the crate's SQL entrypoints.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 7164f5d](https://github.com/hotdata-dev/datafusion-jev/tree/7164f5d168f653f1efaf414f9fb689b8ac09748d). AI-assisted README/`Cargo.toml` inspection. No live DataFusion/TypeSafe run.

Related: [TypeSafe Go](typesafe-go.md), [daf-jev](daf-jev.md).
