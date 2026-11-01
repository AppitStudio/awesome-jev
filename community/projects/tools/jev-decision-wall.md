# Decision Wall (type a text and watch 200 Jev yes/no judgments light up as a heatmap from one parallel call)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency Node demo: type anything and 200 yes/no questions from one of seven question sets are answered by Jev in a single parallel call, shown as a live heatmap with measured latency. A small server proxies the call so the key never reaches the browser.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/charles-forsyth/jev-decision-wall) |
| Maintainer | [charles-forsyth](https://github.com/charles-forsyth). Independently curated. |
| Format | Zero-dependency Node.js server and static page; Docker image |
| Requirements | Node.js 20+; a TypeSafe API key. |
| License | [MIT](https://github.com/charles-forsyth/jev-decision-wall/blob/a4ee45b57fe7e1a52b75d946d3bc9db6c1ea7f81/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`server.js`](https://github.com/charles-forsyth/jev-decision-wall/blob/a4ee45b57fe7e1a52b75d946d3bc9db6c1ea7f81/server.js) at the pinned commit. |

## When to use

- Show how wide a single Jev call can be (many questions, one request).
- Mismatch: a demo, not a library.

## How it works

`server.js` serves the page and forwards `POST /api/jev` to TypeSafe with the key from `TYPESAFE_API_KEY`, `.env` or a key file; the page renders each question's probability as a heatmap cell. Integration evidence: [`server.js`](https://github.com/charles-forsyth/jev-decision-wall/blob/a4ee45b57fe7e1a52b75d946d3bc9db6c1ea7f81/server.js).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/charles-forsyth/jev-decision-wall.git && cd jev-decision-wall
TYPESAFE_API_KEY=... node server.js
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- 70-second demo: [charles-forsyth.github.io/jev-decision-wall/](https://charles-forsyth.github.io/jev-decision-wall/)

## Limits and data handling

Typed text is sent to TypeSafe. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit a4ee45b57fe7](https://github.com/charles-forsyth/jev-decision-wall/tree/a4ee45b57fe7e1a52b75d946d3bc9db6c1ea7f81). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
