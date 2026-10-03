# jev-cli (shetautnetjer)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Clean-room CLI for TypeSafe System One Decision Contracts, search, and benchmarks (distinct from tumf/shaharia-lab jev-cli).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shetautnetjer/jev-cli) |
| Maintainer | [shetautnetjer](https://github.com/shetautnetjer). Independently curated. |
| Format | Python clean-room CLI for Decision Contracts (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/shetautnetjer/jev-cli/blob/3563bc9cfd142e54cb5f4adcb2f0de200a9b0bbb/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from tumf/jev-cli and shaharia-lab/jev-cli (same short name, different packaging and scope). Live install/inference not run on the review host. |

## When to use

Use for Decision Contract scaffolding (`jev init`/`jev run`) and local text/code search helpers. Prefer tumf/jev-cli for a dependency-light PyPI+MCP package, or shaharia-lab/jev-cli for a Rust CLI/MCP.

## How it works

Decision Contracts are the reusable capability; Jev is one execution provider. CLI scaffolds YAML contracts, runs them with state files, and supports ad-hoc Choice asks plus local search specialists.

## Get started

```sh
git clone https://github.com/shetautnetjer/jev-cli.git
cd jev-cli
git checkout 3563bc9cfd142e54cb5f4adcb2f0de200a9b0bbb
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 3563bc9cfd14](https://github.com/shetautnetjer/jev-cli/tree/3563bc9cfd142e54cb5f4adcb2f0de200a9b0bbb). AI-assisted README and license inspection; install/live paths not executed.
