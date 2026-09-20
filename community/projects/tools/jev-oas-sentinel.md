# jev-oas-sentinel

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that compares two OpenAPI documents with deterministic structural checks plus TypeSafe Jev semantic questions about changed contract meaning. Jev never rewrites the spec; Python policy decides pass / review / block.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ShuhanSun/jev-oas-sentinel) |
| Maintainer | [ShuhanSun](https://github.com/ShuhanSun). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package / CLI **jev-oas-sentinel 0.5.0** (uv/pipx-oriented). |
| Requirements | Python 3.9+ (uv recommended); TypeSafe API key for live semantic evaluation. `--no-jev` runs structural checks only. |
| License | [Apache-2.0](https://github.com/ShuhanSun/jev-oas-sentinel/blob/d04bbb2f522cf88ca941b4a21b028388167f0819/LICENSE). |

## When to use

Use it when OpenAPI structural diffs miss behavioral breaks (defaults, pagination, auth/error semantics, example drift). Prefer ordinary OpenAPI diff tools for pure schema shape, or [Moongate](moongate.md) for general PR text rules unrelated to OpenAPI.

## How it works

1. Deterministic loaders resolve local `$ref`s (remote refs rejected; optional `--ref-root`).
2. [`src/jev_oas_sentinel/jev.py`](https://github.com/ShuhanSun/jev-oas-sentinel/blob/d04bbb2f522cf88ca941b4a21b028388167f0819/src/jev_oas_sentinel/jev.py) calls `https://api.typesafe.ai/v1/systemone` (default model `jev-1.13.0`) for bounded semantic decisions (change kind, dimension, migration burden, …).
3. Report/policy code maps probabilities to advisory or blocking findings. Traces redact sensitive key names.

Advisory mode is the default in the upstream MVP.

## Get started

```sh
git clone https://github.com/ShuhanSun/jev-oas-sentinel.git
cd jev-oas-sentinel
git checkout d04bbb2f522cf88ca941b4a21b028388167f0819
uv tool install --editable .
jev-oas-sentinel compare \
  --base examples/base-openapi.yaml \
  --head examples/head-openapi.yaml \
  --no-jev
```

Omit `--no-jev` and set a TypeSafe key for semantic evaluation (provider charges may apply). This listing did not call the API.

## Examples and demos

- Example OpenAPI pair under `examples/`.
- Offline **`PYTHONPATH=src python -m pytest -q`**: **30 passed** on the review host (PyYAML installed). Live Jev compares were not run.

## Limits and data handling

Changed description/example/default text can be sent to TypeSafe. Remote `$ref` fetch is refused. Multi-file trees need an explicit trusted `--ref-root` when schemas live outside the spec directory. MVP scope: JSON and standards-compliant safe YAML.

## Review and maintenance

Reviewed on **2026-09-20** at [commit d04bbb2](https://github.com/ShuhanSun/jev-oas-sentinel/tree/d04bbb2f522cf88ca941b4a21b028388167f0819): **0.5.0**, Apache-2.0. AI-assisted source review of `jev.py`, CLI, README, and license. **`pytest`**: **30 passed**. No live TypeSafe semantic compare.

Related: [Moongate](moongate.md), [Supercov](supercov.md), [Jev Review (Dev Agrawal)](jev-review-devagrawal.md).
