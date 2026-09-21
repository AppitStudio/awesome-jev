# Jev Checkpoint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local MCP server that turns a bounded next-step decision into one TypeSafe Jev Choice question and returns an advisory, confidence-gated route. It never executes the selected action.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ashishakkumar/Jev-Checkpoint) |
| Maintainer | [ashishakkumar](https://github.com/ashishakkumar). Independently curated; this page is not an upstream submission or endorsement. |
| Format | TypeScript · local MCP server (`jev-checkpoint` 0.1.0). |
| Requirements | Node.js with `npm`; `TYPESAFE_API_KEY` (optional `TYPESAFE_API_URL`, default `https://api.typesafe.ai/v1/systemone`). |
| License | [MIT](https://github.com/ashishakkumar/Jev-Checkpoint/blob/e655e30ce58f73f9aa85ed0f61dba57120d633cf/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `tsx` tests **2 passed**; live TypeSafe smoke not run. |

## When to use

Use it when an agent already has compact evidence and must choose among a small fixed set of next steps (proceed / inspect / ask the user, and similar). Prefer fuller planners or [JevRouter](jevrouter.md) when the action set is open-ended or needs permission receipts. It is advisory only—not an approval or execution gate.

## How it works

[`src/decision.ts`](https://github.com/ashishakkumar/Jev-Checkpoint/blob/e655e30ce58f73f9aa85ed0f61dba57120d633cf/src/decision.ts) builds a single Choice question over caller-supplied route ids. [`src/index.ts`](https://github.com/ashishakkumar/Jev-Checkpoint/blob/e655e30ce58f73f9aa85ed0f61dba57120d633cf/src/index.ts) exposes MCP tool `classify_decision`, posts to TypeSafe `/v1/systemone`, and applies a confidence threshold before recommending a route. Evidence and choice text leave the host when a key is set.

## Get started

```sh
git clone https://github.com/ashishakkumar/Jev-Checkpoint.git
cd Jev-Checkpoint
git checkout e655e30ce58f73f9aa85ed0f61dba57120d633cf
npm install
npm run build
npm test
```

Point Claude Code (or another MCP host) at `dist/index.js` with `TYPESAFE_API_KEY` in the server env. Live calls are billed by TypeSafe.

## Examples and demos

- Upstream `examples/claude-code-settings.json` MCP snippet.
- This listing: `npm test` → **2 passed**. No live TypeSafe call.

## Limits and data handling

Decision text, evidence, and choice descriptions are sent to TypeSafe when configured. Missing keys fail the tool call. Latency/cost marketing was not measured here.

## Review and maintenance

Reviewed on **2026-09-21** at [commit e655e30](https://github.com/ashishakkumar/Jev-Checkpoint/tree/e655e30ce58f73f9aa85ed0f61dba57120d633cf): MIT; AI-assisted source review of README, LICENSE, `src/`, build, and offline tests. No live TypeSafe call.

Related: [askjev](askjev.md), [JevRouter](jevrouter.md), [decision-first](decision-first.md).
