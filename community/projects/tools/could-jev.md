# could-jev

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude skill that gives a ten-line gut-check on whether TypeSafe Jev could help with what you are building: verdict, matching pattern from 31 tagged Jev patterns, a state/questions sketch, closest prior, pitfalls and the cheapest test; it does not call Jev itself.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/rlfordon/could-jev) |
| Maintainer | [rlfordon](https://github.com/rlfordon). Independently curated. |
| Format | Claude skill (`SKILL.md` + pattern and capability notes) |
| Requirements | Claude with skills support. No Jev key needed. |
| License | [MIT](https://github.com/rlfordon/could-jev/blob/1018c6d8214696d2cfa343a118ef08d07b73014a/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Decide quickly if a feature should use Jev before prototyping.
- Mismatch: design advice only; capability notes can go stale.

## How it works

See the upstream [README](https://github.com/rlfordon/could-jev/blob/1018c6d8214696d2cfa343a118ef08d07b73014a/README.md) at the pinned commit for architecture and the Jev integration.

## Get started

From the README:

```sh
git clone https://github.com/rlfordon/could-jev.git ~/.claude/skills/could-jev
```

## Limits and data handling

Runs inside Claude; optional local history file `~/.claude/could-jev/history.md`. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-09** (Europe/Sofia) at [commit 1018c6d82146](https://github.com/rlfordon/could-jev/tree/1018c6d8214696d2cfa343a118ef08d07b73014a). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
