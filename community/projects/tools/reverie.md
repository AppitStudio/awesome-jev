# Reverie

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Spec-driven browser test agent: Markdown specs are run step by step by a multimodal pilot while hosted TypeSafe Jev (default, via OpenRouter) or local Laya makes each click and keystroke, with a text model escalating when the decision engine is unsure, commit-button guards and run evidence under `.reverie/runs/`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/r3c0nc1l3r/reverie) |
| Maintainer | [r3c0nc1l3r](https://github.com/r3c0nc1l3r). Independently curated. |
| Format | Python CLI (`uv sync`) |
| Requirements | Python with uv; `OPENROUTER_API_KEY` (covers Jev, pilot and text model); optional laya.cpp for local decisions. |
| License | [MIT](https://github.com/r3c0nc1l3r/reverie/blob/9f8ec9dcb0d9b0527d1cf900a236291fa227615a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Exploratory or regression browser tests written as Markdown specs.
- Mismatch: drives a real browser and can sign in; review guards before pointing at production.

## How it works

See the upstream [README](https://github.com/r3c0nc1l3r/reverie/blob/9f8ec9dcb0d9b0527d1cf900a236291fa227615a/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/r3c0nc1l3r/reverie.git && cd reverie
uv sync
cp .env.example .env   # set OPENROUTER_API_KEY
```

## Limits and data handling

Page observations go to OpenRouter (Jev, pilot, text model) unless Laya is local. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 9f8ec9dcb0d9](https://github.com/r3c0nc1l3r/reverie/tree/9f8ec9dcb0d9b0527d1cf900a236291fa227615a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
