# Venn (vector decision model over your embeddings, with a Decisions API and a Venn-or-Jev guide)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Small local Vector Decision Model that answers Choice, Score and Noul questions over embeddings you already have, decides from recorded outcomes or trains custom heads, accepts requests in the TypeSafe Decisions API format, and documents when to use it instead of Jev.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/markrussinovich/venn-vdm) |
| Maintainer | [markrussinovich](https://github.com/markrussinovich). Independently curated. |
| Format | Python package, server and docs (MIT) |
| Requirements | Python with PyTorch (CPU works); the reader model downloads on first use. |
| License | [MIT](https://github.com/markrussinovich/venn-vdm/blob/ad97513f1cc1fc5abc886f195d17e6145776e091/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`venn/decisions.py`](https://github.com/markrussinovich/venn-vdm/blob/ad97513f1cc1fc5abc886f195d17e6145776e091/venn/decisions.py) at the pinned commit. |

## When to use

- Make repeated typed decisions over vectors you already store.
- Decide when Jev or a local embedding-based head fits a task.
- Mismatch: an alternative to Jev, not a Jev integration; results are the maintainer's.

## How it works

`venn/decisions.py` translates Decisions API requests (choice, score, noul) into native Venn questions and back with model `venn-1`; `docs/venn-and-jev.md` explains the trade-off: Jev for content-and-description decisions, Venn for labeled history, custom heads and repeated decisions over one embedded collection. Integration evidence: [`venn/decisions.py`](https://github.com/markrussinovich/venn-vdm/blob/ad97513f1cc1fc5abc886f195d17e6145776e091/venn/decisions.py).

## Get started

Install the package and run the quickstart.

```sh
git clone https://github.com/markrussinovich/venn-vdm.git && cd venn-vdm
python -m pip install . && venn quickstart
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Venn and Jev: [github.com/markrussinovich/venn-vdm/blob/ad97513f1cc1fc5abc886f195d17e6145776e091/docs/venn-and-jev.md](https://github.com/markrussinovich/venn-vdm/blob/ad97513f1cc1fc5abc886f195d17e6145776e091/docs/venn-and-jev.md)
- Docs site: [markrussinovich.github.io/venn-vdm/](https://markrussinovich.github.io/venn-vdm/)

## Limits and data handling

Runs locally; no request goes to TypeSafe.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit ad97513f1cc1](https://github.com/markrussinovich/venn-vdm/tree/ad97513f1cc1fc5abc886f195d17e6145776e091). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
