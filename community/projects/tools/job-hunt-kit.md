# job-hunt-kit (Claude Code plugin for the whole job hunt, with Jev checking answers and outreach before you send)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that runs a job search from plain files you own: build master resumes from job-description research, tailor one per role with an ATS keyword report, draft application answers and outreach emails, and log every application. A `judge` skill runs a fixed set of yes/no content checks on emails and answers with Jev and suggests a fix for every NO.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/JNK234/job-hunt-kit) |
| Maintainer | [JNK234](https://github.com/JNK234). Independently curated. |
| Format | Claude Code plugin (skills, Python, LaTeX) |
| Requirements | Claude Code; a TypeSafe API key for the judge skill; LaTeX to compile resumes. |
| License | [MIT](https://github.com/JNK234/job-hunt-kit/blob/d2de9315a36d3e8ea047c214a3d1fe91199d3a5c/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/judge/judge.py`](https://github.com/JNK234/job-hunt-kit/blob/d2de9315a36d3e8ea047c214a3d1fe91199d3a5c/skills/judge/judge.py) at the pinned commit. |

## When to use

- Check application answers and outreach for specific problems before submitting.
- Mismatch: Jev is one skill; the rest runs on Claude.

## How it works

`skills/judge/judge.py` uses the official `typesafe_sdk` (`TypeSafeClient`, `Noul`) with a pinned `jev-1.14.0` to ask each content check as a yes/no question. Integration evidence: [`skills/judge/judge.py`](https://github.com/JNK234/job-hunt-kit/blob/d2de9315a36d3e8ea047c214a3d1fe91199d3a5c/skills/judge/judge.py).

## Get started

From the upstream README (not run on the review host):

```sh
/plugin marketplace add JNK234/job-hunt-kit
/plugin install job-hunt-kit@job-hunt-kit
/job-hunt-kit:setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/JNK234/job-hunt-kit#readme](https://github.com/JNK234/job-hunt-kit#readme)

## Limits and data handling

Drafted answers and emails go to TypeSafe when judged; the rest goes to Claude.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit d2de9315a36d](https://github.com/JNK234/job-hunt-kit/tree/d2de9315a36d3e8ea047c214a3d1fe91199d3a5c). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
