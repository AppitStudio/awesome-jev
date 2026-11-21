# scikit-jev (scikit-learn estimators and feature transformer that turn Jev answers into probabilities)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

A pre-alpha scikit-learn integration: `JevTransformer` turns typed Noul, Choice and Score answers about text or JSON into feature columns, and `JevNoulClassifier`, `JevChoiceClassifier` and `JevScoreRegressor` expose `predict_proba` with validated probability distributions, so Jev drops into ordinary sklearn pipelines.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/engkimo/scikit-jev) |
| Maintainer | [engkimo](https://github.com/engkimo). Independently curated. |
| Format | Python library |
| Requirements | Python with scikit-learn; installed from GitHub (not on PyPI yet); `TYPESAFE_API_KEY` for live calls. The offline example needs no key. |
| License | [MIT](https://github.com/engkimo/scikit-jev/blob/05e3b97e5d106b1a3f0241090f22ba2524afb258/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/scikit_jev/backends/typesafe.py`](https://github.com/engkimo/scikit-jev/blob/05e3b97e5d106b1a3f0241090f22ba2524afb258/src/scikit_jev/backends/typesafe.py) at the pinned commit. |

## When to use

- Use Jev answers as calibrated features or classifiers inside existing scikit-learn pipelines.
- Mismatch: high-throughput batch scoring; calls are synchronous and sequential, with no built-in cache.

## How it works

`src/scikit_jev/backends/typesafe.py` wraps the official TypeSafe SDK lazily; each sample's questions go in one System One request, and every response is validated (missing or extra answers, bad distributions) before the next sample is sent. Integration evidence: [`src/scikit_jev/backends/typesafe.py`](https://github.com/engkimo/scikit-jev/blob/05e3b97e5d106b1a3f0241090f22ba2524afb258/src/scikit_jev/backends/typesafe.py).

## Get started

Install from GitHub and run the offline example, which uses hand-written responses and makes no network calls.

```sh
pip install "scikit-jev @ git+https://github.com/engkimo/scikit-jev.git"
git clone https://github.com/engkimo/scikit-jev && cd scikit-jev
python examples/offline_workflow.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Offline example: [github.com/engkimo/scikit-jev/blob/05e3b97e5d106b1a3f0241090f22ba2524afb258/examples/offline_workflow.py](https://github.com/engkimo/scikit-jev/blob/05e3b97e5d106b1a3f0241090f22ba2524afb258/examples/offline_workflow.py)
- README: [github.com/engkimo/scikit-jev/blob/05e3b97e5d106b1a3f0241090f22ba2524afb258/README.md](https://github.com/engkimo/scikit-jev/blob/05e3b97e5d106b1a3f0241090f22ba2524afb258/README.md)

## Limits and data handling

Pre-alpha MVP (status dated 2026-11-10). Each sample's text is sent to TypeSafe when fitting or predicting live.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 05e3b97e5d10](https://github.com/engkimo/scikit-jev/tree/05e3b97e5d106b1a3f0241090f22ba2524afb258). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
