# DecisionOps (calibration and confidence-threshold certification for decision models, with a Jev provider)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Open-source reliability toolkit for decision models: from a decision contract (closed choice set, which choices may run automatically, path costs and miss severities) it measures calibration, certifies a confidence threshold before go-live and monitors it after; providers include hosted Jev, Laya and your own heads.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ellisgeeker/DecisionOps) |
| Maintainer | [ellisgeeker](https://github.com/ellisgeeker). Independently curated. |
| Format | Python CLI and library |
| Requirements | Python 3.12+; the `jev` extra and a TypeSafe API key for the Jev provider. |
| License | [Apache-2.0](https://github.com/ellisgeeker/DecisionOps/blob/e0fd33e98f549039f0886cd590abe9046a555e37/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decisionops/adapters/jev.py`](https://github.com/ellisgeeker/DecisionOps/blob/e0fd33e98f549039f0886cd590abe9046a555e37/src/decisionops/adapters/jev.py) at the pinned commit. |

## When to use

- Decide at what confidence a Jev routing or triage decision is safe to automate.
- Compare Jev with a local model on the same labelled cases.
- Mismatch: not on PyPI yet; install a tagged release from GitHub.

## How it works

`adapters/jev.py` uses the TypeSafe SDK to turn each labelled case into a Choice or binary question with criteria and records the returned probabilities for calibration. Integration evidence: [`src/decisionops/adapters/jev.py`](https://github.com/ellisgeeker/DecisionOps/blob/e0fd33e98f549039f0886cd590abe9046a555e37/src/decisionops/adapters/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install "decisionops[jev] @ git+https://github.com/ellisgeeker/DecisionOps.git@v0.1.1"
export TYPESAFE_API_KEY=...
decisionops eval data.jsonl --provider jev --limit 20
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ellisgeeker/DecisionOps#readme](https://github.com/ellisgeeker/DecisionOps#readme)
- Banking77 comparison example: [github.com/ellisgeeker/DecisionOps/tree/main/examples/banking77](https://github.com/ellisgeeker/DecisionOps/tree/main/examples/banking77)

## Limits and data handling

With the Jev provider, the cases you evaluate are sent to TypeSafe. Results are only as good as your labelled data and contract.

## Review and maintenance

Reviewed **2026-10-25** (Europe/Sofia) at [commit e0fd33e98f54](https://github.com/ellisgeeker/DecisionOps/tree/e0fd33e98f549039f0886cd590abe9046a555e37). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
