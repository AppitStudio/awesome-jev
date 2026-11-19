# Job Hunter Agent by Kiara Dorion (local job-search agent that ranks postings with 16 typed Jev judgments and drafts fact-checked resumes)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Personal job-search agent that runs on your computer twice a day: fetches new postings from public company boards (Greenhouse, Lever, Ashby, Workday, Oracle) and remote-job sites, ranks them by what you value (remote work, industry, pay, stability, fit) from 16 typed Jev judgments weighted by you, drafts a tailored resume and cover letter only from facts you wrote down, checks every sentence, and saves ATS-ready PDF and DOCX files. Sends the shortlist and its questions to you on Telegram. It never applies for you.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kikidorion/job-hunter-agent) |
| Maintainer | [kikidorion](https://github.com/kikidorion). Independently curated. |
| Format | Python CLI and scheduled agent |
| Requirements | Python 3 with the requirements installed, `TYPESAFE_API_KEY`, an LLM key for the writer, and a Telegram bot token for the digest. |
| License | [MIT](https://github.com/kikidorion/job-hunter-agent/blob/ed1c7a65364b9ce4ccdff0876f3079893eaf54eb/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jobhunt/judge.py`](https://github.com/kikidorion/job-hunter-agent/blob/ed1c7a65364b9ce4ccdff0876f3079893eaf54eb/jobhunt/judge.py) at the pinned commit. |

## When to use

- Rank a daily stream of postings by your own priorities and get draft applications you review yourself.
- Mismatch: an auto-apply bot; you submit every application.

## How it works

`jobhunt/judge.py` asks Jev Score, Choice and Noul questions about each posting through `typesafe_sdk`'s `TypeSafeClient`, using a profile summary of the candidate; your weights in `config.yaml` turn the answers into tiers. Integration evidence: [`jobhunt/judge.py`](https://github.com/kikidorion/job-hunter-agent/blob/ed1c7a65364b9ce4ccdff0876f3079893eaf54eb/jobhunt/judge.py).

## Get started

Clone, install, copy the example config, profile and env files, then check and run.

```sh
git clone https://github.com/kikidorion/job-hunter-agent && cd job-hunter-agent
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
cp config.example.yaml config.yaml && cp profile.example.yaml profile.yaml && cp .env.example .env
.venv/bin/python -m jobhunt check && .venv/bin/python -m jobhunt run
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/kikidorion/job-hunter-agent/blob/ed1c7a65364b9ce4ccdff0876f3079893eaf54eb/README.md](https://github.com/kikidorion/job-hunter-agent/blob/ed1c7a65364b9ce4ccdff0876f3079893eaf54eb/README.md)

## Limits and data handling

Postings and your profile facts go to TypeSafe and the writer model on your keys; the digest goes through Telegram. Respect each job board's terms.

## Review and maintenance

Reviewed **2026-11-19** (Europe/Sofia) at [commit ed1c7a65364b](https://github.com/kikidorion/job-hunter-agent/tree/ed1c7a65364b9ce4ccdff0876f3079893eaf54eb). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
