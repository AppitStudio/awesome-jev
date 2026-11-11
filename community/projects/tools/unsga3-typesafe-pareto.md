# Unsga3 TypeSafe Pareto scoring (Jev pass over a U-NSGA-III front)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

U-NSGA-III multi-objective optimizer for .NET with an optional Python helper that asks Jev to score and keep/drop/review a sample of Pareto-front candidates next to the raw objectives.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AppSprout-dev/Unsga3) |
| Maintainer | [AppSprout-dev](https://github.com/AppSprout-dev). Independently curated. |
| Format | Library (.NET) plus Python helper, MIT |
| Requirements | A .NET build for the optimizer, Python 3 for `tools/typesafe-pareto`, and `TYPESAFE_API_KEY` for live calls (mock otherwise). |
| License | [MIT](https://github.com/AppSprout-dev/Unsga3/blob/478909d0c2b24674990da2d8f77a43a4a78d4599/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`tools/typesafe-pareto/score_pareto.py`](https://github.com/AppSprout-dev/Unsga3/blob/478909d0c2b24674990da2d8f77a43a4a78d4599/tools/typesafe-pareto/score_pareto.py) at the pinned commit. |

## When to use

- Add a semantic review layer on top of an evolutionary optimizer.
- Mismatch: additive helper; it does not change NSGA-III objectives or constraints.

## How it works

`tools/typesafe-pareto/score_pareto.py` sends one `/v1/systemone` request with Score and Choice questions per candidate; it runs in mock mode when no key is set, which is what CI uses. Integration evidence: [`tools/typesafe-pareto/score_pareto.py`](https://github.com/AppSprout-dev/Unsga3/blob/478909d0c2b24674990da2d8f77a43a4a78d4599/tools/typesafe-pareto/score_pareto.py).

## Get started

Run the smoke test in mock mode, then set the key for a live pass.

```sh
git clone https://github.com/AppSprout-dev/Unsga3.git && cd Unsga3
python tools/typesafe-pareto/score_pareto.py --smoke --force-mock
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/AppSprout-dev/Unsga3/blob/478909d0c2b24674990da2d8f77a43a4a78d4599/README.md](https://github.com/AppSprout-dev/Unsga3/blob/478909d0c2b24674990da2d8f77a43a4a78d4599/README.md)

## Limits and data handling

Candidate descriptions and objective vectors go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-11** (Europe/Sofia) at [commit 478909d0c2b2](https://github.com/AppSprout-dev/Unsga3/tree/478909d0c2b24674990da2d8f77a43a4a78d4599). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
