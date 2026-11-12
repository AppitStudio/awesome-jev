# jev-router by chrismarchant (MCP/CLI router that offloads parallel-workstream decisions to Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent-agnostic MCP server and CLI that hands the routing, triage, prioritization, conflict detection and verification of parallel workstreams to Jev using its fan-out pattern and box primitive, while your own agent (Claude Code, Mistral Vibe, Codex) does the work.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/chrismarchant/jev-router) |
| Maintainer | [chrismarchant](https://github.com/chrismarchant). Independently curated. |
| Format | MCP server, CLI and agent plugin (Node, zero dependencies, MIT) |
| Requirements | Node 18+ and `TYPESAFE_API_KEY`; installs as a Claude Code plugin, a skill, any MCP client or a plain CLI. |
| License | [MIT](https://github.com/chrismarchant/jev-router/blob/9dd0413cac41d2d7c375a3fe9a08230566ceddab/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`mcp-server/client.js`](https://github.com/chrismarchant/jev-router/blob/9dd0413cac41d2d7c375a3fe9a08230566ceddab/mcp-server/client.js) at the pinned commit. |

## When to use

- Split a coding task into parallel workstreams with typed, scored decisions.
- Check workstreams for conflicts before merging.
- Mismatch: not the Rust jev-router or the Claude effort router of the same name.

## How it works

`mcp-server/client.js` posts to `https://api.typesafe.ai/v1/systemone` with many typed questions per request; the nine `jev_*` tools plan workstreams, detect conflicts and verify results, with thresholds documented in `docs/confidence-and-thresholds.md`. Integration evidence: [`mcp-server/client.js`](https://github.com/chrismarchant/jev-router/blob/9dd0413cac41d2d7c375a3fe9a08230566ceddab/mcp-server/client.js).

## Get started

Set your key and run the CLI from a checkout, or add it to Claude Code from its marketplace.

```sh
export TYPESAFE_API_KEY=...
node bin/jev-router.js plan --task @examples/task.txt --candidates @examples/plan-candidates.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Docs: [github.com/chrismarchant/jev-router/blob/9dd0413cac41d2d7c375a3fe9a08230566ceddab/docs/tools.md](https://github.com/chrismarchant/jev-router/blob/9dd0413cac41d2d7c375a3fe9a08230566ceddab/docs/tools.md)

## Limits and data handling

Task text, candidate plans and file lists go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 9dd0413cac41](https://github.com/chrismarchant/jev-router/tree/9dd0413cac41d2d7c375a3fe9a08230566ceddab). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
