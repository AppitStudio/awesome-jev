# loadline by d-station-grid (Apple Watch training dashboard where Jev checks each line a 3D avatar says in your weekly review)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A web app that imports Apple Watch workouts (through the Health Auto Export iOS app) and shows fitness, fatigue and VO2max on one dashboard. Once a week a 3D VRM avatar speaks a short review of the week and offers two or three options for the next one. Code judges fatigue and load against your own past nine weeks, Gemini writes the line and the options, and Jev checks the line before the avatar is allowed to say it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/d-station-grid/loadline) |
| Tags | `Open source` · `Pricing unverified` |
| Product homepage | [Product homepage](https://api-qbvpsx77dq-an.a.run.app) |
| Pricing and access | Hosted beta with a no-sign-up guest demo ([app](https://api-qbvpsx77dq-an.a.run.app)); no pricing page or plan terms were found, so hosted access terms are unverified. The AGPL-3.0 source build has no purchase fee; self-hosting needs your own Gemini (Vertex AI), TypeSafe, Firebase and database setup. Checked 2026-11-23. |
| Jev evidence | [`api/app/adapters/jev.py`](https://github.com/d-station-grid/loadline/blob/33194fe5931e2776847ae13bac87ea1c6618c59c/api/app/adapters/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/cardilife_app/status/2124715937320583345)). |
| Maintainer | [d-station-grid](https://github.com/d-station-grid). Independently curated. |
| Format | Web app (React + FastAPI) |
| Platform and availability | Web (React frontend, FastAPI backend on Cloud Run); hosted beta and source build. Workout import needs an iPhone with Apple Watch data. |
| Jev's role | Jev returns Noul probabilities that the avatar's drafted line pushes you too hard, gives medical advice or recommends more training, picks a matching facial expression (Choice), and separately checks whether your weekly notes mention pain or illness. Code reads the probabilities; at 0.35 or higher, or if Gemini or Jev fails, a prepared fallback line is used. |
| Requirements | For self-hosting: Docker (PostgreSQL), Python 3.12 with uv, Node.js, a Gemini on Vertex AI project, a TypeSafe API key and Firebase Authentication. |
| License | [AGPL-3.0](https://github.com/d-station-grid/loadline/blob/33194fe5931e2776847ae13bac87ea1c6618c59c/LICENSE) |

## When to use

- See how an LLM-written coaching line can be gated by calibrated Jev checks before a user hears it, with code-owned thresholds and fallbacks.
- Mismatch: medical or coaching advice; the app reviews training load only, and the main README is in Japanese.

## How it works

`api/app/adapters/jev.py` uses the official `typesafe_sdk` (`AsyncTypeSafeClient` with `Noul` and `Choice` questions, model `jev-latest` by default from `api/app/core/config.py`). It waits once with SDK retries turned off and returns nothing on failure, timeout or an unexpected answer, so the caller switches to a fixed line. The thresholds live in `app/domain/line_check` and `note_check`, not in the adapter. Integration evidence: [`api/app/adapters/jev.py`](https://github.com/d-station-grid/loadline/blob/33194fe5931e2776847ae13bac87ea1c6618c59c/api/app/adapters/jev.py).

## Get started

Try the hosted beta with "Try as a guest" (demo data, no sign-up), or run it locally from the repository root.

```sh
git clone https://github.com/d-station-grid/loadline && cd loadline
docker compose up -d   # PostgreSQL
make dev               # API on :8000, frontend on :5173
make check             # lint, type check and tests
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted beta (guest demo): [api-qbvpsx77dq-an.a.run.app](https://api-qbvpsx77dq-an.a.run.app)
- Design article, How much should an LLM decide?: [dev.to/iotarduino/how-much-should-an-llm-decide-building-an-avatar-that-reviews-your-training-week-with-fastapi-40fg](https://dev.to/iotarduino/how-much-should-an-llm-decide-building-an-avatar-that-reviews-your-training-week-with-fastapi-40fg)
- English README: [github.com/d-station-grid/loadline/blob/33194fe5931e2776847ae13bac87ea1c6618c59c/README.en.md](https://github.com/d-station-grid/loadline/blob/33194fe5931e2776847ae13bac87ea1c6618c59c/README.en.md)

## Limits and data handling

Drafted lines and weekly notes are sent to TypeSafe for checks and workout summaries to Gemini; workouts are stored in the app's PostgreSQL database (Neon in the hosted beta) with Firebase sign-in. Hosted beta terms and pricing were not found. AGPL-3.0, except the sample avatar model (VRM Public License 1.0).

## Review and maintenance

Reviewed **2026-11-23** (Europe/Sofia) at [commit 33194fe5931e](https://github.com/d-station-grid/loadline/tree/33194fe5931e2776847ae13bac87ea1c6618c59c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
