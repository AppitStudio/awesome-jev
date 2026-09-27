# pi-jev (kurowashi)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Pi coding-agent extensions that use TypeSafe Jev for semantic checks on file edits and new-file placement.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/kurowashi/pi-jev) |
| Maintainer | [kurowashi](https://github.com/kurowashi). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Pi agent extension monorepo. |
| Requirements | Pi coding agent; TypeSafe API key. |
| License | [MIT](https://github.com/kurowashi/pi-jev/blob/d9f5afed2e5989839a2f5fd1250a3534e996bd83/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from y0usaf/pi-jev and other pi-jev-* listings. |

## When to use

Use when Pi file writes need semantic content/placement gates. Prefer y0usaf/pi-jev for gate/output-judge/jev_ask tooling.

## How it works

Monorepo packages (`content-guard`, placement checks) call TypeSafe System One before accepting edits or new paths. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/kurowashi/pi-jev.git
cd pi-jev
git checkout d9f5afed2e5989839a2f5fd1250a3534e996bd83
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `d9f5afed2e5989839a2f5fd1250a3534e996bd83` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream). Distinct from y0usaf/pi-jev and other pi-jev-* listings. Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit d9f5afed2e59](https://github.com/kurowashi/pi-jev/tree/d9f5afed2e5989839a2f5fd1250a3534e996bd83). AI-assisted README and LICENSE inspection; install/live paths not executed.
