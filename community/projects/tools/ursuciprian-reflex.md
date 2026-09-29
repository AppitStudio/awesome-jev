# Reflex (ursuciprian)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pre-execution risk gate and prompt-injection guard for coding agents; optional TypeSafe Jev (or local Laya) for uncovered commands

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ursuciprian/reflex) |
| Maintainer | [ursuciprian](https://github.com/ursuciprian). Independently curated. npm `@ursuciprian/reflex`. **Distinct from** [Reflex (kaustav1996)](kaustav1996-reflex.md), [jev-reflex (xnuonux)](jev-reflex-xnuonux.md), and [Reflex-1](matu79go-reflex-1.md). |
| Format | JavaScript · hooks/plugins for Claude Code, Codex, opencode, pi, Hermes (MIT; Node 18+; no runtime deps). |
| Requirements | Node.js 18+; optional `TYPESAFE_API_KEY` for `jev` engine (default local/shadow needs no key). |
| License | [MIT](https://github.com/ursuciprian/reflex/blob/f87711c805a80b685491546b5524bd519225990e/LICENSE). Provider usage may incur charges when using Jev. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live agent hooks/Jev not run on the review host. |

## When to use

Use when you want shell-command gating and injection scanning before agents act, with deterministic rules first and optional Jev for the rest.

## How it works

Hooks intercept shell tools; read-only/deterministic lanes settle many commands locally; remaining asks go to `local` / `jev` / `laya` engines under `policy.json`. Prompt-injection scans cover web/MCP/foreign files.

## Get started

```sh
# npm package also published as @ursuciprian/reflex
git clone https://github.com/ursuciprian/reflex.git
cd reflex
git checkout f87711c805a80b685491546b5524bd519225990e
# follow upstream README for one-command agent installs; try shadow mode first
```

## Examples and demos

Upstream demo GIF and `reflex replay` against past sessions. No live hook session on the review host.

## Limits and data handling

Gates shell commands, not file edits/MCP calls; not a sandbox substitute. Jev receives command/context text when the `jev` engine is selected.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit f87711c](https://github.com/ursuciprian/reflex/tree/f87711c805a80b685491546b5524bd519225990e). AI-assisted README + LICENSE inspection; live paths not executed.
