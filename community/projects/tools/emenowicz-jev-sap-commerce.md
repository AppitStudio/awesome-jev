# jev-sap-commerce

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

SAP Commerce (`jevintegration`) extension: TypeSafe Jev moderates product reviews and suggests categories with dry runs, audit records, and human fallback—never auto-writes categories.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Emenowicz/jev-sap-commerce) |
| Maintainer | [Emenowicz](https://github.com/Emenowicz). Independently curated. Not affiliated with TypeSafe or SAP. |
| Format | SAP Commerce Java extension + optional Claude Code skill. |
| Requirements | SAP Commerce 2211.x (tested 2211.46 JDK 17 and 2211-jdk21.17); `customerreview` + `catalog` extensions; TypeSafe API key for live calls. |
| License | [Apache-2.0](https://github.com/Emenowicz/jev-sap-commerce/blob/3428d685e65763787cd4d451911d36aecdf90db3/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Upstream synthetic eval tables not re-run. SAP Commerce server not available on the review host. |

## When to use

Use when an SAP Commerce shop should **gate review moderation and category suggestions** with calibrated Jev answers plus Backoffice audit. Prefer general moderation CLIs such as jevmod when you are not on SAP Commerce.

## How it works

Review flow asks four Nouls (abuse/spam/PII/on-topic) and applies thresholds; category flow walks a taxonomy with hierarchical classification keeping top paths. Cronjobs default to inert without triggers/key; each decision stores a read-only `JevJudgment` (per README).

## Get started

```sh
git clone https://github.com/Emenowicz/jev-sap-commerce.git
cd jev-sap-commerce
git checkout 3428d685e65763787cd4d451911d36aecdf90db3
# Install as SAP Commerce extension per upstream README; set TypeSafe key; run dry-run cronjobs on your data
```

## Examples and demos

- `eval/` synthetic multilingual review and category result TSVs (upstream-reported).
- README notes 22 offline tests on Commerce 2211.

## Limits and data handling

Review and product text reach TypeSafe when live. Without an API key, calls are skipped. Suggestions never mutate product categories automatically.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 3428d68](https://github.com/Emenowicz/jev-sap-commerce/tree/3428d685e65763787cd4d451911d36aecdf90db3). AI-assisted README and LICENSE inspection; Commerce integration tests not executed.
