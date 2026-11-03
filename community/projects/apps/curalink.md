# Curalink (medical research assistant where Jev routes each question to live PubMed and trial search or to saved conversation evidence and picks the 8B or 70B answer model)

[All projects](../README.md) · [Web apps](README.md#web-apps)

Medical research assistant for patients and caregivers: enter a condition and goal once, then ask questions, compare findings and open the PubMed, OpenAlex and ClinicalTrials.gov sources behind each answer. When a TypeSafe key is set, Jev decides whether a question needs fresh retrieval or can be answered from the saved conversation, whether the form's disease still applies, and whether an 8B or 70B Llama writes the answer; without a key the original single-model pipeline runs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/VIVPM/curalink-medical-assistant) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Product homepage](https://curalink-medical-assistant-frontend.onrender.com) |
| Pricing and access | Free source build under MIT; you supply Hugging Face or Cloudflare keys and a TypeSafe key for Jev routing, plus hosting. The hosted demo's terms were not verified. Checked 2026-11-03. |
| Jev evidence | [`backend-python/stages/query_router.py`](https://github.com/VIVPM/curalink-medical-assistant/blob/52ad2d56381f7d0d03dd4809fcaf050dae4b2ee1/backend-python/stages/query_router.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/VIVEKPM99/status/2117595151212400798)). |
| Maintainer | [VIVPM](https://github.com/VIVPM). Independently curated. |
| Format | Web app (React/Vite frontend, Express API, FastAPI research pipeline; Docker) |
| Platform and availability | Self-hosted web app; a hosted demo is linked from the repository. |
| Jev's role | Optional router that chooses retrieval or saved-evidence answering and the 8B or 70B answer model. |
| Requirements | Node and Python services plus Postgres/Redis; a Hugging Face or Cloudflare Workers AI key for answers; optionally `JEV_API_KEY` (TypeSafe) for Jev routing. |
| License | [MIT](https://github.com/VIVPM/curalink-medical-assistant/blob/52ad2d56381f7d0d03dd4809fcaf050dae4b2ee1/LICENSE) |

## When to use

- Explore published research and trial listings for a condition with sources beside each finding.
- Mismatch: it is for exploring research, not diagnosis, treatment decisions or emergencies, and Jev routing is optional.

## How it works

`backend-python/stages/query_router.py` posts the intake context, the current question and up to six prior messages to `https://api.typesafe.ai/v1/systemone` as three typed choice questions (route, model tier, topic); Python enforces first-turn retrieval, falls back to retrieval plus the 70B model when Jev is missing or invalid, and keeps the Jev route and confidence in `pipelineMeta.routing`. Integration evidence: [`backend-python/stages/query_router.py`](https://github.com/VIVPM/curalink-medical-assistant/blob/52ad2d56381f7d0d03dd4809fcaf050dae4b2ee1/backend-python/stages/query_router.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/VIVPM/curalink-medical-assistant.git
cd curalink-medical-assistant
# start the Node, Python and frontend services as described in the README's "Running Locally";
# set JEV_API_KEY in backend-python/.env to turn on Jev routing
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Hosted demo (availability and terms not verified): [curalink-medical-assistant-frontend.onrender.com](https://curalink-medical-assistant-frontend.onrender.com)
- README with the pipeline, routing rules and evaluation notes: [github.com/VIVPM/curalink-medical-assistant#readme](https://github.com/VIVPM/curalink-medical-assistant#readme)

## Limits and data handling

Jev sees the intake context, the question and bounded history (up to 24,000 characters), not account IDs or inference keys, and free text is not de-identified, so do not enter identifiable patient information. The README's 150-question evaluation (judged by Gemini 3.5 Flash-Lite) is the author's own and does not test the Jev routing; confidence thresholds and routing-quality evaluation are deferred. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 52ad2d56381f](https://github.com/VIVPM/curalink-medical-assistant/tree/52ad2d56381f7d0d03dd4809fcaf050dae4b2ee1). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
