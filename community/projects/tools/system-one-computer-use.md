# System One Computer Use (screenshot loop agent driven by Jev)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Prototype computer-use agent in one Python file: it takes a screenshot, asks Jev what to do next (click, type, press Enter, scroll, open a site or stop) and does it with pyautogui; a small web dashboard runs tasks and shows reports.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brainstormity/System-One-Computer-Use) |
| Maintainer | [brainstormity](https://github.com/brainstormity). Independently curated. |
| Format | Python script and dashboard |
| Requirements | Python 3; macOS recommended (tested with Brave); a TypeSafe API key. |
| License | [MIT](https://github.com/brainstormity/System-One-Computer-Use/blob/9ceb7fc4806345fd42f2a631013cd3c5acead684/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_agent.py`](https://github.com/brainstormity/System-One-Computer-Use/blob/9ceb7fc4806345fd42f2a631013cd3c5acead684/jev_agent.py) at the pinned commit. |

## When to use

- Learn how far a decision model can drive a desktop from screenshots.
- Prototype simple browser chores.
- Mismatch: the author warns it is not for production and controls your real mouse and keyboard.

## How it works

`jev_agent.py` posts each screenshot with action questions to `https://api.typesafe.ai/v1/systemone` (`jev-1.14.0`) and acts only above a confidence threshold. Integration evidence: [`jev_agent.py`](https://github.com/brainstormity/System-One-Computer-Use/blob/9ceb7fc4806345fd42f2a631013cd3c5acead684/jev_agent.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -r requirements.txt
cp .env.example .env   # TYPESAFE_API_KEY
python dashboard.py
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/brainstormity/System-One-Computer-Use#readme](https://github.com/brainstormity/System-One-Computer-Use#readme)

## Limits and data handling

Screenshots of your screen are sent to TypeSafe. It can click, type and post on your accounts; watch it while it runs.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit 9ceb7fc48063](https://github.com/brainstormity/System-One-Computer-Use/tree/9ceb7fc4806345fd42f2a631013cd3c5acead684). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
