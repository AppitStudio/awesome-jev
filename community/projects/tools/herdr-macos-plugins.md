# Herdr macOS plugins

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Four macOS plugins for the Herdr agent terminal: open files from agent output, keep the Mac awake, show CPU, disk and folder size, and switch Jev on or off per Claude Code or Codex session through jev-gateway.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/klinter007/herdr-macos-plugins) |
| Maintainer | [klinter007](https://github.com/klinter007). Independently curated. |
| Format | Herdr plugins (Python 3.9+) |
| Requirements | macOS, Herdr 0.9.3+; for the Jev plugin, Node.js 22.15+, a Jev key and `jev-gateway`. |
| License | [MIT](https://github.com/klinter007/herdr-macos-plugins/blob/156029e23a5120622f4022e98049cee8b41ffedc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/GiliBenShahar/status/2112153790573097244)). |
| Jev evidence | [`herdr_tools/jev.py`](https://github.com/klinter007/herdr-macos-plugins/blob/156029e23a5120622f4022e98049cee8b41ffedc/herdr_tools/jev.py) at the pinned commit. |

## When to use

- Run Claude Code or Codex in Herdr and want Jev tool routing on for some sessions only.
- Want file opening, stay-awake and system stats in Herdr's tab bar.
- Mismatch: macOS only; the Jev plugin controls jev-gateway rather than calling Jev itself.

## How it works

The Jev plugin opens a **Claude + Jev** or **Codex + Jev** tab with its own [jev-gateway](jev-gateway.md) instance, which sends the agent's next-tool decisions to Jev, and toggles it per session. `herdr_tools/jev.py` talks to the local gateway's control endpoints on 127.0.0.1. Integration evidence: [`herdr_tools/jev.py`](https://github.com/klinter007/herdr-macos-plugins/blob/156029e23a5120622f4022e98049cee8b41ffedc/herdr_tools/jev.py).

## Get started

From the upstream README: install the plugins you want with `herdr plugin install`, add the key bindings to `~/.config/herdr/config.toml`, and install jev-gateway for the Jev plugin.

```sh
herdr plugin install klinter007/herdr-macos-plugins/plugins/jev
npm install -g jev-gateway
jev-claude --setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- VERIFICATION.md
- README screenshots of the Jev menu

## Limits and data handling

With Jev on, jev-gateway sends tool-choice context to TypeSafe. Plugin shortcuts and status bar need manual config entries.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 156029e23a51](https://github.com/klinter007/herdr-macos-plugins/tree/156029e23a5120622f4022e98049cee8b41ffedc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
