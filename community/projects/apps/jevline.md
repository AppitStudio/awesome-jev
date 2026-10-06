# Jevline

[All projects](../README.md) · [Web apps](README.md#web-apps)

Incident-timeline proof of concept for security analysts: start from one confirmed-malicious process and Jev scores, process by process, which other activity belongs to the same incident, producing a reviewable timeline (web portal, local portal or CLI).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/tsale/jevline) |
| Tags | `Source available` · `Free` · `BYOK` |
| Product homepage | [jev-incident-timeline.vercel.app](https://jev-incident-timeline.vercel.app/) (hosted portal) · [Repository README](https://github.com/tsale/jevline#readme). |
| Pricing and access | Hosted portal is free to open; the bundled example can use the maintainer's demo key, your own files need your own TypeSafe key (optional OpenRouter key for narratives). Local portal uses only the Python standard library. No paid tier found. Checked 2026-10-06. |
| Jev evidence | Inspected [`jev_incident.py`](https://github.com/tsale/jevline/blob/d0fcc1a4727ab4562f3b292e13269f58647917e6/jev_incident.py) and the site relay [`api/jev.js`](https://github.com/tsale/jevline/blob/d0fcc1a4727ab4562f3b292e13269f58647917e6/api/jev.js); README documents one Jev question per candidate process and an experimental 0.8 threshold. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [tsale](https://github.com/tsale). Independently curated. |
| Format | Web portal (Vercel), local Python portal and CLI |
| Platform and availability | Any modern browser for the hosted site; Python 3.9+ for the local portal and CLI. Experimental proof of concept. |
| Jev's role | For each candidate process, Jev judges relatedness to the seed incident given selected telemetry fields and nearby context; code applies the threshold and builds the timeline. An optional OpenRouter model writes narratives. |
| Requirements | Browser, or Python 3.9+; TypeSafe API key for your own data; optional OpenRouter key. |
| License | **No LICENSE file** in the reviewed tree — publicly readable source with unspecified reuse terms; not Open source. |

## When to use

- Triage an endpoint telemetry export after confirming one malicious process, to find related activity quickly.
- Prototype how a calibrated relatedness score can support (not replace) analyst review.
- Mismatch: local JSON exports only (no SIEM queries); no accuracy claim.

## How it works

You load a JSON export, mark the starting execution and add analyst context. For every other process, Jevline sends selected fields of the seed, the candidate and context events to Jev and asks whether it belongs to the same incident; candidates above the cut-off form the timeline. On the website, Jev calls go through the site's relay; narratives go directly from the browser to OpenRouter.

## Get started

Run the local portal with your own key:

```sh
git clone https://github.com/tsale/jevline.git
cd jevline
python3 web_app.py --setup-keys   # hidden prompt, saved to .env
python3 web_app.py                # http://127.0.0.1:8765
```

Analysis makes one TypeSafe request per candidate process; narratives call OpenRouter.

## Examples and demos

- Bundled malicious-events example in the portal.
- README *What leaves your machine* table for each action.

## Limits and data handling

Upstream says it is an experimental proof of concept, not a validated detector; tests mock both providers and the 0.8 threshold is experimental. Selected telemetry fields leave your machine (TypeSafe via relay on the website). No LICENSE file. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-06** (Europe/Sofia) at [commit d0fcc1a4727a](https://github.com/tsale/jevline/tree/d0fcc1a4727ab4562f3b292e13269f58647917e6). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
