# jev-tools (Rcidshacker)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin: OpenJev/Codiv for cheap typed agent judgments (edit hook, skill picker, review pre-check); distinct from CMaintz/jev-tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rcidshacker/jev-tools) |
| Maintainer | [Rcidshacker](https://github.com/Rcidshacker). Independently curated. |
| Format | Claude Code plugin (MIT) |
| Requirements | See upstream README; TypeSafe/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/Rcidshacker/jev-tools/blob/d88bca4208d089cfbfd735bad2f4ed171238d736/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

## Get started

```sh
git clone https://github.com/Rcidshacker/jev-tools.git
cd jev-tools
git checkout d88bca4208d089cfbfd735bad2f4ed171238d736
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit d88bca4208d0](https://github.com/Rcidshacker/jev-tools/tree/d88bca4208d089cfbfd735bad2f4ed171238d736). AI-assisted README and license inspection; install/live paths not executed.
