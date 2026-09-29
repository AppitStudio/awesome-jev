# jevtok-ts

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Offline Jev token counting and request accounting for Node.js/TypeScript — companion port of LabGuy94/jevtok

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/aarzhaev/jevtok-ts) |
| Maintainer | [aarzhaev](https://github.com/aarzhaev). Independently curated. Distinct from Python [jevtok](jevtok.md). |
| Format | TypeScript · library for Node.js/Next.js (MIT). |
| Requirements | Node.js/TypeScript per upstream; no API key for offline counting. |
| License | [MIT](https://github.com/aarzhaev/jevtok-ts/blob/c1d87c92d7176018da6c27b4b887fc0dfc32500a/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Package install/tests not run on the review host. |

## When to use

Use when a TypeScript stack needs offline Jev `input_tokens` / cost estimates before calling TypeSafe (Python users: [jevtok](jevtok.md)).

## How it works

Ports the jevtok accounting model to TS so apps can count tokens and estimate billed request sizes without a live API call.

## Get started

```sh
git clone https://github.com/aarzhaev/jevtok-ts.git
cd jevtok-ts
git checkout c1d87c92d7176018da6c27b4b887fc0dfc32500a
# follow upstream README for package install
```

## Examples and demos

Upstream README usage. No package install executed on the review host.

## Limits and data handling

Offline-only for counting; does not call TypeSafe. Treat estimates as tooling aids, not invoices.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit c1d87c9](https://github.com/aarzhaev/jevtok-ts/tree/c1d87c92d7176018da6c27b4b887fc0dfc32500a). AI-assisted README + LICENSE inspection; install/tests not executed.
