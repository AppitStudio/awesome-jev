# Tweet Index (local search engine for your own X likes and bookmarks, where Jev judges relevance and substance)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Personal tool that turns your X likes and bookmarks into a private search engine. A userscript saves the responses X's page already loads as you scroll your saves; a weekly update stores them in SQLite, describes images, fetches link titles, writes one-line summaries with an OpenAI model and embeds everything locally. At search time Jev judges each candidate's relevance to your topic and each post's substance, and results are ranked by relevance, substance and similarity into strong matches and maybes. The maker reports Jev's ranking raised the share of relevant tweets found from 55% to 82%. Includes an interactive `ti` shell and evaluation scripts.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NachikethRamesh/Tweet-Index) |
| Maintainer | [NachikethRamesh](https://github.com/NachikethRamesh). Independently curated. |
| Format | Python CLI and userscript (MIT) |
| Requirements | Python, a browser userscript manager, an OpenAI key for summaries, and a TypeSafe key (`typesafe-sdk`); the embedding model runs locally. |
| License | [MIT](https://github.com/NachikethRamesh/Tweet-Index/blob/30f13c297f797cdb2b4395be4950453eaf628c65/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/donCheetosSama/status/2122116188113367294)). |
| Jev evidence | [`tweet_index/jev.py`](https://github.com/NachikethRamesh/Tweet-Index/blob/30f13c297f797cdb2b4395be4950453eaf628c65/tweet_index/jev.py) at the pinned commit. |

## When to use

- Find things you saved on X by meaning, ranked by how relevant and substantial they are.
- Mismatch: a hosted service; it is a personal tool with no accounts or hosted version.

## How it works

`tweet_index/jev.py` wraps the TypeSafe Python SDK behind two functions, `judge_tweet` and `relevance`, with a shared rate limiter and spend tracking; `config.yaml` pins `jev-1.13.0`, and the module refuses `jev-latest` so tuned thresholds do not drift. Integration evidence: [`tweet_index/jev.py`](https://github.com/NachikethRamesh/Tweet-Index/blob/30f13c297f797cdb2b4395be4950453eaf628c65/tweet_index/jev.py).

## Get started

Install, capture your likes and bookmarks with the userscript, index them and search.

```sh
git clone https://github.com/NachikethRamesh/Tweet-Index && cd Tweet-Index
pip install -r requirements.txt
# add OpenAI and TypeSafe keys, capture saves with the userscript (see README)
python update.py
python ti.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/NachikethRamesh/Tweet-Index/blob/30f13c297f797cdb2b4395be4950453eaf628c65/README.md](https://github.com/NachikethRamesh/Tweet-Index/blob/30f13c297f797cdb2b4395be4950453eaf628c65/README.md)
- Maker's thread: [x.com/donCheetosSama/status/2122115874262057199](https://x.com/donCheetosSama/status/2122115874262057199)

## Limits and data handling

Your saved posts stay on your machine except the model calls: summaries and image descriptions go to OpenAI and judged candidates go to TypeSafe on your keys. The maker estimates about $0.05 per 100 new posts; the 55%→82% figure is the maker's own measurement on one corpus.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 30f13c297f79](https://github.com/NachikethRamesh/Tweet-Index/tree/30f13c297f797cdb2b4395be4950453eaf628c65). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
