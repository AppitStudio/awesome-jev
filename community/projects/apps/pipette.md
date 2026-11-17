# Pipette by ferced (free daily edition of new research papers, labelled and ranked by Jev with the authors' own words first)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Free daily science feed at pipette.day. Each morning it reads every new paper from arXiv, bioRxiv, medRxiv and 58 journals, quotes the abstract sentence that states the main result exactly as written, and publishes a short, field-balanced edition. Jev answers ten typed questions per paper (topic, kind of contribution, evidence, which sentence states the result or admits a limitation, appeal, size of the step, reading level, hype), and a public formula ranks them; papers that overclaim are left out. Edition papers also get English and Spanish summaries from an open model that Jev checks sentence by sentence against the abstract. A For you page ranks the day's papers against a sentence you write. No ads, tracking or accounts; labels are open CC0 JSON.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ferced/pipette) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://pipette.day) |
| Pricing and access | Free to read, with no account, ads or tracking. Self-hosting the MIT code means paying for your own AWS, Vercel and model usage (the README estimates about US$0.17 of model usage per weekday). Checked 2026-11-17. |
| Jev evidence | [`ingest/pipette/jev.py`](https://github.com/ferced/pipette/blob/df812dcfc01b26d78cb70317be49a48309446266/ingest/pipette/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ferced](https://github.com/ferced). Independently curated. |
| Format | Web app (Next.js) with a daily AWS Lambda pipeline (Python), MIT |
| Platform and availability | Web (pipette.day, English and Spanish); RSS feeds and a public JSON API |
| Jev's role | Jev labels and helps rank every paper with ten typed questions, checks each summary sentence against the abstract, and ranks papers for a reader's own interest sentence. |
| Requirements | Hosted at pipette.day; self-hosting needs AWS (Lambda, S3, Bedrock), Vercel and `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/ferced/pipette/blob/df812dcfc01b26d78cb70317be49a48309446266/LICENSE) |

## When to use

- Skim the day's new research across fields, with the authors' result sentence and Jev's labels shown.
- Mismatch: a literature-review or citation tool; it covers each day's new papers only.

## How it works

`ingest/pipette/jev.py` posts each paper's title and numbered abstract sentences with ten questions to `https://api.typesafe.ai/v1/systemone` (`jev-latest`); `web/app/api/rank/route.ts` sends the reader's interest sentence and the day's papers to Jev for the For you ranking. Integration evidence: [`ingest/pipette/jev.py`](https://github.com/ferced/pipette/blob/df812dcfc01b26d78cb70317be49a48309446266/ingest/pipette/jev.py).

## Get started

Read it at pipette.day, or run the pipeline yourself with your own keys.

```sh
git clone https://github.com/ferced/pipette && cd pipette
# see README: ingest/ (daily Lambda, Python) and web/ (Next.js)
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Live site: [pipette.day](https://pipette.day)
- Method (public questions and ranking rule): [pipette.day/data/v1/method.json](https://pipette.day/data/v1/method.json)
- README: [github.com/ferced/pipette/blob/df812dcfc01b26d78cb70317be49a48309446266/README.md](https://github.com/ferced/pipette/blob/df812dcfc01b26d78cb70317be49a48309446266/README.md)

## Limits and data handling

The hosted site has no accounts; saved papers and interests stay in your browser, and the For you sentence is sent to Jev on the site's key. Summaries are machine-written (labelled) and secondary to the quoted abstract. Preprints are marked as not peer-reviewed.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit df812dcfc01b](https://github.com/ferced/pipette/tree/df812dcfc01b26d78cb70317be49a48309446266). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
