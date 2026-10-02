# openjev-rs

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Rust libraries for local typed decisions from frozen GGUF logits (OpenJev/SemIf readout); CLI/HTTP moved to codesoda/systemone.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/codesoda/openjev-rs) |
| Maintainer | [codesoda](https://github.com/codesoda). Independently curated. |
| Format | Rust · openjev-core + openjev-llama crates (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/codesoda/openjev-rs/blob/8452ef0e5890497deb2cec95f16dc8d94d0c0c02/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Libraries only; CLI/HTTP live in codesoda/systemone. Independent of TypeSafe/SemIf. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/codesoda/openjev-rs.git
cd openjev-rs
git checkout 8452ef0e5890497deb2cec95f16dc8d94d0c0c02
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 8452ef0e5890](https://github.com/codesoda/openjev-rs/tree/8452ef0e5890497deb2cec95f16dc8d94d0c0c02). AI-assisted README and license inspection; install/live paths not executed.
