# Nimble Rubric Evaluator (local web app that scores written responses against your rubric, with a TypeSafe Jev cloud option)

[All projects](../README.md) · [Web apps](README.md#web-apps)

A local web app for teachers and assessors: build a rubric as a grid of criteria and levels, paste or import learners' responses, and get a level per criterion from a System One decision model. It runs nimble in Ollama by default (nothing leaves the machine), can switch to TypeSafe Jev or other cloud models, and ships a batch evaluator and benchmark against public essay datasets.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface) |
| Tags | `Source available` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build that runs locally; the default nimble model runs in Ollama at no API cost, and the optional TypeSafe Jev cloud backend uses your own key. No license file, so reuse terms are not granted. Checked 2026-11-22. |
| Jev evidence | [`index.html`](https://github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface/blob/6390f8a94c8649c8b98da82c47b8e12cd7d56f3d/index.html) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [wheelie-bugsy](https://github.com/wheelie-bugsy). Independently curated. |
| Format | HTML/JS web app + Python helper scripts |
| Platform and availability | Local web app in the browser, served by `serve.py` (Python 3); Ollama 0.35+ for the default local model. |
| Jev's role | Optional cloud backend: scores each response against each rubric criterion through the `/v1/systemone` API (`jev-latest`), instead of the local nimble model. |
| Requirements | Python 3 and Ollama 0.35+ with `nimble` (about 9.5 GB) for local use; a TypeSafe API key only for the Jev cloud option. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |

## When to use

- Draft rubric levels for many written responses locally, with a human checking the results.
- Mismatch: final grades without review; the bundled report notes decision models trail LLM judges on multi-level scales.

## How it works

`index.html` lists TypeSafe Jev (cloud) as a connection preset (`https://api.typesafe.ai/v1`, model `jev-latest`) next to local Ollama nimble/tev1, and `serve.py` forwards requests only to an allowlist of hosts that includes `api.typesafe.ai`; `batch_eval.py` and `benchmark.py` run the same scoring from the command line. Integration evidence: [`index.html`](https://github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface/blob/6390f8a94c8649c8b98da82c47b8e12cd7d56f3d/index.html).

## Get started

Pull the local model, then start the helper server, which opens the app in your browser; choose TypeSafe Jev in Settings to use the cloud.

```sh
git clone https://github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface && cd RLCD-Rubric-Evaluation-interface
ollama pull nimble
python3 serve.py   # opens http://localhost:8787
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Research report: [github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface/blob/6390f8a94c8649c8b98da82c47b8e12cd7d56f3d/REPORT.md](https://github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface/blob/6390f8a94c8649c8b98da82c47b8e12cd7d56f3d/REPORT.md)
- README: [github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface/blob/6390f8a94c8649c8b98da82c47b8e12cd7d56f3d/README.md](https://github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface/blob/6390f8a94c8649c8b98da82c47b8e12cd7d56f3d/README.md)

## Limits and data handling

With the Jev option, each response and its rubric are sent to TypeSafe; the default local mode keeps data on the machine. Jev is an optional backend here, not the default. No license file: reuse terms are not granted.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 6390f8a94c86](https://github.com/wheelie-bugsy/RLCD-Rubric-Evaluation-interface/tree/6390f8a94c8649c8b98da82c47b8e12cd7d56f3d). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
