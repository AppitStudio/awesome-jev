# Trevskills Scrum (multi-agent feature-to-PR skill with Jev gates and ranking)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill that turns a feature request into a squash-merged PR via spec writer, builder, four reviewers and an approver, using Jev for model choice, promotion, dedupe, reviewer and criticality gates plus a `jev-rank` helper.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/trevorwhecht/scrum) |
| Maintainer | [trevorwhecht](https://github.com/trevorwhecht). Independently curated. |
| Format | Agent skill with Python helper scripts and a one-file dashboard (source only) |
| Requirements | A coding agent that runs skills, Python 3, and `TYPESAFE_API_KEY` (or a macOS Keychain item) for Jev. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/trevskills-scrum/jev-gate.py`](https://github.com/trevorwhecht/scrum/blob/5ef67196937903400b08afc9f486569c6e0d41ae/skills/trevskills-scrum/jev-gate.py) at the pinned commit. |

## When to use

- Add cheap, logged Jev decisions to a multi-agent build pipeline.
- Rank text lines by relevance from the shell.
- Mismatch: personal workflow, no license file (source-available only); Keychain fallback is macOS-specific.

## How it works

`jev.py` is a stdlib client for `/v1/systemone` (`jev-latest`); `jev-gate.py` makes one decision per pipeline step, never fails the caller (it prints the step's fallback) and logs each question and answer to `jev.log`; `jev-rank.py` ranks stdin lines by relevance. Integration evidence: [`skills/trevskills-scrum/jev-gate.py`](https://github.com/trevorwhecht/scrum/blob/5ef67196937903400b08afc9f486569c6e0d41ae/skills/trevskills-scrum/jev-gate.py).

## Get started

Install with `install.sh`, set `TYPESAFE_API_KEY`, then run `/trevskills-scrum <feature>` in your agent.

```sh
git clone https://github.com/trevorwhecht/scrum.git && cd scrum
./install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/trevorwhecht/scrum/blob/5ef67196937903400b08afc9f486569c6e0d41ae/README.md](https://github.com/trevorwhecht/scrum/blob/5ef67196937903400b08afc9f486569c6e0d41ae/README.md)

## Limits and data handling

Spec and diff summaries in each gate question go to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 5ef671969379](https://github.com/trevorwhecht/scrum/tree/5ef67196937903400b08afc9f486569c6e0d41ae). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
