# PragYantra (embodied assistant software with optional Jev request interpretation)

[All projects](../README.md) · [Home automation](README.md#home-automation)

Python software for an embodied assistant (seeing, hearing, conversation, memory and a sensor boundary) where optional TypeSafe Jev judgments interpret requests into bounded choices, separately from generated conversation; built on OpenAI inference with Raspberry Pi deployment still unvalidated.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/sriramsme/pragYantra) |
| Maintainer | [sriramsme](https://github.com/sriramsme). Independently curated. |
| Format | Python CLI application (GPL-3.0) |
| Requirements | Python 3.12 with uv, `OPENAI_API_KEY`, and `TYPESAFE_API_KEY` with the `decisions` extra for Jev. |
| License | [GPL-3.0](https://github.com/sriramsme/pragYantra/blob/57068a8aa33c92b8f489568a7902af20080200e0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/pragyantra/providers/typesafe.py`](https://github.com/sriramsme/pragYantra/blob/57068a8aa33c92b8f489568a7902af20080200e0/src/pragyantra/providers/typesafe.py) at the pinned commit. |

## When to use

- Experiment with an assistant that uses typed decisions instead of free text for request handling.
- Mismatch: no robot or actuator control; microphone and Pi deployment not yet validated on devices.

## How it works

`src/pragyantra/providers/typesafe.py` isolates TypeSafe Jev request interpretation (default model `jev-1.14.0`) from application policy; explicit memory commands and device actions stay in application code. Integration evidence: [`src/pragyantra/providers/typesafe.py`](https://github.com/sriramsme/pragYantra/blob/57068a8aa33c92b8f489568a7902af20080200e0/src/pragyantra/providers/typesafe.py).

## Get started

Install the tool with the `decisions` extra and add both keys to `.env`.

```sh
uv tool install --editable '.[audio,webcam,decisions]' --python 3.12
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/sriramsme/pragYantra/blob/57068a8aa33c92b8f489568a7902af20080200e0/README.md](https://github.com/sriramsme/pragYantra/blob/57068a8aa33c92b8f489568a7902af20080200e0/README.md)

## Limits and data handling

Requests and webcam descriptions go to OpenAI and, when enabled, TypeSafe on your keys.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit 57068a8aa33c](https://github.com/sriramsme/pragYantra/tree/57068a8aa33c92b8f489568a7902af20080200e0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
