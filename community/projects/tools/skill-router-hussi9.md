# skill-router by hussi9 (Claude Code hook router that picks the installed skill for each prompt, with Jev choosing over the whole skill index)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hook-driven router for Claude Code that indexes every skill you have installed by when it applies, then injects a short route card before Claude's first action naming the domain skill, the process skill, gates and memory to use. Jev is the model on the hot path: in one call it chooses the skill over the whole index, and it can also pick a light, standard or heavy tier so sub-agents run on a cheaper model. It routes only when Jev is at least 80% confident; otherwise it is silent. Without a key, or if the call is slow, it falls back to local ranking.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/hussi9/skill-router) |
| Maintainer | [hussi9](https://github.com/hussi9). Independently curated. |
| Format | Claude Code skill with hooks (Python scripts, local dashboard) |
| Requirements | Claude Code and Python 3; optionally a `TYPESAFE_API_KEY` for Jev and a small-model key for the tie-break stage. |
| License | [MIT](https://github.com/hussi9/skill-router/blob/2fbf29097a9a3537f5fc6b6431b81b5a6ec06c3e/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. Discovered via X ([post](https://x.com/hussi9/status/2117816546307592525)). |
| Jev evidence | [`scripts/jev_choose.py`](https://github.com/hussi9/skill-router/blob/2fbf29097a9a3537f5fc6b6431b81b5a6ec06c3e/scripts/jev_choose.py) at the pinned commit. |

## When to use

- Stop installed skills from going unused: have a decision model pick the relevant skill and working method for each prompt.
- Mismatch: the author's accuracy numbers (32 of 34 routed prompts right at the 0.8 gate) come from one personal skill set, and routing is tuned to the pinned model version.

## How it works

`scripts/jev_choose.py` posts the prompt and the skill index to `https://api.typesafe.ai/v1/systemone` (`jev-1.13.0`) as Choice questions for the domain skill, process skill, path and tier; answers are mapped back to skills the router already knows, and the router falls back to local ranking on error or after a 1.2 s timeout. Integration evidence: [`scripts/jev_choose.py`](https://github.com/hussi9/skill-router/blob/2fbf29097a9a3537f5fc6b6431b81b5a6ec06c3e/scripts/jev_choose.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/hussi9/skill-router ~/devpro/skill-router
ln -s ~/devpro/skill-router ~/.claude/skills/skill-router
python3 ~/.claude/skills/skill-router/scripts/install_hooks.py
export TYPESAFE_API_KEY=...   # optional, enables Jev
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the routing pipeline, tiers and dashboard: [github.com/hussi9/skill-router#readme](https://github.com/hussi9/skill-router#readme)
- Jev data flow and the measured 0.8 gate: [github.com/hussi9/skill-router/blob/2fbf29097a9a3537f5fc6b6431b81b5a6ec06c3e/docs/jev.md](https://github.com/hussi9/skill-router/blob/2fbf29097a9a3537f5fc6b6431b81b5a6ec06c3e/docs/jev.md)

## Limits and data handling

With a key set, each uncached prompt and the skill summaries go to TypeSafe on your key (the README estimates about $0.0005 per prompt); nothing is sent without a key. The installer wires six hooks into `~/.claude/settings.json`, and accuracy figures are the author's own, in-sample measurements. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-04** (Europe/Sofia) at [commit 2fbf29097a9a](https://github.com/hussi9/skill-router/tree/2fbf29097a9a3537f5fc6b6431b81b5a6ec06c3e). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
