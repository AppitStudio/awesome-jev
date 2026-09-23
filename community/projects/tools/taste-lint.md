# Taste Lint

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Catch AI-sloppy UI motion, copy, and typography before you ship: mechanical rules fail the build, and optional TypeSafe Jev reviews the harder judgment calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mblode/taste-lint) |
| Maintainer | [mblode](https://github.com/mblode) (Matthew Blode). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | npm CLI **taste-lint 0.3.0** (`npx taste-lint@latest init`) plus docs site. |
| Requirements | Node.js **24.11+**. Mechanical `--dry-run` needs no key. Jev review notes need `AI_GATEWAY_API_KEY` (Vercel AI Gateway) or a direct TypeSafe key on the gateway/typesafe transport. |
| License | [MIT](https://github.com/mblode/taste-lint/blob/516c92eae56972516d9cec4486491a352d4a0fed/LICENSE.md). Gateway/TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (`src/map/jev.ts`, README, LICENSE). Package install and live Jev/Gateway runs were **not** executed on the review host. |

## When to use

Use it when a product UI/writing pipeline should **fail the build on known slop patterns** and optionally ask Jev about vague errors, empty states, and similar under-review checks. Prefer [deslop](deslop.md) for page-body ad/slop/SEO probabilities, or [japanese-jev-lint](japanese-jev-lint.md) for Japanese prose flags.

## How it works

Mechanical checks cover motion, copy, and typography (28 blocking; more report-only). Under-review items go to [TypeSafe Jev](https://docs.typesafe.ai/introduction) via [`src/map/jev.ts`](https://github.com/mblode/taste-lint/blob/516c92eae56972516d9cec4486491a352d4a0fed/src/map/jev.ts), which posts System One requests to `https://api.typesafe.ai` or the Vercel AI Gateway evaluation route (`typesafe-ai/jev`), validates answers fail-closed, and never logs response bodies.

## Get started

```sh
npx taste-lint@latest init
npm run taste -- --dry-run   # mechanical checks; no key
# Optional Jev notes (provider charges):
export AI_GATEWAY_API_KEY=…
npm run taste
```

Pin for review: [commit 516c92e](https://github.com/mblode/taste-lint/tree/516c92eae56972516d9cec4486491a352d4a0fed). See upstream [usage docs](https://blode.co/taste-lint/docs/usage).

## Examples and demos

- Profiles: `product`, `writing`, `instructions`, `all`.
- Optional ghostwriter rule packs for voice checks.
- Docs: [blode.co/taste-lint](https://blode.co/taste-lint).

## Limits and data handling

File/snippet excerpts used for under-review questions leave the host on live Jev/Gateway calls. Mechanical dry-run stays local. This listing did not run install or live probes.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 516c92e](https://github.com/mblode/taste-lint/tree/516c92eae56972516d9cec4486491a352d4a0fed) (`taste-lint` **0.3.0**, MIT). AI-assisted review of README, LICENSE.md, `src/map/jev.ts`, npm metadata. No live TypeSafe/Gateway spend.

Related: [deslop](deslop.md), [japanese-jev-lint](japanese-jev-lint.md), [AnchorLint](anchorlint.md).
