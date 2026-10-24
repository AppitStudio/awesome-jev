# syn-horse-notifications (Cloudflare Worker that screens notifications with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Cloudflare Worker queue consumer that logs, rate-limits, moderates and delivers notification messages to ntfy or Pushover; Jev classifies each message, checks for attempts to manipulate the screener and rates urgency.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/synmux/syn-horse-notifications) |
| Maintainer | [synmux](https://github.com/synmux). Independently curated. |
| Format | Cloudflare Worker (TypeScript) |
| Requirements | Cloudflare account (Queues, D1, KV); pnpm; TypeSafe, ntfy and Pushover tokens. |
| License | [MIT](https://github.com/synmux/syn-horse-notifications/blob/cee8bf44b91f44950262b753a2fcacf2c3bedd4c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/synmux/syn-horse-notifications/blob/cee8bf44b91f44950262b753a2fcacf2c3bedd4c/src/jev.ts) at the pinned commit. |

## When to use

- Screen alert or contact-form messages for spam before they page you.
- Run moderation in shadow mode first and enforce later.
- Mismatch: built around ntfy and Pushover delivery.

## How it works

`src/jev.ts` posts one request with three questions to `https://api.typesafe.ai/v1/systemone`; `src/stages/ai.ts` applies drop thresholds in code and fails open if Jev is unreachable. Enforcement is off by default (shadow mode). Integration evidence: [`src/jev.ts`](https://github.com/synmux/syn-horse-notifications/blob/cee8bf44b91f44950262b753a2fcacf2c3bedd4c/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pnpm install
pnpm run db:migrate
wrangler secret put TYPESAFE_API_KEY
pnpm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/synmux/syn-horse-notifications#readme](https://github.com/synmux/syn-horse-notifications#readme)

## Limits and data handling

Message text is sent to TypeSafe. Drops apply only when MODERATION_ENFORCE is true.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit cee8bf44b91f](https://github.com/synmux/syn-horse-notifications/tree/cee8bf44b91f44950262b753a2fcacf2c3bedd4c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
