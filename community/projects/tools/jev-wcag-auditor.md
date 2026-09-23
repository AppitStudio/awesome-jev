# Jev WCAG Auditor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Web app that audits a public URL (including .gov pages): deterministic axe-core checks in headless Chromium plus optional TypeSafe Jev adjudication of judgement-call criteria, with confidence and an uncertainty band on the report.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ctrimm/jev-wcag-auditor) |
| Maintainer | [ctrimm](https://github.com/ctrimm). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Next.js app **jev-wcag-auditor 0.1.0** (axe-core + Python Jev bridge). |
| Requirements | Node for the Next app; Python bridge for Jev ([`lib/jev_bridge.py`](https://github.com/ctrimm/jev-wcag-auditor/blob/e6e0b110132d0eb291b40b6841fb9d451e601dfa/lib/jev_bridge.py)); TypeSafe key for Jev modes. |
| License | [MIT](https://github.com/ctrimm/jev-wcag-auditor/blob/e6e0b110132d0eb291b40b6841fb9d451e601dfa/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected (README, LICENSE, `lib/jev_audit.ts`). Live audits/TypeSafe were **not** run on the review host. Not legal advice. |

## When to use

Use it to combine axe-core with Jev pass/fail/needs-review on semantic criteria (alt text meaning, link purpose, headings, labels, language) for public pages. Prefer pure axe/lighthouse tooling when you do not want Jev; prefer [jev-seo](agrici-jev-seo.md) for SEO/GEO audits.

## How it works

axe-core runs in headless Chromium; [`lib/jev_audit.ts`](https://github.com/ctrimm/jev-wcag-auditor/blob/e6e0b110132d0eb291b40b6841fb9d451e601dfa/lib/jev_audit.ts) builds one Jev Choice batch over a semantic page snapshot (judgement or full modes). Findings combine into an interactive report and optional PDF. Law/standard baselines are cited from public references in the README.

## Get started

```sh
git clone https://github.com/ctrimm/jev-wcag-auditor.git
cd jev-wcag-auditor
git checkout e6e0b110132d0eb291b40b6841fb9d451e601dfa
npm install
npm run build
npm start   # http://localhost:3000
```

Pin for review: [commit e6e0b11](https://github.com/ctrimm/jev-wcag-auditor/tree/e6e0b110132d0eb291b40b6841fb9d451e601dfa). Jev modes send page snapshot text to TypeSafe and may incur charges.

## Examples and demos

- README screenshots (home, usa.gov-style report, print/PDF).
- axe-only mode needs no TypeSafe key.

## Limits and data handling

Not a substitute for assistive-technology testing or legal compliance opinions. Uncertainty band treats needs-review as fail (low) or pass (high). No live audit spend in this listing.

## Review and maintenance

Reviewed on **2026-09-23** at [commit e6e0b11](https://github.com/ctrimm/jev-wcag-auditor/tree/e6e0b110132d0eb291b40b6841fb9d451e601dfa) (**0.1.0**, MIT). AI-assisted source review. No live Chromium/Jev run.

Related: [jev-seo (AgriciDaniel)](agrici-jev-seo.md), [SiteClarity](../apps/siteclarity.md).
