# Jevvy (Pi extension for source-linked Jev review of comments, functions and tests)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi package that extracts selected source units (JavaScript/TypeScript, Rust, Python, Solidity), asks Jev a fixed set of review questions per pack (comments, functions, tests), and saves the answers with the code and question definitions so you and Pi can check the evidence before changing anything. Scans never edit source.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/timbrinded/jevvy) |
| Maintainer | [timbrinded](https://github.com/timbrinded). Independently curated. |
| Format | Pi extension (npm package) |
| Requirements | Pi; Node 26 on macOS or glibc Linux (ARM64 or x64); a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/timbrinded/jevvy/blob/77fe07ff1a00f05377d85eef7ba6aea68f7b9352/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev.ts`](https://github.com/timbrinded/jevvy/blob/77fe07ff1a00f05377d85eef7ba6aea68f7b9352/src/jev.ts) at the pinned commit. |

## When to use

- Get a structured, evidence-backed review of uncommitted changes inside Pi.
- Mismatch: Pi only; Node 26 required.

## How it works

`src/jev.ts` uses `TypeSafeClient` from `@typesafe-ai/sdk` with an explicit endpoint, sending each extracted unit and its context with the pack's questions; validated answers are cached and bundled as review evidence. Integration evidence: [`src/jev.ts`](https://github.com/timbrinded/jevvy/blob/77fe07ff1a00f05377d85eef7ba6aea68f7b9352/src/jev.ts).

## Get started

From the upstream README (not run on the review host):

```sh
pi install npm:jevvy
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Pack questions and evidence: [github.com/timbrinded/jevvy/blob/master/docs/packs.md](https://github.com/timbrinded/jevvy/blob/master/docs/packs.md)

## Limits and data handling

Selected source units and context are sent to TypeSafe; cached results older than 30 days are removed by default. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 77fe07ff1a00](https://github.com/timbrinded/jevvy/tree/77fe07ff1a00f05377d85eef7ba6aea68f7b9352). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
