# Calibrain Harness (forward-testing harness for fast classification models on testnet perpetuals)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Forward-testing harness that asks a fast classification model (Kairos or Jev) a small set of labellable questions on each closed bar of perpetual futures markets, trades on Bybit testnet only, and scores every answer as a forecast to see honestly whether the model has an edge.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zadescoxp/calibrain-harness) |
| Maintainer | [zadescoxp](https://github.com/zadescoxp). Independently curated. |
| Format | Python service with a Next.js terminal UI (MIT) |
| Requirements | Python 3.12, Node.js 20+, a Jev (`TYPESAFE_API_KEY`) or Kairos key, and Bybit testnet keys. |
| License | [MIT](https://github.com/zadescoxp/calibrain-harness/blob/d0f526b06a34e92bf4b45e6e16ecff3ddf9198e1/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ctb/models.py`](https://github.com/zadescoxp/calibrain-harness/blob/d0f526b06a34e92bf4b45e6e16ecff3ddf9198e1/ctb/models.py) at the pinned commit. |

## When to use

- Measure whether a decision model's market forecasts beat chance before risking money.
- Mismatch: under active development; Bybit testnet only (hard-coded); not financial advice.

## How it works

`ctb/models.py` calls `POST {base_url}/v1/systemone` with `TYPESAFE_API_KEY` on `https://api.typesafe.ai` (`jev-1.14.0` pinned); Kairos and Jev share one interface, can be switched live and are evaluated separately. Integration evidence: [`ctb/models.py`](https://github.com/zadescoxp/calibrain-harness/blob/d0f526b06a34e92bf4b45e6e16ecff3ddf9198e1/ctb/models.py).

## Get started

Install the Python service, build the UI once, add keys and start the server.

```sh
git clone https://github.com/zadescoxp/calibrain-harness.git && cd calibrain-harness
python3.12 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python -m ctb.server
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/zadescoxp/calibrain-harness/blob/d0f526b06a34e92bf4b45e6e16ecff3ddf9198e1/README.md](https://github.com/zadescoxp/calibrain-harness/blob/d0f526b06a34e92bf4b45e6e16ecff3ddf9198e1/README.md)

## Limits and data handling

Market data and question sets go to TypeSafe on your key on every closed bar.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit d0f526b06a34](https://github.com/zadescoxp/calibrain-harness/tree/d0f526b06a34e92bf4b45e6e16ecff3ddf9198e1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
