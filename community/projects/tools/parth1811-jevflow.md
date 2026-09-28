# JevFlow

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that keeps agents honest: plans as phases with checks; when Claude tries to stop, JevFlow asks Jev if the work is really done

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Parth1811/JevFlow) |
| Maintainer | [Parth1811](https://github.com/Parth1811). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Claude Code plugin with live plan viewer. |
| Requirements | Claude Code; TypeSafe / provider keys per upstream README. |
| License | [MIT](https://github.com/Parth1811/JevFlow/blob/506ecf583faa3bfe40a8514a49b1dc04b21c221c/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when multi-agent Claude Code sessions need a Jev-backed done/not-done gate and a live plan viewer. Prefer lighter stop-hooks if you only need shell allowlists.

## How it works

Phases and checks are planned in code; Jev answers completion questions before stop. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/Parth1811/JevFlow.git
cd JevFlow
git checkout 506ecf583faa3bfe40a8514a49b1dc04b21c221c
```

Pin revision `506ecf583faa3bfe40a8514a49b1dc04b21c221c` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 506ecf5](https://github.com/Parth1811/JevFlow/tree/506ecf583faa3bfe40a8514a49b1dc04b21c221c). AI-assisted README and LICENSE inspection; install/live paths not executed.
