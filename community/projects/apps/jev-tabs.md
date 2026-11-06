# jev-tabs (Chrome extension that groups and suggests closing tabs with Jev)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension that asks TypeSafe Jev (or OpenRouter/Workers AI decision endpoints) to place each tab into a colored group from its title and URL, and to suggest which tabs are safe to close.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/fatalbazuka/jev-tabs) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/fatalbazuka/jev-tabs#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-07. |
| Jev evidence | [`extension/background.js`](https://github.com/fatalbazuka/jev-tabs/blob/d772dcf90a1d091a55759c03709f96cb6526b1d2/extension/background.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [fatalbazuka](https://github.com/fatalbazuka). Independently curated. |
| Format | Chrome Manifest V3 extension (JavaScript, MIT) |
| Platform and availability | Chromium browser extension (Manifest V3). |
| Jev's role | Classifies tabs into user-defined groups and close-suggestions via typed System One questions to TypeSafe Jev (`jev-latest` at api.typesafe.ai/v1/systemone) or compatible OpenRouter/Workers AI endpoints. |
| Requirements | Chrome/Chromium and a TypeSafe, OpenRouter, or Cloudflare Workers AI key for tab judgments. |
| License | [MIT](https://github.com/fatalbazuka/jev-tabs/blob/d772dcf90a1d091a55759c03709f96cb6526b1d2/LICENSE) |

## When to use

- Auto-group a large tab set by topic.
- Get close suggestions without sending page bodies.
- Mismatch: Russian-first UI in the reviewed tip; titles and URLs only.

## How it works

`extension/background.js` POSTs System One requests to the configured provider endpoint (`https://api.typesafe.ai/v1/systemone` for TypeSafe) with tab title/URL state and applies the returned group/close choices. Integration evidence: [`extension/background.js`](https://github.com/fatalbazuka/jev-tabs/blob/d772dcf90a1d091a55759c03709f96cb6526b1d2/extension/background.js).

## Get started

Load the unpacked extension from `extension/`, open options, and paste a TypeSafe (or OpenRouter/Workers AI) key.

```sh
git clone https://github.com/fatalbazuka/jev-tabs.git && cd jev-tabs
# Chrome → Extensions → Load unpacked → extension/
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/fatalbazuka/jev-tabs/blob/d772dcf90a1d091a55759c03709f96cb6526b1d2/README.md](https://github.com/fatalbazuka/jev-tabs/blob/d772dcf90a1d091a55759c03709f96cb6526b1d2/README.md)

## Limits and data handling

Tab titles and URLs are sent to the configured decision provider on your key. Page bodies are not read in the reviewed tip.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit d772dcf90a1d](https://github.com/fatalbazuka/jev-tabs/tree/d772dcf90a1d091a55759c03709f96cb6526b1d2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
