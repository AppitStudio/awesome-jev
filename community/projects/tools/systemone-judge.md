# systemone-judge (MCP/CLI runner for TypeSafe Jev and local Laya decision engines)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

MCP server, CLI and TypeScript SDK for System One decision models: configure `typesafe-direct` or OpenAI-compatible chat-completions protocols for hosted Jev, or `--laya` for local CPU inference, aimed at Claude Code, Cursor and similar agents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ridlo543/systemone-judge) |
| Maintainer | [Ridlo543](https://github.com/Ridlo543). Independently curated. |
| Format | MCP server + CLI + TypeScript SDK (MIT) |
| Requirements | Node/Bun or the released binaries; a TypeSafe (or compatible) base URL and key for hosted Jev, or Laya for offline. |
| License | [MIT](https://github.com/Ridlo543/systemone-judge/blob/fde2ee1b450bc16c6f4fddf78fde609fa392c94e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/config.ts`](https://github.com/Ridlo543/systemone-judge/blob/fde2ee1b450bc16c6f4fddf78fde609fa392c94e/src/config.ts) at the pinned commit. |

## When to use

- Expose Jev/Laya as MCP tools inside coding agents.
- Switch between hosted TypeSafe-direct and local Laya.
- Mismatch: defaults are configurable; you must point base URL/model at Jev yourself.

## How it works

`src/config.ts` resolves protocol `typesafe-direct` or chat-completions with `JEV_BASE_URL` / `SYSTEMONE_BASE_URL` and API key; `src/client.ts` posts System One requests to the configured endpoint. Integration evidence: [`src/config.ts`](https://github.com/Ridlo543/systemone-judge/blob/fde2ee1b450bc16c6f4fddf78fde609fa392c94e/src/config.ts).

## Get started

`npx -y -p systemone-judge systemone setup` or install binaries per README; set base URL to TypeSafe and your key.

```sh
git clone https://github.com/Ridlo543/systemone-judge.git && cd systemone-judge
# configure SYSTEMONE_BASE_URL=https://api.typesafe.ai and API key
npx -y -p systemone-judge systemone-mcp
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Ridlo543/systemone-judge/blob/fde2ee1b450bc16c6f4fddf78fde609fa392c94e/README.md](https://github.com/Ridlo543/systemone-judge/blob/fde2ee1b450bc16c6f4fddf78fde609fa392c94e/README.md)

## Limits and data handling

Whatever you send as state/questions goes to the configured endpoint on your key. Local Laya stays on-machine.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit fde2ee1b450b](https://github.com/Ridlo543/systemone-judge/tree/fde2ee1b450bc16c6f4fddf78fde609fa392c94e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
