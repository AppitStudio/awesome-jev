# glimpse

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Computer-use harness for the Linux GNOME desktop: a planner model writes the plan, and Jev finds each control, checks each result and decides when the task is done, across LibreOffice, Files, the browser and other apps.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Viverun/glimpse-jev) |
| Maintainer | [Viverun](https://github.com/Viverun). Independently curated. |
| Format | Linux desktop agent (Python) |
| Requirements | Linux with GNOME; an OpenAI-compatible vision planner model; `TYPESAFE_API_KEY`. |
| License | [PolyForm-Noncommercial-1.0.0 (source available, not OSI open source)](https://github.com/Viverun/glimpse-jev/blob/77f70463d1f77bdf88b86215ca3939da7107100a/LICENSE.md) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`live/config.py`](https://github.com/Viverun/glimpse-jev/blob/77f70463d1f77bdf88b86215ca3939da7107100a/live/config.py) at the pinned commit. |

## When to use

- Automate tasks in real desktop apps using the accessibility tree, mouse and keyboard.
- Want a harness that checks results and learns from each task.
- Mismatch: noncommercial license; Linux GNOME only.

## How it works

glimpse gives two fixed models tools, memory, checks and skills. The planner returns a JSON plan; Jev (TypeSafe System One), configured in `live/config.py`, locates controls, verifies each step and decides completion. A bench script runs OSWorld tasks. Integration evidence: [`live/config.py`](https://github.com/Viverun/glimpse-jev/blob/77f70463d1f77bdf88b86215ca3939da7107100a/live/config.py).

## Get started

From the upstream README: run the install script, which starts `glimpse setup`.

```sh
curl -fsSL https://raw.githubusercontent.com/Viverun/glimpse-jev/main/install.sh | bash
glimpse setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- bench/osworld_run.py
- README benchmark section

## Limits and data handling

Screenshots and accessibility data go to the planner and to TypeSafe. Noncommercial use only under PolyForm Noncommercial 1.0.0. Review the install script before piping it to bash.

## Review and maintenance

Reviewed **2026-10-19** (Europe/Sofia) at [commit 77f70463d1f7](https://github.com/Viverun/glimpse-jev/tree/77f70463d1f77bdf88b86215ca3939da7107100a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
