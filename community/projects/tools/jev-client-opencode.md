# jev-client (CLI, TUI, MCP server and web console for Jev through OpenCode)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Command-line client for asking Jev questions about a text or JSON payload through OpenCode's System One endpoint, with an interactive TUI, an MCP server so agents can call it, and a local web console; answers come back with probabilities per option.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/theroich/jev-client) |
| Maintainer | [theroich](https://github.com/theroich). Independently curated. |
| Format | TypeScript CLI, TUI and MCP server |
| Requirements | Node.js; an OpenCode Console key. |
| License | [MIT](https://github.com/theroich/jev-client/blob/ffefc36e75e2b6ed08a86b6f37ec4350c082ee7f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/theroich/jev-client/blob/ffefc36e75e2b6ed08a86b6f37ec4350c082ee7f/src/config.ts) at the pinned commit. |

## When to use

- Ask Jev from the terminal or from an MCP agent without writing code.
- Mismatch: goes through OpenCode rather than TypeSafe directly.

## How it works

`src/config.ts` points at `https://opencode.ai/inference/systemone/v1/systemone`; `src/cli.ts` builds the state and questions and prints each answer. Integration evidence: [`src/config.ts`](https://github.com/theroich/jev-client/blob/ffefc36e75e2b6ed08a86b6f37ec4350c082ee7f/src/config.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/theroich/jev-client && cd jev-client
npm install
npx jev ask --state "I was charged twice this month." --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/theroich/jev-client#readme](https://github.com/theroich/jev-client#readme)

## Limits and data handling

State and questions go to OpenCode and on to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit ffefc36e75e2](https://github.com/theroich/jev-client/tree/ffefc36e75e2b6ed08a86b6f37ec4350c082ee7f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
