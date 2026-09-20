# Eutrya

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Standalone terminal agent with TypeSafe Jev in the decision loop: attention modes, candidate rubrics, single-use decision tickets, research lane, and an optional experimental desktop UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hellozenstrategist-lab/eutrya) |
| Maintainer | [hellozenstrategist-lab](https://github.com/hellozenstrategist-lab). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Node.js CLI **eutrya 0.4.9** (public alpha); optional Linux-first Tauri desktop. |
| Requirements | Node.js 22+; Git. Live sessions need `AI_GATEWAY_API_KEY` (Vercel AI Gateway) for Jev evaluation plus a configured text model. Offline `eutrya demo` needs no credentials. |
| License | [MIT](https://github.com/hellozenstrategist-lab/eutrya/blob/4d5ca7c09573ca2d3a0d238b8f673593d528a57a/LICENSE). |
| Disclosure | Public alpha; upstream states it has not undergone an independent security audit. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live Gateway/agent sessions were not run. |

## When to use

Use it when you want a CLI-owned agent loop where Jev selects attention and scores candidate next steps while a text model proposes options. Prefer [jev-guard](jev-guard.md) or [toolgate](toolgate.md) when you only need to gate an existing coding agent's tools. Prefer [Foreman](foreman.md) for Codex worker supervision.

## How it works

[`src/providers/jev.mjs`](https://github.com/hellozenstrategist-lab/eutrya/blob/4d5ca7c09573ca2d3a0d238b8f673593d528a57a/src/providers/jev.mjs) drives typed Choice/Score/Noul questions through the Vercel AI SDK `experimental_evaluate` path (Gateway). Jev picks an attention mode, evaluates each proposed candidate against independent rubrics, then deterministic policy issues a single-use decision ticket and tool permission. Research mode keeps the strategist text model at boundary cadence while Jev chooses local read-only code operations. Application code owns planning state, permissions, and execution.

## Get started

```sh
git clone https://github.com/hellozenstrategist-lab/eutrya.git
cd eutrya
git checkout 4d5ca7c09573ca2d3a0d238b8f673593d528a57a
npm ci
npm link
eutrya demo          # no credentials
# Live:
# export AI_GATEWAY_API_KEY='…'
# eutrya setup && eutrya
```

Live sessions send task state and candidate text to the Gateway and can incur charges. Read upstream `SECURITY.md` before confidential workspaces. This listing did not run the demo or live agent.

## Examples and demos

- `eutrya demo` offline path and README research/hunt surfaces.
- Extensive `tests/*.test.mjs` suite — not executed on the review host.

## Limits and data handling

Alpha release: CLI is the primary surface; desktop is experimental. Task state, observations, and candidate descriptions leave the host for Jev via the Gateway; text-model prompts are separate. Upstream security-audit disclaimer applies. Cost/latency claims were not independently measured.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 4d5ca7c](https://github.com/hellozenstrategist-lab/eutrya/tree/4d5ca7c09573ca2d3a0d238b8f673593d528a57a): **0.4.9**, MIT. AI-assisted source review of README, LICENSE, `src/providers/jev.mjs`, and package metadata. No live Gateway or agent runs.

Related: [jev-guard](jev-guard.md), [toolgate](toolgate.md), [Foreman](foreman.md).
