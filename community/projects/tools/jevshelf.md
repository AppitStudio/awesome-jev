# JevShelf

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Portable, Skillshare-compatible skill shelf: expose one small router skill to your coding agent and let lexical/BM25 search or Jev choose which specialist `SKILL.md` to load on demand.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ham-zax/jevshelf) |
| Maintainer | [ham-zax](https://github.com/ham-zax). Independently curated. |
| Format | Python CLI + `SKILL.md` shims |
| Requirements | Git, uv, Python 3.11+; optional `TYPESAFE_API_KEY` or `JEV_API_KEY` for `--mode jev`. |
| License | [MIT](https://github.com/ham-zax/jevshelf/blob/3fb8b9a35048150ffb9cbb6985e6944107d78e13/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Keep agent context small when you maintain dozens of specialist skills.
- Share one skill library across Claude Code, Codex and other Skillshare targets.
- Mismatch: Jev mode is optional; lexical mode works offline. Not zero-context: the router description is always visible.

## How it works

`jevshelf search` ranks a configured collection lexically or with Jev and returns metadata and SHA-256 digests only; `jevshelf load --expected-digest` then reads the selected skill, rejecting stale selections. Jev integration: [`src/jevshelf/cli.py`](https://github.com/ham-zax/jevshelf/blob/3fb8b9a35048150ffb9cbb6985e6944107d78e13/src/jevshelf/cli.py). (Summarized from the upstream README and source at the pinned commit; not reproduced here.)

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ham-zax/jevshelf.git
cd jevshelf
bash scripts/bootstrap.sh
./bin/jevshelf init
./bin/jevshelf search --collection writing --mode lexical --task "summarize meeting notes"
```

## Limits and data handling

In Jev mode, task text, skill metadata and bounded excerpts go to TypeSafe. The optional backup script pushes to a private Git repo you configure. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 3fb8b9a35048](https://github.com/ham-zax/jevshelf/tree/3fb8b9a35048150ffb9cbb6985e6944107d78e13). Inspected the upstream README, LICENSE, and the Jev integration file linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
