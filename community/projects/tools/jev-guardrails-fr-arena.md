# jev-guardrails-fr-arena (compare rules, Jev and Shieldstral on the same French safety cases)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Arena that runs the same French guardrail cases through hand-written rules, TypeSafe Jev and a Shieldstral server so you can compare decisions side by side.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-guardrails-fr-arena) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Node.js arena (MIT) |
| Requirements | Node.js, `TYPESAFE_API_KEY`, and optionally a Shieldstral endpoint as documented upstream. |
| License | [MIT](https://github.com/gbesse/jev-guardrails-fr-arena/blob/a4d553e136cf68ebfa8b5434e3be0b2ca58a5424/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.mjs`](https://github.com/gbesse/jev-guardrails-fr-arena/blob/a4d553e136cf68ebfa8b5434e3be0b2ca58a5424/src/jev.mjs) at the pinned commit. |

## When to use

- Benchmark French safety/guardrail cases across rule packs and Jev.
- Keep comparisons on identical inputs.
- Mismatch: French-case focused; Shieldstral is optional.

## How it works

`src/jev.mjs` posts the shared cases to TypeSafe Jev; the CLI aggregates outcomes next to rules and Shieldstral. Integration evidence: [`src/jev.mjs`](https://github.com/gbesse/jev-guardrails-fr-arena/blob/a4d553e136cf68ebfa8b5434e3be0b2ca58a5424/src/jev.mjs).

## Get started

From the upstream README (not run on the review host):

```sh
export TYPESAFE_API_KEY=...
node bin/jev-guardrails-fr-arena.mjs --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-guardrails-fr-arena/blob/a4d553e136cf68ebfa8b5434e3be0b2ca58a5424/README.md](https://github.com/gbesse/jev-guardrails-fr-arena/blob/a4d553e136cf68ebfa8b5434e3be0b2ca58a5424/README.md)

## Limits and data handling

Case texts are sent to TypeSafe on live runs.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit a4d553e136cf](https://github.com/gbesse/jev-guardrails-fr-arena/tree/a4d553e136cf68ebfa8b5434e3be0b2ca58a5424). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
