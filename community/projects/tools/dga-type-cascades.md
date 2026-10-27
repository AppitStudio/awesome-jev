# Type Cascades for DGA Detection (paper code comparing 13 detectors, including Jev, on unseen malware families)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, data and results for a paper on detecting malware domain-generation algorithms on 27 family groups unseen in training, judged on F1, false-positive rate and time per domain together: a fast detector decides most domains and only doubtful ones reach a transformer; variants ask a decision model (d1-3B or Jev) instead of the dictionary rule or as a doubtful-case judge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/reypapin/dga-type-cascades) |
| Maintainer | [reypapin](https://github.com/reypapin). Independently curated. |
| Format | Python research code and paper |
| Requirements | Python; an OpenRouter key only to rerun the Jev variants. |
| License | [MIT](https://github.com/reypapin/dga-type-cascades/blob/9666ae5ddd2803bda02edb50c5cdcf19668f4ad9/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`extension/scripts/run_jev_openrouter.py`](https://github.com/reypapin/dga-type-cascades/blob/9666ae5ddd2803bda02edb50c5cdcf19668f4ad9/extension/scripts/run_jev_openrouter.py) at the pinned commit. |

## When to use

- Compare cascade designs for DGA detection across accuracy, false alarms and latency.
- Mismatch: the Jev variants were designed after the test; results are the authors'.

## How it works

`extension/scripts/run_jev_openrouter.py` sends doubtful domains to `typesafe/jev-1.14` through OpenRouter; `extension/scripts/posthoc_jev.py` sets the thresholds. Integration evidence: [`extension/scripts/run_jev_openrouter.py`](https://github.com/reypapin/dga-type-cascades/blob/9666ae5ddd2803bda02edb50c5cdcf19668f4ad9/extension/scripts/run_jev_openrouter.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/reypapin/dga-type-cascades && cd dga-type-cascades
# see the README for the experiment steps
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/reypapin/dga-type-cascades#readme](https://github.com/reypapin/dga-type-cascades#readme)

## Limits and data handling

Domain names go to OpenRouter and TypeSafe when the Jev variants are rerun.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 9666ae5ddd28](https://github.com/reypapin/dga-type-cascades/tree/9666ae5ddd2803bda02edb50c5cdcf19668f4ad9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
