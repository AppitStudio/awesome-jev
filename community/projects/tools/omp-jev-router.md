# omp jev-router by Daniel Morris (oh-my-pi plugin that picks the model for each turn and agent for each task from a Jev classification plus live quota)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

An extension for the omp (oh-my-pi) coding agent: before each turn it asks Jev how demanding the prompt is (quick, balanced, strong) and combines that with the provider usage limits omp already tracks, so cheap questions go to cheap models and exhausted models are skipped. Part of the author's omp-plugins marketplace repo.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danieljohnmorris/omp-plugins) |
| Maintainer | [danieljohnmorris](https://github.com/danieljohnmorris). Independently curated. |
| Format | omp plugin (TypeScript) |
| Requirements | omp; a TypeSafe API key. |
| License | [MIT](https://github.com/danieljohnmorris/omp-plugins/blob/219a6900a09434e2c9a9f6bcdcc4fa1c379a8df5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/jev-router/src/router.ts`](https://github.com/danieljohnmorris/omp-plugins/blob/219a6900a09434e2c9a9f6bcdcc4fa1c379a8df5/plugins/jev-router/src/router.ts) at the pinned commit. |

## When to use

- Route omp turns and subagent tasks by difficulty and remaining quota.
- Mismatch: other coding agents; it is specific to omp.

## How it works

`plugins/jev-router/src/router.ts` posts the classification question to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) inside omp, with no proxy process. Integration evidence: [`plugins/jev-router/src/router.ts`](https://github.com/danieljohnmorris/omp-plugins/blob/219a6900a09434e2c9a9f6bcdcc4fa1c379a8df5/plugins/jev-router/src/router.ts).

## Get started

Add the marketplace and install the plugin, then restart omp.

```sh
omp plugin marketplace add danieljohnmorris/omp-plugins
omp plugin install jev-router@omp-plugins
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Plugin README: [github.com/danieljohnmorris/omp-plugins/blob/219a6900a09434e2c9a9f6bcdcc4fa1c379a8df5/plugins/jev-router/README.md](https://github.com/danieljohnmorris/omp-plugins/blob/219a6900a09434e2c9a9f6bcdcc4fa1c379a8df5/plugins/jev-router/README.md)

## Limits and data handling

Prompts (or their classification input) are sent to TypeSafe. Replaces the archived omp-jev-router repository.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 219a6900a094](https://github.com/danieljohnmorris/omp-plugins/tree/219a6900a09434e2c9a9f6bcdcc4fa1c379a8df5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
