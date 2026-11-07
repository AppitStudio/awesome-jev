# Jev Prune for Claude Code (local proxy that prunes stale tool results with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local proxy between Claude Code and Anthropic that uses TypeSafe Jev to score old tool results and prune ones no longer relevant, shrinking context while keeping terminal history.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/j-ctang/claude-code-jev-prune) |
| Maintainer | [j-ctang](https://github.com/j-ctang). Independently curated. |
| Format | Node.js CLI proxy (no SPDX license file on the reviewed commit) |
| Requirements | Node.js 20+, Claude Code, and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/services/jevService.ts`](https://github.com/j-ctang/claude-code-jev-prune/blob/303d0de68d730f9869295bc4b12aa88d4a369a1e/src/services/jevService.ts) at the pinned commit. |

## When to use

- Keep long Claude Code sessions within context budgets.
- Inspect pruning decisions via the bundled prune log/stats.
- Mismatch: no OSI license on the reviewed commit.

## How it works

`src/services/jevService.ts` POSTs to `${baseUrl}/v1/systemone` with `jev-latest`; `relevanceScorer.ts` and `contextPruner.ts` use the scores to drop stale tool output. Integration evidence: [`src/services/jevService.ts`](https://github.com/j-ctang/claude-code-jev-prune/blob/303d0de68d730f9869295bc4b12aa88d4a369a1e/src/services/jevService.ts).

## Get started

Clone, `npm link`, set TYPESAFE_API_KEY, and launch Claude Code through `jev-prune`.

```sh
git clone https://github.com/j-ctang/claude-code-jev-prune.git && cd claude-code-jev-prune
export TYPESAFE_API_KEY=...
npm link
jev-prune
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/j-ctang/claude-code-jev-prune/blob/303d0de68d730f9869295bc4b12aa88d4a369a1e/README.md](https://github.com/j-ctang/claude-code-jev-prune/blob/303d0de68d730f9869295bc4b12aa88d4a369a1e/README.md)

## Limits and data handling

Tool output snippets are sent to TypeSafe on your key; proxy sits in the Anthropic request path.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 303d0de68d73](https://github.com/j-ctang/claude-code-jev-prune/tree/303d0de68d730f9869295bc4b12aa88d4a369a1e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
