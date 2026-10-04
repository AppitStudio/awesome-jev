# Conjevture

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Exact logic for uncertain answers: TypeScript library combining Boolean rules with Jev Noul/Choice probabilities (zero runtime deps; MIT).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nibzard/conjevture) |
| Maintainer | [nibzard](https://github.com/nibzard). Independently curated. |
| Format | TypeScript probability/Boolean library + Jev converters (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/nibzard/conjevture/blob/c54c02ac05ac9048db100d0906df5fee26e48a23/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Core library makes no network requests; optional Night Shift browser game can use live TypeSafe Jev or recorded responses. Live install/inference not run on the review host. |

## When to use

Use when you need exact Boolean probability composition over Jev (or other) judgments. Prefer raw SDK calls when you only need a single Noul/Choice without circuits.

## How it works

You declare variables, Bernoulli/joint models, and Boolean gates; evaluate returns rule satisfaction probability. conjevture/jev converters accept existing client answers without calling TypeSafe themselves.

## Get started

```sh
git clone https://github.com/nibzard/conjevture.git
cd conjevture
git checkout c54c02ac05ac9048db100d0906df5fee26e48a23
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit c54c02ac05ac](https://github.com/nibzard/conjevture/tree/c54c02ac05ac9048db100d0906df5fee26e48a23). AI-assisted README and license inspection; install/live paths not executed.
