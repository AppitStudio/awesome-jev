# jev-sec-audit

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Lightning-fast AI supply-chain security auditor: TypeSafe Jev scores typosquatting and malicious package scripts in milliseconds (CLI + GitHub Action)

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/DhanushNehru/jev-sec-audit) |
| Maintainer | [DhanushNehru](https://github.com/DhanushNehru). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | CLI and GitHub Action (npm `jev-sec-audit`). |
| Requirements | Node.js; optional `TYPESAFE_API_KEY` / provider config per upstream README. |
| License | [Apache-2.0](https://github.com/DhanushNehru/jev-sec-audit/blob/b61fe1b7d7b928156dbfe64d75dd9fd4ef800f22/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to scan `package.json` dependency trees and lifecycle scripts for typosquatting, obfuscation, and destructive install hooks before they ship. Prefer heavier SAST/SCA suites when you need deep code analysis beyond npm metadata.

## How it works

Deterministic tree walk plus typed Jev judgments for severity/confidence on suspicious packages and scripts; outputs an ANSI table. Integration evidence: upstream README and source at the pinned commit.

## Get started

```sh
git clone https://github.com/DhanushNehru/jev-sec-audit.git
cd jev-sec-audit
git checkout b61fe1b7d7b928156dbfe64d75dd9fd4ef800f22
```

Pin revision `b61fe1b7d7b928156dbfe64d75dd9fd4ef800f22` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live TypeSafe/provider calls and install paths were not executed on the review host. Treat upstream benchmarks and measured claims as author-reported unless independently reproduced.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit b61fe1b](https://github.com/DhanushNehru/jev-sec-audit/tree/b61fe1b7d7b928156dbfe64d75dd9fd4ef800f22). AI-assisted README and LICENSE inspection; install/live paths not executed.
