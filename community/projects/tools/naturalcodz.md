# naturalcodz

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

npm package of natural-logic helpers (`is` / `pick` / `rate` / `classify` / safety guards) backed by TypeSafe Jev with configurable confidence thresholds.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SuparvaCode/naturalcodz) |
| Maintainer | [SuparvaCode](https://github.com/SuparvaCode). Independently curated. |
| Format | TypeScript library (`naturalcodz` on npm). |
| Requirements | Node.js 20+; `TYPESAFE_API_KEY` (or `configure({ apiKey })`). |
| License | [MIT](https://github.com/SuparvaCode/naturalcodz/blob/ed12b0a1ec197c7118ef2b74ae9badf258fdedd9/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe / npm install not run. |

## When to use

Use it for **ergonomic typed checks** in Node apps without hand-rolling System One clients. Prefer lower-level SDKs when you need full control of question batches.

## How it works

Helpers map to Jev primitives with threshold cutoffs (`boolean`, `strong`, `confidence`, guard block/review). Fluent `natural(text).is(…)` chaining is supported.

## Get started

```sh
npm install naturalcodz
# or pin source:
git clone https://github.com/SuparvaCode/naturalcodz.git
cd naturalcodz
git checkout ed12b0a1ec197c7118ef2b74ae9badf258fdedd9
# TYPESAFE_API_KEY=... node examples/…
```

## Examples and demos

- README quick-start snippets; `examples/` and `tests/` (not executed).

## Limits and data handling

Input text leaves your process for TypeSafe. Threshold defaults are application policy—not calibrated guarantees (pair with Sureband/jev-calibrate if needed).

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit ed12b0a](https://github.com/SuparvaCode/naturalcodz/tree/ed12b0a1ec197c7118ef2b74ae9badf258fdedd9). AI-assisted README inspection.

Related: [askjev](askjev.md), [jev-agent-kit](jev-agent-kit.md).
