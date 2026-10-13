# jev-model-router (m-esm)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code plugin/hook: TypeSafe Jev scores each redacted prompt (trivial → frontier) and whether it is a follow-up, then runs the turn on the model and effort it deserves. Distinct from the separately listed [jev-model-router](jev-model-router.md) mod.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/m-esm/jev-model-router) |
| Maintainer | [m-esm](https://github.com/m-esm). Independently curated. |
| Format | Claude Code plugin (Python hook) |
| Requirements | Claude Code; Python; TypeSafe key. |
| License | [MIT](https://github.com/m-esm/jev-model-router/blob/550e08a8f2a5f09969732e34e3e8ced9677233a2/LICENSE) |
| Jev evidence | [`jev_router.py`](https://github.com/m-esm/jev-model-router/blob/550e08a8f2a5f09969732e34e3e8ced9677233a2/jev_router.py) at the pinned commit. |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Route easy prompts to cheaper models and hard ones to stronger models in Claude Code.
- Mismatch: see [jev-model-router](jev-model-router.md) and [claude-router (alexei-led)](alexei-led-claude-router.md) for other approaches.

## How it works

On `prompt.submit` the redacted prompt goes to Jev with a four-level score and a follow-up noul; the hook maps the result to model and effort. (Summarized from the upstream [README](https://github.com/m-esm/jev-model-router/blob/550e08a8f2a5f09969732e34e3e8ced9677233a2/README.md); not reproduced here.)

## Get started

From the upstream README (not run on the review host): install the plugin per the README and set your key.

## Limits and data handling

Redacted prompts go to TypeSafe. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-13** (Europe/Sofia) at [commit 550e08a8f2a5](https://github.com/m-esm/jev-model-router/tree/550e08a8f2a5f09969732e34e3e8ced9677233a2). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
