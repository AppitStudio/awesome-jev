# Customaise MCP (MCP server and CLI for the Customaise Chrome extension, whose Script Decisions can run on Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server and CLI that connect coding agents (Claude Code, Cursor, Codex, Kiro and others) to the Customaise Chrome extension: manage UserScripts, build AgentScripts, call WebMCP tools inside the signed-in browser session, pick DOM elements and drive tabs. Its Script Decisions feature lets a script ask typed questions with `CM_decisions`; the person chooses Jev, the OpenAI Decisions API or the Gemini Decisions API per script and saves their own key. The MCP server's `get_script_decisions` and `set_script_decisions` tools read and switch that provider, and it ships a guide comparing the three.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/getcustomaise/customaise-mcp) |
| Maintainer | [getcustomaise](https://github.com/getcustomaise). Independently curated. |
| Format | Node.js MCP server and CLI (npm `@customaise/mcp`) (MIT); the Chrome extension itself is a separate product |
| Requirements | Chrome 147+ with the Customaise extension (sign-in; Script Decisions needs the Power User plan and extension 1.3.8+), Node.js for `npx`, and your own Jev (TypeSafe) key saved in Customaise. |
| License | [MIT](https://github.com/getcustomaise/customaise-mcp/blob/a357645b633a024056758e61b8f4e2db99e2f270/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/server.ts`](https://github.com/getcustomaise/customaise-mcp/blob/a357645b633a024056758e61b8f4e2db99e2f270/src/server.ts) at the pinned commit. |

## When to use

- Give a coding agent a real Chrome session and let browser scripts make typed decisions on Jev.
- Mismatch: an open-source end-to-end stack; the extension that makes the Jev calls is a closed product.

## How it works

`src/server.ts` registers `set_script_decisions` with the provider choice `jev`, `openai-decisions` or `gemini-decisions`; `src/script-decisions-guide.ts` documents how scripts call `CM_decisions` and what Jev accepts. The decision calls themselves are made by the extension with the user's saved key. Integration evidence: [`src/server.ts`](https://github.com/getcustomaise/customaise-mcp/blob/a357645b633a024056758e61b8f4e2db99e2f270/src/server.ts).

## Get started

Install the extension and turn on Agent Bridge, add the MCP server to your IDE, then read the Script Decisions guide resource.

```sh
claude mcp add customaise -- npx -y @customaise/mcp
npx -y @customaise/mcp   # or as customaise-mcp from Cursor's mcp.json
customaise resource script-decisions
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/getcustomaise/customaise-mcp/blob/a357645b633a024056758e61b8f4e2db99e2f270/README.md](https://github.com/getcustomaise/customaise-mcp/blob/a357645b633a024056758e61b8f4e2db99e2f270/README.md)
- Script Decisions guide: [customaise.com/learn/script-decisions](https://customaise.com/learn/script-decisions)

## Limits and data handling

The MCP server is MIT; the Customaise extension (where Script Decisions run) is closed source and was not inspected. Customaise has Free and Power User plans (see customaise.com/pricing; prices not verified here). Decisions are billed to the person's own provider key; script inputs go to the chosen provider.

## Review and maintenance

Reviewed **2026-11-18** (Europe/Sofia) at [commit a357645b633a](https://github.com/getcustomaise/customaise-mcp/tree/a357645b633a024056758e61b8f4e2db99e2f270). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
