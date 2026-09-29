# jev-risk-check-provider

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

x402 risk-check provider: TypeSafe Jev typed decisions plus ES256-signed attestations facilitators can verify for agent payments

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/caiovicentino/jev-risk-check-provider) |
| Maintainer | [caiovicentino](https://github.com/caiovicentino). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | TypeScript x402 risk-check provider service. |
| Requirements | Node/TypeScript; `TYPESAFE_API_KEY`; ES256 signing keys per README. |
| License | [MIT](https://github.com/caiovicentino/jev-risk-check-provider/blob/f119bb62964195b0788f988fa95d011b7e2f9962/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when an x402 facilitator or resource server needs an independent Jev-backed risk-check with JWKS-verifiable attestations. Prefer simpler Jev hooks if you are not on the x402 risk-check extension.

## How it works

Discovery at `/.well-known/risk-check.json`, scoring at `POST /v1/risk-check`, compact JWS attestations. Integration evidence: upstream README at the pinned commit.

## Get started

```sh
git clone https://github.com/caiovicentino/jev-risk-check-provider.git
cd jev-risk-check-provider
git checkout f119bb62964195b0788f988fa95d011b7e2f9962
```

Pin revision `f119bb62964195b0788f988fa95d011b7e2f9962` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit f119bb6](https://github.com/caiovicentino/jev-risk-check-provider/tree/f119bb62964195b0788f988fa95d011b7e2f9962). AI-assisted README and LICENSE inspection; install/live paths not executed.
