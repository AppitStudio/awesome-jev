# Nudge for Omarchy

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Omarchy (Hyprland) launcher plugin: describe what you need in plain words and Jev routes it to a reviewed safe desktop operation (night light, brightness, volume, folders, settings panels, reminders, shortcut lookup) or shows a preview and manual guidance for anything else.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cozidian/omarchy-jev) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/cozidian/omarchy-jev#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-10-17. |
| Jev evidence | [`transport.py`](https://github.com/cozidian/omarchy-jev/blob/221d46d66c3f676453555226d60005b137f36d55/transport.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [cozidian](https://github.com/cozidian). Independently curated. |
| Format | Omarchy plugin (Python worker, bar button and optional shortcut) |
| Platform and availability | Linux (Omarchy / Hyprland) |
| Jev's role | Jev routes a plain-language request to a command group, a command and bounded arguments. |
| Requirements | Omarchy on Arch Linux with Hyprland, Python 3, a TypeSafe API key. |
| License | [MIT](https://github.com/cozidian/omarchy-jev/blob/221d46d66c3f676453555226d60005b137f36d55/LICENSE) |

## When to use

- Change brightness, volume or night light by saying how you feel ("my eyes feel tired").
- Find the active keyboard shortcut for something without opening config files.
- Mismatch: only an explicit table of reviewed operations runs automatically; installs, power, network and file changes stay suggestion-only.

## How it works

Two requests to `https://api.typesafe.ai/v1/systemone`: first the command group and intent, then a command from that group plus independent argument choices. Code builds every argv with numeric bounds and `shell=False`; the model never supplies shell commands, paths or free-form arguments. Integration evidence: [`transport.py`](https://github.com/cozidian/omarchy-jev/blob/221d46d66c3f676453555226d60005b137f36d55/transport.py).

## Get started

From the upstream README (not run on the review host):

```sh
omarchy plugin add https://github.com/Cozidian/omarchy-jev --enable
python3 ~/.config/omarchy/plugins/io.github.cozidian.jev/setup.py
hyprctl reload
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Example requests in the README (English and Norwegian).
- Security notes: `SECURITY.md`.

## Limits and data handling

Submitted requests and relevant command metadata go to TypeSafe on your key; no history database or transcript logging. The key is stored in `~/.config/omarchy/jev/api-key` (mode 600).

## Review and maintenance

Reviewed **2026-10-17** (Europe/Sofia) at [commit 221d46d66c3f](https://github.com/cozidian/omarchy-jev/tree/221d46d66c3f676453555226d60005b137f36d55). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
