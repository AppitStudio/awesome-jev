# JEV WHERE?

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin that reads your app and ranks the fuzzy decision points (regex routers, keyword priorities, yes/no LLM calls) where TypeSafe Jev could make the call, with the typed question for each.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/cesarroger/jev-where) |
| Maintainer | [cesarroger](https://github.com/cesarroger). Independently curated. |
| Format | Claude Code plugin / skill |
| Requirements | Claude Code; network access for live sightings checks. |
| License | [MIT](https://github.com/cesarroger/jev-where/blob/4a038037890a0317382f7ec5833872a0a1015deb/LICENSE) |
| Jev evidence | [`skills/jev-where/scripts/jev_radar.py`](https://github.com/cesarroger/jev-where/blob/4a038037890a0317382f7ec5833872a0a1015deb/skills/jev-where/scripts/jev_radar.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Audit an existing codebase for Jev experiments, with cited examples from other projects.
- Mismatch: suggestions only; it never edits code and does not call Jev on your data itself.

## How it works

The skill scans the repository for decision-shaped code, drafts the Jev question and fallback for each, and cites similar public projects from its sightings list (rechecked live). (Summarized from the upstream [README](https://github.com/cesarroger/jev-where/blob/4a038037890a0317382f7ec5833872a0a1015deb/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the plugin from the repo's Claude Code marketplace entry and run the JEV WHERE skill in your project.

## Limits and data handling

Reads your code locally inside Claude Code; also flags hardcoded secrets it notices. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 4a038037890a](https://github.com/cesarroger/jev-where/tree/4a038037890a0317382f7ec5833872a0a1015deb). Inspected the upstream README, LICENSE (where present), and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
