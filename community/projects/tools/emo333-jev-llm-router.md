# jev-llm-router (Pi)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi extension that uses Jev to select a model and thinking level for each user task, keeps the pair through tool continuations, and supports subagents selecting `jev/auto`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/emo333/jev-llm-router) |
| Maintainer | [emo333](https://github.com/emo333). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi 1.0.0+, Node.js 22.19+, Git; Jev provider key. |
| License | [MIT](https://github.com/emo333/jev-llm-router/blob/9836da702f1e92c4e2e49a5d7aca38d8a21bb3f7/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev-llm-rtr.ts`](https://github.com/emo333/jev-llm-router/blob/9836da702f1e92c4e2e49a5d7aca38d8a21bb3f7/src/jev-llm-rtr.ts) at the pinned commit. |

## When to use

- Route Pi tasks to cheaper or stronger models automatically.
- Use `jev/auto` for subagents and nested subagents.
- Mismatch: Pi-only.

## How it works

On each new user task the extension asks Jev to choose a model and thinking level from configured options, then pins that pair for continuations. Integration evidence: [`src/jev-llm-rtr.ts`](https://github.com/emo333/jev-llm-router/blob/9836da702f1e92c4e2e49a5d7aca38d8a21bb3f7/src/jev-llm-rtr.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/emo333/jev-llm-router
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Configuration in the upstream README.

## Limits and data handling

Task text is sent to the Jev provider and billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 9836da702f1e](https://github.com/emo333/jev-llm-router/tree/9836da702f1e92c4e2e49a5d7aca38d8a21bb3f7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
