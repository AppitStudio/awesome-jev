# toolscout (Claude Code mod: compact MCP tool catalog and Jev routing per message)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code mod for sessions with many MCP servers: it replaces the long deferred-tool list with one line per server, asks Jev on every message which tool groups are needed and adds a short hint, and calibrates its group definitions and threshold against Jev at session start; prompts and output are in Italian.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adapt-to-it/toolscout) |
| Maintainer | [adapt-to-it](https://github.com/adapt-to-it). Independently curated. |
| Format | Claude Code plugin (TypeScript) |
| Requirements | Claude Code; a TypeSafe API key for routing (without it, only the catalog is compacted). |
| License | [MIT](https://github.com/adapt-to-it/toolscout/blob/e61e9f7f606bd318de9324f328d032c19204410a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`hooks/routing/jev.ts`](https://github.com/adapt-to-it/toolscout/blob/e61e9f7f606bd318de9324f328d032c19204410a/hooks/routing/jev.ts) at the pinned commit. |

## When to use

- Keep context small when many MCP servers are connected.
- Point Claude to the right tools without loading every tool description.
- Mismatch: Italian-language prompts and hints; calibration also uses Haiku.

## How it works

`hooks/routing/jev.ts` posts each message with one question per tool group to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); groups above the calibrated threshold are named in the hint. Integration evidence: [`hooks/routing/jev.ts`](https://github.com/adapt-to-it/toolscout/blob/e61e9f7f606bd318de9324f328d032c19204410a/hooks/routing/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude plugin marketplace add adapt-to-it/toolscout
claude plugin install toolscout@adapt-to-it
# set typesafe_api_key when prompted, or TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/adapt-to-it/toolscout#readme](https://github.com/adapt-to-it/toolscout#readme)

## Limits and data handling

Each message and tool-group definitions go to TypeSafe; calibration sends tool names and generated test messages to Anthropic (Haiku).

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit e61e9f7f606b](https://github.com/adapt-to-it/toolscout/tree/e61e9f7f606bd318de9324f328d032c19204410a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
