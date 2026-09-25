# specpi-jev-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extension: local deny/fast-pass rules first; uncertain shell/file commands are scored for danger by TypeSafe Jev via OpenRouter (block / ask / allow).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TannerMidd/specpi-jev-guard) |
| Maintainer | [TannerMidd](https://github.com/TannerMidd). Independently curated. |
| Format | npm Pi extension (`specpi-jev-guard`). |
| Requirements | [Pi](https://pi.dev); OpenRouter login or `OPENROUTER_API_KEY` for Jev judgments. |
| License | [MIT](https://github.com/TannerMidd/specpi-jev-guard/blob/da63a13ab7b7b7f3a39799e284a2f103f992477c/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Pi/OpenRouter paths not run on the review host. Upstream suite metrics are author-reported. |

## When to use

Use to **gate risky agent shell/file actions** in Pi with fail-closed behavior when Jev is unavailable or unparsable.

## How it works

Local rules settle obvious cases; remaining commands ask Jev how dangerous they are. High scores block, mid band asks, low scores run.

## Get started

```sh
pi install npm:specpi-jev-guard
# inside pi:
# /login openrouter
# /jev-guard setup
# Pin: https://github.com/TannerMidd/specpi-jev-guard/tree/da63a13ab7b7b7f3a39799e284a2f103f992477c
```

## Examples and demos

- Docs site: [tannermidd.github.io/specpi-jev-guard](https://tannermidd.github.io/specpi-jev-guard/) (devious/red-team pages).

## Limits and data handling

Candidate commands go to OpenRouter/TypeSafe when local rules do not settle them. Without a key or on parse failure, the call does not proceed.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit da63a13](https://github.com/TannerMidd/specpi-jev-guard/tree/da63a13ab7b7b7f3a39799e284a2f103f992477c). AI-assisted README and LICENSE inspection; live Pi install not run.
