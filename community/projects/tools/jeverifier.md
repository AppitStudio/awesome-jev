# JeVerifier

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Coding harness that puts TypeSafe Jev under a Claude session for reading lists, session digests, doc contradiction checks, and code rule checks—Jev only selects/ranks/labels; Claude reviews.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/silvariasereneblossom/jeverifier) |
| Maintainer | [silvariasereneblossom](https://github.com/silvariasereneblossom). Independently curated. |
| Format | Python package (`jeverifier`) + optional Tk keys UI. |
| Requirements | Python 3 + venv; TypeSafe API key; Claude coding session. Linux/macOS/Windows setup documented. |
| License | [MIT](https://github.com/silvariasereneblossom/jeverifier/blob/88da49fb379b005688c30576576315acade70a79/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live provider paths were not exercised on the review host. |

## When to use

Use to **cheaply point Claude at the docs/rules that matter** and re-check only what changed after a full review.

## How it works

Jev builds reading lists and runs contradiction/rule checks; Claude performs the expensive reading. Reviews are recorded to avoid paying twice. Wiki reports measured token effects (upstream).

## Get started

```sh
git clone https://github.com/silvariasereneblossom/jeverifier.git
cd jeverifier
git checkout 88da49fb379b005688c30576576315acade70a79
python3 -m venv .venv && .venv/bin/pip install -e ".[dev]"
source .venv/bin/activate
```

## Examples and demos

- Wiki [Token savings](https://github.com/silvariasereneblossom/jeverifier/wiki/Token-Savings).
- README milestone findings (stale docs / contract errors)—upstream-reported.

## Limits and data handling

Doc and code excerpts may be sent to TypeSafe. Token-savings numbers are author-measured, not re-run here.

## Review and maintenance

Reviewed **2026-09-25** (Europe/Sofia) at [commit 88da49f](https://github.com/silvariasereneblossom/jeverifier/tree/88da49fb379b005688c30576576315acade70a79). AI-assisted README and LICENSE inspection; live TypeSafe/provider integration paths not run.

Related: [jev-seatbelts](jev-seatbelts.md).
