# Jevassic Park

[All projects](../README.md) · [Web apps](README.md#web-apps)

A shared, live isometric theme park where about 100 individually simulated guests pick rides, snacks and spectacles through Jev while code handles movement, queues and rides; anyone can watch at the hosted site.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/orshemtov/jevassic-park) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://jevassic-park.vercel.app/) |
| Pricing and access | Free to watch; MIT source. Self-hosting uses your own Vercel AI Gateway billing. Checked 2026-10-17. |
| Jev evidence | [`src/lib/jev/decide.ts`](https://github.com/orshemtov/jevassic-park/blob/039d5768da72d9e040b94403ba13505de1e9b792/src/lib/jev/decide.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [orshemtov](https://github.com/orshemtov). Independently curated. |
| Format | Hosted Next.js web app (Vercel, Redis), MIT source |
| Platform and availability | Web (hosted on Vercel); self-host with Node.js |
| Jev's role | Jev picks each simulated guest's next activity from the legal options. |
| Requirements | A browser to watch; Node.js 22 and a Vercel AI Gateway key or project OIDC to run it with Jev. |
| License | [MIT](https://github.com/orshemtov/jevassic-park/blob/039d5768da72d9e040b94403ba13505de1e9b792/LICENSE) |

## When to use

- Watch a playful demo of Jev making many small choices among legal options.
- Study budget reservation and no-audience-no-calls patterns for a public Jev demo.
- Mismatch: entertainment; background crowd figures do not make AI calls.

## How it works

Visible spectators poll `/api/watch`; a shared Redis park state feeds Jev (`typesafe-ai/jev-1.14.0` through the Vercel AI Gateway) with legal choices and each guest's needs, and code validates and executes the chosen action. Spending is reserved before each call under a daily ceiling, and hidden tabs stop polling. Integration evidence: [`src/lib/jev/decide.ts`](https://github.com/orshemtov/jevassic-park/blob/039d5768da72d9e040b94403ba13505de1e9b792/src/lib/jev/decide.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
cp .env.example .env
npm run dev   # http://localhost:3000; deterministic decisions work without credentials
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live park: [jevassic-park.vercel.app/](https://jevassic-park.vercel.app/)

## Limits and data handling

The hosted park spends the maintainer's Jev budget while people watch; self-hosting spends yours (`WATCH_DAILY_BUDGET`, default 5 USD per day). Vercel Web Analytics runs on the hosted site.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 039d5768da72](https://github.com/orshemtov/jevassic-park/tree/039d5768da72d9e040b94403ba13505de1e9b792). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
