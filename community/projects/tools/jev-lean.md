# JevLean (experimental Lean 4 tactic where Jev ranks proof steps and Lean checks them)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Lean 4 tactic `jev?` that asks Jev to rank candidate proof steps through a local broker; Lean checks every step and, when search succeeds, prints an ordinary `Try this` suggestion so the final proof no longer needs the model. Not a general automatic prover; committed traces record the benchmark runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jesyspa/jev-lean) |
| Maintainer | [jesyspa](https://github.com/jesyspa). Independently curated. |
| Format | Lean 4 package with a Python broker |
| Requirements | Git, Python 3 and Lean via elan; a TypeSafe API key for the broker. |
| License | [Apache-2.0](https://github.com/jesyspa/jev-lean/blob/2b2ec11747d7101191b8a72e9014de175e2ab764/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevlean/experiment.py`](https://github.com/jesyspa/jev-lean/blob/2b2ec11747d7101191b8a72e9014de175e2ab764/jevlean/experiment.py) at the pinned commit. |

## When to use

- Try model-ranked proof search where Lean, not the model, decides what is correct.
- Get proof suggestions that check without the broker afterwards.
- Mismatch: experimental; small benchmark only.

## How it works

The broker (`jevlean/model_broker.py`) listens on `127.0.0.1:8765` and uses `jevlean/experiment.py`, which posts the proof state and candidate tactic descriptions to `https://api.typesafe.ai/v1/systemone` for ranking. Integration evidence: [`jevlean/experiment.py`](https://github.com/jesyspa/jev-lean/blob/2b2ec11747d7101191b8a72e9014de175e2ab764/jevlean/experiment.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jesyspa/jev-lean.git && cd jev-lean
lake build
TYPESAFE_API_KEY=your_key python3 -m jevlean.model_broker
# in Example.lean: import JevLean, then `by jev?`
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jesyspa/jev-lean#readme](https://github.com/jesyspa/jev-lean#readme)

## Limits and data handling

Proof states and candidate tactics go to TypeSafe; they may contain private theorem statements. The broker binds to localhost.

## Review and maintenance

Reviewed **2026-10-26** (Europe/Sofia) at [commit 2b2ec11747d7](https://github.com/jesyspa/jev-lean/tree/2b2ec11747d7101191b8a72e9014de175e2ab764). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
