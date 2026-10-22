# JevLadder (rules, Jev judge and human gates for coding agents)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small decision authority for coding agents: deterministic rules run first, a cheap judge such as Jev covers only the grey zone, and uncertain or irreversible actions go to a human, with measurable allow, block or human exits for merge gates and model-tier routing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/HaraldSigvartsen/jevladder) |
| Maintainer | [HaraldSigvartsen](https://github.com/HaraldSigvartsen). Independently curated. |
| Format | Codex plugin, TypeScript library and CLI (Node.js) |
| Requirements | Node.js 20+; Codex (primary host) or Claude Code; optional TypeSafe API key for the judge. |
| License | [MIT](https://github.com/HaraldSigvartsen/jevladder/blob/84e714171dfb56313b4d800ffceb60ab86c023fc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugin/scripts/jevladder-mcp.mjs`](https://github.com/HaraldSigvartsen/jevladder/blob/84e714171dfb56313b4d800ffceb60ab86c023fc/plugin/scripts/jevladder-mcp.mjs) at the pinned commit. |

## When to use

- Gate merges with allow, block or human outcomes instead of a free-text LGTM.
- Start coding tasks on a cheap model tier and escalate one step at a time.
- Mismatch: developed and tested on Codex; Claude Code support is validated structurally only.

## How it works

The `jevladder_decide` MCP tool in `plugin/scripts/jevladder-mcp.mjs` applies the deterministic rules and, only when a judge key is set and the rules cannot decide, asks TypeSafe System One (`jev-1.13.0`) at `https://api.typesafe.ai/v1/systemone` with an 8-second timeout. Integration evidence: [`plugin/scripts/jevladder-mcp.mjs`](https://github.com/HaraldSigvartsen/jevladder/blob/84e714171dfb56313b4d800ffceb60ab86c023fc/plugin/scripts/jevladder-mcp.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
codex plugin marketplace add HaraldSigvartsen/jevladder
codex plugin add jevladder@jevladder
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Advanced CLI and CI usage in the README: [github.com/HaraldSigvartsen/jevladder#readme](https://github.com/HaraldSigvartsen/jevladder#readme)
- Changelog: [github.com/HaraldSigvartsen/jevladder/blob/main/CHANGELOG.md](https://github.com/HaraldSigvartsen/jevladder/blob/main/CHANGELOG.md)

## Limits and data handling

With a judge key set, grey-zone decision context is sent to TypeSafe. The observe log keeps only tier and signal metadata, never prompt text, per the README.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 84e714171dfb](https://github.com/HaraldSigvartsen/jevladder/tree/84e714171dfb56313b4d800ffceb60ab86c023fc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
