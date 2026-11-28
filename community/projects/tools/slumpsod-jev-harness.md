# jev-harness by slumpsod (multi-persona agent harness where Jev gates which persona, memory and skills a worker model sees)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Multi-persona agent harness: before any worker model runs, Jev routes the request to a persona, gates which memories it may see, picks skills and suggests collaborators, so the worker (any LLM: LM Studio, llama.cpp, vLLM, Claude) sees only the request and what Jev let through, and acts by writing Python in a sandboxed REPL. Includes a dashboard, browser and desktop tools, cron jobs and a large set of live and offline evals.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/slumpsod/jev-harness) |
| Maintainer | [slumpsod](https://github.com/slumpsod). Independently curated. |
| Format | Python CLI (`jevh`) + web dashboard |
| Requirements | Python; a local System One server (bundled `openjev/` scripts) or a TypeSafe API key for hosted Jev; a worker LLM. |
| License | No licence file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevh/decide.py`](https://github.com/slumpsod/jev-harness/blob/d777fc3d0023463a669e5e815942f374a6507e82/jevh/decide.py) at the pinned commit. |

## When to use

- Builders of local multi-agent assistants who want a cheap gatekeeper deciding context before an LLM runs.
- Mismatch: a small library; this is a full personal harness with many moving parts.

## How it works

`jevh/decide.py` sends one batched `/v1/systemone` call per decision to the configured endpoint: the local adapter by default, or hosted Jev at `https://api.typesafe.ai` with `TYPESAFE_API_KEY` (see SETUP.md). Thresholds come from the routing, memory and skill evals in `evals/`. Integration evidence: [`jevh/decide.py`](https://github.com/slumpsod/jev-harness/blob/d777fc3d0023463a669e5e815942f374a6507e82/jevh/decide.py).

## Get started

Follow SETUP.md to choose local or hosted Jev, then start the chat or dashboard.

```sh
git clone https://github.com/slumpsod/jev-harness && cd jev-harness
# see SETUP.md; for hosted Jev: export TYPESAFE_API_KEY=...
jevh             # chat
jevh dashboard
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Architecture: [github.com/slumpsod/jev-harness/blob/main/docs/architecture/README.md](https://github.com/slumpsod/jev-harness/blob/main/docs/architecture/README.md)
- Setup: [github.com/slumpsod/jev-harness/blob/main/SETUP.md](https://github.com/slumpsod/jev-harness/blob/main/SETUP.md)

## Limits and data handling

The desktop tool drives the mouse and keyboard; browser and device tools act on real sites and machines. Requests go to whichever Jev endpoint and worker models you configure. Several evals are marked unverified in the README. No licence file, so no reuse rights are granted.

## Review and maintenance

Reviewed **2026-11-28** (Europe/Sofia) at [commit d777fc3d0023](https://github.com/slumpsod/jev-harness/tree/d777fc3d0023463a669e5e815942f374a6507e82). Inspected the README, SETUP.md, `jevh/decide.py` and `jevh/tools/_pick.py` at the pinned commit; no licence file present. Not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
