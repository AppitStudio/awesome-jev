# Jev Gatehouse (Kinde)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Kinde starter: identity + permissions, then TypeSafe Jev typed gate before every MCP tool call — allow, step-up approve, or stop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kinde-starter-kits/jev-agent-authorization) |
| Maintainer | [kinde-starter-kits](https://github.com/kinde-starter-kits). Independently curated. Not an endorsement of Kinde or TypeSafe. |
| Format | TypeScript / Convex starter kit (`jev-agent-authorization`). |
| Requirements | Node; Kinde + TypeSafe/OpenRouter credentials per README; Convex backend. |
| License | [MIT](https://github.com/kinde-starter-kits/jev-agent-authorization/blob/e6d10a5b20966ca398adf9124baa4db056fffb2b/LICENSE). Kinde and provider usage may incur charges. |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE, `convex/guard/judgment.ts`). Live Kinde/MCP/Jev **not** run. |

## When to use

Use it to study server-side agent authorization where Kinde answers who/what and Jev judges each tool call before execution. Prefer thinner guards when you do not need IdP integration.

## How it works

[`judgeWithJev`](https://github.com/kinde-starter-kits/jev-agent-authorization/blob/e6d10a5b20966ca398adf9124baa4db056fffb2b/convex/guard/judgment.ts) runs Jev signals through policy (`decideWithSignals`); optional LLM judge cascade; ledger UI shows gate outcomes.

## Get started

```sh
git clone https://github.com/kinde-starter-kits/jev-agent-authorization.git
cd jev-agent-authorization
git checkout e6d10a5b20966ca398adf9124baa4db056fffb2b
# follow upstream README for Kinde + Convex + keys
```

## Examples and demos

- README hero ledger screenshot and architecture flowchart.
- Guard unit tests under `convex/guard/*.test.ts` (not executed here).

## Limits and data handling

Tool-call metadata and reasons go to TypeSafe/Jev (and optional judge model) when live. Starter-kit quality—not a turnkey production IdP. Unavailable Jev steps up per policy.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit e6d10a5](https://github.com/kinde-starter-kits/jev-agent-authorization/tree/e6d10a5b20966ca398adf9124baa4db056fffb2b) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [agent-chaperone](agent-chaperone.md), [jev-guard](jev-guard.md), [DecideKit](decidekit.md).
