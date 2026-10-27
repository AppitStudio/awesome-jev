# Did the News Move the Price? (Dhaka Stock Exchange event study, with Jev scoring the news)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Code, data and manuscript for an event study of 70 company-specific news events on the Dhaka Stock Exchange with a same-firm placebo: Jev scored each headline and article (is it about the company, is it good or bad news), and the finding is no detectable average price reaction, with only a weak negative asymmetry for bad news. The public package reproduces the numbers offline.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/asiqurgem26-del/dse-news-impact) |
| Maintainer | [asiqurgem26-del](https://github.com/asiqurgem26-del). Independently curated. |
| Format | Python research package with manuscript |
| Requirements | Python; a TypeSafe API key only to rescore the articles. |
| License | [MIT](https://github.com/asiqurgem26-del/dse-news-impact/blob/b9dd3e044cd5c1c0255c6bfd6aa6758988c49a4e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`code/classify_articles.py`](https://github.com/asiqurgem26-del/dse-news-impact/blob/b9dd3e044cd5c1c0255c6bfd6aa6758988c49a4e/code/classify_articles.py) at the pinned commit. |

## When to use

- Reuse a small, reproducible Jev news-classification step in an event study.
- Mismatch: one market and 70 events; results are the author's.

## How it works

`code/classify_articles.py` posts each article with Noul questions to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0`) and saves the scores used in the analysis. Integration evidence: [`code/classify_articles.py`](https://github.com/asiqurgem26-del/dse-news-impact/blob/b9dd3e044cd5c1c0255c6bfd6aa6758988c49a4e/code/classify_articles.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/asiqurgem26-del/dse-news-impact && cd dse-news-impact
pip install -r requirements.txt
python code/event_impact.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Manuscript: [github.com/asiqurgem26-del/dse-news-impact/blob/main/manuscript/main.pdf](https://github.com/asiqurgem26-del/dse-news-impact/blob/main/manuscript/main.pdf)
- README: [github.com/asiqurgem26-del/dse-news-impact#readme](https://github.com/asiqurgem26-del/dse-news-impact#readme)

## Limits and data handling

Rescoring sends article text to TypeSafe. Reproducing the tables needs no network. Not investment advice.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit b9dd3e044cd5](https://github.com/asiqurgem26-del/dse-news-impact/tree/b9dd3e044cd5c1c0255c6bfd6aa6758988c49a4e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
