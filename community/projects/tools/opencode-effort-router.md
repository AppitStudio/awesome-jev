# opencode-effort-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode 2 plugin that picks a reasoning effort (low to max) per request for allowlisted models using the OpenRouter Decisions API, defaulting to TypeSafe Jev, with cache-preserving Anthropic and OpenAI adapters.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/draxxris/opencode-effort-router) |
| Maintainer | [draxxris](https://github.com/draxxris). Independently curated. |
| Format | OpenCode plugin (TypeScript) |
| Requirements | OpenCode 2, Node.js to build, `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/draxxris/opencode-effort-router/blob/9ff722f2571b92c3f4f845ae19d3feb080e131dd/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/draxxris/opencode-effort-router/blob/9ff722f2571b92c3f4f845ae19d3feb080e131dd/src/config.ts) at the pinned commit. |

## When to use

- Spend high effort only on turns that need it in OpenCode.
- Already use OpenRouter and want a fast decision model to choose effort.
- Mismatch: built from a local clone; not published to a registry at review time.

## How it works

For each request to a model on the `targets` allowlist, the plugin sends trimmed context to `https://openrouter.ai/api/alpha/decisions` and maps the chosen label to that provider's effort setting. `src/config.ts` sets `typesafe/jev-1.13` as the default decision model. Integration evidence: [`src/config.ts`](https://github.com/draxxris/opencode-effort-router/blob/9ff722f2571b92c3f4f845ae19d3feb080e131dd/src/config.ts).

## Get started

From the upstream README: clone, `npm install --include=dev && npm run build`, then add the local path to `plugins` in `opencode.jsonc`.

```sh
git clone https://github.com/draxxris/opencode-effort-router ../opencode-effort-router
cd ../opencode-effort-router && npm install --include=dev && npm run build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README `opencode.jsonc` example with Anthropic and OpenAI targets

## Limits and data handling

Up to `maxContextChars` of each request goes to OpenRouter for the decision. Wrong effort picks can raise cost or lower quality.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 9ff722f2571b](https://github.com/draxxris/opencode-effort-router/tree/9ff722f2571b92c3f4f845ae19d3feb080e131dd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
