# SEO-Magus (site crawler and technical SEO auditor that proposes internal links, with Jev deciding which links readers would click)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Crawl a website, audit it for orphan and buried pages, broken links, redirect chains, titles and canonicals, then get ready-to-paste internal links: for each pair of pages a fast classifier decides whether the source paragraph gives readers a real reason to click, and the sentence is rewritten with a descriptive anchor. Output is a terminal summary and an HTML report ranking pages in your internal link graph. TypeSafe Jev is the classifier when `TYPESAFE_API_KEY` is set; without it an offline heuristic runs, and OpenAI, Claude, Ollama or your own model can be plugged in.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/lucasrafaldini/SEO-magus) |
| Maintainer | [lucasrafaldini](https://github.com/lucasrafaldini). Independently curated. |
| Format | Python CLI (MIT) |
| Requirements | Python 3.10+; `TYPESAFE_API_KEY` for the Jev classifier (optional, offline heuristic otherwise). |
| License | [MIT](https://github.com/lucasrafaldini/SEO-magus/blob/043f75b41966cc088eee31c456daa4ad4b3a5a59/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/engines/jev_client.py`](https://github.com/lucasrafaldini/SEO-magus/blob/043f75b41966cc088eee31c456daa4ad4b3a5a59/src/engines/jev_client.py) at the pinned commit. |

## When to use

- Rebuild a site's internal link structure from crawl data plus cheap per-link decisions.
- Mismatch: content writing; it proposes links and anchors, not new copy.

## How it works

`src/engines/jev_client.py` posts link decisions to `https://api.typesafe.ai/v1/systemone`; `src/engines/classifiers/factory.py` registers the `jev` preset (`TYPESAFE_API_KEY`) alongside other providers and the offline heuristic. Integration evidence: [`src/engines/jev_client.py`](https://github.com/lucasrafaldini/SEO-magus/blob/043f75b41966cc088eee31c456daa4ad4b3a5a59/src/engines/jev_client.py).

## Get started

Install, try the bundled mock site offline, then audit your own site.

```sh
git clone https://github.com/lucasrafaldini/SEO-magus.git && cd SEO-magus
make install && make audit-mock
cp config/config.example.yaml config/config.yaml
export TYPESAFE_API_KEY=...
python -m src.cli audit --url https://your-site.com/ --config config/config.yaml --html build/report
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/lucasrafaldini/SEO-magus/blob/043f75b41966cc088eee31c456daa4ad4b3a5a59/README.md](https://github.com/lucasrafaldini/SEO-magus/blob/043f75b41966cc088eee31c456daa4ad4b3a5a59/README.md)
- Classifiers guide: [github.com/lucasrafaldini/SEO-magus/blob/043f75b41966cc088eee31c456daa4ad4b3a5a59/docs/CLASSIFIERS.md](https://github.com/lucasrafaldini/SEO-magus/blob/043f75b41966cc088eee31c456daa4ad4b3a5a59/docs/CLASSIFIERS.md)

## Limits and data handling

Jev is optional: without a key an offline heuristic decides. With Jev, paragraph text from the pages you crawl goes to TypeSafe on your key. Crawl only sites you are allowed to crawl.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit 043f75b41966](https://github.com/lucasrafaldini/SEO-magus/tree/043f75b41966cc088eee31c456daa4ad4b3a5a59). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
