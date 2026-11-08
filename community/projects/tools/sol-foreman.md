# Sol Foreman (Codex skill for delegated builds with optional TypeSafe Jev advisory routing)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Standalone Codex skill for leading delegated builds with economical model routing and accountable acceptance; an opt-in, advisory Jev script helps choose routes and records the served model.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/olsenbrands/sol-foreman) |
| Maintainer | [olsenbrands](https://github.com/olsenbrands). Independently curated. |
| Format | Codex skill (Python script, MIT) |
| Requirements | Codex, Python 3, and an OpenRouter key for the optional Jev step. |
| License | [MIT](https://github.com/olsenbrands/sol-foreman/blob/46d5c97c27b7a71a8123034074b598872fdace81/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/sol-foreman/scripts/jev_decide.py`](https://github.com/olsenbrands/sol-foreman/blob/46d5c97c27b7a71a8123034074b598872fdace81/skills/sol-foreman/scripts/jev_decide.py) at the pinned commit. |

## When to use

- Lead delegated Codex builds with explicit acceptance checks.
- Get a cheap advisory routing signal from Jev.
- Mismatch: Jev is opt-in and advisory only.

## How it works

`skills/sol-foreman/scripts/jev_decide.py` posts to `https://openrouter.ai/api/alpha/decisions` with `~typesafe/jev-latest`, falling back to pinned `jev-1.14`/`jev-1.13` only if the alias is not found. Integration evidence: [`skills/sol-foreman/scripts/jev_decide.py`](https://github.com/olsenbrands/sol-foreman/blob/46d5c97c27b7a71a8123034074b598872fdace81/skills/sol-foreman/scripts/jev_decide.py).

## Get started

Copy the skill into your Codex skills folder and optionally set an OpenRouter key.

```sh
git clone https://github.com/olsenbrands/sol-foreman.git && cd sol-foreman
export OPENROUTER_API_KEY=...
python -m pytest
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/olsenbrands/sol-foreman/blob/46d5c97c27b7a71a8123034074b598872fdace81/README.md](https://github.com/olsenbrands/sol-foreman/blob/46d5c97c27b7a71a8123034074b598872fdace81/README.md)

## Limits and data handling

Task summaries sent for advice go to OpenRouter/TypeSafe on your key.

## Review and maintenance

Reviewed **2026-11-08** (Europe/Sofia) at [commit 46d5c97c27b7](https://github.com/olsenbrands/sol-foreman/tree/46d5c97c27b7a71a8123034074b598872fdace81). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
