# Traits

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reusable coding preferences for AI agents: feedback becomes Markdown trait files in `.agents/traits/`, and the agent proposes, gets approval for, and checks its work against them over MCP, with TypeSafe available as a model provider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/crosshatch/traits) |
| Maintainer | [crosshatch](https://github.com/crosshatch). Independently curated. |
| Format | npm package + MCP server |
| Requirements | Node.js; an agent with MCP support; a model provider you choose during setup (TypeSafe is one of the bundled providers). |
| License | [Apache-2.0](https://github.com/crosshatch/traits/blob/e538a6d2083798284dbf17ea476891f8b517b807/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/SamSimonds8/status/2111945655497138547)). |
| Jev evidence | [`traits/package.json`](https://github.com/crosshatch/traits/blob/e538a6d2083798284dbf17ea476891f8b517b807/traits/package.json) at the pinned commit. |

## When to use

- Want an agent to learn and keep your code-style preferences across sessions.
- Want those preferences as reviewable files in the repo, shared with your team.
- Mismatch: model assessments are guidance, not guarantees; Jev is one provider option, not required.

## How it works

Traits stores each preference as a Markdown file with `name`, `subject`, `requirement` and `purpose`. The agent proposes new traits from your feedback, asks you to approve changes, and checks its output against them through the Traits MCP server. The `traits` package lists `@effect/ai-typesafe` as a provider dependency, and the maker describes Jev as part of the tool on X. Integration evidence: [`traits/package.json`](https://github.com/crosshatch/traits/blob/e538a6d2083798284dbf17ea476891f8b517b807/traits/package.json).

## Get started

From the upstream README: paste the setup prompt into your agent inside your project; it follows `SETUP.md`, asks you to pick providers and models, and keeps existing config.

```sh
# inside your agent, in your project:
# Set up Traits using https://github.com/crosshatch/traits/blob/main/SETUP.md
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [traits.sh](https://traits.sh)
- [www.npmjs.com/package/traits](https://www.npmjs.com/package/traits)

## Limits and data handling

Code and feedback are sent to the model provider you configure. Trait checks are model judgments and can be wrong.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit e538a6d20837](https://github.com/crosshatch/traits/tree/e538a6d2083798284dbf17ea476891f8b517b807). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
