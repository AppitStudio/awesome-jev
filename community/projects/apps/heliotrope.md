# Heliotrope (carbon-aware load scheduler with Jev load intake)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Scheduler that shifts EV charging, water heating, laundry and pumps into low-carbon hours without missing deadlines, using OR-Tools; Jev turns plain-words load descriptions into typed load specs and ranks how essential each appliance is.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/StellarieX/Heliotrope) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/StellarieX/Heliotrope#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Hosting and TypeSafe usage are yours. Checked 2026-10-24. |
| Jev evidence | [`backend/app/services/jev_client.py`](https://github.com/StellarieX/Heliotrope/blob/415f4d775ed4c508c9d7af403c5d52891e0869db/backend/app/services/jev_client.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [StellarieX](https://github.com/StellarieX). Independently curated. |
| Format | Web app (Next.js and FastAPI) |
| Platform and availability | Self-hosted web app (Next.js front end, FastAPI backend). |
| Jev's role | Classifies loads from plain words with confidence and judges appliance importance for prioritisation; numbers and schedules stay in code. |
| Requirements | Node.js; Python; Firebase project; a TypeSafe API key for Jev features. |
| License | [MIT](https://github.com/StellarieX/Heliotrope/blob/415f4d775ed4c508c9d7af403c5d52891e0869db/LICENSE) |

## When to use

- Plan household or small-site loads around a live carbon signal.
- Turn "geyser at night" into a typed load spec.
- Mismatch: needs a Firebase setup; carbon signal is an estimate.

## How it works

`jev_client.py` posts to `{JEV_BASE_URL}/v1/systemone` (TypeSafe by default) for `/loads/classify` and `/loads/prioritize`; solvers run locally. Integration evidence: [`backend/app/services/jev_client.py`](https://github.com/StellarieX/Heliotrope/blob/415f4d775ed4c508c9d7af403c5d52891e0869db/backend/app/services/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
npm install && npm run dev
python -m pip install -e "./backend[dev]"
python -m uvicorn app.main:app --app-dir backend --port 8000
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/StellarieX/Heliotrope#readme](https://github.com/StellarieX/Heliotrope#readme)

## Limits and data handling

Load descriptions are sent to TypeSafe. Carbon intensity is labelled as an estimate.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 415f4d775ed4](https://github.com/StellarieX/Heliotrope/tree/415f4d775ed4c508c9d7af403c5d52891e0869db). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
