# jevai

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial async Rust client for TypeSafe System One (noul/choice/score) against docs.typesafe.ai.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tiendvlp/jevai) |
| Maintainer | [tiendvlp](https://github.com/tiendvlp). Independently curated. |
| Format | Unofficial async Rust client for TypeSafe System One (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/tiendvlp/jevai/blob/749aa000ea7e728bba68c3e5137d74408f0a942d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Unofficial community crate—not an official TypeSafe SDK (official SDKs are Python/TypeScript). Live install/inference not run on the review host. |

## When to use

Use when embedding TypeSafe System One in a Rust async service. Prefer official Python/TS SDKs when those languages fit.

## How it works

JevClient posts one state plus named typed questions; API evaluates in parallel. Supports noul, choice, and score criteria builders.

## Get started

```sh
git clone https://github.com/tiendvlp/jevai.git
cd jevai
git checkout 749aa000ea7e728bba68c3e5137d74408f0a942d
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 749aa000ea7e](https://github.com/tiendvlp/jevai/tree/749aa000ea7e728bba68c3e5137d74408f0a942d). AI-assisted README and license inspection; install/live paths not executed.
