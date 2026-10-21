# content-evals (agent skill)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Agent skill that breaks a content requirement into atomic yes/no questions, builds a YAML scoring profile, scores a document with Jev and turns low scores into concrete edits.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/Automatify-Pty-Ltd/content-skills) |
| Maintainer | [Automatify-Pty-Ltd](https://github.com/Automatify-Pty-Ltd). Independently curated. |
| Format | Agent skill (`SKILL.md` plus a Python script) |
| Requirements | An Agent Skills client (Pi, Claude Code, VS Code Copilot); uv and Python 3.9+; `TYPESAFE_API_KEY`. |
| License | [MIT](https://github.com/Automatify-Pty-Ltd/content-skills/blob/af1897c857afc12aebf83c68ec61361839eb6947/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`skills/content-evals/scripts/score.py`](https://github.com/Automatify-Pty-Ltd/content-skills/blob/af1897c857afc12aebf83c68ec61361839eb6947/skills/content-evals/scripts/score.py) at the pinned commit. |

## When to use

- Score drafts for clarity or other rubric items before publishing.
- Give a coding agent a repeatable content check with numeric bands.
- Mismatch: scoring only; it does not write the content for you.

## How it works

`score.py` reads the profile's questions and sends the document with them to `https://api.typesafe.ai/v1/systemone`; the skill then interprets the bands and proposes edits. Integration evidence: [`skills/content-evals/scripts/score.py`](https://github.com/Automatify-Pty-Ltd/content-skills/blob/af1897c857afc12aebf83c68ec61361839eb6947/skills/content-evals/scripts/score.py).

## Get started

From the upstream README (not run on the review host):

```sh
cp -r skills/content-evals ~/.agents/skills/
export TYPESAFE_API_KEY=your-key
cd skills/content-evals && uv run scripts/score.py --input article.md --config profiles/clarity.yaml --pretty
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Smoke test with three sample documents in the README: [github.com/Automatify-Pty-Ltd/content-skills#readme](https://github.com/Automatify-Pty-Ltd/content-skills#readme)

## Limits and data handling

Documents are sent to TypeSafe for scoring.

## Review and maintenance

Reviewed **2026-10-21** (Europe/Sofia) at [commit af1897c857af](https://github.com/Automatify-Pty-Ltd/content-skills/tree/af1897c857afc12aebf83c68ec61361839eb6947). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
