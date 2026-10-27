# Classification without fine-tuning (Jev vs. BERT vs. LLMs on 30,000 product names)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Companion repo for a talk comparing six ways to sort ~30,000 Croatian retail product names into 10 categories, from TF-IDF and fine-tuned BERTić to OpenAI Decisions, Claude Haiku, Qwen and Jev, on the same test items for accuracy, latency and cost, including learning curves and unseen-brand results.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/senko/classification-demo) |
| Maintainer | [senko](https://github.com/senko). Independently curated. |
| Format | Python benchmark with results and report |
| Requirements | uv (Python 3.13); API keys for the providers you rerun. |
| License | [MIT](https://github.com/senko/classification-demo/blob/cdbeea54570eb2689024cbf0e1af63c05c738595/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`run_jev.py`](https://github.com/senko/classification-demo/blob/cdbeea54570eb2689024cbf0e1af63c05c738595/run_jev.py) at the pinned commit. |

## When to use

- Decide between labelled training and a zero-shot decision API for classification.
- Reuse the runners and report for your own label set.
- Mismatch: one dataset and language; numbers are the author's.

## How it works

`run_jev.py` uses the TypeSafe Python SDK with a Choice over the ten categories, pinned to `jev-1.14.0` in `config/jev.toml`. Integration evidence: [`run_jev.py`](https://github.com/senko/classification-demo/blob/cdbeea54570eb2689024cbf0e1af63c05c738595/run_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/senko/classification-demo && cd classification-demo
# see the README for uv setup and run_jev.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/senko/classification-demo#readme](https://github.com/senko/classification-demo#readme)

## Limits and data handling

Product names go to each provider when rerun. Results are the author's, not verified here. Independent research; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit cdbeea54570e](https://github.com/senko/classification-demo/tree/cdbeea54570eb2689024cbf0e1af63c05c738595). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
