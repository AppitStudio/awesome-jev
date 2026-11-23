# jev board by rttq (local workbench for testing Jev questions, comparing wordings across inputs and tracking cost)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A local browser workbench: run single Noul, Choice, Score or Box questions, compare question wordings across many inputs in an experiment matrix, label rows to measure accuracy, and keep every request with its cost in History.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rttq/jev_board) |
| Maintainer | [rttq](https://github.com/rttq). Independently curated. |
| Format | Python app (uv) served on localhost |
| Requirements | Python with uv; a TypeSafe API key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_board/jev.py`](https://github.com/rttq/jev_board/blob/efd3fbac564e848284af104d63b03a30091d0b70/jev_board/jev.py) at the pinned commit. |

## When to use

- Tune Jev question wording against labelled examples before shipping it.
- Mismatch: production serving; it is a local experiment tool.

## How it works

`jev_board/jev.py` wraps the official `typesafe-sdk` Python client (confirmed against 0.7.5 per its notes), including image inputs for Box questions. Integration evidence: [`jev_board/jev.py`](https://github.com/rttq/jev_board/blob/efd3fbac564e848284af104d63b03a30091d0b70/jev_board/jev.py).

## Get started

Set your key and launch.

```sh
git clone https://github.com/rttq/jev_board.git && cd jev_board
export TYPESAFE_API_KEY=...
uv run jevbench   # http://127.0.0.1:8765
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with screenshots: [github.com/rttq/jev_board/blob/efd3fbac564e848284af104d63b03a30091d0b70/README.md](https://github.com/rttq/jev_board/blob/efd3fbac564e848284af104d63b03a30091d0b70/README.md)

## Limits and data handling

Inputs are sent to TypeSafe and billed to your key. No license file.

## Review and maintenance

Reviewed **2026-11-24** (Europe/Sofia) at [commit efd3fbac564e](https://github.com/rttq/jev_board/tree/efd3fbac564e848284af104d63b03a30091d0b70). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
