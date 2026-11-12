# DOXA (Rust multi-agent terminal for Claude, Codex, DeepSeek and GLM with Jev turn routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust terminal workspace that runs Claude, Codex, DeepSeek or GLM coding agents in tabs and split panes with reattachable sessions; Jev (or SubQ Snap) routes each turn among the models you configure and can supervise fleet alignment at host checkpoints.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/docwilde/doxa) |
| Maintainer | [docwilde](https://github.com/docwilde). Independently curated. |
| Format | Rust TUI installed from source by script (AGPL-3.0-only; commercial licence offered) |
| Requirements | Linux or macOS, the engine CLIs or API credentials you use (Claude, Codex, DeepSeek, GLM), and `TYPESAFE_API_KEY` for Jev routing. |
| License | [AGPL-3.0-only (commercial licence available on request)](https://github.com/docwilde/doxa/blob/344d3b98b11a8817fabaa568a080208efa681a13/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Dual-licensed: AGPL-3.0-only, with a separately negotiated commercial licence offered by the author. |
| Jev evidence | [`docs/jev-router.md`](https://github.com/docwilde/doxa/blob/344d3b98b11a8817fabaa568a080208efa681a13/docs/jev-router.md) at the pinned commit. |

## When to use

- Run several coding agents side by side and let Jev pick which model takes each turn.
- Mismatch: a stable release; Rust 2.0 is in beta. AGPL copyleft applies to forks, including network-only ones.

## How it works

`docs/jev-router.md` documents the turn router: it accepts pinned `jev-1.13.0` (or `subq-snap-preview`), asks a Jev choice over the configured targets via `https://api.typesafe.ai/v1/systemone`, and an exact `/model` pin skips Jev selection. The README marks Rust 2.0 as beta and warns that agents run with your privileges. Integration evidence: [`docs/jev-router.md`](https://github.com/docwilde/doxa/blob/344d3b98b11a8817fabaa568a080208efa681a13/docs/jev-router.md).

## Get started

Run the install script (it builds from source and does not verify a release signature; `DOXA_RUST_EXPECTED_SHA` can pin a commit), then check and start an engine.

```sh
curl -fsSL https://raw.githubusercontent.com/docwilde/doxa/main/scripts/install.sh | sh
doxa doctor --engine codex
doxa new --engine codex
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/docwilde/doxa/blob/344d3b98b11a8817fabaa568a080208efa681a13/README.md](https://github.com/docwilde/doxa/blob/344d3b98b11a8817fabaa568a080208efa681a13/README.md)
- Gallery: [docwilde.github.io/doxa/gallery/](https://docwilde.github.io/doxa/gallery/)

## Limits and data handling

Turn summaries go to TypeSafe for routing on your key; prompts and code go to whichever engine provider handles the turn. Agents edit files and run commands with your privileges.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit 344d3b98b11a](https://github.com/docwilde/doxa/tree/344d3b98b11a8817fabaa568a080208efa681a13). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
