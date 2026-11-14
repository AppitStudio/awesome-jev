# Jev GPU Tests (Python library where Jev assesses whether a pull request needs GPU tests or can skip them)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small dependency-free library extracted from the maintainer's PR Labeler: given PR metadata, the full changed-file list and the complete diff, Jev answers two independent assessments — "needs GPU tests" and "can skip GPU tests" — and decision rules turn them into a result, so CI can save GPU runs on changes that cannot affect GPU behaviour.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tohtana/jev-gpu-tests) |
| Maintainer | [tohtana](https://github.com/tohtana). Independently curated. |
| Format | Python library (MIT) |
| Requirements | Python 3.10+ and a `JEV_API_KEY` (TypeSafe). |
| License | [MIT](https://github.com/tohtana/jev-gpu-tests/blob/ede62f220af380060f316af45c3579f33abb001a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_gpu_tests/classifier.py`](https://github.com/tohtana/jev-gpu-tests/blob/ede62f220af380060f316af45c3579f33abb001a/jev_gpu_tests/classifier.py) at the pinned commit. |

## When to use

- Decide in CI whether an expensive GPU test job is needed for a given PR.
- Mismatch: repos without a GPU test split, or PRs whose full diff you cannot fetch.

## How it works

`jev_gpu_tests/classifier.py` posts to `https://api.typesafe.ai/v1/systemone` with model `jev-1.14.0`; the library checks that the supplied diff is complete before asking. Integration evidence: [`jev_gpu_tests/classifier.py`](https://github.com/tohtana/jev-gpu-tests/blob/ede62f220af380060f316af45c3579f33abb001a/jev_gpu_tests/classifier.py).

## Get started

Install from GitHub, set your key, and call `evaluate` with PR data you fetched yourself.

```sh
python3 -m pip install "git+https://github.com/tohtana/jev-gpu-tests.git"
export JEV_API_KEY=...
# see README: evaluate(pull_request_state(pr, files, diff), SKIP_GPU)
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/tohtana/jev-gpu-tests/blob/ede62f220af380060f316af45c3579f33abb001a/README.md](https://github.com/tohtana/jev-gpu-tests/blob/ede62f220af380060f316af45c3579f33abb001a/README.md)

## Limits and data handling

PR titles, descriptions and complete diffs are sent to TypeSafe on your key. The library does not fetch GitHub data. Not published to PyPI.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit ede62f220af3](https://github.com/tohtana/jev-gpu-tests/tree/ede62f220af380060f316af45c3579f33abb001a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
