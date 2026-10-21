# jev-effort-router (hasanzaman22)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that asks Jev how much thinking each prompt needs and how risky it is, then runs the turn at the lowest effort level likely to get it right, leaning toward more effort when Jev is unsure.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hasanzaman22/jev-effort-router) |
| Maintainer | [hasanzaman22](https://github.com/hasanzaman22). Independently curated. |
| Format | Claude Code plugin (Python, no dependencies) |
| Requirements | Claude Code 2.1.306+, Python 3.9+, a Jev key from OpenRouter, OpenCode Zen or TypeSafe (`JEV_API_KEY`). |
| License | [MIT](https://github.com/hasanzaman22/jev-effort-router/blob/28eea82e1f62d5c8bb28818329894dc1368e65cc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_router/judgments.py`](https://github.com/hasanzaman22/jev-effort-router/blob/28eea82e1f62d5c8bb28818329894dc1368e65cc/jev_router/judgments.py) at the pinned commit. |

## When to use

- Spend fewer thinking tokens on easy questions while keeping high effort for debugging and risky changes.
- Keep your chosen model and only change the effort level.
- Mismatch: relies on Claude Code mods, which are early access and may change.

## How it works

A prompt hook sends about 830 tokens of context to a System One endpoint (TypeSafe, OpenRouter or OpenCode Zen, see `jev_router/judgments.py`) and maps the answers to `low` through `xhigh` effort, shown in the status line. Integration evidence: [`jev_router/judgments.py`](https://github.com/hasanzaman22/jev-effort-router/blob/28eea82e1f62d5c8bb28818329894dc1368e65cc/jev_router/judgments.py).

## Get started

From the upstream README (not run on the review host):

```sh
export JEV_API_KEY=your-key
# in Claude Code:
/plugin marketplace add hasanzaman22/jev-effort-router
/plugin install jev-effort-router@jev-effort-router
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup and provider notes in the README: [github.com/hasanzaman22/jev-effort-router#readme](https://github.com/hasanzaman22/jev-effort-router#readme)

## Limits and data handling

Prompts are sent to the chosen Jev provider. Cost estimates are the author's. Community project, not affiliated with TypeSafe or Anthropic.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 28eea82e1f62](https://github.com/hasanzaman22/jev-effort-router/tree/28eea82e1f62d5c8bb28818329894dc1368e65cc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
