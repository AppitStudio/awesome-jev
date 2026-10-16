# jev-harness (Adityakk9031)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Tests a coding-agent setup: replays disguised dangerous commands against your hooks and permission rules, checks whether a gate's confidence is calibrated, probes instruction loss after compaction and compares AI reviewers, with Jev as an optional judge or gate.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Adityakk9031/jev-harness) |
| Maintainer | [Adityakk9031](https://github.com/Adityakk9031). Independently curated. |
| Format | Python CLI (PyPI `jev-harness-sdk`, command `jev-harness`) |
| Requirements | Python 3.11+; a TypeSafe key only for `--judge jev` and `calibrate gate` with Jev (Anthropic/OpenAI judges optional). |
| License | [MIT](https://github.com/Adityakk9031/jev-harness/blob/26fe45092149b6eab5e9a90eb0ab98bb555aba2e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/Adityakuma8784/status/2110823573023793562)). |
| Jev evidence | [`src/jev_harness/core/judge.py`](https://github.com/Adityakk9031/jev-harness/blob/26fe45092149b6eab5e9a90eb0ab98bb555aba2e/src/jev_harness/core/judge.py) at the pinned commit. |

## When to use

- Check whether Claude Code, Codex or Cursor hooks actually block obfuscated destructive commands before you trust them.
- Measure whether a cheap Jev gate's 70% really means 70% and pick a threshold from data.
- Mismatch: `guard` and simulated compaction need no model; Jev is one optional judge. Distinct from the already-listed apixly jev-harness; the unrelated PyPI package `jev-harness` is not this project.

## How it works

`guard` and `calibrate` run deterministically over your own config; when `--judge jev` is selected, the judge client posts typed questions to the TypeSafe `systemone` endpoint, retries on 408/429/5xx/529 with capped backoff and raises an explicit unavailable error instead of guessing when the key or extra is missing. Integration evidence: [`src/jev_harness/core/judge.py`](https://github.com/Adityakk9031/jev-harness/blob/26fe45092149b6eab5e9a90eb0ab98bb555aba2e/src/jev_harness/core/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install 'jev-harness-sdk[stats]'
jev-harness guard run --project . --format summary
jev-harness guard run --project . --judge jev --format summary   # needs TYPESAFE_API_KEY
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Command docs: `docs/GUARD.md`, `docs/CALIBRATE.md`, `docs/COMPACTION.md`, `docs/REVIEWERS.md`.
- Launch video linked from the README (the compaction segment is labelled as simulated).

## Limits and data handling

Guard and calibration read your local agent configuration; with a model judge, the command text or reviewer findings go to the judge provider you select, billed to your key.

## Review and maintenance

Reviewed **2026-10-16** (Europe/Sofia) at [commit 26fe45092149](https://github.com/Adityakk9031/jev-harness/tree/26fe45092149b6eab5e9a90eb0ab98bb555aba2e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
