# jev-local

[All projects](../README.md) · [Independent model research](README.md#independent-model-research)

Local CPU-only Jev-style 0.8B decision service plus an oh-my-pi extension that points the agent's `typesafe` judge provider at it, reading yes/no logits from llama.cpp.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/7n1m4/jev) |
| Maintainer | [7n1m4](https://github.com/7n1m4). Independently curated. |
| Format | Local service + oh-my-pi extension |
| Requirements | Linux with systemd, llama.cpp, oh-my-pi. |
| License | No LICENSE file on the reviewed commit. No open-source license is granted; do not treat as OSI open source. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`service/service.py`](https://github.com/7n1m4/jev/blob/3f6cf8807f69696512159ef9e195868b166768f8/service/service.py) at the pinned commit. |

## When to use

- Run oh-my-pi's judge role locally without cloud calls or keys.
- Mismatch: no LICENSE file; Jev-style model, not TypeSafe Jev.

## How it works

The scorer reads `logit[' yes'] - logit[' no']` at each slot (no text generated); the service exposes the oh-my-pi `systemone` contract on loopback. Integration evidence: [`service/service.py`](https://github.com/7n1m4/jev/blob/3f6cf8807f69696512159ef9e195868b166768f8/service/service.py).

## Get started

From the upstream README (not run on the review host):

```sh
./install.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- systemd unit: `systemd/jev-style-decision.service`.

## Limits and data handling

Runs locally on loopback.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 3f6cf8807f69](https://github.com/7n1m4/jev/tree/3f6cf8807f69696512159ef9e195868b166768f8). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
