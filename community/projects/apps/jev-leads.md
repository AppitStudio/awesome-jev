# jev-leads

[All projects](../README.md) · [Web apps](README.md#web-apps)

Multi-channel inbound lead intake (web/WhatsApp/Telegram/webhooks) buffered in SQLite WAL, qualified by OpenRouter typesafe/jev-1.13 structured decisions, then synced to Airtable with hot-reloadable per-channel configs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SebassContreras/jev-leads) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/SebassContreras/jev-leads#readme) |
| Pricing and access | Free source build; BYOK OpenRouter + Airtable. Checked 2026-10-04. |
| Jev evidence | [Upstream README](https://github.com/SebassContreras/jev-leads/blob/e0ff928087179063af77ec3c3d8cd01d95f6d005/README.md) documents OpenRouter Jev structured decisions and the SQLite→Airtable pipeline. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Distinct from [Airtale](https://github.com/SebassContreras/airtale) by the same author—this listing is the OpenRouter Decisions + SQLite zero-loss buffer + Airtable sync service. Live install/UI paths not run on the Linux review host. |
| Maintainer | [SebassContreras](https://github.com/SebassContreras). Independently curated. |
| Format | Hono TypeScript lead qualification service + Airtable sync (MIT) |
| Platform and availability | Self-hosted Node/Hono HTTP service |
| Jev's role | Jev (typesafe/jev-1.13 via OpenRouter Decisions) assigns category, 0–100 score, and reasoning; application code owns buffering, config routing, and Airtable writes. |
| Requirements | Node.js 24 LTS; OpenRouter key; Airtable token; per-channel configs under configs/ |
| License | [MIT](https://github.com/SebassContreras/jev-leads/blob/e0ff928087179063af77ec3c3d8cd01d95f6d005/LICENSE). Provider usage may incur charges when live. |

## When to use

Use when you need durable inbound lead buffering with Jev qualification into Airtable. Prefer Airtale when you want that author's alternate lead pipeline packaging.

## How it works

Multi-channel inbound lead intake (web/WhatsApp/Telegram/webhooks) buffered in SQLite WAL, qualified by OpenRouter typesafe/jev-1.13 structured decisions, then synced to Airtable with hot-reloadable per-channel configs. Jev supplies typed judgments where configured; application code owns orchestration and side effects.

## Get started

```sh
git clone https://github.com/SebassContreras/jev-leads.git
cd jev-leads
git checkout e0ff928087179063af77ec3c3d8cd01d95f6d005
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/screenshots.

## Limits and data handling

Live Jev may send task text to TypeSafe and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-04** (Europe/Sofia) at [commit e0ff92808717](https://github.com/SebassContreras/jev-leads/tree/e0ff928087179063af77ec3c3d8cd01d95f6d005). AI-assisted README and license inspection; live paths not executed.
