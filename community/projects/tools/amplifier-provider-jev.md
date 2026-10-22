# Amplifier Jev provider (Microsoft)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Optional, experimental provider module for Microsoft's Amplifier agent framework that exposes Jev decisions (predicate, choice and score) to consumers such as browser and computer UI use, without ever joining the chat fallback chain.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/microsoft/amplifier-module-provider-jev) |
| Maintainer | [microsoft](https://github.com/microsoft). Independently curated. |
| Format | Python provider module for Amplifier |
| Requirements | An Amplifier host with an ordinary chat provider; a TypeSafe API key. |
| License | [MIT](https://github.com/microsoft/amplifier-module-provider-jev/blob/7ccade1eed84b17f215bc2e80253a1fb4c3a2130/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`amplifier_module_provider_jev/__init__.py`](https://github.com/microsoft/amplifier-module-provider-jev/blob/7ccade1eed84b17f215bc2e80253a1fb4c3a2130/amplifier_module_provider_jev/__init__.py) at the pinned commit. |

## When to use

- Let Amplifier's UI-use behavior ask Jev for typed decisions while the chat model stays the default and fallback.
- Share one TypeSafe account across several named decision backends.
- Mismatch: marked experimental; interfaces may change, and images and Box are disabled.

## How it works

The provider owns HTTP transport to `https://api.typesafe.ai/v1/systemone` (or a configured HTTPS endpoint) with bounded time and body sizes, no automatic retries or redirects, and redacted errors; the shared `amplifier-lib-decisions` contract normalizes the answers. Integration evidence: [`amplifier_module_provider_jev/__init__.py`](https://github.com/microsoft/amplifier-module-provider-jev/blob/7ccade1eed84b17f215bc2e80253a1fb4c3a2130/amplifier_module_provider_jev/__init__.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv pip install 'amplifier-module-provider-jev @ git+https://github.com/microsoft/amplifier-module-provider-jev@main'
export TYPESAFE_API_KEY=your-key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Config example in the README: [github.com/microsoft/amplifier-module-provider-jev#readme](https://github.com/microsoft/amplifier-module-provider-jev#readme)
- Shared contract: [github.com/microsoft/amplifier-lib-decisions](https://github.com/microsoft/amplifier-lib-decisions)
- UI-use bundle: [github.com/microsoft/amplifier-bundle-ui-use](https://github.com/microsoft/amplifier-bundle-ui-use)

## Limits and data handling

Observations you allow are sent to TypeSafe; consent to transfer an observation does not approve an action. Listed independently; not an endorsement by Microsoft or TypeSafe.

## Review and maintenance

Reviewed **2026-10-22** (Europe/Sofia) at [commit 7ccade1eed84](https://github.com/microsoft/amplifier-module-provider-jev/tree/7ccade1eed84b17f215bc2e80253a1fb4c3a2130). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
