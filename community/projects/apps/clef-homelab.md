# Clef homelab decision engine

[All projects](../README.md) · [Web apps](README.md#web-apps)

Self-hosted homelab dashboard where open Clef-flash (GGUF on a 6 GB laptop GPU) answers System One questions over llama.cpp's `/v1/systemone` endpoint — the same request shape as Jev — to triage Gmail, filter news, watch ~2,350 company job boards for internships and push matches to your phone through ntfy.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/NikhileshThiru/clef) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/NikhileshThiru/clef#readme) (self-hosted; no hosted version). |
| Pricing and access | No fee; runs on your own hardware with free APIs (Gmail read-only, job boards, RSS/HN, optional Finnhub). No TypeSafe key needed. Checked 2026-10-08. |
| Jev evidence | Uses the Jev / System One request shape against a local Clef model, not hosted Jev: [`clefd/decider.py`](https://github.com/NikhileshThiru/clef/blob/17cc0fbb7c5d8a33647022d6627fa14d39cf5c9f/clefd/decider.py) posts `state` + typed `questions` to `/v1/systemone` on llama.cpp. Source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [NikhileshThiru](https://github.com/NikhileshThiru). Independently curated. |
| Format | Python daemon + Three.js web dashboard (self-hosted) |
| Platform and availability | Linux laptop/server with an NVIDIA GPU (author: RTX 3060 6 GB); dashboard in any browser on the tailnet. |
| Jev's role | Clef (System One–compatible) classifies every mail, headline and posting; code polls sources, de-duplicates and alerts. |
| Requirements | NVIDIA GPU with ~6 GB VRAM; llama.cpp v0.6.0+ built with SystemOne support and the Clef-Flash GGUF; Gmail API credentials; optional ntfy and Finnhub. |
| License | [MIT](https://github.com/NikhileshThiru/clef/blob/17cc0fbb7c5d8a33647022d6627fa14d39cf5c9f/LICENSE). |

## When to use

- Run a private, always-on stream of small decisions (mail, news, jobs) on local hardware.
- See how the System One API shape works with an open model before moving to hosted Jev.
- Mismatch: personal homelab project; setup is manual and tuned to the author's sources.

## How it works

Pollers for Gmail, ~2,350 Greenhouse/Lever/Ashby/SmartRecruiters/Workday boards, SimplifyJobs and news feeds turn events into states; one worker drains a priority queue against llama.cpp (~320 ms per decision on the author's GPU) and the dashboard animates each decision.

## Get started

Build llama.cpp with SystemOne support and follow README *Setup*:

```sh
git clone --depth 1 --branch v0.6.0 https://github.com/ggml-org/llama.cpp ~/.local/src/llama.cpp
git clone https://github.com/NikhileshThiru/clef.git && cd clef
# follow README Setup / Configuration for the model, Gmail and ntfy
```

No inference charges (local model); Gmail and job-board APIs used are free.

## Examples and demos

- README *What it does* and *Job watcher* (real output from the author's running system).

## Limits and data handling

Runs Clef, not TypeSafe Jev; mail stays local (Gmail read-only). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit 17cc0fbb7c5d](https://github.com/NikhileshThiru/clef/tree/17cc0fbb7c5d8a33647022d6627fa14d39cf5c9f). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
