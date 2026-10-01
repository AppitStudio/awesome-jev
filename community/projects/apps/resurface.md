# Resurface

[All projects](../README.md) · [Web apps](README.md#web-apps)

Resume screening: LLM writes questions; TypeSafe Jev System One classifies answers.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dolevhayut/resurface) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://github.com/dolevhayut/resurface) |
| Pricing and access | No app purchase fee for the described source-build path, checked **2026-10-01**. TypeSafe/provider usage for live Jev is separate (BYOK). |
| Jev evidence | Upstream README documents TypeSafe Jev / System One typed decisions ([repository](https://github.com/dolevhayut/resurface/tree/9a0f78b5603c5be92b5d48f334e58bc71c1294ec)). Live product paths not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe paths not run on the review host. |
| Maintainer | [dolevhayut](https://github.com/dolevhayut). Independently curated. |
| Format | TypeScript · web app (MIT) |
| Platform and availability | Source-build per upstream README. |
| Jev's role | Typed System One judgments inside the product loop; application code owns UX, rules, and side effects. |
| Requirements | See upstream; TypeSafe/OpenRouter key for live Jev (BYOK). |
| License | [MIT](https://github.com/dolevhayut/resurface/blob/9a0f78b5603c5be92b5d48f334e58bc71c1294ec/LICENSE). |

## When to use

Use when you want this product's workflow with inspectable Jev judgments. Prefer other catalog apps when you need a different platform.

## How it works

The app supplies shared state and authored questions; Jev returns typed answers; application code routes, stops, and renders results.

## Get started

```sh
git clone https://github.com/dolevhayut/resurface.git
cd resurface
git checkout 9a0f78b5603c5be92b5d48f334e58bc71c1294ec
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos.

## Limits and data handling

Live Jev may send app context to TypeSafe or another provider and may incur charges. Catalog checks did not run live sessions on the review host.

## Review and maintenance

Reviewed **2026-10-01** (Europe/Sofia) at [commit 9a0f78b5603c](https://github.com/dolevhayut/resurface/tree/9a0f78b5603c5be92b5d48f334e58bc71c1294ec). AI-assisted README and license inspection; install/live paths not executed.
