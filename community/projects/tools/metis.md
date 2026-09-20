# Metis

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Reusable GitHub Action and Python CLI/library that triage newly opened issues with TypeSafe Jev: category labels, missing-detail prompts, and optional follow-up comments—without inventing labels that do not exist in the repository.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Ayush0054/metis) |
| Maintainer | [Ayush0054 / Ayush Jha](https://github.com/Ayush0054). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **metis-triage 0.1.0** + composite GitHub Action `Ayush0054/metis` (stdlib-only runtime). |
| Requirements | Python ≥ 3.10 for local use; Action needs repository labels (`bug` / `enhancement` / `documentation` / `question` or a custom map) and secret `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Ayush0054/metis/blob/ea89e5c89d07b5075d75f9407ba023c87373b144/LICENSE). |

## When to use

Use it to auto-label and request missing details on new GitHub issues with calibrated Jev judgments. Prefer [Moongate](moongate.md) / [jev-pr-judge](jev-pr-judge.md) for PR-diff or PR-verdict workflows. Do not treat suggested labels as audited security triage.

## How it works

[`src/metis_triage/_triage.py`](https://github.com/Ayush0054/metis/blob/ea89e5c89d07b5075d75f9407ba023c87373b144/src/metis_triage/_triage.py) posts issue title/body to `https://api.typesafe.ai/v1/systemone`, validates category and missing-detail answers, then the Action/CLI may apply existing labels and post a fixed comment template. The library `classify_issue` path never talks to GitHub.

## Get started

```yaml
# .github/workflows/metis.yml on the default branch
name: Metis issue triage
on:
  issues:
    types: [opened]
permissions:
  issues: write
jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: Ayush0054/metis@ea89e5c89d07b5075d75f9407ba023c87373b144
        with:
          typesafe-api-key: ${{ secrets.TYPESAFE_API_KEY }}
```

Issue text is sent to TypeSafe and can incur charges. This listing did not run the Action or live inference.

## Examples and demos

- README library/`metis-triage classify` examples.
- [`action.yml`](https://github.com/Ayush0054/metis/blob/ea89e5c89d07b5075d75f9407ba023c87373b144/action.yml) inputs (`model` default `jev-latest`).

## Limits and data handling

Issue titles and bodies leave GitHub for TypeSafe. Suggested labels are recommendations; callers must ensure labels exist. Upstream PyPI publication may still be pending—install from the pinned checkout if needed.

## Review and maintenance

Reviewed on **2026-09-20** at [commit ea89e5c8](https://github.com/Ayush0054/metis/tree/ea89e5c89d07b5075d75f9407ba023c87373b144): **0.1.0**, MIT. AI-assisted source review of README, `_triage.py`, `action.yml`, `pyproject.toml`, and license. Action runs and live TypeSafe calls were not executed on the review host.

Related: [Moongate](moongate.md), [jev-pr-judge](jev-pr-judge.md), [SemDecide](semdecide.md).
