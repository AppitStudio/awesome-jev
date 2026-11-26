# pi-jev-router by Caph (pi extension with a jev/auto virtual model: Jev rates each task, a strong model plans and a cheaper one implements)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Extension for the pi coding agent that registers one virtual model, `jev/auto`. At the start of each stage Jev rates how complex the prompt is; above a threshold the request goes to the complex model, otherwise the standard one, and after a successful write the router can hand implementation to a cheaper model. Three strategies (adaptive, fixed, record) control how often it re-decides.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Caph-dev/pi-jev-router) |
| Maintainer | [Caph](https://github.com/Caph-dev). Independently curated. |
| Format | pi extension (TypeScript, npm `@caph42/pi-jev-router`) |
| Requirements | pi with virtual-model support (tested against pi 1.6.1), Node 20+, the planning and implementation models configured in pi, and optionally a pi classifier model (default `typesafe/jev-latest`). |
| License | [MIT](https://github.com/Caph-dev/pi-jev-router/blob/f4556356d1b37c64212547ae5da5189d26debdb2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/jev-router.ts`](https://github.com/Caph-dev/pi-jev-router/blob/f4556356d1b37c64212547ae5da5189d26debdb2/extensions/jev-router.ts) at the pinned commit. |

## When to use

- pi users who want plans made on a strong model and routine implementation on a cheaper one without switching by hand.
- Mismatch: other coding agents; this is pi-only. Default model slots name OpenAI Codex models you may need to change.

## How it works

`extensions/jev-router.ts` asks pi's configured classifier (default provider `typesafe`, model `jev-latest`) for the probability that a prompt is complex work; the classifier reads only the prompt text, not model names or prices. Without a classifier it resumes the saved planning model; `record` mode logs the upgrade it would have made without changing routes. Integration evidence: [`extensions/jev-router.ts`](https://github.com/Caph-dev/pi-jev-router/blob/f4556356d1b37c64212547ae5da5189d26debdb2/extensions/jev-router.ts).

## Get started

Install from npm through pi, then pick Auto (Jev) in `/model`.

```sh
pi install npm:@caph42/pi-jev-router
pi --model jev/auto
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live smoke results: [github.com/Caph-dev/pi-jev-router/blob/f4556356d1b37c64212547ae5da5189d26debdb2/plans/p1-live-smoke-results.json](https://github.com/Caph-dev/pi-jev-router/blob/f4556356d1b37c64212547ae5da5189d26debdb2/plans/p1-live-smoke-results.json)

## Limits and data handling

Prompt text goes to whichever classifier you configure (TypeSafe by default). Routing quality depends on your thresholds and models; record mode lets you check them before switching routes. npm version 3.0.0 checked; live routing was not run.

## Review and maintenance

Reviewed **2026-11-26** (Europe/Sofia) at [commit f4556356d1b3](https://github.com/Caph-dev/pi-jev-router/tree/f4556356d1b37c64212547ae5da5189d26debdb2). Inspected the README, LICENSE and `extensions/jev-router.ts` at the pinned commit; npm package version 3.0.0 confirmed. The extension was not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
