# TypeSafe Classifier Dashboard by lecharles (local Next.js app that classifies support e-mails, video titles or any text with Jev and charts the answers)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Local-first Next.js app with three dashboards, a playground, e-mail triage (category, urgency, priority) and a YouTube analyzer (topic, clickbait, sentiment), that sends typed Choice, Score and Noul questions to Jev and charts the answers with donuts, histograms and gauges.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lecharles/typesafe-classifier-dashboard) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/lecharles/typesafe-classifier-dashboard#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-26. |
| Jev evidence | [`lib/jev.ts`](https://github.com/lecharles/typesafe-classifier-dashboard/blob/249ef8e1fc41d056255535b182982033d2112f7c/lib/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [lecharles](https://github.com/lecharles). Independently curated. |
| Format | Next.js app (TypeScript) |
| Platform and availability | Web app run locally (Next.js, React, Recharts). |
| Jev's role | Jev answers all of a dashboard's typed questions in one `/v1/systemone` request per item; the app charts the probabilities. |
| Requirements | Node.js; a TypeSafe API key, or a Vercel AI Gateway key routed to TypeSafe. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Explore what Jev's typed answers look like on your own e-mails or titles, as charts.
- Mismatch: if you need a hosted product; this is a local demo.

## How it works

`lib/jev.ts` calls `POST {base}/v1/systemone` on `https://api.typesafe.ai` or on Vercel AI Gateway's TypeSafe surface, with retries on 429/529/5xx. Without a Jev route the app falls back to emulating the primitives with a chat model (Claude 3 Haiku, Nova Micro) through the gateway; each result records which provider answered. Integration evidence: [`lib/jev.ts`](https://github.com/lecharles/typesafe-classifier-dashboard/blob/249ef8e1fc41d056255535b182982033d2112f7c/lib/jev.ts).

## Get started

Install, add a TypeSafe or Vercel AI Gateway key, and start the dev server.

```sh
git clone https://github.com/lecharles/typesafe-classifier-dashboard
cd typesafe-classifier-dashboard
npm install
export TYPESAFE_API_KEY=...
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository: [github.com/lecharles/typesafe-classifier-dashboard/tree/249ef8e1fc41d056255535b182982033d2112f7c/screenshots](https://github.com/lecharles/typesafe-classifier-dashboard/tree/249ef8e1fc41d056255535b182982033d2112f7c/screenshots)

## Limits and data handling

No license file on the reviewed commit, so no reuse terms are granted. Without a Jev route it silently uses non-TypeSafe chat models to emulate the answers; check each result's `provider` field. The Vercel route is a third-party host. Text you classify is sent to the chosen provider.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit 249ef8e1fc41](https://github.com/lecharles/typesafe-classifier-dashboard/tree/249ef8e1fc41d056255535b182982033d2112f7c). Inspected the README and the Jev client at the pinned commit; the app was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
