# Decision Tagger (Obsidian)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Obsidian tagging assistant: TypeSafe Jev judges customizable tag rules with multi-key parallel vault scans.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/xinye1017/obsidian-decision-tagger) |
| Maintainer | [xinye1017](https://github.com/xinye1017). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Obsidian community-style plugin (JavaScript). |
| Requirements | Obsidian; TypeSafe (or compatible) API key(s) for live tagging. |
| License | [MIT](https://github.com/xinye1017/obsidian-decision-tagger/blob/1ec2a2c642635f7a88c0b703358a287847510c98/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use to auto-tag large Obsidian vaults with System One rules. Prefer manual tags when notes must never leave the device.

## How it works

Rules map tags to decision questions; Jev returns calibrated matches. Batch mode fans out across keys with rate-limit cooldown; single-note mode suggests recommended tags. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/xinye1017/obsidian-decision-tagger.git
cd obsidian-decision-tagger
git checkout 1ec2a2c642635f7a88c0b703358a287847510c98
# follow upstream README / Releases for Obsidian install and API key settings
```

Pin revision `1ec2a2c642635f7a88c0b703358a287847510c98` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live Obsidian/TypeSafe tagging not run on the review host. Note text is sent to the configured provider when classifying.

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 1ec2a2c](https://github.com/xinye1017/obsidian-decision-tagger/tree/1ec2a2c642635f7a88c0b703358a287847510c98). AI-assisted README and LICENSE inspection; install/live paths not executed.
