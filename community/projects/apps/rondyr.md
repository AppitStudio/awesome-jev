# Rondyr by Basaltbytes (self-hosted form backend on Cloudflare that screens messages for spam and sales pitches with Jev)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Point your website's form at Rondyr and every message is saved in your own Cloudflare account, checked by rate limits, honeypot, Turnstile and repeat detection, then classified for spam, unsolicited sales outreach and business relevance. Accepted messages go to email, signed webhooks, Discord, Slack or Airtable; the rest wait in a To review folder for your team.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/basaltbytes/rondyr) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Product homepage](https://rondyr.com) |
| Pricing and access | Free AGPL-3.0 source; you deploy it to your own Cloudflare account, which needs Workers Paid ($5/month per account, per the project's costs guide) plus any Workers AI, email and usage charges. No hosted Rondyr service was found. Checked 2026-11-23. |
| Jev evidence | [`apps/rondyr/src/adapters/ai/jev.ts`](https://github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/apps/rondyr/src/adapters/ai/jev.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [basaltbytes](https://github.com/basaltbytes). Independently curated. |
| Format | Cloudflare Workers web app (TypeScript) |
| Platform and availability | Web app on Cloudflare Workers (one-click Deploy to Cloudflare); pre-alpha. |
| Jev's role | Jev (by default) answers Noul and Choice questions about each message for spam, solicitation and, when you give business context, relevance; thresholds in code route it to Accepted or To review. OpenAI Decisions is an alternative, with optional second-model escalation for uncertain messages. |
| Requirements | A Cloudflare account on Workers Paid and a GitHub or GitLab account; no separate Jev key (Jev runs through Cloudflare Workers AI). |
| License | [AGPL-3.0](https://github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/LICENSE) |

## When to use

- Run your own contact-form backend that keeps sales pitches and spam out of your inbox without a third-party form service.
- Mismatch: production use today; the author marks it pre-alpha and the data model and API can change.

## How it works

`apps/rondyr/src/adapters/ai/jev.ts` calls the Workers AI binding with model `typesafe/jev` through AI Gateway options, sending the message as state with spam, solicitation and relevance questions. Integration evidence: [`apps/rondyr/src/adapters/ai/jev.ts`](https://github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/apps/rondyr/src/adapters/ai/jev.ts).

## Get started

Use the Deploy to Cloudflare button, set a setup token, create the owner account and point a form at your Rondyr URL.

```sh
# Deploy: https://deploy.workers.cloudflare.com/?url=https://github.com/basaltbytes/rondyr
<form action="https://YOUR_RONDYR_HOST/f/YOUR_PUBLIC_ID" method="post">...</form>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Spam protection guide: [github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/docs/spam-protection.md](https://github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/docs/spam-protection.md)
- Classifier evaluation: [github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/docs/evaluation.md](https://github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/docs/evaluation.md)
- Costs and limits: [github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/docs/costs.md](https://github.com/basaltbytes/rondyr/blob/91472e160d425755c7e17221170f5dd6ce2fbc34/docs/costs.md)

## Limits and data handling

Messages are stored in your Cloudflare account and classified by Workers AI. Pre-alpha. AGPL-3.0.

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 91472e160d42](https://github.com/basaltbytes/rondyr/tree/91472e160d425755c7e17221170f5dd6ce2fbc34). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
