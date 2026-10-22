# TypeSafe Unofficial CLI (Jev from the terminal, TypeSafe or OpenRouter)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Unofficial command-line interface for TypeSafe System One models: log in per provider profile, then ask noul, choice or score questions about some text from flags or a JSON or YAML questions file, on TypeSafe or OpenRouter.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gajaguar/typesafe-cli) |
| Maintainer | [gajaguar](https://github.com/gajaguar). Independently curated. |
| Format | Python CLI (PyPI: typesafe-unofficial-cli) |
| Requirements | Python 3.14+; a TypeSafe or OpenRouter API key. |
| License | [MIT](https://github.com/gajaguar/typesafe-cli/blob/397ca30be43b3d7417e03fc296e086bb4be2bf52/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/typesafe_unofficial_cli/commands/ask.py`](https://github.com/gajaguar/typesafe-cli/blob/397ca30be43b3d7417e03fc296e086bb4be2bf52/src/typesafe_unofficial_cli/commands/ask.py) at the pinned commit. |

## When to use

- Try Jev questions from the shell or in scripts without writing code.
- Switch between TypeSafe and OpenRouter with named profiles.
- Mismatch: unofficial and not affiliated with TypeSafe or OpenRouter.

## How it works

`commands/ask.py` builds the questions from flags or a file and calls the chosen provider through `typesafe-sdk`, defaulting to `jev-latest` when no model is set. Integration evidence: [`src/typesafe_unofficial_cli/commands/ask.py`](https://github.com/gajaguar/typesafe-cli/blob/397ca30be43b3d7417e03fc296e086bb4be2bf52/src/typesafe_unofficial_cli/commands/ask.py).

## Get started

From the upstream README (not run on the review host):

```sh
uv tool install typesafe-unofficial-cli
typesafe auth login
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Questions file format and usage in the README: [github.com/gajaguar/typesafe-cli#readme](https://github.com/gajaguar/typesafe-cli#readme)

## Limits and data handling

Text you pass is sent to the selected provider. Separate project from the catalog's other typesafe-cli listing.

## Review and maintenance

Reviewed **2026-10-23** (Europe/Sofia) at [commit 397ca30be43b](https://github.com/gajaguar/typesafe-cli/tree/397ca30be43b3d7417e03fc296e086bb4be2bf52). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
