# pi-skimmer

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension for goal-directed text and JSON filtering powered by Jev (via pi-typesafe), with explicit consent and recoverable results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jon-devlapaz/pi-skimmer) |
| Maintainer | [jon-devlapaz](https://github.com/jon-devlapaz). Independently curated. |
| Format | Pi extension (TypeScript) |
| Requirements | Pi 1.2.0+, Node.js 22.19+, TypeSafe API key via pi-typesafe. |
| License | [MIT](https://github.com/jon-devlapaz/pi-skimmer/blob/9e0f135fa1f71017be5450d580572eb7ccaa807e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extensions/skimmer/index.ts`](https://github.com/jon-devlapaz/pi-skimmer/blob/9e0f135fa1f71017be5450d580572eb7ccaa807e/extensions/skimmer/index.ts) at the pinned commit. |

## When to use

- Keep only the relevant chunks of a long text or the relevant records of a JSON array before the model reads them.
- Require explicit operator consent before anything is sent to TypeSafe.
- Mismatch: does not intercept reads or fetch URLs.

## How it works

`skim_text` and `filter_items` tools send supplied text or selected fields with the goal to Jev through the pi-typesafe SDK and keep what Jev marks relevant; unjudged material is preserved in owner-only recovery files. Integration evidence: [`extensions/skimmer/index.ts`](https://github.com/jon-devlapaz/pi-skimmer/blob/9e0f135fa1f71017be5450d580572eb7ccaa807e/extensions/skimmer/index.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install git:github.com/jon-devlapaz/pi-skimmer
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Commands: `/typesafe login`, `/skim enable`.

## Limits and data handling

Supplied text is sent to TypeSafe after consent and billed to your key; recovery files stay local.

## Review and maintenance

Reviewed **2026-10-15** (Europe/Sofia) at [commit 9e0f135fa1f7](https://github.com/jon-devlapaz/pi-skimmer/tree/9e0f135fa1f71017be5450d580572eb7ccaa807e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
