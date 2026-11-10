# wechat-triage-hud (WeChat PC overlay where Jev decides who in a chat needs you)

[All projects](../README.md) · [Windows apps](README.md#windows-apps)

Windows overlay for PC WeChat that reads the open chat with local offline OCR, groups messages by speaker and asks Jev who actually needs you (alert, todo or silent), with separate ad, scam, flame and policy risk scores. It never sends or drafts replies.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ops120/wechat-triage-hud) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ops120/wechat-triage-hud#readme) (source-built; no separate product site verified). |
| Pricing and access | Free Apache-2.0 source; you supply your own TypeSafe key and pay its usage. Checked 2026-11-10. |
| Jev evidence | [`wechat_triage_hud/jev_engine.py`](https://github.com/ops120/wechat-triage-hud/blob/f3d4c8b726746bae52ce912176dd8bec04710f31/wechat_triage_hud/jev_engine.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [ops120](https://github.com/ops120). Independently curated. |
| Format | Windows desktop overlay (Python 3.10+, Apache-2.0) |
| Platform and availability | Windows 10/11 with PC WeChat (source build or self-packaged exe) |
| Jev's role | Jev judges, per speaker, whether a chat turn needs you and scores ad, scam, flame and policy risks. |
| Requirements | Windows 10/11, PC WeChat, Python 3.10+ (or a self-built exe via `build.bat`), and `TYPESAFE_API_KEY`. |
| License | [Apache-2.0](https://github.com/ops120/wechat-triage-hud/blob/f3d4c8b726746bae52ce912176dd8bec04710f31/LICENSE) |

## When to use

- Stay out of busy WeChat groups until someone actually needs you.
- See per-speaker Jev triage with risk scores kept separate rather than merged.
- Mismatch: Windows and PC WeChat only; docs mostly in Chinese; no prebuilt release on GitHub at review.

## How it works

`jev_engine.py` posts OCR'd, per-speaker state plus your locally entered relationship context to `api.typesafe.ai/v1/systemone`; a coarse pass screens everyone and a second pass judges the top K, while the alert gates stay in code rules, not the model. Integration evidence: [`wechat_triage_hud/jev_engine.py`](https://github.com/ops120/wechat-triage-hud/blob/f3d4c8b726746bae52ce912176dd8bec04710f31/wechat_triage_hud/jev_engine.py).

## Get started

Install the requirements, set your TypeSafe key, then run the HUD next to an open WeChat chat (or package an exe with `build.bat`).

```sh
git clone https://github.com/ops120/wechat-triage-hud.git && cd wechat-triage-hud
pip install -e .
wechat-triage-hud
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshots and data-flow notes: [github.com/ops120/wechat-triage-hud/blob/f3d4c8b726746bae52ce912176dd8bec04710f31/SECURITY.md](https://github.com/ops120/wechat-triage-hud/blob/f3d4c8b726746bae52ce912176dd8bec04710f31/SECURITY.md)

## Limits and data handling

OCR runs locally, but the chat text being judged goes to TypeSafe on your key; see SECURITY.md for the data flow.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit f3d4c8b72674](https://github.com/ops120/wechat-triage-hud/tree/f3d4c8b726746bae52ce912176dd8bec04710f31). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
