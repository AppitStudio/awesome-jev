# Jev-Mod (undeemed)

[All projects](../README.md) · [Discord bots](README.md#discord-bots)

Jev-powered Discord moderation with configurable TypeSafe rules, hosted dashboard, and Cloudflare/Docker self-host options

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/undeemed/jev-mod) |
| Tags | `Open source` · `Free source build` · `BYOK` |
| Product homepage | [jevmod.us](https://jevmod.us) |
| Pricing and access | MIT source and hosted dashboard at jevmod.us / app.jevmod.us with Discord OAuth; bring your own TypeSafe key. No separate app purchase fee documented; TypeSafe and self-host infrastructure costs separate. Checked 2026-09-29. |
| Jev evidence | Upstream README and docs: configure TypeSafe Jev rules for spam/phishing/harassment/hate/threats/explicit text; Monitor-only then Protect modes. [README](https://github.com/undeemed/jev-mod/blob/3ff1305f53988bf70bfa4e35ded099f69579dc54/README.md). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Source inspected; live provider paths not run on the review host. Distinct from [Jev Moderation Bot](jev-moderation-bot.md) and [Soter](soter.md). |
| Maintainer | [undeemed](https://github.com/undeemed). Independently curated. |
| Format | TypeScript · Discord bot + React dashboard (MIT; Cloudflare Workers/D1 or Docker). |
| Platform and availability | Hosted [app.jevmod.us](https://app.jevmod.us); self-host Docker Compose or Cloudflare per docs. |
| Jev's role | TypeSafe Jev classifies messages against configured rules; code owns deletes, timeouts, local filters, and the dashboard. |
| Requirements | TypeSafe API key; Discord Manage Server for install. Self-host needs Docker or Cloudflare credentials per upstream. |
| License | [MIT](https://github.com/undeemed/jev-mod/blob/3ff1305f53988bf70bfa4e35ded099f69579dc54/LICENSE). Provider usage may incur charges when live. |

## When to use

Use for Discord auto-moderation with TypeSafe Jev rules and a managed dashboard. Prefer Soter or the Python Jev Moderation Bot if you already standardize on those stacks.

## How it works

Operators set Jev rules in the dashboard, test in Monitor only, then enable Protect. Local phrase/mention filters and exceptions complement Jev judgments.

## Get started

```sh
git clone https://github.com/undeemed/jev-mod.git
cd jev-mod
git checkout 3ff1305f53988bf70bfa4e35ded099f69579dc54
# or open https://app.jevmod.us — follow docs/guide.md for Cloudflare/Docker
```

Pin revision `3ff1305f53988bf70bfa4e35ded099f69579dc54` when reproducing this review.

## Examples and demos

Hosted site [jevmod.us](https://jevmod.us) and dashboard screenshots in-repo. Live moderation not run on the review host.

## Limits and data handling

Live Discord moderation and accuracy not measured on the review host. Destructive Protect mode can delete/timeout. Distinct from [Jev Moderation Bot](jev-moderation-bot.md) and [Soter](soter.md).

## Review and maintenance

Reviewed **2026-09-29** (Europe/Sofia) at [commit 3ff1305](https://github.com/undeemed/jev-mod/tree/3ff1305f53988bf70bfa4e35ded099f69579dc54). AI-assisted README and LICENSE inspection; install/live paths not executed.
