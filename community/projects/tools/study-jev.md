# study-jev by Y. Yamashiro (seven single-page Jev studies: latency, Cloudflare Workers AI, per-keystroke classifiers and yes/no gates)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Collection of small single-page Jev demos: round-trip latency measurement with statistics, the same on Cloudflare Workers AI over IPv4 or IPv6, a per-keystroke Japanese snack-name classifier, a handwriting recognizer that rasterizes strokes to ASCII art, Score versus Noul on the same input, a Three Laws of Robotics gate built from five `noul` questions and a PARANOIA-themed screening audit.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/uist1idrju3i/study-jev) |
| Maintainer | [Y. Yamashiro](https://github.com/uist1idrju3i). Independently curated. |
| Format | Static HTML pages + small Python local servers |
| Requirements | A browser and a TypeSafe API key (or a Cloudflare account for study 0002). |
| License | [BSD-3-Clause](https://github.com/uist1idrju3i/study-jev/blob/e9ae855829e06faa37850ffdaf903fcd6a361f34/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`study-0001-rtt/index.html`](https://github.com/uist1idrju3i/study-jev/blob/e9ae855829e06faa37850ffdaf903fcd6a361f34/study-0001-rtt/index.html) at the pinned commit. |

## When to use

- Developers who want tiny, readable examples of Jev question types and real latency numbers.
- Mismatch: production code; these are studies.

## How it works

Each page, such as `study-0001-rtt/index.html`, calls `https://api.typesafe.ai/v1/systemone` from the browser with a key held only in page memory and shows probabilities and timings; some studies include a small `serve.py`. Integration evidence: [`study-0001-rtt/index.html`](https://github.com/uist1idrju3i/study-jev/blob/e9ae855829e06faa37850ffdaf903fcd6a361f34/study-0001-rtt/index.html).

## Get started

Clone and open a study page, then paste your key.

```sh
git clone https://github.com/uist1idrju3i/study-jev && cd study-jev/study-0001-rtt
python3 serve.py   # or open index.html; paste your TypeSafe key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Three Laws gate: [github.com/uist1idrju3i/study-jev/tree/main/study-0006-three-laws](https://github.com/uist1idrju3i/study-jev/tree/main/study-0006-three-laws)
- Cloudflare study: [github.com/uist1idrju3i/study-jev/tree/main/study-0002-cloudflare](https://github.com/uist1idrju3i/study-jev/tree/main/study-0002-cloudflare)

## Limits and data handling

Your key is used from the browser and every keystroke study sends a request per input change, which adds up in cost. Some notes are in Japanese.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit e9ae855829e0](https://github.com/uist1idrju3i/study-jev/tree/e9ae855829e06faa37850ffdaf903fcd6a361f34). Inspected the README, LICENSE and the study pages at the pinned commit; nothing was run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
