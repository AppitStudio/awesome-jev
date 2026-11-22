# Harness Reflex by miuzel (System One reflex layer that gates, prunes and stops loops in Claude Code, Codex and other agent harnesses)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A System One decision runtime for agent harnesses: as an MCP server it gives Claude Code, Codex and Antigravity eight tools (`choice`, `score`, `route`, `screen`, `gate`, `prune`, `detect_stagnation`, `status_ledger`), and as a host plugin it intervenes automatically through hooks to prune stale tool output, block repeated calls and check "I'm done" claims before a turn closes. The README (Chinese) has a frank table of which hosts actually honour each hook.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/miuzel/harness-reflex) |
| Maintainer | [miuzel](https://github.com/miuzel). Independently curated. |
| Format | TypeScript CLI + stdio MCP server + host plugins |
| Requirements | Node.js; a Jev key (TypeSafe), or another System One backend such as a vLLM/OpenAI logits endpoint, a self-hosted model or the local heuristic backend. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/backend/jev.ts`](https://github.com/miuzel/harness-reflex/blob/276777c7cd5a6a081243d1a9368da8559ac831d7/src/backend/jev.ts) at the pinned commit. |

## When to use

- Add cheap typed gates and loop-breaking to a coding agent without calling a heavier reasoning model each step.
- Mismatch: hosts without blocking hooks; the README marks where pruning or stop checks are only logged, not enforced.

## How it works

`src/backend/jev.ts` implements the Jev backend against `https://api.typesafe.ai/v1/systemone` with `jev-latest` by default (`src/backend/defaults.ts`); other backends implement the same decision interface, and `setup` writes hook and MCP config for each harness. Integration evidence: [`src/backend/jev.ts`](https://github.com/miuzel/harness-reflex/blob/276777c7cd5a6a081243d1a9368da8559ac831d7/src/backend/jev.ts).

## Get started

Build from source, then generate configuration for your harness.

```sh
git clone https://github.com/miuzel/harness-reflex && cd harness-reflex
npm install
npm run build
node dist/cli/index.js setup claude   # or: setup codex | setup agy | setup all
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- User guide: [github.com/miuzel/harness-reflex/blob/276777c7cd5a6a081243d1a9368da8559ac831d7/USER_GUIDE.md](https://github.com/miuzel/harness-reflex/blob/276777c7cd5a6a081243d1a9368da8559ac831d7/USER_GUIDE.md)
- Changelog: [github.com/miuzel/harness-reflex/blob/276777c7cd5a6a081243d1a9368da8559ac831d7/CHANGELOG.md](https://github.com/miuzel/harness-reflex/blob/276777c7cd5a6a081243d1a9368da8559ac831d7/CHANGELOG.md)

## Limits and data handling

Tool output, plans and claims that are checked go to the configured System One backend. Several host integrations are marked unverified in the README. `package.json` declares MIT, but the repository has no license file, so reuse terms are not granted; the npm release was not yet published at review.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 276777c7cd5a](https://github.com/miuzel/harness-reflex/tree/276777c7cd5a6a081243d1a9368da8559ac831d7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
