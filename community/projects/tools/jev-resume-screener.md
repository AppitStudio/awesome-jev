# Jev resume screener (Claude Code plugin)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that screens a folder of resumes against a job description with Jev: fit ranking, copied-resume clusters, flags for resumes mirroring the job description, and a human review queue. The output is a sorted reading list, never a rejection.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brent-phillips/jbp-plugins) |
| Maintainer | [brent-phillips](https://github.com/brent-phillips). Independently curated. |
| Format | Claude Code plugin (skills and Python scripts) |
| Requirements | Claude Code; Python 3.10+; a TypeSafe API key saved via /jev-setup. |
| License | [MIT](https://github.com/brent-phillips/jbp-plugins/blob/af6823e62ad521756e4ce715f7778f3c2456b958/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`plugins/jev-resume-screener/skills/jev-resume-screener/scripts/jev_client.py`](https://github.com/brent-phillips/jbp-plugins/blob/af6823e62ad521756e4ce715f7778f3c2456b958/plugins/jev-resume-screener/skills/jev-resume-screener/scripts/jev_client.py) at the pinned commit. |

## When to use

- Sort a large pile of resumes into a reading order for a recruiter.
- Spot near-duplicate or job-description-mirroring resumes.
- Mismatch: an aid for human review; hiring decisions stay with people.

## How it works

`jev_client.py` is a minimal client for `POST /v1/systemone` that reads the key from `TYPESAFE_API_KEY` or `~/.typesafe/api_key`; the skill turns the drafted rubric into Jev questions per resume and logs your feedback for later runs. Integration evidence: [`plugins/jev-resume-screener/skills/jev-resume-screener/scripts/jev_client.py`](https://github.com/brent-phillips/jbp-plugins/blob/af6823e62ad521756e4ce715f7778f3c2456b958/plugins/jev-resume-screener/skills/jev-resume-screener/scripts/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add brent-phillips/jbp-plugins
/plugin install jev-resume-screener@jbp-plugins
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Commands and workflow: [github.com/brent-phillips/jbp-plugins/blob/main/plugins/jev-resume-screener/README.md](https://github.com/brent-phillips/jbp-plugins/blob/main/plugins/jev-resume-screener/README.md)

## Limits and data handling

Resume text is sent to TypeSafe; check your local rules on automated screening of candidates.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit af6823e62ad5](https://github.com/brent-phillips/jbp-plugins/tree/af6823e62ad521756e4ce715f7778f3c2456b958). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
