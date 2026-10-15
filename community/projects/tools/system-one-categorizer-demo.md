# System One categorizer demo (Bulgarian)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small blog-category app and side-by-side test of Jev (TypeSafe API) and open Laya multilingual on 50 labelled Bulgarian posts, with a local BgGPT model naming new categories.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/SciScend/system-one-categorizer-demo) |
| Maintainer | [SciScend](https://github.com/SciScend). Independently curated. |
| Format | Python local web app + eval set (Bulgarian UI) |
| Requirements | Python, `uv`; TypeSafe key for Jev (falls back to local Laya on CPU without one). |
| License | [MIT](https://github.com/SciScend/system-one-categorizer-demo/blob/0d7716003d6a1a8525fd812eb9b5f6d1f78439e6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`classifier.py`](https://github.com/SciScend/system-one-categorizer-demo/blob/0d7716003d6a1a8525fd812eb9b5f6d1f78439e6/classifier.py) at the pinned commit. |

## When to use

- Check Jev on a non-English (Bulgarian) categorization task before adopting it.
- See a working pattern for suggest-and-confirm categorization with a model switch.
- Mismatch: 50-post author evaluation (Jev 48/50, Laya 36/50); not reproduced here.

## How it works

The classifier sends each post with existing categories plus a 'new topic' option to Jev through `typesafe-sdk` (or to Laya locally); when 'new topic' wins, a small local LLM proposes a name, and the user accepts or corrects it. Integration evidence: [`classifier.py`](https://github.com/SciScend/system-one-categorizer-demo/blob/0d7716003d6a1a8525fd812eb9b5f6d1f78439e6/classifier.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/SciScend/system-one-categorizer-demo.git && cd system-one-categorizer-demo
uv pip install -r requirements.txt
uv pip install typesafe-sdk==0.7.1
python app.py   # http://127.0.0.1:8770
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author write-up: [sciscend.com/blog/jev-model-koyto-reshava/](https://sciscend.com/blog/jev-model-koyto-reshava/)
- Eval set: `eval_posts.json`.

## Limits and data handling

With Jev selected, posts go to TypeSafe on your key; Laya and BgGPT run locally.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 0d7716003d6a](https://github.com/SciScend/system-one-categorizer-demo/tree/0d7716003d6a1a8525fd812eb9b5f6d1f78439e6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
