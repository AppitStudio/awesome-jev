# Pi Adaptive Effort Router (XDeviation)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension that changes **thinking level only** (never the selected model) using TypeSafe Jev classification—distinct from [philippdubach/pi-jev-router](pi-jev-router.md) (OpenRouter model routing) and from [pi-jev-effort](pi-jev-effort.md).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/XDeviation/pi-jev-router) |
| Maintainer | [XDeviation](https://github.com/XDeviation). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript Pi extension **pi-jev-router 0.2.0** (`index.ts` / effort commands). |
| Requirements | Pi coding agent; TypeSafe API key via `/effort login`, `TYPESAFE_API_KEY` / `JEV_API_KEY`, or private secrets file. Classification **off by default**. |
| License | [MIT](https://github.com/XDeviation/pi-jev-router/blob/178687f7db9582fe8f52f542dc76ba8fdfbb0857/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `src/classifier/jev.ts`). Live Pi/Jev were **not** run on the review host. |

## When to use

Use it when you want Pi to raise/hold thinking effort from Jev without swapping models. Prefer [pi-jev-router](pi-jev-router.md) (philippdubach) for OpenRouter model/role routing; prefer [pi-jev-effort](pi-jev-effort.md) for quota-capped difficulty scoring.

## How it works

When enabled, classification calls fixed `https://api.typesafe.ai/v1/systemone` with a work-order description and flags—not images, files, tool output, or full history ([`src/classifier/jev.ts`](https://github.com/XDeviation/pi-jev-router/blob/178687f7db9582fe8f52f542dc76ba8fdfbb0857/src/classifier/jev.ts)). Local policy applies hysteresis and operator `/thinking` floors. Shadow mode computes decisions without changing Pi’s level.

## Get started

```sh
pi install git:github.com/XDeviation/pi-jev-router
# In Pi: /effort login   # masked TUI prompt; or set TYPESAFE_API_KEY
# /effort status | shadow on | jev on
```

Pin for review: [commit 178687f](https://github.com/XDeviation/pi-jev-router/tree/178687f7db9582fe8f52f542dc76ba8fdfbb0857). Live classification sends bounded task text to TypeSafe and may incur charges.

## Examples and demos

- `examples/adaptive-effort.json`.
- `npm test` / `npm run typecheck` upstream (not re-run here). Optional `PI_JEV_LIVE_TEST=1` live test documented upstream.

## Limits and data handling

Login does not validate the key until first classification. Credential-pattern guard is best-effort. Telemetry is off by default. Default effort without Jev is `high`. No live TypeSafe spend in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 178687f](https://github.com/XDeviation/pi-jev-router/tree/178687f7db9582fe8f52f542dc76ba8fdfbb0857) (**0.2.0**, MIT). AI-assisted source review. Distinct-owner listing vs philippdubach `pi-jev-router`.

Related: [pi-jev-router](pi-jev-router.md), [pi-jev-effort](pi-jev-effort.md), [jev-effort-router](jev-effort-router.md).
