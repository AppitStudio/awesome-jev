# metajev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Cache the decision, compute the policy: record System One distributions under state/question/model keys; change thresholds without re-running Jev (MIT).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/YYTbit/metajev) |
| Maintainer | [YYTbit](https://github.com/YYTbit). Independently curated. |
| Format | Python decision-record store + policy layer (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/YYTbit/metajev/blob/f4246730b4cfedf5d61f1ce155ab52f96d93d3a0/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Not on PyPI yet (install from git). Separates decision records from policy thresholds. Live install/inference not run on the review host. |

## When to use

Use when thresholds and review bands change often and you want to avoid re-running Jev over historical states. Prefer direct SDK calls for one-shot scripts.

## How it works

Client asks a provider (TypeSafe/sglang/openai-compat/mock), stores the full distribution under sha256(state, question, provider, model), then evaluates a separate policy object.

## Get started

```sh
git clone https://github.com/YYTbit/metajev.git
cd metajev
git checkout f4246730b4cfedf5d61f1ce155ab52f96d93d3a0
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit f4246730b4cf](https://github.com/YYTbit/metajev/tree/f4246730b4cfedf5d61f1ce155ab52f96d93d3a0). AI-assisted README and license inspection; install/live paths not executed.
