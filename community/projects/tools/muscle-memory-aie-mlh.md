# Muscle Memory (hackathon code-cleanup factory where Jev settles most cuts and repeated calls become free rules)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

AIE x MLH hackathon project that cleans up AI-written pull requests (restating comments, swallowed exceptions, debug prints): Jev judges each candidate cut as the System 1 tier, Gemini handles the few it is unsure about, every cut is verified against visible and hidden tests, and calls that keep proving correct are written down as Semgrep rules that run instantly with no model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Shri2007/muscle-memory-aie-mlh) |
| Maintainer | [Shri2007](https://github.com/Shri2007). Independently curated. |
| Format | Python pipeline with web dashboard (uv; no license file) |
| Requirements | Python with uv, Node.js for the dashboard, a Postgres database with pgvector (the authors used Tiger Data), a TypeSafe key, and a Gemini key for the System 2 tier and embeddings. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`factory/jev.py`](https://github.com/Shri2007/muscle-memory-aie-mlh/blob/e2bbedf5e3fbcb61259658e59f590369c31a7a71/factory/jev.py) at the pinned commit. |

## When to use

- See a System 1 / System 2 / learned-rule cascade on real code cleanup.
- Mismatch: a maintained tool; it was written at a one-day hackathon.

## How it works

`factory/jev.py` calls `system_one` with `JEV_MODEL` (default `jev-latest`, `factory/config.py`) and the per-kind questions in `factory/questions.py`; code, not the model, decides the candidate kind. In the authors' Nov 13 run Jev settled 80 of 84 model decisions at about 127 ms and $0.00004 each, against about 2 s and $0.003 for Gemini; these are single-run hackathon numbers. Integration evidence: [`factory/jev.py`](https://github.com/Shri2007/muscle-memory-aie-mlh/blob/e2bbedf5e3fbcb61259658e59f590369c31a7a71/factory/jev.py).

## Get started

Sync dependencies, build the dashboard, fill in `.env` and run the smoke script (it also creates the tables), as the README describes.

```sh
git clone https://github.com/Shri2007/muscle-memory-aie-mlh && cd muscle-memory-aie-mlh
uv sync && (cd web && npm install && npm run build)
cp .env.example .env   # fill keys
uv run scripts/smoke.py --apply-schema
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Shri2007/muscle-memory-aie-mlh/blob/e2bbedf5e3fbcb61259658e59f590369c31a7a71/README.md](https://github.com/Shri2007/muscle-memory-aie-mlh/blob/e2bbedf5e3fbcb61259658e59f590369c31a7a71/README.md)
- Live dashboard (snapshot of a real run): [muscle-memory-mjivi.ondigitalocean.app](https://muscle-memory-mjivi.ondigitalocean.app)

## Limits and data handling

Code snippets from the pull requests you process go to TypeSafe and Google on your keys.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit e2bbedf5e3fb](https://github.com/Shri2007/muscle-memory-aie-mlh/tree/e2bbedf5e3fbcb61259658e59f590369c31a7a71). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
