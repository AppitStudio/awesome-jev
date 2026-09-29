# omo-jev-plugin

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Jev-powered decision support for OmO and senpi agents (advise/act modes).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/brianhong-dev/omo-jev-plugin) |
| Maintainer | [brianhong-dev](https://github.com/brianhong-dev). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | OmO / senpi npm plugin. |
| Requirements | OmO or senpi; `TYPESAFE_API_KEY` or `~/.omo/jev-plugin.jsonc` apiKey. |
| License | [MIT](https://github.com/brianhong-dev/omo-jev-plugin/blob/7a8e9783a9656de8bf0f035beca7486222f2507b/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. |

## When to use

Use when OmO/senpi agents should get Jev advice on skill/tool choices without replacing host permissions.

## How it works

Plugin modes off/shadow/advise/act; Jev judges skill and next-action fit, loop detection, and completion without executing tools itself. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/brianhong-dev/omo-jev-plugin.git
cd omo-jev-plugin
git checkout 7a8e9783a9656de8bf0f035beca7486222f2507b
# or: omo install npm:omo-jev-plugin
# set mode/apiKey per upstream README
```

Pin revision `7a8e9783a9656de8bf0f035beca7486222f2507b` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Default mode is off until configured. Live OmO/Jev paths not run on the review host. Upstream README is primarily Korean.

## Review and maintenance

Reviewed **2026-09-28** (Europe/Sofia) at [commit 7a8e978](https://github.com/brianhong-dev/omo-jev-plugin/tree/7a8e9783a9656de8bf0f035beca7486222f2507b). AI-assisted README and LICENSE inspection; install/live paths not executed.
