# LibreHarness (durable Markdown work queue and risk-scaled workflow for OpenCode, with an advisory Jev reviewer)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Harness for OpenCode work that outlives one chat: a Markdown work queue with tasks, goals, dependencies, lanes and evidence plus a generated board; a workflow that scales process to risk (trivial changes skip the queue, others need a brief, a review and evidence); eight skills, agents, commands and four local plugins. Jev is its advisory reviewer: it scores a diff on seven quality axes and gives ship/scope/test verdicts, finds plan gaps and triages close states. It never merges, closes or blocks anything by itself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ezcodelab/libreharness) |
| Maintainer | [ezcodelab](https://github.com/ezcodelab). Independently curated. |
| Format | OpenCode harness (Python stdlib scripts, skills, agents and Node plugins; MIT) |
| Requirements | OpenCode, Python 3 and Linux file locking; for the Jev reviewer an OpenCode System One key (or another endpoint via `JEV_ENDPOINT`). |
| License | [MIT](https://github.com/ezcodelab/libreharness/blob/cc50f948dfd7708a64393c4e3aba626da6e6002b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`bin/jev_review.py`](https://github.com/ezcodelab/libreharness/blob/cc50f948dfd7708a64393c4e3aba626da6e6002b/bin/jev_review.py) at the pinned commit. |

## When to use

- Give an OpenCode agent durable tasks, evidence gates and a structured second opinion on diffs.
- Mismatch: non-Linux hosts; the queue relies on Linux file locking.

## How it works

`bin/jev_review.py` posts typed questions to OpenCode's System One endpoint (`https://opencode.ai/inference/systemone/v1/systemone`) by default, reads the model from `JEV_MODEL` rather than hard-coding one and reads the key from `~/.config/opencode/jev.key`; `bin/jev_plan.py` and `bin/jev_triage.py` reuse it. Integration evidence: [`bin/jev_review.py`](https://github.com/ezcodelab/libreharness/blob/cc50f948dfd7708a64393c4e3aba626da6e6002b/bin/jev_review.py).

## Get started

Clone the harness into your project setup, follow the quickstart, and add a Jev key if you want the reviewer.

```sh
git clone https://github.com/ezcodelab/libreharness && cd libreharness
# follow the README quickstart to install into OpenCode (no key needed)
export JEV_MODEL=<model your endpoint offers>
python3 bin/jev_review.py --help
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/ezcodelab/libreharness/blob/cc50f948dfd7708a64393c4e3aba626da6e6002b/README.md](https://github.com/ezcodelab/libreharness/blob/cc50f948dfd7708a64393c4e3aba626da6e6002b/README.md)
- Jev guide: [github.com/ezcodelab/libreharness/blob/cc50f948dfd7708a64393c4e3aba626da6e6002b/docs/jev.md](https://github.com/ezcodelab/libreharness/blob/cc50f948dfd7708a64393c4e3aba626da6e6002b/docs/jev.md)

## Limits and data handling

Jev is optional: a missing key skips the reviewer and the test suite needs none. With a key, the task, diff or plan goes to OpenCode's endpoint (or the one you set). The script scans for secrets before sending.

## Review and maintenance

Reviewed **2026-11-16** (Europe/Sofia) at [commit cc50f948dfd7](https://github.com/ezcodelab/libreharness/tree/cc50f948dfd7708a64393c4e3aba626da6e6002b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
