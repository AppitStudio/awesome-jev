# SSO as a Decision Model (Rust OpenID AuthZEN policy decision point with Jev judging device, location and time risk)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Rust policy decision point that speaks OpenID AuthZEN and treats every SSO login as a decision: hard rules in Rust handle identity, policy, role and business hours in about 10 ms, while Jev rates device trust, location anomaly, unusual time and overall risk. Every response carries a decision trace saying who judged each factor and why.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/neko32/sso_as_decision_model) |
| Maintainer | [neko32](https://github.com/neko32). Independently curated. |
| Format | Rust service (AuthZEN API) + demo UI |
| Requirements | Rust toolchain; a TypeSafe key; pinned model `jev-1.14.0`. |
| License | [BSD-3-Clause](https://github.com/neko32/sso_as_decision_model/blob/09f1bc02b3ac081e24b979173b7d31bbbbcd4c6b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/src/api/jev.rs`](https://github.com/neko32/sso_as_decision_model/blob/09f1bc02b3ac081e24b979173b7d31bbbbcd4c6b/app/src/api/jev.rs) at the pinned commit. |

## When to use

- Prototype risk-based allow / step-up MFA / deny decisions with an auditable split between rules and model.
- Mismatch: research prototype; not a hardened identity provider.

## How it works

`app/src/api/jev.rs` sends the non-identifying login context to TypeSafe System One with the pinned `jev-1.14.0` model; `app/src/api/authzen.rs` combines the returned probabilities with the Rust rules into Allow, Step-up MFA or Deny plus the trace. The user id is never sent to Jev. Integration evidence: [`app/src/api/jev.rs`](https://github.com/neko32/sso_as_decision_model/blob/09f1bc02b3ac081e24b979173b7d31bbbbcd4c6b/app/src/api/jev.rs).

## Get started

From the upstream README (not run on the review host):

```sh
curl -s localhost:8080/access/v1/evaluation -H 'content-type: application/json' -d '{...}'   # after starting the app per the README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Playwright walkthrough video: [github.com/neko32/sso_as_decision_model/blob/main/docs/demo/playwright-demo.webm](https://github.com/neko32/sso_as_decision_model/blob/main/docs/demo/playwright-demo.webm)

## Limits and data handling

Device, location and time context goes to TypeSafe; identifiers are minimized per the README. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 09f1bc02b3ac](https://github.com/neko32/sso_as_decision_model/tree/09f1bc02b3ac081e24b979173b7d31bbbbcd4c6b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
