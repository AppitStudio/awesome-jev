# jev-chromium-use (browser automation in your signed-in Chromium where Jev picks each click or text entry, with Claude only for visual checks)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Prototype loop for Windows Chromium (Edge, Chrome): give a goal in plain language (Hebrew works), a bridge extension reads the page's controls in a background tab of your signed-in browser, Jev chooses which control to click or what to type at each step, and safety rules stop before risky actions. Screenshot checks go to Claude when needed. The maintainer reports about $0.0001 per step and publishes calibration notes.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/avi720/jev-chromium-use) |
| Maintainer | [avi720](https://github.com/avi720). Independently curated. |
| Format | Python loop plus a Chromium bridge extension and agent skill (MIT) |
| Requirements | Windows, Edge or Chrome, Python 3.12+ and a TypeSafe key; an Anthropic key only for visual checks. |
| License | [MIT](https://github.com/avi720/jev-chromium-use/blob/2cc1db443e7838cc52fa346371072bcaa78bb56b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_core.py`](https://github.com/avi720/jev-chromium-use/blob/2cc1db443e7838cc52fa346371072bcaa78bb56b/jev_core.py) at the pinned commit. |

## When to use

- Cheap step-by-step browser tasks in sites you are already signed in to.
- Mismatch: unattended use on accounts where a wrong click is costly; it is a prototype.

## How it works

`jev_core.py` uses `TypeSafeClient` from `typesafe_sdk` with model `jev-1.14.0` and Choice/Noul questions to pick the next action; `visual.py` sends screenshots to Claude when a visual check is requested. Integration evidence: [`jev_core.py`](https://github.com/avi720/jev-chromium-use/blob/2cc1db443e7838cc52fa346371072bcaa78bb56b/jev_core.py).

## Get started

Install, run setup to get the extension steps, then give a site and a goal.

```sh
git clone https://github.com/avi720/jev-chromium-use && cd jev-chromium-use
pip install -r requirements.txt
python jev_ext_loop.py --setup
python jev_ext_loop.py https://example.com "open the pricing page"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/avi720/jev-chromium-use/blob/2cc1db443e7838cc52fa346371072bcaa78bb56b/README.md](https://github.com/avi720/jev-chromium-use/blob/2cc1db443e7838cc52fa346371072bcaa78bb56b/README.md)

## Limits and data handling

Page controls and your goal go to TypeSafe on your key; screenshots go to Anthropic when visual checks run. It acts in your real signed-in browser, so review the safety rules before use.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 2cc1db443e78](https://github.com/avi720/jev-chromium-use/tree/2cc1db443e7838cc52fa346371072bcaa78bb56b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
