# Beam (Omarchy launcher with optional Jev intent search)

[All projects](../README.md) · [Desktop apps](README.md#desktop-apps)

One-box launcher plugin for Omarchy that launches apps, runs Omarchy menu actions, calculates and converts inline, and opens web searches and URLs; with an optional Jev key it also finds actions by meaning, so typing screen warmer finds Nightlight.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/RohitKaushal7/omarchy-beam) |
| Tags | `Open source` · `Free` |
| Product homepage | [Product homepage](https://plugins.omarchy.org/plugin.html?id=dev.reuk.beam) |
| Pricing and access | Open source (MIT); free to install from the Omarchy plugin directory or GitHub. Jev intent search uses your own TypeSafe key. Checked 2026-10-23. |
| Jev evidence | [`bin/beam/jev.py`](https://github.com/RohitKaushal7/omarchy-beam/blob/7a08674c4bbc7afc49a85b7eb2857c1b5a26383b/bin/beam/jev.py) at the pinned commit. Source inspected; not run on the review host. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Maintainer | [RohitKaushal7](https://github.com/RohitKaushal7). Independently curated. |
| Format | Omarchy plugin (Python and QML) |
| Platform and availability | Linux desktop running Omarchy 4, installed with `omarchy plugin add`. |
| Jev's role | Optional: when typed text does not match an action by name, Jev picks the Omarchy action you most likely mean. |
| Requirements | Omarchy 4 with Python 3 (both included); optional TypeSafe API key. |
| License | [MIT](https://github.com/RohitKaushal7/omarchy-beam/blob/7a08674c4bbc7afc49a85b7eb2857c1b5a26383b/LICENSE) |

## When to use

- Replace Omarchy's app menu with a single launcher.
- Find system actions without remembering their exact names.
- Mismatch: Omarchy only; Jev search is off without a key.

## How it works

`bin/beam/jev.py` sends your query and the list of available actions to `https://api.typesafe.ai/v1/systemone` with `jev-latest`, using `TYPESAFE_API_KEY`, and shows the chosen action marked with ✦. Integration evidence: [`bin/beam/jev.py`](https://github.com/RohitKaushal7/omarchy-beam/blob/7a08674c4bbc7afc49a85b7eb2857c1b5a26383b/bin/beam/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
omarchy plugin add https://github.com/RohitKaushal7/omarchy-beam.git --enable
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Screenshots and keyword list in the README: [github.com/RohitKaushal7/omarchy-beam#readme](https://github.com/RohitKaushal7/omarchy-beam#readme)

## Limits and data handling

With Jev enabled, typed queries and action names are sent to TypeSafe. A keybinding must be added by hand in Hyprland's bindings file.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 7a08674c4bbc](https://github.com/RohitKaushal7/omarchy-beam/tree/7a08674c4bbc7afc49a85b7eb2857c1b5a26383b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
