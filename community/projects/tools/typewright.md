# TypeWright

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Declarative compiler: state/decisions → frozen typed Jev JSON program via DSPy/GEPA (alpha; no live accuracy claims yet).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jev-Engineering/TypeWright) |
| Maintainer | [Jev-Engineering](https://github.com/Jev-Engineering). Independently curated. |
| Format | Python declarative compiler + JSON program runtime (MIT, alpha 0.1) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/Jev-Engineering/TypeWright/blob/67a53ee047dd9a14a70abdf13641974087d42457/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Alpha 0.1. Upstream states no live TypeSafe/DSPy/GEPA accuracy study yet; mock metrics are pipeline checks, not Jev results. Live install/inference not run on the review host. |

## When to use

Use when you want an artifact-first path from a declared decision contract to a frozen JSON program for typed Jev questions. Prefer direct SDK calls when you do not need a compiler pipeline.

## How it works

You declare state, decisions, and labeled examples; TypeWright searches within that contract (DSPy architect + GEPA adapter), fits review policy, and freezes a checksummed JSON program the runtime loads without DSPy.

## Get started

```sh
git clone https://github.com/Jev-Engineering/TypeWright.git
cd TypeWright
git checkout 67a53ee047dd9a14a70abdf13641974087d42457
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 67a53ee047dd](https://github.com/Jev-Engineering/TypeWright/tree/67a53ee047dd9a14a70abdf13641974087d42457). AI-assisted README and license inspection; install/live paths not executed.
