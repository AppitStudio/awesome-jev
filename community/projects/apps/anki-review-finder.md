# Anki Review-Finder

[All projects](../README.md) · [Command-line apps](README.md#command-line-apps)

Alpha CLI that audits Anki flashcards through AnkiConnect with TypeSafe Jev, flagging structural defects such as answer leaks, missing context, scope problems and binary questions, then writes priority and defect tags back to Anki (never card text) and produces an HTML report.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/elias170105/anki-review-finder) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/elias170105/anki-review-finder#readme) (source-built app; no separate website verified). |
| Pricing and access | No fee for the MIT source; requires your own TypeSafe key in `.env` (usage billed by TypeSafe). Checked 2026-10-08. |
| Jev evidence | [`mainanki.py`](https://github.com/elias170105/anki-review-finder/blob/df16ad70169cf457b7888f12c23b28a3250d37b0/mainanki.py) sends card fields to Jev and maps answers to tags; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [elias170105](https://github.com/elias170105). Independently curated. |
| Format | Python CLI (`mainanki.py`) |
| Platform and availability | Any desktop OS running Anki Desktop with the AnkiConnect add-on; Python 3.9+. |
| Jev's role | Classifies each card for defect patterns; tag writing and reporting are code. |
| Requirements | Python 3.9+, Anki Desktop with AnkiConnect (add-on 2055492159), and `JEV_API_KEY` in `.env`. |
| License | [MIT](https://github.com/elias170105/anki-review-finder/blob/df16ad70169cf457b7888f12c23b28a3250d37b0/LICENSE). |

## When to use

- Find weak flashcards in a large deck before your next review session.
- Run `--dry-run --report` first to see results without changing tags.
- Mismatch: alpha; heuristics and tag names may change. Back up your collection first.

## How it works

The script reads cards via AnkiConnect, asks Jev typed questions about each card concurrently (with 429 backoff), assigns `high` / `medium` / `low` review priority and defect tags, and writes an HTML report of latencies and token use.

## Get started

Install and do a dry run (README):

```sh
git clone https://github.com/elias170105/anki-review-finder.git && cd anki-review-finder
pip install -r requirements.txt
echo 'JEV_API_KEY=...' > .env
python mainanki.py --deck "MyDeck" --dry-run --report
```

Each card evaluated is a Jev request billed to your TypeSafe key.

## Examples and demos

- README *Usage* (test run and live run).

## Limits and data handling

Card fields go to TypeSafe; only tags are written back to Anki. Upstream discloses AI-assisted development. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit df16ad70169c](https://github.com/elias170105/anki-review-finder/tree/df16ad70169cf457b7888f12c23b28a3250d37b0). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
