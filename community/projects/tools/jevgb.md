# JevGB

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Unofficial community extension of the listed grok-bot-jev: before Grok Bot does something expensive it calls `jevgb route` with a short JSON state and a router picks one action (e.g. hand off code work to Grok Build as a compact brief, or reuse a cached artifact), logging what each decision cost in a token ledger and dashboard; the default classifier is deterministic rules, with Jev used when `TYPESAFE_API_KEY` and `typesafe-sdk` are present.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SuperfastSimon/jevgb) |
| Maintainer | [SuperfastSimon](https://github.com/SuperfastSimon). Independently curated. |
| Format | Python CLI `jevgb` / `jgb` |
| Requirements | Python; optional `TYPESAFE_API_KEY` + `typesafe-sdk` for Jev (rules otherwise). |
| License | [MIT](https://github.com/SuperfastSimon/jevgb/blob/2924f4fd6b5888734ab75545a5f3fb02b8640b9b/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Measure whether routing actually saves tokens in an assistant workflow.
- Mismatch: dashboard screenshot uses simulated data; not affiliated with xAI.

## How it works

[`jevgb/jev_client.py`](https://github.com/SuperfastSimon/jevgb/blob/2924f4fd6b5888734ab75545a5f3fb02b8640b9b/jevgb/jev_client.py) asks Jev to choose an action; [`jevgb/local_classifier.py`](https://github.com/SuperfastSimon/jevgb/blob/2924f4fd6b5888734ab75545a5f3fb02b8640b9b/jevgb/local_classifier.py) is the rules fallback; [`jevgb/ledger.py`](https://github.com/SuperfastSimon/jevgb/blob/2924f4fd6b5888734ab75545a5f3fb02b8640b9b/jevgb/ledger.py) records costs.

## Get started

Install from source (README *Install*):

```sh
git clone https://github.com/SuperfastSimon/jevgb.git && cd jevgb
python -m venv .venv && .venv/bin/pip install -e ".[tokens]"
```

Jev routing bills your key; rules mode is free.

## Examples and demos

- Handoff format: [`docs/HANDOFF_GROK_BUILD.md`](https://github.com/SuperfastSimon/jevgb/blob/2924f4fd6b5888734ab75545a5f3fb02b8640b9b/docs/HANDOFF_GROK_BUILD.md).
- A/B notes: [`examples/ab_results.md`](https://github.com/SuperfastSimon/jevgb/blob/2924f4fd6b5888734ab75545a5f3fb02b8640b9b/examples/ab_results.md).

## Limits and data handling

Route state goes to TypeSafe in Jev mode. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 2924f4fd6b58](https://github.com/SuperfastSimon/jevgb/tree/2924f4fd6b5888734ab75545a5f3fb02b8640b9b). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
