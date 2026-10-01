# openwebui-jev-style-decisions

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial Open WebUI plugin for JEV-style typed decisions with per-option probabilities from a local Ollama model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tamaker/openwebui-jev-style-decisions) |
| Maintainer | [tamaker](https://github.com/tamaker). Independently curated. |
| Format | Open WebUI plugin (MIT) |
| Requirements | See upstream README; TypeSafe/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/tamaker/openwebui-jev-style-decisions/blob/8fca820a68df7b2e3a6ec88116e7082c0080eb53/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/tamaker/openwebui-jev-style-decisions.git
cd openwebui-jev-style-decisions
git checkout 8fca820a68df7b2e3a6ec88116e7082c0080eb53
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 8fca820a68df](https://github.com/tamaker/openwebui-jev-style-decisions/tree/8fca820a68df7b2e3a6ec88116e7082c0080eb53). AI-assisted README and license inspection; install/live paths not executed.
