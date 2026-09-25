# jev-security-prioritization

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reproducible experiment: TypeSafe Jev prioritizes SCA/SAST findings using richer context than severity scores, compared to severity-only and points baselines via OpenRouter Decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/san3ncrypt3d/jev-security-prioritization) |
| Maintainer | [san3ncrypt3d](https://github.com/san3ncrypt3d). Independently curated. |
| Format | Python experiment scripts + blog write-up + report CLI. |
| Requirements | Python; OpenRouter access to `typesafe/jev-1.13`; dataset/fixtures per README. |
| License | [MIT](https://github.com/san3ncrypt3d/jev-security-prioritization/blob/e3e83d2444781de2d11bf09940c0a2439d68443d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use to **study Jev for vulnerability triage** when you already have reachability/context facts—not as a drop-in scanner replacement.

## How it works

Primary report compares Jev vs `b0_severity_only` vs `b1_context_points` on SCA/SAST sets with choice accuracy and urgency metrics (upstream tables).

## Get started

```sh
git clone https://github.com/san3ncrypt3d/jev-security-prioritization.git
cd jev-security-prioritization
git checkout e3e83d2444781de2d11bf09940c0a2439d68443d
python scripts/report.py primary
```

## Examples and demos

- README console sample for `scripts/report.py primary`.
- Blog: `blog/jev-security-prioritization.md`.

## Limits and data handling

Finding text/context go to OpenRouter/TypeSafe on live runs. Accuracy tables are upstream-reported. Prefer when verified facts already exist (per README guidance).

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit e3e83d2](https://github.com/san3ncrypt3d/jev-security-prioritization/tree/e3e83d2444781de2d11bf09940c0a2439d68443d). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [JevForge jev-security-sentinel](jev-security-sentinel.md).
