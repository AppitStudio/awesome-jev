# context-eng by Mayank Baral (local project-memory MCP server for Codex, Claude Code and Cursor that uses Jev to filter recalled memories)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Stores agent memories (decisions, preferences, workflows, mistakes) in local SQLite databases per category, retrieves candidates with SQLite FTS5, and asks Jev which candidates are actually relevant before returning them to the agent. `init` registers the MCP server for Cursor, Claude Code and Codex and keeps the TypeSafe key in the OS keychain.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mayank-devac/context-eng) |
| Maintainer | [mayank-devac](https://github.com/mayank-devac). Independently curated. |
| Format | Node.js CLI and MCP server (npm `context-eng`) |
| Requirements | Node.js 20+; a TypeSafe API key (optional; skip it at `init`). |
| License | [MIT](https://github.com/mayank-devac/context-eng/blob/8cbd3125c0a2ffefb65fda62143fcbbef67139bc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/typesafe.ts`](https://github.com/mayank-devac/context-eng/blob/8cbd3125c0a2ffefb65fda62143fcbbef67139bc/src/typesafe.ts) at the pinned commit. |

## When to use

- Give coding agents persistent project memory where Jev drops irrelevant recalls.
- Mismatch: shared team memory servers; memories live per user under ~/.context.

## How it works

`src/typesafe.ts` posts recalled candidates to `https://api.typesafe.ai/v1/systemone` with a 20 s deadline and keeps hits above a 0.5 relevance threshold; FTS5 does the first-pass retrieval locally. Integration evidence: [`src/typesafe.ts`](https://github.com/mayank-devac/context-eng/blob/8cbd3125c0a2ffefb65fda62143fcbbef67139bc/src/typesafe.ts).

## Get started

Run `init` inside your project repository.

```sh
cd your-project
npx context-eng@0.1.3 init
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/mayank-devac/context-eng/blob/8cbd3125c0a2ffefb65fda62143fcbbef67139bc/README.md](https://github.com/mayank-devac/context-eng/blob/8cbd3125c0a2ffefb65fda62143fcbbef67139bc/README.md)

## Limits and data handling

Queries and candidate memories are sent to TypeSafe for relevance filtering when a key is set. `init` edits user-level MCP configs and AGENTS.md/CLAUDE.md blocks. Version 0.1.3 at review.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 8cbd3125c0a2](https://github.com/mayank-devac/context-eng/tree/8cbd3125c0a2ffefb65fda62143fcbbef67139bc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
