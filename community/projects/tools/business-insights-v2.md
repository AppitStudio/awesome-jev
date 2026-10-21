# Business Insights v2 (bi2)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

CLI and MCP server that finds a business's name, logo, merchant category code, head-office address, phone, email and social links from its website, rules first and Jev and Gemini last, with a status, confidence and evidence for every answer.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/haneeshraj/business-insights-v2) |
| Maintainer | [haneeshraj](https://github.com/haneeshraj). Independently curated. |
| Format | CLI and MCP server (Python, Playwright) |
| Requirements | Python with Playwright Chromium; optional Jev (`JEV_API_KEY` or keychain) and Gemini keys; rules-only mode needs no key. |
| License | [MIT](https://github.com/haneeshraj/business-insights-v2/blob/97ec88d222c909d490e34b1e6b48ede470ee3377/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/bi2/decide/jev.py`](https://github.com/haneeshraj/business-insights-v2/blob/97ec88d222c909d490e34b1e6b48ede470ee3377/src/bi2/decide/jev.py) at the pinned commit. |

## When to use

- Enrich merchant records for onboarding, KYB or transaction teams with checkable evidence.
- Run fast Jev-only enrichment (`--fast`) on a list of sites.
- Mismatch: accuracy figures are the author's own gold and test sets.

## How it works

bi2 reads each page once without a model (structured data, meta tags, logo candidates, contacts), then field specialists ask Jev (`src/bi2/decide/jev.py`, `https://api.typesafe.ai/v1/systemone`) to pick among candidates; Gemini handles what no candidate covers. Integration evidence: [`src/bi2/decide/jev.py`](https://github.com/haneeshraj/business-insights-v2/blob/97ec88d222c909d490e34b1e6b48ede470ee3377/src/bi2/decide/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "business-insights[mcp]"
playwright install chromium
bi2 keys set jev && bi2 doctor
bi2 analyze https://example.com/ --fast
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results table and architecture notes: [github.com/haneeshraj/business-insights-v2/blob/main/docs/architecture.md](https://github.com/haneeshraj/business-insights-v2/blob/main/docs/architecture.md)

## Limits and data handling

Page content is sent to TypeSafe and Google when keys are set. Cost and accuracy figures (about 3 model calls a site) are self-reported.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 97ec88d222c9](https://github.com/haneeshraj/business-insights-v2/tree/97ec88d222c909d490e34b1e6b48ede470ee3377). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
