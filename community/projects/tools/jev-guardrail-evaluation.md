# Jev Guardrail Evaluation (notebooks and CLI testing Jev as an under-200 ms prompt-injection guard)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Hands-on learning path that measures Jev as an inline prompt-injection and safety layer, starting with one reproducible run and adding datasets, comparisons and latency measurements.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/FabG/jev-guardrail-evaluation) |
| Maintainer | [FabG](https://github.com/FabG). Independently curated. |
| Format | Python notebooks + CLI (no license file) |
| Requirements | Python, Jupyter, and `TYPESAFE_API_KEY`. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_eval/jev.py`](https://github.com/FabG/jev-guardrail-evaluation/blob/2a0ad6784f3c2f804db2b033c4c564d2d497ce1b/src/jev_eval/jev.py) at the pinned commit. |

## When to use

- Measure Jev latency and accuracy as a guardrail.
- Learn Jev step by step in notebooks.
- Mismatch: no license file; ask the author before reuse.

## How it works

`jev_eval/jev.py` wraps `typesafe_sdk.TypeSafeClient` with `Noul`/`Choice` questions; `cli.py` runs live evaluations and the notebooks cover Hugging Face datasets and benchmark publishing. Integration evidence: [`src/jev_eval/jev.py`](https://github.com/FabG/jev-guardrail-evaluation/blob/2a0ad6784f3c2f804db2b033c4c564d2d497ce1b/src/jev_eval/jev.py).

## Get started

Clone, copy `.env.example`, set `TYPESAFE_API_KEY`, and open `notebooks/00_jev_first_decision.ipynb`.

```sh
git clone https://github.com/FabG/jev-guardrail-evaluation.git && cd jev-guardrail-evaluation
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/FabG/jev-guardrail-evaluation/blob/2a0ad6784f3c2f804db2b033c4c564d2d497ce1b/README.md](https://github.com/FabG/jev-guardrail-evaluation/blob/2a0ad6784f3c2f804db2b033c4c564d2d497ce1b/README.md)

## Limits and data handling

Evaluation texts are sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 2a0ad6784f3c](https://github.com/FabG/jev-guardrail-evaluation/tree/2a0ad6784f3c2f804db2b033c4c564d2d497ce1b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
