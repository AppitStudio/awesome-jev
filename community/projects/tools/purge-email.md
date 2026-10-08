# purge-email

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Gmail clean-up CLI: Gmail search does the cheap filtering (age, no attachments, not starred), then TypeSafe Jev judges whether each remaining message is likely personal correspondence, a receipt/financial record or an account/legal/medical/government record; `plan` only labels (`purge` below 0.1 keep-probability, `review` in between) and nothing moves to Trash until you run `apply --yes`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bhdoggett/purge-email) |
| Maintainer | [bhdoggett](https://github.com/bhdoggett). Independently curated. |
| Format | Node CLI (`npm run plan / apply / spam`) |
| Requirements | Node/npm, Gmail API OAuth desktop credentials (your own Google Cloud project), `JEV_API_KEY` or `TYPESAFE_API_KEY`. |
| License | The reviewed tree has **no LICENSE file** — listed as Source available; reuse terms are not granted until the maintainer adds a license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Clear a decade of mail without losing receipts, records or family messages.
- Review a CSV plan and Gmail labels before trashing anything.
- Mismatch: requires your own Gmail OAuth app; messages leave only to Gmail API and TypeSafe.

## How it works

[`core/decide.ts`](https://github.com/bhdoggett/purge-email/blob/040c66624b58ddd0c90ebb72cdb9f5342a9033a5/core/decide.ts) asks the keep questions per message and applies `--keep-at` / `--trash-below` thresholds; [`core/labels.ts`](https://github.com/bhdoggett/purge-email/blob/040c66624b58ddd0c90ebb72cdb9f5342a9033a5/core/labels.ts) manages the `purge` / `review` labels. Runs are resumable.

## Get started

Set up keys and OAuth, then plan on a small sample (README *Setup* / *Use*):

```sh
git clone https://github.com/bhdoggett/purge-email.git && cd purge-email
npm install
npm run auth                   # Gmail OAuth → token.json
npm run plan -- --limit 200    # label only
npm run apply                  # dry count; add -- --yes to trash
```

One Jev request per remaining message, billed to your TypeSafe key.

## Examples and demos

- README *What gets protected* and *Use* (CSV report in `reports/`).

## Limits and data handling

Message metadata and text go to TypeSafe; `.env`, `token.json` and reports are gitignored. Trash is reversible within Gmail's retention. No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 040c66624b58](https://github.com/bhdoggett/purge-email/tree/040c66624b58ddd0c90ebb72cdb9f5342a9033a5). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
