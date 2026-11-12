# hermes-advisor (advisor strategy for Hermes Agent with an optional Jev gate that decides when to consult a stronger model)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

Hermes Agent plugin that keeps conversations on a cheap executor model and brings in a stronger advisor (Opus by default) only on hard turns, without switching the main model so the prompt cache stays warm; an optional Jev yes/no gate scores each user message to nudge or auto-fetch advice.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/superlowburn/hermes-advisor) |
| Maintainer | [superlowburn](https://github.com/superlowburn). Independently curated. |
| Format | Hermes Agent plugin (Python, MIT) |
| Requirements | Hermes Agent, an advisor model on your configured provider, and optionally `TYPESAFE_API_KEY` for the Jev gate. |
| License | [MIT](https://github.com/superlowburn/hermes-advisor/blob/fe869e133032e553e3e0a42db069833a3b9bbbcc/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`core.py`](https://github.com/superlowburn/hermes-advisor/blob/fe869e133032e553e3e0a42db069833a3b9bbbcc/core.py) at the pinned commit. |

## When to use

- Run Hermes mostly on a cheap model and escalate only the turns that need careful judgment.
- Mismatch: if you want the whole conversation moved to a stronger model; this keeps the executor in charge.

## How it works

`core.py` defines one Jev `noul` question (`needs_advisor`) sent to `https://api.typesafe.ai/v1/systemone`; above the configured threshold (0.7 by default) the plugin either nudges the executor to call the advisor tool (`nudge`) or fetches the advice first and injects it (`auto`). The gate fails open: no key, timeout or API error means no escalation. Integration evidence: [`core.py`](https://github.com/superlowburn/hermes-advisor/blob/fe869e133032e553e3e0a42db069833a3b9bbbcc/core.py).

## Get started

Install and enable the plugin in Hermes, then optionally set your TypeSafe key for automatic escalation.

```sh
hermes plugins install https://github.com/superlowburn/hermes-advisor --enable
hermes config set TYPESAFE_API_KEY <key>
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README: [github.com/superlowburn/hermes-advisor/blob/fe869e133032e553e3e0a42db069833a3b9bbbcc/README.md](https://github.com/superlowburn/hermes-advisor/blob/fe869e133032e553e3e0a42db069833a3b9bbbcc/README.md)
- Plugin manifest: [github.com/superlowburn/hermes-advisor/blob/fe869e133032e553e3e0a42db069833a3b9bbbcc/plugin.yaml](https://github.com/superlowburn/hermes-advisor/blob/fe869e133032e553e3e0a42db069833a3b9bbbcc/plugin.yaml)

## Limits and data handling

With the gate on, each user message (above a minimum length) goes to TypeSafe for one yes/no score; transcripts go to the advisor model's provider when advice is requested.

## Review and maintenance

Reviewed **2026-11-13** (Europe/Sofia) at [commit fe869e133032](https://github.com/superlowburn/hermes-advisor/tree/fe869e133032e553e3e0a42db069833a3b9bbbcc). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
