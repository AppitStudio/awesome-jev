# decision-eval

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark harness for zero-shot decision models (choice / noul / score): accuracy, calibration, latency, and cost across suites, with a hosted Jev backend on OpenRouter (`typesafe/jev-1.14`) alongside local Laya/GLiNER and OpenAI Decisions.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NISH1001/decision-eval) |
| Maintainer | [NISH1001](https://github.com/NISH1001). Independently curated. |
| Format | Python CLI (`uvx` / `uv run`) |
| Requirements | Python + uv; OPENROUTER_API_KEY for Jev; optional extras for local backends. |
| License | [MIT](https://github.com/NISH1001/decision-eval/blob/d8a7dd4e073ba7f6c9e75792d4d07a9386cded55/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision_eval/backends.py`](https://github.com/NISH1001/decision-eval/blob/d8a7dd4e073ba7f6c9e75792d4d07a9386cded55/src/decision_eval/backends.py) at the pinned commit. |

## When to use

- Compare Jev to other decision models on identical byte requests.
- Need published suite results with cost and calibration metrics.
- Mismatch: eval harness; suites may need extra data downloads (ReDef).

## How it works

`backends.py` implements `jev_backend` against OpenRouter's decisions API for `typesafe/jev-1.14`, recording snapshot ids, tokens, and cost beside other backends. Integration evidence: [`src/decision_eval/backends.py`](https://github.com/NISH1001/decision-eval/blob/d8a7dd4e073ba7f6c9e75792d4d07a9386cded55/src/decision_eval/backends.py).

## Get started

Use uvx from GitHub or clone; set OPENROUTER_API_KEY; run a suite with `--backend jev`.

```sh
R="git+https://github.com/NISH1001/decision-eval"
uvx --from "$R" decision-eval suites
# OPENROUTER_API_KEY=... uvx --from "$R" decision-eval run --suite stem-synth --backend jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- [nishparadox.com/research/decision-eval/](https://nishparadox.com/research/decision-eval/)
- committed results/*_jev.csv

## Limits and data handling

Hosted Jev bills OpenRouter/TypeSafe. Some suites need external data. Results are author-published.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit d8a7dd4e073b](https://github.com/NISH1001/decision-eval/tree/d8a7dd4e073ba7f6c9e75792d4d07a9386cded55). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
