# jevmory

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Local-first coding-agent memory CLI: ingest session transcripts into SQLite with redaction, optionally grade candidates with TypeSafe Jev, and audit `MEMORY.md` lines with receipt-backed STALE/WRONG/UNSUPPORTED/KEEP labels.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/romiluz13/jevmory) |
| Maintainer | [romiluz13](https://github.com/romiluz13). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Zero-dependency Python CLI (`jevmory`) with Claude Code / Codex hooks. |
| Requirements | Python 3; local project DB under `~/.jevmory`. Live grading needs per-project `init --enable-grading` plus `TYPESAFE_API_KEY`. `--offline` uses FakeJev. |
| License | [MIT](https://github.com/romiluz13/jevmory/blob/a84419303fd998cc4e25dbba952d70864b7edb37/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source and offline pytest inspected. Live TypeSafe grading was not run. Complements [invalidate](invalidate.md) (TTL against new evidence) rather than replacing it. |

## When to use

Use it when you want memory facts to stay verbatim quotes with Jev confidence receipts, and an `audit` report over an existing `MEMORY.md`. Prefer [invalidate](invalidate.md) when the main job is marking superseded facts against new evidence without building a quote store.

## How it works

Hooks ingest transcripts locally with secret redaction. Opt-in `dream` / live `audit` send redacted candidates through [`jevmory/judgment/client.py`](https://github.com/romiluz13/jevmory/blob/a84419303fd998cc4e25dbba952d70864b7edb37/jevmory/judgment/client.py) to `https://api.typesafe.ai/v1/systemone`. Code selects and composes quotes—Jev judges; it does not generate summary text.

## Get started

```sh
git clone https://github.com/romiluz13/jevmory.git
cd jevmory
git checkout a84419303fd998cc4e25dbba952d70864b7edb37
python3 -m pip install -e .
python3 -m pytest -q
# Offline audit path: jevmory audit MEMORY.md --offline
# Live grading (charges TypeSafe): jevmory init --enable-grading && export TYPESAFE_API_KEY=…
```

## Examples and demos

- README one-liner `jevmory audit MEMORY.md` and CLI surface (`dream`, `ingest`, `install`).
- Large offline pytest suite covering redaction, FakeJev, and CLI wiring.

## Limits and data handling

Live grading sends redacted candidate text and bounded context to TypeSafe. Hooks are designed to exit 0 so they do not break agent sessions. `jevmory.md` is sentinel-guarded against silent overwrite. High confidence is not proof a memory line is still true in production.

## Review and maintenance

Reviewed on **2026-09-21** at [commit a844193](https://github.com/romiluz13/jevmory/tree/a84419303fd998cc4e25dbba952d70864b7edb37): MIT. AI-assisted source review of README, `judgment/client.py`, and CLI privacy boundary. **`pytest`**: **531 passed** (7 subtests). No live TypeSafe calls.

Related: [invalidate](invalidate.md), [Hermes Jev Skills](hermes-jev-skills.md).
