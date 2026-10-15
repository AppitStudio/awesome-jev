# loadout

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Picks the model tier, skills and MCP servers for each Claude Code or Codex session from a large library using Jev, then launches the CLI with that selection through official flags without proxying agent traffic.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/erik-hedstrom/loadout) |
| Maintainer | [erik-hedstrom](https://github.com/erik-hedstrom). Independently curated. |
| Format | TypeScript CLI (npm build) |
| Requirements | Node.js; Claude Code or Codex; TypeSafe API key. |
| License | [Apache-2.0](https://github.com/erik-hedstrom/loadout/blob/fbee5cbadd85d2ae80ab467a258db1561295021c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/erik-hedstrom/loadout/blob/fbee5cbadd85d2ae80ab467a258db1561295021c/src/jev.ts) at the pinned commit. |

## When to use

- Load only the skills and MCP servers a task needs from a library of hundreds.
- Pick a model tier per session from the task and repo.
- Mismatch: per-decision cost and timing in the README are the author's benchmark figures.

## How it works

`loadout route` sends the task and repo summary with candidate skills/servers to `POST /v1/systemone`; Jev returns need, tier and fit scores, code applies thresholds to inject clear winners, and the CLI is launched with the selection. Integration evidence: [`src/jev.ts`](https://github.com/erik-hedstrom/loadout/blob/fbee5cbadd85d2ae80ab467a258db1561295021c/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/erik-hedstrom/loadout.git && cd loadout
npm install && npm run build && npm link
loadout route "rename the variable cnt to count in utils.py"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Benchmarks: `bench/RESULTS.md`.

## Limits and data handling

Task text, repo summary and library descriptions go to TypeSafe on your key; agent traffic is not proxied.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit fbee5cbadd85](https://github.com/erik-hedstrom/loadout/tree/fbee5cbadd85d2ae80ab467a258db1561295021c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
