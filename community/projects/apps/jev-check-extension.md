# Jev Check (browser extension)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome and Firefox side-panel extension that asks the page you are reading your own question sets (yes/no, choice, score, multi-pick) and shows probability-ranked answers from Jev, optionally judged against your uploaded resume or checklist.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amir9480/JevCheck) |
| Tags | `Open source` · `Free` · `BYOK` |
| Product homepage | [Product homepage](https://chromewebstore.google.com/detail/acobeddijnaokjkpkmcdfoepbmibpicc) |
| Pricing and access | Free extension on the Chrome Web Store and Firefox Add-ons; you pay your chosen provider for Jev calls. Checked 2026-10-19. |
| Jev evidence | [`src/lib/decision/providers.ts`](https://github.com/amir9480/JevCheck/blob/c9d7daa1ed3da40c695dc053a79618f877bedf79/src/lib/decision/providers.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/amir_9480/status/2112126524128460885)). |
| Maintainer | [amir9480](https://github.com/amir9480). Independently curated. |
| Format | Browser extension (Manifest V3, TypeScript) |
| Platform and availability | Chrome (Chrome Web Store) and Firefox (Firefox Add-ons), Manifest V3. |
| Jev's role | Answers each question in a set about the page's Markdown with typed probabilities; the panel ranks answers and highlights the winner. |
| Requirements | Chrome or Firefox; your own key for a Jev provider (TypeSafe, Vercel AI Gateway or OpenRouter, among others). |
| License | [GPL-3.0](https://github.com/amir9480/JevCheck/blob/c9d7daa1ed3da40c695dc053a79618f877bedf79/LICENSE) |

## When to use

- Want quick answers about a long page (job post fit, article credibility, policy red flags) before reading it all.
- Want to judge pages against your own documents, such as a resume.
- Mismatch: page text and your documents go to the provider you configure; long pages are trimmed in the middle.

## How it works

The extension converts the current page to clean Markdown and sends it with your question set to a decision model. `src/lib/decision/providers.ts` defines the providers, including Vercel AI Gateway (`typesafe-ai/jev`) and OpenRouter (`typesafe/jev-1.13`), and `protocols.ts` maps TypeSafe's `/v1/systemone`. Identical inputs reuse saved results. Integration evidence: [`src/lib/decision/providers.ts`](https://github.com/amir9480/JevCheck/blob/c9d7daa1ed3da40c695dc053a79618f877bedf79/src/lib/decision/providers.ts).

## Get started

From the upstream README: install from the Chrome Web Store or Firefox Add-ons, pick a template, add an API key, then press Evaluate.

```sh
# Chrome: https://chromewebstore.google.com/detail/acobeddijnaokjkpkmcdfoepbmibpicc
# Firefox: https://addons.mozilla.org/en-US/firefox/addon/jev-check-ai-page-evaluator/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [addons.mozilla.org/en-US/firefox/addon/jev-check-ai-page-evaluator/](https://addons.mozilla.org/en-US/firefox/addon/jev-check-ai-page-evaluator/)
- README templates table (tech job, article credibility, policy)

## Limits and data handling

Page content, selected text and uploaded documents go to your chosen provider. Answers are model probabilities, not verified facts. Independent project, not an official TypeSafe product.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit c9d7daa1ed3d](https://github.com/amir9480/JevCheck/tree/c9d7daa1ed3da40c695dc053a79618f877bedf79). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
