# jev-mcp (rules over OpenRouter)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Personal MCP server that lets Claude and other assistants ask Jev yes/no and multiple-choice rules written in a YAML file, returning a decision with a probability and flagging uncertain results for the user.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/achapla/jev-mcp) |
| Maintainer | [achapla](https://github.com/achapla). Independently curated. |
| Format | MCP server (TypeScript, Node) |
| Requirements | Node.js and pnpm; an OpenRouter API key; an MCP client such as Claude Code or Claude Desktop. |
| License | [MIT](https://github.com/achapla/jev-mcp/blob/8d200fdbd131ffdb1188a0cac4c416c9e3f0bc83/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/achapla/jev-mcp/blob/8d200fdbd131ffdb1188a0cac4c416c9e3f0bc83/src/jev.ts) at the pinned commit. |

## When to use

- Keep decision rules (split this issue? reply today? open the PR now?) in a YAML file instead of hard-coding a workflow.
- Give an assistant a probability-backed answer with a threshold per rule.
- Mismatch: the author says it fits their own workflow and skips score, box and image questions.

## How it works

`src/jev.ts` calls `~typesafe/jev-latest` through OpenRouter; the server exposes tools such as `evaluate_rules` that take the context and rule ids, ask Jev, and compare each probability with the rule's threshold, marking answers near the threshold as uncertain. Integration evidence: [`src/jev.ts`](https://github.com/achapla/jev-mcp/blob/8d200fdbd131ffdb1188a0cac4c416c9e3f0bc83/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/achapla/jev-mcp.git
cd jev-mcp
pnpm install && pnpm build
claude mcp add jev --scope user -e OPENROUTER_API_KEY=sk-or-... -- node /full/path/to/jev-mcp/dist/index.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example rules and tips in `examples/README.md`.

## Limits and data handling

The context you pass (issues, emails, tickets) goes to OpenRouter and TypeSafe on your key.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 8d200fdbd131](https://github.com/achapla/jev-mcp/tree/8d200fdbd131ffdb1188a0cac4c416c9e3f0bc83). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
