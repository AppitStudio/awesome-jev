# typesafe-cascade (TypeScript helper that asks Jev first and sends to a slower model, rules engine or human only when confidence is low)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Small TypeScript library for a System 1 to System 2 cascade: Jev answers a typed `choice` question, and if its confidence clears your threshold you take the label; if not, or on an error or missed deadline, the request goes to your System 2 (a language model, a rules engine or a human queue) together with Jev's attempt. An evaluation on GitHub issue triage (bug, feature, docs or question) pins 2,319 issues from large repositories to measure savings instead of guessing.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/monumei/typesafe-cascade) |
| Maintainer | [monumei](https://github.com/monumei). Independently curated. |
| Format | TypeScript library and eval scripts (Bun) |
| Requirements | Bun and a `TYPESAFE_API_KEY`; a System 2 you provide. |
| License | [MIT](https://github.com/monumei/typesafe-cascade/blob/358887c0f3937171b78d2b591fb8ca04a173fe6e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/cascade.ts`](https://github.com/monumei/typesafe-cascade/blob/358887c0f3937171b78d2b591fb8ca04a173fe6e/src/cascade.ts) at the pinned commit. |

## When to use

- Add a cheap first pass in front of an expensive classifier, with a confidence threshold you control.
- Mismatch: it is a pattern and demo, not a hosted service, and the README withholds savings numbers until the evaluation reports.

## How it works

`src/cascade.ts` uses `TypeSafeClient.systemOne` from `@typesafe-ai/sdk` with no retries, honouring `TYPESAFE_DEFAULT_MODEL` and `TYPESAFE_BASE_URL` (default `jev-latest`) and a deadline; below-threshold, error and timeout cases all route to System 2. Integration evidence: [`src/cascade.ts`](https://github.com/monumei/typesafe-cascade/blob/358887c0f3937171b78d2b591fb8ca04a173fe6e/src/cascade.ts).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/monumei/typesafe-cascade.git
cd typesafe-cascade
bun install
bun test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the cascade diagram, usage and evaluation design: [github.com/monumei/typesafe-cascade#readme](https://github.com/monumei/typesafe-cascade#readme)

## Limits and data handling

Text you classify goes to TypeSafe on your key; the live evaluation spends your TypeSafe credits. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 358887c0f393](https://github.com/monumei/typesafe-cascade/tree/358887c0f3937171b78d2b591fb8ca04a173fe6e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
