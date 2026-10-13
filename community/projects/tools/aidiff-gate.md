# aidiff-gate

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that flags flaky AI-written tests, trims walls of text and makes you own the Why of every commit, with TypeSafe Jev (direct or via OpenRouter) as an optional fast judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JohnRiceML/aidiff-gate) |
| Maintainer | [JohnRiceML](https://github.com/JohnRiceML). Independently curated. |
| Format | Claude Code plugin (hooks) |
| Requirements | Claude Code; optional `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/JohnRiceML/aidiff-gate/blob/7137345f3ec5d3354cf2c96124d82658f3d71476/LICENSE) |
| Jev evidence | [`hooks/jev.ts`](https://github.com/JohnRiceML/aidiff-gate/blob/7137345f3ec5d3354cf2c96124d82658f3d71476/hooks/jev.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Catch overreaching or flaky tests from agents with cheap typed checks.
- Mismatch: Jev is optional; without a key only local heuristics run.

## How it works

Hooks send test diffs and messages to Jev; a dim transcript line shows check, time, cost and verdict, which Claude does not see. (Summarized from the upstream [README](https://github.com/JohnRiceML/aidiff-gate/blob/7137345f3ec5d3354cf2c96124d82658f3d71476/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the plugin per the README and optionally add a key to `~/.claude/settings.json`.

## Limits and data handling

Diffs go to TypeSafe/OpenRouter when enabled. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 7137345f3ec5](https://github.com/JohnRiceML/aidiff-gate/tree/7137345f3ec5d3354cf2c96124d82658f3d71476). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
