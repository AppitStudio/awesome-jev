# pi-shift-router

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that routes each turn to a cheap or strong model tier; optional TypeSafe Jev judge returns a calibrated probability instead of prose.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/green-dalii/pi-shift-router) |
| Maintainer | [green-dalii](https://github.com/green-dalii). Independently curated. |
| Format | npm Pi extension (`pi-shift-router`). |
| Requirements | Node.js ≥ 24; Pi coding agent; provider keys for routed models; optional TypeSafe/OpenRouter access when Jev judge is enabled. |
| License | [MIT](https://github.com/green-dalii/pi-shift-router/blob/31a02999bebf5d997a42a489f46be447f4f6a108/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Pi/Jev routing not run on the review host. |

## When to use

Use to **cut flagship spend on routine Pi turns** while upgrading hard turns, with optional Jev as the decision-model judge (beta/opt-in per README).

## How it works

A pluggable judge (LLM JSON classifier or decision-model such as Jev) picks a tier; failover chains handle 429/402/5xx. Task-level orchestration can delegate from a strong “CTO” to fast subagents when enabled.

## Get started

```sh
# From upstream README / npm:
# pi install npm:pi-shift-router
# Pin: https://github.com/green-dalii/pi-shift-router/tree/31a02999bebf5d997a42a489f46be447f4f6a108
npm view pi-shift-router version
```

## Examples and demos

- Project site: [shiftrouter.greenerai.top](https://shiftrouter.greenerai.top)
- README Jev judge section and config docs under `docs/`.

## Limits and data handling

Prompt/route features go to the configured judge and model providers. Jev judge is optional and marked beta upstream.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 31a0299](https://github.com/green-dalii/pi-shift-router/tree/31a02999bebf5d997a42a489f46be447f4f6a108). AI-assisted README and LICENSE inspection; live Pi install not run.
