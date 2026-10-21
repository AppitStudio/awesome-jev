# jev-claude-plugin (Jev around Claude Code tool calls)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that puts Jev at four points around tool calls: it windows long tool output and withholds irrelevant or injected spans, can replace auto mode with a hazard-based allow/deny/ask check, suggests effort and model, and can check final claims against tool results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zacharytgray/jev-claude-plugin) |
| Maintainer | [zacharytgray](https://github.com/zacharytgray). Independently curated. |
| Format | Claude Code plugin (Python hooks) |
| Requirements | Claude Code; Python; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/zacharytgray/jev-claude-plugin/blob/aa18dfd948e4b362cab611f9791253ae57a0e204/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_plugin/jev_client.py`](https://github.com/zacharytgray/jev-claude-plugin/blob/aa18dfd948e4b362cab611f9791253ae57a0e204/jev_plugin/jev_client.py) at the pinned commit. |

## When to use

- Screen every tool result for prompt injection before the agent sees it.
- Trim long Read and Bash output to the relevant windows.
- Mismatch: only the output filter is on by default; the other hooks are opt-in and the design is still experimental per the README.

## How it works

Hooks (`PostToolUse`, `PreToolUse`, `UserPromptSubmit`, `Stop`) send small typed questions to `https://api.typesafe.ai/v1/systemone` (`jev_plugin/jev_client.py`); code settles what it can first and every hook fails open. Integration evidence: [`jev_plugin/jev_client.py`](https://github.com/zacharytgray/jev-claude-plugin/blob/aa18dfd948e4b362cab611f9791253ae57a0e204/jev_plugin/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=your-key
claude --plugin-dir path/to/jev-claude-plugin
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Four points table and measured cut-offs in the README: [github.com/zacharytgray/jev-claude-plugin#readme](https://github.com/zacharytgray/jev-claude-plugin#readme)

## Limits and data handling

Tool output, requests and replies are sent to TypeSafe for the enabled checks. Community project, not affiliated with TypeSafe or Anthropic.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit aa18dfd948e4](https://github.com/zacharytgray/jev-claude-plugin/tree/aa18dfd948e4b362cab611f9791253ae57a0e204). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
