# AiWrangler (guardrails for coding agents where deterministic rules run first and Jev judges plans and diffs against your project's spec and review rules)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server, CLI and editor plugin that checks a coding agent's plans and diffs against the documents that govern your repo (protocol spec, review rules, rulings, open questions): offline rules run first, then Jev judges whether a diff does what the task claims, contradicts the spec or takes sides on an unruled question. Every verdict cites its source and is written to an append-only audit ledger; findings touching secrets or one-way doors need a human approval the agent cannot give.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kodr-pro/AiWrangler) |
| Maintainer | [kodr-pro](https://github.com/kodr-pro). Independently curated. |
| Format | npm package `@kodr/aiwrangler` with CLI, MCP server and editor plugin (TypeScript, Apache-2.0) |
| Requirements | Node.js 20+ and a `TYPESAFE_API_KEY`; without a key only the deterministic rules run and checks are marked degraded. |
| License | [Apache-2.0](https://github.com/kodr-pro/AiWrangler/blob/da8b0b71cf8c2cf9fa617039de89749111a2e0e1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/client.ts`](https://github.com/kodr-pro/AiWrangler/blob/da8b0b71cf8c2cf9fa617039de89749111a2e0e1/src/jev/client.ts) at the pinned commit. |

## When to use

- Hold coding agents to a written spec and review rules, with an audit trail of every verdict.
- Mismatch: repos without governing documents for it to check against.

## How it works

`src/jev/client.ts` creates a `TypeSafeClient` from the TypeSafe SDK with `TYPESAFE_API_KEY` and default model `jev-1.13.0` (set in `src/config.ts`) and warns that task, diff and spec text goes to `api.typesafe.ai`; semantic egress can be turned off in config. Integration evidence: [`src/jev/client.ts`](https://github.com/kodr-pro/AiWrangler/blob/da8b0b71cf8c2cf9fa617039de89749111a2e0e1/src/jev/client.ts).

## Get started

Export your key and add the MCP server to your agent, or run the owner CLI with `npx`.

```sh
export TYPESAFE_API_KEY=...
npx -y --package @kodr/aiwrangler aiwrangler        # owner CLI
npx -y --package @kodr/aiwrangler aiwrangler-mcp    # MCP server for your agent
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kodr-pro/AiWrangler/blob/da8b0b71cf8c2cf9fa617039de89749111a2e0e1/README.md](https://github.com/kodr-pro/AiWrangler/blob/da8b0b71cf8c2cf9fa617039de89749111a2e0e1/README.md)
- npm: [www.npmjs.com/package/@kodr/aiwrangler](https://www.npmjs.com/package/@kodr/aiwrangler)

## Limits and data handling

With the semantic judge on, task, diff and spec text is sent to TypeSafe on your key. Verdicts are only as good as the documents you supply; the human-review gate is enforced by the tool, not by your agent.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit da8b0b71cf8c](https://github.com/kodr-pro/AiWrangler/tree/da8b0b71cf8c2cf9fa617039de89749111a2e0e1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
