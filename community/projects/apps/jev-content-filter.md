# Jev Content Filter (hide classified ads that don't match your plain-language criteria)

[All projects](../README.md) · [Browser extensions](README.md#browser-extensions)

Browser extension for classified-ad and auction sites: you write what you want in plain Czech or English (price range, model year, condition), it asks Jev one yes/no question per ad in batches of ten, and collapses or dims the ads that don't match; works on Bazos.cz/.sk/.pl/.at today, with a modular design for other sites.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Aladincz/Jev-Content-Filter) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/Aladincz/Jev-Content-Filter#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Jev calls are billed to your own TypeSafe key. Checked 2026-10-27. |
| Jev evidence | [`src/api.js`](https://github.com/Aladincz/Jev-Content-Filter/blob/25c582951ea691dd1bfd425e4a6e062c037ef96d/src/api.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [Aladincz](https://github.com/Aladincz). Independently curated. |
| Format | Browser extension (JavaScript, esbuild) |
| Platform and availability | Chromium-based browsers; build from source and load unpacked. Work in progress. |
| Jev's role | Per-ad yes/no filter: each ad's text goes to Jev as a Noul question against your criteria. |
| Requirements | Node.js to build; a TypeSafe API key stored in the extension. |
| License | [MIT](https://github.com/Aladincz/Jev-Content-Filter/blob/25c582951ea691dd1bfd425e4a6e062c037ef96d/LICENSE) |

## When to use

- Filter crowded classifieds by criteria the site's own filters can't express.
- Mismatch: only Bazos sites are supported so far; early-stage project by a first-time author.

## How it works

`src/api.js` posts batches of ad texts as Noul questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); answers are cached in memory and failed ads are marked, not retried. Integration evidence: [`src/api.js`](https://github.com/Aladincz/Jev-Content-Filter/blob/25c582951ea691dd1bfd425e4a6e062c037ef96d/src/api.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Aladincz/Jev-Content-Filter && cd Jev-Content-Filter
npm install
npm run build   # then load dist/ as an unpacked extension
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Aladincz/Jev-Content-Filter#readme](https://github.com/Aladincz/Jev-Content-Filter#readme)

## Limits and data handling

Ad text and your criteria go to TypeSafe when you press Apply. The key stays in the browser's extension storage.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 25c582951ea6](https://github.com/Aladincz/Jev-Content-Filter/tree/25c582951ea691dd1bfd425e4a6e062c037ef96d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
