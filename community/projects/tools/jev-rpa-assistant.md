# Jev RPA Assistant (Windows customer-service prototype that picks approved replies with Jev; Chinese)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Windows desktop prototype (Chinese README) for e-commerce customer service: Clicknium RPA reads the chat page, a vision model transcribes it, and Jev chooses step by step through an approved reply library or hands the chat to a person, with page-state checks before and after sending and a SQLite audit trail. Adapted for Xianyu web in Edge; 1688 is a later target.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ChanghaoLiao/jev-rpa-assistant) |
| Maintainer | [ChanghaoLiao](https://github.com/ChanghaoLiao). Independently curated. |
| Format | Python desktop app (Clicknium RPA, Qt UI) |
| Requirements | Windows, Edge, Python; a vision model key and a TypeSafe or OpenRouter key for live runs. |
| License | [MIT](https://github.com/ChanghaoLiao/jev-rpa-assistant/blob/59dd9d912d1381d6d16ad2f730783fbc3ae8ef89/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jevtool/router.py`](https://github.com/ChanghaoLiao/jev-rpa-assistant/blob/59dd9d912d1381d6d16ad2f730783fbc3ae8ef89/jevtool/router.py) at the pinned commit. |

## When to use

- See Jev used as a layered choice over fixed replies instead of free-text generation.
- Mismatch: prototype; no screenshots or real merchant data published, and only Xianyu web is adapted.

## How it works

`jevtool/router.py` sends the transcribed conversation to System One (`jev-latest`) as layered choice questions over the reply library, with a HUMAN option and confidence thresholds set in `jevtool/config.py`; reply text always comes from the reviewed library. Integration evidence: [`jevtool/router.py`](https://github.com/ChanghaoLiao/jev-rpa-assistant/blob/59dd9d912d1381d6d16ad2f730783fbc3ae8ef89/jevtool/router.py).

## Get started

From the upstream README (not run on the review host):

```sh
py -3.13 -m venv .venv
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
.\.venv\Scripts\python.exe app.py --demo   # mock answers, no API calls
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Setup guide (Chinese): [github.com/ChanghaoLiao/jev-rpa-assistant/blob/main/docs/SETUP.md](https://github.com/ChanghaoLiao/jev-rpa-assistant/blob/main/docs/SETUP.md)

## Limits and data handling

Chat content is sent to the vision provider and TypeSafe/OpenRouter on live runs. Automating marketplace chats may be subject to the platform's rules. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-02** (Europe/Sofia) at [commit 59dd9d912d13](https://github.com/ChanghaoLiao/jev-rpa-assistant/tree/59dd9d912d1381d6d16ad2f730783fbc3ae8ef89). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
