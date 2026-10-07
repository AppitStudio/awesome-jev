# opencode-auto-effort

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

opencode plugin where TypeSafe Jev rates, in about 200 ms before each turn, how much careful reasoning a prompt needs (0–3) and sets opencode's model variant (low → xhigh) accordingly; cache-safe and sharing one settings file with the pi and Claude Code ports.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/justmytwospence/opencode-auto-effort) |
| Maintainer | [justmytwospence](https://github.com/justmytwospence). Independently curated. |
| Format | opencode plugin loaded from GitHub pinned to a commit |
| Requirements | opencode (tested with 1.18.29) and `TYPESAFE_API_KEY` in opencode's environment. |
| License | [MIT](https://github.com/justmytwospence/opencode-auto-effort/blob/e9fa61e10710bf57db7323ffe4deaadf11952630/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Spend high effort only on subtle design, hard debugging or correctness-critical prompts.
- Keep one auto-effort policy across pi, Claude Code and opencode (`~/.config/agents/auto-effort.json`).
- Mismatch: port of pi-auto-effort with the same questions and policy — pick the port for your harness.

## How it works

[`src/jev.ts`](https://github.com/justmytwospence/opencode-auto-effort/blob/e9fa61e10710bf57db7323ffe4deaadf11952630/src/jev.ts) asks Jev to score the request with the two prompts before it, the last answer and what the last run did (tool errors, edits, tool calls); [`src/policy.ts`](https://github.com/justmytwospence/opencode-auto-effort/blob/e9fa61e10710bf57db7323ffe4deaadf11952630/src/policy.ts) maps the score to a variant. The level is set on the user message in `chat.message`, so tool follow-ups in the turn keep it.

## Get started

Add to `opencode.jsonc`, pinned to a commit:

```sh
"plugin": [
  "opencode-auto-effort@github:justmytwospence/opencode-auto-effort#e9fa61e10710"
]
# and export TYPESAFE_API_KEY for opencode
```

One Jev request per prompt, billed to your TypeSafe key.

## Examples and demos

- README score table (0 lookup → 3 subtle design) and *Settings*.
- Sibling ports: [pi-auto-effort](https://github.com/justmytwospence/pi-auto-effort), [claude-auto-effort](https://github.com/justmytwospence/claude-auto-effort).

## Limits and data handling

Recent prompts, the last answer and run metadata go to TypeSafe each turn. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit e9fa61e10710](https://github.com/justmytwospence/opencode-auto-effort/tree/e9fa61e10710bf57db7323ffe4deaadf11952630). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
