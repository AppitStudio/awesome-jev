# You need to learn Jev RIGHT NOW (NetworkChuck's step-by-step companion guide)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Companion guide to the NetworkChuck video: five chapters from trying Jev in the Playground with a spam comment, to a first API call, to letting a coding agent install TypeSafe's skill, to building the model router from the video (Jev picks a small, medium or large model per request), plus a roundup of what people built.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/theNetworkChuck/jev-guide) |
| Maintainer | [theNetworkChuck](https://github.com/theNetworkChuck). Independently curated. |
| Format | Guide with shell and TypeScript examples |
| Requirements | A TypeSafe account; Node.js and an OpenRouter key for the router chapter. |
| License | [MIT](https://github.com/theNetworkChuck/jev-guide/blob/6e72b3b842dbf225765d1f81266ca0bb3ab8c6a2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`examples/router/router.ts`](https://github.com/theNetworkChuck/jev-guide/blob/6e72b3b842dbf225765d1f81266ca0bb3ab8c6a2/examples/router/router.ts) at the pinned commit. |

## When to use

- Learn Jev's question types hands-on, starting with no code.
- Mismatch: a learning resource, not a library.

## How it works

`examples/spam-check.sh` sends the Playground questions with curl; `examples/router/router.ts` asks Jev which model size fits each request and forwards it through OpenRouter. Integration evidence: [`examples/router/router.ts`](https://github.com/theNetworkChuck/jev-guide/blob/6e72b3b842dbf225765d1f81266ca0bb3ab8c6a2/examples/router/router.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/theNetworkChuck/jev-guide && cd jev-guide
# start with guide/01-playground.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Guide chapters: [github.com/theNetworkChuck/jev-guide/tree/main/guide](https://github.com/theNetworkChuck/jev-guide/tree/main/guide)

## Limits and data handling

Example calls send their text to TypeSafe (and OpenRouter for the router).

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 6e72b3b842db](https://github.com/theNetworkChuck/jev-guide/tree/6e72b3b842dbf225765d1f81266ca0bb3ab8c6a2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
