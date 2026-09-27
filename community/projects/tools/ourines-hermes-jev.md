# hermes-jev (ourines)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent decision sidekick: explicit Jev tools and a bundled skill via TypeSafe, Cloudflare, or OpenRouter backends.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ourines/hermes-jev) |
| Maintainer | [ourines](https://github.com/ourines). Independently curated; this entry is not an upstream submission or endorsement. |
| Format | Hermes Agent plugin + skill. |
| Requirements | Hermes Agent; TypeSafe, Cloudflare, or OpenRouter credentials depending on backend. |
| License | [MIT](https://github.com/ourines/hermes-jev/blob/1aff078e5d11d16e951b511ed7b23fe27075f627/LICENSE). Provider usage may incur charges when live. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from hermes-jev-skills, hermes-jev-helper, and hermes-jev-curator. |

## When to use

Use when Hermes should call Jev as an explicit tool/skill rather than a chat-model provider. Prefer Hermes Jev Skills for a broader routing/memory pack.

## How it works

Plugin registers decision tools and a pinned official skill; backends include `api.typesafe.ai/v1/systemone`, Cloudflare `typesafe/jev`, and OpenRouter Decisions. Setup writes credentials into the Hermes profile without changing the main model. Integration evidence: upstream README and source at the pinned commit below.

## Get started

```sh
git clone https://github.com/ourines/hermes-jev.git
cd hermes-jev
git checkout 1aff078e5d11d16e951b511ed7b23fe27075f627
# follow upstream README for install/run; configure credentials as documented
```

Pin revision `1aff078e5d11d16e951b511ed7b23fe27075f627` when reproducing this review.

## Examples and demos

See the upstream README at the pinned commit. No separate live demo was executed on the review host.

## Limits and data handling

Live calls send task/context text to the configured provider (TypeSafe and/or OpenRouter/Cloudflare per upstream). Distinct from hermes-jev-skills, hermes-jev-helper, and hermes-jev-curator. Live paths not run on the review host.

## Review and maintenance

Reviewed **2026-09-27** (Europe/Sofia) at [commit 1aff078e5d11](https://github.com/ourines/hermes-jev/tree/1aff078e5d11d16e951b511ed7b23fe27075f627). AI-assisted README and LICENSE inspection; install/live paths not executed.
