# Jevis

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hooks that give Codex, Claude Code and other coding agents a second pair of eyes: Jev reads each message, each command or edit the agent is about to make and each 'done' it is about to report, then injects lessons at the right moment, refuses likely mistakes and asks for a review before completion.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gldroger/jevis) |
| Maintainer | [gldroger](https://github.com/gldroger). Independently curated. |
| Format | Node.js hooks (installer for Claude Code and Codex; native Codex plugin option) |
| Requirements | Node 22+, a TypeSafe or OpenAI key (or your own Jev-compatible server); Chrome and the `claude` or `codex` CLI for the optional design review. |
| License | [MIT](https://github.com/gldroger/jevis/blob/de11e853a03977897acdfc30a44d6da5fd7234f2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.mjs`](https://github.com/gldroger/jevis/blob/de11e853a03977897acdfc30a44d6da5fd7234f2/src/config.mjs) at the pinned commit. |

## When to use

- Stop a coding agent from repeating a known mistake or running a destructive git command.
- Get a check before the agent reports a task as done.
- Mismatch: adds a decision-model call per hook event; some lesson checks are exact code rules instead.

## How it works

Each hook asks the decision model yes/no questions about the current message, tool call or completion claim; by default that is TypeSafe's hosted Jev, with `JEVIS_JEV_URL` pointing to any `/v1/systemone` server. The key lives in `~/.jevis/secrets/typesafe_api_key` (mode 600). Integration evidence: [`src/config.mjs`](https://github.com/gldroger/jevis/blob/de11e853a03977897acdfc30a44d6da5fd7234f2/src/config.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gldroger/jevis.git && cd jevis
node bin/install.mjs --dry-run   # shows changes to ~/.claude/settings.json and ~/.codex/hooks.json
node bin/install.mjs
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- 73-second explainer video: `docs/media/jevis-explainer.mp4`.
- Results and evaluation steps in the README.

## Limits and data handling

Your messages, planned commands and edits go to the configured decision provider on your key; old harness configs are backed up in `~/.jevis/backups/`.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit de11e853a039](https://github.com/gldroger/jevis/tree/de11e853a03977897acdfc30a44d6da5fd7234f2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
