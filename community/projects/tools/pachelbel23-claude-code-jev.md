# Jev for Claude Code (pachelbel23)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial one-file installer that adds Jev hooks to Claude Code: skill suggestion and task-type classification per prompt, optional subagent model tier choice and shell risk confirmation, plus a jev-vision CLI for image yes/no, choice and Box questions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/pachelbel23/claude-code-jev) |
| Maintainer | [pachelbel23](https://github.com/pachelbel23). Independently curated. |
| Format | Claude Code hooks, `/jev` command and jev-vision skill (Node.js installer) |
| Requirements | Node.js 18+, Claude Code, a TypeSafe API key. |
| License | [MIT](https://github.com/pachelbel23/claude-code-jev/blob/13e1b66248521427a89bfc19f74167186819ea50/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/pachelbel23/claude-code-jev/blob/13e1b66248521427a89bfc19f74167186819ea50/src/jev.mjs) at the pinned commit. |

## When to use

- Get a skill suggested only when it clearly fits the prompt.
- Ask for confirmation before commands Jev judges destructive or secret-touching (full mode).
- Mismatch: unofficial; image and Box questions use TypeSafe's experimental images feature.

## How it works

Hooks call `https://api.typesafe.ai/v1/systemone` from `src/jev.mjs`, reading the key from `TYPESAFE_API_KEY` or a local key file. `lite` mode only suggests skills and classifies tasks; `on` adds the subagent model choice and the shell risk gate. When Jev is unavailable it warns once and Claude Code behaves as before. Integration evidence: [`src/jev.mjs`](https://github.com/pachelbel23/claude-code-jev/blob/13e1b66248521427a89bfc19f74167186819ea50/src/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -fsSLO https://raw.githubusercontent.com/pachelbel23/claude-code-jev/main/setup-jev.mjs && node setup-jev.mjs
# then restart Claude Code; switch with /jev lite | on | off
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Agent install instructions: `AGENT_INSTALL.md`.

## Limits and data handling

Prompts, skill names and (in full mode) shell commands go to TypeSafe on your key. Review the installer before running it.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 13e1b6624852](https://github.com/pachelbel23/claude-code-jev/tree/13e1b66248521427a89bfc19f74167186819ea50). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
