# Baton Agent Orchestrator

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Idea-to-reviewed-code pipeline on your git repo (`jev` CLI): TypeSafe Jev picks the agent, model and effort at each step across Claude Code, Codex CLI and OpenRouter models.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Gane2506/baton) |
| Maintainer | [Gane2506](https://github.com/Gane2506). Independently curated. |
| Format | Python CLI |
| Requirements | Python; git; Claude Code / Codex CLI / OpenRouter access; TypeSafe key. |
| License | [Apache-2.0](https://github.com/Gane2506/baton/blob/a2ec9c757d4d99259fe3e3f84b297ce41d015a9a/LICENSE) |
| Jev evidence | [`src/jev_agent/dispatch/jev.py`](https://github.com/Gane2506/baton/blob/a2ec9c757d4d99259fe3e3f84b297ce41d015a9a/src/jev_agent/dispatch/jev.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Run plan, validation, implementation and review stages with budgets and per-step agent selection.
- Mismatch: alpha (v0.2) with breaking changes; nothing is pushed for you.

## How it works

A run moves through intake, planning, validating, approval and build states; at each decision point Jev chooses the route, and every task runs on its own local branch within your budgets. (Summarized from the upstream [README](https://github.com/Gane2506/baton/blob/a2ec9c757d4d99259fe3e3f84b297ce41d015a9a/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the package per the README, copy `examples/jev.toml`, and start a run with the `jev` CLI.

## Limits and data handling

Task text goes to TypeSafe and to the dispatched agents' providers. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit a2ec9c757d4d](https://github.com/Gane2506/baton/tree/a2ec9c757d4d99259fe3e3f84b297ce41d015a9a). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
