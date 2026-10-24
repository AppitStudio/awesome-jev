# DecisionLint (lint Jev and Luna decision questions in VS Code, CI and MCP)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Linter for the questions you send to decision models: flags mistakes in Jev and OpenAI Luna requests in JSON, JavaScript, TypeScript, Python, Rust and Go as you type, with fixes, a CLI for CI (SARIF and JUnit), an MCP server, and optional Ask commands that have a model review a file.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nolindnaidoo/decisionlint) |
| Maintainer | [nolindnaidoo](https://github.com/nolindnaidoo). Independently curated. |
| Format | VS Code extension, npm CLI and MCP server (TypeScript) |
| Requirements | VS Code 1.101+ or an Open VSX editor, or Node.js for the CLI and MCP server; a provider key only for the Ask and Probe commands. |
| License | [MIT](https://github.com/nolindnaidoo/decisionlint/blob/eb1a14e193c8503bb2d096de52b36da4aff92e4f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/ask/client.ts`](https://github.com/nolindnaidoo/decisionlint/blob/eb1a14e193c8503bb2d096de52b36da4aff92e4f/src/ask/client.ts) at the pinned commit. |

## When to use

- Catch overlapping options, wrong question types and malformed requests before paying for calls.
- Run the same rules in CI with exit codes and SARIF.
- Mismatch: linting is local; only the Ask and Probe commands send questions to a provider.

## How it works

Lint rules run locally. The Ask commands (`src/ask/client.ts`, `src/ask/provider.ts`) send the file's questions to TypeSafe (`jev-1.13.0`), OpenRouter (`typesafe/jev-1.13`), Vercel AI Gateway, OpenAI or another platform you choose, each with its own key. Integration evidence: [`src/ask/client.ts`](https://github.com/nolindnaidoo/decisionlint/blob/eb1a14e193c8503bb2d096de52b36da4aff92e4f/src/ask/client.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npx decisionlint
# or in VS Code: ext install nolindnaidoo.decisionlint
# MCP: npx -y decisionlint-mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- VS Code Marketplace: [marketplace.visualstudio.com/items?itemName=nolindnaidoo.decisionlint](https://marketplace.visualstudio.com/items?itemName=nolindnaidoo.decisionlint)
- npm: [www.npmjs.com/package/decisionlint](https://www.npmjs.com/package/decisionlint)

## Limits and data handling

Ask and Probe send your questions (and state only if you enable it) to the chosen platform. Distinct from the listed PHP decisions-lint.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit eb1a14e193c8](https://github.com/nolindnaidoo/decisionlint/tree/eb1a14e193c8503bb2d096de52b36da4aff92e4f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
