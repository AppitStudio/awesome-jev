# Jev Humanize Writing by win4r (agent writing skill where Jev checks that a lighter edit keeps facts, attribution, caveats and voice)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill plus a standard-library Python CLI for light editing of Chinese and English prose: technical articles, product descriptions, notes and work emails. The host agent (Codex, Claude Code and similar) writes candidate revisions; code protects numbers, quotes, links and code; Jev diagnoses the source and compares candidates with Noul, Score and Choice questions (did a caveat get lost, which draft is clearer); the host then reviews sentence by sentence and delivers one text with a separate report. A local mode runs with no key and no network. It does not generate text, detect AI authorship or promise to pass AI detectors.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/win4r/jev-humanize-writing) |
| Maintainer | [win4r](https://github.com/win4r). Independently curated. |
| Format | Agent skill + Python CLI (stdlib only, MIT) |
| Requirements | Python 3.10+, a host agent that can run Python; `TYPESAFE_API_KEY` for Jev mode (local mode needs none). macOS/Linux. |
| License | [MIT](https://github.com/win4r/jev-humanize-writing/blob/60808926c9c42732577dac87908386684786032f/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev_client.py`](https://github.com/win4r/jev-humanize-writing/blob/60808926c9c42732577dac87908386684786032f/scripts/jev_client.py) at the pinned commit. |

## When to use

- Tighten agent-edited prose while checking that facts, caveats and attribution survived.
- Mismatch: ghost-writing or evading AI detectors; the README rules both out.

## How it works

`scripts/jev_client.py` posts typed questions to `https://api.typesafe.ai/v1/systemone`; `scripts/editor.py` uses it for `--mode jev` diagnose and compare runs, warning that the manuscript is sent unanonymized. Integration evidence: [`scripts/jev_client.py`](https://github.com/win4r/jev-humanize-writing/blob/60808926c9c42732577dac87908386684786032f/scripts/jev_client.py).

## Get started

Clone, install the skill into your agent, or run the CLI directly.

```sh
git clone https://github.com/win4r/jev-humanize-writing && cd jev-humanize-writing
python3 -I -B scripts/editor.py diagnose /abs/source.md --mode local --json-out /tmp/diagnosis.json
python3 -I -B scripts/editor.py compare /abs/source.md --candidate light=/abs/source.humanized.md --mode jev --prompt-key --json-out /tmp/review.json
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (English): [github.com/win4r/jev-humanize-writing/blob/60808926c9c42732577dac87908386684786032f/README.en.md](https://github.com/win4r/jev-humanize-writing/blob/60808926c9c42732577dac87908386684786032f/README.en.md)
- Validation notes: [github.com/win4r/jev-humanize-writing/blob/60808926c9c42732577dac87908386684786032f/docs/validation.md](https://github.com/win4r/jev-humanize-writing/blob/60808926c9c42732577dac87908386684786032f/docs/validation.md)

## Limits and data handling

Jev mode sends the actual source, revisions and brief to TypeSafe on your key; use local mode for private material. Results come from the maker's own validation rounds.

## Review and maintenance

Reviewed **2026-11-17** (Europe/Sofia) at [commit 60808926c9c4](https://github.com/win4r/jev-humanize-writing/tree/60808926c9c42732577dac87908386684786032f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
