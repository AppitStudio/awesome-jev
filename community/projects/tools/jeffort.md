# Jeffort

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin: TypeSafe Jev scores each prompt and sets Claude effort without touching the model (MIT).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/andrewstephenson-v1/Jeffort) |
| Maintainer | [andrewstephenson-v1](https://github.com/andrewstephenson-v1). Independently curated. |
| Format | Claude Code plugin: TypeSafe Jev picks per-turn effort (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/andrewstephenson-v1/Jeffort/blob/d2f47c8d773c26e665cf9592da7bcfb94dccf275/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from jev-effort, jev-opus, and other effort routers—Claude Code marketplace plugin with UI band/pane and cache-aware savings estimates. Only rewrites effort on listed Claude models where cache survives effort changes. Live install/inference not run on the review host. |

## When to use

Use when you want automatic Claude Code effort selection from Jev without rewriting the model. Prefer jev-effort/jev-opus when you need different hook stacks or OpenRouter-first setups.

## How it works

Four narrow Jev questions score the prompt; Jeffort maps to an effort level and rewrites only supported Claude models. Low confidence or API errors leave effort alone.

## Get started

```sh
git clone https://github.com/andrewstephenson-v1/Jeffort.git
cd Jeffort
git checkout d2f47c8d773c26e665cf9592da7bcfb94dccf275
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit d2f47c8d773c](https://github.com/andrewstephenson-v1/Jeffort/tree/d2f47c8d773c26e665cf9592da7bcfb94dccf275). AI-assisted README and license inspection; install/live paths not executed.
