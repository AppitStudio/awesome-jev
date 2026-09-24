# Sureband

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Python library that wraps System One decision outputs (Jev, Laya, and related) with **split conformal prediction** so prediction sets carry a statistically targeted coverage rate from a labeled calibration set—without retraining the model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/TejaPriyan/Sureband) |
| Maintainer | [TejaPriyan](https://github.com/TejaPriyan). Independently curated. |
| Format | Python package (`sureband`) with examples and coverage tests. |
| Requirements | Python; labeled calibration examples; optional live System One calls for end-to-end demos. |
| License | [Apache-2.0](https://github.com/TejaPriyan/Sureband/blob/29048ed883ad6df28c57f9d77e910defdf8164f8/LICENSE) (GitHub SPDX may show `NOASSERTION`; LICENSE file is Apache-2.0). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline math/examples inspected via README; live Jev not run. |

## When to use

Use it when raw System One confidences are **not enough** and you need distribution-free coverage sets for routing/review. Prefer [jev-calibrate](jev-calibrate.md) / [jev-certify](jev-certify.md) for related calibration/certification tooling with different APIs.

## How it works

`Calibrator.fit` learns from `(raw_model_output, true_label)` pairs; `wrap` returns a prediction set, certainty flag, and target coverage. Auto-detects common typed-decision shapes (Choice/Noul/Score family).

## Get started

```sh
pip install sureband
# or
git clone https://github.com/TejaPriyan/Sureband.git
cd Sureband
git checkout 29048ed883ad6df28c57f9d77e910defdf8164f8
python examples/quickstart.py
```

## Examples and demos

- `examples/quickstart.py` (no provider required for the synthetic path).
- `tests/test_coverage.py` overconfident synthetic model check (not re-run here).

## Limits and data handling

Coverage guarantees assume exchangeability of calibration/test draws—read upstream caveats. Live model calls send whatever you pass as model output sources. No quality claim beyond the library's mathematical framing.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 29048ed](https://github.com/TejaPriyan/Sureband/tree/29048ed883ad6df28c57f9d77e910defdf8164f8). AI-assisted README + LICENSE inspection.

Related: [jev-calibrate](jev-calibrate.md), [jev-certify](jev-certify.md), [openjev-sglang](openjev-sglang.md).
