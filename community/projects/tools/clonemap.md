# clonemap (finds helpers many Python apps rewrite by hand, labelled with Jev)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Research probe that clones a few thousand Django and LLM apps, groups functions that do the same thing with different code, compares them with a control set and lists candidates for a missing library; Jev labels the top clusters and checks proposed libraries.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Harthor/clonemap) |
| Maintainer | [Harthor](https://github.com/Harthor). Independently curated. |
| Format | Python research pipeline and static results explorer |
| Requirements | Python 3; OpenRouter key for Jev labelling and Haiku descriptions; local GPU/MPS for embeddings. |
| License | [MIT](https://github.com/Harthor/clonemap/blob/c69fea249950ba15714a69eb1b6b3b1d5d0a9837/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/s8_label.py`](https://github.com/Harthor/clonemap/blob/c69fea249950ba15714a69eb1b6b3b1d5d0a9837/scripts/s8_label.py) at the pinned commit. |

## When to use

- Look for needs revealed by repeated hand-written code rather than by requests.
- Reuse a staged, cached pipeline for code-clustering studies.
- Mismatch: a probe, not a product; candidates need human review.

## How it works

Stage 8 (`scripts/s8_label.py`) uses the official Python SDK to ask Jev (`typesafe/jev-1.13` through OpenRouter) one yes/no question per category and per proposed library; a cluster counts as confirmed only when Jev and Haiku agree. README and comments are partly in Spanish. Integration evidence: [`scripts/s8_label.py`](https://github.com/Harthor/clonemap/blob/c69fea249950ba15714a69eb1b6b3b1d5d0a9837/scripts/s8_label.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Harthor/clonemap
# each stage is a separate script reading config.yaml, e.g. python scripts/s8_label.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Results explorer: [github.com/Harthor/clonemap/tree/main/site](https://github.com/Harthor/clonemap/tree/main/site)
- README with method: [github.com/Harthor/clonemap#readme](https://github.com/Harthor/clonemap#readme)

## Limits and data handling

Cluster summaries are sent to OpenRouter. Findings are the author's own and were not reproduced.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit c69fea249950](https://github.com/Harthor/clonemap/tree/c69fea249950ba15714a69eb1b6b3b1d5d0a9837). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
