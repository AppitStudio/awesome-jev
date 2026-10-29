# GitMemoMark (Chrome extension that saves X posts and web pages to your GitHub repo as Markdown, with optional Jev folder sorting)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Chrome extension (Manifest V3) that saves X posts, web articles, selections, links and images to a GitHub repository you own as Markdown, with folders, tags and notes. Folder choice goes domain rules first, then Jev if you turned it on, then an unsorted folder. Japanese UI and docs; developer preview, not on the Chrome Web Store.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Aero123421/gitmemomark) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/Aero123421/gitmemomark#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (Apache-2.0); free source build. Jev is off by default; usage is billed to your TypeSafe key. Checked 2026-10-29. |
| Jev evidence | [`src/lib/jev.js`](https://github.com/Aero123421/gitmemomark/blob/ae8006e2a793838fe956c86de500485a7fd91c2f/src/lib/jev.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Aero123421](https://github.com/Aero123421). Independently curated. |
| Format | Chrome extension (JavaScript) |
| Platform and availability | Desktop Chrome; load unpacked from the cloned repo (developer preview). |
| Jev's role | Optional: picks the destination folder for a saved page from your folder list and descriptions. |
| Requirements | Desktop Chrome, a GitHub fine-grained token for one repo, and optionally a TypeSafe API key. |
| License | [Apache-2.0](https://github.com/Aero123421/gitmemomark/blob/ae8006e2a793838fe956c86de500485a7fd91c2f/LICENSE) |

## When to use

- Keep a searchable Markdown archive of X posts and articles in git.
- Mismatch: Japanese only; developer preview.

## How it works

`src/lib/jev.js` posts the page title, URL, description, note and candidate folders to `https://api.typesafe.ai/v1/systemone` (`jev-latest` by default) and uses the choice when it clears your threshold. Integration evidence: [`src/lib/jev.js`](https://github.com/Aero123421/gitmemomark/blob/ae8006e2a793838fe956c86de500485a7fd91c2f/src/lib/jev.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Aero123421/gitmemomark.git
# chrome://extensions → Developer mode → Load unpacked → select the folder
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Japanese) with screenshots: [github.com/Aero123421/gitmemomark#readme](https://github.com/Aero123421/gitmemomark#readme)

## Limits and data handling

With Jev on, page title, URL, description, selected text, notes and folder names go to TypeSafe, sometimes before you press save. Tokens are kept in `chrome.storage.local`, not an encrypted vault.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit ae8006e2a793](https://github.com/Aero123421/gitmemomark/tree/ae8006e2a793838fe956c86de500485a7fd91c2f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
