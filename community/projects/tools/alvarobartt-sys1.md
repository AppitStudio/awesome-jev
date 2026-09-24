# sys1 (alvarobartt)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Rust server that exposes a System One–compatible HTTP API for open decision models such as Laya, so Jev-shaped clients can call a local `/v1/systemone` endpoint.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/alvarobartt/sys1) |
| Maintainer | [alvarobartt](https://github.com/alvarobartt). Independently curated. |
| Format | Rust CLI/server (`cargo install sys1`). |
| Requirements | Rust toolchain for build; CPU/Metal/CUDA feature flags; Hugging Face model id (e.g. `convaiinnovations/laya`). |
| License | [Apache-2.0](https://github.com/alvarobartt/sys1/blob/3dfd9166bd14fc492f46ebe983a5f3c72abff52a/LICENSE) (LICENSE file present; GitHub SPDX may show NOASSERTION). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live inference not run. Distinct from hraness/sys1. |

## When to use

Use to **serve** open decision models behind a Jev-compatible HTTP API on your own hardware. Prefer hosted TypeSafe Jev when you want the managed cloud path.

## How it works

`sys1` loads a decision model (Candle + tokenizers) and answers typed System One requests at `/v1/systemone` (and `/v1/decide`) with batching and CPU/CUDA/Metal backends (per README).

## Get started

```sh
cargo install sys1 --features cpu
sys1 --model-id convaiinnovations/laya --dtype auto
# curl http://localhost:3000/v1/systemone ...
```

Pin review tip: `3dfd9166bd14fc492f46ebe983a5f3c72abff52a`.

## Examples and demos

- README curl examples against `/v1/systemone`.

## Limits and data handling

Local inference keeps traffic on your host unless you expose the port. Model/dataset licenses are separate from the Apache-2.0 server code.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 3dfd916](https://github.com/alvarobartt/sys1/tree/3dfd9166bd14fc492f46ebe983a5f3c72abff52a). AI-assisted README and LICENSE inspection; live model serve not run on the review host.
