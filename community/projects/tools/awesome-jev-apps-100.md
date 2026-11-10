# Awesome Jev Apps (100 runnable example apps for TypeSafe Jev across 11 domains)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

A collection of 100 small Jev apps (support triage, tool routing, finance, documents, research and more), each with a shared provider that talks to TypeSafe or OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Justmalhar/awesome-jev-apps) |
| Maintainer | [Justmalhar](https://github.com/Justmalhar). Independently curated. |
| Format | Python example collection (MIT) |
| Requirements | Python and a TypeSafe or OpenRouter key. |
| License | [MIT](https://github.com/Justmalhar/awesome-jev-apps/blob/4e1395ec756a707706df815fa8072c194e52e2a0/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`_shared/jev_provider.py`](https://github.com/Justmalhar/awesome-jev-apps/blob/4e1395ec756a707706df815fa8072c194e52e2a0/_shared/jev_provider.py) at the pinned commit. |

## When to use

- Find a starter for a typed-decision use case.
- Compare TypeSafe direct and OpenRouter routes.
- Mismatch: examples, not production services.

## How it works

`_shared/jev_provider.py` uses the native System One format for TypeSafe direct and OpenRouter's decisions endpoint (default provider `typesafe`); each app under `apps/` reuses it. Integration evidence: [`_shared/jev_provider.py`](https://github.com/Justmalhar/awesome-jev-apps/blob/4e1395ec756a707706df815fa8072c194e52e2a0/_shared/jev_provider.py).

## Get started

Clone, copy `.env.example`, set your key and run any app under `apps/`.

```sh
git clone https://github.com/Justmalhar/awesome-jev-apps.git && cd awesome-jev-apps
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Justmalhar/awesome-jev-apps/blob/4e1395ec756a707706df815fa8072c194e52e2a0/README.md](https://github.com/Justmalhar/awesome-jev-apps/blob/4e1395ec756a707706df815fa8072c194e52e2a0/README.md)

## Limits and data handling

Each app sends its sample inputs to TypeSafe/OpenRouter on your key.

## Review and maintenance

Reviewed **2026-11-10** (Europe/Sofia) at [commit 4e1395ec756a](https://github.com/Justmalhar/awesome-jev-apps/tree/4e1395ec756a707706df815fa8072c194e52e2a0). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
