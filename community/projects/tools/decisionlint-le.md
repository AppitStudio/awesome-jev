# DecisionLint-LE

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Linter for the questions you send to Jev (and Decisions-API-shaped models): VS Code extension, CI command line and MCP server that flag question wording measured to produce bad answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nolindnaidoo/decisionlint-le) |
| Maintainer | [nolindnaidoo](https://github.com/nolindnaidoo). Independently curated. |
| Format | VS Code / Open VSX extension, npm CLI and MCP server (TypeScript) |
| Requirements | Node.js for the CLI; no key needed for linting. Optional live check uses your own TypeSafe or OpenAI key. |
| License | [MIT](https://github.com/nolindnaidoo/decisionlint-le/blob/b4f0dd9f2da47609f93fc5305508bad5ed50e010/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/cli/mcp.ts`](https://github.com/nolindnaidoo/decisionlint-le/blob/b4f0dd9f2da47609f93fc5305508bad5ed50e010/src/cli/mcp.ts) at the pinned commit. |

## When to use

- Lint Jev request JSON and question definitions in code as you type or in CI.
- Give an agent an MCP tool that reviews decision questions before they ship.
- Mismatch: checks question wording, not model accuracy.

## How it works

Rules read Jev-style request bodies out of JSON and source files and report risky question patterns offline. One optional command sends a file to the model you choose (TypeSafe Jev or another Decisions endpoint) with your key. Integration evidence: [`src/cli/mcp.ts`](https://github.com/nolindnaidoo/decisionlint-le/blob/b4f0dd9f2da47609f93fc5305508bad5ed50e010/src/cli/mcp.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npx decisionlint-le src/
npx decisionlint-le --format github .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- VS Code: `ext install nolindnaidoo.jevlint-le`.
- MCP: `npx -y decisionlint-le-mcp`.

## Limits and data handling

Linting runs locally with no network calls. The optional model check sends the file's questions to the endpoint you configure, billed to your key.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit b4f0dd9f2da4](https://github.com/nolindnaidoo/decisionlint-le/tree/b4f0dd9f2da47609f93fc5305508bad5ed50e010). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
