# JEV Orchestrator (Claude Code plugin where Jev picks the model, effort and tools for every subagent)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that intercepts every Agent spawn and asks Jev which model (Haiku, Sonnet or Opus), effort level and tool profile the subagent needs, plus a /jev-orchestrator:run command that executes a prompt file wave by wave with parallel subagents routed the same way. Failed tasks stop only the waves that depend on them, and commits happen only when you ask. Supports a TypeSafe key or an OpenRouter key, stored in the system keychain.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hiyoku/jev-orc) |
| Maintainer | [hiyoku](https://github.com/hiyoku). Independently curated. |
| Format | Claude Code plugin (TypeScript) |
| Requirements | Claude Code and a TypeSafe or OpenRouter API key. |
| License | [MIT](https://github.com/hiyoku/jev-orc/blob/ce65709982e32ec62e68c09f699ca317d1754c7d/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/hiyoku/jev-orc/blob/ce65709982e32ec62e68c09f699ca317d1754c7d/src/jev/client.ts) at the pinned commit. |

## When to use

- Stop paying Opus prices for subagents that only need Haiku, without setting models by hand.
- Mismatch: routing quality depends on your task mix; check the per-task reports.

## How it works

`src/hooks/spawn.ts` catches Agent tool calls and `src/jev/client.ts` sends the task description to Jev and reads back model, effort and tool-profile answers. Integration evidence: [`src/jev/client.ts`](https://github.com/hiyoku/jev-orc/blob/ce65709982e32ec62e68c09f699ca317d1754c7d/src/jev/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add hiyoku/jev-orc
/plugin install jev-orchestrator@jev-orc
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the flow diagram: [github.com/hiyoku/jev-orc#readme](https://github.com/hiyoku/jev-orc#readme)

## Limits and data handling

Subagent task descriptions are sent to TypeSafe or OpenRouter.

## Review and maintenance

Reviewed **2026-10-30** (Europe/Sofia) at [commit ce65709982e3](https://github.com/hiyoku/jev-orc/tree/ce65709982e32ec62e68c09f699ca317d1754c7d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
