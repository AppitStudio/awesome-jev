# fable-harness (Claude Code harness that gives each model one job, with Jev routing prompts and deciding when a run is done)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Drop-in Claude Code setup with seats for an advisor and orchestrator (Fable 5.2), builder and verifier (Opus 5.5) and scout (Haiku 5.5); two Jev hooks do the gating: a route gate classifies each prompt as lookup, build, hard or big before Claude sees it, and a done gate checks whether the output proves every line of `GOAL.md` before a long run may stop.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/seanGSISG/fable-harness) |
| Maintainer | [seanGSISG](https://github.com/seanGSISG). Independently curated. |
| Format | Claude Code hooks, agents and installer (Python with uv, MIT) |
| Requirements | uv, Claude Code with access to the named models, and a TypeSafe key (`TYPESAFE_API_KEY`). |
| License | [MIT](https://github.com/seanGSISG/fable-harness/blob/71646cf1612b28eeb5d3a1e908160850349c5c72/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`template/.claude/hooks/jev_route.py`](https://github.com/seanGSISG/fable-harness/blob/71646cf1612b28eeb5d3a1e908160850349c5c72/template/.claude/hooks/jev_route.py) at the pinned commit. |

## When to use

- Keep expensive models on hard work and stop long Claude Code runs only when the goal is proven.
- Mismatch: if you do not use Claude Code or cannot use the named models.

## How it works

`template/.claude/hooks/jev_route.py` (UserPromptSubmit) and `jev_done.py` (Stop) call `https://api.typesafe.ai` directly with the SDK default `jev-latest` (`jev-1.14.0` on 2026-11-13 per `docs/usage.md`). Below 90% route confidence the prompt goes to the advisor; the done gate gives up after 5 tries and leaves a `REVIEW.md` when Jev is unsure. Integration evidence: [`template/.claude/hooks/jev_route.py`](https://github.com/seanGSISG/fable-harness/blob/71646cf1612b28eeb5d3a1e908160850349c5c72/template/.claude/hooks/jev_route.py).

## Get started

Clone, install into your repository and export your TypeSafe key.

```sh
git clone https://github.com/seanGSISG/fable-harness && cd fable-harness
uv run install.py /path/to/your/repo
export TYPESAFE_API_KEY=...
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/seanGSISG/fable-harness/blob/71646cf1612b28eeb5d3a1e908160850349c5c72/README.md](https://github.com/seanGSISG/fable-harness/blob/71646cf1612b28eeb5d3a1e908160850349c5c72/README.md)
- Usage notes: [github.com/seanGSISG/fable-harness/blob/71646cf1612b28eeb5d3a1e908160850349c5c72/docs/usage.md](https://github.com/seanGSISG/fable-harness/blob/71646cf1612b28eeb5d3a1e908160850349c5c72/docs/usage.md)

## Limits and data handling

Each prompt and, during long runs, check output and `GOAL.md` go to TypeSafe on your key; Claude traffic goes to Anthropic.

## Review and maintenance

Reviewed **2026-11-14** (Europe/Sofia) at [commit 71646cf1612b](https://github.com/seanGSISG/fable-harness/tree/71646cf1612b28eeb5d3a1e908160850349c5c72). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
