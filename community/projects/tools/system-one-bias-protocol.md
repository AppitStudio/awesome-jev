# Swap, Replicate, Read the Mass (University of Málaga protocol for auditing demographic bias in System One decision models)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Audit protocol, harness and analysis from a University of Málaga paper: 1,638,000 decisions over BBQ, CrowS-Pairs and SilverSpoon across thirteen configurations, including Jev as the commercial reference. Every item runs with options swapped, configurations repeat under new seeds, and scores read the full probability distribution so abstention cannot hide bias. Adapted items are on Hugging Face (CC BY-SA 4.0).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/amozo-es/system-one-bias-protocol) |
| Maintainer | [amozo-es](https://github.com/amozo-es). Independently curated. |
| Format | Python research code (execution and analysis) |
| Requirements | Python with uv; a GPU for local models; a TypeSafe key only for the Jev route. |
| License | [MIT](https://github.com/amozo-es/system-one-bias-protocol/blob/bcbfdad838100adf44ea8e50e00acfc805ec5c9f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`execution/src/models.py`](https://github.com/amozo-es/system-one-bias-protocol/blob/bcbfdad838100adf44ea8e50e00acfc805ec5c9f/execution/src/models.py) at the pinned commit. |

## When to use

- Audit a decision model for demographic bias with a published, repeatable protocol.
- Mismatch: research code; results are the authors'.

## How it works

`execution/src/models.py` gives every model the same Jev-shaped `ask(state, questions)` interface, calling TypeSafe's hosted `/v1/systemone` for Jev and local `/v1/systemone` servers for open models. Integration evidence: [`execution/src/models.py`](https://github.com/amozo-es/system-one-bias-protocol/blob/bcbfdad838100adf44ea8e50e00acfc805ec5c9f/execution/src/models.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/amozo-es/system-one-bias-protocol && cd system-one-bias-protocol/execution
uv sync --extra gpu
python cluster/download_datasets.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Dataset: [huggingface.co/datasets/amozo/system-one-bias-audit](https://huggingface.co/datasets/amozo/system-one-bias-audit)
- README: [github.com/amozo-es/system-one-bias-protocol#readme](https://github.com/amozo-es/system-one-bias-protocol#readme)

## Limits and data handling

Benchmark items describe stereotypes by design. Jev runs send items to TypeSafe.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit bcbfdad83810](https://github.com/amozo-es/system-one-bias-protocol/tree/bcbfdad838100adf44ea8e50e00acfc805ec5c9f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
