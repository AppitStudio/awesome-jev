# focuslog (study-time tracker for Hyprland and Omarchy that can ask Jev whether a window supports your goal)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Local study and time-use tracker for Hyprland: it samples the focused window every few seconds, labels activity as study, waste or neutral with local rules and optionally Jev, and shows totals in a loopback dashboard and an Omarchy bar widget.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/piyush97/focuslog) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/piyush97/focuslog#readme) (source-built; no separate product site verified). |
| Pricing and access | Free source build; you supply your own TypeSafe/provider keys and any hosting costs. Checked 2026-11-01. |
| Jev evidence | [`focuslog.py`](https://github.com/piyush97/focuslog/blob/d05b0514d580d3c6d2335cf7894a4f588ff84f68/focuslog.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [piyush97](https://github.com/piyush97). Independently curated. |
| Format | Python script + systemd user service |
| Platform and availability | Linux, Hyprland / Omarchy. |
| Jev's role | Classifies unresolved windows as study, waste or neutral against your goal. |
| Requirements | Linux with Hyprland, Python 3.11+, systemd user session; optional TypeSafe key. |
| License | [MIT](https://github.com/piyush97/focuslog/blob/d05b0514d580d3c6d2335cf7894a4f588ff84f68/LICENSE) |

## When to use

- Track how much screen time actually goes to your study goal.
- Mismatch: classification is an estimate from window titles.

## How it works

`focuslog.py` applies ordered local title and app rules first, then for unresolved windows calls `https://api.typesafe.ai/v1/systemone` (configured in `config.toml`) with the goal and window title; verdicts are cached in SQLite. Integration evidence: [`focuslog.py`](https://github.com/piyush97/focuslog/blob/d05b0514d580d3c6d2335cf7894a4f588ff84f68/focuslog.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/piyush97/focuslog ~/focuslog
cd ~/focuslog
./install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Repository README: [github.com/piyush97/focuslog#readme](https://github.com/piyush97/focuslog#readme)

## Limits and data handling

Window titles are sent to TypeSafe only when Jev is configured; everything else stays in local SQLite. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-01** (Europe/Sofia) at [commit d05b0514d580](https://github.com/piyush97/focuslog/tree/d05b0514d580d3c6d2335cf7894a4f588ff84f68). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
