# Laya for Home Assistant

[All projects](../README.md) · [Home automation](README.md#home-automation)

Fully local Home Assistant Assist conversation agent using open-weight Laya (sibling architecture to TypeSafe Jev HA; independent of hosted Jev).

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/allenporter/home-assistant-laya) |
| Maintainer | [allenporter](https://github.com/allenporter). Independently curated. |
| Format | Home Assistant custom conversation agent (local Laya). |
| Requirements | Home Assistant; local Laya weights/runtime (CPU/CUDA/MPS); optional generative LLM fallback for escalation. |
| License | [Apache-2.0](https://github.com/allenporter/home-assistant-laya/blob/8a4c98a2e1fc8cc724412c9a7ce83475924fe24e/LICENSE). Independent open-weight / self-hosted path—not TypeSafe-hosted Jev. |
| Disclosure | Independent of hosted TypeSafe Jev. AI-assisted catalog review; no affiliation. Listing is not an endorsement. Live TypeSafe/provider paths not run on the review host. Sibling architecture to allenporter/home-assistant-jev (hosted Jev); this listing is local Laya. |

## When to use

Use for **local Assist** device control with open System One weights and no cloud Jev key. Prefer TypeSafe-hosted HA integrations when you want official cloud Jev.

## How it works

Five-stage speculative pipeline scores intents/areas/entities with local Laya in one forward pass; high-confidence paths dispatch HA intents, else escalate to a configured LLM. Independent of hosted TypeSafe Jev.

## Get started

```sh
git clone https://github.com/allenporter/home-assistant-laya.git
cd home-assistant-laya
git checkout 8a4c98a2e1fc8cc724412c9a7ce83475924fe24e
# Install as HA custom component per README; local Laya — not hosted TypeSafe Jev
```

## Examples and demos

- Upstream README quickstart and examples at the pinned commit.
- Separate interactive demos only where the upstream README links them; none were executed on the review host.

## Limits and data handling

Live Jev/TypeSafe (or other provider) calls send the judged text/state to that provider and may incur charges. Offline/demo paths stay local when documented upstream. Catalog checks did not run live integrations.

## Review and maintenance

Reviewed **2026-09-26** (Europe/Sofia) at [commit 8a4c98a](https://github.com/allenporter/home-assistant-laya/tree/8a4c98a2e1fc8cc724412c9a7ce83475924fe24e). AI-assisted README and license inspection; install/live paths not executed.
