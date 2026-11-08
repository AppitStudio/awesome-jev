# Tiller AI AutoCat (Google Sheets transaction categorizer with a TypeSafe Jev option)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Apps Script for Tiller Finance Feeds in Google Sheets that cleans transaction descriptions and auto-categorizes them; supports TypeSafe Jev via OpenRouter, 16 transactions at a time.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sjogreen/tiller_ai_autocat) |
| Maintainer | [sjogreen](https://github.com/sjogreen). Independently curated. |
| Format | Google Apps Script (Apache-2.0) |
| Requirements | Google Sheets with Tiller Finance Feeds and an OpenRouter key. |
| License | [Apache-2.0](https://github.com/sjogreen/tiller_ai_autocat/blob/464f181122d6e981003662b0e8a6767c3678f6bc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ai_autocat.gs`](https://github.com/sjogreen/tiller_ai_autocat/blob/464f181122d6e981003662b0e8a6767c3678f6bc/ai_autocat.gs) at the pinned commit. |

## When to use

- Categorize personal finance transactions automatically.
- Keep categories constrained to your own list.
- Mismatch: originally a Gemini script; Jev is one supported model.

## How it works

`ai_autocat.gs` sets `typesafe/jev-1.13` at `https://openrouter.ai/api/alpha/decisions` and maps choice answers to your category list. Integration evidence: [`ai_autocat.gs`](https://github.com/sjogreen/tiller_ai_autocat/blob/464f181122d6e981003662b0e8a6767c3678f6bc/ai_autocat.gs).

## Get started

Copy the script into your Tiller sheet's Apps Script editor, set the key in Script Properties, and run it.

```sh
git clone https://github.com/sjogreen/tiller_ai_autocat.git && cd tiller_ai_autocat
export OPENROUTER_API_KEY=...
npm install && npm test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sjogreen/tiller_ai_autocat/blob/464f181122d6e981003662b0e8a6767c3678f6bc/README.md](https://github.com/sjogreen/tiller_ai_autocat/blob/464f181122d6e981003662b0e8a6767c3678f6bc/README.md)

## Limits and data handling

Transaction descriptions are sent to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 464f181122d6](https://github.com/sjogreen/tiller_ai_autocat/tree/464f181122d6e981003662b0e8a6767c3678f6bc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
