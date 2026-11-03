# jev-toolkit (Python judge interface for Jev plus a Claude Code mod that routes each prompt's model and effort)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Small tools that put a judgement model next to a generative LLM. The working parts are `jev_core` (a judge interface with a Jev adapter, a fake judge, cache and decision log) and a `jev-router` mod for Claude Code that asks Jev about each prompt and either suggests (advise mode) or switches model and effort (auto mode); the context compiler is measurement only and the rest are designs, not built. The author calls it a learning project.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Wrenik/jev-toolkit) |
| Maintainer | [Wrenik](https://github.com/Wrenik). Independently curated. |
| Format | Python package with a Claude Code mod |
| Requirements | Python 3.11+; Claude Code with mod support for the router; a TypeSafe key (or `JEV_JUDGE=fake` for offline runs). |
| License | [MIT](https://github.com/Wrenik/jev-toolkit/blob/94a00eccc21b3ee933fc300e568a21c2e2e96ade/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_core/jev.py`](https://github.com/Wrenik/jev-toolkit/blob/94a00eccc21b3ee933fc300e568a21c2e2e96ade/src/jev_core/jev.py) at the pinned commit. |

## When to use

- Route Claude Code prompts to a model and effort tier using typed Jev answers, starting in advise mode.
- Mismatch: only the core and the router are working, and the README says the router is still being tuned.

## How it works

`src/jev_core/jev.py` is the only module importing the TypeSafe SDK; it implements the `Judge` interface with `pick` and `rate` questions so a local or other provider can replace it, and logs a hash and length of each state rather than the text. Integration evidence: [`src/jev_core/jev.py`](https://github.com/Wrenik/jev-toolkit/blob/94a00eccc21b3ee933fc300e568a21c2e2e96ade/src/jev_core/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
python -m venv .venv
.venv/bin/python -m pip install -e ".[dev]"
cp .env.example .env   # key, or JEV_JUDGE=fake
.venv/bin/python -m jev_core check
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with project status and the router install: [github.com/Wrenik/jev-toolkit#readme](https://github.com/Wrenik/jev-toolkit#readme)

## Limits and data handling

Everything passed as state goes to TypeSafe; the README notes where it is processed is not stated in TypeSafe's docs (checked 2026-10-30) and warns against sending secrets. Live calls are not covered by an automated test. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit 94a00eccc21b](https://github.com/Wrenik/jev-toolkit/tree/94a00eccc21b3ee933fc300e568a21c2e2e96ade). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
