# laya-vs-jev calibration eval by jupiutrera (Jev and two Laya models on the same 2,000 typed decisions, with raw answers and a pixel-art video)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Measures whether a stated confidence matches accuracy for Jev and two versions of Laya (general and fine-tuned) on 400 typed-decisions test cases (2,000 decisions), then shows how much a per-question-type temperature fit on held-out cases repairs. Reports ECE, Brier scores, reliability curves and bootstrap intervals; every raw answer is committed. Results are also told as 100-square grids in a pixel-art scene and video. English and Spanish READMEs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jupiutrera/laya-vs-jev) |
| Maintainer | [jupiutrera](https://github.com/jupiutrera). Independently curated. |
| Format | Research eval (Python) + raw answers |
| Requirements | Python; a TypeSafe key (or Vercel AI Gateway key) to rerun Jev; Laya runs locally on CPU. |
| License | [MIT](https://github.com/jupiutrera/laya-vs-jev/blob/0d73d7ab4752aad059cb67ef7cc71f38f3ac785b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`medir/preguntar.py`](https://github.com/jupiutrera/laya-vs-jev/blob/0d73d7ab4752aad059cb67ef7cc71f38f3ac785b/medir/preguntar.py) at the pinned commit. |

## When to use

- Builders who set auto-accept thresholds on Jev or Laya confidences and want comparable calibration numbers.
- Mismatch: a general benchmark; it covers one dataset of four workflows.

## How it works

`medir/preguntar.py` sends each case's state and five questions unchanged to `https://api.typesafe.ai/v1/systemone` (`jev-latest`, answered as `jev-1.13.0`) or through Vercel AI Gateway, and `analizar.py` computes calibration metrics and fits. Integration evidence: [`medir/preguntar.py`](https://github.com/jupiutrera/laya-vs-jev/blob/0d73d7ab4752aad059cb67ef7cc71f38f3ac785b/medir/preguntar.py).

## Get started

Recompute the metrics from the committed answers, or rerun with your own key.

```sh
git clone https://github.com/jupiutrera/laya-vs-jev && cd laya-vs-jev
# see README for the analysis and rerun commands
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Spanish README: [github.com/jupiutrera/laya-vs-jev/blob/main/README.es.md](https://github.com/jupiutrera/laya-vs-jev/blob/main/README.es.md)
- Results: [github.com/jupiutrera/laya-vs-jev/blob/main/datos/resultados.json](https://github.com/jupiutrera/laya-vs-jev/blob/main/datos/resultados.json)

## Limits and data handling

One dataset and one model version per run; the fine-tuned Laya was trained on the same dataset's train split. Code identifiers and JSON keys are in Spanish.

## Review and maintenance

Reviewed **2026-11-27** (Europe/Sofia) at [commit 0d73d7ab4752](https://github.com/jupiutrera/laya-vs-jev/tree/0d73d7ab4752aad059cb67ef7cc71f38f3ac785b). Inspected the README, LICENSE and `medir/preguntar.py` at the pinned commit; nothing was run on the review host. Separate from the listed zaferayan/laya-vs-jev. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
