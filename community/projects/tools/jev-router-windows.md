# Jev Router for Windows

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One-click Windows GUI for TypeSafe Jev routing with Codex (jev-codex-bridge) and assisted Claude Code plugin setup.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pouramin/jev-router-windows) |
| Maintainer | [pouramin](https://github.com/pouramin). Independently curated. |
| Format | Windows GUI setup panel for Jev routing (MIT, alpha) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/pouramin/jev-router-windows/blob/aa30e29dea7b3a53f9656da6709142955c5886db/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Windows niche alpha. Complements Unix-oriented routers; Codex path uses jev-codex-bridge; Claude Desktop path is plugin-assisted (not the same transparent proxy). Live install/inference not run on the review host. |

## When to use

Use when you want a graphical Windows installer for Jev routing instead of editing configs by hand. Prefer Unix CLIs/plugins on non-Windows hosts.

## How it works

Portable package: START_JEV_ROUTER.bat launches a control panel. Codex Desktop/CLI gets automatic per-turn routing via jev-codex-bridge; Claude Code in Claude Desktop gets guided plugin setup.

## Get started

```sh
git clone https://github.com/pouramin/jev-router-windows.git
cd jev-router-windows
git checkout aa30e29dea7b3a53f9656da6709142955c5886db
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit aa30e29dea7b](https://github.com/pouramin/jev-router-windows/tree/aa30e29dea7b3a53f9656da6709142955c5886db). AI-assisted README and license inspection; install/live paths not executed.
