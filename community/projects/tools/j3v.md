# J3v

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Rust compiler/runtime that distills Laya-style System One schemas into edge artifacts for Pi/MCU targets ("J3v is to Jev as k3s is to k8s"), returning calibrated probabilities and speaking a System One HTTP shape—with optional cascade to hosted Laya/Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JGalego/J3v) |
| Maintainer | [JGalego](https://github.com/JGalego). Independently curated. |
| Format | Rust crates (`j3v` CLI/compiler) + schemas/firmware demos. |
| Requirements | Linux install or Rust toolchain; Python only at compile time for teacher labeling. |
| License | [MIT](https://github.com/JGalego/J3v/blob/9636aaf731150bda67cc2933d48230e5bd07f485/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Compile/serve/predict not executed on the review host. |

## When to use

Use it to **compile typed decision schemas for edge devices** with accuracy/ECE/flash budgets. Prefer hosted TypeSafe Jev APIs when you do not need an on-device artifact.

## How it works

`j3v compile` takes a schema of Choice/Score/Noul questions, distills from a Laya teacher, fits temperature scaling, and refuses artifacts that miss bounds. Runtime cascade can escalate from MCU → Pi → hosted Laya/Jev when confidence is low.

## Get started

```sh
curl -fsSL https://raw.githubusercontent.com/JGalego/J3v/9636aaf731150bda67cc2933d48230e5bd07f485/install.sh | J3V_MODELS=j3v-models sh
# or from source at the reviewed tip:
git clone https://github.com/JGalego/J3v.git && cd J3v
git checkout 9636aaf731150bda67cc2933d48230e5bd07f485
# cargo install --path crates/j3v   # not run here
```

## Examples and demos

- README `j3v predict` / `j3v serve` support-triage example.
- `demo/getting-started.gif`; `schemas/`.

## Limits and data handling

Compile-time labeling may call a teacher model. Hosted cascade sends System One payloads to the configured endpoint. Edge accuracy depends on schema/data—see upstream ECE gates.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 9636aaf](https://github.com/JGalego/J3v/tree/9636aaf731150bda67cc2933d48230e5bd07f485). AI-assisted README inspection. No compile/serve executed.

Related: [openjev-sglang](openjev-sglang.md), [jev-calibrate](jev-calibrate.md).
