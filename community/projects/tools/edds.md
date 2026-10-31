# EDDS (event-driven decision system: listeners described in plain language, scored in parallel by a decision model like Jev)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

TypeScript library where listeners describe in plain language when they should fire; for each event a decision model scores every listener in parallel and returns one probability per listener, and listeners above their threshold fire. Includes tracing, fallbacks, routing images to a vision model, and a review tool that proposes cheap keyword rules from traces, optionally using Jev to drop coincidental keywords.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gigi-fernandez/edds) |
| Maintainer | [gigi-fernandez](https://github.com/gigi-fernandez). Independently curated. |
| Format | TypeScript · npm library + review CLI |
| Requirements | Node.js; an OpenRouter key for `typesafe/jev-1.14` (or another decision-model / OpenAI-compatible provider). |
| License | [MIT](https://github.com/gigi-fernandez/edds/blob/07c1bcbdc35fb64b89d1af82464c723ad304b74f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/models/openrouter.ts`](https://github.com/gigi-fernandez/edds/blob/07c1bcbdc35fb64b89d1af82464c723ad304b74f/src/models/openrouter.ts) at the pinned commit. |

## When to use

- Fan one event out to many plain-language handlers without writing a classifier per handler.
- Mismatch: provider-agnostic; Jev is the documented default, not a requirement.

## How it works

`src/models/openrouter.ts` calls OpenRouter's decisions endpoint with `typesafe/jev-1.14`, asking one yes/no per listener; `withFallback` and per-event model selection are composed in code, and `dev/review/cli.ts --judge typesafe/jev-1.14` filters proposed rules. Integration evidence: [`src/models/openrouter.ts`](https://github.com/gigi-fernandez/edds/blob/07c1bcbdc35fb64b89d1af82464c723ad304b74f/src/models/openrouter.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
npm run review -- --trace t.jsonl --judge typesafe/jev-1.14
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Support inbox example: [github.com/gigi-fernandez/edds/blob/main/examples/support-inbox.ts](https://github.com/gigi-fernandez/edds/blob/main/examples/support-inbox.ts)

## Limits and data handling

Event text (and images if routed) is sent to the configured provider. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-31** (Europe/Sofia) at [commit 07c1bcbdc35f](https://github.com/gigi-fernandez/edds/tree/07c1bcbdc35fb64b89d1af82464c723ad304b74f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
