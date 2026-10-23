# jevcells (Jev formulas for Google Sheets)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Google Sheets add-on with formulas that ask Jev about every row of a range: probability, yes/no at a threshold, choice, score, multi-label tags, value picking, weighted ranking across criteria and matching rows between two ranges.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/saembit/jevcells) |
| Maintainer | [saembit](https://github.com/saembit). Independently curated. |
| Format | Google Apps Script add-on |
| Requirements | Google Sheets; a TypeSafe API key. |
| License | [MIT](https://github.com/saembit/jevcells/blob/b28dae9332e3da98b16e11736d23fe23bf8218da/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/client.js`](https://github.com/saembit/jevcells/blob/b28dae9332e3da98b16e11736d23fe23bf8218da/src/client.js) at the pinned commit. |

## When to use

- Tag, triage or rank spreadsheet rows without writing code.
- Match records between two sheets by meaning.
- Mismatch: not on the Workspace Marketplace yet; installed by pasting files into Apps Script.

## How it works

`src/client.js` sends batched requests to `https://api.typesafe.ai/v1/systemone` with `jev-latest`. `JEV_RANK` gets one score per item per criterion and applies your weights in code, so changing a weight does not need a new call. Integration evidence: [`src/client.js`](https://github.com/saembit/jevcells/blob/b28dae9332e3da98b16e11736d23fe23bf8218da/src/client.js).

## Get started

From the upstream README (not run on the review host):

```sh
# In a sheet: Extensions > Apps Script, paste the files from dist/
=JEV_CHOICE(A2:A50, "billing, technical, sales")
=JEV_TAGS(A2:A50, "urgent, billing, bug", 0.5)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Formula reference in the README: [github.com/saembit/jevcells#readme](https://github.com/saembit/jevcells#readme)

## Limits and data handling

Cell contents in the referenced ranges are sent to TypeSafe. Not affiliated with TypeSafe or Google.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit b28dae9332e3](https://github.com/saembit/jevcells/tree/b28dae9332e3da98b16e11736d23fe23bf8218da). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
