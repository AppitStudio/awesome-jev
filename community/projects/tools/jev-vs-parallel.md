# Jev vs Parallel Decisions (two real Jev gates scored against answer keys fixed before either tool ran)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Benchmark of Jev against Parallel's new web-searching Decisions API on the questions two of Eric Siu's production Jev gates ask: M&A and ICP criteria for 50 YC companies, and whether a content topic has already been published. Answer keys come from the YC directory and the site's own pages, fixed before either tool ran; results are reported as balanced accuracy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VedantBhayani/jev-vs-parallel) |
| Maintainer | [VedantBhayani](https://github.com/VedantBhayani). Independently curated. |
| Format | Python scripts with results |
| Requirements | Python; TypeSafe and Parallel API keys to rerun. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bench.py`](https://github.com/VedantBhayani/jev-vs-parallel/blob/0a30bfa83139893266cf5e040d65c186973413cd/bench.py) at the pinned commit. |

## When to use

- Decide when a gate needs live web facts rather than a decision model's prior knowledge.
- Mismatch: small samples; results are the author's, dated 2026-10-28.

## How it works

`bench.py` posts the same states to `https://api.typesafe.ai/v1/systemone` (`jev-latest`) and to Parallel, then `score.py` compares them with the fixed keys. Integration evidence: [`bench.py`](https://github.com/VedantBhayani/jev-vs-parallel/blob/0a30bfa83139893266cf5e040d65c186973413cd/bench.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/VedantBhayani/jev-vs-parallel && cd jev-vs-parallel
python build_truth.py yc.json posts.txt
python bench.py    # needs TYPESAFE_API_KEY and PARALLEL_API_KEY
python score.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with results: [github.com/VedantBhayani/jev-vs-parallel#readme](https://github.com/VedantBhayani/jev-vs-parallel#readme)

## Limits and data handling

Public company and topic data goes to both providers.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 0a30bfa83139](https://github.com/VedantBhayani/jev-vs-parallel/tree/0a30bfa83139893266cf5e040d65c186973413cd). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
