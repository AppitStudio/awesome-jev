# AI PM model-router (Claude Code plugin that pins a model tier per chat with optional TypeSafe Jev classification)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

One of the AI PM Skills Marketplace plugins: a local terminal router that picks a model tier for each new chat by rules, with an optional TypeSafe Jev classification of the first prompt.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Abhillashjadhav/AI-PM-essential-skills) |
| Maintainer | [Abhillashjadhav](https://github.com/Abhillashjadhav). Independently curated. |
| Format | Claude Code plugin marketplace + Python runtime (MIT) |
| Requirements | Claude Code, Python 3, and a TypeSafe key for the optional Jev mode (TypeSafe enforces credits; no local spend cap). |
| License | [MIT](https://github.com/Abhillashjadhav/AI-PM-essential-skills/blob/0ef74e223a321586c56040629fe52b1975715e4a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`model-router/model_router/jev.py`](https://github.com/Abhillashjadhav/AI-PM-essential-skills/blob/0ef74e223a321586c56040629fe52b1975715e4a/model-router/model_router/jev.py) at the pinned commit. |

## When to use

- Route new chats to a cheaper or stronger model tier.
- Test Jev classification next to local rules.
- Mismatch: no local spending cap; watch TypeSafe credits.

## How it works

`jev.py` (model `jev-1.13.0`) classifies eligible text-only first prompts; `router.py jev setup|pilot|status|disable` manage the opt-in mode and fall back to rules when unavailable. Integration evidence: [`model-router/model_router/jev.py`](https://github.com/Abhillashjadhav/AI-PM-essential-skills/blob/0ef74e223a321586c56040629fe52b1975715e4a/model-router/model_router/jev.py).

## Get started

Add the marketplace with `claude plugin marketplace add Abhillashjadhav/AI-PM-essential-skills`, then enable Jev with `python3 model-router/router.py jev setup`.

```sh
claude plugin marketplace add Abhillashjadhav/AI-PM-essential-skills
python3 model-router/router.py jev setup
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- model-router README: [github.com/Abhillashjadhav/AI-PM-essential-skills/blob/0ef74e223a321586c56040629fe52b1975715e4a/model-router/README.md](https://github.com/Abhillashjadhav/AI-PM-essential-skills/blob/0ef74e223a321586c56040629fe52b1975715e4a/model-router/README.md)

## Limits and data handling

First prompts are sent to TypeSafe when the Jev mode is on.

## Review and maintenance

Reviewed **2026-11-09** (Europe/Sofia) at [commit 0ef74e223a32](https://github.com/Abhillashjadhav/AI-PM-essential-skills/tree/0ef74e223a321586c56040629fe52b1975715e4a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
