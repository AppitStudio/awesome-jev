# Mailroom by origna8 (self-hosted email for people and AI agents on Cloudflare, where Jev applies your auto-labels)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted email system on your own Cloudflare account: people use a Gmail-style web UI, agents read and send through MCP with scoped OAuth, and every agent-drafted reply waits for one-click approval. Your natural-language label rules are checked against new mail by Jev. Separate from the listed Kevin-Liu-01 Mailroom.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/origna8/mailroom) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/origna8/mailroom#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build under Apache-2.0; needs Cloudflare Workers Paid for outbound mail plus Workers AI usage. Checked 2026-11-03. |
| Jev evidence | [`src/worker/email/label.ts`](https://github.com/origna8/mailroom/blob/c64453d200aa7f9d7d54778584d6c8d74b26aa93/src/worker/email/label.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [origna8](https://github.com/origna8). Independently curated. |
| Format | Web app + MCP server (Cloudflare Workers, D1, R2) |
| Platform and availability | Self-hosted on Cloudflare. |
| Jev's role | Checks each new email against your natural-language label rules. |
| Requirements | A domain on Cloudflare, R2, Workers Paid for outbound email, and the Workers AI binding for Jev labels. |
| License | [Apache-2.0](https://github.com/origna8/mailroom/blob/c64453d200aa7f9d7d54778584d6c8d74b26aa93/LICENSE) |

## When to use

- Run a shared inbox where agents can draft and send under human approval.
- Mismatch: Cloudflare-only; Jev is used only for automatic labels.

## How it works

`src/worker/email/label.ts` builds one noul question per label rule (up to 20) from the new message's subject, sender and body and runs it through the Workers AI binding with the `typesafe/jev` model, tagging every label scoring 0.5 or more. Integration evidence: [`src/worker/email/label.ts`](https://github.com/origna8/mailroom/blob/c64453d200aa7f9d7d54778584d6c8d74b26aa93/src/worker/email/label.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/origna8/mailroom.git
cd mailroom
npm ci
npm run db:migrate:local
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Deploy and feature guide: [github.com/origna8/mailroom#readme](https://github.com/origna8/mailroom#readme)

## Limits and data handling

Message text (up to 8,000 characters) is sent to Jev through Cloudflare Workers AI for labelling; drafts go to the model you configure. Web app and MCP sit behind Cloudflare Access. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit c64453d200aa](https://github.com/origna8/mailroom/tree/c64453d200aa7f9d7d54778584d6c8d74b26aa93). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
