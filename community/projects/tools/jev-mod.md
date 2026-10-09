# Jev-Mod

[All projects](../README.md) · [Customer feedback and marketing](README.md#customer-feedback-and-marketing)

Open-source Discord moderation bot where TypeSafe Jev rules detect spam, phishing, harassment, hate, threats and explicit text, with log/delete/timeout actions, local phrase and mention filters, exceptions and a case dashboard; use the hosted service with your own TypeSafe key or self-host.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/i098/jev-mod) |
| Maintainer | [i098](https://github.com/i098). Independently curated. |
| Format | Discord bot + web dashboard (hosted at jevmod.us, or self-host) |
| Requirements | Discord server with Manage Server; your TypeSafe API key. |
| License | [MIT](https://github.com/i098/jev-mod/blob/9b66d6ae538ef607c27bedd6879628508917146e/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Community moderation with a monitor-only mode before enforcing.
- Mismatch: hosted service is third-party; self-host if messages must stay with you.

## How it works

See the upstream [README](https://github.com/i098/jev-mod/blob/9b66d6ae538ef607c27bedd6879628508917146e/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/i098/jev-mod.git   # self-host, see docs/guide.md
```

## Limits and data handling

Message text goes to TypeSafe with your key; hosted mode also runs through the maintainer's service. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 9b66d6ae538e](https://github.com/i098/jev-mod/tree/9b66d6ae538ef607c27bedd6879628508917146e). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
