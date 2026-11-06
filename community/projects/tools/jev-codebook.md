# jev-codebook (apply a qualitative codebook to open-ended answers with Jev and a human review queue)

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Python 3.11+ stdlib toolkit that turns each codebook entry into a typed yes/no Jev question, emits per-code probabilities, frequency tables with intervals, and an export/apply review queue that fingerprints rows so stale reviews are rejected.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gbesse/jev-codebook) |
| Maintainer | [gbesse](https://github.com/gbesse). Independently curated. |
| Format | Python 3.11+ CLI/library (MIT; stdlib only) |
| Requirements | Python 3.11+ and `TYPESAFE_API_KEY` for live coding (offline fixtures available). |
| License | [MIT](https://github.com/gbesse/jev-codebook/blob/6f602ec9ec7ca4b6461d9d327f2c21e5725f5aaf/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_codebook/client.py`](https://github.com/gbesse/jev-codebook/blob/6f602ec9ec7ca4b6461d9d327f2c21e5725f5aaf/src/jev_codebook/client.py) at the pinned commit. |

## When to use

- Code survey answers or interview excerpts against an explicit codebook.
- Keep a re-importable human review loop with fingerprints.
- Mismatch: not a generative labeler; thresholds stay in your code.

## How it works

`src/jev_codebook/client.py` posts to `https://api.typesafe.ai/v1/systemone` with a minimal stdlib client, validation, fake provider and rate limits. Integration evidence: [`src/jev_codebook/client.py`](https://github.com/gbesse/jev-codebook/blob/6f602ec9ec7ca4b6461d9d327f2c21e5725f5aaf/src/jev_codebook/client.py).

## Get started

Clone and run the offline review-roundtrip example, then set a key for live coding.

```sh
git clone https://github.com/gbesse/jev-codebook.git && cd jev-codebook
PYTHONPATH=src python3 -m examples.review_roundtrip
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/gbesse/jev-codebook/blob/6f602ec9ec7ca4b6461d9d327f2c21e5725f5aaf/README.md](https://github.com/gbesse/jev-codebook/blob/6f602ec9ec7ca4b6461d9d327f2c21e5725f5aaf/README.md)

## Limits and data handling

Answer text is sent to TypeSafe on your key. Public alpha; human review remains required for uncertain rows.

## Review and maintenance

Reviewed **2026-11-06** (Europe/Sofia) at [commit 6f602ec9ec7c](https://github.com/gbesse/jev-codebook/tree/6f602ec9ec7ca4b6461d9d327f2c21e5725f5aaf). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
