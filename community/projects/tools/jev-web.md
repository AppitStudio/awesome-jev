# jev-web

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Browser runtime for open-weight typed-decision models (open-jev/Laya/Strands/…); local after weight cache—independent of hosted TypeSafe Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/warsang/jev-web) |
| Maintainer | [warsang](https://github.com/warsang). Independently curated. |
| Format | Browser npm runtime for open-weight typed-decision models (MIT) |
| Requirements | See upstream README; TypeSafe/OpenRouter keys when using hosted Jev paths. |
| License | [MIT](https://github.com/warsang/jev-web/blob/008e27230555b10b9e56e1ae497e720ebf4f54bb/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Open-weight browser runtime—independent of hosted TypeSafe Jev. Distinct from the Chrome WebMCP extension (sdras/jev-webmcp-extension) and from jackson7705/jev-web-skills. Live install/inference not run on the review host. |

## When to use

Use for private/offline browser typed decisions with open weights. Prefer hosted TypeSafe Jev when you need the production Jev model. Distinct from jev-webmcp-extension (Chrome WebMCP side panel).

## How it works

createDecisionRuntime / createDecider runs a single forward pass over state + typed questions in the browser; weights download once then cache. Live demo: [warsang.github.io/jev-web](https://warsang.github.io/jev-web/).

## Get started

```sh
git clone https://github.com/warsang/jev-web.git
cd jev-web
git checkout 008e27230555b10b9e56e1ae497e720ebf4f54bb
# follow upstream README for install/run
```

## Examples and demos

- Upstream README and any linked demos/benchmarks.

## Limits and data handling

Live Jev may send task text to TypeSafe or another provider and may incur charges. Catalog checks did not execute install or live inference on the review host.

## Review and maintenance

Reviewed **2026-10-03** (Europe/Sofia) at [commit 008e27230555](https://github.com/warsang/jev-web/tree/008e27230555b10b9e56e1ae497e720ebf4f54bb). AI-assisted README and license inspection; install/live paths not executed.
