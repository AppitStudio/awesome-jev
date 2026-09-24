# undertone

[All projects](../README.md) · [Web apps](README.md#web-apps)

A text box that reads how your draft sounds before you send: TypeSafe Jev scores tone, flags, urgency, formality, and boss-safety as you type.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Nuu-maan/undertone) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [undertone-app.vercel.app](https://undertone-app.vercel.app) — also source-buildable. |
| Pricing and access | Public source has **no LICENSE file** at tip—not Open source. Hosted demo and local build need `TYPESAFE_API_KEY` for live readings. No app purchase fee observed **2026-09-24**; TypeSafe usage separate. |
| Jev evidence | Inspected [`src/lib/jev/client.ts`](https://github.com/Nuu-maan/undertone/blob/456f4731656688800238ebc47dffd4a84c1ceb52/src/lib/jev/client.ts): `@typesafe-ai/sdk` `systemOne` with default model `jev-latest` over draft text (`questions.ts`). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Implementation inspected from public source; no LICENSE. Live typing session not run. |
| Maintainer | [Nuu-maan](https://github.com/Nuu-maan). Independently curated. |
| Format | Next.js / Bun web app. |
| Platform and availability | Hosted Vercel app or `bun` source build. |
| Jev's role | Server-side tone reading; UI maps probabilities to colors/copy. Requires key for live path (`hasJevKey`). |
| Requirements | Bun/Node; `TYPESAFE_API_KEY`; optional `JEV_MODEL`. |
| License | **No LICENSE** in the reviewed tree. Treat as source-available, not Open source. |

## When to use

Use it when you want a **calibrated pre-send tone check** on a short draft. Prefer a desktop paste tool when you need offline or OS-wide hooks.

## How it works

Draft text is sent server-side to TypeSafe System One. Answers cover tone Choice probabilities plus Noul flags (passive-aggressive, sarcastic, apologetic, pushy), urgency/formality scores, and boss-safe Noul. The UI renders the reading; sending remains your action outside the app.

## Get started

```sh
git clone https://github.com/Nuu-maan/undertone.git
cd undertone
git checkout 456f4731656688800238ebc47dffd4a84c1ceb52
bun install
# TYPESAFE_API_KEY=... 
bun dev
```

Or open the [hosted demo](https://undertone-app.vercel.app) if the operator has configured a key.

## Examples and demos

- Hosted app URL above.
- Source under `src/lib/jev/` and `src/lib/tone/`.

## Limits and data handling

Draft text leaves the host on live Jev calls (3s timeout, no retries in client). Missing key disables live readings. No OSS license file.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 456f473](https://github.com/Nuu-maan/undertone/tree/456f4731656688800238ebc47dffd4a84c1ceb52). AI-assisted inspection of README and `src/lib/jev/*`. No live TypeSafe spend.

Related: [Regret Check](regret-check.md), [Smart Paste](smart-paste.md).
