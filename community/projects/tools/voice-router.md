# voice-router (Home Assistant voice command router using TypeSafe Jev)

[All projects](../README.md) · [Home automation](README.md#home-automation)

HTTP service plus Home Assistant component that turns a spoken command into the named devices and action using TypeSafe Jev, while Home Assistant executes and logs each action.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jaimemachadoneto/voice-router) |
| Maintainer | [jaimemachadoneto](https://github.com/jaimemachadoneto). Independently curated. |
| Format | Python service + Home Assistant custom component (no SPDX license file on the reviewed commit) |
| Requirements | Python 3, Home Assistant, and an OpenRouter key with TypeSafe Jev access. |
| License | NONE on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/voice_router/jev.py`](https://github.com/jaimemachadoneto/voice-router/blob/43e3709e0c9b15df5707587b03efa2bef0d3812b/src/voice_router/jev.py) at the pinned commit. |

## When to use

- Resolve voice commands to Home Assistant entities with typed answers.
- Keep execution in Home Assistant with a logged decision trail.
- Mismatch: no OSI license on the reviewed commit.

## How it works

`src/voice_router/jev.py` calls the `systemone` endpoint (default via OpenRouter, model `~typesafe/jev-latest`) to resolve devices and actions; the router never runs actions itself. Integration evidence: [`src/voice_router/jev.py`](https://github.com/jaimemachadoneto/voice-router/blob/43e3709e0c9b15df5707587b03efa2bef0d3812b/src/voice_router/jev.py).

## Get started

Clone, set VOICE_ROUTER_TOKEN and the Jev key, run the service, and install the HA component.

```sh
git clone https://github.com/jaimemachadoneto/voice-router.git && cd voice-router
export TYPESAFE_API_KEY=...
pip install -e . && pytest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/jaimemachadoneto/voice-router/blob/43e3709e0c9b15df5707587b03efa2bef0d3812b/README.md](https://github.com/jaimemachadoneto/voice-router/blob/43e3709e0c9b15df5707587b03efa2bef0d3812b/README.md)

## Limits and data handling

Command text and device lists are sent to the configured provider.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 43e3709e0c9b](https://github.com/jaimemachadoneto/voice-router/tree/43e3709e0c9b15df5707587b03efa2bef0d3812b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
