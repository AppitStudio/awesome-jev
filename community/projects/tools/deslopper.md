# deslopper (slop linter for Markdown whose optional --jev flag has Jev judge whether each flagged phrase should be kept or rewritten)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Markdown linter for machine-writing habits such as em-dash asides, filler verbs and `not just X but Y` padding. The core is plain patterns: 38 tells plus an opt-in aggressive preset, no model and no network, so it is safe in CI and pre-commit. `deslopper lint --jev` additionally sends each flagged line with its neighbours to Jev, which answers keep or rewrite with a probability; Jev only adds notes and never changes the lint result. It also has an eval for model rewrite passes and a skill for coding agents.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jv-k/deslopper) |
| Maintainer | [jv-k](https://github.com/jv-k). Independently curated. |
| Format | Python command-line tool (Python 3.10+, no dependencies) and agent skill |
| Requirements | Python 3.10+; for `--jev`, an `AI_GATEWAY_API_KEY` for the Vercel AI Gateway. |
| License | [MIT](https://github.com/jv-k/deslopper/blob/584f81725a6fc4ed9ba8fc95b4db32df07cf5e21/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/deslopper/jev.py`](https://github.com/jv-k/deslopper/blob/584f81725a6fc4ed9ba8fc95b4db32df07cf5e21/src/deslopper/jev.py) at the pinned commit. |

## When to use

- Lint documentation for AI-writing tells in CI, with a decision model triaging the ambiguous cases.
- Mismatch: the lint is deterministic without Jev, and `--jev` is an optional extra; it does not check spelling, grammar or house style.

## How it works

`src/deslopper/jev.py` sends typed keep-or-rewrite questions for each flagged line to the `typesafe-ai/jev` model through the Vercel AI Gateway (one request per file with smells, with a disk cache), and Jev's verdicts are shown as notes only. Integration evidence: [`src/deslopper/jev.py`](https://github.com/jv-k/deslopper/blob/584f81725a6fc4ed9ba8fc95b4db32df07cf5e21/src/deslopper/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
uvx --from git+https://github.com/jv-k/deslopper deslopper lint
export AI_GATEWAY_API_KEY=...
uvx --from git+https://github.com/jv-k/deslopper deslopper lint --jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the tells, presets and CI recipes: [github.com/jv-k/deslopper#readme](https://github.com/jv-k/deslopper#readme)
- Triage smells with Jev: [github.com/jv-k/deslopper/blob/584f81725a6fc4ed9ba8fc95b4db32df07cf5e21/docs/jev.md](https://github.com/jv-k/deslopper/blob/584f81725a6fc4ed9ba8fc95b4db32df07cf5e21/docs/jev.md)

## Limits and data handling

With `--jev`, flagged lines and their neighbours go to Vercel's AI Gateway (on your gateway key) and on to TypeSafe's Jev model; without the flag nothing leaves your machine. The README reports a cost of well under a cent per run, which was not measured here. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 584f81725a6f](https://github.com/jv-k/deslopper/tree/584f81725a6fc4ed9ba8fc95b4db32df07cf5e21). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
