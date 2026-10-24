# jev-sdk by ogarciarevett (typed Jev verdicts for agents, with secrets masked before sending)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript library, CLI and MCP server for asking Jev typed questions about repository or agent state: it masks secrets locally before sending, applies a confidence bar per question by its stakes, retries rate limits and returns 'undecided' instead of guessing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ogarciarevett/jev-sdk) |
| Maintainer | [ogarciarevett](https://github.com/ogarciarevett). Independently curated. |
| Format | npm package with CLI and MCP server (TypeScript) |
| Requirements | Node.js or Bun; a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/ogarciarevett/jev-sdk/blob/c53b8562f10e8e64315bfb926c2e3ec7af2713a1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/judge.ts`](https://github.com/ogarciarevett/jev-sdk/blob/c53b8562f10e8e64315bfb926c2e3ec7af2713a1/src/judge.ts) at the pinned commit. |

## When to use

- Give coding agents a yes/no, choice or score verdict before risky steps, with a stop when unsure.
- Reuse ready question packs such as agent-operations.
- Mismatch: verdicts are advisory; the README says they never authorize an action by themselves.

## How it works

`src/judge.ts` posts to `https://api.typesafe.ai/v1/systemone` with `jev-latest` (and `jev-1.14.0` for box questions) after masking secrets in the state; answers below the stakes bar become `undecided`. Integration evidence: [`src/judge.ts`](https://github.com/ogarciarevett/jev-sdk/blob/c53b8562f10e8e64315bfb926c2e3ec7af2713a1/src/judge.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm i @ogarciarevett/jev-sdk
export TYPESAFE_API_KEY=...
npx --no-install jev-judge --state - --questions questions/agent-operations.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- npm: [www.npmjs.com/package/@ogarciarevett/jev-sdk](https://www.npmjs.com/package/@ogarciarevett/jev-sdk)
- README: [github.com/ogarciarevett/jev-sdk#readme](https://github.com/ogarciarevett/jev-sdk#readme)

## Limits and data handling

Masked state is sent to TypeSafe. Masking is pattern-based; review what your state contains.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit c53b8562f10e](https://github.com/ogarciarevett/jev-sdk/tree/c53b8562f10e8e64315bfb926c2e3ec7af2713a1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
