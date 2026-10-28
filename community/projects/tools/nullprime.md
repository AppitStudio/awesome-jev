# NullPrime (a negative-control dataset for models that claim to know when they don't, tested on Jev and LLMs)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Dataset of integers labelled prime or composite where the only learnable surface pattern has been removed, so any model should be at chance: a negative control for uncertainty, abstention and calibration claims. Includes a certificate run with standard learners, an LLM study and a Jev evaluation using a Noul probability and a Choice with an abstain option.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bmiedlar/nullprime) |
| Maintainer | [bmiedlar](https://github.com/bmiedlar). Independently curated. |
| Format | Python dataset and evaluation code |
| Requirements | Python; a TypeSafe API key only to rerun the Jev evaluation. |
| License | [MIT](https://github.com/bmiedlar/nullprime/blob/edc9eb4a84f79d1312e5525a67e0cc1c31476f04/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/nullprime/jev_eval.py`](https://github.com/bmiedlar/nullprime/blob/edc9eb4a84f79d1312e5525a67e0cc1c31476f04/src/nullprime/jev_eval.py) at the pinned commit. |

## When to use

- Check whether a model's confidence drops when the answer can't be known.
- Mismatch: a test set, not a tool; findings are the author's.

## How it works

`src/nullprime/jev_eval.py` uses the official TypeSafe Python SDK (`jev-latest`) to ask each item as a Noul and as a Choice with an abstain option. Integration evidence: [`src/nullprime/jev_eval.py`](https://github.com/bmiedlar/nullprime/blob/edc9eb4a84f79d1312e5525a67e0cc1c31476f04/src/nullprime/jev_eval.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/bmiedlar/nullprime && cd nullprime
python -m nullprime.certify
python -m nullprime.jev_eval --out runs/jev-timing --limit 50   # needs TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Write-up: [miedlar.com/writing/nullprime/](https://miedlar.com/writing/nullprime/)
- README: [github.com/bmiedlar/nullprime#readme](https://github.com/bmiedlar/nullprime#readme)

## Limits and data handling

Only integers are sent to TypeSafe. Raw Jev responses are kept local.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit edc9eb4a84f7](https://github.com/bmiedlar/nullprime/tree/edc9eb4a84f79d1312e5525a67e0cc1c31476f04). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
