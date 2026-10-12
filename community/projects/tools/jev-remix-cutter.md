# jev-remix-cutter

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Independent Agent Skill and Python CLI for local video remixing: shot awareness, beat/narration slots, TypeSafe Jev judgments, constrained assembly, and originality/licensing reports (distinct from jev-highlight-cutter).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/gnipbao/jev-remix-cutter) |
| Maintainer | [gnipbao](https://github.com/gnipbao). Independently curated. |
| Format | Python · Agent Skill + CLI (vendors jevkit) |
| Requirements | Python; TypeSafe key for live Jev text calls; local media toolchain per README. |
| License | [MIT](https://github.com/gnipbao/jev-remix-cutter/blob/3a6b003728b2a18c2756062e11cb79bda978afde/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Automate constrained remix cuts with an auditable Jev judgment layer.
- Mismatch: Early 0.1.0—some E3/E4 paths and image providers incomplete per upstream coverage notes.

## How it works

Pipeline stages call Jev (via vendored jevkit pinned to jev-1.13.0) for slot-fit and related judgments before hard gates. Jev client: [`_vendor/jevkit/jev.py`](https://github.com/gnipbao/jev-remix-cutter/blob/3a6b003728b2a18c2756062e11cb79bda978afde/_vendor/jevkit/jev.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/gnipbao/jev-remix-cutter.git
cd jev-remix-cutter
# install per README; requires Python deps
```

## Limits and data handling

Text prompts/metadata for judgments go to TypeSafe when live; media stays local unless configured otherwise. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 3a6b003728b2](https://github.com/gnipbao/jev-remix-cutter/tree/3a6b003728b2a18c2756062e11cb79bda978afde). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
