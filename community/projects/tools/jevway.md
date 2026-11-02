# jevway (hand a browser goal to Jev from your coding agent and get one short summary back)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

MCP server, Claude Code plugin and CLI that take a browser goal from a coding agent and let Jev pick each click, type and select in your own Chrome or a throwaway one, returning a short verified summary instead of every step. Formerly jev-browse; built on the browser-use jev-ultrafast loop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AbdallahAHO/jevway) |
| Maintainer | [AbdallahAHO](https://github.com/AbdallahAHO). Independently curated. |
| Format | TypeScript MCP server + CLI (npm `jevway`) |
| Requirements | Node.js, Chrome, `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY`. |
| License | [MIT](https://github.com/AbdallahAHO/jevway/blob/d15ec66ac63eb370e9a434b894416c100ab1a2b3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev/decide.ts`](https://github.com/AbdallahAHO/jevway/blob/d15ec66ac63eb370e9a434b894416c100ab1a2b3/src/jev/decide.ts) at the pinned commit. |

## When to use

- Offload routine browser steps from an agent to a fast decision model.
- Mismatch: Jev picks actions from a DOM snapshot; complex pages may need the agent to take over.

## How it works

`src/jev/decide.ts` uses `@typesafe-ai/sdk` to send the page snapshot and the action space to Jev as typed questions each step, with optional screenshot questions on Jev 1.14; `jevway doctor` checks the key, route and browser before a run. Integration evidence: [`src/jev/decide.ts`](https://github.com/AbdallahAHO/jevway/blob/d15ec66ac63eb370e9a434b894416c100ab1a2b3/src/jev/decide.ts).

## Get started

From the upstream README (not run on the review host):

```sh
claude mcp add jevway -s user -- npx -y -p jevway jevway-mcp
npx -y jevway doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- npm package: [www.npmjs.com/package/jevway](https://www.npmjs.com/package/jevway)

## Limits and data handling

Page text from the sites you visit is sent to TypeSafe or OpenRouter on each step. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit d15ec66ac63e](https://github.com/AbdallahAHO/jevway/tree/d15ec66ac63eb370e9a434b894416c100ab1a2b3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
