# Jev Linux (voice desktop controller)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Voice controller for Ubuntu: local Moonshine speech recognition, a Gemini planner that splits your command into steps, and Jev choosing the desktop action for each step (open apps and sites, click, type, scroll, create notes).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/musagithub1/Browser_use) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/musagithub1/Browser_use#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-17. |
| Jev evidence | [`jev_linux/provider.py`](https://github.com/musagithub1/Browser_use/blob/8e4dcda461bc0220159bd52427d17efd73b920a9/jev_linux/provider.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/035_raja/status/2111168403872600082)). |
| Maintainer | [musagithub1](https://github.com/musagithub1). Independently curated. |
| Format | Python GTK desktop app (source checkout, `./run.sh`) |
| Platform and availability | Ubuntu Linux (source build) |
| Jev's role | Jev picks the desktop action for each planned step from a bounded set of operations. |
| Requirements | Ubuntu with GNOME, Python 3 and the listed apt packages, a microphone (optional), an OpenRouter API key (or a direct TypeSafe key for Jev). |
| License | [MIT](https://github.com/musagithub1/Browser_use/blob/8e4dcda461bc0220159bd52427d17efd73b920a9/LICENSE) |

## When to use

- Drive common desktop tasks on Ubuntu by voice or typed command, such as opening an app and writing a note.
- Study a planner-plus-decision-model split where Jev only picks among permitted operation types for each step.
- Mismatch: Ubuntu/GNOME only; planning and note writing use Gemini through OpenRouter, so it is not Jev-only.

## How it works

A Gemini 2.5 Flash plan lists ordered steps; for each step the app rereads the available desktop controls and asks Jev (`typesafe/jev-1.13` via OpenRouter, or `jev-1.13.0` direct at `https://api.typesafe.ai/v1/systemone`) to choose the action. Runs stop at 60 actions or 300 seconds by default, and Stop or Escape discards queued decisions. Integration evidence: [`jev_linux/provider.py`](https://github.com/musagithub1/Browser_use/blob/8e4dcda461bc0220159bd52427d17efd73b920a9/jev_linux/provider.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/musagithub1/Browser_use.git jev-linux && cd jev-linux
sudo apt install python3-gi gir1.2-gtk-3.0 gir1.2-atspi-2.0 alsa-utils python3-venv
./scripts/setup.sh
./run.sh --doctor && ./run.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Demo video in the author's X post.
- Commands to try: README section Commands to try.

## Limits and data handling

Speech is transcribed locally; command text, page text and desktop control descriptions go to OpenRouter or TypeSafe on your key. Keyboard and scrolling need you to approve Ubuntu's desktop-sharing prompt.

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 8e4dcda461bc](https://github.com/musagithub1/Browser_use/tree/8e4dcda461bc0220159bd52427d17efd73b920a9). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
