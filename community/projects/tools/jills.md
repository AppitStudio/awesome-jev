# Jills (saved agent-team workflows)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Saved agent workflows (`JILL.md`, like `SKILL.md`) that Jev suggests when a chat message matches one; each Jill runs as a separate job in its own git worktree for Pi, DeepSeek Harness or Claude Code and reports back with a branch and logs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aidanrausch4231/jills) |
| Maintainer | [aidanrausch4231](https://github.com/aidanrausch4231). Independently curated. |
| Format | CLI and MCP server (TypeScript) with Pi, dsh and Claude Code add-ons |
| Requirements | Node 22+, pnpm, git 2.38+; `TYPESAFE_API_KEY` for suggestions. |
| License | [MIT](https://github.com/aidanrausch4231/jills/blob/91491d187a4e9816269fa94914ae5ae708f93bed/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/plugins/matcher-jev.ts`](https://github.com/aidanrausch4231/jills/blob/91491d187a4e9816269fa94914ae5ae708f93bed/src/plugins/matcher-jev.ts) at the pinned commit. |

## When to use

- Reuse multi-step agent workflows without retyping them, with suggestions from chat.
- Run a workflow in an isolated worktree so nothing merges unless a step says so.
- Mismatch: v1 targets Pi and DeepSeek Harness; the Claude Code add-on is v2.

## How it works

A matcher plug-in (`src/plugins/matcher-jev.ts`) asks Jev whether a new chat message is a task that fits one of your saved Jills; in manual mode the add-on shows a suggestion card, in auto mode the main agent starts it. Without a key, suggestions are off. Integration evidence: [`src/plugins/matcher-jev.ts`](https://github.com/aidanrausch4231/jills/blob/91491d187a4e9816269fa94914ae5ae708f93bed/src/plugins/matcher-jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cd jills && pnpm install && pnpm build
ln -sf "$PWD/dist/src/cli.js" ~/.local/bin/jills
jills check && jills try hello --dry-run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup skill: [github.com/aidanrausch4231/jills/blob/main/skills/jills-setup/SKILL.md](https://github.com/aidanrausch4231/jills/blob/main/skills/jills-setup/SKILL.md)

## Limits and data handling

Chat messages are sent to TypeSafe for matching. Jills run agents that can change code in worktrees; review what each Jill does.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 91491d187a4e](https://github.com/aidanrausch4231/jills/tree/91491d187a4e9816269fa94914ae5ae708f93bed). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
