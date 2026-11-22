# Domios by Andrey Kovalev (desktop workspace that runs Claude Code, Codex and other agents as one team, with Jev ranking shared memory)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

A Tauri desktop app for macOS, Windows and Linux that runs Claude Code, Codex, OpenCode, Cursor, Aider and ACP agents side by side with your shells. A Planner scopes tasks, Workers take them and an Orchestrator reviews the evidence before a task closes; local memory keeps facts, decisions and skills across sessions, and a private mesh lets you reach agents on other machines or reply from Telegram.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/domios-dev/domios) |
| Tags | `Open source` · `Freemium` · `Commercial` · `BYOK` |
| Product homepage | [Product homepage](https://domios.dev) |
| Pricing and access | Free download and AGPL-3.0 source; the app has a Pro subscription (`domios account upgrade pro`) with plan limits on workspaces, Teams and tabs. Pro pricing was not verified ([account and subscription docs](https://github.com/domios-dev/domios/blob/256431d544651fd50a3891fcef58caaa4ba83b39/prod-docs/ACCOUNT.md), [website](https://domios.dev)). Jev is optional and uses your own TypeSafe key. Checked 2026-11-23. |
| Jev evidence | [`src-tauri/crates/codeterm-mem/src/decision/typesafe.rs`](https://github.com/domios-dev/domios/blob/256431d544651fd50a3891fcef58caaa4ba83b39/src-tauri/crates/codeterm-mem/src/decision/typesafe.rs) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Commercial access: the app offers an optional Pro subscription alongside the free AGPL-3.0 build. Discovered via X ([post](https://x.com/rollacode/status/2124577454182330634)). |
| Maintainer | [domios-dev](https://github.com/domios-dev). Independently curated. |
| Format | Desktop app (Tauri) + `domios` CLI |
| Platform and availability | Desktop (Tauri v2 with a Rust host and React UI) on macOS Apple Silicon, Windows x64 and Linux x64. |
| Jev's role | Optional: the Supporter Agent uses Jev to rerank memory and documentation candidates by how much each helps with the current question and to surface context; Domios works without it. |
| Requirements | One or more coding-agent CLIs you already use (Claude Code, Codex, OpenCode and so on); a TypeSafe API key only if you turn on the Jev supporter adapter. |
| License | [AGPL-3.0](https://github.com/domios-dev/domios/blob/256431d544651fd50a3891fcef58caaa4ba83b39/LICENSE) |

## When to use

- Run several coding agents on one plan with review before done, shared memory and access from other machines.
- Mismatch: a single-agent setup; Domios is a large workspace app, and Jev only plays a supporting role in memory ranking.

## How it works

`src-tauri/crates/codeterm-mem/src/decision/typesafe.rs` is the `typesafe-jev` decision adapter: it posts typed questions to `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default, using a key from the local token store. It is enabled through `[supporter] adapter = "typesafe-jev"` in the config, with a stage deadline (3,000 ms in the documented example). Integration evidence: [`src-tauri/crates/codeterm-mem/src/decision/typesafe.rs`](https://github.com/domios-dev/domios/blob/256431d544651fd50a3891fcef58caaa4ba83b39/src-tauri/crates/codeterm-mem/src/decision/typesafe.rs).

## Get started

Download an installer from the latest release, or build from source; then set the supporter adapter to `typesafe-jev` and add your key to enable Jev.

```sh
git clone https://github.com/domios-dev/domios && cd domios
pnpm install --frozen-lockfile
./build.sh dev
# then in a Domios terminal:
domios agent providers
domios mem search "project conventions"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Website and interactive demo: [domios.dev](https://domios.dev)
- 3-minute film: [youtu.be/kMZJDku4xcE](https://youtu.be/kMZJDku4xcE)
- Supporter adapter config: [github.com/domios-dev/domios/blob/256431d544651fd50a3891fcef58caaa4ba83b39/prod-docs/CONFIG.md](https://github.com/domios-dev/domios/blob/256431d544651fd50a3891fcef58caaa4ba83b39/prod-docs/CONFIG.md)
- Memory and Jev data handling: [github.com/domios-dev/domios/blob/256431d544651fd50a3891fcef58caaa4ba83b39/prod-docs/MEMORY.md](https://github.com/domios-dev/domios/blob/256431d544651fd50a3891fcef58caaa4ba83b39/prod-docs/MEMORY.md)

## Limits and data handling

Per the memory docs, query and candidate text (capped at 2,000 characters by default), configured docs or session excerpts and recent screen, chat or runtime context may be sent to the adapter, so Jev at TypeSafe receives that text when enabled; tokens stay local. The app has opt-in product analytics and a cloud account service for plans. AGPL-3.0: network use of modified versions carries source obligations.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 256431d54465](https://github.com/domios-dev/domios/tree/256431d544651fd50a3891fcef58caaa4ba83b39). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
