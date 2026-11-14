# COAT-Learn (causal-discovery research framework that can use hosted Jev to annotate, review and deduplicate the factors an LLM proposes)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Python implementation of COAT (JMLR paper): a language model proposes candidate factors from unstructured text such as reviews, a decision model annotates each observation with them, and statistical methods study causal structure. The default decision model is Kev, run locally; `--decision-model jev` switches annotation, review and deduplication to hosted Jev, which the README suggests for a first attempt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/causalcoat/COAT-Learn) |
| Maintainer | [causalcoat](https://github.com/causalcoat). Independently curated. |
| Format | Python package and CLI with config presets (Apache-2.0) |
| Requirements | Python 3; for the hosted path a `DEEPSEEK_API_KEY` (proposer) and `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/causalcoat/COAT-Learn/blob/3a74612772b668e187fa34f21d1fbe02d5e6d96b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`coatlearn/models/systemone.py`](https://github.com/causalcoat/COAT-Learn/blob/3a74612772b668e187fa34f21d1fbe02d5e6d96b/coatlearn/models/systemone.py) at the pinned commit. |

## When to use

- Turn a text column into measured variables for causal analysis without building a local model server.
- Mismatch: image or database inputs; the ready interfaces take a text column.

## How it works

`coatlearn/models/systemone.py` holds the native System One client and `JevConfig`; presets such as `config/mb.toml` set `base_url = "https://api.typesafe.ai"` and model `jev-1.14.0`. Only `--run` calls models. Integration evidence: [`coatlearn/models/systemone.py`](https://github.com/causalcoat/COAT-Learn/blob/3a74612772b668e187fa34f21d1fbe02d5e6d96b/coatlearn/models/systemone.py).

## Get started

Install, set both keys, and run an example task with Jev.

```sh
git clone https://github.com/causalcoat/COAT-Learn && cd COAT-Learn && pip install -e .
export DEEPSEEK_API_KEY=... TYPESAFE_API_KEY=...
python -m coatlearn mb --config config/mb.toml --decision-model jev --run --output-dir runs/apple-mb
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/causalcoat/COAT-Learn/blob/3a74612772b668e187fa34f21d1fbe02d5e6d96b/README.md](https://github.com/causalcoat/COAT-Learn/blob/3a74612772b668e187fa34f21d1fbe02d5e6d96b/README.md)
- Paper: [www.jmlr.org/papers/v27/25-2137.html](https://www.jmlr.org/papers/v27/25-2137.html)

## Limits and data handling

With Jev selected, the selected text is sent to TypeSafe and the proposer's provider on your keys. The default Kev path is local and does not use Jev.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 3a74612772b6](https://github.com/causalcoat/COAT-Learn/tree/3a74612772b668e187fa34f21d1fbe02d5e6d96b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
