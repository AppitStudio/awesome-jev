# jev-evolve

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Self-improving agent experiments where every decision is a typed TypeSafe Jev question: evolve a policy from the agent’s own mistakes and report how much measured gain is selection noise versus real improvement.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/novaleolin/jev-evolve) |
| Maintainer | [novaleolin](https://github.com/novaleolin). Independently curated; this page is not an upstream submission or endorsement. |
| Format | Python package **jev-evolve** on PyPI (`pip install jev-evolve`); depends on `evalfloor`. |
| Requirements | Python ≥ 3.9. Live agent runs need TypeSafe (or documented backends). Optional `local` extras for torch/transformers. Offline unit tests need no API key. |
| License | [MIT](https://github.com/novaleolin/jev-evolve/blob/3a937d42f2e0a7fa19795ad0881f347a20a9defa/LICENSE). TypeSafe/provider usage has separate costs. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline pytest run; live evolution loops and billed Jev not run. |

## When to use

Use it when studying policy improvement with typed decisions and honest selection-bias reporting. Prefer simpler harnesses ([jev-harness](jev-harness.md), [daf-jev](daf-jev.md)) when you only need gates/evals without evolution. Distinct from open-weight lookalikes that imitate Jev’s interface without TypeSafe.

## How it works

Upstream API centers on `Policy`, typed `choice`/`noul` builders, `run_policy`, and measurement helpers (`permutation_sensitivity`, `Marginalized`, `confusions`, `point_accuracy`, `overconfident`, `cost`). Agents return tool results or `{jev_evolve.STOP: True}` to finish. Typed Jev answers drive control flow instead of free-form generated text; code owns execution and stop conditions. README documents comparative latency notes for `typesafe/jev-1.13` versus other backends (upstream measurements, not re-run here).

## Get started

```sh
pip install jev-evolve
python -c 'import jev_evolve; print(jev_evolve.__doc__[:80] if jev_evolve.__doc__ else "ok")'
```

Pinned review checkout:

```sh
git clone https://github.com/novaleolin/jev-evolve.git
cd jev-evolve
git checkout 3a937d42f2e0a7fa19795ad0881f347a20a9defa
pip install -e '.[dev]'
pytest -q
```

Follow upstream Quickstart for a live policy loop (incurs provider charges).

## Examples and demos

- Upstream README Quickstart / API sections and bilingual docs (`README.zh-CN.md`).
- [`tests/test_jev_evolve.py`](https://github.com/novaleolin/jev-evolve/blob/3a937d42f2e0a7fa19795ad0881f347a20a9defa/tests/test_jev_evolve.py).
- This listing ran `pytest -q`: **30 passed**. No live TypeSafe evolution run.

## Limits and data handling

Live runs send episode state and questions to the configured decision backend. Treat README benchmark tables as upstream reports. Optional local-model extras are separate from TypeSafe Jev.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 3a937d4](https://github.com/novaleolin/jev-evolve/tree/3a937d42f2e0a7fa19795ad0881f347a20a9defa): MIT; AI-assisted source review of README, LICENSE, package layout and tests; pytest **30 pass**. No live TypeSafe call.

Related: [jev-harness](jev-harness.md), [daf-jev](daf-jev.md), [jevals](jevals.md), [Responsible AI Harness](responsible-ai-harness.md).
