# riff

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Prose linter with ruff-style rule codes for writing: deterministic static rules plus optional TypeSafe Jev judgment rules for semantic style checks.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/scale-venture-partners/riff) |
| Maintainer | [Scale Venture Partners](https://github.com/scale-venture-partners). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package **`riff-lint` 0.1.0** (CLI `riff`). |
| Requirements | Python ≥ 3.11; `TYPESAFE_API_KEY` for live Jev rules (`tests/test_jev_live.py` / live lint paths). |
| License | [MIT](https://github.com/scale-venture-partners/riff/blob/70f203e5d356148970e9e1900af3969320b8088d/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline unit suite inspected; live TypeSafe not run on the review host. Distinct from [Sniff Test](snifftest.md) (countable rules + optional Jev after confirmation). |

## When to use

Use it when you want a **writing linter** with stable rule codes and an optional Jev backend for semantic judgments. Prefer [Sniff Test](snifftest.md) for a different prose-linter UX, or [jev-pref](jev-pref.md) for coding-agent preference checks on diffs.

## How it works

Static rules run locally. Jev-backed rules call TypeSafe System One for typed judgments about prose (see `tests/test_jev_unit.py` and live tests). Application code owns extraction, reporting, and which rule codes require a key.

## Get started

```sh
git clone https://github.com/scale-venture-partners/riff.git
cd riff
git checkout 70f203e5d356148970e9e1900af3969320b8088d
python3 -m pip install -e .
python3 -m pytest -q -k 'not live'
# Live Jev rules (not run here): set TYPESAFE_API_KEY per upstream docs
```

Live Jev rules send prose excerpts to TypeSafe and may incur charges.

## Examples and demos

- Offline on the review host: `pytest -q -k 'not live'` → **105 passed**, 7 deselected (live).
- Upstream CHANGELOG and CONTRIBUTING for rule authoring.

## Limits and data handling

Document text leaves the host when Jev rules run. Static rules need no key. Treat Jev style judgments as advisory, not ground truth.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 70f203e](https://github.com/scale-venture-partners/riff/tree/70f203e5d356148970e9e1900af3969320b8088d): **`riff-lint` 0.1.0**, MIT. AI-assisted source review of README, pyproject, LICENSE, Jev unit tests. Offline: `pytest -k 'not live'` → 105 passed. No live TypeSafe on the review host.

Related: [Sniff Test](snifftest.md), [jev-pref](jev-pref.md), [patdown](patdown.md).
