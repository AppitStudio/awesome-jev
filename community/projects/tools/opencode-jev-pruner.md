# opencode-jev-pruner (OpenCode V2 plugin where Jev drops irrelevant MCP tools and skills from each request)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Context-only middleware for OpenCode V2: before every model call it asks Jev which MCP servers, MCP tools and skills are relevant to the prompt and removes the rest from the outgoing request (Code Mode catalogs, native tool maps and skill lists), cutting input tokens and wrong-tool calls. Tool registries and connections are untouched.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/theroich/opencode-jev-pruner) |
| Maintainer | [theroich](https://github.com/theroich). Independently curated. |
| Format | OpenCode V2 plugin (TypeScript) |
| Requirements | OpenCode V2 and an OpenCode console key for its System One endpoint. |
| License | [MIT](https://github.com/theroich/opencode-jev-pruner/blob/c552e5e20a141608646d5453f78b6394dd74e166/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/theroich/opencode-jev-pruner/blob/c552e5e20a141608646d5453f78b6394dd74e166/src/config.ts) at the pinned commit. |

## When to use

- Shrink prompts in OpenCode sessions with many MCP servers and skills.
- Mismatch: OpenCode V2 only; a pruned tool can still be called by name.

## How it works

`src/config.ts` points at OpenCode's System One endpoint (`https://opencode.ai/inference/systemone/v1/systemone`, `jev-1.13`); a first request keeps or drops whole servers, a second filters tools and skills above a probability threshold. Integration evidence: [`src/config.ts`](https://github.com/theroich/opencode-jev-pruner/blob/c552e5e20a141608646d5453f78b6394dd74e166/src/config.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/theroich/opencode-jev-pruner
# register the plugin in OpenCode V2 per the README and set the key from .env.example
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/theroich/opencode-jev-pruner#readme](https://github.com/theroich/opencode-jev-pruner#readme)

## Limits and data handling

The prompt and tool and skill descriptions go to OpenCode's Jev endpoint on each turn.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit c552e5e20a14](https://github.com/theroich/opencode-jev-pruner/tree/c552e5e20a141608646d5453f78b6394dd74e166). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
