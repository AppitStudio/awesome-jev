# gr-jev (paper code: asymmetric probability allocation when several choices are correct)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code and data for the arXiv paper "When Multiple Choices Are Correct: Asymmetric Probability Allocation in Jev and Other Decision Models": experiments showing that when two options are both correct, or five options are identical, Jev and other decision models split probability unevenly, which breaks threshold-based multi-select.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Rushab1/gr-jev) |
| Maintainer | [Rushab1](https://github.com/Rushab1). Independently curated. |
| Format | Python research code and paper sources |
| Requirements | Python 3.13 with uv; a TypeSafe API key and a Vercel AI Gateway key for the comparison models. |
| License | [MIT](https://github.com/Rushab1/gr-jev/blob/5a6161365b78848b7611fc237bfb5ebb77dc72db/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/grjev/constants.py`](https://github.com/Rushab1/gr-jev/blob/5a6161365b78848b7611fc237bfb5ebb77dc72db/src/grjev/constants.py) at the pinned commit. |

## When to use

- Check whether a multi-select threshold on Jev's probabilities will drop needed choices.
- Reproduce or extend the paper's experiments (a dry run prints the call count first).
- Mismatch: research findings, not a fix; saved model responses are not in the repository.

## How it works

`src/grjev/constants.py` sets the direct TypeSafe endpoint `https://api.typesafe.ai/v1/systemone` and a Vercel gateway route for other decision models; experiments send passage and ticket lists as Choice questions. Integration evidence: [`src/grjev/constants.py`](https://github.com/Rushab1/gr-jev/blob/5a6161365b78848b7611fc237bfb5ebb77dc72db/src/grjev/constants.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv sync && source .venv/bin/activate
cp .env.example .env   # TYPESAFE_API_KEY, VERCEL_GATEWAY_API_KEY
python scripts/run/run_experiment.py copied --dry-run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper: [arxiv.org/abs/2610.29217](https://arxiv.org/abs/2610.29217)
- README: [github.com/Rushab1/gr-jev#readme](https://github.com/Rushab1/gr-jev#readme)

## Limits and data handling

Experiment inputs go to TypeSafe and the gateway. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 5a6161365b78](https://github.com/Rushab1/gr-jev/tree/5a6161365b78848b7611fc237bfb5ebb77dc72db). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
