# decisionkit (adityajha2005)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

decisionkit is a provider-neutral CLI, MCP server and Claude Code plugin for yes/no, choice, scale and rank decisions in coding agents, scripts and CI, with Jev (TypeSafe or OpenRouter) as one of its decision backends.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/adityajha2005/decisionkit) |
| Maintainer | [adityajha2005](https://github.com/adityajha2005). Independently curated. |
| Format | npm CLI, MCP server and Claude Code plugin |
| Requirements | Node.js 20+; a TypeSafe or OpenRouter key for Jev (other providers optional). |
| License | [MIT](https://github.com/adityajha2005/decisionkit/blob/06da6f7553714494f76fae13066e42cdcd01e430/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Add probability-scored decisions to shell scripts, CI jobs or MCP-capable coding agents.
- Mismatch: not Jev-only; probabilities from non-Jev providers are not comparable.

## How it works

You pipe text and a typed question to the CLI or MCP tool; decisionkit routes the request to the configured decision provider and returns probabilities. (Summarized from the upstream [README](https://github.com/adityajha2005/decisionkit/blob/06da6f7553714494f76fae13066e42cdcd01e430/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `npm i -g @adxtya21/decisionkit`, set the provider and key environment variables, and pipe text into `decisionkit choice`.

## Limits and data handling

Input text is sent to the selected provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 06da6f755371](https://github.com/adityajha2005/decisionkit/tree/06da6f7553714494f76fae13066e42cdcd01e430). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
