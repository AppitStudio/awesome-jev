# jev-verify (stillmarcus24)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Checks published Jev outputs against the Yurin confidence identity and flags fixtures that violate it (distinct from xienda/dsh-jev-verify).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/stillmarcus24/jev-verify) |
| Maintainer | [stillmarcus24](https://github.com/stillmarcus24). Independently curated. Not an endorsement. Identity credited to Stanislav Yurin / bernoulli.app. |
| Format | JavaScript CLI (`bin/jev-verify.cjs`). |
| Requirements | Node.js. Offline on published fixtures; no live TypeSafe calls required for identity checks. |
| License | [MIT](https://github.com/stillmarcus24/jev-verify/blob/2c92b900b5a2e128de65cb59f860e56b811de8ef/LICENSE). |
| Disclosure | AI-assisted catalog review. Source inspected (README, LICENSE). Fixture census **not** re-run on the review host. Distinct from [dsh-jev-verify](dsh-jev-verify.md). |

## When to use

Use it to audit published Choice/Score answers for consistency with the documented confidence identity. Prefer live labeled benches (dsh-jev-verify) when you need API round-trips.

## How it works

Recomputes confidence from returned probabilities via Yurin’s identity and reports residuals/violations for repo fixtures.

## Get started

```sh
git clone https://github.com/stillmarcus24/jev-verify.git
cd jev-verify
git checkout 2c92b900b5a2e128de65cb59f860e56b811de8ef
node bin/jev-verify.cjs   # see README for paths/flags
```

## Examples and demos

- README identity formulas and Yurin credit link.
- Census scripts under `scripts/` (documented upstream).

## Limits and data handling

Operates on published numeric answers; does not prove an upstream call occurred—only identity consistency. Author-reported residuals are not remeasured here.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 2c92b90](https://github.com/stillmarcus24/jev-verify/tree/2c92b900b5a2e128de65cb59f860e56b811de8ef) (MIT). AI-assisted source review. No live TypeSafe spend.

Related: [dsh-jev-verify](dsh-jev-verify.md), [jev-calibrate](jev-calibrate.md).
