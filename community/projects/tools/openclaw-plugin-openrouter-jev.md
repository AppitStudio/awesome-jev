# OpenRouter Jev Decisions (OpenClaw)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

OpenClaw decision-provider plugin that routes boolean, choice and score batches to Jev models through OpenRouter's Decisions API.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/eulrich101618/openclaw-plugin-openrouter-jev) |
| Maintainer | [eulrich101618](https://github.com/eulrich101618). Independently curated. |
| Format | OpenClaw plugin (TypeScript) |
| Requirements | OpenClaw; OpenRouter API key. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/index.ts`](https://github.com/eulrich101618/openclaw-plugin-openrouter-jev/blob/6376e9f8dda602ea0962191589c17ddc0b6424c8/src/index.ts) at the pinned commit. |

## When to use

- Use Jev as an OpenClaw decision provider.
- Mismatch: no LICENSE file; decisions only, no chat models.

## How it works

The plugin registers `openrouter-jev`, translates OpenClaw decision batches to OpenRouter Decisions requests, and returns probabilities. Integration evidence: [`src/index.ts`](https://github.com/eulrich101618/openclaw-plugin-openrouter-jev/blob/6376e9f8dda602ea0962191589c17ddc0b6424c8/src/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
# install per README (openclaw.plugin.json)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Tests: `src/index.test.ts`.

## Limits and data handling

Inputs go to OpenRouter.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 6376e9f8dda6](https://github.com/eulrich101618/openclaw-plugin-openrouter-jev/tree/6376e9f8dda602ea0962191589c17ddc0b6424c8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
