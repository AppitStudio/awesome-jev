# decision-toolkit

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local-first toolkit from GIA-UH and Syalia for open-weights System One decision models: typed choice, yes/no, and score questions with calibrated probabilities on CPU, as a library, CLI, and REST server that speaks TypeSafe's System One contract.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gia-uh/decision-toolkit) |
| Maintainer | [gia-uh](https://github.com/gia-uh). Independently curated. |
| Format | Python library + CLI + FastAPI server |
| Requirements | Python; optional extras for Laya, Von, or the server. |
| License | [MIT](https://github.com/gia-uh/decision-toolkit/blob/255d090ed654df1ef2d015c85d39836936ef5bf4/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/decision_toolkit/backends/systemone.py`](https://github.com/gia-uh/decision-toolkit/blob/255d090ed654df1ef2d015c85d39836936ef5bf4/src/decision_toolkit/backends/systemone.py) at the pinned commit. |

## When to use

- Run decision models locally with the same wire format as Jev.
- Point existing Jev clients at a local server by changing the base URL.
- Mismatch: runs open-weights models, not Jev itself; remote Jev is one backend.

## How it works

`backends/systemone.py` speaks `POST /v1/systemone` so local models and a remote Jev endpoint share one contract; `dtk serve` lets Jev clients switch with `TYPESAFE_BASE_URL`. Integration evidence: [`src/decision_toolkit/backends/systemone.py`](https://github.com/gia-uh/decision-toolkit/blob/255d090ed654df1ef2d015c85d39836936ef5bf4/src/decision_toolkit/backends/systemone.py).

## Get started

pip install decision-toolkit (add `[laya]` or `[server]` extras as needed).

```sh
pip install "decision-toolkit[server]"
dtk serve
# then TYPESAFE_BASE_URL=http://localhost:8000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README backend list
- src/decision_toolkit/backends/systemone.py

## Limits and data handling

Local by default; remote backends send state to the configured host. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 255d090ed654](https://github.com/gia-uh/decision-toolkit/tree/255d090ed654df1ef2d015c85d39836936ef5bf4). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
