# creator-teardown

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Claude Code / Cowork skill that analyzes a creator's recent posts, labels posts and sentences with TypeSafe Jev, and produces a playbook plus rebuilt drafts for your brand (local first-use wizard; no baked-in identity).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/ai-orchestrators/creator-teardown) |
| Maintainer | [ai-orchestrators](https://github.com/ai-orchestrators). Independently curated. |
| Format | Python · Claude Code / Cowork skill |
| Requirements | Claude Code or Cowork; TypeSafe/OpenRouter credentials per skill setup. |
| License | [MIT](https://github.com/ai-orchestrators/creator-teardown/blob/5fd0ec871f4127b555cf3ce536df86174ed9d460/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live Jev calls not run on the review host. |

## When to use

- Competitive creative teardown with typed labels instead of freeform notes.
- Mismatch: Needs access to the creator's public posts via your tooling.

## How it works

Decision schemas under `decisions/` drive Jev labeling; scripts assemble the report. Evidence: [`scripts/jev_client.py`](https://github.com/ai-orchestrators/creator-teardown/blob/5fd0ec871f4127b555cf3ce536df86174ed9d460/scripts/jev_client.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/ai-orchestrators/creator-teardown.git
# install skill + run first-use wizard per README
```

## Limits and data handling

Provider-bound inputs may be billed by TypeSafe/OpenRouter when live. Not run on the review host.

## Review and maintenance

Reviewed **2026-10-12** (Europe/Sofia) at [commit 5fd0ec871f41](https://github.com/ai-orchestrators/creator-teardown/tree/5fd0ec871f4127b555cf3ce536df86174ed9d460). Inspected the upstream README, LICENSE, and the Jev integration evidence linked above; install and live Jev calls were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
