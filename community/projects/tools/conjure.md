# Conjure (decision model art-directs Three.js scenes)

[All projects](../README.md) · [Games and simulation](README.md#games-and-simulation)

Type an idea or mood and a decision model picks worlds, things, looks and directions from a catalogue of procedural Three.js components, then builds and prints the scene in seconds; works with Jev directly or other System One hosts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/captnocap/conjure) |
| Maintainer | [captnocap](https://github.com/captnocap). Independently curated. |
| Format | Local web app (Node.js, Three.js) |
| Requirements | Node.js 22.12+; a decision-model key (`TYPESAFE_API_KEY`, or OpenRouter or NanoGPT). |
| License | [MIT](https://github.com/captnocap/conjure/blob/4915aa63464cbcc323be791d3dc9847be7d93852/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server/providers.ts`](https://github.com/captnocap/conjure/blob/4915aa63464cbcc323be791d3dc9847be7d93852/server/providers.ts) at the pinned commit. |

## When to use

- Turn a sentence into a procedural scene at a fraction of a cent.
- Inspect and pin every art-direction decision.
- Mismatch: compositions come from the built-in catalogue, not image generation.

## How it works

`server/providers.ts` configures TypeSafe (`jev-latest`, `jev-preview`) and other System One hosts; the model answers typed questions with probabilities to choose each component, and a spend cap tracks cost. Integration evidence: [`server/providers.ts`](https://github.com/captnocap/conjure/blob/4915aa63464cbcc323be791d3dc9847be7d93852/server/providers.ts).

## Get started

From the upstream README (not run on the review host):

```sh
npm install
cp .env.example .env   # add a decision-model key
npm run dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Gallery: [github.com/captnocap/conjure/blob/main/docs/gallery/README.md](https://github.com/captnocap/conjure/blob/main/docs/gallery/README.md)
- Component guide: [github.com/captnocap/conjure/blob/main/COMPONENTS.md](https://github.com/captnocap/conjure/blob/main/COMPONENTS.md)

## Limits and data handling

Your prompt is sent to the decision-model provider you configure.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 4915aa63464c](https://github.com/captnocap/conjure/tree/4915aa63464cbcc323be791d3dc9847be7d93852). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
