# ynab-mcp-server (MCP server for YNAB with an opt-in Jev category-suggestion preview)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Model Context Protocol server that lets Claude Code, Claude Desktop or a remote MCP client read and modify a YNAB budget, locally over stdio or as a Cloudflare Worker. An opt-in tool previews category suggestions for unapproved, uncategorized outflows using Jev; it never applies suggestions or approves transactions by itself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/calebl/ynab-mcp-server) |
| Maintainer | [calebl](https://github.com/calebl). Independently curated. |
| Format | TypeScript · MCP server (stdio or Cloudflare Worker) |
| Requirements | Node.js; a YNAB Personal Access Token; `TYPESAFE_API_KEY` plus `YNAB_AI_CATEGORIZATION=true` for the suggestion tool. |
| License | [MIT](https://github.com/calebl/ynab-mcp-server/blob/7255f1c9505a95b3d83229beb391158bf5b8e5cb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/tools/SuggestCategoriesTool.ts`](https://github.com/calebl/ynab-mcp-server/blob/7255f1c9505a95b3d83229beb391158bf5b8e5cb/src/tools/SuggestCategoriesTool.ts) at the pinned commit. |

## When to use

- Let an assistant propose budget categories that you then confirm.
- Mismatch: suggestions are previews only; nothing is categorized without a separate write.

## How it works

`src/tools/SuggestCategoriesTool.ts` sends each eligible transaction (payee, memo, amount and the budget's category list) to `api.typesafe.ai/v1/systemone` pinned to `jev-1.13.0` as a choice question, with a 10 s timeout; the tool is only exposed when both the key and the opt-in flag are set. Integration evidence: [`src/tools/SuggestCategoriesTool.ts`](https://github.com/calebl/ynab-mcp-server/blob/7255f1c9505a95b3d83229beb391158bf5b8e5cb/src/tools/SuggestCategoriesTool.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/calebl/ynab-mcp-server.git && cd ynab-mcp-server
npm install && npm run build
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Local decision-model notes: [github.com/calebl/ynab-mcp-server/blob/main/docs/local-decision-model.md](https://github.com/calebl/ynab-mcp-server/blob/main/docs/local-decision-model.md)

## Limits and data handling

Transaction details are sent to TypeSafe when the suggestion tool runs; `YNAB_AI_TYPICAL_PAYEES` additionally sends frequent payee names (off by default). The YNAB token stays in the server environment. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 7255f1c9505a](https://github.com/calebl/ynab-mcp-server/tree/7255f1c9505a95b3d83229beb391158bf5b8e5cb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
