# bilterm-visual-regression (semantic visual regression tests for a terminal UI, where Jev locates, classifies and checks rendered frames)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Out-of-band test harness for the bilterm terminal emulator: instead of pixel-diff snapshots, rendered frames are sent to Jev with a `box` question to locate the sessions drawer and status bar, `choice` questions for pane layout, theme and style, and a `noul` assertion for drawer visibility. Ships 8 real frames, recorded live responses, 89 offline tests and a report of measured accuracy (theme detection on nord was unreliable).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/bsommers/bilterm-visual-regression) |
| Maintainer | [bsommers](https://github.com/bsommers). Independently curated. |
| Format | Python package and CLI `bilterm-vr` (Apache-2.0) |
| Requirements | Python, `pip install -e '.[dev]'`; a TypeSafe key with image access for live runs (offline tests use a mock). |
| License | [Apache-2.0](https://github.com/bsommers/bilterm-visual-regression/blob/851dacf15407d84568e9ed3f09df15790a5ebe34/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/bilterm_vr/client.py`](https://github.com/bsommers/bilterm-visual-regression/blob/851dacf15407d84568e9ed3f09df15790a5ebe34/src/bilterm_vr/client.py) at the pinned commit. |

## When to use

- Replace brittle pixel snapshots of a GUI or TUI with coarse semantic checks.
- Mismatch: exact rendering checks, or CI gates that must run without network calls.

## How it works

`src/bilterm_vr/client.py` posts to TypeSafe's `/v1/systemone` (following the published `openapi.json`) with `jev-latest` and the `TypeSafe-Danger-Zone-Images: true` header for image input; `MockTypeSafeClient` runs the same assertions offline, and `tests/test_live_recordings.py` replays recorded Jev answers to pin measured accuracy. Integration evidence: [`src/bilterm_vr/client.py`](https://github.com/bsommers/bilterm-visual-regression/blob/851dacf15407d84568e9ed3f09df15790a5ebe34/src/bilterm_vr/client.py).

## Get started

Install and run the offline tests, then inspect a frame in mock or live mode.

```sh
git clone https://github.com/bsommers/bilterm-visual-regression && cd bilterm-visual-regression
pip install -e '.[dev]'
pytest -v
bilterm-vr fixtures/real/modern__nord__drawer.png --mock --verify-drawer visible
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/bsommers/bilterm-visual-regression/blob/851dacf15407d84568e9ed3f09df15790a5ebe34/README.md](https://github.com/bsommers/bilterm-visual-regression/blob/851dacf15407d84568e9ed3f09df15790a5ebe34/README.md)
- Report: [github.com/bsommers/bilterm-visual-regression/blob/851dacf15407d84568e9ed3f09df15790a5ebe34/docs/REPORT.md](https://github.com/bsommers/bilterm-visual-regression/blob/851dacf15407d84568e9ed3f09df15790a5ebe34/docs/REPORT.md)

## Limits and data handling

Live runs send rendered PNG frames to TypeSafe on your key. The author reports theme detection on nord as unreliable (4/15) and the status-bar box as coarse.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 851dacf15407](https://github.com/bsommers/bilterm-visual-regression/tree/851dacf15407d84568e9ed3f09df15790a5ebe34). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
