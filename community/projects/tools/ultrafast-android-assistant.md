# Ultrafast Android Assistant by Jiang Sheng (Android UI navigation where Jev picks the next action from a numbered list of on-screen controls)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Reads the current screen with UIAutomator, turns visible actionable controls into a numbered action space, and asks Jev in two typed steps: a choice for the action plus a noul for task completion, then a second choice for the target only when needed. Re-observes the screen before acting and refuses input if it changed. Executes guarded taps, scrolls and back through ADB. Chinese docs.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/doskoi/ultrafast-android-assistant) |
| Maintainer | [Jiang Sheng](https://github.com/doskoi). Independently curated. |
| Format | Python CLI and library (uv) |
| Requirements | Python 3.12, uv, ADB with a connected Android device, and a TypeSafe API key. |
| License | [MIT](https://github.com/doskoi/ultrafast-android-assistant/blob/52811aed6de7f39222ae4fcfe25a0bd6705acf81/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_android_assistant/policy.py`](https://github.com/doskoi/ultrafast-android-assistant/blob/52811aed6de7f39222ae4fcfe25a0bd6705acf81/src/jev_android_assistant/policy.py) at the pinned commit. |

## When to use

- Automate Android UI navigation with a small, code-checked action space.
- Mismatch: screens with sensitive content; the author says such UI trees must not go to remote Jev.

## How it works

`src/jev_android_assistant/policy.py` (`JevPolicy`) sends the action space through `typesafe-sdk`; Jev is the only model provider, and legacy local-model settings raise an error rather than silently going remote. Integration evidence: [`src/jev_android_assistant/policy.py`](https://github.com/doskoi/ultrafast-android-assistant/blob/52811aed6de7f39222ae4fcfe25a0bd6705acf81/src/jev_android_assistant/policy.py).

## Get started

Sync, load your key, inspect a screen (no model call), then run suggest or run.

```sh
git clone https://github.com/doskoi/ultrafast-android-assistant.git && cd ultrafast-android-assistant
uv sync
source ~/.config/ultrafast/jev.env   # TYPESAFE_API_KEY
uv run --no-sync ultrafast-android-assistant --serial <device> --package <allowed.app> suggest "<task>"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README (Chinese): [github.com/doskoi/ultrafast-android-assistant/blob/52811aed6de7f39222ae4fcfe25a0bd6705acf81/README.md](https://github.com/doskoi/ultrafast-android-assistant/blob/52811aed6de7f39222ae4fcfe25a0bd6705acf81/README.md)

## Limits and data handling

The semantic content of the current UI is sent to TypeSafe on `suggest` and `run`. Every run must name the one Android package it may operate, and it stops if another app is in front.

## Review and maintenance

Reviewed **2026-11-25** (Europe/Sofia) at [commit 52811aed6de7](https://github.com/doskoi/ultrafast-android-assistant/tree/52811aed6de7f39222ae4fcfe25a0bd6705acf81). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
