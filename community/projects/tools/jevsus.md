# Jevsus (3,600+ forced true/false statements put to TypeSafe Jev, with published results)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open dataset and runner that asks TypeSafe Jev thousands of templated true/false statements with one subject swapped, in multiple wordings and option orders, and publishes every probability.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/2nd1st/Jevsus) |
| Maintainer | [2nd1st](https://github.com/2nd1st). Independently curated. |
| Format | Python runner + published result tables (MIT) |
| Requirements | Python 3 and a TypeSafe API key to re-run. |
| License | [MIT](https://github.com/2nd1st/Jevsus/blob/8e1d55a8c60f6c929886de32b6a07c4119cefaa3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run.py`](https://github.com/2nd1st/Jevsus/blob/8e1d55a8c60f6c929886de32b6a07c4119cefaa3/run.py) at the pinned commit. |

## When to use

- Explore how Jev answers forced binary choices across subjects.
- Reuse the method to probe order and wording sensitivity.
- Mismatch: probing study; results are not ground truth about the subjects.

## How it works

`run.py` posts each statement to `https://api.typesafe.ai/v1/systemone` with `jev-latest` and `TYPESAFE_API_KEY`, swapping option order to measure position effects. Integration evidence: [`run.py`](https://github.com/2nd1st/Jevsus/blob/8e1d55a8c60f6c929886de32b6a07c4119cefaa3/run.py).

## Get started

Clone, set TYPESAFE_API_KEY, and re-run or browse the published tables.

```sh
git clone https://github.com/2nd1st/Jevsus.git && cd Jevsus
export TYPESAFE_API_KEY=...
python run.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/2nd1st/Jevsus/blob/8e1d55a8c60f6c929886de32b6a07c4119cefaa3/README.md](https://github.com/2nd1st/Jevsus/blob/8e1d55a8c60f6c929886de32b6a07c4119cefaa3/README.md)

## Limits and data handling

Statements touch politically sensitive topics; numbers reflect model outputs only.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 8e1d55a8c60f](https://github.com/2nd1st/Jevsus/tree/8e1d55a8c60f6c929886de32b6a07c4119cefaa3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
