# hermes-swift / Alpine Swift (fast, verified browser tasks for Hermes Agent)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Browser plugin for Nous Research's Hermes Agent on Ubuntu: Jev picks each step from the page's indexed controls, Inception's Mercury 3 writes form values, tasks count as verified only when a code check on the final page passes, logins and cards come from Hermes's vault so no model sees a password, and irreversible steps are reviewed.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Iamnanisyam/alpine_swift) |
| Maintainer | [Iamnanisyam](https://github.com/Iamnanisyam). Independently curated. |
| Format | Hermes Agent plugin (Python) |
| Requirements | Ubuntu 22.04/24.04, Hermes Agent and Google Chrome; a TypeSafe API key and an Inception API key. |
| License | [MIT](https://github.com/Iamnanisyam/alpine_swift/blob/e977690c7d4095aa29302d1e6651638e8ad97b18/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/IamnanisyamDara/status/2114965562145341807)). |
| Jev evidence | [`swift/config.py`](https://github.com/Iamnanisyam/alpine_swift/blob/e977690c7d4095aa29302d1e6651638e8ad97b18/swift/config.py) at the pinned commit. |

## When to use

- Give Hermes faster browser actions with code-checked results.
- Mismatch: Ubuntu and Hermes only; speed figures are the author's; builds on browser-use's Jev Ultrafast code (MIT, credited).

## How it works

`swift/config.py` points at `https://api.typesafe.ai/v1/systemone` with pinned `jev-1.14.0`; `swift/jev.py` sends the indexed controls for one action choice per step. Integration evidence: [`swift/config.py`](https://github.com/Iamnanisyam/alpine_swift/blob/e977690c7d4095aa29302d1e6651638e8ad97b18/swift/config.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/Iamnanisyam/alpine_swift && cd alpine_swift
bash deploy/install-ubuntu.sh
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Iamnanisyam/alpine_swift#readme](https://github.com/Iamnanisyam/alpine_swift#readme)

## Limits and data handling

Page controls go to TypeSafe and form context to Inception; secrets stay in Hermes's vault. Discovered on X from the creator's post.

## Review and maintenance

Reviewed **2026-10-27** (Europe/Sofia) at [commit e977690c7d40](https://github.com/Iamnanisyam/alpine_swift/tree/e977690c7d4095aa29302d1e6651638e8ad97b18). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
