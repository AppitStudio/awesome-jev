# FederationJevGuard (FederationLib plugin where Jev reviews spam reports, evidence and repeat offenders, and acts only when confident)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Plugin for FederationLib, a PHP service for sharing spam, scam, phishing and malware reports: it closes open reports the model is confident about, classifies unassigned evidence and content scans (including images), and temporarily blacklists entities with repeated spam reports. The model sees the full context (report, sender history, messages, attachments, earlier decisions); code decides what the answers mean, and anything uncertain is left to operators.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/nosial/FederationJevGuard) |
| Maintainer | [nosial](https://github.com/nosial). Independently curated. |
| Format | FederationLib plugin (PHP, ncc package; MIT) |
| Requirements | FederationLib 2.1.0+, PHP with GD and exif, and a TypeSafe key (`FEDERATION_JEVGUARD_SYSTEMONE_API_KEY`). |
| License | [MIT](https://github.com/nosial/FederationJevGuard/blob/19184bd9059f061d0ac4c935cd12a3cab4e39e71/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/FederationJevGuard/Classes/Configuration/SystemOneConfiguration.php`](https://github.com/nosial/FederationJevGuard/blob/19184bd9059f061d0ac4c935cd12a3cab4e39e71/src/FederationJevGuard/Classes/Configuration/SystemOneConfiguration.php) at the pinned commit. |

## When to use

- Cut operator workload on a FederationLib instance by auto-closing clear-cut spam reports.
- Mismatch: deployments without FederationLib.

## How it works

`SystemOneConfiguration.php` defaults the endpoint to `https://api.typesafe.ai/v1/systemone` and checks whether the configured host is TypeSafe's; another System One-compatible endpoint can be configured. Questions and judges live under `src/FederationJevGuard/`. Integration evidence: [`src/FederationJevGuard/Classes/Configuration/SystemOneConfiguration.php`](https://github.com/nosial/FederationJevGuard/blob/19184bd9059f061d0ac4c935cd12a3cab4e39e71/src/FederationJevGuard/Classes/Configuration/SystemOneConfiguration.php).

## Get started

Build the ncc package and install it into FederationLib, or mount it in FederationLib's Docker image.

```sh
make target/release/net.nosial.federation_jevguard.ncc
ncc install --package="$PWD/target/release/net.nosial.federation_jevguard.ncc" --yes --reinstall
# then enable FEDERATION_PLUGINS=net.nosial.federation_jevguard and set the API key
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/nosial/FederationJevGuard/blob/19184bd9059f061d0ac4c935cd12a3cab4e39e71/README.md](https://github.com/nosial/FederationJevGuard/blob/19184bd9059f061d0ac4c935cd12a3cab4e39e71/README.md)
- FederationLib: [git.n64.cc/nosial/federationlib](https://git.n64.cc/nosial/federationlib)

## Limits and data handling

Report contents, sender history, messages, attachments and images are sent to TypeSafe on your key. Blacklisting is automatic when the model is confident; review the thresholds before enabling it.

## Review and maintenance

Reviewed **2026-11-15** (Europe/Sofia) at [commit 19184bd9059f](https://github.com/nosial/FederationJevGuard/tree/19184bd9059f061d0ac4c935cd12a3cab4e39e71). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
