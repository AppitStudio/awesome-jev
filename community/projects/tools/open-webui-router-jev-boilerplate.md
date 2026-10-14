# Open WebUI Router (Jev boilerplate)

[All projects](../README.md) · [SDKs and integrations](README.md#sdks-and-integrations)

Single-file Open WebUI router pipe that asks Jev which specialist model should answer, with sticky follow-ups, prefix overrides and a clarification fallback.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/foteev/open-webui-router-jev-boilerplate) |
| Maintainer | [foteev](https://github.com/foteev). Independently curated. |
| Format | Open WebUI pipe function (Python) |
| Requirements | Open WebUI admin access, TypeSafe API key. |
| License | [MIT](https://github.com/foteev/open-webui-router-jev-boilerplate/blob/d963d36c95d9162599762020f5b61675fc0c4ef5/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`src/route.py`](https://github.com/foteev/open-webui-router-jev-boilerplate/blob/d963d36c95d9162599762020f5b61675fc0c4ef5/src/route.py) at the pinned commit. |

## When to use

- Expose one 'front door' model in Open WebUI that dispatches to specialist models.
- Mismatch: boilerplate; adapt the agent list to your instance.

## How it works

Jev answers a Choice (`agent`) and a Noul (`follow_up`); code filters models by caller permissions, honors `/code`-style overrides, and asks a numbered clarification when confidence is low. Integration evidence: [`src/route.py`](https://github.com/foteev/open-webui-router-jev-boilerplate/blob/d963d36c95d9162599762020f5b61675fc0c4ef5/src/route.py).

## Get started

From the upstream README (not run on the review host):

```sh
# paste dist/router_pipe.py into Open WebUI Admin → Functions
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- Deployable file: `dist/router_pipe.py`.
- Evals: `eval/`; agent manual: `AGENTS.md`.

## Limits and data handling

User prompts go to TypeSafe for routing, then to the chosen specialist.

## Review and maintenance

Reviewed **2026-10-14** (Europe/Sofia) at [commit d963d36c95d9](https://github.com/foteev/open-webui-router-jev-boilerplate/tree/d963d36c95d9162599762020f5b61675fc0c4ef5). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
