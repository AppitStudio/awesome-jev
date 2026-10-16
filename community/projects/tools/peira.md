# peira

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Open-source stress test for decision models and guardrails: it measures whether hostile input can flip a model's typed output, pairing every attack with a benign twin and reporting attack success rates with Wilson intervals; includes a Jev adapter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/david-engelmann/peira) |
| Maintainer | [david-engelmann](https://github.com/david-engelmann). Independently curated. |
| Format | Python package and CLI (`pip install -e .`) |
| Requirements | Python 3; a TypeSafe API key to test Jev (a mock adapter runs offline). |
| License | [MIT](https://github.com/david-engelmann/peira/blob/12a9d0250ed80fdae7bf4db6560470ae2e4ceb28/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`python/peira/adapters/jev.py`](https://github.com/david-engelmann/peira/blob/12a9d0250ed80fdae7bf4db6560470ae2e4ceb28/python/peira/adapters/jev.py) at the pinned commit. |

## When to use

- Check whether prompt injection in the input can change a Jev decision in your own task before you rely on it.
- Compare decision models or guardrails on the same attack suite.
- Mismatch: measures decision flips under attack, not accuracy on clean input.

## How it works

The Jev adapter pins an exact snapshot (`jev-1.13.0` by default, `jev-1.14.0` supported, never `jev-latest`) so measurements are reproducible; `peira run` executes a suite and `peira report` renders HTML. Integration evidence: [`python/peira/adapters/jev.py`](https://github.com/david-engelmann/peira/blob/12a9d0250ed80fdae7bf4db6560470ae2e4ceb28/python/peira/adapters/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/david-engelmann/peira.git && cd peira
pip install -e .
peira run --adapter mock --suite trial --seed 0 --out runs
peira report --run runs/mock-trial.json --out report.html
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Methodology: `docs/Methodology.md`; adapters: `docs/Adapters.md`.

## Limits and data handling

Attack and benign inputs go to the provider you test, on your key.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 12a9d0250ed8](https://github.com/david-engelmann/peira/tree/12a9d0250ed80fdae7bf4db6560470ae2e4ceb28). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
