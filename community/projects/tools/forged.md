# forged

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Terminal tool that screens a PDF or image for signs of document fraud: it reads the file's metadata, renders pages to images, and asks Jev through Vercel AI Gateway for a fraud probability and the likelihood of each fixed fraud signal.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/colesmcintosh/forged) |
| Maintainer | [colesmcintosh](https://github.com/colesmcintosh). Independently curated. |
| Format | Bun CLI (TypeScript) |
| Requirements | Bun 1.3+, a Vercel AI Gateway API key. |
| License | [MIT](https://github.com/colesmcintosh/forged/blob/89777c466e07df59ddc439147737449adaeaf924/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/fraud-check.ts`](https://github.com/colesmcintosh/forged/blob/89777c466e07df59ddc439147737449adaeaf924/src/fraud-check.ts) at the pinned commit. |

## When to use

- Get a quick screening signal on an invoice, receipt or statement before a human looks closer.
- See how Jev's image input and probabilities behave on metadata plus page images.
- Mismatch: a screening signal, not a determination; the author says the probabilities are not calibrated for fraud.

## How it works

`src/document.ts` collects size, hash and PDF or EXIF/XMP metadata, pages are rendered with pdf.js (first 10 pages of a PDF), and `src/fraud-check.ts` sends them to `typesafe-ai/jev` via AI Gateway with a fixed set of signal questions, printing a verdict, reasons, or JSON. Integration evidence: [`src/fraud-check.ts`](https://github.com/colesmcintosh/forged/blob/89777c466e07df59ddc439147737449adaeaf924/src/fraud-check.ts).

## Get started

From the upstream README (not run on the review host):

```sh
bun install
cp .env.example .env   # add your AI Gateway API key
bun run check invoice.pdf
bun run check receipt.jpg --json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Sample output in the README.

## Limits and data handling

Document images and metadata go to Vercel AI Gateway and TypeSafe on your key; do not send documents you are not allowed to share. Jev's image input is experimental.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit 89777c466e07](https://github.com/colesmcintosh/forged/tree/89777c466e07df59ddc439147737449adaeaf924). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
