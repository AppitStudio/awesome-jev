# ClaimSignal (insurance claim triage with Jev on Cloudflare Workers AI)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Insurance claim triage service for Cloudflare Workers: Jev answers claim type, fraud-indicator score and needs-review in one call, a routing policy auto-resolves, falls back to an LLM or sends the claim to a person, and a benchmark harness compares Jev with an LLM.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sanketmuchhala/ClaimSignal) |
| Maintainer | [sanketmuchhala](https://github.com/sanketmuchhala). Independently curated. |
| Format | Cloudflare Worker (TypeScript) |
| Requirements | Cloudflare account with Workers AI; Node.js and Wrangler. |
| License | [MIT](https://github.com/sanketmuchhala/ClaimSignal/blob/2b48a506e91e170e65da8ced51565b55d404e64a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/sanketmuchhala/ClaimSignal/blob/2b48a506e91e170e65da8ced51565b55d404e64a/src/jev.ts) at the pinned commit. |

## When to use

- Prototype confidence-based routing for claims or similar cases.
- Compare Jev with an LLM on the same claims.
- Mismatch: the author marks it as actively in progress; data is synthetic.

## How it works

`src/jev.ts` calls Jev through the Workers AI binding (`typesafe/jev`) with a choice, a score and a yes/no question per claim, and validates that the returned probabilities are consistent before routing. Integration evidence: [`src/jev.ts`](https://github.com/sanketmuchhala/ClaimSignal/blob/2b48a506e91e170e65da8ced51565b55d404e64a/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm ci
npm test
npm run benchmark -- --mock
npx wrangler@4.141.0 login
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live comparison report: [github.com/sanketmuchhala/ClaimSignal/blob/main/reports/live-comparison.md](https://github.com/sanketmuchhala/ClaimSignal/blob/main/reports/live-comparison.md)
- README: [github.com/sanketmuchhala/ClaimSignal#readme](https://github.com/sanketmuchhala/ClaimSignal#readme)

## Limits and data handling

Claim text goes to Cloudflare Workers AI. Not a production claims system.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 2b48a506e91e](https://github.com/sanketmuchhala/ClaimSignal/tree/2b48a506e91e170e65da8ced51565b55d404e64a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
