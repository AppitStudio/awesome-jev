# Muffin (owner-run personal agent with a TypeSafe Jev shadow-judgment layer)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Human-first personal agent that keeps memory, work and authority across models; its judgment port uses TypeSafe Jev as a shadow layer for bounded decisions and never as approval.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/muffin-project/muffin-agent) |
| Maintainer | [muffin-project](https://github.com/muffin-project). Independently curated. |
| Format | TypeScript agent (AGPL-3.0) |
| Requirements | Node, the agent's model providers, and a TypeSafe key for Jev judgments. |
| License | [AGPL-3.0](https://github.com/muffin-project/muffin-agent/blob/a66e81fcfe9b72cdd546b0215e8281a29a6c8d50/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core/judgment/typesafe.ts`](https://github.com/muffin-project/muffin-agent/blob/a66e81fcfe9b72cdd546b0215e8281a29a6c8d50/core/judgment/typesafe.ts) at the pinned commit. |

## When to use

- Add calibrated shadow judgments to a personal agent.
- Compare Jev verdicts with code-owned facts before trusting them.
- Mismatch: Jev never approves actions here.

## How it works

`core/judgment/typesafe.ts` implements the System One port with `TypeSafeClient`; the `jev-shadow` skill logs Jev verdicts on milestone relevance, triage and scope drift next to deterministic checks. Integration evidence: [`core/judgment/typesafe.ts`](https://github.com/muffin-project/muffin-agent/blob/a66e81fcfe9b72cdd546b0215e8281a29a6c8d50/core/judgment/typesafe.ts).

## Get started

Clone, install dependencies and follow the README setup; enable the TypeSafe judgment port with your key.

```sh
git clone https://github.com/muffin-project/muffin-agent.git && cd muffin-agent
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- jev-shadow skill: [github.com/muffin-project/muffin-agent/blob/a66e81fcfe9b72cdd546b0215e8281a29a6c8d50/.agents/skills/jev-shadow/SKILL.md](https://github.com/muffin-project/muffin-agent/blob/a66e81fcfe9b72cdd546b0215e8281a29a6c8d50/.agents/skills/jev-shadow/SKILL.md)

## Limits and data handling

Decision context is sent to TypeSafe when the judgment port is on.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit a66e81fcfe9b](https://github.com/muffin-project/muffin-agent/tree/a66e81fcfe9b72cdd546b0215e8281a29a6c8d50). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
