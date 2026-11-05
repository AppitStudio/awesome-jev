# Jev Gate Lite (cloud-only edition of Jev Gate for Claude Code and Codex: hybrid compaction, tool-output pruning and advisory MCP judgment tools)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Slimmed-down Jev Gate that uses only cloud Jev (no local Laya model). Hybrid compaction starts at 60% of context or 200K tokens, has Jev decide per tool call whether to drop it and keeps remaining text verbatim, handing back to built-in compaction if less than 30% is saved; long tool output is pruned to relevant passages; an MCP server offers `jev_evaluate` and `jev_apply_policy` as advisory tools.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/royalskynet/jev-gate-lite) |
| Maintainer | [royalskynet](https://github.com/royalskynet). Independently curated. |
| Format | Node.js plugin for Claude Code and Codex with an MCP server |
| Requirements | Node.js 22 or 24 and a Jev key (OpenCode Zen free tier or OpenRouter, per the README). |
| License | [MIT](https://github.com/royalskynet/jev-gate-lite/blob/8ca776b7c325469a16c62a00a4c2f8807ef0af7f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`agent-glue/vendor/fast-jev/client.js`](https://github.com/royalskynet/jev-gate-lite/blob/8ca776b7c325469a16c62a00a4c2f8807ef0af7f/agent-glue/vendor/fast-jev/client.js) at the pinned commit. |

## When to use

- Cut agent context without a local model, keeping kept messages word for word.
- Add advisory classification and review tools to a coding agent.
- Mismatch: lite edition of the already listed Jev Gate; the subagent-tier hook is a placeholder that does not change models yet.

## How it works

Vendored fast-jev code builds typed Jev requests (`client.js`, `request.js`) for per-call keep/drop decisions; hooks in `agent-glue/claude` and `.codex` wire it into compaction and tool-output pruning. Integration evidence: [`agent-glue/vendor/fast-jev/client.js`](https://github.com/royalskynet/jev-gate-lite/blob/8ca776b7c325469a16c62a00a4c2f8807ef0af7f/agent-glue/vendor/fast-jev/client.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/royalskynet/jev-gate-lite.git
cd jev-gate-lite
npm install && npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- English README: [github.com/royalskynet/jev-gate-lite/blob/8ca776b7c325469a16c62a00a4c2f8807ef0af7f/README.en.md](https://github.com/royalskynet/jev-gate-lite/blob/8ca776b7c325469a16c62a00a4c2f8807ef0af7f/README.en.md)

## Limits and data handling

Tool output and context are sent to the Jev provider you configure (the README names the OpenCode Zen free tier and OpenRouter); savings figures are the author's. Install and live calls were not run.

## Review and maintenance

Reviewed **2026-11-05** (Europe/Sofia) at [commit 8ca776b7c325](https://github.com/royalskynet/jev-gate-lite/tree/8ca776b7c325469a16c62a00a4c2f8807ef0af7f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
