# hermes-jev-helper

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent `pre_llm_call` plugin: TypeSafe Jev (via OpenRouter Decisions, model `~typesafe/jev-latest`) classifies each turn into a closed route set and injects a natural-language path guide—fail-open without a key.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/maurorosero/hermes-jev-helper) |
| Maintainer | [maurorosero](https://github.com/maurorosero). Independently curated. |
| Format | Python Hermes plugin (`plugin.yaml`, `classifier.py`, `routing.py`). |
| Requirements | Hermes Agent; credential env (default `OPENROUTER_API_KEY`) for Decisions/`~typesafe/jev-latest`. |
| License | [MIT](https://github.com/maurorosero/hermes-jev-helper/blob/b535286792ca4c67d56bf25b0a1da77eae1b8821/LICENSE). |
| Disclosure | AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live Hermes/Jev not run. |

## When to use

Use it to **stabilize Hermes routing** (skill vs research vs memory…) before the main model acts. Prefer [Hermes Jev Skills](hermes-jev-skills.md) for a broader skill pack, or [hermes-jev-curator](hermes-jev-curator.md) for skill archival judgments.

## How it works

[`classifier.py`](https://github.com/maurorosero/hermes-jev-helper/blob/b535286792ca4c67d56bf25b0a1da77eae1b8821/classifier.py) POSTs a Choice question to the Decisions endpoint; on success the plugin injects a route guide. Errors/missing keys return `None` and the turn continues unchanged.

## Get started

```sh
hermes plugins install maurorosero/hermes-jev-helper
hermes plugins enable hermes-jev-helper
# or: clone b535286792ca4c67d56bf25b0a1da77eae1b8821 and hermes plugins install ./hermes-jev-helper
# set OPENROUTER_API_KEY (or configured api_key_env)
```

## Examples and demos

- `evidence/` comparison scripts and JSON runs in-repo.
- `tests/test_plugin.py` (not executed on this review host).

## Limits and data handling

Turn text used for classification leaves the host to OpenRouter/TypeSafe when enabled. Fail-open by design—do not treat silence as a hard deny.

## Review and maintenance

Reviewed **2026-09-24** (Europe/Sofia) at [commit b535286](https://github.com/maurorosero/hermes-jev-helper/tree/b535286792ca4c67d56bf25b0a1da77eae1b8821). AI-assisted README + `classifier.py` inspection. No live Hermes/TypeSafe run.

Related: [Hermes Jev Skills](hermes-jev-skills.md), [hermes-jev-curator](hermes-jev-curator.md), [ask-jev-skill](ask-jev-skill.md).
