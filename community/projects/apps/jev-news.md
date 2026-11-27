# Jev News (じぇぶニュース) by dezigozi (hourly Japanese headline portal where Jev sorts news into 16 genres)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Personal news portal that collects headlines from a wide range of sources every hour, has Jev sort each into one of 16 genres and shows headlines only, with Japanese translations of English headlines from Groq. Built and published to GitHub Pages by a scheduled GitHub Actions job.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/dezigozi/jev_news) |
| Tags | `Source available` · `Free` |
| Product homepage | [Product homepage](https://dezigozi.github.io/jev_news/) |
| Pricing and access | Free to read; source is public without a licence. Self-hosting needs your own TypeSafe and Groq keys. Checked 2026-11-27. |
| Jev evidence | [`src/classify.js`](https://github.com/dezigozi/jev_news/blob/f33ca36bf877cdb0789d3f3388266bd720b93bae/src/classify.js) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [dezigozi](https://github.com/dezigozi). Independently curated. |
| Format | Static site built by Node.js + GitHub Actions |
| Platform and availability | Web (GitHub Pages); Japanese interface. |
| Jev's role | Classifier. Each new headline gets one Jev request: a `choice` over 16 genres that decides its section, plus two `noul` questions scoring whether it broadens knowledge and whether it is a widely discussed story. |
| Requirements | A browser to read; Node.js, a TypeSafe key and a Groq key to build your own copy. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Japanese readers who want a quick, genre-sorted headline page.
- Mismatch: full articles or English-language news; it lists headlines only.

## How it works

`src/classify.js` builds the genre `choice` and two `noul` questions for each headline (title, outlet and feed as state) and `src/jev.js` posts them to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) with retries and a 15-second timeout; the hourly `update.yml` workflow restores earlier classifications from cache, classifies new headlines and deploys the site. Integration evidence: [`src/classify.js`](https://github.com/dezigozi/jev_news/blob/f33ca36bf877cdb0789d3f3388266bd720b93bae/src/classify.js).

## Get started

Open the site, or build it locally.

```sh
# site: https://dezigozi.github.io/jev_news/
git clone https://github.com/dezigozi/jev_news && cd jev_news
npm ci && npm run build && npm run preview
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Site: [dezigozi.github.io/jev_news/](https://dezigozi.github.io/jev_news/)

## Limits and data handling

Headlines link to their sources; genre labels come from Jev and may be wrong. English headline translations come from Groq. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit f33ca36bf877](https://github.com/dezigozi/jev_news/tree/f33ca36bf877cdb0789d3f3388266bd720b93bae). Inspected the README, `src/jev.js` and the update workflow at the pinned commit and confirmed the site returns HTTP 200; no licence file present. Not built on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
