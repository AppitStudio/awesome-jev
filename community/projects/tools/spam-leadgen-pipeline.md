# Spam → Lead Gen Pipeline

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Mines your Gmail spam folder for ICP-fit senders: Jev classifies and scores each email, then the pipeline audits the sender's email infrastructure and drafts (never sends) a reverse pitch.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/automatewithuday/spam-leadgen-pipeline) |
| Maintainer | [automatewithuday](https://github.com/automatewithuday). Independently curated. |
| Format | Node.js pipeline + Claude Code commands |
| Requirements | Gmail API OAuth, TypeSafe API key, Supabase. |
| License | [MIT](https://github.com/automatewithuday/spam-leadgen-pipeline/blob/030bb0a3d3fb1d0a56a478a0af1d86c94ef8a9ff/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/classify.ts`](https://github.com/automatewithuday/spam-leadgen-pipeline/blob/030bb0a3d3fb1d0a56a478a0af1d86c94ef8a9ff/src/classify.ts) at the pinned commit. |

## When to use

- Turn cold emails that landed in spam into qualified prospects for a deliverability offer.
- Classify senders by segment, business type and legitimacy with typed judgments.
- Mismatch: drafts only; review outreach for consent and law in your jurisdiction.

## How it works

Each spam email gets one batched Jev request with segment, business-type and legitimacy questions; an ICP rule qualifies senders, DNS/header audits run in code, and drafts are stored in Supabase. Integration evidence: [`src/classify.ts`](https://github.com/automatewithuday/spam-leadgen-pipeline/blob/030bb0a3d3fb1d0a56a478a0af1d86c94ef8a9ff/src/classify.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run ingest
npm run classify -- --sample 10
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Flow diagram in the upstream README.

## Limits and data handling

Email headers and bodies from your spam folder are sent to TypeSafe and billed to your key; data is stored in your Supabase.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 030bb0a3d3fb](https://github.com/automatewithuday/spam-leadgen-pipeline/tree/030bb0a3d3fb1d0a56a478a0af1d86c94ef8a9ff). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
