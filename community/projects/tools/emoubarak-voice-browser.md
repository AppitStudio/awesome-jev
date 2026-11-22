# Voice Browser by El Mahdi Moubarak (talk to your own Chromium profile: Claude plans, Jev picks each click and keystroke)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

A side-panel extension and local native host for Linux: you speak or type a command, `claude -p` splits it into narrow goals, and the jev-ultrafast loop has Jev pick one action at a time from the page's element list while the extension clicks and types in your signed-in tabs. It uses ordinary extension APIs (no `chrome.debugger`), opens tabs in the background and asks before clicks that look irreversible.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/emoubarak/voice-browser) |
| Maintainer | [emoubarak](https://github.com/emoubarak). Independently curated. |
| Format | Chromium extension + Python native host |
| Requirements | Linux, a Chromium-based browser, Python 3.12+ with uv, the Claude Code CLI logged in, a `TYPESAFE_API_KEY`, an OpenAI-compatible text model key (OpenRouter by default) for typed text; Cloudflare Workers AI credentials only for voice. |
| License | [MIT](https://github.com/emoubarak/voice-browser/blob/15fcd4867b4d8582085bdae90fccaa89b415a7aa/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`host/voice_browser_host.py`](https://github.com/emoubarak/voice-browser/blob/15fcd4867b4d8582085bdae90fccaa89b415a7aa/host/voice_browser_host.py) at the pinned commit. |

## When to use

- Hands-free or typed browsing tasks in the browser you already use, with your own logins, and approval before risky clicks.
- Mismatch: macOS or Windows (Linux only for now) and pages that need vision; Jev picks from the element list and does not see images or canvas.

## How it works

`host/voice_browser_host.py` loads `jev_ultrafast.model` (Browser Use's jev-ultrafast) and runs its decision loop against the page snapshot the extension sends; every chosen element is re-checked (still connected, visible, enabled, not covered) before the extension acts, otherwise Jev looks again. Integration evidence: [`host/voice_browser_host.py`](https://github.com/emoubarak/voice-browser/blob/15fcd4867b4d8582085bdae90fccaa89b415a7aa/host/voice_browser_host.py).

## Get started

Clone and run the installer, which sets up the Python environment, registers the native host and creates the key file; or try it in a throwaway Chromium profile first.

```sh
git clone https://github.com/emoubarak/voice-browser && cd voice-browser
bin/install
# add TYPESAFE_API_KEY and OPENROUTER_API_KEY to ~/.config/voice-browser/env
CHROME=/path/to/chromium bin/try   # throwaway profile with a demo site
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (architecture, safety and measured timings): [github.com/emoubarak/voice-browser/blob/15fcd4867b4d8582085bdae90fccaa89b415a7aa/README.md](https://github.com/emoubarak/voice-browser/blob/15fcd4867b4d8582085bdae90fccaa89b415a7aa/README.md)

## Limits and data handling

Each Jev step sends the goal, page URL, title, up to 6,000 characters of visible text, the actionable elements with their current values (password, file and hidden inputs excluded) and the last 10 actions to TypeSafe; commands and page excerpts go to Anthropic, audio to Cloudflare. The irreversible-click check is a word list, not a guarantee.

## Review and maintenance

Reviewed **2026-11-22** (Europe/Sofia) at [commit 15fcd4867b4d](https://github.com/emoubarak/voice-browser/tree/15fcd4867b4d8582085bdae90fccaa89b415a7aa). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
