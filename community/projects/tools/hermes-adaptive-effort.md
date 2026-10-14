# Hermes Adaptive Effort

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent plugin that asks a separate scorer (Jev by default) to judge each task and sets the outgoing request's reasoning effort.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/atostivint/hermes-adaptive-effort) |
| Maintainer | [atostivint](https://github.com/atostivint). Independently curated. |
| Format | Hermes Agent plugin (Python) |
| Requirements | Hermes Agent; `TYPESAFE_API_KEY` for the default Jev scorer (OpenAI Decisions, OpenRouter, Clef or custom endpoints optional). |
| License | [MIT](https://github.com/atostivint/hermes-adaptive-effort/blob/3a7c5335181b122c7d434ece4b0c18a99c6240e3/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`jev_client.py`](https://github.com/atostivint/hermes-adaptive-effort/blob/3a7c5335181b122c7d434ece4b0c18a99c6240e3/jev_client.py) at the pinned commit. |

## When to use

- Lower reasoning-effort cost on easy Hermes turns while keeping high effort for hard ones.
- Mismatch: v0.3.0 pre-release; live effort acceptance only partly validated upstream.

## How it works

The scorer judges the task; code maps the result onto a supported effort field on registered routes. The plugin starts off; if classification fails the original request continues unchanged. Integration evidence: [`jev_client.py`](https://github.com/atostivint/hermes-adaptive-effort/blob/3a7c5335181b122c7d434ece4b0c18a99c6240e3/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
hermes plugins install 'atostivint/hermes-adaptive-effort' --enable
export TYPESAFE_API_KEY="YOUR_KEY"
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Release notes and validation status: `docs/releases/v0.3.0.md`.
- Scorer clients: `jev_client.py`, `openai_decision_client.py`, `openrouter_client.py`.

## Limits and data handling

Task text goes to the selected scorer provider. Pre-release; not run on the review host.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit 3a7c5335181b](https://github.com/atostivint/hermes-adaptive-effort/tree/3a7c5335181b122c7d434ece4b0c18a99c6240e3). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
