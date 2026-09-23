# jev-seo (AgriciDaniel)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Live website SEO audit from one homepage URL: crawl + 52 Search Central–tied rules + PageSpeed, with TypeSafe Jev page/site judgments, then ranked fixes as PDF/XLSX/Markdown. Distinct from the Rust [jev-seo](jev-seo.md) (AkashPriyadarshii) CLI/MCP.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AgriciDaniel/jev-seo) |
| Maintainer | [AgriciDaniel](https://github.com/AgriciDaniel) (Agrici Daniel). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python CLI **`jevseo` 0.1.1** + Claude Code skill (`SKILL.md`). |
| Requirements | Python ≥ 3.10; WeasyPrint/Pango for PDF; optional Playwright Chromium and DataForSEO for `--full`. Live Jev needs `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/AgriciDaniel/jev-seo/blob/55a184a3b0d09565a4c84268f725a47784e62528/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, pyproject, skill). Live crawl/Jev/DataForSEO runs were **not** executed on the review host. Upstream cost and evaluation tables are author-reported. |

## When to use

Use it when you want a one-URL live audit with typed Jev meaning judgments and client-ready PDF/XLSX. Prefer [jev-seo](jev-seo.md) (Akash) for a Rust SERP/GEO MCP without the PDF pipeline; prefer [SiteClarity](../apps/siteclarity.md) for hosted answer-readiness page audits.

## How it works

`bin/jevseo` crawls, applies deterministic rules, optionally calls PageSpeed and TypeSafe Jev (page type, intent, helpfulness, …), scores/ranks actions in code, and renders three report formats from one `audit.json`. `--full` adds paid DataForSEO visibility data. Budget caps and a cost ledger bound spend.

## Get started

```sh
git clone https://github.com/AgriciDaniel/jev-seo.git
cd jev-seo
git checkout 55a184a3b0d09565a4c84268f725a47784e62528
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # TYPESAFE_API_KEY optional; without it Jev sections are skipped
bin/jevseo doctor
python -m unittest discover -s tests -v   # offline, no keys
# Live (charges): bin/jevseo run https://example.com
```

## Examples and demos

- [`examples/claude-seo.md/`](https://github.com/AgriciDaniel/jev-seo/tree/55a184a3b0d09565a4c84268f725a47784e62528/examples/claude-seo.md) sample PDF/XLSX/Markdown (author run).
- `references/judgments.md`, `references/evaluation.md`, `references/method.md`.

## Limits and data handling

Live audits send page text/metadata to TypeSafe and may call Google PageSpeed / DataForSEO. Scores rank work; they do not predict rankings or traffic. This listing did not crawl live sites or spend on APIs.

## Review and maintenance

Reviewed on **2026-09-23** at [commit 55a184a](https://github.com/AgriciDaniel/jev-seo/tree/55a184a3b0d09565a4c84268f725a47784e62528) (**0.1.1**, MIT). AI-assisted source review of README, LICENSE, pyproject. No live TypeSafe/DataForSEO spend.

Related: [jev-seo](jev-seo.md), [SiteClarity](../apps/siteclarity.md), [deslop](deslop.md).
