# Live Jev

[All projects](../README.md) · [Apps](README.md) · [macOS apps](README.md#macos-apps)

macOS controller for Ableton Live: a hotkey bar takes a short English or Japanese phrase, TypeSafe Jev picks typed mixer/device/transport actions, and a Live Remote Script applies them locally.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/okinaaudio/live-jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [live-jev project homepage](https://github.com/okinaaudio/live-jev) — source-built app; no separate product website. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-20**. Requires a TypeSafe key (`TYPESAFE_API_KEY`). Ableton Live 12 and Apple Silicon macOS 14+ are required. Provider usage can incur charges; free-tier eligibility was not verified. |
| Jev evidence | Inspected [`daemon.py`](https://github.com/okinaaudio/live-jev/blob/a91a8cdd621f24cad6aaff347f988d3ed5ae579f/daemon.py) posting to `https://api.typesafe.ai/v1/systemone`. Live Ableton control was not tested on the Linux review host. |
| Disclosure | Free source access does not include inference. Early **0.1x** source distribution (no packaged installer yet). AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. |
| Maintainer | [okinaaudio](https://github.com/okinaaudio). |
| Format | Swift AppKit bar + Python 3.13 daemon + Ableton Remote Script (`LiveJev`). |
| Platform and availability | Apple Silicon Mac, macOS 14+, Ableton Live 12. Early source build via `scripts/build-app.sh`; restart Live after selecting the Remote Script. |
| Jev's role | Chooses among typed Live actions from short phrases; fixed phrases can be answered locally without Jev. No general LLM in the command path; unclear phrases ask the user. Code drives Live over localhost. |
| Requirements | Homebrew, Xcode Command Line Tools, Python 3.13, `TYPESAFE_API_KEY`, Ableton User Library Remote Scripts slot. |
| License | [MIT](https://github.com/okinaaudio/live-jev/blob/a91a8cdd621f24cad6aaff347f988d3ed5ae579f/LICENSE). |

## When to use

Use it for hands-on Ableton mixer, transport, clip, note, and device control from short spoken or typed phrases. Prefer [Jev Voice](jev-voice.md) or [TipTour](tiptour.md) for general macOS automation outside Live.

## How it works

The Swift bar collects a phrase; the Python daemon asks Jev (or a local phrase table) for structured actions, then the Remote Script mutates the Live set over a local socket. Multi-part commands are validated before run and can roll back on later failure. Only TypeSafe traffic leaves the machine for judgment calls.

## Get started

Upstream [INSTALL.md](https://github.com/okinaaudio/live-jev/blob/a91a8cdd621f24cad6aaff347f988d3ed5ae579f/INSTALL.md) is the authoritative macOS path. Offline tests on the review host:

```sh
git clone https://github.com/okinaaudio/live-jev.git
cd live-jev
git checkout a91a8cdd621f24cad6aaff347f988d3ed5ae579f
python3 -m pytest -q
```

Building the app and controlling Live need macOS + Ableton and incur TypeSafe usage for non-local phrases. This review did not build the Swift app or drive Live.

## Examples and demos

- Upstream README phrase examples (mixer, transport, devices, multi-track, Japanese).
- Offline suite under [`tests/`](https://github.com/okinaaudio/live-jev/tree/a91a8cdd621f24cad6aaff347f988d3ed5ae579f/tests).

## Limits and data handling

Phrases and candidate action context go to TypeSafe when Jev is called. Live traffic stays on `127.0.0.1`. Early release: no installer; keep the clone where the built app expects `daemon.py`. Undo is available but treat session changes carefully. Timing claims in the README are upstream anecdotes.

## Review and maintenance

Reviewed on **2026-09-20** at [commit a91a8cd](https://github.com/okinaaudio/live-jev/tree/a91a8cdd621f24cad6aaff347f988d3ed5ae579f): early **0.1x**, MIT. AI-assisted source review of `daemon.py`, Remote Script layout, README, and license. On Python 3.12+, **`pytest -q`: 325 passed, 1 skipped (518 subtests)**. No macOS build, Ableton session, or live TypeSafe calls were performed.

Related: [Jev Voice](jev-voice.md), [TipTour](tiptour.md), [macbrow](macbrow.md).
