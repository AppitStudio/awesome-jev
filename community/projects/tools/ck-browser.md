# ck-browser (plain-language browser checks)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Runs browser checks written as plain-language steps in a real Chrome, with Jev picking each element from a DOM snapshot and deciding whether the page has settled, and writes per-step probabilities, timings, cost and screenshots.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/luv-agarwal/ck-browser) |
| Maintainer | [luv-agarwal](https://github.com/luv-agarwal). Independently curated. |
| Format | CLI (Python 3.11+ standard library only) |
| Requirements | Python 3.11+, Chrome or Chromium, `TYPESAFE_API_KEY` (or `--stub` for the offline matcher). |
| License | [MIT](https://github.com/luv-agarwal/ck-browser/blob/0de2c408aff9aacef8cfb09ae029bc1e4c99de5f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`ck_browser/model.py`](https://github.com/luv-agarwal/ck-browser/blob/0de2c408aff9aacef8cfb09ae029bc1e4c99de5f/ck_browser/model.py) at the pinned commit. |

## When to use

- Let coding agents verify a flow in fewer browser calls and less context.
- Write checks like "fill Username" and "expect You logged into a secure area!" without selectors.
- Mismatch: not faster end to end per the README; the gain is fewer calls.

## How it works

Each step's decision goes to Jev at `api.typesafe.ai` (`ck_browser/model.py`) as a calibrated pick over candidate elements from the DOM snapshot, never pixels; every run writes `run.json` and a `jev-trace.jsonl`. Integration evidence: [`ck_browser/model.py`](https://github.com/luv-agarwal/ck-browser/blob/0de2c408aff9aacef8cfb09ae029bc1e4c99de5f/ck_browser/model.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/luv-agarwal/ck-browser && cd ck-browser
export TYPESAFE_API_KEY=your-key
bin/ck-browser doctor
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example flows (in the clone): [github.com/luv-agarwal/ck-browser/tree/main/examples](https://github.com/luv-agarwal/ck-browser/tree/main/examples)
- Agent skill: [github.com/luv-agarwal/ck-browser/tree/main/skills](https://github.com/luv-agarwal/ck-browser/tree/main/skills)

## Limits and data handling

DOM snapshots of tested pages are sent to TypeSafe. Comparison numbers are the author's. Not on PyPI.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit 0de2c408aff9](https://github.com/luv-agarwal/ck-browser/tree/0de2c408aff9aacef8cfb09ae029bc1e4c99de5f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
