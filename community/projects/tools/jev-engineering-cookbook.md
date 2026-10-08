# Jev Engineering Cookbook

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Curriculum of Jupyter notebook recipes for building with Jev one bounded decision at a time — state in, typed `choice` / `noul` / `score` questions out — with offline fixture runs that need no API key, a live mode, and explicit provenance rules separating synthetic pipeline checks from measured Jev results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Jev-Engineering/cookbook) |
| Maintainer | [Jev-Engineering](https://github.com/Jev-Engineering). Independently curated. |
| Format | Notebook repository (`recipes/NN-*/notebook.ipynb`) |
| Requirements | Python 3.10+ and git; a TypeSafe key only for live mode. |
| License | [MIT](https://github.com/Jev-Engineering/cookbook/blob/67a23342c5ec10c7fae01622f130cb5af8bb8eb9/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Teach a team typed-decision design with runnable examples.
- Reuse recipe structure (fixtures, replay keys, thresholds) in your own evals.
- Mismatch: many catalog rows are planned and marked coming soon; synthetic metrics are not Jev results.

## How it works

Each recipe pairs a notebook with fixtures (e.g. [`recipes/01-sentiment-classification`](https://github.com/Jev-Engineering/cookbook/blob/67a23342c5ec10c7fae01622f130cb5af8bb8eb9/recipes/01-sentiment-classification/README.md)); [`docs/offline-and-live.md`](https://github.com/Jev-Engineering/cookbook/blob/67a23342c5ec10c7fae01622f130cb5af8bb8eb9/docs/offline-and-live.md) defines the modes. Distinct from other projects named "Jev cookbook".

## Get started

Run offline (README *Quick start*):

```sh
git clone https://github.com/Jev-Engineering/cookbook.git && cd cookbook
python -m venv .venv && . .venv/bin/activate
pip install -e ".[dev]"
```

Offline runs are free; live mode bills your TypeSafe key.

## Examples and demos

- Getting started: [`docs/getting-started.md`](https://github.com/Jev-Engineering/cookbook/blob/67a23342c5ec10c7fae01622f130cb5af8bb8eb9/docs/getting-started.md).
- Glossary: [`docs/glossary.md`](https://github.com/Jev-Engineering/cookbook/blob/67a23342c5ec10c7fae01622f130cb5af8bb8eb9/docs/glossary.md).

## Limits and data handling

Live mode sends recipe inputs to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 67a23342c5ec](https://github.com/Jev-Engineering/cookbook/tree/67a23342c5ec10c7fae01622f130cb5af8bb8eb9). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
