# jev-gate (MongLong0214)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin: TypeSafe Jev-backed Gate (admission), Router (effort/subagent), Evidence search, plus non-Jev Compact/Output modules

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/MongLong0214/jev-gate) |
| Maintainer | [MongLong0214](https://github.com/MongLong0214). Independently curated. Distinct from [jev-gate (Neoo-Blue)](neoo-blue-jev-gate.md) and other “jev-gate*” listings. |
| Format | TypeScript · Claude Code marketplace plugin (Node.js 22+). |
| Requirements | Claude Code; optional `TYPESAFE_API_KEY` and `CLAUDE_CODE_ENABLE_FUNCTION_HOOKS=1` for Jev-using parts. |
| License | **No LICENSE file** in the reviewed tree (GitHub reports no SPDX license). Public readability does not establish reuse permission — treat as source-available / terms unspecified. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Experimental; no general cost saving claimed. Live Claude/Jev not run on the review host. |

## When to use

Use when you want one Claude Code plugin that can admit/route tasks with narrow Jev judgments and optional evidence search — separate from plan/stop gating in Neoo-Blue’s jev-gate.

## How it works

Gate may admit direct/single/orchestrated work; Router may change effort/subagent model; Evidence can semantic-page via Jev. Compact and Output do not call Jev. Missing key → Gate/Router stay native.

## Get started

```text
/plugin marketplace add MongLong0214/jev-gate
/plugin install jev-gate@jev-gate
```

Pin review revision `a00f652ac73ef6b784f4e6cfb4eefd46c2de35ba`. Merge `TYPESAFE_API_KEY` into Claude Code env settings per upstream README; restart the session.

## Examples and demos

Upstream README tables for the five parts. No live plugin session on the review host.

## Limits and data handling

With a key, Gate/Router/Evidence semantic pages may send requests or source windows to TypeSafe — not the whole repository. No LICENSE file at review tip.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit a00f652](https://github.com/MongLong0214/jev-gate/tree/a00f652ac73ef6b784f4e6cfb4eefd46c2de35ba). AI-assisted README inspection; no LICENSE present; live paths not executed.
