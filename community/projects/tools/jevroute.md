# jevroute

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code skill-hint hook via TypeSafe Jev—STOPPED after baseline pilot (69/75 without hints); published negative findings.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maxkulish/jevroute) |
| Maintainer | [maxkulish](https://github.com/maxkulish). Independently curated. |
| Format | Rust Claude Code UserPromptSubmit hook experiment (MIT; stopped) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/maxkulish/jevroute/blob/7efc45e96c0b0e3035b501431a2d9f0fa19e5fc3/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. STOPPED 2026-10-03 after baseline pilot (69/75 correct with no hint) met the stop rule—no binary built. Valuable negative-result write-up in docs/findings. Live install/inference not run on the review host. |

## When to use

Read for evaluation design and negative findings about skill-hint hooks. Do not expect a shipped binary—upstream stopped before build.

## How it works

Designed as a UserPromptSubmit hook asking Jev which skill fits, adding a one-line hint only when confident. Baseline without hints already met the stop threshold, so the gated plan ended.

## Get started

```sh
git clone https://github.com/maxkulish/jevroute.git
cd jevroute
git checkout 7efc45e96c0b0e3035b501431a2d9f0fa19e5fc3
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 7efc45e96c0b](https://github.com/maxkulish/jevroute/tree/7efc45e96c0b0e3035b501431a2d9f0fa19e5fc3). AI-assisted README and license inspection; install/live paths not executed.
