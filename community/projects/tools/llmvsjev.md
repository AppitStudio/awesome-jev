# LLM vs Jev

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Teaching demo that races Gemini against TypeSafe Jev on the same 1,000 bank transactions into 12 categories, side by side, scored on speed and accuracy, with a no-key mock mode and a tiny Node proxy for the Jev key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/codergarten/llmvsjev) |
| Maintainer | [codergarten](https://github.com/codergarten). Independently curated. |
| Format | Static web demo |
| Requirements | Node for `npx serve`; Gemini and TypeSafe keys for live mode. |
| License | [MIT](https://github.com/codergarten/llmvsjev/blob/61428eb3bdfe2152804dd166f592ea3f2df26e08/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Teach System One vs LLM trade-offs.
- Mismatch: teaching demo only, no key vaulting.

## How it works

See the upstream [README](https://github.com/codergarten/llmvsjev/blob/61428eb3bdfe2152804dd166f592ea3f2df26e08/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/codergarten/llmvsjev.git && cd llmvsjev
npx serve .
```

## Limits and data handling

Live mode sends synthetic transactions to Gemini and TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 61428eb3bdfe](https://github.com/codergarten/llmvsjev/tree/61428eb3bdfe2152804dd166f592ea3f2df26e08). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.

<!-- knowledge:backlinks:start -->
## Knowledge guides

- [Jev vs LLMs: when to use each](../../knowledge-base/articles/jev-vs-llms.md) — Independently suggested by JevList; not an endorsement by Akshay 🚀 (@akshay_pachaar). Explore bounded classification versus text generation with a no-key comparison interface.
<!-- knowledge:backlinks:end -->
