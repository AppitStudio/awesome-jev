# pytest-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pytest plugin for semantic assertions: ask whether text *holds* or *lacks* plain-language claims (plus choice/score helpers), judged by TypeSafe Jev instead of exact string matches.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/allebee/pytest-jev) |
| Maintainer | [allebee](https://github.com/allebee). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | PyPI package **`pytest-jev` 0.1.0** (pytest11 entry point `jev`). |
| Requirements | Python ≥ 3.10; depends on `pytest` and `typesafe-sdk`. Live judgments need `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY` (`--jev-provider` auto, typesafe, or openrouter). Offline unit tests use a fake Jev. |
| License | [MIT](https://github.com/allebee/pytest-jev/blob/aa163e448706477ec69998c1784fa6ccef157e84/LICENSE). TypeSafe/OpenRouter usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `uv run pytest`: **36 passed**. No live TypeSafe calls here. |

## When to use

Use it when LLM-app tests should check meaning (“the reply apologizes and offers a refund”) rather than brittle substrings. Prefer classical `assert` for exact contracts; prefer [Typed Evals](typed-evals.md) for larger eval harnesses outside pytest fixtures.

## How it works

[`src/pytest_jev/judge.py`](https://github.com/allebee/pytest-jev/blob/aa163e448706477ec69998c1784fa6ccef157e84/src/pytest_jev/judge.py) builds Noul/Choice/Score questions and calls `TypeSafeClient.system_one`. The `jev` fixture exposes `holds`, `lacks`, `expect`, `choice`, and `score`. [`plugin.py`](https://github.com/allebee/pytest-jev/blob/aa163e448706477ec69998c1784fa6ccef157e84/src/pytest_jev/plugin.py) wires CLI/ini options (threshold, model, provider, cache).

## Get started

```sh
uv tool install pytest-jev   # or: pip install pytest-jev
export TYPESAFE_API_KEY=your_key   # live tests only
# From source at the reviewed commit:
git clone https://github.com/allebee/pytest-jev.git
cd pytest-jev
git checkout aa163e448706477ec69998c1784fa6ccef157e84
uv sync --group dev
uv run pytest          # offline: fake Jev
```

Live assertions send the text under test (and optional context) to TypeSafe/OpenRouter and can incur charges.

## Examples and demos

- `examples/` — usage snippets.
- `tests/` — offline suite with a fake judge (no API key).
- README demo GIF and Jev-vs-LLM judge notes (vendor/author-reported; not re-run here).

## Limits and data handling

Judged text leaves the host on live runs. Thresholds and provider choice affect flakiness; cache options reduce repeat spend. This listing did not run live semantic assertions.

## Review and maintenance

Reviewed on **2026-09-21** at [commit aa163e4](https://github.com/allebee/pytest-jev/tree/aa163e448706477ec69998c1784fa6ccef157e84) (`pytest-jev` 0.1.0, MIT). AI-assisted source review of README, LICENSE, `judge.py`, `plugin.py`. Offline `uv run pytest`: 36 passed. No live provider calls.

Related: [Typed Evals](typed-evals.md), [daf-jev](daf-jev.md), [askjev](askjev.md).
