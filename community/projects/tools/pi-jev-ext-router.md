# pi-jev-ext-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension where Jev (via OpenRouter) picks which lazily loaded extension a prompt needs and activates it before the model turn.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/shourovrm/pi-jev-ext-router) |
| Maintainer | [shourovrm](https://github.com/shourovrm). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | pi 1.0+ with pi-lazy-extensions; OpenRouter API key with `typesafe/jev-1.13` access. |
| License | [MIT](https://github.com/shourovrm/pi-jev-ext-router/blob/e763a9dbea88d160b31899fd6f0c5f073bebbd3f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/shourovrm/pi-jev-ext-router/blob/e763a9dbea88d160b31899fd6f0c5f073bebbd3f/src/jev.ts) at the pinned commit. |

## When to use

- Save round trips spent searching and activating lazy extensions.
- Gate Jev calls behind local cues so ordinary prompts are not sent.
- Mismatch: only useful with pi-lazy-extensions installed.

## How it works

A local cue gate decides whether a prompt is sent; if so, the router asks Jev through OpenRouter's Decisions endpoint which manifest entry is needed and runs `/ext activate` for confident answers. Integration evidence: [`src/jev.ts`](https://github.com/shourovrm/pi-jev-ext-router/blob/e763a9dbea88d160b31899fd6f0c5f073bebbd3f/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/shourovrm/pi-jev-ext-router
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Configuration: `<agent-dir>/jev-ext-router.json`.

## Limits and data handling

Prompts that pass the cue gate are sent to OpenRouter/TypeSafe and billed to your OpenRouter key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit e763a9dbea88](https://github.com/shourovrm/pi-jev-ext-router/tree/e763a9dbea88d160b31899fd6f0c5f073bebbd3f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
