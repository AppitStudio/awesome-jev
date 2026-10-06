# Jev for Excel

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial Excel add-in that calls TypeSafe Jev from worksheet formulas — `=JEV.ASK("choice"|"score"|"noul", A2, …)`, shortcut functions and `JEV.STATE` for multi-field rows — as an async Office add-in for Microsoft 365 or a Windows VBA edition.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/paulobrien/jev-excel) |
| Maintainer | [paulobrien](https://github.com/paulobrien). Independently curated. |
| Format | Office.js custom-functions add-in (self-hosted/Cloudflare) + VBA `.xlam` edition |
| Requirements | Excel for Windows, Mac or web (Microsoft 365) for the add-in, or Windows desktop Excel for VBA; a TypeSafe API key; Node.js to run or deploy the add-in. |
| License | [MIT](https://github.com/paulobrien/jev-excel/blob/609f01d1984a3095776ac98ab7772ff8b2100a6c/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Label survey answers, tickets or reviews in a spreadsheet with `JEV.ASK("choice", …)`.
- Score rows on a rubric or evaluate several fields at once with `JEV.STATE`.
- Mismatch: you host the add-in yourself (local or Cloudflare); unofficial and BYOK.

## How it works

Custom functions ([`src/functions.js`](https://github.com/paulobrien/jev-excel/blob/609f01d1984a3095776ac98ab7772ff8b2100a6c/src/functions.js), [`src/jev-core.js`](https://github.com/paulobrien/jev-excel/blob/609f01d1984a3095776ac98ab7772ff8b2100a6c/src/jev-core.js)) batch and parallelize calls; the VBA edition ([`vba/modJev.bas`](https://github.com/paulobrien/jev-excel/blob/609f01d1984a3095776ac98ab7772ff8b2100a6c/vba/modJev.bas)) calls one cell at a time. The key is kept in the add-in's browser storage, never in the workbook; an optional proxy is documented.

## Get started

Try it locally (Excel opens with the add-in sideloaded):

```sh
git clone https://github.com/paulobrien/jev-excel.git && cd jev-excel
npm install
npm run certs
npm start
# Excel: Home ▸ Jev → paste key → Test connection; then =JEV.ASK("choice", A2, "complaint", "question", "praise")
```

Each non-blank evaluated cell is a Jev request billed to your key.

## Examples and demos

- README *Worked examples* and *Function reference* (modes, rubric levels, errors).
- README *Deploy to Cloudflare* and *VBA edition* guides.

## Limits and data handling

Only the `text` argument (or `JEV.STATE` fields) and the question are sent (upstream statement). Unofficial. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit 609f01d1984a](https://github.com/paulobrien/jev-excel/tree/609f01d1984a3095776ac98ab7772ff8b2100a6c). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
