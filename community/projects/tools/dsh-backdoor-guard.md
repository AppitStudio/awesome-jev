# dsh-backdoor-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Guard for DeepSeek Harness: every model-requested tool call is judged by a decision model, hosted TypeSafe Jev or a self-hosted LiquidAI d1, before it runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/miketako3/dsh-backdoor-guard) |
| Maintainer | [miketako3](https://github.com/miketako3). Independently curated. |
| Format | DeepSeek Harness extension |
| Requirements | DeepSeek Harness; TypeSafe key (Option A) or self-hosted d1. |
| License | [MIT](https://github.com/miketako3/dsh-backdoor-guard/blob/c7dc5f0a5d48e2c804423785193774394a88204d/LICENSE) |
| Jev evidence | [`src/judge.ts`](https://github.com/miketako3/dsh-backdoor-guard/blob/c7dc5f0a5d48e2c804423785193774394a88204d/src/judge.ts) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Add a fast yes/no safety check before agent tool calls.
- Mismatch: harness-specific; Jev is one of two backends.

## How it works

Tool-call state goes to the decision model with guard questions; probability thresholds allow or block the call. (Summarized from the upstream [README](https://github.com/miketako3/dsh-backdoor-guard/blob/c7dc5f0a5d48e2c804423785193774394a88204d/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install per the README and choose Option A (hosted Jev) or the bundled d1 server.

## Limits and data handling

Tool-call arguments go to TypeSafe when using Jev. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit c7dc5f0a5d48](https://github.com/miketako3/dsh-backdoor-guard/tree/c7dc5f0a5d48e2c804423785193774394a88204d). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
