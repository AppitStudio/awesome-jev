# System One Models — Getting Started

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Turns the six claims of TypeSafe's Jev launch post into runnable experiments where Jev, Claude (via TypeSafe's system-one-adapter) and keyword rules answer the same typed questions and code measures latency, tokens, cost and calibration.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gsaini/system-one-models-getting-started) |
| Maintainer | [gsaini](https://github.com/gsaini). Independently curated. |
| Format | Python experiments (`uv`) with offline tests |
| Requirements | Python 3.11+, `uv`; TypeSafe key for live Jev runs and an Anthropic key for the LLM arm (baselines and tests run offline). |
| License | [MIT](https://github.com/gsaini/system-one-models-getting-started/blob/50721f111b56d7ace7f4ab306330e556f450e288/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/systemone/arms.py`](https://github.com/gsaini/system-one-models-getting-started/blob/50721f111b56d7ace7f4ab306330e556f450e288/src/systemone/arms.py) at the pinned commit. |

## When to use

- Learn the Jev request shape and compare it with an LLM on the same questions.
- Reproduce calibration, parallelism and wiki-race experiments with bounded, opt-in live runs.
- Mismatch: learning project built the day after launch; prices and SDKs may have changed.

## How it works

All arms implement one `system_one(state, questions)` call: Jev through the official `typesafe-sdk`, Claude through the adapter with structured outputs, and keyword rules behind the real SDK via a mock transport; reports and raw numbers are saved under `runs/`. Integration evidence: [`src/systemone/arms.py`](https://github.com/gsaini/system-one-models-getting-started/blob/50721f111b56d7ace7f4ab306330e556f450e288/src/systemone/arms.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gsaini/system-one-models-getting-started.git && cd system-one-models-getting-started
uv sync
uv run systemone demo
uv run systemone calibration --live --yes   # needs TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Experiments: `src/systemone/experiments/` (demo, parallel, calibration, wikirace).

## Limits and data handling

Live runs send experiment prompts to TypeSafe and Anthropic on your keys; offline runs make no calls.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 50721f111b56](https://github.com/gsaini/system-one-models-getting-started/tree/50721f111b56d7ace7f4ab306330e556f450e288). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
