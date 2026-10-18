# Screen Intelligence (desk)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

macOS command-line "hands and eyes" for Claude Code: Claude writes a plan and Jev does the looking and clicking, using the accessibility tree first and a two-pass Box search on pixels second; 47 of 48 buttons found in about 0.6 s each, and it stops before send, submit, delete or pay.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/zacfink/screen-intelligence) |
| Maintainer | [zacfink](https://github.com/zacfink). Independently curated. |
| Format | Python command-line tool (`desk`) for Claude Code on macOS |
| Requirements | macOS with Screen Recording and Accessibility granted, Python 3.10, a separate Python 3.12 venv with `typesafe-sdk` 0.7.5+ and `TYPESAFE_API_KEY` (Jev 1.14 image and Box features). |
| License | [MIT](https://github.com/zacfink/screen-intelligence/blob/ed65f10e899e99d0d45a2020510eaa45216840a6/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/zacfinkelstein/status/2111645575594619328)). |
| Jev evidence | [`screen_intelligence/jev_look.py`](https://github.com/zacfink/screen-intelligence/blob/ed65f10e899e99d0d45a2020510eaa45216840a6/screen_intelligence/jev_look.py) at the pinned commit. |

## When to use

- Let Claude Code fill in forms and click through Mac apps without reading a full screenshot before every click.
- Ask yes/no questions about the screen (`desk see`) for about 10 tokens instead of a screenshot.
- Mismatch: set up for the author's machine, so paths need adjusting; macOS only.

## How it works

`desk do` runs a plan step by step: plain steps (type, press, choose, attach) run without a model call; other steps send a screenshot and the accessibility tree to Jev, which picks the move and the element or box. `desk find` boxes the target on the full screen and again on a close-up crop, and refuses to click below 0.6 confidence. Integration evidence: [`screen_intelligence/jev_look.py`](https://github.com/zacfink/screen-intelligence/blob/ed65f10e899e99d0d45a2020510eaa45216840a6/screen_intelligence/jev_look.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install -r requirements.txt
python -m unittest      # no mouse or network
desk see "Did the form submit?"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Author's X post with video: [x.com/zacfinkelstein/status/2111645575594619328](https://x.com/zacfinkelstein/status/2111645575594619328)
- Demo GIF in `docs/desk-demo.gif`.

## Limits and data handling

Screenshots and accessibility text of your screen go to TypeSafe on your key. It drives the real mouse and keyboard; risky steps are refused, and it stops if you move the mouse or switch apps.

## Review and maintenance

Reviewed **2026-10-18** (Europe/Sofia) at [commit ed65f10e899e](https://github.com/zacfink/screen-intelligence/tree/ed65f10e899e99d0d45a2020510eaa45216840a6). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
