# JevGym by Erik Lyngved (CLI that measures and compares prompts for Jev Choice questions with proper statistics)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Evaluates a Jev Choice prompt (instructions plus one description per option) on a labelled dataset and reports accuracy with a 95% Wilson interval, Brier score and log loss. Compares two prompts with a paired McNemar test against the run-to-run noise floor, guards the test split, and logs every run.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/elyngved/jevgym) |
| Maintainer | [elyngved](https://github.com/elyngved). Independently curated. |
| Format | Python CLI (`jevgym`, uv) |
| Requirements | Python 3.12+, uv, and a TypeSafe API key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/elyngved/jevgym/blob/62e78b88906cdbd4a8207a40a091f5373efab930/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevgym/jev.py`](https://github.com/elyngved/jevgym/blob/62e78b88906cdbd4a8207a40a091f5373efab930/jevgym/jev.py) at the pinned commit. |

## When to use

- Tune Jev Choice wording with numbers you can trust instead of eyeballing a few examples.
- Mismatch: Noul or Score questions, or automatic prompt optimisation (the optimizer is not in yet).

## How it works

`jevgym/jev.py` posts each row straight to `POST /v1/systemone` on `https://api.typesafe.ai`, checks the answer came from the pinned `jev-1.14.0`, and records the exact request and response. Integration evidence: [`jevgym/jev.py`](https://github.com/elyngved/jevgym/blob/62e78b88906cdbd4a8207a40a091f5373efab930/jevgym/jev.py).

## Get started

Sync dependencies, set your key, add a dataset and an arms file to a workspace, then run an eval.

```sh
git clone https://github.com/elyngved/jevgym.git && cd jevgym
uv sync
export TYPESAFE_API_KEY=...
uv run jevgym eval --arm a1 --split dev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/elyngved/jevgym/blob/62e78b88906cdbd4a8207a40a091f5373efab930/README.md](https://github.com/elyngved/jevgym/blob/62e78b88906cdbd4a8207a40a091f5373efab930/README.md)

## Limits and data handling

Dataset rows are sent to TypeSafe; runs show a cost estimate and stop above $1 without `--approve-usd`. Work in progress with no tagged release.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit 62e78b88906c](https://github.com/elyngved/jevgym/tree/62e78b88906cdbd4a8207a40a091f5373efab930). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
