# jev-browse (danielnc)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

browser-harness helpers so coding agents hand off website sub-tasks in one call; TypeSafe Jev decides each click/type. Port of jev-ultrafast patterns—distinct from cooper667/jev-browse.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danielnc/jev-browse) |
| Maintainer | [danielnc](https://github.com/danielnc). Independently curated. |
| Format | Python package helpers on browser-harness (`fast_run`, `jev_close`, doctor). |
| Requirements | Python 3.11+; Chrome + browser-harness; `TYPESAFE_API_KEY`; optional Claude CLI for text backend. |
| License | [MIT](https://github.com/danielnc/jev-browse/blob/3d27b3e73056bdafbc13eb5ea866bc56a778ff4e/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use when Claude/Codex should **delegate a multi-step form/nav sub-task** instead of spending a frontier turn per click.

## How it works

`fast_run(url, goal)` loops observe→Jev→act until done/blocked; returns status, reason, and URL. Upstream README reports author speed/cost vs agent-driven harness (not re-measured here).

## Get started

```sh
git clone https://github.com/danielnc/jev-browse.git
cd jev-browse
git checkout 3d27b3e73056bdafbc13eb5ea866bc56a778ff4e
# Follow install.md / agent install prompt; run: python3 -m jev_browse doctor
```

## Examples and demos

- README Wikipedia Gödel `fast_run` snippet.
- Benchmark section on upstream README.

## Limits and data handling

Page observations go to TypeSafe. Speed/cost multipliers are author-reported. Distinct listing from [jev-browse (cooper667)](cooper667-jev-browse.md).

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 3d27b3e](https://github.com/danielnc/jev-browse/tree/3d27b3e73056bdafbc13eb5ea866bc56a778ff4e). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [jev-browse (cooper667)](cooper667-jev-browse.md), [Jev Ultrafast](jev-ultrafast.md).
