# antigravity-jev-skills (Antigravity workers with TypeSafe Jev evidence triage)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Skill pack where external workers implement/fix code, TypeSafe Jev triages evidence via a calibrated `jev` CLI (`POST /v1/systemone`), and independent High reviewers plus a read-only Codex final review check the result.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AJackTi/antigravity-jev-skills) |
| Maintainer | [AJackTi](https://github.com/AJackTi). Independently curated. |
| Format | Skill pack + Python Jev CLI (repo has no root SPDX license; bundled TypeSafe skills text is MIT) |
| Requirements | Antigravity/compatible agent host and a TypeSafe API key. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev-calibrated-decisions/scripts/jev.py`](https://github.com/AJackTi/antigravity-jev-skills/blob/fcfffb92b1ae1c8d172e881c84e32bff843ee6a2/jev-calibrated-decisions/scripts/jev.py) at the pinned commit. |

## When to use

- Add Jev evidence triage to an Antigravity worker loop.
- Use the calibrated jev CLI for batch/rank/gate calls.
- Mismatch: no root SPDX license on the reviewed commit.

## How it works

`jev-calibrated-decisions/scripts/jev.py` POSTs to `https://api.typesafe.ai/v1/systemone` (default `jev-latest`) using `TYPESAFE_API_KEY` or `~/.config/typesafe/api_key`. Integration evidence: [`jev-calibrated-decisions/scripts/jev.py`](https://github.com/AJackTi/antigravity-jev-skills/blob/fcfffb92b1ae1c8d172e881c84e32bff843ee6a2/jev-calibrated-decisions/scripts/jev.py).

## Get started

Follow the repo README to install skills and configure TYPESAFE_API_KEY.

```sh
git clone https://github.com/AJackTi/antigravity-jev-skills.git && cd antigravity-jev-skills
export TYPESAFE_API_KEY=...
# follow README
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/AJackTi/antigravity-jev-skills/blob/fcfffb92b1ae1c8d172e881c84e32bff843ee6a2/README.md](https://github.com/AJackTi/antigravity-jev-skills/blob/fcfffb92b1ae1c8d172e881c84e32bff843ee6a2/README.md)

## Limits and data handling

No root SPDX license on the reviewed commit. Evidence/text under triage is sent to TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit fcfffb92b1ae](https://github.com/AJackTi/antigravity-jev-skills/tree/fcfffb92b1ae1c8d172e881c84e32bff843ee6a2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
