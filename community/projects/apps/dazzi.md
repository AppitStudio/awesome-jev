# Dazzi by NomaDamas (Finder-style desktop file manager that answers questions about your files with citations, powered by AutoRAG and Jev)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Desktop file manager for macOS and Windows built on the AutoRAG librarian: browse files, preview with Space, find duplicates and version stacks, and ask questions across documents, chats and mail with every answer citing its source. The librarian's Jev decisions (query routing, citation and evidence checks) run on Dazzi's managed models or on your own provider key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NomaDamas/AutoRAG-app) |
| Tags | `Source available` · `Freemium` · `Commercial` |
| Product homepage | [Product homepage](https://dazziapp.com/) |
| Pricing and access | Freemium: Free ($0, small credit allowance covering chat, embeddings, reranking and Jev), Air $4/mo, Pro $20/mo and Max $200/mo per [dazziapp.com](https://dazziapp.com/); or connect your own provider key and pay the provider. Checked 2026-11-25. |
| Jev evidence | [`src/main/decision-model.ts`](https://github.com/NomaDamas/AutoRAG-app/blob/b4aa008127b8e211e2072e5d92b688c50d7f9236/src/main/decision-model.ts) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Commercial product: freemium, with paid Air, Pro and Max plans for managed models. |
| Maintainer | [NomaDamas / Marker Inc.](https://github.com/NomaDamas). Independently curated. |
| Format | Electron desktop app (TypeScript) |
| Platform and availability | macOS (Apple silicon DMG) and Windows (x64 installer). |
| Jev's role | Through the bundled AutoRAG librarian, Jev routes each question and judges whether cited excerpts are relevant and supported before an answer is shown. |
| Requirements | macOS on Apple silicon or Windows x64; a Dazzi account (managed models) or your own provider key. |
| License | [FSL-1.1-MIT (Fair Source)](https://github.com/NomaDamas/AutoRAG-app/blob/b4aa008127b8e211e2072e5d92b688c50d7f9236/LICENSE) |

## When to use

- Search and ask across local files, mail and messengers from one Finder-like window.
- Mismatch: if you need an OSI open-source app; Dazzi is Fair Source (FSL-1.1-MIT), converting to MIT two years after each release.

## How it works

`src/main/decision-model.ts` wires the librarian's Jev backend (`jev-use`) to Dazzi Models when signed in and to OpenRouter otherwise; `src/main/jev-migration.ts` migrates older configs because the librarian made the decision model mandatory. Integration evidence: [`src/main/decision-model.ts`](https://github.com/NomaDamas/AutoRAG-app/blob/b4aa008127b8e211e2072e5d92b688c50d7f9236/src/main/decision-model.ts).

## Get started

Download the installer from dazziapp.com, or build from source.

```sh
git clone https://github.com/NomaDamas/AutoRAG-app
cd AutoRAG-app
make run   # dev build; see README for requirements
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Engine: [github.com/Marker-Inc-Korea/AutoRAG](https://github.com/Marker-Inc-Korea/AutoRAG)
- Pricing: [dazziapp.com/](https://dazziapp.com/)

## Limits and data handling

Commercial product by the same team as AutoRAG. Source available under FSL-1.1-MIT (free for non-competing use). With managed models, questions and cited excerpts go to Dazzi's hosted service; cloud embedding (Pro) only after opt-in. Plan credit allowances are not quantified on the pricing page.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit b4aa008127b8](https://github.com/NomaDamas/AutoRAG-app/tree/b4aa008127b8e211e2072e5d92b688c50d7f9236). Inspected the README, license, pricing page and the decision-model wiring at the pinned commit; the app was not installed on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
