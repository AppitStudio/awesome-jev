# Talos

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Chat-led multi-agent orchestration TUI forked from thurbox: conversational routing, tmux worker panes, a kanban board and spec-driven execution, with a built-in Jev decision engine that powers the Auto model/agent selection.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zatzk/talos) |
| Maintainer | [zatzk](https://github.com/zatzk). Independently curated. |
| Format | Rust TUI (`talos`) + headless `talos-cli` |
| Requirements | Rust, tmux 3.2+, at least one agent CLI; Jev access for Auto routing. |
| License | [MIT](https://github.com/zatzk/talos/blob/03280b259d92549058e49fd15c10064ab347ab41/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Run several coding agents with Jev picking the runner.
- Mismatch: fork with submodules; early project.

## How it works

See the upstream [README](https://github.com/zatzk/talos/blob/03280b259d92549058e49fd15c10064ab347ab41/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/zatzk/talos.git && cd talos
./install.sh
```

## Limits and data handling

Routing prompts go to Jev when Auto is selected. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 03280b259d92](https://github.com/zatzk/talos/tree/03280b259d92549058e49fd15c10064ab347ab41). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
