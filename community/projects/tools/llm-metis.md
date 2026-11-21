# llm-metis by Kyeongmo Yang (local gateway for Codex and Claude Code where Jev picks tools and reasoning effort)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

`metis-codex` and `metis-claude` launch Codex or Claude Code through a local gateway; on each turn one Jev evaluation decides which tools to expose and how much reasoning effort to use, and the gateway tracks token usage. Jev is reached through OpenRouter (default), Vercel AI Gateway or TypeSafe directly.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gaeng2y/llm-metis) |
| Maintainer | [gaeng2y](https://github.com/gaeng2y). Independently curated. |
| Format | Node.js CLI + local gateway |
| Requirements | Node.js 22.15+, Codex CLI or Claude Code installed and signed in, and an OpenRouter, Vercel AI Gateway or TypeSafe key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/gaeng2y/llm-metis/blob/53da9ad319adcb9f8242c57e107ffcfd0a3c169e/src/jev.ts) at the pinned commit. |

## When to use

- Cut wasted reasoning and tool calls in Codex or Claude Code by letting Jev pick effort and tools per turn.
- Mismatch: production use; the author marks it experimental.

## How it works

`src/jev.ts` builds the Jev evaluation (via the AI SDK) and pins the provider (OpenRouter `only: ['typesafe']`, Vercel `typesafe-ai`, or TypeSafe `jev-latest`); `src/routing.ts` applies the answers to tool choice and effort before forwarding to the coding model. Integration evidence: [`src/jev.ts`](https://github.com/gaeng2y/llm-metis/blob/53da9ad319adcb9f8242c57e107ffcfd0a3c169e/src/jev.ts).

## Get started

Install from a checkout, configure a provider, then launch your coding client through Metis.

```sh
git clone https://github.com/gaeng2y/llm-metis.git && cd llm-metis
npm install
npm link
metis-codex configure
metis-codex   # or: metis-claude
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gaeng2y/llm-metis/blob/53da9ad319adcb9f8242c57e107ffcfd0a3c169e/README.md](https://github.com/gaeng2y/llm-metis/blob/53da9ad319adcb9f8242c57e107ffcfd0a3c169e/README.md)

## Limits and data handling

Turn context is sent to the selected Jev provider in addition to the coding model's provider. No license file: reuse terms are not granted. Not the same project as the existing Metis listing.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 53da9ad319ad](https://github.com/gaeng2y/llm-metis/tree/53da9ad319adcb9f8242c57e107ffcfd0a3c169e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
