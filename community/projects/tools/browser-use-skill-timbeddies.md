# browser-use skill by timbeddies (Claude Code skill that splits browser work between Claude, Jev and code)

[All projects](../README.md) · [Browser and computer use](README.md#browser-and-computer-use)

Claude Code skill that routes browser work by decision type: Claude plans and judges screenshots, Jev navigates pages through jev-browser and answers many small typed questions via the TypeSafe API, and code (playwright-cli, axe-core, Lighthouse) gives every verdict that must be reproducible.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/timbeddies/browser-use-skill) |
| Maintainer | [timbeddies](https://github.com/timbeddies). Independently curated. |
| Format | Claude Code skill with Python and shell scripts (MIT) |
| Requirements | Claude Code, Node.js (`npx`), Python 3, a TypeSafe key, and optionally `ANTHROPIC_API_KEY` for typing into forms. |
| License | [MIT](https://github.com/timbeddies/browser-use-skill/blob/c78ae40330c9d36fb019acd1924554ebbd4ba378/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`scripts/jev_ask.py`](https://github.com/timbeddies/browser-use-skill/blob/c78ae40330c9d36fb019acd1924554ebbd4ba378/scripts/jev_ask.py) at the pinned commit. |

## When to use

- Run post-deploy UI checks, form smoke tests or broken-link crawls cheaply.
- Mismatch: Claude Code only; reproducible verdicts come from code, not Jev.

## How it works

`scripts/jev_ask.py` posts typed questions to `https://api.typesafe.ai/v1/systemone` with the model pinned to `jev-1.14.0`; `scripts/jev-run.sh` drives jev-browser navigation. Integration evidence: [`scripts/jev_ask.py`](https://github.com/timbeddies/browser-use-skill/blob/c78ae40330c9d36fb019acd1924554ebbd4ba378/scripts/jev_ask.py).

## Get started

Clone the skill into your Claude Code skills folder and set your TypeSafe key.

```sh
git clone https://github.com/timbeddies/browser-use-skill ~/.claude/skills/browser-use
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/timbeddies/browser-use-skill/blob/c78ae40330c9d36fb019acd1924554ebbd4ba378/README.md](https://github.com/timbeddies/browser-use-skill/blob/c78ae40330c9d36fb019acd1924554ebbd4ba378/README.md)

## Limits and data handling

Page content and screenshots go to TypeSafe and Anthropic on your keys.

## Review and maintenance

Reviewed **2026-11-12** (Europe/Sofia) at [commit c78ae40330c9](https://github.com/timbeddies/browser-use-skill/tree/c78ae40330c9d36fb019acd1924554ebbd4ba378). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
