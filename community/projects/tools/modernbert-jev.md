# modernbert-jev (Jev-class typed decisions on one CPU with a ModernBERT NLI model, TypeSafe-compatible)

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Tiny decision-model stack that answers choice, score and yes/no questions about text or JSON on one CPU with 2 GB of RAM: a ModernBERT-base NLI cross-encoder where entailment probability is the option's probability, plus distillation, a library, CLI and an HTTP server that speaks TypeSafe's `POST /v1/systemone`, so existing clients switch by base URL. A working preview; numbers are the author's local measurements.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/KSonny4/modernbert-jev) |
| Maintainer | [KSonny4](https://github.com/KSonny4). Independently curated. |
| Format | Python package, CLI and HTTP server |
| Requirements | Python with uv; a CPU is enough. No TypeSafe key. |
| License | No license file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/petrkubelkaa/status/2115448829411496325)). |
| Jev evidence | [`src/modernbert_jev/server.py`](https://github.com/KSonny4/modernbert-jev/blob/20b564205b1498fc615f2e884d9b18cd2ba914ec/src/modernbert_jev/server.py) at the pinned commit. |

## When to use

- Run private, near-free typed decisions on modest hardware.
- Mismatch: preview; not TypeSafe's model; official JevBench placement pending.

## How it works

`src/modernbert_jev/server.py` serves `POST /v1/systemone` and `GET /v1/models`, validated by `api.py` against the TypeSafe request and response shapes. Integration evidence: [`src/modernbert_jev/server.py`](https://github.com/KSonny4/modernbert-jev/blob/20b564205b1498fc615f2e884d9b18cd2ba914ec/src/modernbert_jev/server.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/KSonny4/modernbert-jev && cd modernbert-jev
uv venv && uv pip install -e .
modernbert-jev pull modernbert-jev
modernbert-jev serve --model models/modernbert-jev --port 11436
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/KSonny4/modernbert-jev#readme](https://github.com/KSonny4/modernbert-jev#readme)
- JevMan leaderboard entry (author's PR): [github.com/opper-ai/jevman-benchmark/pull/22](https://github.com/opper-ai/jevman-benchmark/pull/22)

## Limits and data handling

Runs locally; nothing is sent to TypeSafe.

## Review and maintenance

Reviewed **2026-10-28** (Europe/Sofia) at [commit 20b564205b14](https://github.com/KSonny4/modernbert-jev/tree/20b564205b1498fc615f2e884d9b18cd2ba914ec). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
