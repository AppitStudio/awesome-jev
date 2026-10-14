# decision-shadow

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Zero-dependency Python wrapper to shadow-test Jev against an existing LLM classifier, report agreement, tune thresholds, then switch over with fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jatingargiitk/decision-shadow) |
| Maintainer | [jatingargiitk](https://github.com/jatingargiitk). Independently curated. |
| Format | Python library |
| Requirements | Python 3.9+, OpenRouter API key (Jev via OpenRouter). |
| License | [MIT](https://github.com/jatingargiitk/decision-shadow/blob/75b05edace00e0e643b8b2a14f014de340507bb2/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`decision_shadow/backends.py`](https://github.com/jatingargiitk/decision-shadow/blob/75b05edace00e0e643b8b2a14f014de340507bb2/decision_shadow/backends.py) at the pinned commit. |

## When to use

- Migrate a chat-model classifier to Jev without trusting it blind.
- Pick a certainty threshold from logged disagreements and labels.

## How it works

Modes: shadow (your function decides, Jev runs alongside and both are logged), report, tune, and on (Jev decides; low certainty or errors fall back to your function). Integration evidence: [`decision_shadow/backends.py`](https://github.com/jatingargiitk/decision-shadow/blob/75b05edace00e0e643b8b2a14f014de340507bb2/decision_shadow/backends.py).

## Get started

From the upstream README (not run on the review host):

```sh
pip install git+https://github.com/jatingargiitk/decision-shadow
export OPENROUTER_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Usage example `from decision_shadow import Shadow, choice` in README.
- Examples folder: `examples/`.

## Limits and data handling

Inputs go to OpenRouter in shadow/on modes.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 75b05edace00](https://github.com/jatingargiitk/decision-shadow/tree/75b05edace00e0e643b8b2a14f014de340507bb2). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
