# jev-compaction (Waxmell114514)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Context compaction library (`jevctx`) where Jev **only scores**—never rewrites—so retained lines stay original, elided text is recoverable byte-for-byte, and prompt-cache prefixes can survive. Distinct from [fast-jev-compaction](fast-jev-compaction.md) / [jev-compact](jev-compact.md) / omp variants.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Waxmell114514/jev-compaction) |
| Maintainer | [Waxmell114514](https://github.com/Waxmell114514). Independently curated. |
| Format | Python package `jevctx` + HTTP sidecar + OpenCode plugin; offline `demo.py`. |
| Requirements | Python; optional TypeSafe Jev for live scoring; `uv` recommended. |
| License | [MIT](https://github.com/Waxmell114514/jev-compaction/blob/65628ad76beace7cfdc9d9b137f93164b9ac31f5/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline demo path not executed here; SWE-bench figures are upstream-reported. |

## When to use

Use it when agents drown in tool output and you want **admission/recall without summary invention**. Prefer harness-specific compaction plugins when you need a drop-in for one agent only.

## How it works

Admission profiles segments via Jev; pointers replace low-value runs; `expand`/`recall` recover text; supersession and work-area rewrites are cost-aware. See [`jevctx/pipeline.py`](https://github.com/Waxmell114514/jev-compaction/blob/65628ad76beace7cfdc9d9b137f93164b9ac31f5/jevctx/pipeline.py) and [`jevctx/jev.py`](https://github.com/Waxmell114514/jev-compaction/blob/65628ad76beace7cfdc9d9b137f93164b9ac31f5/jevctx/jev.py).

## Get started

```sh
git clone https://github.com/Waxmell114514/jev-compaction.git
cd jev-compaction
git checkout 65628ad76beace7cfdc9d9b137f93164b9ac31f5
uv venv .venv && uv pip install --python .venv/bin/python -e '.[dev]'
.venv/bin/python demo.py   # offline tour; no API key
```

## Examples and demos

- Project site: [waxmell114514.github.io/jev-compaction](https://waxmell114514.github.io/jev-compaction/)
- `RESULTS.md` SWE-bench notes; `integrations/opencode/`.

## Limits and data handling

Live scoring sends segments to TypeSafe. Upstream SWE-bench metrics were not re-run. Quarantine/injection claims are upstream-reported.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit 65628ad](https://github.com/Waxmell114514/jev-compaction/tree/65628ad76beace7cfdc9d9b137f93164b9ac31f5). AI-assisted README + `jevctx` layout inspection.

Related: [fast-jev-compaction](fast-jev-compaction.md), [jev-compact](jev-compact.md), [omp-jev-compaction](omp-jev-compaction.md).
