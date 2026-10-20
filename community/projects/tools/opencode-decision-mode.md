# opencode-decision-mode (decision tools for OpenCode)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

OpenCode plugin that gives the coding agent `decision`, `decision_map` and `decision_results` tools, so judgement calls on one item or on every record of a CSV or JSONL file go to Jev (through OpenRouter or TypeSafe directly) instead of being read through the controller model's context.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Hacklone/opencode-decision-mode) |
| Maintainer | [Hacklone](https://github.com/Hacklone). Independently curated. |
| Format | OpenCode plugin (TypeScript, npm `@coool/opencode-decision-mode`) |
| Requirements | OpenCode; an OpenRouter or TypeSafe key (`OPENROUTER_API_KEY` or `TYPESAFE_API_KEY`), or an OpenAI key for the `gpt-6-luna` backend. |
| License | [MIT](https://github.com/Hacklone/opencode-decision-mode/blob/ee07a1e0d5f1eea0a39ec6d578b5b4c4a0985683/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/Hacklone/status/2112469253597085855)). |
| Jev evidence | [`src/adapters/backends/typesafe-backend.ts`](https://github.com/Hacklone/opencode-decision-mode/blob/ee07a1e0d5f1eea0a39ec6d578b5b4c4a0985683/src/adapters/backends/typesafe-backend.ts) at the pinned commit. |

## When to use

- Triage a ticket dump or check every row of a CSV against a few rules without paging the data through the agent's context.
- Turn Jev probabilities into PASS, REVIEW or FAIL labels with your own thresholds and export the results to a file.
- Mismatch: OpenCode only; the controller model still decides what to ask.

## How it works

The controller model calls the tools from OpenCode's Code Mode. Each record becomes one request with your state and noul, choice or score questions; `src/adapters/backends/typesafe-backend.ts` uses the TypeSafe SDK against `/v1/systemone`, and the OpenRouter backend defaults to `typesafe/jev-1.14`. A threshold policy maps probabilities to verdicts, results stay in a server-side store with a content-hashed cache, and runs stop after six failures with the same signature. `/decision` toggles the tools; when off they are removed from model requests. Integration evidence: [`src/adapters/backends/typesafe-backend.ts`](https://github.com/Hacklone/opencode-decision-mode/blob/ee07a1e0d5f1eea0a39ec6d578b5b4c4a0985683/src/adapters/backends/typesafe-backend.ts).

## Get started

From the upstream README (not run on the review host):

```sh
opencode plugin add @coool/opencode-decision-mode
export OPENROUTER_API_KEY=...   # or TYPESAFE_API_KEY / OPENAI_API_KEY
# in the OpenCode TUI:
/decision
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author's X post: [x.com/Hacklone/status/2112469253597085855](https://x.com/Hacklone/status/2112469253597085855)
- README examples (ticket dump triage, decision answer shape)

## Limits and data handling

Records and questions go to OpenRouter, TypeSafe or OpenAI, depending on the backend. The 130-record cost figure is the author's; not rerun here.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit ee07a1e0d5f1](https://github.com/Hacklone/opencode-decision-mode/tree/ee07a1e0d5f1eea0a39ec6d578b5b4c4a0985683). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
