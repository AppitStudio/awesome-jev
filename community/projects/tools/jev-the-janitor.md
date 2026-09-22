# Jev the Janitor

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Markdown-vault janitor: TypeSafe Jev votes on each note (bucket, persist, secret, duplicate, …); code only adds frontmatter or quarantines suspected secrets—never deletes or rewrites note bodies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kylehovance-ai/jev-the-janitor) |
| Maintainer | [kylehovance-ai](https://github.com/kylehovance-ai). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Python package / CLI **`jev-the-janitor` 0.1.1** (`jev-janitor` console script). |
| Requirements | Python ≥ 3.11; `pyyaml`, `python-frontmatter`. Live Jev path: optional extra `.[jev]` (`typesafe-sdk`). Offline/keyword stand-in needs no key. |
| License | [MIT](https://github.com/kylehovance-ai/jev-the-janitor/blob/191c374f7fd0238b6940532145fc0a97979d9f50/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not endorsement. Offline pytest mostly green on the review host; live TypeSafe not run. Not affiliated with TypeSafe. |

## When to use

Use it when an Obsidian-style (or plain) markdown folder has outgrown hand-sorting and you want **typed votes + human review of the low-confidence pile**. Prefer [Jev Second Brain](jev-second-brain.md) for broader personal-knowledge agents rather than a dry-run vault filer.

## How it works

[`janitor/client.py`](https://github.com/kylehovance-ai/jev-the-janitor/blob/191c374f7fd0238b6940532145fc0a97979d9f50/janitor/client.py) maps System One answers onto a `Vote` (Choice bucket, Score persist, Noul secret/duplicate/decision/actionable/git-safe). Local redaction runs before any upload. Dry-run is default; `--apply` writes frontmatter or moves suspected secrets to quarantine. `--offline` uses a keyword stand-in so nothing leaves the machine.

## Get started

```sh
git clone https://github.com/kylehovance-ai/jev-the-janitor.git
cd jev-the-janitor
git checkout 191c374f7fd0238b6940532145fc0a97979d9f50
python3 -m pip install -e '.[dev]'
pytest -q
jev-janitor ./fixtures/notes --offline
# Live (charges; not run here): pip install -e '.[jev]' && export TYPESAFE_API_KEY=...
# jev-janitor ./fixtures/notes --plan
```

## Examples and demos

- Fixture vault under `fixtures/notes/`.
- Offline pytest on the review host: **83 passed, 1 failed** (`test_snapshot_detects_a_change` — mtime-only rewrite not observed on this filesystem; hashing/immutability tests still passed).

## Limits and data handling

Live mode sends redacted note excerpts and taxonomy questions to TypeSafe. Taxonomy must be tuned per vault; upstream reports one small live sample, not a calibrated production accuracy claim. Never deletes note bodies.

## Review and maintenance

Reviewed on **2026-09-22** at [commit 191c374](https://github.com/kylehovance-ai/jev-the-janitor/tree/191c374f7fd0238b6940532145fc0a97979d9f50): **0.1.1**, MIT. AI-assisted source review of README, `janitor/client.py`, LICENSE, tests. Offline pytest as above. No live TypeSafe spend.

Related: [Jev Second Brain](jev-second-brain.md), [Metis](metis.md), [jevtriage](jevtriage.md).
