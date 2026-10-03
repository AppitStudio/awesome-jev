# Modex

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Open Codex-App–style desktop coding agent (Electron+React) driving Claude Code/Codex CLIs; optional TypeSafe Jev Auto routing picks model/effort per turn.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TypeSafeAI/modex) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/TypeSafeAI/modex#readme) |
| Pricing and access | Free MIT source build; no app purchase fee. Optional TypeSafe key for Auto; Claude/Codex billed separately. Checked 2026-10-01. |
| Jev evidence | [Upstream README](https://github.com/TypeSafeAI/modex/blob/c1dd0b8b9d0d984f8c5ed69b3a29e83cfe915fe8/README.md) Auto routing section: TypeSafe Jev as the fast judge for model/effort selection when a key is configured. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. First-party TypeSafeAI repository; listing is not an endorsement. Same scrutiny as external submissions. Live install/UI paths not run on the Linux review host. |
| Maintainer | [TypeSafeAI](https://github.com/TypeSafeAI). Independently curated. |
| Format | Electron + React · desktop coding agent (MIT) |
| Platform and availability | Desktop (Electron); build from source |
| Jev's role | Optional Auto mode: Jev (or heuristic fallback) picks model, reasoning effort, and fast mode within user bounds; UI shows a receipt. |
| Requirements | Node/toolchain to build Electron app; Claude Code and/or Codex CLI; optional TypeSafe API key. |
| License | [MIT](https://github.com/TypeSafeAI/modex/blob/c1dd0b8b9d0d984f8c5ed69b3a29e83cfe915fe8/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when the workflow matches the upstream README. Prefer other catalog apps when you need a different platform or a hosted-only product.

## How it works

Open Codex-App–style desktop coding agent (Electron+React) driving Claude Code/Codex CLIs; optional TypeSafe Jev Auto routing picks model/effort per turn. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/TypeSafeAI/modex.git
cd modex
git checkout c1dd0b8b9d0d984f8c5ed69b3a29e83cfe915fe8
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit c1dd0b8b9d0d](https://github.com/TypeSafeAI/modex/tree/c1dd0b8b9d0d984f8c5ed69b3a29e83cfe915fe8). AI-assisted README and license inspection; live paths not executed.
