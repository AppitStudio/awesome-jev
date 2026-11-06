# jev-screen (title/abstract screening for systematic reviews with Jev include/exclude/maybe buckets)

[All projects](../README.md) · [Search and retrieval](README.md#search-and-retrieval)

Python 3.11+ stdlib screener that judges bibliographic records against explicit inclusion and exclusion criteria with TypeSafe Jev, routes `maybe` rows to humans, and reports PRISMA counts, RIS exports and recall intervals. Positioned as a second screener, never a sole decider.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-screen) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python 3.11+ CLI (MIT; stdlib only) |
| Requirements | Python 3.11+ and `TYPESAFE_API_KEY` for live screening (offline fixtures available). |
| License | [MIT](https://github.com/gbesse/jev-screen/blob/9f663beafb33264521a217770f9aea6815fbc8ad/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_screen/cli.py`](https://github.com/gbesse/jev-screen/blob/9f663beafb33264521a217770f9aea6815fbc8ad/src/jev_screen/cli.py) at the pinned commit. |

## When to use

- Prioritize title/abstract screening for a systematic review.
- Need PRISMA-style counts and a human maybe queue.
- Mismatch: not a sole inclusion authority; recall on small pilots proves little.

## How it works

The CLI posts title/abstract state with criterion questions to TypeSafe Jev and writes decisions plus export artifacts. Integration evidence: [`src/jev_screen/cli.py`](https://github.com/gbesse/jev-screen/blob/9f663beafb33264521a217770f9aea6815fbc8ad/src/jev_screen/cli.py).

## Get started

Clone and run the offline demo, then estimate cost before a live screen.

```sh
git clone https://github.com/gbesse/jev-screen.git && cd jev-screen
PYTHONPATH=src python -m examples.offline_demo
export TYPESAFE_API_KEY=...
jev-screen estimate records.ris --criteria criteria.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-screen/blob/9f663beafb33264521a217770f9aea6815fbc8ad/README.md](https://github.com/gbesse/jev-screen/blob/9f663beafb33264521a217770f9aea6815fbc8ad/README.md)

## Limits and data handling

Titles and abstracts are sent to TypeSafe on your key. Public alpha.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 9f663beafb33](https://github.com/gbesse/jev-screen/tree/9f663beafb33264521a217770f9aea6815fbc8ad). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
