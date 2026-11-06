# jev-toolkit-usage (Claude Code judge interface and model/effort router with TypeSafe Jev)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Experimental Claude Code toolkit: a judge interface, offline fake judge, and model/effort router built on typed judgments, with `TYPESAFE_API_KEY` wiring into `src/jev_core` for live TypeSafe Jev calls.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Wrenik/Jev-toolkit-usage) |
| Maintainer | [Wrenik](https://github.com/Wrenik). Independently curated. |
| Format | Python package + Claude Code plugin hooks (MIT) |
| Requirements | Claude Code (for the plugin path) and a TypeSafe API key for live judgments. |
| License | [MIT](https://github.com/Wrenik/Jev-toolkit-usage/blob/53c966b9ab4d8e2a22606e97c82680ecbdecbe5b/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/jev_core/jev.py`](https://github.com/Wrenik/Jev-toolkit-usage/blob/53c966b9ab4d8e2a22606e97c82680ecbdecbe5b/src/jev_core/jev.py) at the pinned commit. |

## When to use

- Route Claude Code model/effort with typed Jev judgments.
- Run an offline fake judge in CI.
- Mismatch: experimental learning project; APIs may change.

## How it works

`src/jev_core/jev.py` talks to TypeSafe System One when `TYPESAFE_API_KEY` is set; `__main__.py` reports missing keys and points at `.env`. Integration evidence: [`src/jev_core/jev.py`](https://github.com/Wrenik/Jev-toolkit-usage/blob/53c966b9ab4d8e2a22606e97c82680ecbdecbe5b/src/jev_core/jev.py).

## Get started

Clone, copy `.env.example`, set `TYPESAFE_API_KEY`, and install the Claude Code plugin hooks per README.

```sh
git clone https://github.com/Wrenik/Jev-toolkit-usage.git && cd Jev-toolkit-usage
cp .env.example .env  # set TYPESAFE_API_KEY
# follow README for Claude Code plugin hooks
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/Wrenik/Jev-toolkit-usage/blob/53c966b9ab4d8e2a22606e97c82680ecbdecbe5b/README.md](https://github.com/Wrenik/Jev-toolkit-usage/blob/53c966b9ab4d8e2a22606e97c82680ecbdecbe5b/README.md)

## Limits and data handling

Judgment state/questions are sent to TypeSafe on your key when live mode is enabled. Experimental status—pin a commit.

## Review and maintenance

Reviewed **2026-11-07** (Europe/Sofia) at [commit 53c966b9ab4d](https://github.com/Wrenik/Jev-toolkit-usage/tree/53c966b9ab4d8e2a22606e97c82680ecbdecbe5b). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
