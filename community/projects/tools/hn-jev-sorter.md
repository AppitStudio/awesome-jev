# HN Jev Sorter

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Chrome extension that sorts Hacker News comments into buckets you define (for example "it's overhyped" or "off topic") in real time, with TypeSafe Jev classifying each comment and showing its probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ritza-co/hn-jev-sorter) |
| Maintainer | [ritza-co](https://github.com/ritza-co). Independently curated. |
| Format | Chrome / Chromium extension (load unpacked) |
| Requirements | Chrome or another Chromium browser; TypeSafe API key. |
| License | [MIT](https://github.com/ritza-co/hn-jev-sorter/blob/bd823169dffbc136bcc267cd78390bf7f843cf24/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Skim a long Hacker News thread by theme.
- Mismatch: Hacker News only; each comment is a hosted Jev call.

## How it works

Each comment is sent to Jev as a choice over your buckets; the label and probability are drawn on the page and buckets can be browsed by probability. (Summarized from the upstream [README](https://github.com/ritza-co/hn-jev-sorter/blob/bd823169dffbc136bcc267cd78390bf7f843cf24/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Clone or download the repo, load it unpacked at `chrome://extensions`, and paste your TypeSafe key on the setup page.

## Limits and data handling

Comment text is sent to `api.typesafe.ai`; the key is stored in Chrome local extension storage. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit bd823169dffb](https://github.com/ritza-co/hn-jev-sorter/tree/bd823169dffbc136bcc267cd78390bf7f843cf24). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
