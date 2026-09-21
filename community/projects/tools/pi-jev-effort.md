# pi-jev-effort

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that sets each prompt's thinking level from a TypeSafe Jev score of prompt difficulty, then caps that level by remaining quota/burn pressure. Distinct from [pi-jev-router](pi-jev-router.md) (model/role routing) and [pi-jev](pi-jev.md) (tool gate / output judge).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/namenu/pi-jev-effort) |
| Maintainer | [namenu](https://github.com/namenu). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension **pi-jev-effort 0.1.0** (`index.ts` / `usage.ts`; zero npm runtime deps; `pi install npm:pi-jev-effort`). |
| Requirements | Pi coding agent with extension API `setThinkingLevel`. Live TypeSafe path: `TYPESAFE_API_KEY` or `~/.jev/config.json`. OpenRouter Decisions path can reuse Pi's OpenRouter auth (allow TypeSafe under Guardrails). |
| License | [MIT](https://github.com/namenu/pi-jev-effort/blob/2e1d6f192c0bd878c70ff6ecf423340ec2a0b538/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline `node --test` inspected. Live Pi sessions and live TypeSafe/OpenRouter calls were not run. |

## When to use

Use it when you want Pi's reasoning effort to track prompt hardness without manually toggling levels, while protecting remaining budget. Prefer [pi-jev-router](pi-jev-router.md) when the decision is which *model* to call; prefer fixed low effort when every turn is cheap and local.

## How it works

[`index.ts`](https://github.com/namenu/pi-jev-effort/blob/2e1d6f192c0bd878c70ff6ecf423340ec2a0b538/index.ts) posts a Score question to TypeSafe `https://api.typesafe.ai/v1/systemone` (or OpenRouter Decisions with `~typesafe/jev-latest`), maps the expected score onto thinking levels with hysteresis, then applies a ceiling from local usage/burn windows before calling `pi.setThinkingLevel`. Missing keys or malformed answers leave the current level unchanged.

## Get started

```sh
git clone https://github.com/namenu/pi-jev-effort.git
cd pi-jev-effort
git checkout 2e1d6f192c0bd878c70ff6ecf423340ec2a0b538
node --test
# Install into Pi: pi install npm:pi-jev-effort
# or symlink the checkout under ~/.pi/agent/extensions/
# Live judgments need a TypeSafe or OpenRouter path and incur charges.
```

## Examples and demos

- Upstream README tables of scored prompts and quota-ceiling examples.
- Review host: **`node --test`**: **12 passed** (including `usage.test.ts`).

## Limits and data handling

Prompt text (as scored) leaves the host toward TypeSafe or OpenRouter when judging. Quota ceilings depend on local usage accounting, not a guarantee from your provider plan. Thinking-level quality was not measured on the review host.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 2e1d6f1](https://github.com/namenu/pi-jev-effort/tree/2e1d6f192c0bd878c70ff6ecf423340ec2a0b538): **0.1.0**, MIT. AI-assisted source review of README, `index.ts`, `usage.ts`, and LICENSE. Offline tests: **12 passed**. No live TypeSafe/OpenRouter or Pi install.

Related: [pi-jev](pi-jev.md), [pi-jev-router](pi-jev-router.md), [Jev Model Router](jev-model-router.md).
