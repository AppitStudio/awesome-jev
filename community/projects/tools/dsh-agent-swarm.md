# dsh-agent-swarm by zhairy (DeepSeek Harness multi-agent plugin with task-card gates and seven built-in Jev judgment tools)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Multi-agent plugin for DeepSeek Harness (Chinese and English docs): an orchestrator leads 12 specialist agents (requirements, architecture, code exploration, research, implementation, review, verification and more), and work is accepted through task cards, gates and real evidence, with tiered model routes that fall back on failure. Jev triages task cards into hard gates, rates the reliability of delegated deliverables, and is exposed to the agents as seven built-in tools (`jev_check`, `jev_classify`, `jev_score`, `jev_match`, `jev_screen`, `jev_ask`, `jev_health`) plus `jev-judgments` and `typesafe-ai` skills. Jev can use the official TypeSafe API or a third-party Jev-compatible model from the DSH catalog.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zhairy/dsh-agent-swarm) |
| Maintainer | [zhairy](https://github.com/zhairy). Independently curated. |
| Format | DeepSeek Harness plugin (TypeScript, MIT) |
| Requirements | DeepSeek Harness 0.2.2-rc.3 (host bridges and Node.js 24.9+ for some features) and a TypeSafe key in the DSH credential store, or a third-party Jev-compatible model. |
| License | [MIT](https://github.com/zhairy/dsh-agent-swarm/blob/178b6a40be43313d524f2f79fe947d6a638b04f8/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/zhairy/dsh-agent-swarm/blob/178b6a40be43313d524f2f79fe947d6a638b04f8/src/jev.ts) at the pinned commit. |

## When to use

- Run a gated multi-agent coding workflow in DeepSeek Harness with Jev checks at each gate.
- Mismatch: other harnesses; it targets specific DSH releases and fails closed without matching bridges.

## How it works

`src/jev.ts` sends the triage and judgment questions to `https://api.typesafe.ai` at `/v1/systemone` (official source by default; `src/config.ts` holds the settings schema), and redacts common secret formats before sending. Integration evidence: [`src/jev.ts`](https://github.com/zhairy/dsh-agent-swarm/blob/178b6a40be43313d524f2f79fe947d6a638b04f8/src/jev.ts).

## Get started

Install the plugin in DeepSeek Harness (see docs/安装.md), add your Jev key in settings, and start a session in the Agent Swarm preset.

```sh
git clone https://github.com/zhairy/dsh-agent-swarm
# install per docs/安装.md, then: Settings -> Agent Swarm -> Jev API key
# new session -> "百工模式" (Agent Swarm) preset
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/zhairy/dsh-agent-swarm/blob/178b6a40be43313d524f2f79fe947d6a638b04f8/README.md](https://github.com/zhairy/dsh-agent-swarm/blob/178b6a40be43313d524f2f79fe947d6a638b04f8/README.md)

## Limits and data handling

Task cards, deliverable summaries and tool inputs go to TypeSafe (or the chosen third-party model) on your key; secrets are redacted before sending. Docs are mostly in Chinese.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 178b6a40be43](https://github.com/zhairy/dsh-agent-swarm/tree/178b6a40be43313d524f2f79fe947d6a638b04f8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
