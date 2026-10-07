# omarchy-mouse-sacrifice

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

Omarchy (Hyprland) plugin: move the pointer into the bottom-right corner and a card offers up to five keyboard shortcuts that fit what is on screen, ranked by TypeSafe Jev from a list built in code (focused app, workspace windows, bar widgets, recent use, your real Hyprland binds and press counts); no screenshots or typed text are sent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ignotas/omarchy-mouse-sacrifice) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [Repository README](https://github.com/ignotas/omarchy-mouse-sacrifice#readme) (source-built app; no separate website verified). |
| Pricing and access | No app fee for the MIT plugin; requires your own TypeSafe key (stored with `secret-tool`); Jev input tokens billed by TypeSafe, tallied locally. Checked 2026-10-07. |
| Jev evidence | [`corner/jev.py`](https://github.com/ignotas/omarchy-mouse-sacrifice/blob/a5b7ee7db2533c4e07c70ac5558e759bcc753180/corner/jev.py) sends two Choice questions to rank the shortcut list; source inspected at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation. Not commercial. Listing is not an endorsement. Live app not run on the review host. |
| Maintainer | [ignotas](https://github.com/ignotas). Independently curated. |
| Format | Omarchy shell plugin (`Service.qml` + Python daemon in `corner/`) |
| Platform and availability | Linux with Omarchy (Hyprland); installed with `omarchy plugin add`. |
| Jev's role | Jev only ranks a list of real shortcuts assembled in code; it re-runs when the set of five changes. Code tracks presses, fades ignored suggestions and runs the chosen shortcut. |
| Requirements | Omarchy with `secret-tool`, a TypeSafe API key. |
| License | [MIT](https://github.com/ignotas/omarchy-mouse-sacrifice/blob/a5b7ee7db2533c4e07c70ac5558e759bcc753180/LICENSE). |

## When to use

- Discover and use Hyprland shortcuts that fit the current window without memorising them.
- Mismatch: Omarchy-only; locked hardware-key binds are excluded by design.

## How it works

[`corner/daemon.py`](https://github.com/ignotas/omarchy-mouse-sacrifice/blob/a5b7ee7db2533c4e07c70ac5558e759bcc753180/corner/daemon.py) watches the corner and builds the list ([`corner/model.py`](https://github.com/ignotas/omarchy-mouse-sacrifice/blob/a5b7ee7db2533c4e07c70ac5558e759bcc753180/corner/model.py), [`corner/keyboard.py`](https://github.com/ignotas/omarchy-mouse-sacrifice/blob/a5b7ee7db2533c4e07c70ac5558e759bcc753180/corner/keyboard.py)); [`corner/jev.py`](https://github.com/ignotas/omarchy-mouse-sacrifice/blob/a5b7ee7db2533c4e07c70ac5558e759bcc753180/corner/jev.py) asks Jev to rank it. Working notes, press logs and the spend tally live under `~/.local/state/omarchy/mouse-sacrifice/`.

## Get started

Install with Omarchy's plugin command:

```sh
omarchy plugin add https://github.com/ignotas/omarchy-mouse-sacrifice.git --enable
# remove: omarchy plugin remove ignotas.mouse-sacrifice
```

Jev charges input tokens only ($0.042 per million per upstream); cached opens make no call.

## Examples and demos

- README *What it sends*, *Cost* (debug view shows the last request) and *Learning*.

## Limits and data handling

Window app names/titles, bar widgets, recent use and shortcut lists go to TypeSafe; no screenshot or typed text (upstream). Not run on the review host.

## Review and maintenance

Reviewed **2026-10-07** (Europe/Sofia) at [commit a5b7ee7db253](https://github.com/ignotas/omarchy-mouse-sacrifice/tree/a5b7ee7db2533c4e07c70ac5558e759bcc753180). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
