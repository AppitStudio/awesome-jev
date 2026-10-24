# Jev Amazing (macOS WeChat sidebar for witty reply ideas, ranked by Jev)

[All projects](../README.md) · [macOS apps](README.md#macos-apps)

Native macOS side window for WeChat: one click reads the visible chat (text, images, stickers), a generative model drafts replies in five tones, and Jev ranks them; you edit and send yourself. A derivative of the Jev Chat assistant for macOS.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/yxjsxy/jevchat-amazing-response-macos) |
| Tags | `Open source` · `Free source build` |
| Product homepage | [Repository README](https://github.com/yxjsxy/jevchat-amazing-response-macos#readme) (source-built; no separate product site verified). |
| Pricing and access | Open source (MIT); free source build. Model calls use your own OpenRouter/TypeSafe keys. Checked 2026-10-24. |
| Jev evidence | [`src/judge_jev.py`](https://github.com/yxjsxy/jevchat-amazing-response-macos/blob/b8dd0033068a28f7efbab25367f6a4241815f30f/src/judge_jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [yxjsxy](https://github.com/yxjsxy). Independently curated. |
| Format | macOS app (Python payload, native launcher) |
| Platform and availability | macOS on Apple Silicon, built from source with setup.command. |
| Jev's role | Ranks candidate replies by comparison; generation and vision use other models. |
| Requirements | Apple Silicon Mac; uv and Xcode command-line tools; OpenRouter key (and TypeSafe key for ranking). |
| License | [MIT](https://github.com/yxjsxy/jevchat-amazing-response-macos/blob/b8dd0033068a28f7efbab25367f6a4241815f30f/LICENSE) |

## When to use

- Get reply ideas for WeChat without copying chats into another app.
- Choose a tone and strength for suggestions.
- Mismatch: not offline; cropped chat images leave your Mac.

## How it works

`src/judge_jev.py` posts candidates to `https://api.typesafe.ai` (`jev-latest`; gateways configurable) for ranking after DeepSeek generates them. Integration evidence: [`src/judge_jev.py`](https://github.com/yxjsxy/jevchat-amazing-response-macos/blob/b8dd0033068a28f7efbab25367f6a4241815f30f/src/judge_jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/yxjsxy/jevchat-amazing-response-macos.git
cd jevchat-amazing-response-macos
./setup.command
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/yxjsxy/jevchat-amazing-response-macos#readme](https://github.com/yxjsxy/jevchat-amazing-response-macos#readme)

## Limits and data handling

Cropped chat images and text go to cloud models. It does not inject into or send WeChat messages. Not affiliated with WeChat or Tencent.

## Review and maintenance

Reviewed **2026-10-24** (Europe/Sofia) at [commit b8dd0033068a](https://github.com/yxjsxy/jevchat-amazing-response-macos/tree/b8dd0033068a28f7efbab25367f6a4241815f30f). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
