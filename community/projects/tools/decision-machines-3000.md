# DecisionMachines3000 (web demo of Jev's Noul, Choice and Score primitives, side by side with other decision APIs)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Single-page demo where you compose one decision request in a tree editor or as JSON, pick the primitive (Noul, Choice or Score), tick providers (TypeSafe Jev, SubQ Snap, OpenAI Decisions) and see each provider's answers and probabilities as bars in one table; a separate demo shows cold versus warm connection latency.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/schalkneethling/decision-machines-3000) |
| Maintainer | [schalkneethling](https://github.com/schalkneethling). Independently curated. |
| Format | Cloudflare Worker + Vite web app (TypeScript; no license file) |
| Requirements | Node 24, Vite+ (`vp`), a Cloudflare account to deploy, and at least one provider key such as `TYPESAFE_API_KEY`. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`worker/providers/typesafe.ts`](https://github.com/schalkneethling/decision-machines-3000/blob/34ff2ce2a7b1ebc0821225beb0e035580edeacf0/worker/providers/typesafe.ts) at the pinned commit. |

## When to use

- Learn how Noul, Choice and Score requests look and compare Jev with other decision APIs on the same request.
- Mismatch: production use; it is a demo app.

## How it works

`worker/providers/typesafe.ts` sends the request to `https://api.typesafe.ai/v1/systemone` from the Worker, so the browser never sees the key; providers without a key are hidden. The README says a fresh deployed instance refuses runs until it is put behind Cloudflare Access. Integration evidence: [`worker/providers/typesafe.ts`](https://github.com/schalkneethling/decision-machines-3000/blob/34ff2ce2a7b1ebc0821225beb0e035580edeacf0/worker/providers/typesafe.ts).

## Get started

Install with Vite+ and run locally, or use the Deploy to Cloudflare button and then protect the instance with Cloudflare Access.

```sh
git clone https://github.com/schalkneethling/decision-machines-3000 && cd decision-machines-3000
vp install
vp dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/schalkneethling/decision-machines-3000/blob/34ff2ce2a7b1ebc0821225beb0e035580edeacf0/README.md](https://github.com/schalkneethling/decision-machines-3000/blob/34ff2ce2a7b1ebc0821225beb0e035580edeacf0/README.md)
- Deploy guide: [github.com/schalkneethling/decision-machines-3000/blob/34ff2ce2a7b1ebc0821225beb0e035580edeacf0/docs/deploy.md](https://github.com/schalkneethling/decision-machines-3000/blob/34ff2ce2a7b1ebc0821225beb0e035580edeacf0/docs/deploy.md)

## Limits and data handling

Requests you compose (and any images, for providers that take them) go to the ticked providers on the deployer's keys.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 34ff2ce2a7b1](https://github.com/schalkneethling/decision-machines-3000/tree/34ff2ce2a7b1ebc0821225beb0e035580edeacf0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
