# aiscript

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

CLI that turns a plain-English intent into a cached Bash or PowerShell script written by an LLM, then checks every generated script with a static scan and optionally Jev (or a local Ollaya model) before it is saved or run; risky scripts need an explicit approval.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/illescasDaniel/aiscript) |
| Maintainer | [illescasDaniel](https://github.com/illescasDaniel). Independently curated. |
| Format | Command-line tool (Python 3.10+, PyPI) |
| Requirements | Python 3.10+; an OpenAI key for writing scripts; `TYPESAFE_API_KEY` for Jev review (or a local Ollaya model instead). |
| License | [MIT](https://github.com/illescasDaniel/aiscript/blob/b3ed3a6e0680f2f3d7de3d38fecf928235eba8db/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/aiscript/config.py`](https://github.com/illescasDaniel/aiscript/blob/b3ed3a6e0680f2f3d7de3d38fecf928235eba8db/src/aiscript/config.py) at the pinned commit. |

## When to use

- Reuse one-off shell tasks as cached scripts that run instantly next time.
- Add a decision-model safety review before generated scripts run.
- Mismatch: the writer is a generative LLM; review approvals carefully.

## How it works

The writer model (`default_provider`) generates the script once and aiscript caches it. Before saving or running, a static scan and the reviewer (`reviewer_provider`) check it; `src/aiscript/config.py` sets Jev's default model `jev-latest` and reads `TYPESAFE_API_KEY`. Risky scripts are shown with a `[y/N]` prompt. Integration evidence: [`src/aiscript/config.py`](https://github.com/illescasDaniel/aiscript/blob/b3ed3a6e0680f2f3d7de3d38fecf928235eba8db/src/aiscript/config.py).

## Get started

From the upstream README: install from PyPI, then create the config file and add keys.

```sh
uv tool install aiscript
aiscript --init
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- docs/development.md

## Limits and data handling

Your intent and generated scripts go to the configured providers. A passed review is a model judgment, not a guarantee the script is safe.

## Review and maintenance

Reviewed **2026-10-20** (Europe/Sofia) at [commit b3ed3a6e0680](https://github.com/illescasDaniel/aiscript/tree/b3ed3a6e0680f2f3d7de3d38fecf928235eba8db). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
