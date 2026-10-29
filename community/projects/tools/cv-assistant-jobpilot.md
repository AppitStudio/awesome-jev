# CV Assistant + Jobpilot (job-search skills and a local dashboard that scores jobs against your evidence with Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Job-search kit: seven skills for Claude Code, Claude.ai, ChatGPT and Codex that turn your real experience into an evidence-graded skills pool and a tailored ATS-friendly CV per ad, plus Jobpilot, a local Windows dashboard that collects jobs from public boards (Greenhouse, Lever, Ashby, peviitor.ro), scores them with Jev and can fill and apply to the best ones. Auto-submit is off by default. Romanian docs with an English summary.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/AlexNegulescu111/cv-assistant) |
| Maintainer | [AlexNegulescu111](https://github.com/AlexNegulescu111). Independently curated. |
| Format | Agent skills and Python package with local dashboard |
| Requirements | Python, Playwright Chromium, a TypeSafe API key for scoring; Windows for the dashboard. |
| License | [MIT](https://github.com/AlexNegulescu111/cv-assistant/blob/1929832a9b80082c5f2c90f3c5101b4732211a05/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jobpilot/score.py`](https://github.com/AlexNegulescu111/cv-assistant/blob/1929832a9b80082c5f2c90f3c5101b4732211a05/jobpilot/score.py) at the pinned commit. |

## When to use

- Rank many job ads against what you can actually prove before you tailor CVs.
- Mismatch: Windows-first dashboard; Romanian UI.

## How it works

`jobpilot/score.py` posts each job description and your skills pool to `https://api.typesafe.ai/v1/systemone`, applying knockout checks on must-have requirements and a 0-100 fit score. Integration evidence: [`jobpilot/score.py`](https://github.com/AlexNegulescu111/cv-assistant/blob/1929832a9b80082c5f2c90f3c5101b4732211a05/jobpilot/score.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/AlexNegulescu111/cv-assistant.git
pip install -e "./cv-assistant[dashboard,browser,cv]"
python -m playwright install chromium
jobpilot init --workspace ./applications --open
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/AlexNegulescu111/cv-assistant#readme](https://github.com/AlexNegulescu111/cv-assistant#readme)

## Limits and data handling

Job texts and your skills pool go to TypeSafe for scoring; CV work goes to the chat assistant you use. Review applications before enabling auto-submit.

## Review and maintenance

Reviewed **2026-10-29** (Europe/Sofia) at [commit 1929832a9b80](https://github.com/AlexNegulescu111/cv-assistant/tree/1929832a9b80082c5f2c90f3c5101b4732211a05). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
