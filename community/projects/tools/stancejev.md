# StanceJEV (paper code: zero-shot stance detection as a typed Jev choice)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Paper code that treats zero-shot stance detection as a typed choice over favor, against and none: context reconstruction and batch reasoning by an LLM feed a Jev decision, and a local consistency check verifies it; the README reports results on SemEval-2016 and VAST with two remote calls per item.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/danikstifloanpaarnatl/jev-stance) |
| Maintainer | [danikstifloanpaarnatl](https://github.com/danikstifloanpaarnatl). Independently curated. |
| Format | Python research code with paper |
| Requirements | Python 3; an OpenRouter key for the reasoning model and Jev. |
| License | [MIT](https://github.com/danikstifloanpaarnatl/jev-stance/blob/4c531363ab6d014a1a54835f48d73370cd1429f7/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/stancejev/decision.py`](https://github.com/danikstifloanpaarnatl/jev-stance/blob/4c531363ab6d014a1a54835f48d73370cd1429f7/src/stancejev/decision.py) at the pinned commit. |

## When to use

- Study how a decision model can make the final call in a stance or classification pipeline.
- Reproduce the paper's SemEval-2016 and VAST runs.
- Mismatch: research code; scores are the author's.

## How it works

`src/stancejev/decision.py` sends the reconstructed context and reasoning with a stance Choice to the OpenRouter Decisions API using `typesafe/jev-1.13` (overridable with `JEV_MODEL`). Integration evidence: [`src/stancejev/decision.py`](https://github.com/danikstifloanpaarnatl/jev-stance/blob/4c531363ab6d014a1a54835f48d73370cd1429f7/src/stancejev/decision.py).

## Get started

From the upstream README (not run on the review host):

```sh
python3 -m venv .venv && source .venv/bin/activate
pip install numpy scipy scikit-learn requests   # see the README for run scripts and the offline smoke test
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Paper PDF: [github.com/danikstifloanpaarnatl/jev-stance/blob/main/paper/paper.pdf](https://github.com/danikstifloanpaarnatl/jev-stance/blob/main/paper/paper.pdf)
- README: [github.com/danikstifloanpaarnatl/jev-stance#readme](https://github.com/danikstifloanpaarnatl/jev-stance#readme)

## Limits and data handling

Texts and targets go to OpenRouter and on to TypeSafe; Jev is reached through OpenRouter. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 4c531363ab6d](https://github.com/danikstifloanpaarnatl/jev-stance/tree/4c531363ab6d014a1a54835f48d73370cd1429f7). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
