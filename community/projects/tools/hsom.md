# hsom (jevdo)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

hsom (Harness for System One Models, repository jevdo) lets Jev operate a bash shell by walking a strict-allowlist decision tree of commands, subcommands, flags and path slots defined in a TOML file.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gi-dellav/jevdo) |
| Maintainer | [gi-dellav](https://github.com/gi-dellav). Independently curated. |
| Format | Python CLI |
| Requirements | Python; a TypeSafe or OpenRouter API key. |
| License | [GPL-3.0](https://github.com/gi-dellav/jevdo/blob/f6797a6e7fdceea3e7d158c5dc9e1a1097c67e92/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Turn plain-language requests into allowlisted shell commands with confirmation for writes.
- Mismatch: only commands defined in `environment.toml` are reachable; not a general shell agent.

## How it works

Jev picks command, then subcommand, flags and path slots by navigating the TOML-defined tree; read actions run directly, write and destructive actions ask for confirmation, and `--dry-run` previews. (Summarized from the upstream [README](https://github.com/gi-dellav/jevdo/blob/f6797a6e7fdceea3e7d158c5dc9e1a1097c67e92/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): `pip install -e .`, export `TYPESAFE_API_KEY`, and copy `environment.toml.example` to `environment.toml`.

## Limits and data handling

Requests and shell context are sent to the configured provider. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit f6797a6e7fdc](https://github.com/gi-dellav/jevdo/tree/f6797a6e7fdceea3e7d158c5dc9e1a1097c67e92). Inspected the upstream README and LICENSE status at the pinned commit; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
