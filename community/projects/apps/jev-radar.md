# Jev Radar

[All projects](../README.md) · [Apps](README.md) · [Web apps](README.md#web-apps)

Local research workspace: Jev steers investigation steps over public sources while optional text models propose questions and draft answers for Jev to check.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Eliovp-BV/Jev-Radar) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Jev Radar repository](https://github.com/Eliovp-BV/Jev-Radar) — local web UI; no separate hosted product. |
| Pricing and access | MIT source has no app purchase fee, checked **2026-09-19**. Requires `TYPESAFE_API_KEY`; automatic discovery also needs `BRAVE_SEARCH_API_KEY`. Optional text-provider keys. Default spend ceilings (**$5 Jev / $20 text model per investigation**) are estimated limits in Settings, not billing guarantees. Search and provider usage can incur charges. |
| Jev evidence | Inspected [backend/radar/research.py](https://github.com/Eliovp-BV/Jev-Radar/blob/ee248944cb16ff4d12a9b4e38a62a2cc45b0fdc0/backend/radar/research.py) and related modules importing `typesafe_sdk` (`Choice`/`Score`/`Noul`); [test_core.py](https://github.com/Eliovp-BV/Jev-Radar/blob/ee248944cb16ff4d12a9b4e38a62a2cc45b0fdc0/tests/test_core.py) mocks `AsyncTypeSafeClient` against `api.typesafe.ai`. Live investigations were not run. |
| Disclosure | Free source access does not include inference or search. AI-assisted, independently curated listing; no commercial relationship was declared. Inclusion is not endorsement. Implementation reviewed from public source. |
| Maintainer | [Eliovp BV](https://github.com/Eliovp-BV). |
| Format | Local FastAPI + front-end research app (`./scripts/run.sh` → local UI on port 8787). |
| Platform and availability | Linux, macOS, or WSL. Python 3.11+, Node.js 22.12+ (or Node 20.19+ within Node 20). Experimental local tool; no login—bind to localhost on untrusted networks. |
| Jev's role | Selects research methods, accepts/declines proposed questions and searches, chooses leads to inspect, assesses evidence, and checks answer claims. Search/browser tools fetch public content; an optional text model proposes questions and drafts synthesis for Jev to verify. |
| Requirements | Keys above; optional Chromium via `./scripts/install.sh --with-browser` for JS-rendered pages. |
| License | [MIT](https://github.com/Eliovp-BV/Jev-Radar/blob/ee248944cb16ff4d12a9b4e38a62a2cc45b0fdc0/LICENSE). |

## When to use

Run competitive/landscape research, claim investigation, or evidence-linked comparisons where you want every Jev decision inspectable with source passages. Prefer simpler single-shot classifiers when you do not need multi-step discovery and spend controls.

## How it works

Radar enforces budgets and acquisition rules, shows activity and estimated spend, and stores decisions for replay without new provider calls. Jev remains the structured decision component; Brave Search supplies discovery; optional text models assist proposals and drafting only.

## Get started

Installer creates a blank `.env`; add keys locally before research that hits the network.

```sh
git clone https://github.com/Eliovp-BV/Jev-Radar.git
cd Jev-Radar
git checkout ee248944cb16ff4d12a9b4e38a62a2cc45b0fdc0
./scripts/install.sh
# edit .env: TYPESAFE_API_KEY, BRAVE_SEARCH_API_KEY, optional text keys
./scripts/run.sh
```

Open the printed local URL (default port **8787**). **Trusted networks only** unless `RADAR_HOST=127.0.0.1`. Live research incurs TypeSafe, search, and optional text-model charges.

Offline tests (no keys required for the suite as run here):

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.in
python -m pytest -q
```

## Examples and demos

Upstream README includes a recorded demo GIF/MP4 and setup/architecture docs. Saved replay makes no new provider calls.

## Limits and data handling

Approved goals, bounded public passages, URLs, and typed questions go to TypeSafe; optional text providers receive bounded goals/evidence when enabled. Keys stay server-side. There is no authentication—anyone who can reach the bind address can start paid work. Two browser private-subrequest tests failed on this review host; treat network allowlisting as worth verifying before production use.

## Review and maintenance

Reviewed on **2026-09-19** at [commit ee24894](https://github.com/Eliovp-BV/Jev-Radar/tree/ee248944cb16ff4d12a9b4e38a62a2cc45b0fdc0): MIT. AI-assisted source review of README, `backend/radar` Jev integration points, and license. On Python 3.13.5 with a local venv, **`pytest`: 600 passed, 2 failed** (`test_browser_denies_private_subrequests` for status 200 and 404), **22 skipped**. No live investigation or TypeSafe spend was performed for this listing.

Related X discovery post: [status/2101405199827149139](https://x.com/Vpoile1/status/2101405199827149139).
