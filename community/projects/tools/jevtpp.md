# JevT++

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

C++20 library for typed model-backed routing, classification, and scoring: compile-time schemas, inspectable distributions, optional local Laya (ONNX Runtime / ggml) or remote backends.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wiatrM/jevtpp) |
| Maintainer | [wiatrM](https://github.com/wiatrM). Independently curated. |
| Format | C++20 library (`jevt`) with optional adapters, metrics, and docs site. |
| Requirements | C++20 toolchain; optional ONNX Runtime or ggml for local Laya; optional remote inference credentials. |
| License | [MIT](https://github.com/wiatrM/jevtpp/blob/241b72e46c30aed9f988bd1212c171bc0e0eb7da/LICENSE). |
| Disclosure | Independent open-source library—not proprietary Jev or an official TypeSafe SDK (upstream README). AI-assisted catalog review; no affiliation. Listing is not an endorsement. Build/inference demos not run on the review host. |

## When to use

Use for **in-process C++ typed decisions** with strong types and optional local Laya. Prefer official/hosted TypeSafe clients when you only need cloud Jev from another language.

## How it works

Define schemas/options at compile time; supply runtime context; get enums, P(true), scores, and full distributions. Optional decision graphs and skill runtime load versioned JSON graphs without recompiling operators.

## Get started

```sh
git clone https://github.com/wiatrM/jevtpp.git
cd jevtpp
git checkout 241b72e46c30aed9f988bd1212c171bc0e0eb7da
# Follow upstream Build and test / docs: https://wiatrm.github.io/jevtpp/
```

## Examples and demos

- `examples/laya_routing_demo.cpp` and skill/warehouse configs.
- Mario research demo (upstream video; not a completed-game claim).

## Limits and data handling

Local backends keep inference in-process; remote backends send context off-box. Model quality depends on Laya weights and task. Decision-graph primitives do not by themselves guarantee safe actions.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 241b72e](https://github.com/wiatrM/jevtpp/tree/241b72e46c30aed9f988bd1212c171bc0e0eb7da). AI-assisted README and LICENSE inspection; build/tests not executed.
