# Voyager (fast macOS computer use where Jev verifies every step)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Computer use for Mac apps: Claude Code plans a batch of steps at once, a small local daemon carries them out through macOS accessibility and ScreenCaptureKit, Jev checks each step against the screen, and safety rules in code pause before anything is sent.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jordanhilado/voyager) |
| Maintainer | [jordanhilado](https://github.com/jordanhilado). Independently curated. |
| Format | Python daemon for Claude Code |
| Requirements | macOS, Python 3.11+ and Claude Code; a TypeSafe API key (required); Anthropic key optional. |
| License | [MIT](https://github.com/jordanhilado/voyager/blob/30ec6b9ff8409533c38b1f5bc712ac5455a5ea37/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/voyager/config.py`](https://github.com/jordanhilado/voyager/blob/30ec6b9ff8409533c38b1f5bc712ac5455a5ea37/src/voyager/config.py) at the pinned commit. |

## When to use

- Let Claude Code operate Mac apps with step-by-step verification.
- Mismatch: macOS only (Windows not implemented).

## How it works

`src/voyager/config.py` sets `https://api.typesafe.ai/v1/systemone` with `jev-1.14.0`; after each action the daemon asks Jev whether the step succeeded, using Claude only if a Jev call fails. Integration evidence: [`src/voyager/config.py`](https://github.com/jordanhilado/voyager/blob/30ec6b9ff8409533c38b1f5bc712ac5455a5ea37/src/voyager/config.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jordanhilado/voyager && cd voyager
./install.sh   # then add TYPESAFE_API_KEY to the config file it prints
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jordanhilado/voyager#readme](https://github.com/jordanhilado/voyager#readme)

## Limits and data handling

Screen text from the controlled window goes to TypeSafe (and to Anthropic only on a failed Jev call); run logs stay local.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit 30ec6b9ff840](https://github.com/jordanhilado/voyager/tree/30ec6b9ff8409533c38b1f5bc712ac5455a5ea37). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
