# claude-model-guard

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code hooks plus a CLI picker where TypeSafe Jev chooses the model tier (Haiku, Sonnet, Opus or a long-form tier) for every prompt and can block a prompt sent to the wrong model when it confidently disagrees; tier criteria are editable and there are no dependencies beyond Node's `fetch`.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/mcowdery/claude-model-guard) |
| Maintainer | [mcowdery](https://github.com/mcowdery). Independently curated. |
| Format | Node scripts copied into your project and registered as Claude Code hooks; `npm run model:pick` CLI |
| Requirements | Node.js 18+, a Claude Code project with `.claude/`, and a `TYPESAFE_API_KEY` in `.env.jev`. |
| License | [MIT](https://github.com/mcowdery/claude-model-guard/blob/b49513ea343fc448f56ed678f673ddf876bd2357/LICENSE). External project keeps its own license. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live inference not run on the review host. |

## When to use

- Stop Opus-sized tasks running on Haiku (or the reverse) without deciding by hand each time.
- Pick a tier before starting a session with `model:pick --launch`.
- Mismatch: blocking is on by default when Jev is confident; edit `jev.config.json` tiers to fit your codebase.

## How it works

[`promptAdvisor.mjs`](https://github.com/mcowdery/claude-model-guard/blob/b49513ea343fc448f56ed678f673ddf876bd2357/scripts/promptAdvisor.mjs) runs on `UserPromptSubmit`, asks Jev via [`jev.mjs`](https://github.com/mcowdery/claude-model-guard/blob/b49513ea343fc448f56ed678f673ddf876bd2357/scripts/jev.mjs) which tier fits, and compares it with the model recorded by [`recordModelSwitch.mjs`](https://github.com/mcowdery/claude-model-guard/blob/b49513ea343fc448f56ed678f673ddf876bd2357/scripts/recordModelSwitch.mjs); a confident mismatch blocks the prompt, a close call only adds a note.

## Get started

Copy the scripts and add your key (README *Install*), then register the three hooks in `.claude/settings.local.json`:

```sh
git clone https://github.com/mcowdery/claude-model-guard.git
cp -r claude-model-guard/scripts your-project/scripts/model-guard
cp claude-model-guard/.env.jev.example your-project/.env.jev   # set TYPESAFE_API_KEY
```

Every submitted prompt triggers one Jev request billed to your TypeSafe key.

## Examples and demos

- README *Using the CLI picker* (`npm run model:pick -- "fix the off-by-one…"`).
- Tier criteria: [`jev.config.example.json`](https://github.com/mcowdery/claude-model-guard/blob/b49513ea343fc448f56ed678f673ddf876bd2357/jev.config.example.json).

## Limits and data handling

The text of each prompt goes to TypeSafe. Upstream notes Jev access was early access/waitlist at time of writing. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-08** (Europe/Sofia) at [commit b49513ea343f](https://github.com/mcowdery/claude-model-guard/tree/b49513ea343fc448f56ed678f673ddf876bd2357). Inspected the upstream README, LICENSE, and the Jev integration described there; install and live inference were not run on the review host. Catalog checks (`npm run lint`, `check:links`, `check:community`) ran locally; they verify navigation, not project claims. AI-assisted review.
