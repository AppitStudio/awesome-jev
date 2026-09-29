# jev-filter (ByteBell)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

After grep, let TypeSafe Jev decide which candidate files are relevant before the coding LLM reads them.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ByteBell/jev-filter) |
| Maintainer | [ByteBell](https://github.com/ByteBell). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code plugin with `/jev-find` style workflow. |
| Requirements | Claude Code (or compatible agent); TypeSafe/OpenRouter Jev access per upstream. |
| License | [MIT](https://github.com/ByteBell/jev-filter/blob/71b8d3cf6cc0dd44201a233ebe25ede7f713c79e/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when coding agents waste tokens reading huge grep hit lists. Prefer ordinary grep when the hit set is already small.

## How it works

Grep gathers candidates; Jev answers per-file noul relevance with probabilities; the agent reads only kept files. Includes a benchmark folder with author-reported comparisons. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/ByteBell/jev-filter.git
cd jev-filter
git checkout 71b8d3cf6cc0dd44201a233ebe25ede7f713c79e
# follow upstream README for Claude Code plugin install and API key
```

Pin revision `71b8d3cf6cc0dd44201a233ebe25ede7f713c79e` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Cost/accuracy tables are author-reported. Live Claude Code/Jev not run on the review host. File contents are sent to the classifier provider.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 71b8d3c](https://github.com/ByteBell/jev-filter/tree/71b8d3cf6cc0dd44201a233ebe25ede7f713c79e). AI-assisted README and LICENSE inspection; install/live paths not executed.
