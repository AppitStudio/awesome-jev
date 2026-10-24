# json-render Jev demo (support desk built and triaged by Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Demo of Jev with json-render: you describe the support console you want and Jev picks and arranges configured panels, then judges every ticket with yes/no, score and topic questions while json-render draws the result.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sethdavis512/json-render-jev-demo) |
| Maintainer | [sethdavis512](https://github.com/sethdavis512). Independently curated. |
| Format | Web app demo (React Router, Bun) |
| Requirements | Bun; a TypeSafe API key (JEV_API_KEY). |
| License | [MIT](https://github.com/sethdavis512/json-render-jev-demo/blob/89a49fdd8191004b99632ec87df6cc4fe35a68d5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`app/lib/desk/judge.server.ts`](https://github.com/sethdavis512/json-render-jev-demo/blob/89a49fdd8191004b99632ec87df6cc4fe35a68d5/app/lib/desk/judge.server.ts) at the pinned commit. |

## When to use

- See how Jev can compose a UI from a fixed set of panels without writing props.
- Triage tickets with several typed questions in one batch.
- Mismatch: a demo with a made-up company and seed data.

## How it works

`judge.server.ts` uses `@typesafe-ai/sdk` (`choice`, `noul`, `score`) to ask ten questions per ticket in one request; `compose.server.ts` uses batched choice requests to pick panels. Code assembles and validates the spec. Integration evidence: [`app/lib/desk/judge.server.ts`](https://github.com/sethdavis512/json-render-jev-demo/blob/89a49fdd8191004b99632ec87df6cc4fe35a68d5/app/lib/desk/judge.server.ts).

## Get started

From the upstream README (not run on the review host):

```sh
cp .env.example .env   # add JEV_API_KEY
bun install
bun run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- json-render: [json-render.dev](https://json-render.dev)
- README: [github.com/sethdavis512/json-render-jev-demo#readme](https://github.com/sethdavis512/json-render-jev-demo#readme)

## Limits and data handling

Seed tickets and your console requests are sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 89a49fdd8191](https://github.com/sethdavis512/json-render-jev-demo/tree/89a49fdd8191004b99632ec87df6cc4fe35a68d5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
