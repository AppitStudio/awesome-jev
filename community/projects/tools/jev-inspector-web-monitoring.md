# Jev-Inspector by ABK (Playwright site crawler and synthetic monitor where Jev judges whether each page state is an error)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Give it a root URL and it crawls the site in a real Chromium browser, de-duplicates pages, runs declared business flows with SLA limits, and captures DOM, console and network errors. Jev answers Noul, Choice and Score questions about each captured state. Reports, SQLite history and Prometheus metrics included; docs are in Chinese.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ABK3528/jev-inspector) |
| Maintainer | [ABK3528](https://github.com/ABK3528). Independently curated. |
| Format | Python CLI and package (Playwright) |
| Requirements | Python 3.10+, Playwright with Chromium, and a TypeSafe API key (`TYPESAFE_API_KEY` or `--api-key`). |
| License | [Apache-2.0](https://github.com/ABK3528/jev-inspector/blob/e0ded1dc91f1ccabd9d9214a8c88bc9522edade5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_inspector/decision/jev_client.py`](https://github.com/ABK3528/jev-inspector/blob/e0ded1dc91f1ccabd9d9214a8c88bc9522edade5/jev_inspector/decision/jev_client.py) at the pinned commit. |

## When to use

- Hunt for silent front-end failures across a large admin or SaaS site without writing an E2E script per page.
- Mismatch: sites you are not allowed to crawl.

## How it works

`jev_inspector/decision/jev_client.py` posts directly to `https://api.typesafe.ai/v1/systemone` to send page state with `is_error` Noul, an error-type Choice and a severity Score in one request. Integration evidence: [`jev_inspector/decision/jev_client.py`](https://github.com/ABK3528/jev-inspector/blob/e0ded1dc91f1ccabd9d9214a8c88bc9522edade5/jev_inspector/decision/jev_client.py).

## Get started

Install the requirements and Chromium, then point it at a site.

```sh
git clone https://github.com/ABK3528/jev-inspector.git && cd jev-inspector
pip install -r requirements.txt && playwright install chromium
python main.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/ABK3528/jev-inspector/blob/e0ded1dc91f1ccabd9d9214a8c88bc9522edade5/README.md](https://github.com/ABK3528/jev-inspector/blob/e0ded1dc91f1ccabd9d9214a8c88bc9522edade5/README.md)
- Report preview: [github.com/ABK3528/jev-inspector/blob/e0ded1dc91f1ccabd9d9214a8c88bc9522edade5/demo_report_preview.png](https://github.com/ABK3528/jev-inspector/blob/e0ded1dc91f1ccabd9d9214a8c88bc9522edade5/demo_report_preview.png)

## Limits and data handling

Page text, console and network snippets are sent to TypeSafe. Crawling logged-in sites needs stored credentials. Marketing-style README claims were not verified.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit e0ded1dc91f1](https://github.com/ABK3528/jev-inspector/tree/e0ded1dc91f1ccabd9d9214a8c88bc9522edade5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
