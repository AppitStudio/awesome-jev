# jevtriage

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

GitHub Action and Python CLI that triage a pull request with one TypeSafe Jev Choice (`ready` / `needs_review` / `risky`), then gate exit codes on official `ChoiceAnswer.confidence` (fail-closed for low-confidence `ready`).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sathariels/jevtriage) |
| Maintainer | [sathariels](https://github.com/sathariels). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | PyPI package **`jevtriage` 0.1.0** + composite GitHub Action `sathariels/jevtriage` (`action.yml`). |
| Requirements | Python ≥ 3.10; `typesafe-sdk`. Live triage needs `TYPESAFE_API_KEY` and a pinned model (`TYPESAFE_DEFAULT_MODEL` or Action `model`). Optional `GITHUB_TOKEN` for PR fetch / `jev:*` labels. |
| License | [MIT](https://github.com/sathariels/jevtriage/blob/6aee509e9a8b99adfb847434d7e4aacfae0dac71/LICENSE). TypeSafe usage billed separately. |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Offline `pytest`: **50 passed**. No live TypeSafe or Action runs. Distinct from [Metis](metis.md) (issue labels) and [jev-ci-selector](jev-ci-selector.md) (which CI jobs apply). |

## When to use

Use it when every PR should get a merge-readiness gate with typed exit codes and optional labels. Prefer [Metis](metis.md) for new-issue category triage; prefer [jev-review-action](jev-review-action.md) for template review comments rather than a ready/risky gate.

## How it works

[`src/jevtriage/questions.py`](https://github.com/sathariels/jevtriage/blob/6aee509e9a8b99adfb847434d7e4aacfae0dac71/src/jevtriage/questions.py) builds one official `Choice` with three criteria. [`client.py`](https://github.com/sathariels/jevtriage/blob/6aee509e9a8b99adfb847434d7e4aacfae0dac71/src/jevtriage/client.py) calls System One with `TYPESAFE_API_KEY` only. [`gate.py`](https://github.com/sathariels/jevtriage/blob/6aee509e9a8b99adfb847434d7e4aacfae0dac71/src/jevtriage/gate.py) maps verdict + confidence to exit `0` / `1` / `2` (low-confidence `ready` becomes `needs_review`). The Action installs the PyPI pin and can apply labels.

## Get started

```yaml
# .github/workflows/pr-triage.yml
name: pr-triage
on: pull_request
permissions:
  contents: read
  pull-requests: write
jobs:
  triage:
    runs-on: ubuntu-latest
    steps:
      - uses: sathariels/jevtriage@v0.1.0
        env:
          TYPESAFE_API_KEY: ${{ secrets.TYPESAFE_API_KEY }}
        with:
          model: jev-1.13.0
          apply-labels: true
```

From source at the reviewed commit:

```sh
git clone https://github.com/sathariels/jevtriage.git
cd jevtriage
git checkout 6aee509e9a8b99adfb847434d7e4aacfae0dac71
pip install -e '.[dev]'
pytest -q
```

Live Action/CLI runs send PR title/body/diff excerpts to TypeSafe and can incur charges. Unit tests mock the client.

## Examples and demos

- README Action and CLI examples; `fixtures/` replay shapes for jevcheck-friendly contracts.
- Offline tests under `tests/` (executed for this listing).

## Limits and data handling

PR text and diffs leave GitHub for TypeSafe on live runs. Labels are caller-controlled. Do not treat `ready` as a security audit. This listing did not run the Action or live inference.

## Review and maintenance

Reviewed on **2026-09-21** at [commit 6aee509](https://github.com/sathariels/jevtriage/tree/6aee509e9a8b99adfb847434d7e4aacfae0dac71): `jevtriage` **0.1.0**, MIT. AI-assisted source review of README, LICENSE, `questions.py`, `gate.py`, `client.py`, `action.yml`. Offline `pytest`: 50 passed. No live TypeSafe calls.

Related: [Metis](metis.md), [jev-ci-selector](jev-ci-selector.md), [jev-debtgate](jev-debtgate.md).
