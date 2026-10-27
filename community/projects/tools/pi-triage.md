# pi-triage (pi tool that decides how much work a request deserves before it spends a token)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

pi coding-agent tool that sorts each request into one of six routes (answer inline, worker, scout then worker, planner then worker, browser QA, or review) and returns the tier, confidence, verification level and route string, using Jev on OpenRouter first, a self-hosted Laya engine second and capped keyword rules last.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tripplen23/pi-triage) |
| Maintainer | [tripplen23](https://github.com/tripplen23). Independently curated. |
| Format | pi package (TypeScript) |
| Requirements | pi; an OpenRouter API key (or pi's stored credential) for the Jev engine; Laya optional. |
| License | [MIT](https://github.com/tripplen23/pi-triage/blob/4fb47528f38ddcfaa6f8bf028563518e57ab217b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/engines.ts`](https://github.com/tripplen23/pi-triage/blob/4fb47528f38ddcfaa6f8bf028563518e57ab217b/src/engines.ts) at the pinned commit. |

## When to use

- Stop spawning sub-agents for requests that can be answered inline.
- Get a confidence and a route string instead of a bare label.
- Mismatch: pi only; Jev is reached through OpenRouter.

## How it works

`src/engines.ts` asks `jev-1.13` on OpenRouter for the tier with a 2.5 s timeout and falls back to Laya, then to keyword rules capped at 0.6 confidence so they cannot authorise expensive routes alone. Integration evidence: [`src/engines.ts`](https://github.com/tripplen23/pi-triage/blob/4fb47528f38ddcfaa6f8bf028563518e57ab217b/src/engines.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/tripplen23/pi-triage
# then call triage({ prompt: "<the user's request>" }) at the start of a request
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tripplen23/pi-triage#readme](https://github.com/tripplen23/pi-triage#readme)

## Limits and data handling

Request text goes to OpenRouter and on to TypeSafe, or to your Laya server. Accuracy figures are the author's.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 4fb47528f38d](https://github.com/tripplen23/pi-triage/tree/4fb47528f38ddcfaa6f8bf028563518e57ab217b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
