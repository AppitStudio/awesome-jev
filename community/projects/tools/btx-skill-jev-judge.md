# btx-skill-jev-judge

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that hands repeated judgments to TypeSafe Jev from a tested script (redaction, rate limits).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bitranox/btx-skill-jev-judge) |
| Maintainer | [bitranox](https://github.com/bitranox). Independently curated. |
| Format | Claude Code plugin (MIT) |
| Requirements | See upstream README; TypeSafe/provider keys when using hosted Jev paths. |
| License | [MIT](https://github.com/bitranox/btx-skill-jev-judge/blob/6dd4419cfd86ceb8f24c14eddaffcb46666d0ca8/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live install/inference not run on the review host. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog entries when you need a different stack or a hosted-only product.

## How it works

Jev (or a disclosed local/open System One substitute) supplies typed judgments; ordinary application code owns orchestration, I/O, and side effects. See upstream for the exact question schemas and failure handling.

Note: GitHub rename of bitranox/btx-skill-jev → btx-skill-jev-judge.

## Get started

```sh
git clone https://github.com/bitranox/btx-skill-jev-judge.git
cd btx-skill-jev-judge
git checkout 6dd4419cfd86ceb8f24c14eddaffcb46666d0ca8
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-02** (Europe/Sofia) at [commit 6dd4419cfd86](https://github.com/bitranox/btx-skill-jev-judge/tree/6dd4419cfd86ceb8f24c14eddaffcb46666d0ca8). AI-assisted README and license inspection; install/live paths not executed.
