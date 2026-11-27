# Site scan by Gabriel Parra (crawls a website for broken links and images, then has Jev label and rank each failure without hiding any)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Crawls a site within its own domain, checks every link and image (status, redirects, timeouts, DNS and TLS errors, image bytes, mixed content) and writes a Markdown, JSON or CSV report. Jev labels each failure as confirmed broken, likely false positive or needs review and gives it a severity; the HTTP results stay the source of truth. CLI with CI-friendly exit codes plus a small self-hosted web UI.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gabeparra/site-scan) |
| Maintainer | [Gabriel Parra](https://github.com/gabeparra). Independently curated. |
| Format | Python CLI + web UI |
| Requirements | Python 3.11+; a TypeSafe API key for real triage (without one a built-in mock triage runs). |
| License | [MIT](https://github.com/gabeparra/site-scan/blob/2806e1345451cd768fcfaebc97f886d6b63cd18e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/site_scan/triage/jev.py`](https://github.com/gabeparra/site-scan/blob/2806e1345451cd768fcfaebc97f886d6b63cd18e/src/site_scan/triage/jev.py) at the pinned commit. |

## When to use

- Site owners and CI pipelines that want broken links found and the bot-block false positives separated out.
- Mismatch: SEO or accessibility audits; it checks links and images only.

## How it works

`src/site_scan/triage/jev.py` sends a compact record of each failure to `https://api.typesafe.ai/v1/systemone` (default `jev-1.13.0`) with questions from `questions.json`; any error or unclear answer leaves the item as `needs_review`. Integration evidence: [`src/site_scan/triage/jev.py`](https://github.com/gabeparra/site-scan/blob/2806e1345451cd768fcfaebc97f886d6b63cd18e/src/site_scan/triage/jev.py).

## Get started

Install from source and scan a site.

```sh
git clone https://github.com/gabeparra/site-scan && cd site-scan
python3 -m venv .venv && source .venv/bin/activate
pip install -e ".[dev]"
export TYPESAFE_API_KEY=...
site-scan https://example.com --max-pages 50 --out reports/
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Triage questions: [github.com/gabeparra/site-scan/blob/main/src/site_scan/triage/questions.json](https://github.com/gabeparra/site-scan/blob/main/src/site_scan/triage/questions.json)

## Limits and data handling

Failed URLs, status codes and short error text go to TypeSafe; page content does not. It respects robots.txt and refuses private network targets by default; scan only sites you are allowed to crawl. Headless browser mode needs a package that is not published yet.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 2806e1345451](https://github.com/gabeparra/site-scan/tree/2806e1345451cd768fcfaebc97f886d6b63cd18e). Inspected the README, LICENSE and `src/site_scan/triage/jev.py` at the pinned commit; nothing was installed or run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
