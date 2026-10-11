# Jev Starter

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Jev Starter is a skeleton for small web apps that make decisions with Jev through OpenRouter: Express plus Vite/React/TypeScript, an AGENTS.md guide for coding agents, and Docker plus Caddy deployment to a VPS.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/simplybychris/jev-starter) |
| Maintainer | [simplybychris](https://github.com/simplybychris). Independently curated. |
| Format | Node/React starter template |
| Requirements | Node.js 22.12+; an OpenRouter key with credits; optional VPS for deploy. |
| License | [MIT](https://github.com/simplybychris/jev-starter/blob/bdbb39b913cf807302ba772d6f3cd203a0747479/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Bootstrap a small Jev-backed web app with a coding agent.
- Mismatch: uses OpenRouter only; template, not a library.

## How it works

A server route calls Jev via OpenRouter with Choice, Score and yes/no questions; the React front end shows answers, time and cost. (Summarized from the upstream [README](https://github.com/simplybychris/jev-starter/blob/bdbb39b913cf807302ba772d6f3cd203a0747479/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Copy `.env.example` to `.env`, add your OpenRouter key, then `npm install` and `npm run dev`.

## Limits and data handling

Input text is sent to OpenRouter. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit bdbb39b913cf](https://github.com/simplybychris/jev-starter/tree/bdbb39b913cf807302ba772d6f3cd203a0747479). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
