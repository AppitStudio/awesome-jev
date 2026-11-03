# DecideOnce (MCP server that records an agent's repeated decisions and lets confident ones skip the LLM call, with hosted Jev as the first decider)

[All projects](../README.md) · [Developer tools](README.md#developer-tools)

MCP server that finds decision and categorisation steps in agent workflows, records each decision with its inputs, choice and outcome, and then lets confident decisions skip the LLM call. Once a decision point reaches shadow mode it routes through hosted Jev (System One over OpenRouter or TypeSafe) with a temperature and threshold fitted from the first 200 labelled calls and a monthly budget; a private model is trained only when the report recommends it.

| At a glance | Details |
| --- | --- |
| Source | [Source](https://github.com/jcsancho/decideonce) |
| Maintainer | [jcsancho](https://github.com/jcsancho). Independently curated. |
| Format | Python MCP server and local gateway (uv) |
| Requirements | Python and uv; for the hosted tier a Jev key supplied at runtime and a `hosted_jev.monthly_budget_usd`; `backend = "tiered"` in `decideonce.toml`. |
| License | [MIT](https://github.com/jcsancho/decideonce/blob/ddc82a5e0ce8a490fa1130dc3e33d6334cf0a81a/LICENSE) |
| Disclosure | AI-assisted catalog review; no affiliation with the maintainer. Listing is not an endorsement. Install and live calls not run on the review host. |
| Jev evidence | [`decideonce/deciders/hosted.py`](https://github.com/jcsancho/decideonce/blob/ddc82a5e0ce8a490fa1130dc3e33d6334cf0a81a/decideonce/deciders/hosted.py) at the pinned commit. |

## When to use

- Turn repeated classification steps in an agent's skills into cheap, measured decisions with a budget.
- Mismatch: the default install uses the local legacy decider, where promotion needs a trained probe instead of the hosted Jev tier.

## How it works

`decideonce/deciders/hosted.py` calls the System One endpoint (allowed hosts `openrouter.ai` and `api.typesafe.ai`) after rules and before the threshold check, counts every call against the budget and keeps the key only in server memory. Integration evidence: [`decideonce/deciders/hosted.py`](https://github.com/jcsancho/decideonce/blob/ddc82a5e0ce8a490fa1130dc3e33d6334cf0a81a/decideonce/deciders/hosted.py).

## Get started

From the upstream README (not run on the review host):

```sh
git clone https://github.com/jcsancho/decideonce.git
cd decideonce
uv sync
uv run decideonce-gateway   # 127.0.0.1:8787
```

Live commands may contact TypeSafe (or the configured provider) and incur charges. These commands were not run on the review host.

## Examples and demos

- README with the tool flow and the hosted tier: [github.com/jcsancho/decideonce#readme](https://github.com/jcsancho/decideonce#readme)

## Limits and data handling

Decision context goes to hosted Jev on your key and counts against your budget; the project's own claims about savings are not independently measured. Independent project; not affiliated with TypeSafe.

## Review and maintenance

Reviewed **2026-11-03** (Europe/Sofia) at [commit ddc82a5e0ce8](https://github.com/jcsancho/decideonce/tree/ddc82a5e0ce8a490fa1130dc3e33d6334cf0a81a). Inspected the upstream README, license status, and the Jev integration file linked above; install and live inference were not run on the review host. Catalog checks (`npm run check`) ran locally; they verify navigation, not project claims. AI-assisted review.
