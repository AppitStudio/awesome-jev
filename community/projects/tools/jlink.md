# jlink

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Links records under a plain-English match rule using Jev Noul pair judgments, with local candidate blocking and match resolution.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/keltokhy/jlink) |
| Maintainer | [keltokhy](https://github.com/keltokhy) (Khaled Eltokhy); submitted from the maintainer's account with Codex assistance. |
| Format | Python library and CLI; `jlink` 0.1.0. |
| Requirements | Python 3.10+; live inference requires a configured TypeSafe or OpenRouter key and incurs provider charges. |
| Access | MIT-licensed source; bring your own provider key. No hosted service is included. |
| License | [MIT](https://github.com/keltokhy/jlink/blob/2c103536b92cea133cdafddc3e77c0e876c4a44e/LICENSE). |
| Disclosure | Maintainer self-submission, prepared and source-reviewed by Codex; no independent human review or directory endorsement is claimed. |

## When to use

Use it to link firm names, publication records, products, or other tabular entities when the match definition needs semantic judgment. Python, CLI, R, and Stata entry points are documented upstream.

## How it works

Jev receives the candidate pair and the user-defined identity rule as a Noul question. Local blocking determines which pairs are considered; match resolution applies thresholds and cardinality constraints. The reviewed version also has a normalized exact-match shortcut, so not every pair causes an API call.

Inspected implementation:

- [src/jlink/core.py](https://github.com/keltokhy/jlink/blob/2c103536b92cea133cdafddc3e77c0e876c4a44e/src/jlink/core.py#L178)
- [src/jlink/judge.py](https://github.com/keltokhy/jlink/blob/2c103536b92cea133cdafddc3e77c0e876c4a44e/src/jlink/judge.py#L26)
- [src/jlink/resolve.py](https://github.com/keltokhy/jlink/blob/2c103536b92cea133cdafddc3e77c0e876c4a44e/src/jlink/resolve.py#L1)

Default model identifiers at the reviewed revision: `jev-latest` on TypeSafe; `~typesafe/jev-latest` on OpenRouter; aliases can change.

## Get started

Install [uv](https://docs.astral.sh/uv/) and use the upstream instructions for other package managers.

```sh
git clone https://github.com/keltokhy/jlink.git
cd jlink
uv sync --group dev
# Offline tests use mocked provider answers.
uv run pytest -q tests/test_judge.py tests/test_resolve.py
```

For live use, configure `TYPESAFE_API_KEY` or `OPENROUTER_API_KEY` privately, following the [upstream README](https://github.com/keltokhy/jlink/blob/2c103536b92cea133cdafddc3e77c0e876c4a44e/README.md). Input text is sent to the chosen provider and calls may be billed.

The repository includes `examples/compustat_sample.csv` and `examples/patent_assignees.csv`. After configuring a provider key, follow the README toy linkage command (`uv run jev-link link ...`) to create a links CSV. Its `--on` fields, entity definition, blocking rules, and thresholds determine the output; inspect the resulting probabilities before accepting matches.

The example commands above were checked against source and documentation. The submission review ran only the tests listed below; it did not run a live provider workflow or independently test the published package installation.

## Examples and demos

- [Upstream usage examples](https://github.com/keltokhy/jlink/blob/2c103536b92cea133cdafddc3e77c0e876c4a44e/README.md) document the CLI and Python paths.
- [Tests](https://github.com/keltokhy/jlink/tree/2c103536b92cea133cdafddc3e77c0e876c4a44e/tests) provide runnable fixture-based checks.
- No separate hosted demo was verified for this submission.

## Limits and data handling

The selected comparison fields for candidate pairs are sent to TypeSafe or OpenRouter. Candidate generation and resolution run locally. Blocking can omit real matches, and model probabilities require evaluation on the intended data. Cached decisions support replay, but neither a cache nor a deterministic resolver establishes correctness. The optional exact shortcut is a code decision and should be considered when defining linkage rules.

## Review and maintenance

Reviewed on **2026-09-20** at [commit 2c10353](https://github.com/keltokhy/jlink/tree/2c103536b92cea133cdafddc3e77c0e876c4a44e). Codex inspected the public README, license, package manifest, Jev call sites, and relevant tests.

Ran `uv run --group dev pytest -q tests/test_judge.py tests/test_resolve.py`: **43 passed in 12.16s**. These offline fixture checks verify software behavior; they do not measure Jev accuracy, latency, or calibration. No live inference was performed for this listing.
