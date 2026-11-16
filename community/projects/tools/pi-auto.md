# pi-auto by ekil1100 (Pi extension that asks Jev or another selector how much thinking effort each task needs, without switching models)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding agent extension that picks the current model's thinking effort before each task and never switches the model itself. A selector decides the effort: by default a System One classifier with configured credentials, preferring `typesafe/jev-latest`, or a fixed chat model you choose in a two-tab `/auto model` picker. The answering model owns its effort options and receives the final choice; the footer shows `auto` and the selector in use.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ekil1100/pi-auto) |
| Maintainer | [ekil1100](https://github.com/ekil1100). Independently curated. |
| Format | Pi agent extension (npm `pi-auto`, TypeScript, MIT) |
| Requirements | Pi 1.5.0+, Node.js 22.19+, and TypeSafe credentials in Pi for Jev (or another classifier or chat model). |
| License | [MIT](https://github.com/ekil1100/pi-auto/blob/8a2b3e82d17cd06b288984b5c78a135e390bf51b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/backends.ts`](https://github.com/ekil1100/pi-auto/blob/8a2b3e82d17cd06b288984b5c78a135e390bf51b/src/backends.ts) at the pinned commit. |

## When to use

- Spend less reasoning on easy Pi tasks and more on hard ones automatically.
- Mismatch: model routing; it adjusts effort only.

## How it works

`src/backends.ts` lists Pi's available classifier models with credentials and picks `typesafe/jev-latest` first; `src/classifier.ts` asks it which effort level fits the task. Integration evidence: [`src/backends.ts`](https://github.com/ekil1100/pi-auto/blob/8a2b3e82d17cd06b288984b5c78a135e390bf51b/src/backends.ts).

## Get started

Install from npm into Pi and pick a selector.

```sh
pi install npm:pi-auto
# inside Pi:
/auto model    # choose the system one tab -> typesafe/jev-latest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ekil1100/pi-auto/blob/8a2b3e82d17cd06b288984b5c78a135e390bf51b/README.md](https://github.com/ekil1100/pi-auto/blob/8a2b3e82d17cd06b288984b5c78a135e390bf51b/README.md)
- npm: [www.npmjs.com/package/pi-auto](https://www.npmjs.com/package/pi-auto)

## Limits and data handling

The task text goes to the selector's provider on your credentials. Jev is the default but not required.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 8a2b3e82d17c](https://github.com/ekil1100/pi-auto/tree/8a2b3e82d17cd06b288984b5c78a135e390bf51b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
