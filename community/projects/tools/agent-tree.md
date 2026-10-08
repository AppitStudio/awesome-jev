# agent-tree

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that only watches: optional bottom HUD lines merged into your status line plus an on-demand `/agent-tree` pane showing the main agent and subagents, and — when you opt in — TypeSafe Jev reading a small session summary to draw four advisory flags (looping, stuck, fan-out wide, near done) and a health score.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/s112076649/agent-tree) |
| Maintainer | [s112076649](https://github.com/s112076649). Independently curated. |
| Format | Claude Code plugin marketplace (`agent-tree@agent-tree`) with optional status-line wrapper |
| Requirements | Claude Code 2.1.287+; for Jev flags, `TYPESAFE_API_KEY` in the environment and `jevEnabled` switched on via `/plugin configure`. |
| License | [MIT](https://github.com/s112076649/agent-tree/blob/817f97332537d0649400b18156e5a21ae7426e0a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Keep an eye on parallel subagents without reading every transcript.
- Get an early 'looping' or 'stuck' hint while you do something else.
- Mismatch: advisory only — it never blocks or changes tool calls.

## How it works

[`plugins/agent-tree/hooks/jev-core.ts`](https://github.com/s112076649/agent-tree/blob/817f97332537d0649400b18156e5a21ae7426e0a/plugins/agent-tree/hooks/jev-core.ts) builds a summary of at most the last 50 session events (event kind, tool name, failure, time) and calls `https://api.typesafe.ai/v1/systemone` only when something happened since the last call; [`hud.ts`](https://github.com/s112076649/agent-tree/blob/817f97332537d0649400b18156e5a21ae7426e0a/plugins/agent-tree/hooks/hud.ts) renders the HUD. With Jev off the plugin makes no requests.

## Get started

Install from the marketplace (README *Install*):

```sh
claude plugin marketplace add s112076649/agent-tree
claude plugin install agent-tree@agent-tree
# optional Jev flags: export TYPESAFE_API_KEY=... then /plugin configure agent-tree@agent-tree
```

With Jev flags on, periodic Jev calls are billed to your TypeSafe key.

## Examples and demos

- README *What it shows* (HUD sample) and *Jev flags (opt-in)*.

## Limits and data handling

With Jev on, a short event summary (no file contents per README) goes to TypeSafe; the key is never saved or logged. Upstream release gates ran on Windows 11. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 817f97332537](https://github.com/s112076649/agent-tree/tree/817f97332537d0649400b18156e5a21ae7426e0a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
