# claude-auto-effort

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod where TypeSafe Jev rates, in about 200 ms before each turn, how much careful reasoning a prompt needs (0–3) and sets the effort level with smoothing; Claude Code port of pi-auto-effort sharing its questions, policy and settings file.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/justmytwospence/claude-auto-effort) |
| Maintainer | [justmytwospence](https://github.com/justmytwospence). Independently curated. |
| Format | Claude Code plugin directory with a hooks module (`claude --plugin-dir <checkout>`) |
| Requirements | Claude Code 2.1.287+ (tested 2.1.289) and `TYPESAFE_API_KEY` in the environment. |
| License | [MIT](https://github.com/justmytwospence/claude-auto-effort/blob/4c791755b19c8b5ef1fbdff3bd3d9f72623a2d4d/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Avoid paying xhigh effort for lookups and mechanical edits while keeping it for hard work.
- Share one auto-effort policy with the pi and opencode ports.
- Mismatch: subagent loops are left alone; relies on Claude Code's mod API.

## How it works

[`hooks/request.ts`](https://github.com/justmytwospence/claude-auto-effort/blob/4c791755b19c8b5ef1fbdff3bd3d9f72623a2d4d/hooks/request.ts) builds the Jev request (prompt, two before it, last answer, last-run signals); [`hooks/policy.ts`](https://github.com/justmytwospence/claude-auto-effort/blob/4c791755b19c8b5ef1fbdff3bd3d9f72623a2d4d/hooks/policy.ts) smooths the score (`e = 0.5·score + 0.5·e_prev`) and picks the level at `turn.start`, applied to every `turn.step`.

## Get started

Load the plugin directory (README *Install*):

```sh
git clone https://github.com/justmytwospence/claude-auto-effort.git
export TYPESAFE_API_KEY=...
claude --plugin-dir ./claude-auto-effort
```

One Jev request per prompt, billed to your TypeSafe key.

## Examples and demos

- README *Commands* and *Settings*.
- Sibling ports: [pi-auto-effort](https://github.com/justmytwospence/pi-auto-effort), [opencode-auto-effort](https://github.com/justmytwospence/opencode-auto-effort).

## Limits and data handling

Recent prompts, the last answer and run metadata go to TypeSafe each turn. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 4c791755b19c](https://github.com/justmytwospence/claude-auto-effort/tree/4c791755b19c8b5ef1fbdff3bd3d9f72623a2d4d). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
