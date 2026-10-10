# finance-decision-evals

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Independent evaluation of TypeSafe Jev on ASC 606 revenue-recognition calls: whether a non-standard software contract clause needs revenue accounting review and which issue it raises, using expert-designed synthetic clauses, a frozen held-out set, and a results site.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/vicwlau/finance-decision-evals) |
| Maintainer | [vicwlau](https://github.com/vicwlau). Independently curated. |
| Format | Evaluation repo (scripts, report, results site) |
| Requirements | Node.js/TypeScript per the repo scripts; TypeSafe API key to rerun. |
| License | [MIT](https://github.com/vicwlau/finance-decision-evals/blob/b02a3c653a9adfbabfa1dc078ccc148f0ea03e05/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- See how question wording and code-computed facts change Jev accuracy on a domain accounting task.
- Mismatch: small synthetic set (20 held-out clauses); results are the author's.

## How it works

Clauses are generated from structured facts; Jev is asked rule-based and term-based questions under several setups and scored over repeated runs. (Summarized from the upstream [README](https://github.com/vicwlau/finance-decision-evals/blob/b02a3c653a9adfbabfa1dc078ccc148f0ea03e05/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): Read `rev-rec/report.md` and the `site/` results page; rerun scripts per the README.

## Limits and data handling

Uses synthetic contract clauses only. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-10** (Europe/Sofia) at [commit b02a3c653a9a](https://github.com/vicwlau/finance-decision-evals/tree/b02a3c653a9adfbabfa1dc078ccc148f0ea03e05). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
