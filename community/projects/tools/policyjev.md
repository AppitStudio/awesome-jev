# PolicyJEV

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Frozen-protocol comparison of zero-shot Jev with TF-IDF logistic regression and fine-tuned DistilBERT on Jigsaw toxic comments: Jev ranks worse (mean AP 0.527 against 0.583 and 0.677), and as a three-way allow/review/action policy it sends the most comments to human review.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AbbasRana001/PolicyJEV) |
| Maintainer | [AbbasRana001](https://github.com/AbbasRana001). Independently curated. |
| Format | Python research package with API, console front end, artifacts and Zenodo DOI |
| Requirements | Python with the listed requirements, Node for the console; a TypeSafe key to re-run Jev scoring. |
| License | [MIT](https://github.com/AbbasRana001/PolicyJEV/blob/c47471cf8782b180a094911fff97b22200e04e1c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/policyjev/jev/client.py`](https://github.com/AbbasRana001/PolicyJEV/blob/c47471cf8782b180a094911fff97b22200e04e1c/src/policyjev/jev/client.py) at the pinned commit. |

## When to use

- See an honest negative result for zero-shot Jev against trained baselines on a well-known moderation dataset.
- Reuse the policy analysis: thresholds fitted on validation and judged once on test.
- Mismatch: English toxic comments; three question sets written for this study.

## How it works

Each label is described as natural-language questions; `client.py` scores comments with Jev and caches the answers. Calibrated probabilities from all three systems feed the same allow, review or action policy, with paired bootstrap intervals and pre-registered measures. Integration evidence: [`src/policyjev/jev/client.py`](https://github.com/AbbasRana001/PolicyJEV/blob/c47471cf8782b180a094911fff97b22200e04e1c/src/policyjev/jev/client.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m pip install -r requirements.txt
python -m pip install -e .
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- DOI: [doi.org/10.5281/zenodo.23407397](https://doi.org/10.5281/zenodo.23407397)
- Policy results: `docs/results_policy.md`.

## Limits and data handling

Jigsaw comments (public, but offensive) go to TypeSafe on your key when re-scoring.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit c47471cf8782](https://github.com/AbbasRana001/PolicyJEV/tree/c47471cf8782b180a094911fff97b22200e04e1c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
