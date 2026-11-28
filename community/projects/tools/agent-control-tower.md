# Agent Control Tower by royharden (demo where Jev scores each tool call an LLM planner proposes and code allows, queues or blocks it)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Full-stack demo of a System 2 / System 1 split: an LLM agent plans tool calls, Jev checks every proposed call, and policy code with confidence thresholds allows it, queues it for human approval or blocks it, on simulated tools. A mock planner keeps Jev live without an OpenAI key, and a local file-backed mode runs without Supabase.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/royharden/agent-control-tower) |
| Maintainer | [royharden](https://github.com/royharden). Independently curated. |
| Format | React + Vite web app with Supabase Edge Functions |
| Requirements | Node.js; a Supabase project, a TypeSafe key and optionally an OpenAI key for the live path. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`supabase/functions/jev-check/index.ts`](https://github.com/royharden/agent-control-tower/blob/0fcb3c822c03100b1104dc823d330af6434b22cb/supabase/functions/jev-check/index.ts) at the pinned commit. |

## When to use

- Teams prototyping a human-in-the-loop gate for agent tool calls.
- Mismatch: production enforcement; the tools are simulated.

## How it works

`supabase/functions/jev-check/index.ts` sends each proposed call's details to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) with server-side keys and a daily usage cap; the frontend applies the allow/approve/block thresholds. Integration evidence: [`supabase/functions/jev-check/index.ts`](https://github.com/royharden/agent-control-tower/blob/0fcb3c822c03100b1104dc823d330af6434b22cb/supabase/functions/jev-check/index.ts).

## Get started

Try the local demo without Supabase.

```sh
git clone https://github.com/royharden/agent-control-tower && cd agent-control-tower && npm install
node scripts/local-run-log.mjs serve --port 8787
ACT_RUNLOG_ORIGIN=http://127.0.0.1:8787 VITE_LOCAL_DEMO=1 npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Local demo steps: [github.com/royharden/agent-control-tower#local-demo-without-supabase](https://github.com/royharden/agent-control-tower#local-demo-without-supabase)

## Limits and data handling

Proposed tool calls go to TypeSafe (and plans to OpenAI when configured). No licence file, so no reuse rights are granted. One of 15 Jev demos by the same author published together; others are tracked for later runs.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit 0fcb3c822c03](https://github.com/royharden/agent-control-tower/tree/0fcb3c822c03100b1104dc823d330af6434b22cb). Inspected the README and the `jev-check` Edge Function at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
