# Crush Monitor with Jev

[All projects](../README.md) · [Web apps](README.md#web-apps)

WeChat chat affinity analyzer forked from Crush Monitor: import transcripts, pick a relationship mode, and let TypeSafe Jev label emotion/intent and score affinity inside a chat-style UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zhengge6/crush-monitor-with-jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Project homepage](https://github.com/zhengge6/crush-monitor-with-jev#readme) — local/web UI; see upstream for any hosted trial. |
| Pricing and access | MIT source build; configure provider key via setup. Trial/account extras may exist upstream—verify before relying on free hosted use. Checked **2026-09-24**. TypeSafe usage separate. |
| Jev evidence | Inspected [`server/provider.ts`](https://github.com/zhengge6/crush-monitor-with-jev/blob/3f46f9263e2a71b71c52cd4e37937e29766aca73/server/provider.ts) (`@typesafe-ai/sdk` System One validation) and [`shared/affinity.ts`](https://github.com/zhengge6/crush-monitor-with-jev/blob/3f46f9263e2a71b71c52cd4e37937e29766aca73/shared/affinity.ts) score dimensions. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live chat analysis not run. Derivative of FerryCorleone/crush-monitor (MIT). |
| Maintainer | [zhengge6](https://github.com/zhengge6). Independently curated. |
| Format | Node.js/TypeScript web app (`server/` + `src/`). |
| Platform and availability | Local Node ≥ 22.12; optional deploy scripts under `deploy/`. |
| Jev's role | Structured emotion/intent/affinity judgments; application owns UI, memory, and ratings. |
| Requirements | Node.js 22.12+; TypeSafe (or compatible) API key. |
| License | [MIT](https://github.com/zhengge6/crush-monitor-with-jev/blob/3f46f9263e2a71b71c52cd4e37937e29766aca73/LICENSE) (see NOTICE for upstream attribution). |

## When to use

Use it for **relationship-signal analysis on imported WeChat-style logs** with a productized UI. Prefer upstream [Crush Monitor](crush-monitor.md) for the original localhost analyzer.

## How it works

Imported chat text is scored through affinity dimensions and provider calls validated against System One answer schemas. The UI presents labels and follow-up chat; it is a reference aid, not ground truth about offline relationships.

## Get started

```sh
git clone https://github.com/zhengge6/crush-monitor-with-jev.git
cd crush-monitor-with-jev
git checkout 3f46f9263e2a71b71c52cd4e37937e29766aca73
npm install
npm run setup   # provider key
npm run dev     # follow README scripts
```

## Examples and demos

- README screenshots under `docs/assets/`.
- English notes in `README.en.md`.

## Limits and data handling

Chat contents leave your machine for the configured Jev provider. Trial/account features may store more—read upstream privacy notes. Model judgments ignore offline context.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 3f46f92](https://github.com/zhengge6/crush-monitor-with-jev/tree/3f46f9263e2a71b71c52cd4e37937e29766aca73). AI-assisted README + provider/affinity inspection. No live TypeSafe spend.

Related: [Crush Monitor](crush-monitor.md), [tg-crush](tg-crush.md), [SignalLens](signal-lens.md).
